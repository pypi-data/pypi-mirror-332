import xarray as xr
import click
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from skimage.segmentation import mark_boundaries
from matplotlib.widgets import Button

def interactive_plot(cleanqueen, queenframe):
	selected_values = set(np.unique(cleanqueen[cleanqueen > 0]))  # Start with all selected
	fig, ax = plt.subplots()
	plt.subplots_adjust(bottom=0.2)  # Make space for buttons

	queenframe = mark_boundaries(queenframe, cleanqueen, mode='thick')
	img_display = ax.imshow(queenframe)

	blue_overlay = np.zeros((*cleanqueen.shape, 4))  # RGBA
	blue_overlay[:, :, 2] = 1  # Blue channel full
	blue_overlay[:, :, 3] = 0.3  # Transparency

	# Initial mask
	mask = cleanqueen > 0
	overlay_display = ax.imshow(blue_overlay, extent=ax.get_xlim() + ax.get_ylim(), zorder=2)

	def update_overlay():
		nonlocal overlay_display
		new_mask = np.isin(cleanqueen, list(selected_values), invert=False) & mask
		new_overlay = blue_overlay.copy()
		new_overlay[~new_mask] = [0, 0, 0, 0]  # Remove transparency where deselected
		overlay_display.set_data(new_overlay)
		fig.canvas.draw_idle()

	def on_click(event):
		if event.xdata is None or event.ydata is None:
			return
		x, y = int(event.xdata), int(event.ydata)
		value = cleanqueen[y, x]
		if value > 0:
			if value in selected_values:
				selected_values.remove(value)
			else:
				selected_values.add(value)
			update_overlay()
	
	def select_all(event):
		nonlocal selected_values
		selected_values = set(np.unique(cleanqueen[cleanqueen > 0]))
		update_overlay()
	
	def deselect_all(event):
		nonlocal selected_values
		selected_values.clear()
		update_overlay()
	
	fig.canvas.mpl_connect('button_press_event', on_click)
	
	ax_select_all = plt.axes([0.7, 0.05, 0.1, 0.075])
	ax_deselect_all = plt.axes([0.81, 0.05, 0.1, 0.075])
	
	btn_select_all = Button(ax_select_all, 'Select All')
	btn_deselect_all = Button(ax_deselect_all, 'Deselect All')
	
	btn_select_all.on_clicked(select_all)
	btn_deselect_all.on_clicked(deselect_all)
	
	update_overlay()
	plt.show()

	return np.array([s for s in selected_values])


def select_chroms(ds: xr.Dataset):
	stitching = xr.open_zarr(ds, f'stitching')
	cleanqueen = stitching.cleanqueen.data.compute()
	try:
		ref_chunk = stitching.stitching_matrix.attrs['ref_chunk']
	except:
		ref_chunk = 0
	queenaverage = xr.open_zarr(ds, f'chunk_{ref_chunk}').chunkaverage.data.compute()

	values = interactive_plot(cleanqueen, queenaverage)
	print(values)

	cleanqueen[np.isin(cleanqueen, values, invert=True)] = 0

	cleanqueen = xr.DataArray(cleanqueen, dims=['x', 'y'], name='cleanqueen')
	cleanqueen.to_zarr(ds, group='stitching', mode='a')
