from pathlib import Path
import click
from matplotlib.colors import ListedColormap
import torch
import torch.nn as nn
import torch.optim as optim
import torchmetrics.classification
import torchmetrics.segmentation
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
import torchmetrics

from .unet_utils import UNet3Layers as UNet



CMAP_4CLASSES = ListedColormap([[1, 1, 1], [255/255, 200/255, 0], [255/255, 127/255, 0], [65/255, 35/255, 0]])
CMAP_2CLASSES = ListedColormap([[1, 1, 1], [65/255, 35/255, 0]])
WINDOW_SIZE = 128
BATCH_SIZE = 32


def plot_and_save_metrics(train_losses, train_accuracies, train_ious, train_dices, val_losses, val_accuracies, val_ious, val_dices, output_dir="plots",
                          val_every_n_epochs=5):
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
    dataset = copy.deepcopy(dataset)
    dataset.transform = A.Compose([t for t in dataset.transform if not isinstance(t, (A.Normalize, ToTensorV2))])
    figure, ax = plt.subplots(nrows=2, ncols=samples, figsize=(24, 10))
    for i in range(samples):
        image, mask = dataset[idx] if i>0 else dataset.get_raw(idx)
        ax[0, i].imshow(image)
        ax[1, i].imshow(mask, interpolation="nearest", cmap=CMAP_4CLASSES)
        ax[0, i].set_title("Augmented image" if i>0 else "Original image", c='black' if i>0 else 'dodgerblue')
        ax[1, i].set_title("Augmented mask" if i>0 else "Original mask", c='black' if i>0 else 'dodgerblue')
        ax[0, i].set_axis_off()
        ax[1, i].set_axis_off()
    plt.tight_layout()
    plt.show()


