"""
Area Clustering Module.

This module provides functionality for clustering chromatophores based on their area
time series and for visualizing the resulting clusters. The clustering is performed by computing
a correlation matrix between chromatophore time series and then applying a clustering algorithm
(e.g., AffinityPropagation). The module also includes a function to visualize the clustering results
by overlaying segmentation data on an image.

Functions:
	cluster_areas(dataset: str, chunk_int: int, method: str = 'AffinityPropagation', 
				   clustering_kwargs: dict = None, max_tries: int = 5,
				   debug_args: dict = None)
		Clusters chromatophores based on area correlations and stores the results.
	visualize_clustering(dataset: str, chunk_int: int)
		Overlays segmented regions on an image using cluster labels.
"""

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import os
from skimage.segmentation import mark_boundaries
import click
import matplotlib
import zarr
import matplotlib.cm as cm
from ..utils.decorators import error_handler, convergence_handler
from .clustering_utils import cluster_correlation


@error_handler('Areas clustering', cluster=False)
def cluster_areas(dataset: str, chunk_int: int, method: str = 'AffinityPropagation',
				  clustering_kwargs: dict = None, max_tries: int = 5,
				  debug_args: dict = None):
	"""
	Cluster chromatophores based on the correlation of their area time series.

	This function loads area data from the specified dataset (in zarr format), aligns the data across
	frames, computes the correlation matrix between chromatophores, and applies a clustering algorithm
	(by default, AffinityPropagation) to assign cluster labels. The computed labels and related parameters
	are then stored back into the dataset. Optionally, if debugging visualization is enabled, the clustering
	results can be visualized.

	Args:
		dataset (str): Path to the dataset (zarr store).
		chunk_int (int): The chunk index from which to load data. If None or a list, multiple chunks are used.
		method (str, optional): The clustering method to use. Defaults to 'AffinityPropagation'.
		clustering_kwargs (dict, optional): Additional keyword arguments for the clustering algorithm.
			Defaults to None.
		max_tries (int, optional): Maximum number of attempts for convergence. Defaults to 5.
		debug_args (dict, optional): Dictionary with debugging options. For example:
			{'debug': False, 'debug_visual': False}. Defaults to None.

	Returns:
		None
	"""
	# Initialize mutable defaults.
	if clustering_kwargs is None:
		clustering_kwargs = {}
	if debug_args is None:
		debug_args = {'debug': False, 'debug_visual': False}

	# LOAD DATA:
	if chunk_int is None:
		chunknames = [chunk for chunk in zarr.open(dataset).keys() if chunk.startswith('chunk_')]
		group = 'area_clustering'
	elif isinstance(chunk_int, list):
		chunknames = [f'chunk_{chunk}' for chunk in chunk_int]
		group = 'area_clustering'
	elif isinstance(chunk_int, int):
		chunknames = [f'chunk_{chunk_int}']
		group = f'chunk_{chunk_int}/area_clustering'
	else:
		raise ValueError(f'{chunk_int=} not valid.')

	chunks = [xr.open_zarr(dataset, group=chunk) for chunk in chunknames]
	areas = [chunk.areas.data.compute() for chunk in chunks]

	if debug_args['debug']:
		click.echo(f'[DEBUG] Using chunknames = {chunknames!r}.')
		click.echo(f'[DEBUG] Using group = {group!r}.')
		click.echo('[DEBUG] Areas shapes: ' + '; '.join([str(a.shape) for a in areas]))

	# Align the areas arrays by concatenating along the frames axis.
	# Resulting shape: (n_frames_total, n_chromatophores)
	areas = np.concatenate(areas, axis=0)

	if debug_args['debug']:
		click.echo(f'[DEBUG] Aligned areas shape: {areas.shape}')

	# Compute the correlation matrix between chromatophores (columns)
	# Using rowvar=False so that each column is considered a variable.
	corr = np.corrcoef(areas, rowvar=False)
	corr = np.nan_to_num(corr, nan=0.0)

	if debug_args['debug']:
		click.echo(f'{corr.shape=}')
	if debug_args['debug_visual']:
		plt.imshow(corr, cmap='Blues')
		plt.title("Correlation matrix")
		plt.xlabel("Chrom")
		plt.ylabel("Chrom")
		plt.colorbar()
		plt.show()

	labels = convergence_handler(cluster_correlation, max_tries=max_tries)(corr, method, **clustering_kwargs)

	click.echo(f'Found {len(np.unique(labels))} clusters.')
	if debug_args['debug']:
		click.echo(f'[DEBUG] {labels.shape=}, {labels.min()=}, {labels.max()=}')

	# STORE DATA:
	zarr_store = zarr.open(dataset, mode='a')
	if group in zarr_store.keys():
		if 'labels' in zarr_store[group]:
			click.secho('WARNING: Removing `labels` from dataset since it already exists.', italic=True)
			del zarr_store[f'{group}/labels']
			# Optionally, wait for deletion if necessary:
			while 'labels' in zarr_store:
			    pass

	labels_ds = xr.Dataset({
		'labels': xr.DataArray(
			labels,
			attrs={
				'chunk_int': chunk_int,
				'method': method,
				'max_tries': max_tries,
				**clustering_kwargs
			}
		)
	})
	labels_ds.to_zarr(dataset, group=group, mode='a')

	if debug_args['debug_visual']:
		visualize_clustering(dataset, chunk_int)


