"""
Training of Neural Network based Segmentation (U-Net excluded)
==============================================================

This module provides tools and functionalities to train and evaluate deep learning
models for chromatophore segmentation of cephalopod images.
It includes methods for data preparation, model selection, training, loss computation,
evaluation metrics, and visualization of results.

Features:
    - **Data Preparation:** 
        - Read images and masks from specified directories.
        - Crop images into windows for training.
        - Map color-coded masks to class indices.
    - **Custom Dataset and DataLoader:**
        - Define a PyTorch Dataset for cephalopod images.
        - Create DataLoaders with optional data augmentation using Albumentations.
    - **Model Selection:**
        - Support for various segmentation architectures (e.g., FCN, DeepLabV3)
          with options for pretrained weights and custom classifier configurations.
    - **Loss Functions and Metrics:**
        - Combined loss function blending Cross Entropy Loss and Dice Loss.
        - Functions to compute evaluation metrics including accuracy, IoU, and Dice coefficient.
    - **Training Loop:**
        - Comprehensive training loop with periodic validation.
        - Learning rate scheduling and best model checkpointing.
    - **Visualization:**
        - Plot training and validation metrics over epochs.
        - Display image grids with original, ground truth, and predicted masks.
        - Visualize augmentation effects on images and masks.

Possible Usage:
    To train a segmentation model, call the `train` function with the appropriate
    parameters. For example:

        >>> train(input_dir='/path/to/dataset', nr_epochs=500, architecture='fcn_resnet50')
"""


from pathlib import Path
import click
from matplotlib.colors import ListedColormap
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import albumentations as A
from albumentations.pytorch import ToTensorV2
import copy
import torch.nn.functional as F
import os
from datetime import datetime
from skimage.segmentation import mark_boundaries
from ..utils.decorators import error_handler


CMAP_4CLASSES = ListedColormap([[1, 1, 1], [255/255, 200/255, 0], [255/255, 127/255, 0], [65/255, 35/255, 0]])
CMAP_2CLASSES = ListedColormap([[1, 1, 1], [65/255, 35/255, 0]])
WINDOW_SIZE = 512
BATCH_SIZE = 7


def calculate_metrics(output, target, num_classes):
    """
    Calculate evaluation metrics including overall accuracy, mean IoU, and mean Dice coefficient.

    Args:
        output (torch.Tensor): The raw output logits from the model.
        target (torch.Tensor): The ground truth segmentation masks.
        num_classes (int): Number of segmentation classes.

    Returns:
        tuple: A tuple containing:
            - accuracy (float): Overall pixel accuracy.
            - mean_iou (float): Mean Intersection over Union score.
            - mean_dice (float): Mean Dice coefficient.
    """
    _, predicted = torch.max(output, 1)

    # Compute per-class Dice and IoU
    dice = dice_coef(predicted, target, num_classes)
    iou = jaccard_index(predicted, target, num_classes)

    # Flatten for overall accuracy
    predicted = predicted.view(-1)
    target = target.view(-1)
    accuracy = torch.mean((predicted == target).float())

    # Calculate mean Dice and IoU, ignoring NaN values
    mean_dice = np.nanmean(dice)
    mean_iou = np.nanmean(iou)

    return accuracy.item(), mean_iou, mean_dice


def jaccard_index(predicted, target, num_classes):
    """
    Compute the Jaccard Index (Intersection over Union) for each class.

    Args:
        predicted (torch.Tensor): Predicted segmentation mask.
        target (torch.Tensor): Ground truth segmentation mask.
        num_classes (int): Number of segmentation classes.

    Returns:
        list: A list of IoU scores for each class. Returns NaN for a class if there is no ground truth.
    """
    iou = []
    for cls in range(num_classes):
        # Compute intersection and union
        intersection = torch.logical_and(target == cls, predicted == cls).sum().float()
        union = torch.logical_or(target == cls, predicted == cls).sum().float()
        if union.item() == 0:
            iou.append(float('nan'))  # If there is no ground truth, do not include in evaluation
        else:
            # Compute IoU and convert to float
            iou_score = (intersection / union).item()
            iou.append(iou_score)
    return iou