def prepare_data(image_paths, mask_paths, window_size=WINDOW_SIZE, color_to_class: dict=None, shrink_factors=[1.0]) -> tuple[list[np.ndarray], list[np.ndarray]]:
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

        # Convert RGBA to RGB if necessary:
        if original_image.mode == 'RGBA':
            original_image = original_image.convert('RGB')
        if original_mask.mode == 'RGBA':
            original_mask = original_mask.convert('RGB')

        # plt.imshow(original_mask)
        # plt.show()

        for shrink_factor in shrink_factors:
            if shrink_factor != 1.0:
                new_size = (int(original_image.width * shrink_factor), int(original_image.height * shrink_factor))
                image = original_image.resize(new_size, Image.NEAREST)
                mask = original_mask.resize(new_size, Image.NEAREST)
            else:
                image = original_image
                mask = original_mask
            
            assert image.size == mask.size, f"Image and mask sizes do not match for {ip} and {mp}"

            if window_size is not None:
                assert min(image.size[:2]) >= window_size, f"Image size must be at least {window_size}x{window_size}, your smallest shrink factor is too small"
                for i in range(0, image.height - window_size + 1, window_size // 2):
                    for j in range(0, image.width - window_size + 1, window_size // 2):
                        window = image.crop((j, i, j + window_size, i + window_size))
                        mask_window = mask.crop((j, i, j + window_size, i + window_size))

                        if window.format != 'RGB':
                            window = window.convert('RGB')

                        if mask_window.format != 'RGB':
                            mask_window = mask_window.convert('RGB')

                        mask_window_rgba = np.array(mask_window)
                        # mask_window = np.zeros(mask_window_rgba.shape[:2])
                        # for color, cls in color_to_class.items():
                        #     mask_window[(mask_window_rgba == color).all(axis=-1)] = cls
                        mask_window = (mask_window_rgba[..., 0] < 125).astype(np.uint8)

                        if np.mean(mask_window) > 0:
                            windows.append(np.array(window))
                            masks.append(mask_window)
            else:
                mask_rgba = np.array(mask)
                mask = np.zeros(mask_rgba.shape[:2])
                for color, cls in color_to_class.items():
                    mask[(mask_rgba == color).all(axis=-1)] = cls
                if np.mean(mask) > 0:
                    windows.append(np.array(image))
                    masks.append(mask)

    return windows, masks


# Model Selection
def get_model(name='fcn_resnet50', num_classes=3, pretrained=True, weights=None):
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
    elif name == 'unet':
        model = UNet(num_classes=num_classes)
    else:
        raise ValueError(f"Model {name} not supported")

    if name != 'unet':
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


# Dataset
class CephalopodDataset(Dataset):
    def __init__(self, images, masks, transform=None):
        self.images = images
        self.masks = masks
        self.transform = transform

    def __len__(self) -> int:
        return len(self.images)

    def __getitem__(self, idx: int) -> tuple[np.ndarray, np.ndarray]:
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
        image = self.images[idx]
        mask = self.masks[idx]
        return image, mask
    

# Create dataset and dataloader
def get_dataloader(images, masks, batch_size=BATCH_SIZE, transform=None):

    dataset = CephalopodDataset(images, masks, transform=transform)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True, )

    return dataloader, dataset


train_transform = A.Compose(
    [
        # A.Resize(520, 520),
        A.ShiftScaleRotate(shift_limit=0.2, scale_limit=0.2, rotate_limit=30, p=0.25),
        A.RGBShift(r_shift_limit=25, g_shift_limit=25, b_shift_limit=25, p=0.25),
        A.RandomBrightnessContrast(brightness_limit=0.1, contrast_limit=0.3, p=0.25),
        # A.Downscale(scale_range=(0.25, 0.75), p=0.1),
        # A.RandomShadow(shadow_roi=(0, 0, 1, 1), num_shadows_limit=(1, 3), shadow_dimension=5, p=0.05),
        # A.FancyPCA(alpha=0.1, p=0.1),
        A.Perspective(scale=(0.05, 0.5), p=0.25),
        A.VerticalFlip(p=0.5),
        # A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
        # A.Normalize(normalization='min_max'),
        ToTensorV2(),
    ]
)
val_transform = A.Compose(
    [ToTensorV2()]
    # [A.Resize(WINDOW_SIZE, WINDOW_SIZE), A.Normalize(normalization='min_max'), ToTensorV2()]
)


def train_model(model, train_loader, val_loader, nr_classes, num_epochs=25, device='cuda',
                val_every_n_epochs=5, architecture='fcn_resnet50', output_dir='plots'):
    
    train_losses, train_accuracies, train_ious, train_dices = [], [], [], []
    val_losses, val_accuracies, val_ious, val_dices, val_maccs = [], [], [], [], []
    best_model_wts = copy.deepcopy(model.state_dict())
    best_loss = float('inf')

    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)  # Adjust lr as needed
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=20, gamma=0.5)
    scaler = torch.cuda.amp.GradScaler()

    # Move model to device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    # DEFINE LOSS FUNCTION:
    ce_weight = torch.tensor([0.2] + [0.8/(nr_classes-1)] * (nr_classes-1))
    ce_weight = torch.tensor([.5, .5])
    criterion = nn.CrossEntropyLoss(weight=ce_weight).to(device)
    # Metrics:
    miou = torchmetrics.segmentation.MeanIoU(num_classes=nr_classes, input_format='index').to(device)
    dice = torchmetrics.segmentation.GeneralizedDiceScore(num_classes=nr_classes, input_format='index').to(device)
    macc = torchmetrics.classification.MulticlassAccuracy(num_classes=nr_classes, average=None).to(device)

    for epoch in range(num_epochs):
        model.train()
        loss_score, iou_score, dice_score = torch.tensor(0.0), torch.tensor(0.0), torch.tensor(0.0)
        total_samples = 0

        for inputs, masks in train_loader:
            # fig, ax = plt.subplots(1, 3, figsize=(15, 5), sharex=True, sharey=True)
            # ax[0].imshow(inputs[0].permute(1, 2, 0))
            # ax[0].set_title('Input image')
            # ax[1].imshow(masks[0].squeeze(), cmap=CMAP_4CLASSES)
            # ax[1].set_title('Ground truth mask')
            # ax[2].imshow(mark_boundaries(inputs[0].permute(1, 2, 0).numpy(), masks[0].squeeze().numpy(), color=(0, 1, 0)))
            # ax[2].set_title('Image with mask')
            # fig.suptitle('First image and mask of training batch input')
            # plt.show()
            
            # One hot encode the masks

            optimizer.zero_grad()
            with torch.amp.autocast('cuda'):
                inputs = inputs.to(device).float().div(255)
                masks = masks.to(device)

                outputs = model(inputs)['out']
                loss = criterion(outputs, masks)

            scaler.scale(loss).backward()
            scaler.step(optimizer)
            scaler.update()

            batch_size = inputs.size(0)
            total_samples += batch_size

            preds = torch.argmax(outputs, 1)
            loss_score += loss.cpu().detach() * batch_size
            iou_score += miou(preds, masks).cpu().detach() * batch_size
            dice_score += dice(preds, masks).cpu().detach() * batch_size

            

        train_loss = loss_score / total_samples
        train_iou = iou_score / total_samples
        train_dice = dice_score / total_samples

        train_losses.append(train_loss)
        train_ious.append(train_iou)
        train_dices.append(train_dice)

        # UPDATE THE LEARNING RATE:
        scheduler.step()
        current_lr = scheduler.get_last_lr()[0]

        if (epoch + 1) % val_every_n_epochs == 0:
            model.eval()
            loss_score, iou_score, dice_score = torch.tensor(0.0), torch.tensor(0.0), torch.tensor(0.0)
            macc_score = torch.zeros(nr_classes)
            total_samples = 0
            
            with torch.no_grad():
                for inputs, masks in val_loader:
                    with torch.cuda.amp.autocast():
                        inputs = inputs.to(device).float().div(255)
                        masks = masks.to(device)

                        outputs = model(inputs)['out']
                        loss = criterion(outputs, masks)


                    batch_size = inputs.size(0)
                    total_samples += batch_size

                    preds = torch.argmax(outputs, 1).detach()
                    loss_score += loss.cpu() * batch_size
                    iou_score += miou(preds, masks).cpu() * batch_size
                    dice_score += dice(preds, masks).cpu() * batch_size
                    macc_score += macc(preds, masks).cpu() * batch_size


            val_loss = loss_score / total_samples
            val_iou = iou_score / total_samples
            val_dice = dice_score / total_samples
            macc_score = macc_score.cpu() / total_samples
            val_losses.append(val_loss)
            val_ious.append(val_iou)
            val_dices.append(val_dice)
            val_maccs.append(macc_score)
            
            if val_loss < best_loss:
                best_loss = val_loss
                best_model_wts = copy.deepcopy(model.state_dict())
            
            click.echo(f'Epoch {epoch + 1}/{num_epochs} - '
                       f'Train Loss: {train_loss:.4f}, Acc: _.____, IoU: {train_iou:.4f}, Dice: {train_dice:.4f} - '
                       f'Val Loss: {val_loss:.4f}, Acc: {macc_score.mean():.4f}, IoU: {val_iou:.4f}, Dice: {val_dice:.4f} - '
                       f'LR: {current_lr:.6f}')

    click.echo(f'Best val loss: {best_loss}')
    model.load_state_dict(best_model_wts)
    torch.save(model.state_dict(), os.path.join(output_dir, f'{architecture}_{num_epochs}_best_model.pth'))
    
    fig, ax = plt.subplots(2, 2, figsize=(15, 8))
    ax[0, 0].plot(train_losses, label='Train Loss', marker='o')
    ax[0, 0].set_ylim(0, 1)
    ax[0, 0].plot(range(0, len(train_losses), val_every_n_epochs), val_losses, marker='o', label='Val Loss')
    ax[0, 0].set_ylabel('Loss')
    ax[0, 0].set_xlabel('Epoch')
    ax[0, 0].legend()
    miou.plot(train_ious, ax=ax[0, 1])
    ax[0, 1].plot(range(0, len(train_ious), val_every_n_epochs), val_ious, marker='o')
    dice.plot(train_dices, ax=ax[1, 0])
    ax[1, 0].plot(range(0, len(train_dices), val_every_n_epochs), val_dices, marker='o')
    macc.plot(val_maccs, ax=ax[1, 1])
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'metrics_plot.png'), dpi=900)
    plt.close()
    
    return model


