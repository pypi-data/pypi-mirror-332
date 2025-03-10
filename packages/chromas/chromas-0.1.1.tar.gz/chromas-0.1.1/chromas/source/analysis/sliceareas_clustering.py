"""
Slice Areas Clustering Module.

This module provides functionality for clustering the slice areas of chromatophores.
Each chromatophore is divided into a number of slices so that the underlying data are
represented by time series for each slice (with overall shape: n_frames x n_chromatophores x n_slices).
The module provides functions for clustering these slice time series (using the same approach as for
the overall areas) as well as for visualizing the clustering by overlaying schematic wedge plots on
the background image.

Functions:
	cluster_slice_areas(dataset: str, chunk_int: int, method: str = 'AffinityPropagation', 
						 clustering_kwargs: dict = None, max_tries: int = 5, 
						 debug_args: dict = None)
		Clusters the slice area time series and stores the resulting labels.
	plot_slice_cluster(dataset: str, chunk_int: int, output_dir: str = None)
		Plots the slice area clustering by overlaying, for each chromatophore, a schematic ring
		(divided into slices) colored according to the cluster labels.
"""

import os
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches
import matplotlib.cm as cm
import click
import zarr
import matplotlib.patches as patches
from ..utils.decorators import error_handler, convergence_handler
from .clustering_utils import cluster_correlation


