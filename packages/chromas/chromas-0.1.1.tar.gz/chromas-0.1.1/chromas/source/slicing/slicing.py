import json
import os
from functools import partial
from pathlib import Path
from typing import Tuple, Union

import click
import cv2
import dask.array as da
import numpy as np
import scipy.ndimage
import xarray as xr
import zarr
from matplotlib import pyplot as plt
from scipy.ndimage import binary_dilation, binary_erosion
from scipy.spatial import Delaunay
from skimage.segmentation import find_boundaries, mark_boundaries

from ..utils.decorators import error_handler
from .interactive_motion_marker_tuner import InteractiveMotionMarkerTuner
from .motion_marker_utils import compute_stats, stats2mms


def warp_frame(image: Union[np.ndarray, Tuple[np.ndarray, ...]], maps: np.ndarray, border_value: int = 255, remove_border: bool|int=False) -> Union[np.ndarray, Tuple[np.ndarray, ...]]:
	"""
	Warp an image using a pushforward grid.

	Args:
		image (Union[np.ndarray, Tuple[np.ndarray, ...]]): The image or tuple of images to warp.
		maps (np.ndarray): The pushforward or pullback grid.
		border_value (int, optional): The value to use for the border. Defaults to 255.

	Returns:
		Union[np.ndarray, Tuple[np.ndarray, ...]]: The warped image or tuple of warped images.

	Raises:
		ValueError: If the input type of image is invalid.

	Note:
		This function uses OpenCV's remap function for warping.
	"""
	def warp_single(image: np.ndarray) -> np.ndarray:
		out = cv2.remap(image, maps, None, interpolation=cv2.INTER_NEAREST, borderMode=cv2.BORDER_CONSTANT, borderValue=border_value)
		if remove_border:
			out[:remove_border, :] = border_value
			out[-remove_border:, :] = border_value
			out[:, :remove_border] = border_value
			out[:, -remove_border:] = border_value
		return out
	

	if isinstance(image, np.ndarray):
		return warp_single(image)
	elif isinstance(image, tuple) and isinstance(image[0], np.ndarray):
		return tuple(warp_single(i) for i in image)
	else:
		raise ValueError(f'Invalid input type of image {type(image)}.')


def identify_motion_markers_interactively(
	areas,
	masterframe,
	chunkaverage,
	cleanqueen,
	max_eccentricity=0.6,
	max_area=2000,
	max_cv=1.0,
	zero_proportion=0.5,
	zero_consecutive=10,
	params=None,
	debug=False
):
	"""
	A convenient wrapper that creates the class, runs it, and returns the final result.
	"""
	tuner = InteractiveMotionMarkerTuner(
		areas=areas,
		masterframe=masterframe,
		chunkaverage=chunkaverage,
		cleanqueen=cleanqueen,
		max_eccentricity=max_eccentricity,
		max_area=max_area,
		max_cv=max_cv,
		zero_proportion=zero_proportion,
		zero_consecutive=zero_consecutive,
		params=params,
		debug=debug
	)
	final_markers = tuner.run()
	return final_markers, tuner.param



def identify_motion_marker(areas: np.ndarray, masterframe: np.ndarray, cleanqueen: np.ndarray,
				 max_area_cutoff: int=10_000, max_eccentricity: float=0.6, max_area: int=2000, max_cv: float=1.0,
				 zero_proportion: float=0.5, zero_consecutive: int=10, params: dict = None,
				 debug: bool = False, debug_visual: bool = False) -> np.ndarray:
	assert max_area_cutoff > 0, 'max_area_cutoff must be positive.'
	assert max_eccentricity >= 0, 'max_eccentricity must be non-negative.'
	assert max_area > 0, 'max_area must be positive.'
	assert max_cv >= 0, 'max_cv must be non-negative.'

	areas[areas > max_area_cutoff] = 0

	stats = compute_stats(areas, masterframe, cleanqueen)

	if params is None:
		params = {
			"Max eccentricity:": {"value": max_eccentricity, "active": True},
			"Max area:": {"value": max_area, "active": True},
			"Max CV:": {"value": max_cv, "active": True},
			"Zero proportion:": {"value": zero_proportion, "active": True},
			"Zero consecutive:": {"value": zero_consecutive, "active": True},
		}


	motion_markers = stats2mms(stats, params, debug)

	if debug_visual:
		plotframe = np.stack((255-255*(masterframe/masterframe.max()),)*3, axis=-1).astype(np.uint8)
		plotframe[np.isin(cleanqueen, motion_markers) & (masterframe > 0)] = [255, 0, 0]
		plt.imshow(plotframe)
		plt.title('Motion markers (red)')
		plt.show()

	return motion_markers


