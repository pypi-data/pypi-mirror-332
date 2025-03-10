import traceback

import click
import numpy as np
import xarray as xr

from ..utils.decorators import error_handler
from .ica_utils import compute_pca_ica


def chunk_pca_ica(dataset: str, chunk_int: int, chrom_subset=None, n_slices=36):

	areas = xr.open_zarr(dataset, group=f'chunk_{chunk_int}').areas.sel(chromatophore=chrom_subset).compute()
	n_frames = areas.shape[0]
	print(f'{n_frames=}, {areas.shape=}')
	
	ep, ev, isrc, mm, inf = compute_pca_ica(areas)

	print(f'{ep.shape=}, {ev.shape=}, {isrc.shape=}, {mm.shape=}, {inf.shape=}')
	
	ica = xr.Dataset(
		{
			'explained_variance': xr.DataArray(ev, dims=['frame']),
			'ica_sources': xr.DataArray(isrc, dims=['diff', 'component']),
			'mixing_matrix': xr.DataArray(mm, dims=['chrom', 'component']),
			'influence': xr.DataArray(inf, dims=['chrom', 'component']),
		},
		coords={'chrom': chrom_subset, 'frame': np.arange(n_frames), 'diff': np.arange(n_frames-1), 'component': np.arange(ep)},
		attrs={'n_ic': ep}
	)

	ica.to_zarr(dataset, group=f'ica_area_chunk_{chunk_int}', mode='w')

	
@error_handler('ICA (areas)', cluster=False)
def ica(dataset_path: str, chunk_int: int, n_slices: int=36) -> None:
	try:
		click.secho(f'Run ICA on chunk {chunk_int} of {dataset_path}', fg='blue')
		chunk = xr.open_zarr(dataset_path, group=f'chunk_{chunk_int}', consolidated=True)
		available_chrom_ids = chunk.non_anchor.data
		chunk_pca_ica(dataset_path, chunk_int, chrom_subset=available_chrom_ids, n_slices=n_slices)

	except Exception as e: 
		click.secho(f'\n\n--------> Error:\n\n{"".join(traceback.format_exception(e))}', fg='red')
		click.secho('\ICA failed!', fg='red', bold=True)
		return False
	else:
		click.secho('ICA done.', fg='green', bold=True)
		return True
