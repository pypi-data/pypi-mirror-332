
from pathlib import Path

import click
import cv2
import numpy as np
import xarray as xr

from skimage.segmentation import mark_boundaries

from ..utils.decorators import error_handler


@error_handler('Generating motion marker', cluster=False)
def generate_motion_marker_video(dataset: str, chunk: int, motion_marker_centers: np.ndarray, interpolation_indicator: np.ndarray,
								 output: str=None, fps: int=None, start: int=None, end: int=None, buffer: int=0) -> None:
	assert Path(dataset).is_dir(), f'{dataset} is not a valid dataset. Show-slicing does not take videos as input, but datasets geneated through e.g. slicing.'
	if output is not None:
		assert Path(output).suffix == '.mp4', 'Output must be an mp4 file.'
		assert Path(output).parent.exists(), f'Output directory {Path(output).parent} does not exist.'
		assert not Path(output).exists(), f'Output file {output} already exists.'
	else:
		output = str(Path(dataset).with_suffix(f'.chunk_{chunk}_epicenters.mp4'))
	
	chunk = xr.open_zarr(dataset, group=f'chunk_{chunk}')
	try:
		cap = cv2.VideoCapture(chunk.segmentation.attrs['chunk_path'])
	except RuntimeError:
		absolute_path = Path(chunk.segmentation.attrs['chunk_path']).absolute()
		cap = cv2.VideoCapture(str(Path(dataset).parent / absolute_path.name))
	if fps is not None:
		assert fps > 0, 'FPS must be a positive number.'
		assert isinstance(fps, int), 'FPS must be an integer.'
	else:
		fps = cap.get(cv2.CAP_PROP_FPS)
	if start is not None:
		assert start >= 0, 'Start frame must be a non-negative integer.'
		start = start * int(cap.get(cv2.CAP_PROP_FPS))
	else:
		start = 0
	if end is not None:
		end = end * int(cap.get(cv2.CAP_PROP_FPS))
		assert end > start, 'End frame must be greater than start frame.'
	else:
		end = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1

	vw = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*'mp4v'), fps, (chunk.segmentation.shape[2], chunk.segmentation.shape[1]))
	cap.set(cv2.CAP_PROP_POS_FRAMES, start-1)
	with click.progressbar(range(start, end-1), label='Generating epicenter video', show_percent=True, show_pos=True) as bar:
		for i in bar:
			ret, img = cap.read()
			if not ret:
				click.secho(f'[ERROR] Video ended unexpectedly at frame {i} of {end}.', fg='red', bold=True)
			img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
			seg = chunk.segmentation.isel(frame=i).data.compute()
			clq = chunk.warped_cleanqueen.isel(frame=i).data.compute()
			mm_centers = motion_marker_centers[i]
			mm_indicator = interpolation_indicator[i]
			
			# clq = clear_border(clq, buffer_size=buffer)
			img = mark_boundaries(img, clq, color=(1, 1, 1), mode='thick')
			img = mark_boundaries(img, seg, color=(0, 1, 0), mode='thick')
			img = (img * 255).astype(np.uint8)

			for center, indicator in zip(mm_centers, mm_indicator):
				cv2.circle(img, tuple(center[::-1].astype(int)), 3, (0, 0, 255) if indicator else (255, 0, 0), -1)

			vw.write(img[...,::-1])
	vw.release()
	click.secho(f'Potential motion marker video saved to {output}', fg='green', bold=True)


