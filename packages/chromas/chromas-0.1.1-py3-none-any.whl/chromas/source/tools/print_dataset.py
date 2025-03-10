import xarray as xr
import click

def print_dataset(ds: xr.Dataset):
    chunking = xr.open_zarr(ds, 'chunking')
    nr_chunks = chunking.sizes['chunk']

    click.echo(f"Number of chunks: {nr_chunks}")

    for chunk in range(nr_chunks):
        click.secho(f"\nChunk {chunk}:", bold=True)
        chunk = xr.open_zarr(ds, f'chunk_{chunk}')
        # Echo chunk tabbed:
        click.echo(chunk) 
        