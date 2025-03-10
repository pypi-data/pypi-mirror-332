from pathlib import Path
import cv2

import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
from skimage.segmentation import mark_boundaries
import dask.array as da
import decord
import click
from matplotlib.widgets import RadioButtons

from .lookup_utils import build_lookup_table, segment_image_with_lookup, kmeans_with_manual_centers, convert
from ..utils.decorators import error_handler


def calibrate_segmentation(video_path: str, calibration_frame: int = 0, test_frame: int = 20,
						   initial_color_space='RGB', n_points_per_cluster=1,
						   debug_args={'debug': False, 'debug_visual': False}) -> np.ndarray:
	
	color_space_choice = initial_color_space
	# Initialize video and frames
	video = cv2.VideoCapture(video_path)
	video.set(cv2.CAP_PROP_POS_FRAMES, calibration_frame)
	ret, frame = video.read()
	calibration_frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	video.set(cv2.CAP_PROP_POS_FRAMES, test_frame)
	ret, frame = video.read()
	test_frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# Initial processing in the selected color space
	calibration_frame_preprocessed = convert(calibration_frame_rgb, initial_color_space)
	selected_centers = []

	# Function to clear and update the image in the chosen color space
	def update_image(color_space):
		nonlocal calibration_frame_preprocessed, color_space_choice
		calibration_frame_preprocessed = convert(calibration_frame_rgb, color_space)
		color_space_choice = color_space
		ax.cla()  # Clear the axes
		ax.imshow(calibration_frame_preprocessed)
		selected_centers.clear()  # Clear selected points on color space change
		fig.canvas.draw()  # Redraw figure

	# Mouse click handler
	def onclick(event):
		# Ignore clicks in zoom/pan mode
		if plt.get_current_fig_manager().toolbar.mode != "":
			return

		if event.inaxes and event.button == 1:
			x, y = int(event.xdata), int(event.ydata)
			color = calibration_frame_preprocessed[y, x]
			selected_centers.append(color)

			# Draw a small green cross at the selected point
			cross_size = 5
			ax.plot([x - cross_size, x + cross_size], [y, y], color="lime", linewidth=1)
			ax.plot([x, x], [y - cross_size, y + cross_size], color="lime", linewidth=1)
			# Draw a white circle around the selected point
			circle = plt.Circle((x, y), 15, color="white", fill=False, linewidth=3)
			ax.add_artist(circle)
			plt.draw()
			print(f"Selected center at ({x}, {y}) with color {color}")

	# Set up figure and interactive elements
	fig, ax = plt.subplots()
	ax.imshow(calibration_frame_preprocessed)
	ax.set_title("Click to select cluster centers (Press 'Q' to finish)")
	fig.canvas.mpl_connect('button_press_event', onclick)

	# Radio buttons for color space selection
	color_spaces = ['RGB', 'HSV', 'Grayscale']
	radio_ax = plt.axes([0.05, 0.7, 0.15, 0.15], facecolor='lightgoldenrodyellow')
	color_radio = RadioButtons(radio_ax, color_spaces)

	def on_color_space_change(label):
		update_image(label)

	color_radio.on_clicked(on_color_space_change)
	plt.show()


	# KMeans clustering with selected points
	segmented_image, labeled_image, kmeans = kmeans_with_manual_centers(calibration_frame_preprocessed, selected_centers, n_points_per_cluster)

	# Display results
	fig, axs = plt.subplots(1, 4, figsize=(20, 10), sharex=True, sharey=True)
	axs[0].imshow(calibration_frame_rgb)
	axs[0].set_title("Original Image")
	axs[0].axis("off")

	axs[1].imshow(segmented_image)
	axs[1].set_title("Segmented Image")
	axs[1].axis("off")

	axs[2].imshow(labeled_image, cmap='viridis')
	axs[2].set_title("Labeled Image")
	axs[2].axis("off")

	axs[3].imshow(mark_boundaries(calibration_frame_rgb, labeled_image == 0, color=(0, 1, 0), mode='thick'))
	axs[3].set_title("Class 0")
	axs[3].axis("off")
	plt.show()

	# Compute lookup table
	lookup_table = build_lookup_table(kmeans, lambda x: convert(x, initial_color_space), n_points_per_cluster)
	if debug_args['debug']:
		click.echo(f'[DEBUG] {np.unique(lookup_table, return_counts=True)=}')

	# Display lookup table
	if debug_args['debug_visual']:
		fig, axs = plt.subplots(4, 4, figsize=(18, 18))
		for i in range(16):
			axs.flatten()[i].imshow(lookup_table[:, :, i], cmap='viridis')
		plt.suptitle("Lookup Table for 4-Bit Quantization")
		plt.show()

	# Segment test frame
	segmented_image = segment_image_with_lookup(test_frame_rgb, lookup_table.flatten())

	# Display test frame results
	fig, axs = plt.subplots(1, 3, figsize=(18, 6))
	axs[0].imshow(test_frame_rgb)
	axs[0].set_title("Original Test Image")
	axs[0].axis("off")
	
	if debug_args['debug']:
		click.echo(f'[DEBUG] {segmented_image.min()=}, {segmented_image.max()=}, {segmented_image.dtype=}, {segmented_image.shape=}')
	axs[1].imshow(segmented_image)
	axs[1].set_title("Segmented Test Image (4-Bit Quantization)")
	axs[1].axis("off")

	axs[2].imshow(mark_boundaries(test_frame_rgb, segmented_image == 0, color=(0, 1, 0), mode='thick'))
	axs[2].set_title("Class 0")
	axs[2].axis("off")
	plt.show()

	if debug_args['debug']:
		click.echo(f'[DEBUG] {color_space_choice=}')
	return lookup_table, color_space_choice



