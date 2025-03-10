from collections.abc import Callable
from functools import partial
import click
import os
import zarr
import cv2
import dask.array as da
import joblib
import numpy as np
import xarray as xr
from skimage.feature import multiscale_basic_features
from skimage.morphology import binary_closing, binary_dilation, binary_erosion

from ..utils.decorators import error_handler

# =============================================================================
# Wrapper Class: Bundles Classifier & Feature Extraction Parameters
# =============================================================================
class SegmentationModelWrapper:
    def __init__(self, classifier, sigma_min: float, sigma_max: float, num_sigma: int = 4):
        self.classifier = classifier
        self.sigma_min = sigma_min
        self.sigma_max = sigma_max
        self.num_sigma = num_sigma

    def extract_features(self, image: np.ndarray) -> np.ndarray:
        """
        Extract multiscale basic features from an RGB image.
        Uses the stored sigma parameters and number of scales.
        """
        features_func = partial(
            multiscale_basic_features,
            intensity=True,
            edges=True,
            texture=False,
            sigma_min=self.sigma_min,
            sigma_max=self.sigma_max,
            num_sigma=self.num_sigma,
            channel_axis=-1,
            num_workers=16
        )
        return features_func(image)

    def predict(self, image: np.ndarray) -> np.ndarray:
        """
        Predict the segmentation for a single RGB image.
        Extracts features and applies the classifier.
        """
        feat = self.extract_features(image)
        H, W = image.shape[:2]
        feat_flat = feat.reshape(-1, feat.shape[-1])
        predictions = self.classifier.predict(feat_flat)
        return predictions.reshape(H, W)


# =============================================================================
# Video Frame Loading Function
# =============================================================================
def load(frame_idx: list[int], video_file: str) -> np.ndarray:
    """
    Load frames from a video file.
    
    Args:
        frame_idx (list[int]): List of frame indices to load.
        video_file (str): Path to the video file.
    
    Returns:
        np.ndarray: Loaded frames as a stack (n_frames, height, width, 3).
    """
    cap = cv2.VideoCapture(video_file)
    if not cap.isOpened():
        raise ValueError(f"Failed to open video file: {video_file}")
    frames = []
    for idx in frame_idx:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if not ret:
            raise ValueError(f"Failed to read frame at index {idx}")
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(frame)
    cap.release()
    return np.stack(frames)


# =============================================================================
# Updated Segmentation Function for Video Frames
# =============================================================================
def segment_frames(frames: int | list[int] | np.ndarray[int],
                   video_file: str,
                   model_wrapper: SegmentationModelWrapper) -> np.ndarray:
    """
    Segment video frames using the provided model wrapper.
    
    Args:
        frames (int | list[int] | np.ndarray[int]): Frame number(s) to process.
        video_file (str): Path to the video file.
        model_wrapper (SegmentationModelWrapper): Wrapped model with classifier and feature parameters.
    
    Returns:
        np.ndarray[int]: Segmented frames with shape (n_frames, height, width).
    """
    batch = load(frames, video_file)
    segmented_frames = []
    for frame in batch:
        segmentation = model_wrapper.predict(frame)
        segmented_frames.append(segmentation)
    segmented_frames = np.array(segmented_frames)

    def postprocess(y_pred):
        binary_erosion(y_pred, out=y_pred)
        binary_erosion(y_pred, out=y_pred)
        binary_dilation(y_pred, out=y_pred)
        binary_dilation(y_pred, out=y_pred)
        binary_closing(y_pred, out=y_pred)
        return y_pred

    segmented_frames = np.array([postprocess(y_pred) for y_pred in segmented_frames], dtype=np.uint8)
    return segmented_frames


def postprocess(y_pred: np.ndarray) -> np.ndarray:
    """
    Apply a series of morphological operations to the segmentation result.
    """
    # Make a copy to avoid modifying in-place if needed.
    y = y_pred.copy()
    binary_erosion(y, out=y)
    binary_erosion(y, out=y)
    binary_dilation(y, out=y)
    binary_dilation(y, out=y)
    binary_closing(y, out=y)
    return y