@error_handler('Generating center video', cluster=False)
def generate_center_video(dataset: str, chunk: int, output: str=None, fps: int=None, start: int=None, end: int=None, buffer: int=0) -> None:
	assert Path(dataset).is_dir(), f'{dataset} is not a valid dataset. Show-slicing does not take videos as input, but datasets geneated through e.g. slicing.'
	if output is not None:
		assert Path(output).suffix == '.mp4', 'Output must be an mp4 file.'
		assert Path(output).parent.exists(), f'Output directory {Path(output).parent} does not exist.'
		assert not Path(output).exists(), f'Output file {output} already exists.'
	else:
		output = str(Path(dataset).with_suffix(f'.chunk_{chunk}_epicenters.mp4'))
	
	chunk = xr.open_zarr(dataset, group=f'chunk_{chunk}')
	try:
		cap = cv2.VideoCapture(chunk.segmentation.attrs['chunk_path'])
	except RuntimeError:
		absolute_path = Path(chunk.segmentation.attrs['chunk_path']).absolute()
		cap = cv2.VideoCapture(str(Path(dataset).parent / absolute_path.name))
	if fps is not None:
		assert fps > 0, 'FPS must be a positive number.'
		assert isinstance(fps, int), 'FPS must be an integer.'
	else:
		fps = cap.get(cv2.CAP_PROP_FPS)
	if start is not None:
		assert start >= 0, 'Start frame must be a non-negative integer.'
		start = start * int(cap.get(cv2.CAP_PROP_FPS))
	else:
		start = 0
	if end is not None:
		end = end * int(cap.get(cv2.CAP_PROP_FPS))
		assert end > start, 'End frame must be greater than start frame.'
	else:
		end = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1

	
	non_motion_markers = chunk.non_motion_markers.data.compute()
	

	vw = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*'mp4v'), fps, (chunk.segmentation.shape[2], chunk.segmentation.shape[1]))
	cap.set(cv2.CAP_PROP_POS_FRAMES, start-1)
	with click.progressbar(range(start, end), label='Generating epicenter video', show_percent=True, show_pos=True) as bar:
		for i in bar:
			ret, img = cap.read()
			if not ret:
				click.secho(f'[ERROR] Video ended unexpectedly at frame {i} of {end}.', fg='red', bold=True)
			img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
			seg = chunk.segmentation.isel(frame=i).data.compute()
			clq = chunk.warped_cleanqueen.isel(frame=i).data.compute()
			centers = chunk.centers.isel(frame=i).data.compute()
			motion_marker_centers = chunk.motion_marker_centers.isel(frame=i).data.compute()
			
			# clq = clear_border(clq, buffer_size=buffer)
			img = mark_boundaries(img, clq, color=(1, 1, 1), mode='thick')
			img = mark_boundaries(img, seg, color=(0, 1, 0), mode='thick')
			img = (img * 255).astype(np.uint8)

			for idx, center in zip(non_motion_markers, centers):
				if np.isnan(center).any():
					continue
				if np.sum(center) == 0:
					continue
				cv2.circle(img, tuple(center[::-1].astype(int)), 3, (0, 0, 255), -1)
			# Scatter motion_marker centers using cv2:
			for ac in motion_marker_centers:
				cv2.circle(img, tuple(ac[::-1].astype(int)), 3, (255, 0, 0), -1)

			vw.write(img[...,::-1])
	vw.release()
	click.secho(f'Center video saved to {output}', fg='green', bold=True)


def rectify_mask(mask, padding = 100, return_limits: bool = False):
	# Find the indices of the True values
	true_indices = np.argwhere(mask)

	# Get the bounding box of the True values
	min_row, min_col = true_indices.min(axis=0)
	max_row, max_col = true_indices.max(axis=0)

	# Add padding
	min_row = max(min_row - padding, 0)
	min_col = max(min_col - padding, 0)
	max_row = min(max_row + padding, mask.shape[0] - 1)
	max_col = min(max_col + padding, mask.shape[1] - 1)
	if return_limits:
		return (min_row, max_row) , (min_col, max_col)
	# Create a new mask with the padded rectangle
	padded_mask = np.zeros_like(mask, dtype=bool)
	padded_mask[min_row:max_row+1, min_col:max_col+1] = True
	return padded_mask