def visualize_clustering(dataset: str, chunk_int: int):
	"""
	Visualize the area clustering by overlaying segmented regions on an image.

	This function loads the clustering labels and segmentation images (queenframe and cleanqueen)
	from the dataset and overlays each chromatophore's segmented region with a color corresponding to
	its cluster label. The segmentation is based on the 'stitching' group within the dataset.

	Args:
		dataset (str): Path to the dataset (zarr store).
		chunk_int (int): The chunk index to load data from. If None or a list, the default group is used.

	Returns:
		None
	"""
	# LOAD DATA:
	if chunk_int is None or isinstance(chunk_int, list):
		group = 'area_clustering'
	elif isinstance(chunk_int, int):
		group = f'chunk_{chunk_int}/area_clustering'
	else:
		raise ValueError(f'{chunk_int=} not valid.')

	# Load clustering labels.
	try:
		labels_ds = xr.open_zarr(dataset, group=group)
	except Exception as e:
		click.secho(f"Error loading labels from group '{group}': {e}", fg='red')
		return
	# Assume labels are stored in a variable named "labels" as a 1D array.
	labels = labels_ds.labels.data.compute()

	try:
		# Load the stitching group to obtain queenframe and cleanqueen.
		stitching = xr.open_zarr(dataset, group='stitching')
		queenframe = stitching.queenframe.data.compute()
		cleanqueen = stitching.cleanqueen.data.compute()
	except Exception as e:
		click.secho(f"Error loading image data: {e}", fg='red')
		return

	# Get the list of chromatophore IDs (exclude background assumed to be 0).
	chrom_ids = np.unique(cleanqueen)
	chrom_ids = chrom_ids[chrom_ids != 0]

	# Determine unique cluster labels and build a colormap.
	unique_clusters = np.unique(labels)
	cmap = cm.get_cmap("tab20", len(unique_clusters))
	# Map each cluster label to a color (RGBA tuple)
	cluster_color = {cluster: cmap(i) for i, cluster in enumerate(unique_clusters)}

	# Create a blank plot frame with a white background.
	plot_frame = np.full(queenframe.shape + (3,), 255, dtype=np.uint8)
	plot_frame[queenframe > 0] = 0

	# For each chromatophore, overlay its region in the color of its cluster.
	for chrom_id in chrom_ids:
		# Assuming chromatophore IDs are 1-indexed, get the label from the labels array.
		idx = int(chrom_id) - 1
		if idx < 0 or idx >= len(labels):
			continue  # skip if the index is out of range
		cluster_label = labels[idx]
		color = cluster_color[cluster_label]

		# Create a mask from cleanqueen (using queenframe as additional filter)
		mask = (cleanqueen == chrom_id) & (queenframe > 0)
		plot_frame[mask] = (np.array(color[:3]) * 255).astype(np.uint8)  # convert RGBA [0,1] to RGB [0,255]

	# Create a plot.
	fig, ax = plt.subplots()
	ax.imshow(plot_frame)
	ax.axis("off")
	ax.set_title("Area Clustering")
	plt.show()