def dice_coef(predicted, target, num_classes, smooth=1e-6):
    """
    Compute the Dice coefficient for each class.

    Args:
        predicted (torch.Tensor): Predicted segmentation mask.
        target (torch.Tensor): Ground truth segmentation mask.
        num_classes (int): Number of segmentation classes.
        smooth (float, optional): Smoothing factor to avoid division by zero. Defaults to 1e-6.

    Returns:
        list: A list of Dice coefficients for each class.
    """
    dice = []
    for cls in range(num_classes):
        pred_cls = (predicted == cls).float()
        target_cls = (target == cls).float()
        intersection = (pred_cls * target_cls).sum()
        union = pred_cls.sum() + target_cls.sum()
        dice_cls = (2. * intersection + smooth) / (union + smooth)
        dice.append(dice_cls.item())
    return dice


def dice_loss(pred, target, smooth=1e-6):
    """
    Compute the average Dice loss across all classes.

    Args:
        pred (torch.Tensor): Predicted probabilities (after softmax) with shape (N, C, H, W).
        target (torch.Tensor): One-hot encoded ground truth masks with shape (N, C, H, W).
        smooth (float, optional): Smoothing factor to avoid division by zero. Defaults to 1e-6.

    Returns:
        torch.Tensor: Average Dice loss computed over all classes.
    """
    num_classes = pred.shape[1]
    dice_loss = 0
    for i in range(num_classes):
        pred_flat = pred[:, i, :, :].contiguous().view(-1)
        target_flat = target[:, i, :, :].contiguous().view(-1)
        intersection = (pred_flat * target_flat).sum()
        union = pred_flat.sum() + target_flat.sum()
        dice_loss += 1 - (2. * intersection + smooth) / (union + smooth)
    return dice_loss / num_classes


class CombinedLoss(nn.Module):
    """
    Combined loss function that blends Cross Entropy Loss and Dice Loss.

    Attributes:
        alpha (float): Weighting factor between Cross Entropy Loss and Dice Loss.
        cross_entropy (nn.Module): Instance of CrossEntropyLoss.
    """

    def __init__(self, alpha=0.5):
        """
        Initialize the CombinedLoss module.

        Args:
            alpha (float, optional): Weighting factor between Cross Entropy and Dice losses. Defaults to 0.5.
        """
        super(CombinedLoss, self).__init__()
        self.cross_entropy = nn.CrossEntropyLoss()  # CrossEntropyLoss
        self.alpha = alpha  # Weighting factor for CrossEntropy vs Dice Loss

    def forward(self, pred, target):
        """
        Compute the combined loss given predictions and targets.

        Args:
            pred (torch.Tensor): Raw logits from the model.
            target (torch.Tensor): Ground truth segmentation masks.

        Returns:
            torch.Tensor: Computed combined loss value.
        """
        # Cross-Entropy Loss
        # print(f'{pred.shape=}, {target.shape=}')
        ce_loss = self.cross_entropy(pred, target)
        
        # Dice Loss (convert predicted logits to probabilities using softmax for multi-class)
        dice = dice_loss(F.softmax(pred, dim=1), F.one_hot(target, num_classes=pred.shape[1]).permute(0, 3, 1, 2).float())
        
        # Combine losses with a weighting factor alpha
        return self.alpha * ce_loss + (1 - self.alpha) * dice


