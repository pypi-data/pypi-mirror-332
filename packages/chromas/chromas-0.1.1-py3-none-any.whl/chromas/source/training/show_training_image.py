import os
import matplotlib.pyplot as plt
from skimage import io
from skimage.segmentation import mark_boundaries
import numpy as np

def plot_image_mask_segmentation(file_path):
    """
    Given a file path, this function checks whether the file is in the 'images' or 'masks' directory.
    It then finds the corresponding mask or image, respectively, and plots the image, mask, and
    the segmentation overlay using matplotlib.

    Parameters:
    - file_path (str): The path to the image or mask file.

    Raises:
    - ValueError: If the file is not in 'images' or 'masks' directory, or if the corresponding file is not found.
    """
    # Normalize the file path
    file_path = os.path.abspath(file_path)
    dir_name, file_name = os.path.split(file_path)
    parent_dir = os.path.basename(dir_name)

    # Determine corresponding directory
    if parent_dir == 'images':
        corresponding_dir = os.path.join(os.path.dirname(dir_name), 'masks')
    elif parent_dir == 'masks':
        corresponding_dir = os.path.join(os.path.dirname(dir_name), 'images')
    else:
        raise ValueError("The file must be located in either 'images' or 'masks' directory.")

    # Construct the path to the corresponding file
    corresponding_file_path = os.path.join(corresponding_dir, file_name)

    if not os.path.exists(corresponding_file_path):
        raise ValueError(f"Corresponding file not found in '{corresponding_dir}': {file_name}")

    # Load image and mask
    if parent_dir == 'images':
        image = io.imread(file_path)
        mask = io.imread(corresponding_file_path)
    else:
        mask = io.imread(file_path)
        image = io.imread(corresponding_file_path)

    # Convert RGBA to RGB if necessary
    if image.ndim == 3 and image.shape[-1] == 4:
        image = image[..., :3]
    
    # Normalize image if it's in integer format
    if image.dtype == np.uint8:
        image = image / 255.0
    elif image.dtype == np.uint16:
        image = image / 65535.0
    elif image.dtype == np.float32 or image.dtype == np.float64:
        image = np.clip(image, 0, 1)
    else:
        raise ValueError(f"Unsupported image data type: {image.dtype}")

    # Ensure mask is binary
    if mask.ndim == 3:
        # If mask has multiple channels, convert to grayscale
        mask = np.any(mask > 0, axis=2)
    else:
        mask = mask > 0

    # Create segmentation overlay
    segmentation = mark_boundaries(image, mask, color=(1, 0, 0))  # RGB color

    # Plotting
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    ax = axes.ravel()

    ax[0].imshow(image)
    ax[0].set_title('Image')
    ax[0].axis('off')

    ax[1].imshow(mask, cmap='gray')
    ax[1].set_title('Mask')
    ax[1].axis('off')

    ax[2].imshow(segmentation)
    ax[2].set_title('Segmentation Overlay')
    ax[2].axis('off')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_image_mask_segmentation('/gpfs/laur/data/ukrowj/training/sepia/sepia_binary_test_modified_2_classes/images/6_0_1024.png')
    plot_image_mask_segmentation('/gpfs/laur/data/ukrowj/training/sepia/sepia_binary_test_modified_2_classes/masks/frame1.png')