""" Tools to track the isotropic expansion of chromatophores. """

from pathlib import Path
import time
import click
import numpy as np
import pandas as pd
import dask.array as da
import xarray as xr
import zarr
import matplotlib.pyplot as plt
import cv2
from skimage.segmentation import mark_boundaries
from typing import Optional
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
from dash import dcc, html, callback, Input, Output, Dash
import plotly.express as px
from ..utils.utils import clear_edges, make_cleanqueen
from ..utils.decorators import error_handler



def warp_frame(image: np.ndarray|list[np.ndarray], maps: np.ndarray, border_value: int=255, grid_size: int=32,
			   frame_shape: tuple=(1, 1), remove_border: int=0) -> np.ndarray|list[np.ndarray]:


	scale_up_transform = np.array([
				[grid_size, 0, 0],
				[0, grid_size, 0],
			], 'float32')
	maps = cv2.warpAffine(maps, scale_up_transform, frame_shape[::-1], flags=cv2.INTER_LINEAR)

	def set_border_values(image, border_value, remove_border):
		if remove_border:
			image[:remove_border] = border_value
			image[-remove_border:] = border_value
			image[:, :remove_border] = border_value
			image[:, -remove_border:] = border_value
		return image
	
	if isinstance(image, np.ndarray) or isinstance(image, da.Array):
		y = cv2.remap(image, maps, None, interpolation=cv2.INTER_NEAREST, borderMode=cv2.BORDER_CONSTANT, borderValue=border_value)
		return set_border_values(y, border_value, remove_border)
	elif isinstance(image, list):
		y = list(cv2.remap(i, maps, None, interpolation=cv2.INTER_NEAREST, borderMode=cv2.BORDER_CONSTANT, borderValue=border_value) for i in image)
		y = [set_border_values(i, border_value, remove_border) for i in y]
		return y	

	else:
		raise ValueError(f'Invalid input type of image {type(image)}.')
	

def compute_areas(segmentation: np.ndarray, cleanqueen: np.ndarray, minlength: Optional[int] = None) -> np.ndarray:
	"""
	Compute areas of chromatophores.

	Args:
		segmentation (np.ndarray): The segmentation array.
		cleanqueen (np.ndarray): The cleanqueen array.
		minlength (Optional[int], optional): Minimum length for bincount. Defaults to None.

	Returns:
		np.ndarray: The computed areas.

	Raises:
		ValueError: If segmentation and cleanqueen have incompatible shapes.
	
	Note:
		The area of a chromatophore is calculated as the number of pixels within the largest connected component of the segmentation that falls inside the corresponding territory.
	"""
	if minlength is None:
		minlength = np.max(cleanqueen) + 1
	
	if segmentation.ndim == cleanqueen.ndim == 2 and segmentation.shape == cleanqueen.shape:
		return np.bincount(cleanqueen[segmentation>0], minlength=minlength)[:minlength].astype(np.uint16)
	elif segmentation.ndim == cleanqueen.ndim == 3 and segmentation.shape == cleanqueen.shape:
		y = [np.bincount(clq[seg>0], minlength=minlength)[:minlength].astype(np.uint16) 
			 for clq, seg in zip(cleanqueen, segmentation)]
		return np.stack(y, axis=0)
	else:
		raise ValueError(f"segmentation ({segmentation.shape=}) and cleanqueen ({cleanqueen.shape=}) must have the same shape")