def barycentric2cartesian_coordinates(barycentric_coords: np.ndarray, motion_marker_points: np.ndarray) -> np.ndarray:
	assert barycentric_coords.ndim == 2 and (barycentric_coords.shape[1] == 3), f'{barycentric_coords.shape=}'
	assert motion_marker_points.ndim == 4 and (motion_marker_points.shape[2] == 3) and (motion_marker_points.shape[3] == 2), f'{motion_marker_points.shape=}'
	return np.einsum('ij,hijk->hik', barycentric_coords, motion_marker_points)


def cartesian2barycentric_coordinates(r: np.ndarray, tri: tuple[np.ndarray, np.ndarray, np.ndarray]) -> np.ndarray:
	r1, r2, r3 = tri
	denominator = np.cross(r1 - r3, r2 - r3)
	l1 = np.cross(r - r3, r2 - r3) / denominator 
	l2 = np.cross(r - r3, r3 - r1) / denominator
	coords = np.array([l1, l2, 1 - l1 - l2])
	return coords


def center_of_mass(segmentation: np.ndarray, cleanqueen: np.ndarray, index: int) -> np.ndarray:
	with np.errstate(divide='ignore', invalid='ignore'):
		return np.array(scipy.ndimage.center_of_mass(segmentation, labels=cleanqueen, index=index))


def compute_motion_marker_centers(segmentations: np.ndarray, cleanqueens: np.ndarray, motion_markers: np.ndarray, buffer: int=0) -> np.ndarray:
	motion_marker_centers = np.zeros((segmentations.shape[0], len(motion_markers), 2), dtype=np.float64)
	for i, (seg, clq) in enumerate(zip(segmentations, cleanqueens)):
		motion_marker_centers[i] = center_of_mass(seg, clq, motion_markers)
	return motion_marker_centers


def compute_local_coordinates(frames: np.ndarray, segmentations: np.ndarray, cleanqueens: np.ndarray, motion_marker_centerss: np.ndarray,
					  		  epiframes: np.ndarray, non_motion_markers: np.ndarray, all_epiframes: np.ndarray, buffer: int=0) -> np.ndarray:
	frames = frames[0][0]
	output = np.zeros((len(frames), 2, len(all_epiframes), 3), dtype=np.float64)
	for i, (frame, seg, clq, acs) in enumerate(zip(frames, segmentations, cleanqueens, motion_marker_centerss)):
		# clq = clear_border(clq, buffer_size=buffer)


		resting_chromatophores = np.intersect1d(np.argwhere(all_epiframes == frame)[:,0], non_motion_markers)
		if not resting_chromatophores.size:
			click.echo(f'No resting chromatophores found in frame {frame}.\n{np.argwhere(epiframes == frame)[:,0]=}')
		resting_chromatophores_centers = center_of_mass(seg, clq, resting_chromatophores)

		triangulation = Delaunay(acs)
		simplices = triangulation.simplices[triangulation.find_simplex(resting_chromatophores_centers)]
		local_motion_marker_centers = acs[simplices]

		barycentric_coords = np.array([cartesian2barycentric_coordinates(r, tri) for r, tri in zip(resting_chromatophores_centers, local_motion_marker_centers)])
	
		output[i, 0, resting_chromatophores] = barycentric_coords
		simplices[np.isnan(simplices)] = 0
		simplices = simplices.astype(np.float64)
		output[i, 1, resting_chromatophores] = simplices
	return output


def compute_epicenters(motion_marker_centerss: np.ndarray, non_motion_markers: np.ndarray, motion_markers: np.ndarray, barycentric_coordinates: np.ndarray,
					   simplices: np.ndarray, debug: bool = False, debug_visual: bool = False) -> np.ndarray:
	num_frames = motion_marker_centerss.shape[0]
	num_chromatophores = len(non_motion_markers)
	
	# Gather the motion_marker points for each simplex
	assert motion_marker_centerss.ndim == 3 and motion_marker_centerss.shape[1] == len(motion_markers) and motion_marker_centerss.shape[2] == 2, f'{motion_marker_centerss.shape=}'
	motion_marker_points = motion_marker_centerss[:, simplices]  # Shape: (num_frames, num_chromatophores, 3, 2)
	assert motion_marker_points.ndim == 4 and motion_marker_points.shape[2] == 3 and motion_marker_points.shape[3] == 2 and motion_marker_points.shape[0] == num_frames and motion_marker_points.shape[1] == num_chromatophores, motion_marker_points.shape

	epicenters = barycentric2cartesian_coordinates(barycentric_coordinates, motion_marker_points)
	return epicenters