@error_handler('Generating slice video', cluster=False)
def generate_slice_video(dataset: str, chunk: int, output: str=None, fps: int=None, start: int=None, end: int=None, buffer: int=0,
						 interactive: bool=False, individual: bool=False) -> None:
	from matplotlib import collections
	from matplotlib import pyplot as plt
	
	# I/O handling:
	chunk_int = int(chunk)
	assert Path(dataset).is_dir(), f'{dataset} is not a valid dataset. Show-slicing does not take videos as input, but datasets geneated through e.g. slicing.'
	if output is not None:
		assert Path(output).suffix == '.mp4', 'Output must be an mp4 file.'
		assert Path(output).parent.exists(), f'Output directory {Path(output).parent} does not exist.'
		assert not Path(output).exists(), f'Output file {output} already exists.'
	else:
		output = str(Path(dataset).with_suffix(f'.chunk_{chunk}_slice.mp4'))
	
	chunk = xr.open_zarr(dataset, group=f'chunk_{chunk}')
	try:
		cap = cv2.VideoCapture(chunk.segmentation.attrs['chunk_path'])
	except RuntimeError:
		absolute_path = Path(chunk.segmentation.attrs['chunk_path']).absolute()
		cap = cv2.VideoCapture(str(Path(dataset).parent / absolute_path.name))
	if fps is not None:
		assert fps > 0, 'FPS must be a positive number.'
		assert isinstance(fps, int), 'FPS must be an integer.'
	else:
		fps = cap.get(cv2.CAP_PROP_FPS)
	if start is not None:
		assert start >= 0, 'Start frame must be a non-negative integer.'
		start = start * int(cap.get(cv2.CAP_PROP_FPS))
	else:
		start = 0
	if end is not None:
		end = end * int(cap.get(cv2.CAP_PROP_FPS))
		assert end > start, 'End frame must be greater than start frame.'
	else:
		end = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1)

	non_motion_markers = chunk.non_motion_markers.data.compute()
	cleanqueen = chunk.cleanqueen.data.compute()

	if interactive:
		ret, frame_0 = cap.read()
		frame_0 = cv2.cvtColor(frame_0, cv2.COLOR_BGR2RGB)
		plot_frame = mark_boundaries(frame_0, cleanqueen, color=(0, 0, 1))
		selected_chroms = []

		def on_click(event):
			# Get the indices of the clicked point
			x, y = int(event.xdata), int(event.ydata)
			
			# Get the label of the clicked territory
			label = cleanqueen[y, x]

			if label not in non_motion_markers:
				click.secho(f"Clicked on motion marker territory {label}.", fg='yellow')
				return
			
			if label in selected_chroms:
				# If already selected, remove from the list and unhighlight
				selected_chroms.remove(label)
				click.echo(f"Removed: {label}")
			else:
				# If not selected, add to the list and highlight
				selected_chroms.append(label)
				click.echo(f"Added: {label}")
			
			# Redraw the plot with updated highlights
			update_plot()

		def update_plot():
			plt.clf()
			plt.imshow(plot_frame, cmap='viridis')
			
			# Highlight selected territories
			for label in selected_chroms:
				plt.contour(cleanqueen == label, colors='magenta', linewidths=2)
			
			plt.draw()

		# Plot the initial array
		plt.imshow(plot_frame)
		plt.title("Click to select/deselect territories")

		# Connect the click event to the handler
		plt.gcf().canvas.mpl_connect('button_press_event', on_click)

		plt.show()
	else:
		selected_chroms = non_motion_markers

	selected_chroms = list(sorted(selected_chroms))
	chrom_mask = np.isin(non_motion_markers, selected_chroms)

	import matplotlib
	matplotlib.use('Agg')
	from matplotlib import pyplot as plt
	from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	from matplotlib.patches import Wedge

	if not individual:
		ret, img = cap.read()
		(width, height) = img.shape[:2]

		centers = chunk.centers.isel(frame=0).data.compute()[chrom_mask]
		motion_marker_centers = chunk.motion_marker_centers.isel(frame=0).data.compute()
		slice_areas = chunk.slice_areas.isel(frame=0).data.compute()[chrom_mask]
		nr_slices = slice_areas.shape[1]

		fig, ax = plt.subplots(figsize=(width/100, height/100), dpi=100)

		img_artist = ax.imshow(img, interpolation='none')
		ax.set_axis_off()
		fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

		canvas = FigureCanvas(fig)

		wedges = []
		for _ in range(len(centers) * nr_slices):
			w = Wedge((0, 0), 0, 0, 0, alpha=0.2, color='dodgerblue', linewidth=3)
			ax.add_patch(w)
			wedges.append(w)

		scat_red_artist = ax.scatter(centers[:, 1], centers[:, 0], c='r', s=25)
		scat_blue_artist = ax.scatter(motion_marker_centers[:, 1], motion_marker_centers[:, 0], c='b', s=25)	
						
		vw = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*'mp4v'), fps, (height, width))

		del cap
		try:
			cap = cv2.VideoCapture(chunk.segmentation.attrs['chunk_path'])
		except RuntimeError:
			absolute_path = Path(chunk.segmentation.attrs['chunk_path']).absolute()
			cap = cv2.VideoCapture(str(Path(dataset).parent / absolute_path.name))


		for _ in range(start):
			cap.read()

		print('pre-load data:')
		_centers = chunk.centers.compute()
		_motion_marker_centers = chunk.motion_marker_centers.compute()
		_orientation_angles = chunk.orientation_angles.compute()
		print('done')

		with click.progressbar(range(start, end), label='Generating slice video', show_percent=True, show_pos=True) as bar:
			for frame in bar:
				# print('running frame', frame)
				ret, img = cap.read()

				img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
				if not ret:
					click.secho(f'[ERROR] Video ended unexpectedly at frame {frame} of {end}.', fg='red', bold=True)
				clq = chunk.warped_cleanqueen.sel(frame=frame).data.compute()
				seg = chunk.segmentation.sel(frame=frame).data.compute()
				centers = _centers.sel(frame=frame).data[chrom_mask]
				motion_marker_centers = _motion_marker_centers.sel(frame=frame).data
				orientation_angles = _orientation_angles.sel(frame=frame).data[chrom_mask]
				slice_areas = chunk.slice_areas.sel(frame=frame).data.compute()[chrom_mask]
				    
				# clq = clear_border(clq, buffer_size=buffer)
				img = mark_boundaries(img, clq, color=(1, 1, 1), mode='thick')
				img = mark_boundaries(img, seg, color=(0, 1, 0), mode='outer')
				img = (img * 255).astype(np.uint8)

				img_artist.set_data(img)
				
				for i, (cen, motion_marker_angle, areas) in enumerate(zip(centers, orientation_angles, slice_areas)):
					for j, (angle, slice_area) in enumerate(zip(reversed(np.linspace(0, 360, nr_slices+1)[:-1]), areas)):
						wedges[i*nr_slices + j].set_center((cen[1], cen[0]))
						wedges[i*nr_slices + j].set_radius(slice_area)
						wedges[i*nr_slices + j].set_theta1(270 - motion_marker_angle + angle)
						wedges[i*nr_slices + j].set_theta2(270 - motion_marker_angle + angle + 360//nr_slices)
				
				scat_red_artist.set_offsets(centers[...,::-1])
				scat_blue_artist.set_offsets(motion_marker_centers[...,::-1])
				
				canvas.draw()

				rgb_buffer = np.array(canvas.renderer.buffer_rgba())[..., :3]
				# print(f'{rgb_buffer.shape=}')
				# plt.imsave(f'test_frame_{frame}.png', rgb_buffer)	
			
				vw.write(rgb_buffer[...,::-1])

		vw.release()
		click.secho(f'Slice video saved to {output}', fg='green', bold=True)

	else:
		outputs = [str(Path(dataset).with_suffix(f'.chunk_{chunk_int}_slices_chrom_{c}.mp4')) for c in selected_chroms]

		ret, img = cap.read()
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		if not ret:
			click.secho(f'[ERROR] Video ended unexpectedly at frame {i} of {end}.', fg='red', bold=True)
		plt.figure(figsize=(40, 40 * img.shape[0] / img.shape[1]))
		plt.imshow(img)
		plt.axis('off')
		plt.xlim(1, 201)
		plt.ylim(1, 201)
		plt.tight_layout()
		plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
		plt.margins(0, 0)
		plt.gca().xaxis.set_major_locator(plt.NullLocator())
		plt.gca().yaxis.set_major_locator(plt.NullLocator())
		plt.gcf().canvas.draw()

		video_frame = np.frombuffer(plt.gcf().canvas.tostring_rgb(), dtype=np.uint8)
		video_frame = video_frame.reshape((plt.gcf().canvas.get_width_height()[::-1] + (3,)))
		plt.close()
		
		vws = [cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*'mp4v'), fps, (video_frame.shape[1], video_frame.shape[0])) for output in outputs]

		cap.set(cv2.CAP_PROP_POS_FRAMES, start-1)
		with click.progressbar(range(start, end), label='Generating slice video', show_percent=True, show_pos=True) as bar:
			for i in bar:
				ret, img = cap.read()
				img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
				if not ret:
					click.secho(f'[ERROR] Video ended unexpectedly at frame {i} of {end}.', fg='red', bold=True)
				clq = chunk.warped_cleanqueen.isel(frame=i).data.compute()
				centers = chunk.centers.isel(frame=i).data.compute()[chrom_mask]
				motion_marker_centers = chunk.motion_marker_centers.isel(frame=i).data.compute()
				orientation_angles = chunk.orientation_angles.isel(frame=i).data.compute()[chrom_mask]
				slice_areas = chunk.slice_areas.isel(frame=i).data.compute()[chrom_mask]
				nr_slices = slice_areas.shape[1]
				
				# clq = clear_border(clq, buffer_size=buffer)
				img = mark_boundaries(img, clq, color=(1, 1, 1), mode='thick')
				img = (img * 255).astype(np.uint8)

				for c, cen, motion_marker_angle, areas, vw in zip(selected_chroms, centers, orientation_angles, slice_areas, vws):
					# Make figure twice the size of the image to avoid clipping of the wedges
					plt.figure(figsize=(40, 40 * img.shape[0] / img.shape[1]))
					plt.imshow(img)

					wedges = [
						Wedge(
							(cen[1], cen[0]), slice_area, 270 - motion_marker_angle + angle, 270 - motion_marker_angle + angle + 360//nr_slices, alpha=0.3, color='dodgerblue' if i else 'orange', linewidth=3,
							) for i, (angle, slice_area) in enumerate(zip(reversed(np.linspace(0, 360, nr_slices+1)[:-1]), areas))
					]
					plt.gca().add_collection(collections.PatchCollection(wedges, match_original=True))
					plt.scatter(cen[1], cen[0], c='r', s=400)

					# Get figure as numpy array:
					plt.axis('off')
					plt.xlim(int(cen[1])-100, int(cen[1])+100)
					plt.ylim(int(cen[0])-100, int(cen[0])+100)
					plt.tight_layout()
					plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
					plt.margins(0, 0)
					plt.gca().xaxis.set_major_locator(plt.NullLocator())
					plt.gca().yaxis.set_major_locator(plt.NullLocator())
					plt.gcf().canvas.draw()

					video_frame = np.frombuffer(plt.gcf().canvas.tostring_rgb(), dtype=np.uint8)
					video_frame = video_frame.reshape((plt.gcf().canvas.get_width_height()[::-1] + (3,)))

					plt.close()
					vw.write(video_frame[...,::-1])

		for vw in vws:
			vw.release()