def chunk_areas(chunk: xr.Dataset, remove_border: bool|int=False, datagroup: str=None, name: str=None) -> tuple[xr.DataArray, xr.DataArray]:
	
	grid_size = chunk.pullbacks.attrs['grid_size']
	cleanqueen = chunk.cleanqueen.data.compute()

	def _warp_cleanqueen(x, cleanqueen, remove_border):
		return np.expand_dims(warp_frame(cleanqueen, x[0], border_value=0, remove_border=remove_border,
										 grid_size=grid_size, frame_shape=cleanqueen.shape), 0)
	

	warped_cleanqueen = da.map_blocks(_warp_cleanqueen,
								   chunk.pushforwards.data.rechunk((1, chunk.sizes['x_grid'], chunk.sizes['y_grid'], 2)),
								   cleanqueen, remove_border,
								   dtype=np.uint16, chunks=(1, chunk.sizes['x'], chunk.sizes['y']), drop_axis=3)
	
	warped_cleanqueen = xr.DataArray(warped_cleanqueen, dims=('frame', 'x', 'y'), name='warped_cleanqueen')

	click.secho(f'Cleanqueen warped and stored for chunk {name} in {datagroup}.', color='green')
	time.sleep(1)
	
	minlength = cleanqueen.max() + 1

	def _compute_areas(*args, **kwargs):
		return compute_areas(*args, **kwargs, minlength=minlength)

	areas = da.map_blocks(_compute_areas, chunk.segmentation.data.rechunk((1,  chunk.sizes['x'], chunk.sizes['y'])),
					   warped_cleanqueen.data.rechunk((1,  chunk.sizes['x'], chunk.sizes['y'])),
					   dtype=np.uint16, chunks=(1, minlength), drop_axis=[1, 2], new_axis=[1])
		
	areas = xr.DataArray(areas, dims=('frame', 'chromatophore'))
	warped_cleanqueen.to_dataset(name='warped_cleanqueen').to_zarr(datagroup, mode='a', group=name)
	areas.to_dataset(name='areas').to_zarr(datagroup, mode='a', group=name)
	return True


# MAIN FUNCTION:
@error_handler('Areas')
def areas(datagroup: str, chunk_selection: list[int]=[], compute_cleanqueen: bool=True, cleanqueen_kwargs: dict=None,
		  cluster_args: dict={'processes': False, 'n_workers': 1, 'threads_per_worker': 4},
		  debug_args: dict={'debug': False, 'debug_visual': False}) -> None:

	if not chunk_selection:
		chunknames = [chunk for chunk in zarr.open(datagroup).keys() if chunk.startswith('chunk_')]
	else:
		chunknames = [f'chunk_{chunk}' for chunk in chunk_selection]
	chunks = [xr.open_zarr(datagroup, group=chunk) for chunk in chunknames]

	click.echo(f'Processing {len(chunks)} chunks.')
	if not chunks:
		raise ValueError("No chunks found in the provided data group.")
	
	zarr_store = zarr.open(datagroup, mode='a')
	for chunkname in chunknames:
		for var in ['areas', 'warped_cleanqueen', 'chromatophore']:
			if var in zarr_store[chunkname]:
				click.secho(f'WARNING: Removing {var} from {chunkname} since it already exists.', fg='yellow', italic=True)
				del zarr_store[f'{chunkname}/{var}']
				# Wait for the deletion to finish
				while var in zarr_store[chunkname]:
					pass
	
	queenframe = xr.open_zarr(datagroup, group='stitching').queenframe.data.compute()
	
	if compute_cleanqueen and 'cleanqueen' in zarr_store['stitching']:
		click.secho('Removing cleanqueen from stitching group since it already exists.', fg='yellow', italic=True)
		del zarr_store['stitching/cleanqueen']

	if compute_cleanqueen:
		cleanqueen = make_cleanqueen(queenframe, **cleanqueen_kwargs, debug_args=debug_args)

		if debug_args['debug_visual']:
			plt.imshow(mark_boundaries(queenframe, cleanqueen))
			plt.title('Cleanqueen')
			plt.show()

		# Store the cleanqueen in the chunk
		cleanqueen_z = xr.DataArray(cleanqueen, dims=('x', 'y'), name='cleanqueen')
		cleanqueen_z.to_dataset(name='cleanqueen').to_zarr(datagroup, mode='a', group='stitching')
	
	if len(chunknames) > 1:
		# Warp the cleanqueen to each chunk:
		stitching = xr.open_zarr(datagroup, group='stitching')
		cleanqueen = stitching.cleanqueen.data.compute()
		stitching_matrix = stitching.stitching_matrix.data.compute()
		mf_shape = stitching.queenframe.shape
		grid_size = stitching.stitching_matrix.attrs['grid_size']
		ref_chunk = stitching.stitching_matrix.attrs['ref_chunk']

		try:
			chunk_mask = stitching.chunk_mask.data
			chunknames = [c for c, m in zip(chunknames, chunk_mask) if m]
		except:
			pass
	
	print(f'{len(chunknames)=}')
	for chunkname in chunknames:
		chunk = xr.open_zarr(datagroup, group=chunkname)
		chunk_idx = int(chunkname.split('_')[-1])
		if len(chunknames) == 1 or chunk_idx == ref_chunk:
			warped_cleanqueen = cleanqueen.copy()
		else:
			grow_t = np.array([[grid_size, 0., 0.], [0., grid_size, 0.]], 'float32')
			maps = cv2.warpAffine(stitching_matrix[chunk_idx, ref_chunk], grow_t, mf_shape[::-1])
			warped_cleanqueen = cv2.remap(cleanqueen.astype('float64'), maps, None, interpolation=cv2.INTER_NEAREST, borderMode=cv2.BORDER_CONSTANT).astype('int32')
			warped_cleanqueen = clear_edges(warped_cleanqueen, 10)
			if debug_args['debug_visual']:
				plt.imshow(mark_boundaries(chunk.masterframe.data.compute(), warped_cleanqueen))
				plt.axis('off')
				plt.title(f'Cleanqueen warped into chunk {chunk_idx}')
				plt.show()

		warped_cleanqueen = xr.DataArray(warped_cleanqueen, dims=('x', 'y'), name='cleanqueen')
		warped_cleanqueen.to_dataset(name='cleanqueen').to_zarr(datagroup, mode='a', group=chunkname)

	click.echo(f'{len(np.unique(cleanqueen))-1} chromatophores found in cleanqueen.')

	chunks = [xr.open_zarr(datagroup, group=chunk) for chunk in chunknames]
	with click.progressbar(zip(chunknames, chunks), len(chunks), label='Compute areas') as bar:
		for name, chunk in bar:
			chunk_areas(chunk, remove_border=10, datagroup=datagroup, name=name)
	