def interpolate_missing_values(data):

	# Get the number of frames
	n_frames = data.shape[0]
	frames = np.arange(n_frames)  # Frame indices
	
	# Iterate over coordinates (x, y)
	for coord in range(2):  # For 2D coordinates
		values = data[:, :, coord]  # Extract data for the current coordinate
		# Find NaN and zero locations
		nans = np.isnan(values)
		for motion_marker in range(data.shape[1]):  # Iterate over motion_markers
			if np.any(nans[:, motion_marker]):  # Interpolate only if there are NaNs
				try:
					values[nans[:, motion_marker], motion_marker] = np.interp(
						frames[nans[:, motion_marker]], frames[~nans[:, motion_marker]], values[~nans[:, motion_marker], motion_marker]
					)
				except Exception as e:
					click.secho(f'[ERROR] {e}', fg='red')
					click.secho(f'{nans[:, motion_marker]=}\n{frames[nans[:, motion_marker]]=}\n{frames[~nans[:, motion_marker]]=}\n{values[~nans[:, motion_marker], motion_marker]=}', fg='red')
					raise e
		data[:, :, coord] = values  # Update the data for this coordinate

	return data


def find_motion_markers(masterframe: np.ndarray, cleanqueen: np.ndarray, chunkaverage: np.ndarray, areas: np.ndarray,
					     max_area_cutoff: int=10_000, max_eccentricity: float=0.6, max_area: int=2000,
					 	 max_cv: float=1.0, min_num_motion_markers: int=30, zero_proportion: float=0.2, zero_consecutive: int=10,
					 	 debug: bool = False, debug_visual: bool = False, interactive: bool = False, params: dict = None) -> tuple[xr.DataArray]:
	if params is not None:
		max_eccentricity = params["Max eccentricity:"]['value']
		max_area = params["Max area:"]['value']
		max_cv = params["Max CV:"]['value']
		zero_proportion = params["Zero proportion:"]['value']
		zero_consecutive = params["Zero consecutive:"]['value']

	# Identify motion markers and compute their centers:
	if interactive:
		motion_markers, params = identify_motion_markers_interactively(areas, masterframe, chunkaverage, cleanqueen, max_eccentricity=max_eccentricity, max_area=max_area, max_cv=max_cv,
														 zero_proportion=zero_proportion, zero_consecutive=zero_consecutive, params=params, debug=debug)
	else:
		motion_markers = identify_motion_marker(areas, masterframe, cleanqueen, max_area_cutoff=max_area_cutoff, max_eccentricity=max_eccentricity, max_area=max_area, max_cv=max_cv,
					 				 		    zero_proportion=zero_proportion, zero_consecutive=zero_consecutive, params=params,
											    debug=debug, debug_visual=debug_visual)
		params = {'max_eccentricity': max_eccentricity, 'max_area': max_area, 'max_cv': max_cv, 'zero_proportion': zero_proportion, 'zero_consecutive': zero_consecutive}

	if len(motion_markers) < min_num_motion_markers:
		raise ValueError(f'Found only {len(motion_markers)} motion markers, but need at least {min_num_motion_markers}.')
	
	return motion_markers, params




