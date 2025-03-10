"""
Training of Random Forest based Segmentation
============================================

This module provides functionality for training a Random Forest-based segmentation model 
using multiscale features. Leveraging traditional machine learning methods rather 
than deep learning.

Key Features:
    - Reads training images and corresponding masks from a specified input directory.
    - Extracts multiscale features for segmentation.
    - Optionally applies grid search for hyperparameter tuning.
    - Removes duplicate features to improve training efficiency.
    - Trains a Random Forest classifier and wraps it with feature extraction parameters.
    - Saves the trained model using joblib for future inference.

Expected Directory Structure:
    input_dir/
        images/    (contains training images)
        masks/     (contains corresponding integer-labeled masks)
"""


import os
import click
import joblib

from .random_forest_utils import train_segmentation_model

def train(input_dir, output_dir):
    """
    Train a Random Forest segmentation model using multiscale features.
    
    Args:
        input_dir (str): Path to the input directory containing 'images' and 'masks' subdirectories.
        output_dir (str): Path to the directory where the trained model will be saved.
                          If None, the model will be saved in the input_dir.

    Raises:
        ValueError: If the expected 'images' and 'masks' subdirectories do not exist, or if no training
                    images are found in the 'images' directory.

    Returns:
        None
    """
    click.echo("Training Random Forest segmentation model...")
    
    # Define paths for images and labels (modify as needed)
    images_dir = os.path.join(input_dir, 'images')
    labels_dir = os.path.join(input_dir, 'masks')
    
    if not os.path.isdir(images_dir) or not os.path.isdir(labels_dir):
        raise ValueError("Expected 'images' and 'masks' subdirectories inside input_dir.")
    
    # If no output directory is provided, use input_dir
    if output_dir is None:
        output_dir = input_dir
    os.makedirs(output_dir, exist_ok=True)
    output_model_path = os.path.join(output_dir, 'rf_segmentation_model_wrapper.pkl')
    
    # Use the first image as a test image for feature extraction configuration
    image_files = sorted(os.listdir(images_dir))
    if not image_files:
        raise ValueError("No training images found in the images directory.")
    test_img_path = os.path.join(images_dir, image_files[0])
    
    # Train the segmentation model.
    # The function train_segmentation_model should return a tuple: (model_wrapper, segmentation_result)
    # Here, augmentation, grid search, and duplicate removal are enabled (adjust as needed).
    model_wrapper, _ = train_segmentation_model(
         images_dir=images_dir,
         labels_dir=labels_dir,
         test_img_path=test_img_path,
         output_model_path=output_model_path,
         augmentation=False,
         use_grid_search=True,
         remove_duplicates=True,
         plot=False
    )
    
    # Save the wrapped model (which includes both the classifier and feature extraction parameters)
    joblib.dump(model_wrapper, output_model_path)
    click.echo(f"Random Forest segmentation model trained and saved to {output_model_path}.")