#################################################################################################################!
############# VISUALIZATION FUNCTIONS ###########################################################################!
#################################################################################################################!
@error_handler('Show areas', cluster=False)
def show_areas(datagroup: str, chunk: int, no_interactive: bool=False) -> None:
	chunk_int = int(chunk)
	chunk = xr.open_zarr(datagroup, group=f'chunk_{chunk}')
	areas = chunk.areas.data.compute()
	clq = chunk.warped_cleanqueen[0].data.compute()
	masterframe = chunk.masterframe.data.compute()

	if no_interactive:
		plt.plot(areas[:, 1:])
		plt.title(f'Areas for chunk {chunk_int}')
		plt.show()
		return

	app = Dash(__name__)

	# Example data
	image = (mark_boundaries(masterframe / masterframe.max(), clq) * 255).astype(np.uint8)
	graphs = areas.T

	m, n = graphs.shape
	df = pd.DataFrame({
		'chromatophore': np.repeat(np.arange(m), n),
		'frame': np.tile(np.arange(n), m),
		'size': graphs.flatten()
	})

	# Create the initial plotly figure
	fig = make_subplots(rows=1, cols=2, column_widths=[0.5, 0.5],
						subplot_titles=("Cleanqueen", "Areas"))

	# Add the image to the left subplot
	fig.add_trace(
		go.Image(z=image),
		row=1, col=1
	)

	# Add the areas to the right subplot
	plot = px.line(df.query('chromatophore != 0'), x='frame', y='size', color='chromatophore')
	for trace in plot.data:
		fig.add_trace(trace, row=1, col=2)
	fig.update_xaxes(title_text='Frame', row=1, col=2)
	fig.update_yaxes(title_text='Size', row=1, col=2)

	fig.update_layout(title_text='Interactive areas plot', hovermode='closest')

	# Make both subplots fill out the maximum width and height of the window:
	fig.update_layout(
		width=2000,
		height=1000,
	)

	# Define the layout of the Dash app
	app.layout = html.Div([
		dcc.Graph(id='interactive-plot', figure=fig),
		dcc.Store(id='cleanqueen-image', data=image.tolist()),
		dcc.Store(id='cleanqueen-array', data=clq.tolist())
	])

	# Define the callback to update the image and highlight the line on hover
	@callback(
		Output('interactive-plot', 'figure'),
		Input('interactive-plot', 'clickData'),
		Input('cleanqueen-image', 'data'),
		Input('cleanqueen-array', 'data'),
	)
	def update_image_on_click(clickData, cleanqueen_image, cleanqueen_array):
		if clickData is None:
			return dash.no_update

		chromatophore = clickData['points'][0]['curveNumber']
		if fig['data'][chromatophore]['name'] is None:
			return dash.no_update
		
		label = int(fig['data'][chromatophore]['name'])

		cleanqueen_image = np.array(cleanqueen_image)
		cleanqueen_array = np.array(cleanqueen_array)

		# Overlay yellow half-transparent where the chromatophore is
		highlighted_image = cleanqueen_image.copy()
		highlighted_image[cleanqueen_array == label] = np.array([255, 255, 0]) * 0.5 + 0.5 * cleanqueen_image[cleanqueen_array == label]
		fig['data'][0]['z'] = highlighted_image
		# Highlight the corresponding line in the line plot
		for trace in fig['data'][1:]:
			if trace['name'] == label:
				trace['line']['width'] = 16
			else:
				trace['line']['width'] = 2

		print(f'Clicked on chromatophore {label}')

		return fig

	app.run_server(debug=True)