def epicenters_chunk(chunk: xr.Dataset, motion_markers: np.ndarray, buffer: int=0, max_movement: int = 15,
					 debug: bool = False, debug_visual: bool = False) -> tuple[xr.DataArray]:
	cleanqueen = chunk.warped_cleanqueen.sel(frame=0).data.compute()
	masterframe = chunk.masterframe.data.compute()
	areas = chunk.areas.data.compute()
	masterframe = masterframe / masterframe.max()

	# Print if areas has nans and if so how many %:
	if np.isnan(areas).any():
		click.secho(f'[WARNING] Found {100*np.isnan(areas).mean():.2f}% NaN values in areas.', fg='yellow')

	click.echo('Computing epicenters of motion markers...')
	_compute_motion_marker_centers = partial(compute_motion_marker_centers, motion_markers=motion_markers, buffer=buffer)
	motion_marker_centers = da.map_blocks(_compute_motion_marker_centers, chunk.segmentation.data,
								chunk.warped_cleanqueen.data, dtype=np.float64, chunks=(1, len(motion_markers), 2), drop_axis=[1, 2], new_axis=[1, 2]).compute()
	motion_marker_centers = interpolate_missing_values(motion_marker_centers)

	# Triangulate the other chromatophores using the motion markers:
	triangulation = Delaunay(motion_marker_centers[0])

	chrom_ids = np.unique(cleanqueen)
	all_centers = np.array(scipy.ndimage.center_of_mass(masterframe>0, labels=cleanqueen, index=chrom_ids))
	chrom_ids = np.array([chrom_id for (chrom_id, center) in zip(chrom_ids, all_centers) if (triangulation.find_simplex(center) >= 0 and chrom_id)])
	motion_markers = motion_markers.data

	non_motion_markers = np.array(sorted(list(set(chrom_ids) - set([m for m in motion_markers]))))
	
	if debug:
		click.secho(f'\n[DEBUG]{non_motion_markers=}.\n\n{chrom_ids=}', fg='yellow')
	if debug_visual:
		plt.imshow(mark_boundaries(mark_boundaries(1 - masterframe/masterframe.max(), np.isin(cleanqueen, chrom_ids) * cleanqueen, color=(1, 0, 0), mode='thick'), np.isin(cleanqueen, motion_markers) * cleanqueen, color=(0, 0, 1), mode='thick'))
		plt.imshow(np.isin(cleanqueen, non_motion_markers), alpha=0.2, cmap='Reds')
		plt.triplot(motion_marker_centers[0][:, 1], motion_marker_centers[0][:, 0], triangulation.simplices, color='blue', alpha=0.5)
		plt.title('Motion markers (blue) and tracked chromatophores (red)')
		plt.gcf().canvas.manager.set_window_title('CHROMAS - Visualizing Motion Markers')
		plt.show()
	
	# Compute epiframes:
	all_epiframes = np.argmin(np.where(areas > 0, areas, np.inf), axis=0)
	epiframes = sorted(np.unique(all_epiframes[non_motion_markers]))

	epiframe_segmentations = chunk.segmentation.data[epiframes]
	epiframe_cleanqueens = chunk.warped_cleanqueen.data[epiframes]
	epiframe_motion_marker_centers = motion_marker_centers[epiframes]
	click.echo(f'Found {len(motion_markers)} motion markers, {len(non_motion_markers)} non-motion-markers and {len(epiframes)} epiframes.')

	# Compute local coordinates:
	click.echo('Computing local coordinates...')
	_compute_local_coordinates = partial(compute_local_coordinates, epiframes=epiframes, non_motion_markers=non_motion_markers, all_epiframes=all_epiframes, buffer=buffer)
	epipositions = da.map_blocks(_compute_local_coordinates, da.from_array(np.expand_dims(epiframes, [1, 2]), chunks=(1, 1, 1)),
								  epiframe_segmentations, epiframe_cleanqueens, da.from_array(epiframe_motion_marker_centers).rechunk((1, -1, 2)),
								  dtype=np.float64, chunks=(1, 2, -1, 3), new_axis=[1, 2, 3], drop_axis=[1, 2])
	epipositions = da.sum(epipositions, axis=0)
	local_coordinates, simplices = epipositions.compute()

	local_coordinates, simplices = local_coordinates[non_motion_markers], simplices[non_motion_markers].astype(np.int32)

	# Compute epicenters for all chromatophore, based on local coordinates and motion marker centers:
	click.echo('Computing epicenters...')
	_compute_epicenters = partial(compute_epicenters, non_motion_markers=non_motion_markers, motion_markers=motion_markers, barycentric_coordinates=local_coordinates,
								  simplices=simplices, debug=debug, debug_visual=debug_visual)
	centers = da.map_blocks(_compute_epicenters, da.from_array(motion_marker_centers, chunks=(1, -1, 2)), dtype=np.float64).compute()

	# Check if the euclidean distance between the epicenter of frame i and frame i+1 is within a certain threshold, otherwise remove the chromatophore:
	distances = np.linalg.norm(np.diff(centers, axis=0), axis=2)
	
	invalid = np.any(distances > max_movement, axis=0)

	non_motion_markers = non_motion_markers[~invalid]
	centers = centers[:, ~invalid]
	simplices = simplices[~invalid]
	if invalid.any():
		click.secho(f'[WARNING] Removed {invalid.sum()} ({100*invalid.mean():.2f}%) chromatophores due to large distance between epicenters in consecutive frames.', fg='yellow')

	centers = xr.DataArray(centers, dims=('frame', 'non_motion_marker', 'coordinate'), coords={'non_motion_marker': non_motion_markers})
	motion_marker_centers = xr.DataArray(motion_marker_centers, dims=('frame', 'motion_marker', 'coordinate'), coords={'motion_marker': motion_markers})
	non_motion_markers = xr.DataArray(non_motion_markers, dims=('non_motion_marker'))
	motion_markers = xr.DataArray(motion_markers, dims=('motion_marker'))
	simplices = xr.DataArray(simplices, dims=('non_motion_marker', 'triangle_point'), coords={'triangle_point': [0, 1, 2]}).astype(np.int32)
	
	return centers, motion_marker_centers, non_motion_markers, motion_markers, simplices


########################################################################################
##########################  SLICE AREAS ###############################################
########################################################################################