def train(input_dir: str, nr_epochs: int=500, val_every_n_epochs: int=5, architecture: str='fcn_resnet50',
          pretrained: bool=True, nr_classes: int=4, output_dir: str=None, weights: str=None):

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
    assert len(mask_paths) > 0, f"No masks found in {input_dir / 'masks'}" #add by Math
    assert len(image_paths) == len(mask_paths), "Number of images and masks must be the same"

    if nr_epochs < val_every_n_epochs:
        val_every_n_epochs = 1
        click.secho("Validation every n epochs must be less than the total number of epochs. Setting it to 1.", fg="yellow")

    model = get_model(architecture, pretrained=pretrained, num_classes=nr_classes, weights=weights)
    click.secho(f"Training {architecture} model with {nr_classes} classes", fg="blue")
    # Print number of trainable and number of total parameters:
    num_trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    num_total_params = sum(p.numel() for p in model.parameters())
    click.secho(f"Number of trainable parameters: {num_trainable_params}. Number of total parameters: {num_total_params}.", fg='blue')

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
            (0, 254, 0): 0,  # Green -> Class 1 (chromatophores)
            (255, 0, 0): 1,   # Red -> Class 1 (chromatophores)
            (254, 0, 0): 1,   # Red -> Class 1 (chromatophores)
            (0, 0, 255): 1,   # Blue -> Class 1 (chromatophores)
            (0, 0, 254): 1,   # Blue -> Class 1 (chromatophores)
            (255, 255, 255): 1  # White -> Class 1 (chromophores)
        }

    windows, masks = prepare_data(image_paths, mask_paths, color_to_class=color_to_class, window_size=WINDOW_SIZE)

    np.random.seed(41)
    np.random.shuffle(windows)
    np.random.seed(41)
    np.random.shuffle(masks)

    fig, ax = plt.subplots(1, 3)
    ax[0].imshow(windows[0])
    ax[0].set_title("X (Image)")
    ax[1].imshow(masks[0], cmap='binary')  # CMAP_4CLASSES if nr_classes == 4 else CMAP_2CLASSES
    ax[1].set_title("Y (Mask)")
    ax[2].imshow(mark_boundaries(windows[0], masks[0] > 0, color=(0, 1, 0)))
    ax[2].set_title("X with Y (Overlay)")
    fig.suptitle("Example image and mask from training data")
    plt.show()

    N_TRAIN_SAMPLES = (int(0.9 * len(windows)) // BATCH_SIZE) * BATCH_SIZE
    train_windows, train_masks = windows[:N_TRAIN_SAMPLES], masks[:N_TRAIN_SAMPLES]
    val_windows, val_masks = windows[N_TRAIN_SAMPLES:], masks[N_TRAIN_SAMPLES:]
    click.echo(f"Training on {len(train_windows)} image cutouts, validating on {len(val_windows)} image cutouts")

    train_dataloader, train_dataset = get_dataloader(train_windows, train_masks, transform=train_transform)
    val_dataloader, val_dataset = get_dataloader(val_windows, val_masks, transform=val_transform)

    # Train the model
    _ = train_model(model, train_dataloader, val_dataloader, nr_classes, num_epochs=nr_epochs, val_every_n_epochs=val_every_n_epochs, architecture=architecture, output_dir=output_dir)
    click.secho("Training complete.", fg="green", bold=True)