@error_handler('Generating slice frame', cluster=False)
def generate_slice_frame(dataset: str, chunk: int, frame: int=0, output: str=None, buffer: int=0,
						 interactive: bool=False, individual: bool=False) -> None:
	from matplotlib import collections
	from matplotlib import pyplot as plt
	
	chunk_int = int(chunk)
	assert Path(dataset).is_dir(), f'{dataset} is not a valid dataset. Show-slicing does not take videos as input, but datasets geneated through e.g. slicing.'
	if output is not None:
		assert Path(output).suffix in ['.png', '.jpg'], 'Output must be png or jpg file.'
		assert Path(output).parent.exists(), f'Output directory {Path(output).parent} does not exist.'
		assert not Path(output).exists(), f'Output file {output} already exists.'
	else:
		output = str(Path(dataset).with_suffix(f'.chunk_{chunk}_frame_{frame}.png'))
	
	chunk = xr.open_zarr(dataset, group=f'chunk_{chunk}')
	try:
		cap = cv2.VideoCapture(chunk.segmentation.attrs['chunk_path'])
	except RuntimeError:
		absolute_path = Path(chunk.segmentation.attrs['chunk_path']).absolute()
		cap = cv2.VideoCapture(str(Path(dataset).parent / absolute_path.name))

	non_motion_markers = chunk.non_motion_markers.data.compute()
	cleanqueen = chunk.cleanqueen.data.compute()

	if interactive:
		ret, frame_0 = cap.read()
		frame_0 = cv2.cvtColor(frame_0, cv2.COLOR_BGR2RGB)
		plot_frame = mark_boundaries(frame_0, cleanqueen, color=(0, 0, 1))
		selected_chroms = []

		def on_click(event):
			# Get the indices of the clicked point
			x, y = int(event.xdata), int(event.ydata)
			
			# Get the label of the clicked territory
			label = cleanqueen[y, x]

			if label not in non_motion_markers:
				click.secho(f"Clicked on motion marker territory {label}.", fg='yellow')
				return
			
			if label in selected_chroms:
				# If already selected, remove from the list and unhighlight
				selected_chroms.remove(label)
				click.echo(f"Removed: {label}")
			else:
				# If not selected, add to the list and highlight
				selected_chroms.append(label)
				click.echo(f"Added: {label}")
			
			# Redraw the plot with updated highlights
			update_plot()

		def update_plot():
			plt.clf()
			plt.imshow(plot_frame, cmap='viridis')
			
			# Highlight selected territories
			for label in selected_chroms:
				plt.contour(cleanqueen == label, colors='magenta', linewidths=2)
			
			plt.draw()

		# Plot the initial array
		plt.imshow(plot_frame)
		plt.title("Click to select/deselect territories")

		# Connect the click event to the handler
		plt.gcf().canvas.mpl_connect('button_press_event', on_click)

		plt.show()
	else:
		selected_chroms = non_motion_markers

	selected_chroms = list(sorted(selected_chroms))
	chrom_mask = np.isin(non_motion_markers, selected_chroms)
	ylim, xlim = rectify_mask(np.isin(cleanqueen, selected_chroms), padding=100, return_limits=True)

	import matplotlib
	matplotlib.use('Agg')
	from matplotlib import collections
	from matplotlib import pyplot as plt
	from matplotlib.patches import Wedge

	cap.set(cv2.CAP_PROP_POS_FRAMES, frame-1)
		
	ret, img = cap.read()
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	if not ret:
		click.secho('[ERROR] Video ended unexpectedly.', fg='red', bold=True)
	clq = chunk.warped_cleanqueen.isel(frame=frame).data.compute()
	centers = chunk.centers.isel(frame=frame).data.compute()[chrom_mask]
	motion_marker_centers = chunk.motion_marker_centers.isel(frame=frame).data.compute()
	orientation_angles = chunk.orientation_angles.isel(frame=frame).data.compute()[chrom_mask]
	slice_areas = chunk.slice_areas.isel(frame=frame).data.compute()[chrom_mask]
	nr_slices = slice_areas.shape[1]
	
	# clq = clear_border(clq, buffer_size=buffer)
	img = mark_boundaries(img, clq, color=(1, 1, 1), mode='thick')
	img = (img * 255).astype(np.uint8)

	if not individual:				
		plt.figure(figsize=(40, 40 * img.shape[0] / img.shape[1]))
		plt.imshow(img)

		wedges = [
			Wedge(
				(cen[1], cen[0]), slice_area, 270 - motion_marker_angle + angle, 270 - motion_marker_angle + angle + 360//nr_slices, alpha=0.3, color='dodgerblue', linewidth=3,
				) for cen, motion_marker_angle, areas in zip(centers, orientation_angles, slice_areas) for angle, slice_area in zip(reversed(np.linspace(0, 360, nr_slices+1)[:-1]), areas)
		]
		plt.gca().add_collection(collections.PatchCollection(wedges, match_original=True))
		plt.scatter(centers[:, 1], centers[:, 0], c='r', s=25)
		plt.scatter(motion_marker_centers[:, 1], motion_marker_centers[:, 0], c='b', s=25)
		plt.axis('off')
		plt.xlim(*xlim)
		plt.ylim(*ylim)
		plt.tight_layout()
		plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
		plt.margins(0, 0)
		plt.gca().invert_yaxis()
		plt.savefig(output, bbox_inches='tight', pad_inches=0)
		plt.close()

		click.secho(f'Slice plot frame saved to {output}', fg='green', bold=True)
	else:
		outputs = [str(Path(dataset).with_suffix(f'.chunk_{chunk_int}_frame_{frame}_slices_chrom_{c}.png')) for c in selected_chroms]

		for c, cen, motion_marker_angle, areas, output in zip(selected_chroms, centers, orientation_angles, slice_areas, outputs):
			# Make figure twice the size of the image to avoid clipping of the wedges
			plt.figure(figsize=(40, 40 * img.shape[0] / img.shape[1]))
			plt.imshow(img)

			wedges = [
				Wedge(
					(cen[1], cen[0]), slice_area, 270 - motion_marker_angle + angle, 270 - motion_marker_angle + angle + 360//nr_slices, alpha=0.3, color='dodgerblue' if i else 'orange', linewidth=3,
					) for i, (angle, slice_area) in enumerate(zip(reversed(np.linspace(0, 360, nr_slices+1)[:-1]), areas))
			]
			plt.gca().add_collection(collections.PatchCollection(wedges, match_original=True))
			plt.scatter(cen[1], cen[0], c='r', s=400)

			plt.axis('off')
			plt.xlim(int(cen[1])-100, int(cen[1])+100)
			plt.ylim(int(cen[0])-100, int(cen[0])+100)
			plt.tight_layout()
			plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
			plt.margins(0, 0)
			plt.savefig(output, bbox_inches='tight', pad_inches=0)
			plt.close()
			