def get_labeled_borders(segmentations: np.ndarray, cleanqueens: np.ndarray) -> np.ndarray:
	""" Returns the labeled borders of the objects in the given image. """
	labeled_borders = np.zeros_like(cleanqueens)
	for i, (seg, clq) in enumerate(zip(segmentations, cleanqueens)):
		clq_borders = binary_dilation(find_boundaries(clq))
		borders = (seg > 0) & (~binary_erosion((seg > 0).astype(np.uint8), iterations=1) | ((seg > 0) & (clq_borders > 0)))
		labeled_borders[i][borders] = clq[borders]
	return labeled_borders      


def compute_slice_areas(labeled_borders: np.ndarray, centers: np.ndarray, motion_marker_centers: np.ndarray,
						simplices: np.ndarray, non_motion_markers: np.ndarray, n_slices: int=36) -> tuple[np.ndarray, np.ndarray]:
	n_labels = max(labeled_borders.max().astype(int) + 1, non_motion_markers.max() + 1)

	labeled_borders = labeled_borders[0]
	centers = centers[0]
	motion_marker_centers = motion_marker_centers[0]
	centers_ = np.zeros((n_labels, 2), dtype=np.float16)
	centers_[non_motion_markers] = centers
	centers = centers_

	local_motion_marker_centers = motion_marker_centers[simplices[:, :2].astype(int)]

	d = np.diff(local_motion_marker_centers, axis=1)
	orientation_angles = np.zeros(n_labels, dtype=np.float16)
	orientation_angles[non_motion_markers] = np.degrees(np.arctan2(d[:, 0, 0], d[:, 0, 1]))
	oa = orientation_angles.copy()
	
	# Create a mask for non-zero pixels
	mask = labeled_borders != 0

	# Get the coordinates of the non-zero pixels
	non_zero_coords = np.argwhere(mask)

	# Get the labels of the non-zero pixels
	labels = labeled_borders[mask]
	orientation_angles = orientation_angles[labels]

	# Get the corresponding centers for these labels
	corresponding_centers = centers[labels]

	# Calculate the distances using vectorized operations
	distances = np.linalg.norm(non_zero_coords - corresponding_centers, axis=1)

	# Calculate the angles using vectorized operations
	angles = np.degrees(np.arctan2(corresponding_centers[:, 1] - non_zero_coords[:, 1], 
						corresponding_centers[:, 0] - non_zero_coords[:, 0]))
	angles = np.mod(angles - orientation_angles, 360)
	angles[angles == 360] = 0

	distance_map = np.zeros_like(labeled_borders, dtype=np.float16)
	angle_map = np.zeros_like(labeled_borders, dtype=np.float16)

	distance_map[mask] = distances
	angle_map[mask] = angles

	distance_sums = np.zeros((n_labels, n_slices), dtype=np.float32)
	counts = np.zeros((n_labels, n_slices), dtype=int)
	angle_bins = np.digitize(angle_map, bins=np.linspace(0, 360, n_slices+1), right=False)
	angle_bins[angle_bins == n_slices+1] = n_slices
	angle_bins -= 1

	# Accumulate distances and counts for each bin and label
	np.add.at(distance_sums, (labeled_borders, angle_bins), distance_map)
	np.add.at(counts, (labeled_borders, angle_bins), 1)

	# Compute the average distance for each bin and label
	counts[counts == 0] = 1
	average_distances = np.divide(distance_sums, counts)

	# Handle bins with no counts to avoid division by zero (NaN)
	average_distances[np.isnan(average_distances)] = 0
	 # Average distances are now of shape (n_labels, n_slices), orientation angles are of shape (n_labels,) add them such that
	 # they have shape (n_labels, n_slices + 1) and the orientation angles are in the last column:
	average_distances = np.concatenate([average_distances, np.expand_dims(oa, 1)], axis=1)
	average_distances = average_distances[non_motion_markers]
	return np.expand_dims(average_distances, 0)



def slicearea_chunk(chunk: xr.Dataset, n_slices: int=36) -> tuple[xr.DataArray, xr.DataArray]:
	non_motion_markers = chunk.non_motion_markers.data.compute()

	_compute_slice_areas = partial(compute_slice_areas, simplices=chunk.simplices.compute(), non_motion_markers=non_motion_markers, n_slices=n_slices)

	labeled_borders = da.map_blocks(get_labeled_borders, chunk.segmentation.data, chunk.warped_cleanqueen.data)

	result = da.map_blocks(_compute_slice_areas, labeled_borders, chunk.centers.data.rechunk((1, -1, 2)),
						   chunk.motion_marker_centers.data.rechunk((1, -1, 2)), new_axis=[1, 2], chunks=(1, len(non_motion_markers), n_slices+1),
						   drop_axis=[1, 2], dtype=np.float32)
	slice_areas, orientation_angles = result[:, :, :-1], result[:, :, -1]

	# Add the new variables to the chunk
	slice_areas = xr.DataArray(slice_areas, dims=('frame', 'non_motion_marker', 'slice'), coords={'slice': np.arange(n_slices)})
	orientation_angles = xr.DataArray(orientation_angles, dims=('frame', 'non_motion_marker'))

	return slice_areas, orientation_angles


