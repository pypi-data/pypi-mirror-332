import os
import numpy as np
import matplotlib.pyplot as plt
import functools
import joblib
import PIL
import PIL.ImageEnhance
from PIL import Image
import skimage.feature
import skimage.measure
import skimage.segmentation
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import balanced_accuracy_score
import cv2

# =============================================================================
# Wrapper Class to Bundle the Classifier and Feature Extraction Parameters
# =============================================================================
class SegmentationModelWrapper:
    def __init__(self, classifier, sigma_min, sigma_max, num_sigma=4):
        self.classifier = classifier
        self.sigma_min = sigma_min
        self.sigma_max = sigma_max
        self.num_sigma = num_sigma
        
    def extract_features(self, image: np.ndarray) -> np.ndarray:
        """Extract multiscale features using stored parameters."""
        return extract_multiscale_features(image, self.sigma_min, self.sigma_max, self.num_sigma)
    
    def predict(self, image: np.ndarray) -> np.ndarray:
        """Predict segmentation mask for a given image."""
        feat = self.extract_features(image)
        H, W = image.shape[:2]
        feat_flat = feat.reshape(-1, feat.shape[-1])
        predicted = self.classifier.predict(feat_flat)
        return predicted.reshape(H, W)

# =============================================================================
# Feature Extraction and Scale Computation Functions
# =============================================================================
def extract_multiscale_features(image: np.ndarray, sigma_min: float, sigma_max: float, num_sigma: int = 4) -> np.ndarray:
    """
    Extract multiscale basic features from the image.
    Returns a feature array of shape (H, W, n_features).
    """
    features_func = functools.partial(
        skimage.feature.multiscale_basic_features,
        intensity=True, edges=True, texture=False,
        sigma_min=sigma_min, sigma_max=sigma_max, num_sigma=num_sigma,
        channel_axis=-1, num_workers=None
    )
    return features_func(image)

def compute_scale_parameters(labels_list):
    """
    Compute typical object sizes from a list of integer label images.
    For each unique label in each image, compute region properties (after clearing border artifacts)
    and then use the 1st and 99th percentiles of the minor/major axis lengths to set sigma parameters.
    """
    axis_lengths = []
    for label_img in labels_list:
        for cls in np.unique(label_img):
            mask = (label_img == cls)
            mask = skimage.segmentation.clear_border(mask)
            labeled_mask = skimage.measure.label(mask)
            regions = skimage.measure.regionprops(labeled_mask)
            for region in regions:
                axis_lengths.append((region.axis_minor_length, region.axis_major_length))
    axis_lengths = np.array(axis_lengths)
    if axis_lengths.size == 0:
        raise ValueError("No regions found in label images. Check your labels.")
    minor_axis_length = np.percentile(axis_lengths[:, 0], 1) / 2
    major_axis_length = np.percentile(axis_lengths[:, 1], 99) / 2
    sigma_min = minor_axis_length / (2 * np.sqrt(2))
    sigma_max = major_axis_length / (2 * np.sqrt(2))
    print(f"Estimated object radii: ~{minor_axis_length:.2f} to ~{major_axis_length:.2f} pixels.")
    print(f"Using sigma_min={sigma_min:.2f} and sigma_max={sigma_max:.2f}.")
    return sigma_min, sigma_max