def segment_frames(frames, video_path, lookup_table, frame_shape) -> np.ndarray:
	# Initialize the VideoCapture object
	cap = cv2.VideoCapture(video_path)
	extracted_frames = np.zeros((len(frames), *frame_shape, 3), dtype=np.uint8)

	# Assert that frames is ascending:
	assert np.all(np.diff(frames) == 1), "Frames must be in ascending order."

	# Extract the specified frames
	cap.set(cv2.CAP_PROP_POS_FRAMES, frames[0])
	for i, frame_idx in enumerate(frames):
		ret, frame = cap.read()
		
		if not ret:
			click.secho(f"[Warning] Could not read frame {frame_idx}", fg='yellow')
			continue
		
		# Optionally convert BGR (OpenCV) to RGB if needed by `segment_image_with_lookup`
		extracted_frames[i] = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# Release the VideoCapture object
	cap.release()

	# Segment the frames using the lookup table
	segmented_frames = segment_image_with_lookup(extracted_frames, lookup_table)
	return segmented_frames


def segment_video(video_path, lookup_table, dataset_path, chunk_idx: int=0, color_space='RGB', n_points_per_cluster=1):
	"""
	Processes a video frame-by-frame, applies segmentation, and stores the result in a new xarray dataset.
	
	Parameters:
	- video_path: Path to the input video file.
	- lookup_table: Precomputed lookup table for segmentation.
	- dataset_path: Path to save the xarray dataset using Zarr.
	"""

	vr = decord.VideoReader(video_path)
	num_frames = len(vr)
	frame_shape = vr[0].shape[:2]
	del vr


	blocksize = 150
	frames = (da.arange(num_frames, chunks=(1,))).rechunk((blocksize, -1))

	lookup_table_flattened = lookup_table.flatten()
	predictions = da.map_blocks(segment_frames, frames, video_path, lookup_table_flattened, frame_shape, dtype=np.uint8, chunks=(blocksize, *frame_shape), new_axis=[1, 2])
	predictions = predictions.rechunk((1, *frame_shape))

	# Remove tailing prediction due to blocksize:
	predictions = predictions[:num_frames]

	predictions = xr.DataArray(predictions, dims=['frame', 'x', 'y'], name='segmentation',
											coords={'frame': np.arange(len(predictions))},
											attrs={'chunk_path': video_path,
												   'chunk_idx': chunk_idx, 'img_size': frame_shape,})
	lookup_table = xr.DataArray(lookup_table, dims=['channel1', 'channel2', 'channel3'], name='lookup_table',
								attrs={'color_space': color_space, 'n_points_per_cluster': n_points_per_cluster})
	predictions.to_zarr(dataset_path, group=f'chunk_{chunk_idx}', mode='w')
	lookup_table.to_zarr(dataset_path, group=f'chunk_{chunk_idx}', mode='a')


@error_handler('Segmentation (lookup-table)', cluster=True)
def segmentation(dataset: str, weights: str = None, n_classes:int=None, n_points_per_cluster: int=1, 
				 debug_args={'debug': False, 'debug_visual': False}, **kwargs):
	video_path = xr.open_zarr(dataset, 'chunking').chunk_paths.data.compute()[0]

	if weights:
		click.echo(f'Using lookup-table from {weights}.')
		x = np.load(weights, allow_pickle=True)
		weights, color_space = x['weights'], x['color_space']
	else:
		click.echo('Creating lookup-table.')
		weights, color_space = calibrate_segmentation(video_path, calibration_frame=0, test_frame=20, n_points_per_cluster=n_points_per_cluster,
													  debug_args=debug_args)
		file_path = str(Path(dataset).parent / 'lookup_table')
		np.savez(file_path, allow_pickle=True, weights=weights, color_space=color_space)

	n_chunks = xr.open_zarr(dataset, group='chunking').sizes['chunk']
	for chunk_idx in range(n_chunks):
		click.echo(f'Segmenting chunk {chunk_idx}...')
		segment_video(video_path, weights, dataset, chunk_idx=chunk_idx, color_space=color_space, n_points_per_cluster=n_points_per_cluster)