def plot_and_save_metrics(train_losses, train_accuracies, train_ious, train_dices, val_losses, val_accuracies, val_ious, val_dices, output_dir="plots",
                          val_every_n_epochs=5):
    """
    Plot and save training and validation metrics.

    Args:
        train_losses (list): List of training loss values.
        train_accuracies (list): List of training accuracy values.
        train_ious (list): List of training IoU values.
        train_dices (list): List of training Dice coefficient values.
        val_losses (list): List of validation loss values.
        val_accuracies (list): List of validation accuracy values.
        val_ious (list): List of validation IoU values.
        val_dices (list): List of validation Dice coefficient values.
        output_dir (str, optional): Directory to save the plot. Defaults to "plots".
        val_every_n_epochs (int, optional): Frequency of validation epochs. Defaults to 5.

    Returns:
        None
    """
    os.makedirs(output_dir, exist_ok=True)

    fig, axs = plt.subplots(2, 2, figsize=(15, 8))  # 2 rows, 2 columns of subplots

    axs[0, 0].plot(range(1, len(train_losses) + 1), train_losses, label="Training Loss")
    axs[0, 0].plot(range(val_every_n_epochs, val_every_n_epochs * len(val_losses) + 1, val_every_n_epochs), val_losses, label="Validation Loss")
    axs[0, 0].set_title("Loss")
    axs[0, 0].set_xlabel("Epoch")
    axs[0, 0].set_ylabel("Loss")
    axs[0, 0].legend()
    axs[0, 0].grid(True)

    axs[0, 1].plot(range(1, len(train_losses) + 1), train_accuracies, label="Training Accuracy")
    axs[0, 1].plot(range(val_every_n_epochs, val_every_n_epochs * len(val_losses) + 1, val_every_n_epochs), val_accuracies, label="Validation Accuracy")
    axs[0, 1].set_title("Accuracy")
    axs[0, 1].set_xlabel("Epoch")
    axs[0, 1].set_ylabel("Accuracy")
    axs[0, 1].legend()
    axs[0, 1].grid(True)

    axs[1, 0].plot(range(1, len(train_losses) + 1), train_ious, label="Training IoU")
    axs[1, 0].plot(range(val_every_n_epochs, val_every_n_epochs * len(val_losses) + 1, val_every_n_epochs), val_ious, label="Validation IoU")
    axs[1, 0].set_title("IoU")
    axs[1, 0].set_xlabel("Epoch")
    axs[1, 0].set_ylabel("IoU")
    axs[1, 0].legend()
    axs[1, 0].grid(True)

    axs[1, 1].plot(range(1, len(train_losses) + 1), train_dices, label="Training Dice")
    axs[1, 1].plot(range(val_every_n_epochs, val_every_n_epochs * len(val_losses) + 1, val_every_n_epochs), val_dices, label="Validation Dice")
    axs[1, 1].set_title("Dice")
    axs[1, 1].set_xlabel("Epoch")
    axs[1, 1].set_ylabel("Dice")
    axs[1, 1].legend()
    axs[1, 1].grid(True)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "metrics_plot.png"))  # Save the figure


def display_image_grid(images, masks, predicted_masks=None, output_dir="plots"):
    """
    Display and save a grid of images along with their ground truth and predicted masks.

    Args:
        images (list): List of images.
        masks (list): List of ground truth masks.
        predicted_masks (list, optional): List of predicted masks. Defaults to None.
        output_dir (str, optional): Directory to save the grid image. Defaults to "plots".

    Returns:
        None
    """
    cols = 3 if predicted_masks else 2
    rows = len(images)
    figure, ax = plt.subplots(nrows=cols, ncols=rows, figsize=(20, 10))
    if predicted_masks is None:
        predicted_masks = [None] * len(images)
    for i, (image, mask, pred) in enumerate(zip(images, masks, predicted_masks)):
        ax[0, i].imshow(image)
        ax[1, i].imshow(mask, interpolation="nearest", cmap=CMAP_4CLASSES)
        ax[0, i].set_title("Image")
        ax[1, i].set_title("Ground truth mask")
        ax[0, i].set_axis_off()
        ax[1, i].set_axis_off()

        if pred is not None:
            ax[2, i].imshow(pred, interpolation="nearest", cmap=CMAP_4CLASSES)
            ax[2, i].set_title("Predicted mask")
            ax[2, i].set_axis_off()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "predictions.png"))


def visualize_augmentations(dataset, idx=0, samples=5):
    """
    Visualize original and augmented versions of a sample from the dataset.

    Args:
        dataset (Dataset): Dataset object with a transform attribute.
        idx (int, optional): Index of the sample to visualize. Defaults to 0.
        samples (int, optional): Number of augmentation samples to display. Defaults to 5.

    Returns:
        None
    """
    dataset = copy.deepcopy(dataset)
    dataset.transform = A.Compose([t for t in dataset.transform if not isinstance(t, (A.Normalize, ToTensorV2))])
    figure, ax = plt.subplots(nrows=2, ncols=samples, figsize=(24, 10))
    for i in range(samples):
        image, mask = dataset[idx] if i > 0 else dataset.get_raw(idx)
        ax[0, i].imshow(image)
        ax[1, i].imshow(mask, interpolation="nearest", cmap=CMAP_4CLASSES)
        ax[0, i].set_title("Augmented image" if i > 0 else "Original image", c='black' if i > 0 else 'dodgerblue')
        ax[1, i].set_title("Augmented mask" if i > 0 else "Original mask", c='black' if i > 0 else 'dodgerblue')
        ax[0, i].set_axis_off()
        ax[1, i].set_axis_off()
    plt.tight_layout()
    plt.show()