# =============================================================================
# Main Training Function
# =============================================================================
def train_segmentation_model(
    images_dir: str,
    labels_dir: str,
    test_img_path: str,
    output_model_path: str,
    augmentation: bool = False,
    use_grid_search: bool = False,
    remove_duplicates: bool = False,
    plot: bool = True
):
    # Load test image
    test_img = np.asarray(Image.open(test_img_path).convert('RGB'))
    images = []
    labels = []
    
    # Ensure proper pairing by sorting file names
    image_files = sorted(os.listdir(images_dir))
    label_files = sorted(os.listdir(labels_dir))
    
    for img_file, label_file in zip(image_files, label_files):
        with Image.open(os.path.join(images_dir, img_file)) as img:
            img = img.convert('RGB')
            img_np = np.array(img)
        with Image.open(os.path.join(labels_dir, label_file)) as lab:
            # Labels are stored as integer images (in 'L' mode)
            lab_np = np.array(lab.convert('L'))
        images.append(img_np)
        labels.append(lab_np)
        # Augmentation (only intensity-based; mask remains unchanged)
        if augmentation:
            for factor in np.linspace(0.7, 1.3, 5):
                brightness = PIL.ImageEnhance.Brightness(img).enhance(factor)
                color_enh = PIL.ImageEnhance.Color(img).enhance(factor)
                contrast = PIL.ImageEnhance.Contrast(img).enhance(factor)
                sharpness = PIL.ImageEnhance.Sharpness(img).enhance(factor)
                for aug_img in [brightness, color_enh, contrast, sharpness]:
                    images.append(np.array(aug_img.convert('RGB')))
                    labels.append(lab_np)
                    
    # Compute sigma parameters from training masks
    sigma_min, sigma_max = compute_scale_parameters(labels)
    
    # Extract pixelwise features from training images
    x_train_list = []
    y_train_list = []
    for img_np, lab_np in zip(images, labels):
        feat = extract_multiscale_features(img_np, sigma_min, sigma_max, num_sigma=4)
        x_train_list.append(feat.reshape(-1, feat.shape[-1]))
        y_train_list.append(lab_np.ravel())
        
    x_train = np.concatenate(x_train_list, axis=0)
    y_train = np.concatenate(y_train_list, axis=0)
    print("Combined training features shape:", x_train.shape)
    print("Combined training labels shape:", y_train.shape)
    
    # Optionally remove duplicate feature vectors (and corresponding labels)
    if remove_duplicates:
        print("Removing duplicate features to reduce training size...")
        unique_features, unique_indices = np.unique(x_train, axis=0, return_index=True)
        x_train = unique_features
        y_train = y_train[unique_indices]
        print("After duplicate removal, features shape:", x_train.shape)
        
    # Optionally perform grid search for hyperparameter tuning
    if use_grid_search:
        X_tr, X_val, y_tr, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=42)
        param_grid = {
            'n_estimators': [10, 50, 100, 200],
            'max_depth': [5, 10, 25, None],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }
        rf = RandomForestClassifier(random_state=42, n_jobs=-1)
        grid_search = GridSearchCV(rf, param_grid, cv=3, scoring='balanced_accuracy', n_jobs=-1)
        print("Performing grid search...")
        grid_search.fit(X_tr, y_tr)
        best_rf = grid_search.best_estimator_
        print("Best parameters from grid search:", grid_search.best_params_)
        y_val_pred = best_rf.predict(X_val)
        print("Validation balanced accuracy:", balanced_accuracy_score(y_val, y_val_pred))
    else:
        best_rf = RandomForestClassifier(n_estimators=32, max_depth=32, random_state=42, n_jobs=-1)
        best_rf.fit(x_train, y_train)
        
    # Create segmentation model wrapper object that bundles classifier and feature parameters
    segmentation_model = SegmentationModelWrapper(best_rf, sigma_min, sigma_max, num_sigma=4)
    
    # Save the segmentation model wrapper (this includes both the classifier and feature extraction details)
    joblib.dump(segmentation_model, output_model_path)
    print(f"Model wrapper saved to {output_model_path}.")
    
    # Predict segmentation for the test image (using the raw classifier)
    test_features = extract_multiscale_features(test_img, sigma_min, sigma_max, num_sigma=4)
    H_test, W_test = test_img.shape[:2]
    test_features_flat = test_features.reshape(-1, test_features.shape[-1])
    predicted_labels = best_rf.predict(test_features_flat)
    segmentation_result = predicted_labels.reshape(H_test, W_test)
    
    if plot:
        fig, ax = plt.subplots(1, 2, figsize=(10, 5))
        ax[0].imshow(skimage.segmentation.mark_boundaries(test_img, segmentation_result, mode='thick'))
        ax[0].set_title('Test Image with Segmentation Boundaries')
        ax[1].imshow(segmentation_result, cmap='nipy_spectral')
        ax[1].set_title('Segmentation Result')
        plt.tight_layout()
        plt.show()
    
    return segmentation_model, segmentation_result

