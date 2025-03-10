""" Utility functions to plot data. """

import matplotlib.pyplot as plt
import numpy as np

def plot_queenframe(queenframe: np.ndarray) -> None:
    """
    Plot the queenframe image.

    Args:
        queenframe (np.ndarray): The queenframe image to be plotted.

    Returns:
        None

    This function displays the queenframe image using a grayscale colormap.
    """
    plt.imshow(queenframe, cmap='gray')
    plt.title('Queenframe')
    plt.show()


def plot_initial_registration(start_image_rgb: np.ndarray, target_image_rgb: np.ndarray, 
                              warped_image_rgb: np.ndarray, target_image: np.ndarray, 
                              start_image_initialy_registered: np.ndarray) -> None:
    """
    Plot the initial registration of images.

    Args:
        start_image_rgb (np.ndarray): The RGB start image.
        target_image_rgb (np.ndarray): The RGB target image.
        warped_image_rgb (np.ndarray): The RGB warped image after initial registration.
        target_image (np.ndarray): The grayscale target image.
        start_image_initialy_registered (np.ndarray): The grayscale start image after initial registration.

    Returns:
        None

    This function creates a figure with four subplots showing the start image, target image,
    initially registered start image, and an overlay of the target and registered start images.
    """
    fig, ax = plt.subplots(1, 4, figsize=(15, 5), sharex=True, sharey=True)
    target_image_red = np.zeros((*target_image.shape, 3))
    target_image_red[..., 0] = target_image
    start_image_initialy_registered_blue = np.zeros((*start_image_initialy_registered.shape, 3))
    start_image_initialy_registered_blue[..., 2] = start_image_initialy_registered

    ax[0].imshow(start_image_rgb)
    ax[0].set_title('Start image')

    ax[1].imshow(target_image_rgb)
    ax[1].set_title('Target image')

    ax[2].imshow(warped_image_rgb)
    ax[2].set_title('Initial registration of start image')

    ax[3].imshow(start_image_initialy_registered_blue + target_image_red)
    ax[3].set_title('Overlay')
    plt.suptitle('Initial registration of start image to target image')
    plt.tight_layout()
    plt.show()


def plot_grid_registration(target_image: np.ndarray, start_image_initialy_registered: np.ndarray, 
                           gridpoints: np.ndarray, target_grid: np.ndarray, image_warped: np.ndarray) -> None:
    """
    Plot the grid registration results.

    Args:
        target_image (np.ndarray): The target image.
        start_image_initialy_registered (np.ndarray): The initially registered start image.
        gridpoints (np.ndarray): The grid points on the start image.
        target_grid (np.ndarray): The corresponding grid points on the target image.
        image_warped (np.ndarray): The warped image after grid registration.

    Returns:
        None

    This function creates a figure with four subplots showing the start image with grid points,
    target image with grid points, overlay of start and target images, and the warped image.
    """
    fig, ax = plt.subplots(1, 4, figsize=(24, 6))
    ax[0].imshow(start_image_initialy_registered, cmap='gray')
    ax[0].scatter(gridpoints[:, 1], gridpoints[:, 0], color='red', s=5)
    ax[0].set_title('Chunk 1')

    ax[1].imshow(target_image, cmap='gray')
    ax[1].scatter(gridpoints[:, 1], gridpoints[:, 0], color='red', s=5)
    ax[1].set_title('Chunk 2')

    overlay_image = np.zeros((*image_warped.shape, 3))
    overlay_image[..., 0] = target_image  # Red channel
    overlay_image[..., 2] = image_warped  # Blue channel
    ax[3].imshow(overlay_image)
    ax[3].set_title('Warped image')

    overlay_initial_registered = np.zeros((*start_image_initialy_registered.shape, 3))
    overlay_initial_registered[..., 2] = start_image_initialy_registered  # Red channel
    overlay_initial_registered[..., 0] = target_image  # Blue channel
    ax[2].imshow(overlay_initial_registered)
    ax[2].set_title('Overlay image')

    ax[1].scatter(target_grid[:, 1], target_grid[:, 0], color='green', s=15)
    plt.tight_layout()
    plt.show()


def plot_reprojection(chunk_idx: int, cutouts: list, target_chunk_idx: int, 
                      gridpoints: np.ndarray, points_in_target: np.ndarray, 
                      points_mapped_back: np.ndarray) -> None:
    """
    Plot the reprojection results.

    Args:
        chunk_idx (int): Index of the current chunk.
        cutouts (list): List of image cutouts.
        target_chunk_idx (int): Index of the target chunk.
        gridpoints (np.ndarray): Original grid points.
        points_in_target (np.ndarray): Corresponding points in the target image.
        points_mapped_back (np.ndarray): Points mapped back to the original image.

    Returns:
        None

    This function creates a figure with two subplots showing the original image with grid points
    and arrows indicating the reprojection, and the target image with corresponding points.
    """
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    ax[0].imshow(cutouts[chunk_idx], cmap='gray')
    ax[1].imshow(cutouts[target_chunk_idx], cmap='gray')
    ax[0].plot(gridpoints[:, 1], gridpoints[:, 0], 'ro')
    ax[1].plot(points_in_target[:, 1], points_in_target[:, 0], 'ro')
    # Plot arrows from gridpoints_memory[chunk_idx] to points_mapped_back:
    for i, (gp, pm, pt) in enumerate(zip(gridpoints, points_mapped_back, points_in_target)):
        ax[0].arrow(gp[1], gp[0], pm[1]-gp[1], pm[0]-gp[0], color='green', head_width=2, head_length=2)
    plt.show()