@error_handler('Slicing')
def slice(datagroup: str, n_slices: int=36, buffer: int=0, max_area_cutoff: int=10_000, max_eccentricity: float=0.6,
		  max_area: int=2000, max_cv: float=1.0, zero_proportion: float=0.5, zero_consecutive: int=10,
		  min_num_motion_markers: int=30, chunk_selection: list[int]=[], max_movement: int = 15,
		  interactive: bool=False, use_defaults: bool=False, do_not_run: bool=False, combinded: bool=False, only_areas: bool=False,
		  cluster_args: dict={'n_workers': 1, 'threads_per_worker': 1, 'processes': False},
		  debug_args: dict = {'debug': False, 'debug_visual': False}) -> None:
	
	if not chunk_selection:
		chunknames = [chunk for chunk in zarr.open(datagroup).keys() if chunk.startswith('chunk_')]
		try:
			chunk_mask = xr.open_zarr(datagroup, 'stitching').chunk_mask.data
			chunknames = [c for c, m in zip(chunknames, chunk_mask) if m]
			click.echo(f'Chunknames: {chunknames}')
		except:
			pass
	else:
		if debug_args['debug']:
			click.secho(f'[DEBUG] Using debug mode. Only processing chunks {chunk_selection}.', fg='yellow', italic=True)
		chunknames = [f'chunk_{chunk}' for chunk in chunk_selection]
	chunks = [xr.open_zarr(datagroup, group=chunk) for chunk in chunknames]

	if not chunks:
		click.secho("No chunks found in the provided data group. Have you run segmentation yet?", fg='red', bold=True)
		return False
	click.echo(f'Processing {len(chunks)} chunks.')

	params = {c: None for c in chunknames}

	zarr_store = zarr.open(datagroup, mode='a')

	if not combinded and not only_areas:
		for chunkname in chunknames:
			for var in ['slice_areas', 'orientation_angles', 'motion_marker', 'motion_markers', 'slice',
						'non_motion_marker', 'non_motion_markers', 'simplices', 'centers', 'motion_marker_centers']:
				if var in zarr_store[chunkname]:
					if debug_args['debug']:
						click.secho(f'[DEBUG] Deleting {var} from chunk {chunkname} because it already exists.', fg='yellow')
					del zarr_store[f'{chunkname}/{var}']

			params_path = Path(datagroup) / chunkname / '._motion_marker_params.json'
			
			if ((interactive and not use_defaults) or (not interactive and not use_defaults)) and params_path.exists():
				params[chunkname] = json.loads(params_path.read_text())
				if debug_args['debug']:
					click.secho(f'[DEBUG] Loaded parameters for motion marker selection in chunk {chunkname}:', fg='yellow', bold=True)
					for k, v in params[chunkname].items():
						click.secho(f'\t{k}\t{v}', fg='yellow')
			elif params_path.exists():
				os.remove(params_path)
				if debug_args['debug']:
					click.secho(f'[DEBUG] Deleted parameters for motion marker selection in chunk {chunkname}.', fg='yellow')

		all_motion_markers = []
		for i, (name, chunk) in enumerate(zip(chunknames, chunks)):
			click.secho(f"\nFinding motion markers for chunk {name} ({100*(i+1)/len(chunks):.2f}%).")
			
			cleanqueen = chunk.warped_cleanqueen.isel(frame=0).data.compute()
			masterframe = chunk.masterframe.data.compute()
			try:
				chunkaverage = chunk.chunkaverage.data.compute()
			except AttributeError:
				video = chunk.segmentation.attrs['chunk_path']
				import decord
				vr = decord.VideoReader(video)
				chunkaverage = vr[0].asnumpy()
				del vr
			areas = chunk.areas.data.compute()
			masterframe = masterframe / masterframe.max()

			motion_markers, params[name] = find_motion_markers(masterframe, cleanqueen, chunkaverage, areas,
				max_area_cutoff, max_eccentricity, max_area, max_cv, min_num_motion_markers, zero_proportion, zero_consecutive, debug=debug_args['debug'], debug_visual=debug_args['debug_visual'],
				interactive=interactive, params=params[name])
			
			all_motion_markers.append(motion_markers)
			
			if debug_args['debug']:
				click.secho(f'[DEBUG] Running with parameters for motion marker selection in chunk {name}:', fg='yellow', bold=True)
				for k, v in params[name].items():
					click.secho(f'\t{k}\t{v}', fg='yellow')
			
			# Store the motion marker parameters if interactive mode is used
			if interactive:
				params_json = json.dumps(params[name])
				params_path = Path(datagroup) / name / '._motion_marker_params.json'
				params_path.write_text(params_json)
				if do_not_run:
					click.secho(f"Skipping epicenter and slicearea computation for chunk {name} ({100*(i+1)/len(chunks):.2f}%).", fg='yellow')
					continue
	
	elif not only_areas:
		if 'slicing' in zarr_store:
			click.secho('[WARNING] Deleting slicing from dataset since it already existed.', fg='yellow')
			del zarr_store['slicing']

		params_path = Path(datagroup) / '._motion_marker_params_all_chunks.json'
		
		params = None
		if ((interactive and not use_defaults) or (not interactive and not use_defaults)) and params_path.exists():
			params= json.loads(params_path.read_text())
			if debug_args['debug']:
				click.secho('[DEBUG] Loaded parameters for motion marker selection for all chunks:', fg='yellow', bold=True)
				for k, v in params.items():
					click.secho(f'\t{k}\t{v}', fg='yellow')
		elif params_path.exists():
			os.remove(params_path)
			if debug_args['debug']:
				click.secho('[DEBUG] Deleted parameters for motion marker selection in all chunks.', fg='yellow')
		
		stitching = xr.open_zarr(datagroup, 'stitching')
		queenframe = stitching.queenframe.data.compute()
		queenframe = queenframe / queenframe.max()
		cleanqueen = stitching.cleanqueen.data.compute()
		try:
			ref_chunk = stitching.stitching_matrix.attrs['ref_chunk']
		except AttributeError:
			ref_chunk = 0
		click.echo(f'Using reference chunk {ref_chunk} for motion marker selection.')
		chunk = xr.open_zarr(datagroup, f'chunk_{ref_chunk}')
		try:
			chunkaverage = chunk.chunkaverage.data.compute()
		except AttributeError:
			video = chunk.segmentation.attrs['chunk_path']
			import decord
			vr = decord.VideoReader(video)
			chunkaverage = vr[0].asnumpy()
			del vr

		areas = [chunk.areas.compute() for chunk in chunks]
		adjusted_arrays = []
		cumulative_frame = 0
		for arr, length in zip(areas, [chunk.sizes['frame'] for chunk in chunks]):
			# Update the 'frame' coordinate to global frame indices
			adjusted_arr = arr.assign_coords(frame=(arr['frame'] + cumulative_frame))
			adjusted_arrays.append(adjusted_arr)
			cumulative_frame += length
		areas = xr.concat(adjusted_arrays, dim='frame').data
		
		click.secho("\nSelecting motion markers for all chunks.")
		motion_markers, params = find_motion_markers(queenframe, cleanqueen, chunkaverage, areas,
													max_area_cutoff, max_eccentricity, max_area, max_cv, min_num_motion_markers, zero_proportion, zero_consecutive, debug=debug_args['debug'], debug_visual=debug_args['debug_visual'],
													interactive=interactive, params=params)
		all_motion_markers = [motion_markers] * len(chunknames)
		
		if debug_args['debug']:
			click.secho('[DEBUG] Running with parameters for motion marker selection all chunks:', fg='yellow', bold=True)
			for k, v in params.items():
				click.secho(f'\t{k}\t{v}', fg='yellow')
		
		# Store the motion marker parameters if interactive mode is used
		if interactive:
			params_json = json.dumps(params)
			params_path.write_text(params_json)

	if do_not_run:
		click.secho(f"Skipping epicenter and slicearea computation for chunk {name} ({100*(i+1)/len(chunks):.2f}%).", fg='yellow')
		return True
	
	# DEBUG INFO:
	if debug_args['debug'] and not combinded and not only_areas:
		# Compute overlap matrix
		mms = {name: set(chunk.motion_markers.data.compute()) for name, chunk in zip(chunknames, chunks)}
		overlap_matrix = np.zeros((len(chunks), len(chunks)))
		for i in range(len(chunks)):
			for j in range(i + 1,len(chunks)):
				markers_i = mms[chunknames[i]]
				markers_j = mms[chunknames[j]]
				overlap = len(markers_i & markers_j) / len(markers_i | markers_j) * 100
				overlap_matrix[i, j] = overlap

		# Print upper triangle matrix
		click.secho("[DEBUG] Overlap of motion markers between chunks (Jaccard Similarity Index):", fg='yellow')
		click.secho(" " * 12 + " ".join(f"{name:>12}" for name in chunknames), fg='yellow')
		for i, row_name in enumerate(chunknames):
			row = [f"{overlap_matrix[i, j]:>12.2f}" if j > i else " " * 12 for j in range(len(chunks))]
			click.secho(f"{row_name:>12} " + " ".join(row), fg='yellow')
	
	if only_areas:
		try:
			all_motion_markers = [xr.open_zarr(datagroup, 'slicing').motion_marker.data] * len(chunknames)
		except FileNotFoundError:
			all_motion_markers = [xr.open_zarr(datagroup, chunknames[0]).motion_markers.data] * len(chunknames)

	# COMPUTE SLICEAREAS FOR EACH CHUNK:
	click.secho('Compute sliceareas for all chunks', bold=True)
	for i, (name, chunk, motion_markers) in enumerate(zip(chunknames, chunks, all_motion_markers)):
		click.echo(f'Computing slice areas for {name} ({i+1}/{len(chunknames)}).')
		
		for var in ['centers', 'motion_marker_centers', 'non_motion_marker', 'non_motion_markers', 'motion_markers', 'motion_marker', 'simplices',
			        'slice_areas', 'orientation_angles']:
			if var in zarr_store[name]:
				if debug_args['debug']:
					click.secho(f'[DEBUG] Deleting {var} from chunk {name} because it already exists.', fg='yellow')
				del zarr_store[f'{name}/{var}']
				
		centers, motion_marker_centers, non_motion_markers, motion_markers, simplices = epicenters_chunk(chunk, motion_markers, buffer, max_movement, **debug_args)

		

		epicenters = xr.Dataset({
			'centers': centers,
			'motion_marker_centers': motion_marker_centers,
			'non_motion_markers': non_motion_markers,
			'motion_markers': motion_markers,
			'simplices': simplices
		})
		epicenters.to_zarr(datagroup, group=name, mode='a')
		
		click.secho(f"Computing sliceareas for chunk {name} ({100*(i+1)/len(chunks):.2f}%).")
		chunk = xr.open_zarr(datagroup, group=name)
		slice_areas, orientation_angles = slicearea_chunk(chunk, n_slices)
		slices = xr.Dataset({
			'slice_areas': slice_areas,
			'orientation_angles': orientation_angles
		})
		slices.to_zarr(datagroup, group=name, mode='a')
		click.secho(f"Stored epicenters and sliceareas for chunk {name} ({100*(i+1)/len(chunks):.2f}%).", fg='green')

	# CONCATENATING SLICEAREAS:
	click.echo('Concatenating slice areas from all chunks.')
	if combinded:
		xr.DataArray(all_motion_markers[0], name='motion_marker').to_zarr(datagroup, group='slicing', mode='a')
		areas = [xr.open_zarr(datagroup, group=name).slice_areas.compute() for name in chunknames]
		adjusted_arrays = []
		cumulative_frame = 0
		for arr, length in zip(areas, [chunk.sizes['frame'] for chunk in chunks]):
			# Update the 'frame' coordinate to global frame indices
			adjusted_arr = arr.assign_coords(frame=(arr['frame'] + cumulative_frame))
			adjusted_arrays.append(adjusted_arr)
			cumulative_frame += length
		areas = xr.concat(adjusted_arrays, dim='frame')
		areas.to_zarr(datagroup, group='slicing', mode='a')
	