def prepare_data(image_paths, mask_paths, window_size=WINDOW_SIZE, color_to_class: dict = None, shrink_factors=[1.0]) -> tuple[list[np.ndarray], list[np.ndarray]]:
    """
    Prepare data by reading images and masks, resizing, and cropping windows.

    Args:
        image_paths (str or list): Path or list of paths to the images.
        mask_paths (str or list): Path or list of paths to the masks.
        window_size (int, optional): Size of the window to crop from the images. Defaults to WINDOW_SIZE.
        color_to_class (dict, optional): Mapping from color tuples to class indices. Defaults to None.
        shrink_factors (list, optional): List of shrink factors to resize images. Each value must be between 0 and 1. Defaults to [1.0].

    Returns:
        tuple: A tuple containing two lists:
            - List of image windows as numpy arrays.
            - List of corresponding mask windows as numpy arrays.
    """
    if isinstance(image_paths, str) and isinstance(mask_paths, str):
        image_paths = [image_paths]
        mask_paths = [mask_paths]
    assert isinstance(image_paths, list) and isinstance(mask_paths, list), "image_paths and mask_paths must be a list of strings"
    assert len(image_paths) == len(mask_paths), "image_paths and mask_paths must have the same length"
    assert all(0 < sf <= 1.0 for sf in shrink_factors), "Shrink factors must be between 0 and 1"

    windows = []
    masks = []

    for ip, mp in zip(image_paths, mask_paths):
        assert os.path.exists(ip), f"{ip} does not exist"
        assert os.path.exists(mp), f"{mp} does not exist"

        original_image = Image.open(ip)
        original_mask = Image.open(mp)

        for shrink_factor in shrink_factors:
            if shrink_factor != 1.0:
                new_size = (int(original_image.width * shrink_factor), int(original_image.height * shrink_factor))
                image = original_image.resize(new_size, Image.NEAREST)
                mask = original_mask.resize(new_size, Image.NEAREST)
            else:
                image = original_image
                mask = original_mask
            
            assert image.size == mask.size, f"Image and mask sizes do not match for {ip} and {mp}"
            assert min(image.size[:2]) >= window_size, f"Image size must be at least {window_size}x{window_size}, your smallest shrink factor is too small"

            for i in range(0, image.height - window_size + 1, window_size // 2):
                for j in range(0, image.width - window_size + 1, window_size // 2):
                    window = image.crop((j, i, j + window_size, i + window_size))
                    mask_window = mask.crop((j, i, j + window_size, i + window_size))

                    if window.format != 'RGB':
                        window = window.convert('RGB')

                    if mask_window.format != 'RGB':
                        mask_window = mask_window.convert('RGB')

                    if np.mean(mask_window) > 0:
                        windows.append(np.array(window))
                        masks.append(np.array(mask_window)[..., 0])

    return windows, masks


def get_model(name='fcn_resnet50', num_classes=3, pretrained=True, weights=None):
    """
    Retrieve a segmentation model and adjust its classifier for the given number of classes.

    Args:
        name (str, optional): Name of the model architecture. Supported options include 'fcn_resnet50', 'fcn_resnet101', 'deeplabv3_resnet101', 'deeplabv3_resnet50', and 'deeplabv3_mobilenet_v3_large'. Defaults to 'fcn_resnet50'.
        num_classes (int, optional): Number of classes for segmentation. Defaults to 3.
        pretrained (bool, optional): Whether to use pretrained weights. Defaults to True.
        weights (str, optional): Path to custom weights to load. Defaults to None.

    Raises:
        ValueError: If the specified model name is not supported.

    Returns:
        torch.nn.Module: The configured segmentation model.
    """
    if name == 'fcn_resnet50':
        model = models.segmentation.fcn_resnet50(weights=models.segmentation.FCN_ResNet50_Weights.DEFAULT if pretrained else None)
    elif name == 'fcn_resnet101':
        model = models.segmentation.fcn_resnet101(pretrained=pretrained)
    elif name == 'deeplabv3_resnet101':
        model = models.segmentation.deeplabv3_resnet101(pretrained=pretrained)
    elif name == 'deeplabv3_resnet50':
        model = models.segmentation.deeplabv3_resnet50(pretrained=pretrained)
    elif name == 'deeplabv3_mobilenet_v3_large':
        model = models.segmentation.deeplabv3_mobilenet_v3_large(pretrained=pretrained)
    else:
        raise ValueError(f"Model {name} not supported")

    # Replace the classifier's final convolution layer
    if hasattr(model.classifier[-1], 'in_channels'):
        in_channels = model.classifier[-1].in_channels
        model.classifier[-1] = nn.Conv2d(in_channels, num_classes, kernel_size=1)

    # Replace the aux_classifier's final convolution layer if it exists
    if hasattr(model, 'aux_classifier') and hasattr(model.aux_classifier[-1], 'in_channels'):
        in_channels = model.aux_classifier[-1].in_channels
        model.aux_classifier[-1] = nn.Conv2d(in_channels, num_classes, kernel_size=1)

    if weights is not None:
        model.load_state_dict(torch.load(weights), strict=False)

    return model


class CephalopodDataset(Dataset):
    """
    Custom dataset for cephalopod images and masks.

    Args:
        images (list): List of image arrays.
        masks (list): List of mask arrays.
        transform (callable, optional): Transformation to apply on the images and masks. Defaults to None.
    """

    def __init__(self, images, masks, transform=None):
        self.images = images
        self.masks = masks
        self.transform = transform

    def __len__(self) -> int:
        """
        Return the total number of samples in the dataset.

        Returns:
            int: Number of samples.
        """
        return len(self.images)

    def __getitem__(self, idx: int) -> tuple[np.ndarray, np.ndarray]:
        """
        Retrieve the image and mask at the specified index, applying transformations if provided.

        Args:
            idx (int): Index of the sample.

        Returns:
            tuple: A tuple (image, mask), where both may be transformed if a transform is provided.
        """
        image = self.images[idx]
        mask = self.masks[idx]

        if self.transform is not None:
            transformed = self.transform(image=image, mask=mask)
            image = transformed["image"]
            try:
                mask = transformed["mask"].long()
            except AttributeError:
                mask = transformed["mask"]
        return image, mask

    def get_raw(self, idx: int) -> tuple[np.ndarray, np.ndarray]:
        """
        Retrieve the raw image and mask at the specified index without applying any transformations.

        Args:
            idx (int): Index of the sample.

        Returns:
            tuple: A tuple (image, mask) in their original form.
        """
        image = self.images[idx]
        mask = self.masks[idx]
        return image, mask
    

def get_dataloader(images, masks, batch_size=BATCH_SIZE, transform=None):
    """
    Create a DataLoader for the given images and masks.

    Args:
        images (list): List of image arrays.
        masks (list): List of mask arrays.
        batch_size (int, optional): Number of samples per batch. Defaults to BATCH_SIZE.
        transform (callable, optional): Transformation to apply on the samples. Defaults to None.

    Returns:
        tuple: A tuple containing:
            - DataLoader: DataLoader for the dataset.
            - CephalopodDataset: The underlying dataset.
    """
    dataset = CephalopodDataset(images, masks, transform=transform)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True, )

    return dataloader, dataset


train_transform = A.Compose(
    [
        A.Resize(520, 520),
        A.ShiftScaleRotate(shift_limit=0.2, scale_limit=0.2, rotate_limit=30, p=0.25),
        A.RGBShift(r_shift_limit=25, g_shift_limit=25, b_shift_limit=25, p=0.25),
        A.RandomBrightnessContrast(brightness_limit=0.1, contrast_limit=0.3, p=0.25),
        # A.Downscale(scale_range=(0.25, 0.75), p=0.1),
        # A.RandomShadow(shadow_roi=(0, 0, 1, 1), num_shadows_limit=(1, 3), shadow_dimension=5, p=0.05),
        # A.FancyPCA(alpha=0.1, p=0.1),
        A.Perspective(scale=(0.05, 0.5), p=0.25),
        A.VerticalFlip(p=0.5),
        A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
        # A.Normalize(normalization='min_max'),
        ToTensorV2(),
    ]
)
val_transform = A.Compose(
    [A.Resize(520, 520), A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)), ToTensorV2()]
    # [A.Resize(WINDOW_SIZE, WINDOW_SIZE), A.Normalize(normalization='min_max'), ToTensorV2()]
)


