import os
import shutil
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import matplotlib.gridspec as gridspec
from ..utils.decorators import error_handler

@error_handler(cluster=False)
def process_images_and_masks(DIR: str, N_classes: int, debug: bool=False):
    """
    Processes images and masks in the specified directory, allowing interactive class assignments.

    Parameters:
    - DIR (str): Path to the main directory containing 'images' and 'masks' subdirectories.
    - N_classes (int): Number of classes (>1) to assign in the masks.
    - debug (bool): If True, prints debug information.

    Raises:
    - ValueError: If the directory structure is invalid or image-mask pairs are inconsistent.
    """
    # Validate inputs
    if debug:
        print(f"Starting process_images_and_masks with DIR: {DIR}, N_classes: {N_classes}, debug: {debug}")

    if not os.path.isdir(DIR):
        raise ValueError(f"The directory {DIR} does not exist.")
    if debug:
        print(f"Verified that directory {DIR} exists.")

    images_dir = os.path.join(DIR, 'images')
    masks_dir = os.path.join(DIR, 'masks')

    if not os.path.isdir(images_dir) or not os.path.isdir(masks_dir):
        raise ValueError(f"The directory {DIR} must contain 'images' and 'masks' subdirectories.")
    if debug:
        print(f"Verified that 'images' and 'masks' subdirectories exist within {DIR}.")

    image_filenames = sorted([f for f in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir, f))])
    mask_filenames = sorted([f for f in os.listdir(masks_dir) if os.path.isfile(os.path.join(masks_dir, f))])

    if debug:
        print(f"Found {len(image_filenames)} images and {len(mask_filenames)} masks.")

    # Find common filenames
    common_filenames = sorted(set(image_filenames).intersection(set(mask_filenames)))
    if not common_filenames:
        raise ValueError("No matching image-mask pairs found.")
    if debug:
        print(f"Found {len(common_filenames)} common image-mask pairs.")

    # Prepare list of image-mask pairs
    image_mask_pairs = []
    for filename in common_filenames:
        image_path = os.path.join(images_dir, filename)
        mask_path = os.path.join(masks_dir, filename)
        try:
            with Image.open(image_path) as img:
                img = img.convert('RGB')
                img_np = np.array(img)
            with Image.open(mask_path) as msk:
                msk = msk.convert('RGB')
                msk_np = np.array(msk)
            if img_np.shape != msk_np.shape:
                print(f"Size mismatch for {filename}. Skipping this pair.")
                if debug:
                    print(f"Image size: {img_np.shape}, Mask size: {msk_np.shape}")
                continue
            image_mask_pairs.append((filename, img_np, msk_np))
            if debug:
                print(f"Added pair: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}. Skipping this pair.")
            if debug:
                print(f"Exception: {e}")
            continue

    if not image_mask_pairs:
        raise ValueError("No valid image-mask pairs to process.")
    if debug:
        print(f"Total valid image-mask pairs to process: {len(image_mask_pairs)}")

    # Prepare output directory
    output_dir = f"{DIR}_modified_{N_classes}_classes"
    output_images_dir = os.path.join(output_dir, 'images')
    output_masks_dir = os.path.join(output_dir, 'masks')
    os.makedirs(output_images_dir, exist_ok=True)
    os.makedirs(output_masks_dir, exist_ok=True)
    if debug:
        print(f"Created output directories at {output_dir}")

    # Function to handle each image-mask pair
    for idx, (filename, img_np, msk_np) in enumerate(image_mask_pairs):
        print(f"Processing {idx+1}/{len(image_mask_pairs)}: {filename}")
        if debug:
            print(f"Processing file: {filename}")

        # Initialize new mask M
        M = np.zeros((msk_np.shape[0], msk_np.shape[1]), dtype=np.uint8)
        if debug:
            print("Initialized new mask M with zeros.")

        # Setup matplotlib figure with shared axes
        plt.close('all')
        fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharex=True, sharey=True)
        fig.canvas.manager.set_window_title("CHROMAS - Unifying training data") if hasattr(fig.canvas.manager, 'set_window_title') else None
        plt.suptitle(filename)

        ax_img, ax_msk, ax_new_msk = axes

        img_display = ax_img.imshow(img_np)
        ax_img.set_title('Image')
        ax_img.axis('off')

        msk_display = ax_msk.imshow(msk_np)
        ax_msk.set_title('Mask')
        ax_msk.axis('off')

        new_msk_display = ax_new_msk.imshow(M, cmap='gray', vmin=0, vmax=N_classes-1)
        ax_new_msk.set_title('New Mask')
        ax_new_msk.axis('off')

        # Add buttons
        reset_ax = plt.axes([0.7, 0.01, 0.1, 0.05])
        next_ax = plt.axes([0.81, 0.01, 0.1, 0.05])
        reset_button = Button(reset_ax, 'Reset')
        next_button = Button(next_ax, 'Next')

        # Initialize variables for interaction
        current_class = 0
        class_labels = list(range(N_classes))
        class_names = [f"class {i}" for i in range(N_classes)]
        plt.subplots_adjust(bottom=0.15)

        # Display instructions
        instruction_text = fig.text(0.5, 0.95, "Instructions: Use the toolbar to zoom/pan. Click on images to assign classes.",
                                     ha='center', va='top', fontsize=12, color='blue')

        # Set window title (fallback handled above)
        if hasattr(fig.canvas.manager, 'set_window_title'):
            try:
                fig.canvas.manager.set_window_title(f"Processing {filename}")
                if debug:
                    print(f"Set window title to 'Processing {filename}'")
            except AttributeError:
                print("Warning: Could not set window title.")
                if debug:
                    print("AttributeError: 'FigureCanvas' object has no attribute 'manager' or 'set_window_title'.")
        else:
            if debug:
                print("Figure canvas manager does not have 'set_window_title' attribute.")

        # Instructions
        title = ax_new_msk.set_title(f"Select {class_names[current_class]}")
        plt.draw()

        # Event handler
        def onclick(event):
            nonlocal M, current_class
            if debug:
                print("Click event detected.")

            # Check if the toolbar is active (e.g., zoom or pan)
            if fig.canvas.manager.toolbar.mode != '':
                if debug:
                    print(f"Toolbar mode active: {fig.canvas.manager.toolbar.mode}. Click ignored.")
                return  # Ignore clicks when toolbar is in pan/zoom mode

            if event.inaxes not in [ax_img, ax_msk]:
                if debug:
                    print("Click was outside of image and mask axes. Ignored.")
                return

            try:
                x, y = int(event.xdata + 0.5), int(event.ydata + 0.5)
                if debug:
                    print(f"Clicked at x: {x}, y: {y}")
                if x < 0 or y < 0 or y >= msk_np.shape[0] or x >= msk_np.shape[1]:
                    if debug:
                        print("Click coordinates out of bounds.")
                    return
                # Get mask value at clicked position
                mask_value = tuple(msk_np[y, x])
                if debug:
                    print(f"Mask value at clicked position: {mask_value}")
                # Find all pixels with this mask value
                matches = np.all(msk_np == mask_value, axis=2)
                num_matches = np.sum(matches)
                if debug:
                    print(f"Number of matching pixels: {num_matches}")
                # Assign current class to these pixels
                previous_assignments = np.sum(M == current_class)
                M[matches] = current_class
                current_assignments = np.sum(M == current_class)
                if debug:
                    print(f"Assigned {current_assignments - previous_assignments} pixels to class {current_class}")
                # Update the new mask display
                new_msk_display.set_data(M)
                new_msk_display.set_clim(vmin=0, vmax=N_classes-1)
                fig.canvas.draw_idle()
            except Exception as e:
                print(f"Error during click event: {e}")
                if debug:
                    print(f"Exception in onclick: {e}")

        def reset(event):
            nonlocal M
            if debug:
                print(f"Reset button clicked for class {current_class}")
            # Reset assignments for the current class
            M[M == current_class] = 0
            # Update the new mask display
            new_msk_display.set_data(M)
            new_msk_display.set_clim(vmin=0, vmax=N_classes-1)
            fig.canvas.draw_idle()
            if debug:
                print(f"Reset completed for class {current_class}")

        def next_class(event):
            nonlocal current_class
            if debug:
                print("Next button clicked.")
            if current_class < N_classes -1:
                current_class += 1
                title.set_text(f"Select {class_names[current_class]}")
                if debug:
                    print(f"Moved to class {current_class}: {class_names[current_class]}")
                plt.draw()
            else:
                if debug:
                    print("All classes processed. Closing the figure.")
                plt.close(fig)

        # Connect events
        cid = fig.canvas.mpl_connect('button_press_event', onclick)
        reset_button.on_clicked(reset)
        next_button.on_clicked(next_class)

        # Show the interactive plot
        plt.show()

        # After closing the plot, save the new mask
        try:
            if debug:
                print(f"Saving new mask for {filename}")
            mask_image = Image.fromarray(M)
            mask_image = mask_image.convert('L')  # Convert to grayscale
            # Ensure the filename has .png extension
            base_filename, _ = os.path.splitext(filename)
            mask_save_filename = base_filename + '.png'
            mask_save_path = os.path.join(output_masks_dir, mask_save_filename)
            mask_image.save(mask_save_path, format='PNG')
            if debug:
                print(f"Saved new mask at {mask_save_path}")
        except Exception as e:
            print(f"Error saving mask for {filename}: {e}. Skipping saving.")
            if debug:
                print(f"Exception while saving mask: {e}")
            continue

        # Copy the image to the new directory
        try:
            if debug:
                print(f"Copying image {filename} to {output_images_dir}")
            shutil.copy(os.path.join(images_dir, filename), os.path.join(output_images_dir, filename))
            if debug:
                print(f"Copied image {filename} successfully.")
        except Exception as e:
            print(f"Error copying image {filename}: {e}. Skipping copying.")
            if debug:
                print(f"Exception while copying image: {e}")
            continue

    print(f"Processing completed. Modified data saved in {output_dir}.")
    if debug:
        print("Function process_images_and_masks has finished execution.")


if __name__ == "__main__":
    process_images_and_masks('/gpfs/laur/data/ukrowj/training/sepia/sepia_binary_test', 2, True)