@error_handler('Slice areas clustering', cluster=False)
def cluster_slice_areas(dataset: str, chunk_int: int, method: str = 'AffinityPropagation',
						clustering_kwargs: dict = None, max_tries: int = 5,
						debug_args: dict = None):
	"""
	Cluster slice areas of chromatophores.

	This function loads the slice area data (assumed to be stored under the variable
	``slice_areas`` in each chunk) from a Zarr dataset. Each chunk is assumed to contain data
	with shape `(n_frames_per_chunk, n_chromatophores, n_slices)`. The data from all chunks are
	concatenated along the frame axis, then reshaped to form a 2D array with shape
	`(n_frames_total, n_chromatophores * n_slices)`. A correlation matrix is computed on this data
	and then clustered (by default, using AffinityPropagation via a shared function). The resulting
	slice cluster labels (reshaped into `(n_chromatophores, n_slices)`) are stored back into the dataset.

	Args:
		dataset (str): Path to the dataset (Zarr store).
		chunk_int (int): The chunk index from which to load the data. If None or a list, multiple
			chunks are used.
		method (str, optional): Clustering method to use. Defaults to 'AffinityPropagation'.
		clustering_kwargs (dict, optional): Additional keyword arguments to pass to the clustering
			algorithm. Defaults to None.
		max_tries (int, optional): Maximum number of attempts for convergence. Defaults to 5.
		debug_args (dict, optional): Dictionary of debugging options (e.g.,
			{'debug': False, 'debug_visual': False}). Defaults to None.

	Returns:
		None
	"""
	# Initialize mutable defaults.
	if clustering_kwargs is None:
		clustering_kwargs = {}
	if debug_args is None:
		debug_args = {'debug': False, 'debug_visual': False}

	# Determine Zarr group name.
	if chunk_int is None:
		chunknames = [chunk for chunk in zarr.open(dataset).keys() if chunk.startswith('chunk_')]
		group = 'sliceareas_clustering'
	elif isinstance(chunk_int, list):
		chunknames = [f'chunk_{chunk}' for chunk in chunk_int]
		group = 'sliceareas_clustering'
	elif isinstance(chunk_int, int):
		chunknames = [f'chunk_{chunk_int}']
		group = f'chunk_{chunk_int}/sliceareas_clustering'
	else:
		raise ValueError(f'{chunk_int=} not valid.')

	# Load slice_areas data from each chunk.
	chunks = [xr.open_zarr(dataset, group=chunk) for chunk in chunknames]
	slice_areas_list = [chunk.slice_areas.data.compute() for chunk in chunks]

	if debug_args['debug']:
		click.echo(f'[DEBUG] Using chunknames = {chunknames!r}.')
		click.echo(f'[DEBUG] Using group = {group!r}.')
		click.echo('[DEBUG] Slice areas shapes: ' +
				   '; '.join([str(a.shape) for a in slice_areas_list]))

	# Concatenate along the frames axis.
	slice_areas = np.concatenate(slice_areas_list, axis=0)  # shape: (n_frames_total, n_chrom, n_slices)
	if debug_args['debug']:
		click.echo(f'[DEBUG] Concatenated slice_areas shape: {slice_areas.shape}')

	# Reshape to 2D: each column is one slice time series.
	n_frames_total, n_chrom, n_slices = slice_areas.shape
	slice_areas_reshaped = slice_areas.reshape(n_frames_total, n_chrom * n_slices)
	if debug_args['debug']:
		click.echo(f'[DEBUG] Reshaped slice_areas shape: {slice_areas_reshaped.shape}')

	# Compute correlation matrix.
	corr = np.corrcoef(slice_areas_reshaped, rowvar=False)
	corr = np.nan_to_num(corr, nan=0.0)
	if debug_args['debug']:
		click.echo(f'[DEBUG] Correlation matrix shape: {corr.shape}')
	if debug_args['debug_visual']:
		plt.imshow(corr, cmap='Blues')
		plt.title("Correlation Matrix (Slice Areas)")
		plt.xlabel("Slice ID")
		plt.ylabel("Slice ID")
		plt.colorbar()
		plt.show()

	# Cluster the slice time series.
	labels = convergence_handler(cluster_correlation, max_tries=max_tries)(corr, method, **clustering_kwargs)
	click.echo(f'Found {len(np.unique(labels))} clusters for slice areas.')
	if debug_args['debug']:
		click.echo(f'[DEBUG] Labels shape: {labels.shape}, min: {labels.min()}, max: {labels.max()}')

	# Reshape labels to (n_chrom, n_slices)
	slice_labels = labels.reshape(n_chrom, n_slices)

	# Store clustering labels.
	zarr_store = zarr.open(dataset, mode='a')
	if group in zarr_store.keys():
		if 'slice_labels' in zarr_store[group]:
			click.secho('WARNING: Removing `slice_labels` from dataset since it already exists.', italic=True)
			del zarr_store[f'{group}/slice_labels']
	labels_ds = xr.Dataset({
		'slice_labels': xr.DataArray(
			slice_labels,
			dims=['chrom_id', 'slice'],
			attrs={
				'chunk_int': chunk_int,
				'method': method,
				'max_tries': max_tries,
				'n_slices': n_slices,
				**clustering_kwargs
			}
		)
	})
	labels_ds.to_zarr(dataset, group=group, mode='a')

	if debug_args.get('debug_visual'):
		plot_slice_cluster(dataset, chunk_int, output_dir=None)


