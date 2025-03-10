import os
from collections import namedtuple
from pathlib import Path
from typing import Callable

import click
import cv2
import dask
import dask.array as da
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from tqdm import tqdm
import moving_least_squares
import numpy as np
import xarray as xr
import zarr
from cv2 import calcOpticalFlowPyrLK, warpAffine
from dask.diagnostics import ProgressBar
from matplotlib.colors import Normalize
from scipy.spatial import KDTree
from skimage.measure import label, regionprops

from ..utils.decorators import error_handler


coordinate = namedtuple('coordinate', ['x', 'y'])


def detect_points_to_track(segmented_image: np.ndarray, offset_percentage: float=0.075, max_num_points_to_detect: int=1_000,
						   min_num_points_to_detect: int=40, grid_size: int=16, eccentricity: float=0.7, solidity: float=0.7,
						   min_area: int=40, max_area: int=1_000, debug_visual: bool=False, debug: bool=False,) -> np.ndarray:
	"""
	Detect and filter chromatophore centers in a segmented image, then distribute them evenly across a grid.

	This function processes a segmented image to identify chromatophore centers, filters them based on
	shape properties, and then redistributes them to achieve a more even spatial distribution.

	Parameters:
	-----------
	segmented_image : np.ndarray
		A binary segmented image where chromatophores are represented as non-zero pixels.
	offset_percentage : float, optional
		Percentage of image dimensions to use as an offset from the edges (default is 0.075).
	max_num_points_to_detect : int, optional
		Maximum number of points to detect, used to determine grid size (default is 1000).
	min_num_points_to_detect : int, optional
		Minimum number of points that need to be detected (default is 40).
	grid_size : int, optional
		Size of the grid used to distribute chromatophores (default is 16).
	eccentricity : float, optional
		Maximum eccentricity threshold for filtering chromatophores (default is 0.7).
	solidity : float, optional
		Minimum solidity threshold for filtering chromatophores (default is 0.7).
	min_area : int, optional
		Minimum area threshold for filtering chromatophores (default is 40).
	max_area : int, optional
		Maximum area threshold for filtering chromatophores (default is 1000).
	debug_visual : bool, optional
		If True, displays debug visualizations of the detection process (default is False).
	debug : bool, optional
		If True, prints debug information (default is False).

	Returns:
	--------
	np.ndarray
		An array of evenly spaced chromatophore centers as (x, y) coordinates.

	Raises:
	-------
	AssertionError: If not enough chromatophores are detected

	Notes:
	------
	1. Calculates an offset to exclude image edges from processing.
	2. Identifies and labels regions in the segmented image.
	3. Filters regions based on eccentricity, solidity, and area thresholds.
	4. Creates a grid of points across the image.
	5. Maps grid points to the nearest chromatophore centers.
	6. Returns a unique set of chromatophore centers distributed across the grid.

	The function uses regionprops for feature extraction, KDTree for efficient nearest neighbor search,
	and optionally matplotlib for visualization.
	"""
	
	offset = coordinate(int(segmented_image.shape[0] * offset_percentage), int(segmented_image.shape[1] * offset_percentage))
	props = regionprops(label(segmented_image[offset.x:-offset.x, offset.y:-offset.y]), offset=offset)
	filtered_props = list(filter(lambda x: x.eccentricity < eccentricity and x.solidity > solidity and x.area >= min_area and x.area <= max_area, props))
	round_chromatophore_centers = np.array([x.centroid for x in filtered_props])

	assert round_chromatophore_centers.shape[0] >= min_num_points_to_detect, f'Not enough chromatophores detected ({len(round_chromatophore_centers)} < {min_num_points_to_detect}).'
	x_grid, y_grid = np.meshgrid(np.linspace(offset.x, segmented_image.shape[0]-offset.x, (segmented_image.shape[0] - 2*offset.x) // grid_size), np.linspace(offset.y, segmented_image.shape[1]-offset.y, (segmented_image.shape[1] - 2*offset.y) // grid_size))
	
	tree = KDTree(round_chromatophore_centers)
	_, index = tree.query(list(zip(x_grid.ravel(), y_grid.ravel())), k=1)
	grid_chromatophore_centers = np.unique(round_chromatophore_centers[index], axis=0)[...,::-1]

	if grid_chromatophore_centers.shape[0] > max_num_points_to_detect:
		click.secho(f'[WARNING] Too many chromatophores detected ({grid_chromatophore_centers.shape[0]} > {max_num_points_to_detect}).' + \
			  	     'Taking random sample. Consider increasing grid size or `max_num_points_to_detect` threshold', bold=True)
		grid_chromatophore_centers = grid_chromatophore_centers[np.random.choice(grid_chromatophore_centers.shape[0], max_num_points_to_detect, replace=False)]

	if debug_visual:
		fig, ax = plt.subplots(1, 3, sharex=True, sharey=True)
		for axis in ax:
			axis.imshow(segmented_image, cmap='binary')
			axis.axis('off')
		ax[0].scatter([p.centroid[1] for p in props], [p.centroid[0] for p in props], c='r')
		ax[1].scatter([round_chromatophore_centers[:, 1]], [round_chromatophore_centers[:, 0]], c='r')
		ax[1].scatter(y_grid, x_grid, c='b', marker='+')
		ax[2].scatter([grid_chromatophore_centers[:, 0]], [grid_chromatophore_centers[:, 1]], c='r')
		ax[0].set_title('Detected chromatophore centers')
		ax[1].set_title('Filtered (round) chromatophore centers')
		ax[2].set_title('~Evenly spaced chromatophore centers')
		plt.tight_layout()
		plt.show()
	
	return grid_chromatophore_centers.astype('float32')


def track_points(gray0: np.ndarray, gray1: np.ndarray, points: np.ndarray, window_size: int=21, max_distance: float=100,
				 debug: bool=False, debug_visual: bool=False) -> tuple[np.ndarray]:
	"""
	Track points between two consecutive frames using optical flow.

	This function uses the Lucas-Kanade method with pyramids to track a set of points
	from one frame to the next in a video sequence.

	Parameters:
	-----------
	gray0 : np.ndarray
		The first frame (previous frame) of the video sequence in grayscale.
	gray1 : np.ndarray
		The second frame (current frame) of the video sequence in grayscale.
	points : np.ndarray
		An array of points to track, specified as (x, y) coordinates.
	window_size : int, optional
		Size of the search window at each pyramid level (default is 21).
	max_distance : float, optional
		Maximum distance (in pixels) points are allowed to move between frames.
	debug : bool, optional
		If True, prints debug information about the tracking process (default is False).
	debug_visual : bool, optional
		If True, displays a visual representation of the tracking results (default is False).

	Returns:
	--------
	tuple
		A tuple containing:
		- np.ndarray: The original points that were successfully tracked.
		- np.ndarray: The new positions of the tracked points in the second frame.
		- np.ndarray: A boolean array indicating which points were successfully tracked.

	Raises:
	-------
	ValueError: If no points were tracked.

	Notes:
	------
	1. Applies the Lucas-Kanade optical flow method to track points between frames.
	2. Filters out points that couldn't be tracked successfully.

	The function uses OpenCV's calcOpticalFlowPyrLK for point tracking and matplotlib
	for optional result visualization.
	"""
	
	points_moved, status, err = calcOpticalFlowPyrLK(gray0, gray1, points, None, winSize=(window_size, window_size), maxLevel=3)
	if status is None or status[:, 0].sum() <= 0.75 * len(points):
		click.secho(f'[WARNING] Less than 75% of points were tracked ({status[:, 0].sum()}/{len(points)}). Retrying with smaller window size.', bold=True)
		points_moved, status, err = calcOpticalFlowPyrLK(gray0, gray1, points, None, winSize=(window_size//2, window_size//2), maxLevel=3)
	if status is None:
		raise ValueError(f'No points were tracked.\n{err=}')
	status = status[:, 0].astype(bool)

	distances = np.linalg.norm(points - points_moved, axis=1)
	small_enough = distances < max_distance
	status = status & small_enough
	if debug_visual:
		points_old = points.copy()
	points, points_moved = points[status], points_moved[status]


	if debug:
		click.secho(f'[DEBUG] {len(points)} of {len(status)} points found in next frame ({100 * len(points) / len(status):.2f}% found; {100 * sum(small_enough) / len(small_enough):.2f}% nearby).', italic=True)
	if debug_visual and status.mean() < 0.9:
		fig, ax = plt.subplots(1, 2, sharex=True, sharey=True)
		for axis in ax:
			axis.axis('off')
		ax[0].imshow(gray0, cmap='binary')
		ax[1].imshow(gray1, cmap='binary')
		ax[0].scatter(points_old[:, 0], points_old[:, 1], c='r', marker='+', s=300, lw=3)
		ax[0].scatter(points[:, 0], points[:, 1], c='lime', marker='+', s=300, lw=3)
		ax[1].plot([points[:, 0], points_moved[:, 0]], [points[:, 1], points_moved[:, 1]], c='dodgerblue', lw=3)
		ax[1].scatter(points[:, 0], points[:, 1], c='dodgerblue', marker='+', s=300, lw=3)
		ax[1].scatter(points_moved[:, 0], points_moved[:, 1], c='lime', marker='+', s=300, lw=3)
		ax[0].set_title('Previous frame')
		ax[1].set_title('Next frame')
		plt.tight_layout()
		plt.show()
	return points, points_moved, status


def track_grid(frame_shape: np.ndarray|tuple, points: np.ndarray, points_moved: np.ndarray, grid_size: int=64, alpha: float=3) -> tuple[np.ndarray, np.ndarray]:
	"""
	Track a grid of points using Moving Least Squares (MLS) deformation.

	This function applies the MLS deformation to track a grid of points between two frames,
	based on the movement of a set of tracked points.

	Parameters:
	-----------
	frame_shape : np.ndarray or tuple
		The shape of the frame (height, width).
	points : np.ndarray
		The original positions of tracked points.
	points_moved : np.ndarray
		The new positions of tracked points.
	grid_size : int, optional
		The size of the grid cells (default is 64).
	alpha : float, optional
		The alpha parameter for MLS deformation (default is 3).

	Returns:
	--------
	tuple
		A tuple containing two np.ndarrays:
		- pullback_warped: The backward (pullback) deformation map.
		- pushforward_warped: The forward (pushforward) deformation map.

	Notes:
	------
	1. Creates a grid based on the frame shape and grid size.
	2. Applies MLS deformation to compute pushforward and pullback transformations.
	3. Scales up the transformation maps to match the original frame size.
	4. Converts the maps to the format required by OpenCV's remap function.

	The function uses the moving_least_squares module for similarity transformations
	and OpenCV for affine warping and map conversion.
	"""

	grid = np.dstack(np.meshgrid(*tuple(np.arange(0, s + 1, grid_size) for s in reversed(frame_shape)))).astype('float32')
	if isinstance(points, da.Array):
		points = points.compute()
	if isinstance(points_moved, da.Array):
		points_moved = points_moved.compute()
	if isinstance(points, xr.DataArray):
		points = points.data
	if isinstance(points_moved, xr.DataArray):
		points_moved = points_moved.data
	pushforward = moving_least_squares.similarity(points_moved, points, grid.reshape((-1, 2)), alpha=alpha).reshape(grid.shape)
	pullback = moving_least_squares.similarity(points, points_moved, grid.reshape((-1, 2)), alpha=alpha).reshape(grid.shape)

	return pullback, pushforward


def visualize_trajectories(chunk: xr.Dataset, tail_length: int=30, color: str='blue') -> None:
	"""
	Visualize point trajectories over a video or blank background.

	This function creates an animation of point trajectories, optionally overlaid on a video.

	Parameters:
	-----------
	trajectories : xr.DataArray
		An xarray DataArray containing point trajectories.
	output_path : str
		Path where the output video will be saved.
	video_path : str, optional
		Path to the background video file (default is None).
	fps : int, optional
		Frames per second for the output video (default is 30).
	tail_length : int, optional
		Number of frames to show in the trajectory tail (default is 30).
	color : str, optional
		Color of the trajectory points and lines (default is 'blue').

	Returns:
	--------
	None

	Notes:
	------
	1. Sets up the plot based on video dimensions or trajectory bounds.
	2. Creates an animation showing points moving along their trajectories.
	3. Optionally overlays the animation on a background video.
	4. Uses a trailing effect to show recent trajectory history.
	5. Saves the animation as a video file.

	The function uses matplotlib for plotting and animation, and OpenCV for video reading.
	"""

	fig, ax = plt.subplots(figsize=(10, 8))

	video = chunk.segmentation.attrs['chunk_path']  # Alternqtively, use 'chunk_path' attribute
	trajectories = chunk.points_trajectories.data.compute()
	output = Path(video)

	output_path = output.with_suffix('.tracking_trajectories.mp4')

	if video:
		cap = cv2.VideoCapture(video)
		ret, frame = cap.read()
		if not ret:
			raise ValueError("Failed to read the video file.")
		height, width = frame.shape[:2]
		ax.set_xlim(0, width)
		ax.set_ylim(height, 0)
	else:
		ax.set_xlim(trajectories.sel(coordinate='x').min().item(), 
					trajectories.sel(coordinate='x').max().item())
		ax.set_ylim(trajectories.sel(coordinate='y').max().item(), 
					trajectories.sel(coordinate='y').min().item())
	
	background = ax.imshow(cap.read()[1]) if video else None
	points = [ax.plot([], [], marker='o', color=color, markersize=4)[0] for _ in range(trajectories.shape[1])]
	trails = [ax.plot([], [], '-', color=color, alpha=0.5, linewidth=1)[0] for _ in range(trajectories.shape[1])]
	
	def update(frame):
		if video:
			cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
			ret, img = cap.read()
			if ret:
				background.set_array(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
		
		for i, (point, trail) in enumerate(zip(points, trails)):
			x = trajectories[frame, point, 0]
			y = trajectories[frame, point, 1]
			point.set_data([x], [y])
			
			# start_frame = max(0, frame - tail_length)
			# trail_x = trajectories.sel(frame=slice(start_frame, frame), point=i, coordinate=0)
			# trail_y = trajectories.sel(frame=slice(start_frame, frame), point=i, coordinate=1)
			# trail.set_data(trail_x, trail_y)
			# exit()
		
		ax.set_title(f'Frame: {frame}')
		return [background] + points + trails if background else points + trails
	
	if video:
		dpi = 100
		fig.set_size_inches(width/dpi, height/dpi)
	
	writer = animation.FFMpegWriter(fps=20, metadata=dict(artist='SOFTWARE_NAME'), bitrate=1800)
	
	with writer.saving(fig, output_path, dpi=100):
		for frame in tqdm(range(trajectories.shape[0]), desc="Visualizing Trajectories"):
			update(frame)
			writer.grab_frame()
	
	plt.close(fig)
	if video:
		cap.release()


def warp_frame(image: np.ndarray|list[np.ndarray], maps: np.ndarray, border_value: int=255, grid_size: int=32, frame_shape: tuple=(1, 1)) -> np.ndarray|list[np.ndarray]:
	"""
	Warp an image or tuple of images using provided mapping.

	This function applies a geometric transformation to an image or tuple of images
	using the provided mapping.

	Parameters:
	-----------
	image : np.ndarray or tuple of np.ndarray
		The input image(s) to be warped.
	maps : np.ndarray
		The mapping to be applied for the warping.
	border_value : int, optional
		Value to fill borders after warping (default is 255).

	Returns:
	--------
	np.ndarray or tuple of np.ndarray
		The warped image(s).

	Notes:
	------
	1. Uses OpenCV's remap function to apply the warping.
	2. Handles both single numpy arrays and tuples of numpy arrays as input.
	3. Uses nearest neighbor interpolation and constant border mode.

	Raises a ValueError if the input type is not supported.
	"""

	scale_up_transform = np.array([
				[grid_size, 0, 0],
				[0, grid_size, 0],
			], 'float32')
	maps = warpAffine(maps, scale_up_transform, frame_shape[::-1], flags=cv2.INTER_LINEAR)
	
	if isinstance(image, np.ndarray) or isinstance(image, da.Array):
		return cv2.remap(image, maps, None, interpolation=cv2.INTER_NEAREST, borderMode=cv2.BORDER_CONSTANT, borderValue=border_value)
	elif isinstance(image, list):
		return list(cv2.remap(i, maps, None, interpolation=cv2.INTER_NEAREST, borderMode=cv2.BORDER_CONSTANT, borderValue=border_value) for i in image)
	else:
		raise ValueError(f'Invalid input type of image {type(image)}.')
	
	

def compute_distance_map(flow: np.ndarray) -> np.ndarray:
	"""
	Compute a distance map from an optical flow field.

	This function calculates the Euclidean distance between each pixel's position
	and its mapped position according to the optical flow.

	Parameters:
	-----------
	flow : np.ndarray
		The optical flow field, typically of shape (height, width, 2).

	Returns:
	--------
	np.ndarray
		A 2D array representing the distance each pixel has moved.

	Notes:
	------
	1. Creates a grid of coordinates matching the flow field dimensions.
	2. Computes the Euclidean distance between original and mapped positions.
	"""
	h, w = flow.shape[:2]
	y, x = np.mgrid[:h, :w]
	distances = np.sqrt(np.sum((flow - np.dstack([x, y]))**2, axis=2))
	return distances


def remove_border(array: np.ndarray, border_fraction: float=0.1) -> np.ndarray:
	"""
	Remove the border region from a 2D or 3D numpy array.

	This function crops the border of an input array by a specified fraction.

	Parameters:
	-----------
	array : np.ndarray
		The input array to be cropped (2D or 3D).
	border_fraction : float, optional
		The fraction of each dimension to remove as border (default is 0.1).

	Returns:
	--------
	np.ndarray
		The input array with borders removed.

	Notes:
	------
	1. Handles both 2D and 3D arrays.
	2. Calculates border size based on the input fraction.
	3. Returns a view of the original array, not a copy.
	"""

	if array.ndim == 3:
		h, w, c = array.shape
		h_border = int(h * border_fraction)
		w_border = int(w * border_fraction)
		return array[h_border:-h_border, w_border:-w_border, :]
	elif array.ndim == 2:
		h, w = array.shape
		h_border = int(h * border_fraction)
		w_border = int(w * border_fraction)
		return array[h_border:-h_border, w_border:-w_border]


def visualize_flow_distance(chunk: xr.Dataset, border_fraction: float=0.1):
	"""
	Visualize the distance map of optical flow over time.

	This function creates an animation of the distance map derived from optical flow,
	showing how pixels move over a sequence of frames.

	Parameters:
	-----------
	flow_array : np.ndarray
		A 4D array of optical flow data (frames, height, width, 2).
	output_path : str
		Path where the output video will be saved.
	fps : int, optional
		Frames per second for the output video (default is 30).
	border_fraction : float, optional
		Fraction of border to remove from each frame (default is 0.1).

	Returns:
	--------
	None

	Notes:
	------
	1. Computes distance maps for all frames, removing borders.
	2. Creates an animation of these distance maps over time.
	3. Uses a consistent color scale across all frames.
	4. Saves the animation as a video file with a progress bar.

	The function uses matplotlib for plotting and animation, and tqdm for progress tracking.
	"""

	fig, ax = plt.subplots(figsize=(10, 8))
	plt.close()  # Prevent display of the empty figure
	
	video = chunk.segmentation.attrs['chunk_path']  # Alternqtively, use 'chunk_path' attribute
	nr_frames = chunk.sizes['frame']
	flow_array = chunk.pullbacks.data.compute()
	output = Path(video)

	output_path = output.with_suffix('.tracking_trajectories.mp4')
	
	# Remove border and compute distance maps for all frames
	distance_maps = np.array([
		compute_distance_map(remove_border(flow, border_fraction))
		for flow in flow_array
	])
	distance_maps[0] = 0
	
	# Set up normalization for consistent color scaling, using only values inside borders
	vmin = distance_maps.min()
	vmax = distance_maps.max()
	norm = Normalize(vmin=vmin, vmax=vmax)
	
	# Initialize the plot
	im = ax.imshow(distance_maps[0], cmap='viridis', norm=norm, animated=True)
	plt.colorbar(im, ax=ax, label='Distance')
	ax.set_title('Flow Distance Map')
	ax.axis('off')  # Hide axes for cleaner visualization
	
	def update(frame):
		im.set_array(distance_maps[frame])
		ax.set_title(f'Flow Distance Map - Frame {frame}')
		return [im]
	
	# Create the animation
	anim = animation.FuncAnimation(fig, update, frames=nr_frames, blit=True)
	
	# Set up the writer with progress bar
	writer = animation.FFMpegWriter(fps=20, metadata=dict(artist='Me'), bitrate=1800)
	
	# Save the animation with progress bar
	with tqdm(total=nr_frames, desc="Visualizing Flow Distance") as pbar:
		anim.save(output_path, writer=writer, progress_callback=lambda i, n: pbar.update(1))
	
	plt.close(fig)
	plt.close()


def generate_masterframe_and_videos(chunk: xr.DataArray, grid_size: int, videos: bool=True):
	"""
	Generate a masterframe and average frame from a video chunk, applying registration.

	This function processes a chunk of video frames, applies registration using pullback maps,
	and generates a masterframe (average segmentation) and chunk average (average color frame).

	Parameters:
	-----------
	chunk : xarray.DataArray
		A chunk of segmented video frames.
	pullbacks : xarray.DataArray
		Pullback maps for frame registration.
	input_video_path : str
		Path to the input video file.
	create_videos : bool, optional
		If True, creates registered segmentation and video files (default is True).
	output : str, optional
		Base path for output files (default is '').

	Returns:
	--------
	tuple
		A tuple containing:
		- masterframe: The average segmentation frame.
		- chunkaverage: The average color frame.
		- registered_segmentation_path: Path to the registered segmentation video (if created).
		- registered_video_path: Path to the registered video (if created).

	Notes:
	------
	1. Reads frames from the input video.
	2. Applies pullback maps to register each frame.
	3. Accumulates registered frames to create masterframe and chunk average.
	4. Optionally creates videos of the registered segmentation and frames.
	5. Uses tqdm for progress tracking.

	The function uses OpenCV for video reading and writing, and custom warp_frame function
	for applying the registration.
	"""

	frame_shape = (chunk.sizes['x'], chunk.sizes['y'])
	nr_frames = chunk.sizes['frame']
	video = chunk.segmentation.attrs['chunk_path']
	output = Path(video)

	# Ensure the output directory exists
	os.makedirs(str(output.parent), exist_ok=True)

	if videos:
		registered_segmentation_path = output.with_suffix('.registered_segmentation.mp4')
		registered_video_path = output.with_suffix('.registered_video.mp4')
		registered_segmentation = cv2.VideoWriter(registered_segmentation_path, cv2.VideoWriter_fourcc(*'mp4v'), 20, frame_shape[::-1], isColor=False)
		registered_video = cv2.VideoWriter(registered_video_path, cv2.VideoWriter_fourcc(*'mp4v'), 20, frame_shape[::-1], isColor=True)

		masterframe = np.zeros(frame_shape, dtype='int64')
		chunkaverage = np.zeros(frame_shape + (3,), dtype='int64')

		cap = cv2.VideoCapture(video)

		# Process and warp each frame
		with click.progressbar(range(nr_frames), label="Warping Frames", ) as frames:
			for frame_idx in frames:
				ret, img = cap.read()
				if not ret:
					raise ValueError(f"Error reading frame {frame_idx} from video.")

				segmentation_frame = (255 * (chunk.segmentation.isel(frame=frame_idx).data.compute() > 0)).astype(np.uint8)

				pullback_map = chunk.pullbacks.isel(frame=frame_idx).data.compute()
				warped_segmentation, warped_image = warp_frame([segmentation_frame, img],
															pullback_map, grid_size=grid_size, frame_shape=frame_shape)
				
				registered_segmentation.write((255 - warped_segmentation).astype(np.uint8))
				registered_video.write(warped_image.astype(np.uint8))

				masterframe += (warped_segmentation > 125).astype(np.int64)
				chunkaverage += warped_image.astype(np.int64)
	
		registered_segmentation.release()
		registered_video.release()

		masterframe = masterframe.astype(np.float64) / nr_frames
		chunkaverage = (chunkaverage / nr_frames).astype(np.uint8)

		chunkaverage = cv2.cvtColor(chunkaverage, cv2.COLOR_BGR2RGB)

		masterframe = xr.DataArray(masterframe, name='masterframe', dims=('x', 'y'), coords={'x': range(frame_shape[0]), 'y': range(frame_shape[1])})	
		chunkaverage = xr.DataArray(chunkaverage, name='chunkaverage', dims=('x', 'y', 'channel'), coords={'x': range(frame_shape[0]), 'y': range(frame_shape[1]), 'channel': ['r', 'g', 'b']})
	else:		
		blocksize = 100

		def warp_block(X_block, Y, block_info=None):
			block_idx = block_info[0]['chunk-location'][0]
			Y_block = Y[block_idx * blocksize: (block_idx + 1) * blocksize]
			
			Z_block = np.zeros_like(X_block, dtype='float16')
			for i in range(blocksize):
				try:
					Z_block[i] = warp_frame((X_block[i] > 0).astype('uint8'), Y_block[i], grid_size=grid_size, frame_shape=frame_shape, border_value=0).astype('float16')
				except IndexError:
					pass
			return Z_block

		# Apply map_blocks with a custom processing function
		masterframe = da.map_blocks(
			warp_block,
			chunk.segmentation.chunk({'frame': blocksize}).data,
			dtype="float16",
			Y = chunk.pullbacks.chunk({'frame': blocksize}).data,
		)

		masterframe = da.mean(masterframe, axis=0).astype(float)

		masterframe = xr.DataArray(masterframe, name='masterframe', dims=('x', 'y'), coords={'x': range(frame_shape[0]), 'y': range(frame_shape[1])})
		chunkaverage = None

	return masterframe, chunkaverage


def track_points_trajectories(chunk: xr.DataArray, original_points_to_track: np.ndarray, track_points: Callable=track_points,
							  window_size: int=21,  max_distance: float=10,
							  debug: bool=False, debug_visual: bool=False) -> xr.DataArray:
	
	video_path = chunk.segmentation.attrs['chunk_path']
	cap = cv2.VideoCapture(video_path)

	points = original_points_to_track.copy().astype('float32') #* 0.25
	points_trajectories = [points]

	ret, frame0 = cap.read()
	if not ret:
		click.secho(f'[ERROR] Could not open the video file {video_path} with OpenCV.', bold=True)
		raise ValueError("Failed to read the video file.")
	is_rgb_video = frame0.ndim == 3

	if is_rgb_video:
		frame0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)
	
	# frame0 = cv2.resize(frame0, (0, 0), fx=0.25, fy=0.25)

	points_trajectories = np.zeros((chunk.sizes['frame'], points.shape[0], 2), dtype='float32')
	points_trajectories[0] = points.astype('float32')
	original_status = np.ones(points.shape[0], dtype=bool)

	with click.progressbar(range(1, chunk.sizes['frame']), label='Tracking points') as frames:
		for frame_idx in frames:
			ret, frame1 = cap.read()
			if not ret:
				click.secho(f'[ERROR] Could not read frame {frame_idx} from the video file {video_path}.', bold=True)
				raise ValueError("Failed to read the video file.")
		
			if is_rgb_video:
				frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
			
			# frame1 = cv2.resize(frame1, (0, 0), fx=0.25, fy=0.25)
			
			points, points_moved, status = track_points(
				frame0, frame1, points, debug=debug, debug_visual=debug_visual, window_size=window_size, max_distance=max_distance
			)
			original_status[original_status] = status
			points_trajectories[frame_idx][original_status] = points_moved.astype('float32')

			points = points_moved
			frame0 = frame1

	points_trajectories = xr.DataArray(
		points_trajectories[:, original_status],
		name='points_trajectories',
		dims=('frame', 'point', 'coordinate'), 
		coords={'frame': range(chunk.sizes['frame']), 'point': range(int(np.sum(original_status))), 'coordinate': ['x', 'y']}
	)

	return points_trajectories


def compute_pullbacks_pushforwards(chunk: xr.DataArray, grid_size: int = 16, mls_alpha: float=3.0, compute: bool=False) -> tuple[xr.DataArray, xr.DataArray]:
	"""
	Compute pullback and pushforward deformation maps based on point trajectories using Dask for parallelization.

	This function generates pullback and pushforward deformation maps for each frame
	in a video sequence, based on tracked point trajectories. It uses Dask for parallel
	computation, allowing for efficient processing of large datasets.

	Parameters:
	-----------
	points_trajectories : xr.DataArray
		Trajectories of tracked points across frames.
	chunk : xr.DataArray
		A chunk of video data, used for determining frame dimensions.
	grid_size : int, optional
		Size of the grid used in deformation computation (default is 16).
	compute : bool, optional
		If True, immediately compute and return results. If False, return lazy Dask arrays (default is False).

	Returns:
	--------
	tuple
		A tuple containing two xr.DataArrays:
		- pullbacks: Pullback deformation maps for each frame.
		- pushforwards: Pushforward deformation maps for each frame.
		If compute is False, these are lazy Dask arrays.

	Notes:
	------
	1. Converts input trajectories to a Dask array for parallel processing.
	2. Uses the first frame's points as the reference for all deformations.
	3. Applies the track_grid function to chunks of frames in parallel.
	4. Separates results into pullback and pushforward maps.
	5. Returns results as xarray DataArrays with appropriate dimensions and coordinates.
	6. Optionally computes results immediately if compute is True.

	The function assumes that the track_grid function is available and computes
	both pullback and pushforward mappings for a single frame.
	"""
	
	frame_shape = (chunk.sizes['x'], chunk.sizes['y'])
	nr_frames = chunk.sizes['frame']


	original_points = chunk.points_trajectories.isel(frame=0).data.compute()
	
	def _track_grid(points_moved):
		results = []
		for p in points_moved:
			pullback, pushforward = track_grid(frame_shape, original_points, p, grid_size=grid_size, alpha=mls_alpha)
			results.append((pullback, pushforward))
		
		return np.array(results, dtype='float32')
	
	# Apply the process_chunk function to each chunk of frames
	maps_shape = np.ceil((np.array(frame_shape) + 1) / grid_size).astype(int)
	results = da.map_blocks(_track_grid,
							da.from_array(chunk.points_trajectories.data.compute(), chunks=(1, -1, 2)),
							dtype='float32',
							chunks=(1, 2, *maps_shape, 2),
							new_axis=[2, 3, 4],
							drop_axis=[2])

	pullbacks = results[:, 0]
	pushforwards = results[:, 1]

	# Convert back to xarray DataArrays
	pullbacks = xr.DataArray(pullbacks, name='pullback', dims=('frame', 'x_grid', 'y_grid', 'coordinate'),
							 coords={'frame': range(nr_frames), 'coordinate': ['x', 'y'], 'x_grid': range(maps_shape[0]), 'y_grid': range(maps_shape[1])})
	pushforwards = xr.DataArray(pushforwards, name='pushforward', dims=('frame', 'x_grid', 'y_grid', 'coordinate'),
								coords={'frame': range(nr_frames), 'coordinate': ['x', 'y'], 'x_grid': range(maps_shape[0]), 'y_grid': range(maps_shape[1])})
	
	if compute:
		with ProgressBar():
			pullbacks, pushforwards = dask.compute(pullbacks, pushforwards)

	return pullbacks, pushforwards


def optical_flow(chunk: xr.Dataset, track_grid_size: int=32, window_size: int=21, max_distance: int=10,
				 min_num_points_to_detect: int=40, max_num_points_to_detect: int = 400,
				 min_area: int=40, max_area: int=1_000, eccentricity: float=0.7, solidity: float=0.7,
				 debug: bool=False, debug_visual: bool=False,) -> xr.Dataset:
	point_detection_frame = 0
	while (chunk.segmentation.sel(frame=point_detection_frame) > 0).mean().compute() < 0.05:
		click.secho(f'[WARNING] Skipping frame {point_detection_frame} for point detection due to low segmentation coverage (less than 5%).', bold=True, fg='yellow')
		point_detection_frame += 1
	click.secho(f'Point detection frame {point_detection_frame} has {100*(chunk.segmentation.sel(frame=point_detection_frame) > 0).mean().compute():.3f}% segmentation coverage.')
	click.secho(f'Trying to find between {min_num_points_to_detect} and {max_num_points_to_detect} points.')
	
	original_points_to_track = detect_points_to_track(chunk.segmentation.sel(frame=point_detection_frame).data.compute() > 0, debug_visual=debug_visual, max_num_points_to_detect=max_num_points_to_detect,
												      min_num_points_to_detect=min_num_points_to_detect, grid_size=track_grid_size, min_area=min_area, max_area=max_area, debug=debug,
												      eccentricity=eccentricity, solidity=solidity)
	
	points_trajectories = track_points_trajectories(chunk, original_points_to_track, track_points, window_size, max_distance,
												    debug=debug, debug_visual=debug_visual)

	return points_trajectories


def interpolate_maps(chunk: xr.Dataset, interpolate_grid_size: int=16, mls_alpha: float=3.0) -> tuple[xr.DataArray]:
	pullbacks, pushforwards = compute_pullbacks_pushforwards(chunk, grid_size=interpolate_grid_size, mls_alpha=mls_alpha)
	
	pullbacks = xr.DataArray(pullbacks, name='pullback', dims=('frame', 'x_grid', 'y_grid', 'coordinate'),
							 attrs={'grid_size': interpolate_grid_size, 'mls_alpha': mls_alpha},
						     coords={'frame': range(pullbacks.shape[0]), 'x_grid': range(pullbacks.shape[1]), 'y_grid': range(pullbacks.shape[2]), 'coordinate': range(2)})
	pushforwards = xr.DataArray(pushforwards, name='pushforwards', dims=('frame', 'x_grid', 'y_grid', 'coordinate'),
							    attrs={'grid_size': interpolate_grid_size, 'mls_alpha': mls_alpha},
								coords={'frame': range(pushforwards.shape[0]), 'x_grid': range(pushforwards.shape[1]), 'y_grid': range(pushforwards.shape[2]), 'coordinate': range(2)})
	return pullbacks, pushforwards


@error_handler('Registration')
def registration(dataset: str, min_num_points_to_detect: int=40, max_num_points_to_detect: int = 400, 
			 	 window_size: int=21, track_grid_size: int=32, interpolate_grid_size: int=16,
				 max_distance: int=10, mls_alpha: float=3.0,
			     compute_videos: bool=False, masterframe_only: bool=False,
				 detection_args={'min_area': 40, 'max_area': 1_000, 'eccentricity': 0.7, 'solidity': 0.7},
				 cluster_args={'processes': False, 'n_workers': 1, 'threads_per_worker': 4},
				 debug_args={'debug': False, 'debug_visual': False}) -> None:

	chunknames = [chunk for chunk in zarr.open(dataset).keys() if chunk.startswith('chunk_')]
	chunks = [xr.open_zarr(dataset, group=chunk) for chunk in chunknames]
	if not chunks:
		click.secho("No chunks found in the provided data group. Have you run segmentation yet?", fg='red', bold=True)
		return False
	click.echo(f'Processing {len(chunks)} chunks.')

	zarr_store = zarr.open(dataset, mode='a')
	for chunkname in chunknames:
		for var in ['points_trajectories', 'pullbacks', 'pushforwards', 'coordinate', 'point', 'x_grid', 'y_grid', 'masterframe', 'chunkaverage']:
			if var in zarr_store[chunkname]:
				click.secho(f'WARNING: Removing {var} from {chunkname} since it already exists.', italic=True)
				del zarr_store[f'{chunkname}/{var}']
				# Wait for the deletion to finish
				while var in zarr_store[chunkname]:
					pass


	for i, name in enumerate(chunknames):
		if not masterframe_only:
			click.secho(f"Track points using optical flow for {name}...")
			chunk = xr.open_zarr(dataset, group=name)
			points_trajectories = optical_flow(chunk, track_grid_size, window_size, max_distance,
									min_num_points_to_detect, max_num_points_to_detect, 
									**detection_args, **debug_args)
			
			points_trajectories.to_dataset(name='points_trajectories').to_zarr(dataset, group=name, mode='a') #.chunk(chunks={'frame': 1,'point': 'auto','coordinate': 2})
			click.secho(f"Stored optical flow tracked points for chunk {name} ({100*(i+1)/len(chunks):.2f}%).")

			click.secho(f"Interpolating pullback and pushforward maps for {name}...")
			chunk = xr.open_zarr(dataset, group=name)
			pullbacks, pushforwards = interpolate_maps(chunk, interpolate_grid_size=interpolate_grid_size, mls_alpha=mls_alpha)
			pullbacks.to_dataset(name='pullbacks', promote_attrs=True).to_zarr(dataset, group=name, mode='a')
			pushforwards.to_dataset(name='pushforwards',  promote_attrs=True).to_zarr(dataset, group=name, mode='a')
			click.secho(f"Stored interpolated maps for chunk {name} ({100*(i+1)/len(chunks):.2f}%).")
		
		if compute_videos:
			click.secho(f"Visualizing registration results and computing masterframe for {name}...")
		else:
			click.secho(f"Computing masterframe for {name}...")
		chunk = xr.open_zarr(dataset, group=name)
		masterframe, chunkaverage = generate_masterframe_and_videos(chunk, grid_size=interpolate_grid_size, videos=compute_videos)
		
		masterframe.to_dataset(name='masterframe').to_zarr(dataset, group=name, mode='a')
		if compute_videos:
			chunkaverage.to_dataset(name='chunkaverage').to_zarr(dataset, group=name, mode='a')
		
		click.secho(f"Stored masterframe {', chunkaverage and visualization videos ' if compute_videos else ''}for {name} ({100*(i+1)/len(chunks):.2f} %).\n")


def show_masterframe(datagroup: str, chunk: int, peaks: bool=False) -> None:
	chunk_nr = int(chunk)
	chunk = xr.open_zarr(datagroup, group=f'chunk_{chunk}')
	if peaks:
		mf = chunk.masterframe.data.compute()
		df = np.stack((mf,) * 3, -1)
		df[mf == 1] = [1, 0, 0]
		plt.imshow(df)
	else:
		chunk.masterframe.plot.imshow(yincrease=False, cmap='binary')
	plt.title(f'Masterframe of chunk {chunk_nr}')
	plt.show()