# -----------------------------------------------------------------------------
# Frame-by-Frame Segmentation without Dask
# -----------------------------------------------------------------------------
@error_handler('Segmentation (random forest)', cluster=False)
def segmentation(dataset: str,
                 weights: str,
                 n_classes: int = 2,
                 cluster_args: dict = None,
                 debug_args: dict = dict({'debug': False, 'debug_visual': False}),
                 ):
    """
    For each chunk defined in the metadata (group 'chunking') of the given Zarr store,
    process the corresponding video file frame-by-frame and store the segmentation output
    incrementally in a subgroup named 'chunk_X' (e.g. 'chunk_0' for the first chunk).
    
    This implementation writes each frame's segmentation directly to disk, avoiding loading the entire
    chunk into memory.
    """
    # Open metadata from the "chunking" group
    chunking_dataset = xr.open_zarr(dataset, group='chunking')
    chunk_times = chunking_dataset.chunk_times.compute()
    chunk_paths = chunking_dataset.chunk_paths.compute()

    # Load the model wrapper from the weights file
    model_wrapper = joblib.load(weights)

    # Open (or create) the Zarr store at the given dataset path
    store = zarr.DirectoryStore(dataset)
    root = zarr.open(store, mode='a')

    # Process each chunk separately
    for chunk_idx, (chunk_time, chunk_path) in enumerate(zip(chunk_times, chunk_paths)):
        start, end = chunk_time.data  # start and end frame indices for this chunk
        video_file = str(chunk_path.data)
        click.echo(f"Segmenting chunk {chunk_idx} from video {video_file} (frames {start} to {end})...")

        # Open video file to determine dimensions and number of frames in this chunk
        cap = cv2.VideoCapture(video_file)
        if not cap.isOpened():
            raise ValueError(f"Failed to open video file: {video_file}")
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        total_frames = end - start
        cap.release()

        # Create (or overwrite) a subgroup for this chunk and allocate a Zarr dataset for segmentation
        chunk_group = root.require_group(f"chunk_{chunk_idx}")
        seg_arr = chunk_group.create_dataset(
            "segmentation",
            shape=(total_frames, height, width),
            chunks=(1, height, width),
            dtype="uint8",
            fill_value=None,
            overwrite=True,
        )
        # Set the dimension metadata so xarray knows the dims
        seg_arr.attrs["_ARRAY_DIMENSIONS"] = ["frame", "x", "y"]
        seg_arr.attrs["chunk_path"] = video_file

        # Re-open the video file to process frames
        cap = cv2.VideoCapture(video_file)
        if not cap.isOpened():
            raise ValueError(f"Failed to open video file: {video_file}")
        cap.set(cv2.CAP_PROP_POS_FRAMES, start)

        # Process frames one by one and write segmentation directly to the Zarr dataset
        for frame_idx in range(total_frames):
            ret, frame = cap.read()
            if not ret:
                click.echo(f"Warning: Could not read frame {start + frame_idx} from video {video_file}. Stopping early.")
                break
            # Convert the frame from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Compute segmentation for the frame
            seg = model_wrapper.predict(frame)
            seg = postprocess(seg)
            # Write the result to disk immediately
            seg_arr[frame_idx, :, :] = seg
        cap.release()

        # Update the chunk group's attributes (consistent with the neuralnet script)
        chunk_group.attrs.update({
            "chunk_idx": chunk_idx,
            "start": start,
            "end": end,
            "img_size": (height, width),
            "model_architecture": "rf",
            "model_weights": weights,
        })

        click.echo(f"Chunk {chunk_idx} segmented and stored in subgroup 'chunk_{chunk_idx}'.")

    # Consolidate metadata so that xarray can read the attributes from the consolidated store
    zarr.consolidate_metadata(dataset)