def train_model(model, criterion, optimizer, train_loader, val_loader, nr_classes, num_epochs=25, device='cuda',
                val_every_n_epochs=5, architecture='fcn_resnet50', output_dir='plots', scheduler=None):
    """
    Train the segmentation model and evaluate it on a validation set.

    Args:
        model (torch.nn.Module): The segmentation model to be trained.
        criterion (callable): Loss function to optimize.
        optimizer (torch.optim.Optimizer): Optimizer for training.
        train_loader (DataLoader): DataLoader for training data.
        val_loader (DataLoader): DataLoader for validation data.
        nr_classes (int): Number of segmentation classes.
        num_epochs (int, optional): Total number of training epochs. Defaults to 25.
        device (str, optional): Device to use ('cuda' or 'cpu'). Defaults to 'cuda'.
        val_every_n_epochs (int, optional): Frequency (in epochs) to run validation. Defaults to 5.
        architecture (str, optional): Model architecture name. Defaults to 'fcn_resnet50'.
        output_dir (str, optional): Directory to save output plots and model weights. Defaults to 'plots'.
        scheduler (torch.optim.lr_scheduler, optional): Learning rate scheduler. Defaults to None.

    Returns:
        torch.nn.Module: The trained model loaded with the best validation weights.
    """
    train_losses, train_accuracies, train_ious, train_dices = [], [], [], []
    val_losses, val_accuracies, val_ious, val_dices = [], [], [], []
    best_model_wts = copy.deepcopy(model.state_dict())
    best_loss = float('inf')
    
    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0
        running_acc = 0.0
        running_iou = 0.0
        running_dice = 0.0

        for inputs, masks in train_loader:
            # print(f'{inputs.shape=} {masks.shape=}')
            # fig, ax = plt.subplots(1, 3, figsize=(15, 5), sharex=True, sharey=True)
            # ax[0].imshow(inputs[0].permute(1, 2, 0))
            # ax[1].imshow(masks[0].squeeze(), cmap=CMAP_4CLASSES)
            # ax[2].imshow(mark_boundaries(inputs[0].permute(1, 2, 0).numpy(), masks[0].squeeze().numpy(), color=(1, 0, 1)), alpha=0.5)
            # plt.show()
            inputs = inputs.to(device)
            masks = masks.to(device)
            optimizer.zero_grad()
            outputs = model(inputs)['out']
            # outputs = torch.argmax
            loss = criterion(outputs, masks)
            acc, iou, dice = calculate_metrics(outputs, masks, num_classes=nr_classes)
            loss.backward()
            optimizer.step()

            running_loss += loss.item() * inputs.size(0)
            running_acc += acc * inputs.size(0)
            running_iou += iou * inputs.size(0)
            running_dice += dice * inputs.size(0)

        epoch_loss = running_loss / len(train_loader.dataset)
        epoch_acc = running_acc / len(train_loader.dataset)
        epoch_iou = running_iou / len(train_loader.dataset)
        epoch_dice = running_dice / len(train_loader.dataset)

        train_losses.append(epoch_loss)
        train_accuracies.append(epoch_acc)
        train_ious.append(epoch_iou)
        train_dices.append(epoch_dice)

        if (epoch + 1) % val_every_n_epochs == 0:
            model.eval()
            val_running_loss = 0.0
            val_running_acc = 0.0
            val_running_iou = 0.0
            val_running_dice = 0.0

            with torch.no_grad():
                for val_inputs, val_masks in val_loader:
                    val_inputs = val_inputs.to(device)
                    val_masks = val_masks.to(device)
                    val_outputs = model(val_inputs)['out']
                    val_loss = criterion(val_outputs, val_masks)
                    val_acc, val_iou, val_dice = calculate_metrics(val_outputs, val_masks, num_classes=nr_classes)

                    val_running_loss += val_loss.item() * val_inputs.size(0)
                    val_running_acc += val_acc * val_inputs.size(0)
                    val_running_iou += val_iou * val_inputs.size(0)
                    val_running_dice += val_dice * val_inputs.size(0)

            val_epoch_loss = val_running_loss / len(val_loader.dataset)
            val_epoch_acc = val_running_acc / len(val_loader.dataset)
            val_epoch_iou = val_running_iou / len(val_loader.dataset)
            val_epoch_dice = val_running_dice / len(val_loader.dataset)

            val_losses.append(val_epoch_loss)
            val_accuracies.append(val_epoch_acc)
            val_ious.append(val_epoch_iou)
            val_dices.append(val_epoch_dice)

            if val_epoch_loss < best_loss:
                best_loss = val_epoch_loss
                best_model_wts = copy.deepcopy(model.state_dict())
            
            if scheduler is not None:
                # Step the learning rate scheduler based on validation loss
                scheduler.step(val_epoch_loss)  # Reduce LR if validation loss plateaus

            click.echo(f'Epoch {epoch + 1}/{num_epochs} - '
                       f'Train Loss: {epoch_loss:.4f}, Acc: {epoch_acc:.4f}, IoU: {epoch_iou:.4f}, Dice: {epoch_dice:.4f} - '
                       f'Val Loss: {val_epoch_loss:.4f}, Acc: {val_epoch_acc:.4f}, IoU: {val_epoch_iou:.4f}, Dice: {val_epoch_dice:.4f}')

    click.echo(f'Best val loss: {best_loss}')
    model.load_state_dict(best_model_wts)
    torch.save(model.state_dict(), os.path.join(output_dir, f'{architecture}_{num_epochs}_best_model.pth'))
    
    # Plot and save metrics
    plot_and_save_metrics(train_losses, train_accuracies, train_ious, train_dices, val_losses, val_accuracies, val_ious, val_dices, output_dir=output_dir,
                            val_every_n_epochs=val_every_n_epochs)
    
    # Run once on the validation set to get predictions
    model.eval()
    images, masks = [], []
    predicted_masks = []
    with torch.no_grad():
        for val_inputs, val_masks in val_loader:
            val_inputs = val_inputs.to(device)
            val_masks = val_masks.to(device)
            val_outputs = model(val_inputs)['out']
            for i in range(len(val_inputs)):
                normalized_image = val_inputs[i].cpu().numpy().transpose(1, 2, 0)
                image = (normalized_image * np.array([0.229, 0.224, 0.225]) + np.array([0.485, 0.456, 0.406]))
                images.append(image)
                masks.append(val_masks[i].cpu().numpy())
                predicted_masks.append(val_outputs[i].argmax(0).cpu().numpy())
    display_image_grid(images[:7], masks[:7], predicted_masks[:7], output_dir=output_dir)

    return model


