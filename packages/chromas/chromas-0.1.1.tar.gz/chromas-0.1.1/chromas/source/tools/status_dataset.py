from pathlib import Path

import click
import xarray as xr


def status_dataset(dataset: str) -> None:

    click.secho(f'\n{str(dataset)}', bold=True)

    dataset_path = Path(dataset)
    if not dataset_path.exists():
        click.secho('Dataset does not exist!', fg='red')
        return

    try:
        chunking = xr.open_zarr(dataset, 'chunking')
        nr_chunks = chunking.sizes['chunk']
        click.secho(f'Chunking:\t\u2714\t({nr_chunks} chunk{"s" if nr_chunks > 1 else ""})', fg='green')
    except:
        click.secho('Chunking:\t\u2718', fg='red')
        return
    
    try:
        chunk = xr.open_zarr(dataset, 'chunk_0')
        frames = chunk.sizes['frame']
        click.secho(f'Segmentation:\t\u2714\t({frames} frame{"s" if frames > 1 else ""})', fg='green')
    except:
        click.secho('Segmentation:\t\u2718', fg='red')
        return
    
    if 'masterframe' in chunk:
        click.secho('Registration:\t\u2714\t', fg='green')
    else:
        click.secho('Registration:\t\u2718', fg='red')
        return
    
    try:
        stitching = xr.open_zarr(dataset, 'stitching')
        click.secho('Stitching:\t\u2714', fg='green')
    except:
        click.secho('Stitching:\t\u2718', fg='red')
        return
    
    if 'areas' in chunk:
        click.secho('Areas:\t\t\u2714\t', fg='green')
    else:
        click.secho('Areas:\t\t\u2718', fg='red')
        return
    
    if (dataset_path / 'chunk_0/._motion_marker_params.json').exists():
        click.secho('MM chosen:\t\u2714\t', fg='green')
    else:
        click.secho('MM chosen:\t\u2718', fg='red')
        return
    
    if 'slice_areas' in chunk:
        click.secho('Slice areas:\t\u2714\t', fg='green')
    else:
        click.secho('Slice areas:\t\u2718', fg='red')
        return
    

    