@error_handler('Show cleanqueen', cluster=False)
def show_cleanqueen(dataset: str, chunk: int|str, frame: int, raw: bool=False, id: int|None=None) -> None:
	import decord
	# Check that dataset is a directory
	
	chunk_data = xr.open_zarr(dataset, group=f'chunk_{chunk}')
	if isinstance(chunk, int) and chunk == -1:
		clq = xr.open_zarr(dataset, group='stitching').cleanqueen.data.compute()
	else:
		if frame == 0:
			clq = chunk_data.cleanqueen.data.compute()
		else:
			clq = chunk_data.warped_cleanqueen.isel(frame=frame).data.compute()

	vr = decord.VideoReader(chunk_data.segmentation.attrs['chunk_path'])
	img = vr.get_batch([frame]).asnumpy()[0]
	
	if id is not None:
		img = clq == id
	elif not raw:
		img = mark_boundaries(img, clq, color=(1, 0, 0))
	else:
		img = clq
	plt.imshow(img)
	plt.title(f'Cleanqueen on frame {frame}')

	plt.show()


@error_handler('Generate cleanqueen video', cluster=False)
def generate_cleanqueen_video(dataset: str, chunk: int, output: str=None, fps: int=None, start: int=None, end: int=None) -> None:
	import decord
	assert Path(dataset).is_dir(), f'{dataset} is not a valid dataset. Generate-cleanqueen-video does not take videos as input, but datasets geneated through e.g. segmentation.'
	if output is not None:
		assert Path(output).suffix == '.mp4', 'Output must be an mp4 file.'
		assert Path(output).parent.exists(), f'Output directory {Path(output).parent} does not exist.'
		assert not Path(output).exists(), f'Output file {output} already exists.'
	else:
		output = str(Path(dataset).with_suffix(f'.chunk_{chunk}_cleanqueen_overlay.mp4'))
	
	chunk = xr.open_zarr(dataset, group=f'chunk_{chunk}')
	try:
		vr = decord.VideoReader(chunk.segmentation.attrs['chunk_path'])
	except RuntimeError:
		absolute_path = Path(chunk.segmentation.attrs['chunk_path']).absolute()
		vr = decord.VideoReader(str(Path(dataset).parent / absolute_path.name))
	decord.bridge.set_bridge('native')
	if fps is not None:
		assert fps > 0, 'FPS must be a positive number.'
		assert isinstance(fps, int), 'FPS must be an integer.'
	else:
		fps = vr.get_avg_fps()
	if start is not None:
		assert start >= 0, 'Start frame must be a non-negative integer.'
		start = start * int(vr.get_avg_fps())
	else:
		start = 0
	if end is not None:
		end = end * int(vr.get_avg_fps())
		assert end > start, 'End frame must be greater than start frame.'
	else:
		end = len(vr)-1
	

	vw = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*'mp4v'), fps, (chunk.segmentation.shape[2], chunk.segmentation.shape[1]))

	with click.progressbar(range(start, end), label='Generating cleanqueen video', show_percent=True, show_pos=True) as bar:
		for i in bar:
			img = vr.get_batch([i]).asnumpy()[0]
			segmentation = chunk.segmentation.isel(frame=i).data.compute()
			warped_cleanqueen = chunk.warped_cleanqueen.isel(frame=i).data.compute()
			
			img = mark_boundaries(img, segmentation==1, color=(0, 0, 1))
			img = mark_boundaries(img, segmentation==2, color=(0, 1, 0))
			img = mark_boundaries(img, segmentation==3, color=(1, 0, 0))
			img = mark_boundaries(img, warped_cleanqueen, color=(1, 0, 1))

			vw.write((img * 255).astype(np.uint8)[..., ::-1])

	vw.release()
	click.secho(f'\nCleanqueen video saved to {output}', fg='green')