########################################################################################
################## MOTION MARKER DETECTION UTILITIES ###################################
########################################################################################

def show_motion_marker(dataset: str, chunk: int=0, max_eccentricity: float=0.6, max_area: int=2000, max_cv: float=1.0, max_area_cutoff: int=10_000,
					   zero_proportion: float=0.2, zero_consecutive: int=10) -> None:
	chunk_int = int(chunk)
	chunk = xr.open_zarr(dataset, group=f'chunk_{chunk_int}')

	if 'motion_markers' in chunk:
		masterframe = chunk.masterframe.data.compute()
		cleanqueen = chunk.warped_cleanqueen.sel(frame=0).data.compute()
		motion_markers = chunk.motion_markers.data.compute()
		plotframe = np.stack((255-255*(masterframe/masterframe.max()),)*3, axis=-1).astype(np.uint8)
		plotframe[np.isin(cleanqueen, motion_markers) & (masterframe > 0)] = [255, 0, 0]
		plt.imshow(plotframe)
		plt.title('Motion markers (red)')
		plt.show()
	else:
		click.echo(f'Detecting potential motion markers for chunk {chunk_int}.')
		identify_motion_marker(chunk.areas.data.compute(), chunk.masterframe.data.compute(), chunk.warped_cleanqueen.sel(frame=0).data.compute(), debug_visual=True,
			   		 max_area_cutoff=max_area_cutoff, max_eccentricity=max_eccentricity, max_area=max_area, max_cv=max_cv,
					 zero_proportion=zero_proportion, zero_consecutive=zero_consecutive)
	return
