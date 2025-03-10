import traceback

import click
import numpy as np
import xarray as xr
import zarr
from tqdm import tqdm

from ..utils.decorators import error_handler
from .ica_utils import compute_pca_ica


def chunk_pca_ica(dataset: str, chunk: int|None, slice_areas: xr.DataArray, chrom_subset, n_slices=36):

	n_frames = slice_areas.shape[0]

	elbow_points = np.zeros(len(chrom_subset), dtype='uint8')
	explained_variances = np.zeros((len(chrom_subset), n_slices), dtype='float32')
	ica_sources = np.zeros((len(chrom_subset), n_frames-1, n_slices), dtype='float32')
	mixing_matrices = np.zeros((len(chrom_subset), n_slices, n_slices), dtype='float32')
	influences = np.zeros((len(chrom_subset), n_slices, n_slices), dtype='float32')
	
	for j, chrom_id in enumerate(tqdm(chrom_subset, desc='Run PCA-ICA', total=len(chrom_subset), unit='chrom')):
		slice_area = slice_areas.sel(non_motion_marker=chrom_id).data
		try:
			ep, ev, isrc, mm, inf = compute_pca_ica(slice_area)
			elbow_points[j] = ep
			explained_variances[j] = ev
			ica_sources[j, :, :ep] = isrc
			mixing_matrices[j, :, :ep] = mm
			influences[j, :, :ep] = inf
		except Exception as e:
			click.secho(f'Error in chrom_id {chrom_id}: {e}, {traceback.print_exc()}', fg='red', bold=True)
			continue

	# Save the results
	elbow_points_da = xr.DataArray(elbow_points, dims='chrom_id', name='elbow_point', coords={'chrom_id': chrom_subset})
	explained_variances_da = xr.DataArray(explained_variances, dims=('chrom_id', 'slice'), name='explained_variance', coords={'chrom_id': chrom_subset, 'slice': np.arange(n_slices)})
	ica_sources_da = xr.DataArray(ica_sources, dims=('chrom_id', 'diff', 'component'), name='ica_sources', coords={'chrom_id': chrom_subset, 'diff': np.arange(n_frames-1), 'component': np.arange(n_slices)})
	mixing_matrices_da = xr.DataArray(mixing_matrices, dims=('chrom_id', 'slice', 'component'), name='mixing_matrix', coords={'chrom_id': chrom_subset, 'slice': np.arange(n_slices), 'component': np.arange(n_slices)})
	influences_da = xr.DataArray(influences, dims=('chrom_id', 'slice', 'component'), name='influence', coords={'chrom_id': chrom_subset, 'slice': np.arange(n_slices), 'component': np.arange(n_slices)})

	ica = xr.Dataset({
		'elbow_point': elbow_points_da,
		'explained_variance': explained_variances_da,
		'ica_sources': ica_sources_da,
		'mixing_matrix': mixing_matrices_da,
		'influence': influences_da
	})

	if isinstance(chunk, int):
		ica.to_zarr(dataset, group=f'ica_chunk_{chunk}', mode='w')
	else:
		ica.to_zarr(dataset, group='ica', mode='w')

	
@error_handler('ICA', cluster=False)
def ica(dataset: str, chunk_int: int, n_slices: int=36) -> None:

	if isinstance(chunk_int, int):
		click.secho(f'Run ICA on chunk {chunk_int} of {dataset}')
		chunk = xr.open_zarr(dataset, group=f'chunk_{chunk_int}', consolidated=True)
		available_chrom_ids = chunk.non_motion_markers.data
		slice_areas = chunk.slice_areas.compute()
		chunk_pca_ica(dataset, chunk_int, slice_areas, chrom_subset=available_chrom_ids, n_slices=n_slices)
	else:
		click.secho('Run ICA on full dataset.')

		chunknames = [chunk for chunk in zarr.open(dataset).keys() if chunk.startswith('chunk_')]
		chunks = [xr.open_zarr(dataset, group=chunk) for chunk in chunknames]
		try:
			chunk_mask = xr.open_zarr(dataset, 'stitching').chunk_mask.data
			chunknames = [c for c, m in zip(chunknames, chunk_mask) if m]
			chunks = [c for c, m in zip(chunks, chunk_mask) if m]
			click.echo(f'Chunknames: {chunknames}')
		except:
			pass
		chunklengths = [chunk.sizes['frame'] for chunk in chunks]
		non_motion_markers = [set(c.non_motion_markers.values) for c in chunks]
		common_chroms = sorted(set.intersection(*non_motion_markers))
		click.secho([len(m) for m in non_motion_markers])
		click.secho(f'Running ICA on {len(common_chroms)} chroms.')
		click.secho([len(c.motion_marker.values) for c in chunks])
		click.secho(len(set.intersection(*[set(c.motion_marker.values) for c in chunks])))


		# Step 2: Subset all xarrays to common 'chroms'
		all_sliceareas = [chunk.slice_areas.sel(non_motion_marker=common_chroms).compute() for chunk in chunks]

		# Step 3: Adjust 'frame' coordinate and concatenate
		adjusted_arrays = []
		cumulative_frame = 0
		for arr, length in zip(all_sliceareas, chunklengths):
			# Update the 'frame' coordinate to global frame indices
			adjusted_arr = arr.assign_coords(frame=(arr['frame'] + cumulative_frame))
			adjusted_arrays.append(adjusted_arr)
			cumulative_frame += length

		# Step 4: Concatenate along the 'frame' dimension
		sliceareas = xr.concat(adjusted_arrays, dim='frame')
	
		chunk_pca_ica(dataset, None, sliceareas, chrom_subset=common_chroms, n_slices=n_slices)