# =============================================================================
# Synthetic Data Generation Functions
# =============================================================================
def generate_synthetic_image_and_mask(size=(50, 50)):
    """
    Generate a synthetic RGB image with a circular object and its corresponding mask.
    The mask is a single-channel image with 0 as background and 1 as the object.
    """
    image = np.zeros((size[0], size[1], 3), dtype=np.uint8)
    mask = np.zeros((size[0], size[1]), dtype=np.uint8)
    center = (size[1] // 2, size[0] // 2)
    radius = min(size) // 4
    color = (200, 100, 50)  # arbitrary object color
    cv2.circle(image, center, radius, color, -1)
    cv2.circle(mask, center, radius, 1, -1)  # object label = 1
    return image, mask

# =============================================================================
# Main: Generate Synthetic Data, Train Model, and Test Prediction
# =============================================================================
if __name__ == "__main__":
    # Create directories for synthetic training images and labels
    os.makedirs("synthetic_train_images", exist_ok=True)
    os.makedirs("synthetic_train_labels", exist_ok=True)
    
    # Generate and save synthetic training images and masks
    num_train = 3
    for i in range(num_train):
        img, mask = generate_synthetic_image_and_mask(size=(50, 50))
        img_pil = Image.fromarray(img)
        # Save mask as a grayscale image (scale mask values to 0/255 for visualization)
        mask_pil = Image.fromarray((mask * 255).astype(np.uint8))
        img_pil.save(f"synthetic_train_images/train_img_{i}.png")
        mask_pil.save(f"synthetic_train_labels/train_mask_{i}.png")
    
    # Generate and save a synthetic test image (without a label)
    test_img, _ = generate_synthetic_image_and_mask(size=(50, 50))
    test_img_pil = Image.fromarray(test_img)
    test_img_path = "synthetic_test_image.png"
    test_img_pil.save(test_img_path)
    
    # Train the segmentation model using the synthetic data
    model_output_path = "segmentation_model_wrapper.pkl"
    segmentation_model, segmentation_result = train_segmentation_model(
        images_dir="synthetic_train_images",
        labels_dir="synthetic_train_labels",
        test_img_path=test_img_path,
        output_model_path=model_output_path,
        augmentation=True,
        use_grid_search=True,
        remove_duplicates=True,
        plot=True
    )
    
    # Demonstrate loading the saved model wrapper and using it for prediction
    loaded_model = joblib.load(model_output_path)
    test_img_loaded = np.asarray(Image.open(test_img_path).convert("RGB"))
    predicted_segmentation = loaded_model.predict(test_img_loaded)
    
    # Display the loaded model's prediction (with segmentation boundaries)
    plt.figure(figsize=(5,5))
    plt.imshow(skimage.segmentation.mark_boundaries(test_img_loaded, predicted_segmentation, mode="thick"))
    plt.title("Predicted Segmentation from Loaded Model")
    plt.axis("off")
    plt.show()
    
    # Optionally, map predicted integer labels to colors (for visualization)
    color_mapping = {
        0: (0, 0, 0),         # Background
        1: (255, 0, 0),
        2: (0, 255, 0),
        3: (0, 0, 255)
    }
    seg_img = np.zeros((predicted_segmentation.shape[0], predicted_segmentation.shape[1], 3), dtype=np.uint8)
    for class_id, color in color_mapping.items():
        seg_img[predicted_segmentation == class_id] = color
    plt.figure(figsize=(5,5))
    plt.imshow(seg_img)
    plt.title("Color-mapped Predicted Segmentation")
    plt.axis("off")
    plt.show()