def plot_slice_cluster(dataset: str, chunk_int: int, output_dir: str = None):
	"""
	Plot slice area clustering by overlaying wedge plots on chromatophore centers.

	This function loads the stored slice cluster labels and the chunk data. It then loads
	the background image (``chunkaverage``), segmentation masks (``queenframe`` and ``cleanqueen``),
	and the chromatophore centers, orientation angles, and slice areas from the specified chunk.
	For each chromatophore, a circular overlay is drawn at its center. This circle is divided
	into wedges (one per slice) whose colors correspond to the slice’s cluster label.

	Args:
		dataset (str): Path to the dataset (Zarr store).
		chunk_int (int): The chunk index from which to load data.
		output_dir (str, optional): Directory to save the generated plot image. If None, the plot is
			displayed interactively.

	Returns:
		None
	"""
	# Determine the group name for slice clustering.
	if chunk_int is None or isinstance(chunk_int, list):
		group = 'sliceareas_clustering'
	elif isinstance(chunk_int, int):
		group = f'chunk_{chunk_int}/sliceareas_clustering'
	else:
		raise ValueError(f'{chunk_int=} not valid.')

	# Load the slice cluster labels.
	try:
		labels_ds = xr.open_zarr(dataset, group=group)
	except Exception as e:
		click.secho(f"Error loading slice labels from group '{group}': {e}", fg='red')
		return
	slice_labels = labels_ds.slice_labels.compute()  # shape: (n_chrom, n_slices)

	# Load chunk data.
	if not isinstance(chunk_int, int):
		try:
			chunk_int = xr.open_zarr(dataset, 'stitching').attrs['ref_chunk']
		except:
			chunk_int = 0
	try:
		chunk = xr.open_zarr(dataset, group=f'chunk_{chunk_int}')
		stitching = xr.open_zarr(dataset, 'stitching')
		queenframe = stitching.queenframe.data.compute()
		cleanqueen = stitching.cleanqueen.data.compute()
		centers = chunk.centers.sel(frame=0).compute()  # assumes coordinate 'non_motion_marker'
		orientation_angles = chunk.orientation_angles.sel(frame=0).compute()
		slice_areas = chunk.slice_areas.max(dim='frame').compute()
	except Exception as e:
		click.secho(f"Error loading chunk image data: {e}", fg='red')
		return

	# Assume chromatophore IDs are given by the 'non_motion_marker' coordinate of centers.
	chroms2analyse = centers.non_motion_marker.data

	# Create a colormap for slice cluster labels.
	unique_clusters = np.unique(slice_labels.data)
	cmap = cm.get_cmap("tab20", len(unique_clusters))
	cluster_color = {cluster: cmap(i) for i, cluster in enumerate(unique_clusters)}

	# Plot background image with segmentation boundaries.
	from skimage.segmentation import mark_boundaries
	plot_frame = mark_boundaries(queenframe, cleanqueen, color=(1, 1, 1), outline_color=None)
	plt.figure(figsize=(10, 10))
	plt.imshow(plot_frame)

	# Determine number of slices.
	n_slices = slice_labels.data.shape[1]
	angle_width = 360 / n_slices

	n_chrom = len(chroms2analyse)
	
	# Iterate over the indices of chromatophores (from centers)
	for i in range(n_chrom):
		try:
			# Use isel() to retrieve data for the i-th chromatophore.
			center = centers.isel(non_motion_marker=i).data  # [y, x]
			angle0 = orientation_angles.isel(non_motion_marker=i).data  # base angle (scalar)
			chrom_slice_labels = slice_labels.data[i, :]  # shape: (n_slices,)
			chrom_slice_areas = slice_areas.isel(non_motion_marker=i).data  # shape: (n_slices,)
		except Exception as e:
			click.secho(f"Error retrieving data for chromatophore index {i}: {e}", fg='red')
			continue

		slice_angles = list(reversed(np.linspace(0, 360, n_slices + 1)[:-1]))
		for j, (label_val, s_area, angle) in enumerate(zip(chrom_slice_labels, chrom_slice_areas, slice_angles)):
			start_angle = 270 - angle0 + angle
			end_angle = start_angle + (360 / n_slices)
			wedge = patches.Wedge(
				(center[1], center[0]),  # (x, y) if centers are [y, x]
				s_area,  # using the slice area as the wedge radius
				start_angle,
				end_angle,
				facecolor=cluster_color.get(label_val, (1, 1, 1, 1)),
				edgecolor='white',
				lw=1,
				alpha=1.0
			)
			plt.gca().add_patch(wedge)

	plt.scatter(centers.data[:, 1], centers.data[:, 0], color='red', s=30, marker='x')


	plt.axis("off")
	plt.title("Slice Area Clustering")
	if output_dir:
		os.makedirs(output_dir, exist_ok=True)
		output_path = os.path.join(output_dir, f"slice_cluster_chunk_{chunk_int}.png")
		plt.savefig(output_path, dpi=300, bbox_inches='tight')
		click.echo(f"Saved slice cluster plot to {output_path}")
	else:
		plt.show()
	plt.close()