@error_handler('Plot slicing', cluster=False)
def plot_slicing(K, motion_marker_centers, image, centers, slice_areas, orientation_angles, nr_slices, cleanqueen):
	from matplotlib import pyplot as plt
	import matplotlib.collections as collections
	from matplotlib.patches import Wedge
	
	plt.figure(figsize=(10, 10))
	plt.imshow(mark_boundaries(1 - image / image.max(), cleanqueen, color=(0, 1, 0)))

	# plt.scatter(centers[chroms, 1], centers[chroms, 0], c='r', s=5, alpha=0.5)
	# This is tricky: angles in the previous steps are computed as angles counterclockwise from the y-axis. But in matplotlib (Wedges), they have to be given
	# as angles clockwise from the x-axis. So we have to subtract the angles from 360 to correct for counterclockwise/clockwise difference, and then subtract 90
	# for the x-axis/y-axis difference. Hence angle_matplotlib = 360 - angle_computed - 90 = 270 - angle_computed. Furthermore, we have t iterate over the areas 
	# in reversed order, because matplotlib expects the angles in clockwise order.
	wedges = [
		Wedge(
			(cen[1], cen[0]), slice_area, 270 - motion_marker_angle + angle, 270 - motion_marker_angle + angle + 360//nr_slices, alpha=0.2, color='magenta'
			) for cen, motion_marker_angle, areas in zip(centers, orientation_angles, slice_areas) for angle, slice_area in zip(reversed(np.linspace(0, 360, nr_slices+1)[:-1]), areas)
	]
	plt.gca().add_collection(collections.PatchCollection(wedges, match_original=True))
	plt.scatter(centers[:, 1], centers[:, 0], c='r', s=5)
	plt.scatter(motion_marker_centers[:, 1], motion_marker_centers[:, 0], c='b', s=5)
	plt.show()
	return K