@error_handler('Training', cluster=False)
def train(input_dir: str, nr_epochs: int = 500, val_every_n_epochs: int = 5, architecture: str = 'fcn_resnet50',
          pretrained: bool = True, nr_classes: int = 4, output_dir: str = None, weights: str = None):
    """
    Train a segmentation model on a dataset of cephalopod images and masks.

    This function loads images and masks from the specified input directory, prepares the data,
    initializes the model, and trains it for a given number of epochs. It also performs validation,
    saves the best model weights, and generates metric plots.

    Args:
        input_dir (str): Path to the directory containing 'images' and 'masks' subdirectories.
        nr_epochs (int, optional): Number of training epochs. Defaults to 500.
        val_every_n_epochs (int, optional): Frequency (in epochs) of running validation. Defaults to 5.
        architecture (str, optional): Model architecture to use. Defaults to 'fcn_resnet50'.
        pretrained (bool, optional): Whether to use pretrained weights for the model. Defaults to True.
        nr_classes (int, optional): Number of segmentation classes. Defaults to 4.
        output_dir (str, optional): Directory to save output results. If None, a new directory is created. Defaults to None.
        weights (str, optional): Path to custom model weights to load. Defaults to None.

    Returns:
        None

    Raises:
        AssertionError: If the input directory or required subdirectories/files do not exist.
    """
    input_dir = Path(input_dir)
    assert input_dir.exists(), f"{input_dir} does not exist"
    assert (input_dir / 'images').exists(), f"{input_dir / 'images'} does not exist"
    assert (input_dir / 'masks').exists(), f"{input_dir / 'masks'} does not exist"

    if output_dir is None:
        output_dir = f'train_{architecture}_{nr_epochs}_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
        # Create a new directory for the output
        os.makedirs(output_dir, exist_ok=True)
    else:
        assert Path(output_dir).exists(), f"{output_dir} does not exist"

    image_paths = list((input_dir / 'images').glob('*.png'))
    mask_paths = list((input_dir / 'masks').glob('*.png'))

    assert len(image_paths) > 0, f"No images found in {input_dir / 'images'}"
    assert len(mask_paths) > 0, f"No masks found in {input_dir / 'masks'}"  #add by Math
    assert len(image_paths) == len(mask_paths), "Number of images and masks must be the same"

    if nr_epochs < val_every_n_epochs:
        val_every_n_epochs = 1
        click.secho("Validation every n epochs must be less than the total number of epochs. Setting it to 1.", fg="yellow")

    model = get_model(architecture, pretrained=pretrained, num_classes=nr_classes, weights=weights)
    click.secho(f"Training {architecture} model with {nr_classes} classes", fg="blue")

    if nr_classes == 4:
        color_to_class = {
            (0, 0, 0): 0,  # Black -> Class 0 (background)
            (0, 255, 0): 1,  # Green -> Class 1 (yellow chromophores)
            (255, 0, 0): 2,   # Red -> Class 2 (orange chromatophores)
            (0, 0, 255): 3   # Blue -> Class 3 (dark chromatophores)
        }
    else:
        color_to_class = {
            (0, 0, 0): 0,  # Black -> Class 0 (background)
            (0, 255, 0): 0,  # Green -> Class 1 (chromatophores)
            (255, 0, 0): 1,   # Red -> Class 1 (chromatophores)
            (0, 0, 255): 1,   # Blue -> Class 1 (chromatophores)
            (255, 255, 255): 1  # White -> Class 1 (chromatophores)
        }

    windows, masks = prepare_data(image_paths, mask_paths, color_to_class=color_to_class)
    np.random.seed(41)
    np.random.shuffle(windows)
    np.random.seed(41)
    np.random.shuffle(masks)

    plt.imshow(masks[0].astype(float), cmap='binary' if nr_classes == 2 else 'jet')
    plt.show()

    plt.imshow(windows[0])
    plt.show()

    N_TRAIN_SAMPLES = (int(0.9 * len(windows)) // BATCH_SIZE) * BATCH_SIZE
    click.echo(f'{N_TRAIN_SAMPLES=}, N_SAMPLES={len(windows)}')
    train_windows, train_masks = windows[:N_TRAIN_SAMPLES], masks[:N_TRAIN_SAMPLES]
    val_windows, val_masks = windows[N_TRAIN_SAMPLES:], masks[N_TRAIN_SAMPLES:]
    click.echo(f"Training on {len(train_windows)} image cutouts, validating on {len(val_windows)} image cutouts")

    train_dataloader, train_dataset = get_dataloader(train_windows, train_masks, transform=train_transform)
    val_dataloader, val_dataset = get_dataloader(val_windows, val_masks, transform=val_transform)

    # Define loss function and optimizer
    criterion = CombinedLoss(alpha=0.5)  # Adjust alpha as needed

    optimizer = optim.Adam(model.parameters(), lr=0.001)  # Adjust lr as needed

    # Learning rate scheduler: Reduce LR when the validation loss has stopped improving
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.1, patience=5, verbose=True)

    # Move model to device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    # Train the model
    _ = train_model(model, criterion, optimizer, train_dataloader, val_dataloader, nr_classes, num_epochs=nr_epochs, device=device,
                    val_every_n_epochs=val_every_n_epochs, architecture=architecture, output_dir=output_dir, scheduler=scheduler)
    click.secho("Training complete.", fg="green", bold=True)
