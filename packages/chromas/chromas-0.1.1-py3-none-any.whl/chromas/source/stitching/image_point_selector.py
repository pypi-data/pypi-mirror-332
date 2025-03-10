from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import numpy as np
import itertools
import cv2
from scipy.interpolate import Rbf

from tkinter import Tk, messagebox
import click
import matplotlib as mpl
from matplotlib.colors import to_rgb
from sys import platform
if platform == 'darwin':
    mpl.use('tkagg')
mpl.rcParams['axes.spines.top']    = False
mpl.rcParams['axes.spines.right']  = False
mpl.rcParams['axes.spines.left']   = False
mpl.rcParams['axes.spines.bottom'] = False


BROWN = "#f76700"
BROWN_RGB = (np.array(to_rgb(BROWN)) * 255).astype(int)
GREEN = '#5ff700'
GREEN_RGB = (np.array(to_rgb(GREEN)) * 255).astype(int)


class ImagePointSelector:
	def __init__(self, image1, image2, grid_spacing=50, hints = None):
		"""
		Initialize the ImagePointSelector with two images.

		Parameters:
		- image1: Source image (numpy array).
		- image2: Destination image (numpy array).
		- grid_spacing: Spacing between grid points for transformation.
		"""
		self.image1 = image1
		self.image2 = image2
		self.grid_spacing = grid_spacing  # Spacing between grid points

		self.point_pairs = []
		self.click_count = 0
		self.last_click_axes = None
		self.colors = itertools.cycle(['red', 'blue', 'green', 'orange', 'purple',
									   'yellow', 'cyan', 'magenta', 'lime', 'pink',
									   'brown', 'black'])
		self.color = None
		self.transformation_method = 'Affine'

		# Initialize history stacks for Undo/Redo
		self.history = []
		self.redo_stack = []

		# Initialize figure with three subplots
		self.fig, (self.ax1, self.ax2, self.ax3) = plt.subplots(1, 3, figsize=(24, 12))
		self.ax1.imshow(self.image1, cmap='gray')
		self.ax2.imshow(self.image2, cmap='gray')
		self.ax3.imshow(self.image2, cmap='gray')  # Initialize with image2 as base
		self.ax1.set_title('Image A')
		self.ax2.set_title('Image B')
		self.ax3.set_title('Overlay: Image B + Warped Image A')

		plt.subplots_adjust(left=0.05, bottom=0.25, right=0.95, top=0.90, wspace=0.3)


		# Initialize slider parameters
		self.transparency = 0.5  # Default transparency
		self.tps_smoothness = 1.0  # Default TPS smoothness
		self.mls_weight_radius = 100.0  # Default MLS weight radius
		self.mls_poly_degree = 1  # Default MLS polynomial degree

		# Create sliders for transparency and smoothness
		slider_ax_transparency = self.fig.add_axes([0.3, 0.25, 0.6, 0.03])
		self.slider_transparency = widgets.Slider(
			ax=slider_ax_transparency,
			label='Overlay Transparency',
			valmin=0.0,
			valmax=1.0,
			valinit=self.transparency,
			valstep=0.01,
			initcolor='lightgrey',
			track_color='lightgrey',
			handle_style={
				'facecolor': BROWN,
				'edgecolor': 'white',
				'size': 12
			},
			color=BROWN,
		)

		slider_ax_tps_smoothness = self.fig.add_axes([0.3, 0.15, 0.6, 0.03])
		self.slider_tps_smoothness = widgets.Slider(
			ax=slider_ax_tps_smoothness,
			label='TPS Smoothness',
			valmin=0.0,
			valmax=100.0,
			valinit=self.tps_smoothness,
			valstep=0.1,
			initcolor='lightgrey',
			track_color='lightgrey',
			handle_style={
				'facecolor': BROWN,
				'edgecolor': 'white',
				'size': 12
			},
			color=BROWN,
		)

		# Create sliders for MLS parameters
		slider_ax_mls_weight = self.fig.add_axes([0.3, 0.10, 0.6, 0.03])
		self.slider_mls_weight = widgets.Slider(
			ax=slider_ax_mls_weight,
			label='MLS Weight Radius',
			valmin=10.0,
			valmax=300.0,
			valinit=self.mls_weight_radius,
			valstep=5.0,
			initcolor='lightgrey',
			track_color='lightgrey',
			handle_style={
				'facecolor': BROWN,
				'edgecolor': 'white',
				'size': 12
			},
			color=BROWN,
		)

		slider_ax_mls_poly = self.fig.add_axes([0.3, 0.05, 0.6, 0.03])
		self.slider_mls_poly = widgets.Slider(
			ax=slider_ax_mls_poly,
			label='MLS Polynomial Degree',
			valmin=1,
			valmax=10,
			valinit=self.mls_poly_degree,
			valstep=1,
			initcolor='lightgrey',
			track_color='lightgrey',
			handle_style={
				'facecolor': BROWN,
				'edgecolor': 'white',
				'size': 12
			},
			color=BROWN,
		)

		# Create slider for Grid Spacing
		slider_ax_grid = self.fig.add_axes([0.3, 0.20, 0.6, 0.03])  # Adjust y-position as needed
		self.slider_grid_spacing = widgets.Slider(
			ax=slider_ax_grid,
			label='Grid Spacing',
			valmin=20,        # Minimum grid spacing
			valmax=100,       # Maximum grid spacing
			valinit=self.grid_spacing,  # Initial value based on existing grid_spacing
			valstep=5.0,
			initcolor='lightgrey',
			track_color='lightgrey',
			handle_style={
				'facecolor': BROWN,
				'edgecolor': 'white',
				'size': 12
			},
			color=BROWN,
		)

		# Create checkbox for selecting transformation method
		checkbox_ax = self.fig.add_axes([0.05, 0.15, 0.1, 0.10])  # Adjust y-position as needed
		self.checkbox = widgets.CheckButtons(
			ax=checkbox_ax,
			labels=['Affine', 'MLS', 'TPS'],
			actives=[True, False, False],
			frame_props=dict(edgecolor='lightgrey', lw=5),
			check_props=dict(facecolor=BROWN, edgecolor='white', lw=3),
		)

		# Connect sliders and checkbox to update function
		self.slider_transparency.on_changed(self.update_overlay)
		self.slider_tps_smoothness.on_changed(self.update_overlay)
		self.slider_mls_weight.on_changed(self.update_overlay)
		self.slider_mls_poly.on_changed(self.update_overlay)
		self.checkbox.on_clicked(self.toggle_transformation_method)
		self.slider_grid_spacing.on_changed(self.update_overlay)

		for slider in [self.slider_tps_smoothness, self.slider_mls_weight, self.slider_mls_poly, self.slider_grid_spacing]:
			slider.ax.set_visible(False)


		# Create additional buttons
		# Help Button
		help_ax = self.fig.add_axes([0.05, 0.9, 0.08, 0.05])
		self.help_button = widgets.Button(help_ax, 'Help', color=BROWN, hovercolor='lightgrey',)
		self.help_button.edgecolor = 'none'
		self.help_button.label.set_color('white')
		self.help_button.label.set_fontsize(12)
	
		self.help_button.on_clicked(self.show_help)
		self.help_button.label.set_color('white')
		self.help_button.label.set_fontsize(12)

		# Undo Button
		undo_ax = self.fig.add_axes([0.15, 0.9, 0.08, 0.05])
		self.undo_button = widgets.Button(undo_ax, 'Undo', color=BROWN, hovercolor='lightgrey')
		self.undo_button.on_clicked(self.undo_action)
		self.undo_button.label.set_color('white')
		self.undo_button.label.set_fontsize(12)

		# Redo Button
		redo_ax = self.fig.add_axes([0.25, 0.9, 0.08, 0.05])
		self.redo_button = widgets.Button(redo_ax, 'Redo', color=BROWN, hovercolor='lightgrey')
		self.redo_button.on_clicked(self.redo_action)
		self.redo_button.label.set_color('white')
		self.redo_button.label.set_fontsize(12)

		# Reset Button
		reset_ax = self.fig.add_axes([0.35, 0.9, 0.08, 0.05])
		self.reset_button = widgets.Button(reset_ax, 'Reset', color=BROWN, hovercolor='lightgrey')
		self.reset_button.on_clicked(self.reset_all)
		self.reset_button.label.set_color('white')
		self.reset_button.label.set_fontsize(12)

		# Save Warped Image Button
		save_image_ax = self.fig.add_axes([0.45, 0.9, 0.08, 0.05])
		self.save_image_button = widgets.Button(save_image_ax, 'Save Image', color=BROWN, hovercolor='lightgrey')
		self.save_image_button.on_clicked(self.save_warped_image)
		self.save_image_button.label.set_color('white')
		self.save_image_button.label.set_fontsize(12)

		# Auto Match Button
		auto_match_ax = self.fig.add_axes([0.55, 0.9, 0.08, 0.05])
		self.auto_match_button = widgets.Button(auto_match_ax, 'Auto Match', color=BROWN, hovercolor='lightgrey')
		self.auto_match_button.on_clicked(self.auto_match_features)
		self.auto_match_button.label.set_color('white')
		self.auto_match_button.label.set_fontsize(12)

		# # Export Transformed Points Button
		# export_points_ax = self.fig.add_axes([0.85, 0.47, 0.10, 0.05])
		# self.export_points_button = widgets.Button(export_points_ax, 'Export Points')
		# self.export_points_button.on_clicked(self.export_transformed_points)
		# self.export_points_button.label.set_color('white')
		# self.export_points_button.label.set_fontsize(12)


		# Connect keyboard shortcuts
		self.fig.canvas.mpl_connect('key_press_event', self.on_key_press)

		# Connect mouse click and hover events
		self.fig.canvas.mpl_connect('button_press_event', self.on_click)
		# self.fig.canvas.mpl_connect('motion_notify_event', self.on_hover)

		# Initialize message box for user feedback
		self.message_box = self.fig.text(0.05, 0.02, "", fontsize=10,
										 bbox=dict(facecolor='lightyellow', alpha=0.5, edgecolor='black'))

		self.hints = hints
		if hints is not None:
			self.set_hints()

		# Connect mouse click event handler
		self.fig.canvas.mpl_connect('button_press_event', self.on_click)
		plt.gcf().canvas.manager.set_window_title('CHROMAS - Image Warping Tool')
		plt.show()


	def set_hints(self):
		""" Plot the pair of points as hints on the images """
		click.secho("[INFO] Plotting hints on the images...", fg='green')
		for pair, color in zip(self.hints, self.colors):
			self.ax1.plot(pair[0][0], pair[0][1], '*', markeredgecolor=color, markerfacecolor='white', markersize=12, markeredgewidth=2)
			self.ax2.plot(pair[1][0], pair[1][1], '*', markeredgecolor=color, markerfacecolor='white', markersize=12, markeredgewidth=2)
		


	# -------------------- Undo/Redo Functionality --------------------

	def undo_action(self, event):
		"""
		Undo the last action (add or remove point pair).
		"""
		if not self.history:
			self.display_message("Nothing to undo.", color='red')
			return
		action, point = self.history.pop()
		if action == 'add':
			if self.point_pairs:
				removed_point = self.point_pairs.pop()
				self.redo_stack.append(('add', removed_point))
		elif action == 'remove':
			self.point_pairs.append(point)
			self.redo_stack.append(('remove', point))
		self.redraw_points()
		self.update_overlay()
		self.display_message("Undo successful.", color='green')


	def redo_action(self, event):
		"""
		Redo the last undone action.
		"""
		if not self.redo_stack:
			self.display_message("Nothing to redo.", color='red')
			return
		action, point = self.redo_stack.pop()
		if action == 'add':
			self.point_pairs.append(point)
			self.history.append(('add', point))
		elif action == 'remove':
			if self.point_pairs:
				removed_point = self.point_pairs.pop()
				self.history.append(('remove', removed_point))
		self.redraw_points()
		self.update_overlay()
		self.display_message("Redo successful.", color='green')

	# -------------------- Reset Button --------------------

	def reset_all(self, event):
		"""
		Reset all point pairs and sliders to default values.
		"""
		self.point_pairs = []
		self.history = []
		self.redo_stack = []
		self.click_count = 0
		self.last_click_axes = None

		# Reset sliders to default values
		self.slider_transparency.reset()
		self.slider_grid_spacing.reset()
		self.slider_tps_smoothness.reset()
		self.slider_mls_weight.reset()
		self.slider_mls_poly.reset()

		# Reset transformation method to TPS
		self.transformation_method = 'TPS'
		self.checkbox.set_active(0)  # Uncheck 'Use MLS'
		self.toggle_mls_sliders(enable=False)
		self.slider_tps_smoothness.ax.set_visible(True)

		# Redraw overlay
		self.redraw_points()
		self.update_overlay()
		self.display_message("Reset successful.", color='green')

	# -------------------- Keyboard Shortcuts for Common Actions --------------------

	def on_key_press(self, event):
		"""
		Handle keyboard shortcuts for common actions.
		"""
		if event.key == 'ctrl+z':
			self.undo_action(None)
		elif event.key == 'ctrl+y':
			self.redo_action(None)
		elif event.key == 'r':
			self.reset_all(None)
		elif event.key == 's':
			self.save_warped_image() 
		# elif event.key == 'e':
		#     timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
		#     filepath = f'point_pairs_{timestamp}.json'
		#     self.export_transformed_points(f'transformed_points_{filepath}.csv')  # Or prompt for file path

	
	 # -------------------- Display Message --------------------

	def display_message(self, message, color='black'):
		"""
		Display a message in the GUI.

		Parameters:
		- message: The message string to display.
		- color: Color of the text.
		"""
		self.message_box.set_text(message)
		self.message_box.set_color(color)
		self.fig.canvas.draw()

	# -------------------- Automated Feature Detection and Matching --------------------

	def auto_match_features(self, event):
		"""
		Automatically detect and match features between image1 and image2.
		Includes a confirmation step and allows users to remove undesired matches.
		"""
		# Initialize ORB detector
		orb = cv2.ORB_create()

		# Find keypoints and descriptors with ORB
		kp1, des1 = orb.detectAndCompute(self.image1, None)
		kp2, des2 = orb.detectAndCompute(self.image2, None)

		# Initialize matcher
		bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

		# Match descriptors
		if des1 is None or des2 is None:
			self.display_message("No descriptors found in one or both images.", color='red')
			return

		matches = bf.match(des1, des2)

		# # Sort matches by distance
		# matches = sorted(matches, key=lambda x: x.distance)

		# Select top N matches
		N = 20  # Adjust as needed
		matches = matches[:N]

		if not matches:
			self.display_message("No matches found.", color='red')
			return

		# Display matched points for confirmation
		confirmation = messagebox.askyesno("Confirm Matches", f"Found {len(matches)} matches. Do you want to add them?")

		if not confirmation:
			self.display_message("Auto match cancelled by user.", color='yellow')
			return

		# Add matched points to point_pairs
		for match in matches:
			src_pt = kp1[match.queryIdx].pt
			dst_pt = kp2[match.trainIdx].pt
			# Check if this pair already exists
			if any(np.allclose(src_pt, pair[0]) and np.allclose(dst_pt, pair[1]) for pair in self.point_pairs):
				continue  # Skip duplicates

			self.point_pairs.append((src_pt, dst_pt, next(self.colors)))
			self.history.append(('add', self.point_pairs[-1]))

		self.redo_stack.clear()
		self.redraw_points()
		self.update_overlay()
		self.display_message(f"Automatically added {len(matches)} point pairs.", color='green')


		# -------------------- Help Menu --------------------

	def show_help(self, event):
		"""
		Display a help dialog with comprehensive documentation.
		"""
		help_text = (
			"Image Warping Help:\n\n"
			"1. Add Points:\n"
			"   - Left-click on a point in Image 1 (or 2).\n"
			"   - Left-click on the corresponding point in Image 2 (or 1, resp.).\n"
			"   - Repeat to add multiple point pairs (minimum 3).\n\n"
			"2. Remove Points:\n"
			"   - Right-click near a point in either Image 1 or Image 2 to remove it as well as its paired point, if exists.\n\n"
			"3. Transformation Methods:\n"
			"   - Select between TPS (Thin-Plate-Spline) or MLS (Moving-Least-Squares).\n"
			"4. Sliders:\n"
			"   - Overlay Transparency: Adjust blending between images (visualization only).\n"
			"   - Grid Spacing: Adjust the interpolation grid size.\n"
			"   - TPS Smoothness: Control TPS transformation smoothness.\n"
			"   - MLS Weight Radius: Define MLS influence radius.\n"
			"   - MLS Polynomial Degree: Set MLS polynomial degree.\n\n"
			"5. Buttons:\n"
			"   - Undo: Revert the last action.\n"
			"   - Redo: Reapply the last undone action.\n"
			"   - Reset: Clear all points and reset sliders.\n"
			"   - Auto Match: Automatically detect and match features.\n"
			"   - Help: Show this help message.\n\n"
			"6. Keyboard Shortcuts:\n"
			"   - Ctrl+Z: Undo\n"
			"   - Ctrl+Y: Redo\n"
			"   - R: Reset\n"
			"   - S: Save warped image\n"
			"7. Automated Feature Matching:\n"
			"   - Click 'Auto Match' to automatically detect and match features between images.\n"
			"   - Remove undesired matches manually by right-clicking near them.\n\n"
			"For further assistance, please refer to the documentation."
		)

		root = Tk()
		root.withdraw()
		messagebox.showinfo("Help - Image Warping", help_text)
		root.destroy()


	def toggle_transformation_method(self, label):
		"""
		Toggle between TPS and MLS transformation methods based on checkbox status.
		"""
		if label is None:
			return
		if label == self.transformation_method:
			return
		self.transformation_method = label
		self.checkbox.clear()

		match label:
			case 'Affine':
				# Checkboxes: [Affine, MLS, TPS]
				self.toggle_mls_sliders(enable=False)
				self.toggle_tps_sliders(enable=False)
				self.slider_grid_spacing.ax.set_visible(True)
				self.checkbox.set_active(0)

			case 'MLS':
				self.toggle_mls_sliders(enable=True)
				self.toggle_tps_sliders(enable=False)
				self.slider_grid_spacing.ax.set_visible(True)
				self.checkbox.set_active(1)

			case 'TPS':
				self.toggle_mls_sliders(enable=False)
				self.toggle_tps_sliders(enable=True)
				self.slider_grid_spacing.ax.set_visible(True)
				self.checkbox.set_active(2)
		self.update_overlay()
		

	def toggle_mls_sliders(self, enable=True):
		"""
		Show or hide MLS-specific sliders based on the selected transformation method.
		"""
		if enable:
			self.slider_mls_weight.ax.set_visible(True)
			self.slider_mls_poly.ax.set_visible(True)
		else:
			self.slider_mls_weight.ax.set_visible(False)
			self.slider_mls_poly.ax.set_visible(False)
		plt.draw()

	
	def toggle_tps_sliders(self, enable=True):
		"""
		Show or hide TPS-specific sliders based on the selected transformation method.
		"""
		if enable:
			self.slider_tps_smoothness.ax.set_visible(True)
		else:
			self.slider_tps_smoothness.ax.set_visible(False)
		plt.draw()


	def on_click(self, event):
		"""
		Handle mouse click events for adding or removing point pairs.
		"""
		if event.inaxes not in [self.ax1, self.ax2]:
			return
		if event.button == 1 and event.dblclick:
			return
		# If in zoom or pan activate, return
		if plt.get_current_fig_manager().toolbar.mode != '':
			return

		# Left click: Add point
		if event.button == 1:
			if self.click_count == 0:
				# First click on either image
				if event.inaxes == self.ax1 or event.inaxes == self.ax2:
					self.last_click_axes = event.inaxes
					x, y = event.xdata, event.ydata
					self.color = next(self.colors)
					event.inaxes.plot(x, y, 'o', markeredgecolor='white',
									 markerfacecolor=self.color, markersize=8)
					self.click_count += 1
					self.fig.canvas.draw()

			elif self.click_count == 1:
				# Second click must be on the other image
				if event.inaxes != self.last_click_axes:
					x, y = event.xdata, event.ydata
					event.inaxes.plot(x, y, 'o', markeredgecolor='white',
									 markerfacecolor=self.color, markersize=8)
					self.fig.canvas.draw()

					# Store point pair in the data structure
					if self.last_click_axes == self.ax1:
						self.point_pairs.append((
							(self.last_click_axes.lines[-1].get_xdata()[0],
							 self.last_click_axes.lines[-1].get_ydata()[0]),
							(x, y),
							self.color
						))
					else:
						self.point_pairs.append((
							(x, y),
							(self.last_click_axes.lines[-1].get_xdata()[0],
							 self.last_click_axes.lines[-1].get_ydata()[0]),
							self.color
						))

					# Reset state
					self.click_count = 0
					self.last_click_axes = None
					self.history.append(('add', self.point_pairs[-1]))
					self.redo_stack.clear()

					# Update the overlay
					self.update_overlay()

		# Right click: Remove point
		elif event.button == 3:
			if len(self.point_pairs) == 0 and self.click_count == 0:
				return
			if self.click_count == 1:
				self.last_click_axes = None
				self.click_count = 0
			else:
				removed_point = None
				x, y = event.xdata, event.ydata
				# Search for closest point regardless of which axes were last clicked
				for index, ((x1, y1), (x2, y2), _) in enumerate(self.point_pairs):
					if event.inaxes == self.ax1 and np.hypot(x - x1, y - y1) < 50:
						removed_point = self.point_pairs.pop(index)
						self.history.append(('remove', removed_point))
						break
					elif event.inaxes == self.ax2 and np.hypot(x - x2, y - y2) < 50:
						removed_point = self.point_pairs.pop(index)
						self.history.append(('remove', removed_point))
						break
				if removed_point:
					self.redo_stack.clear()
					self.update_overlay()

			# Clear and redraw the axes
			self.ax1.clear()
			self.ax2.clear()
			self.ax3.clear()
			self.ax1.imshow(self.image1, cmap='gray')
			self.ax2.imshow(self.image2, cmap='gray')
			self.ax3.imshow(self.image2, cmap='gray')  # Reset overlay to image2
			self.ax1.set_title('Image 1')
			self.ax2.set_title('Image 2')
			self.ax3.set_title('Overlay: Image 2 + Warped Image 1')

			if self.hints is not None:
				self.set_hints()

			# Re-draw all points from updated data structure
			if self.point_pairs:
				for ((x1, y1), (x2, y2), color) in self.point_pairs:
					self.ax1.plot(x1, y1, 'o', markeredgecolor='white',
								 markerfacecolor=color, markersize=8)
					self.ax2.plot(x2, y2, 'o', markeredgecolor='white',
								 markerfacecolor=color, markersize=8)

			self.fig.canvas.draw()

			# Update the overlay
			self.update_overlay()

	def get_point_pairs(self):
		"""
		Retrieve the list of point pairs.

		Returns:
		- List of tuples: [((x1, y1), (x2, y2)), ...]
		"""
		return [(pair[0], pair[1]) for pair in self.point_pairs]
	



	def estimate_transformation_tps(self, grid_points, smoothness):
		"""
		Estimate TPS transformation for the grid points.

		Parameters:
		- grid_points: Nx2 array of grid points.
		- smoothness: Smoothness parameter for TPS.

		Returns:
		- Transformed grid points as two separate arrays: warped_x, warped_y
		"""
		if len(self.point_pairs) < 3:
			click.secho("[WARNING] Not enough points to estimate TPS transformation. At least 3 pairs are needed.", fg='yellow')
			return None, None

		# Separate point pairs into source and destination arrays
		src_points = np.array([pair[0] for pair in self.point_pairs])  # Image1
		dst_points = np.array([pair[1] for pair in self.point_pairs])  # Image2

		try:
			# Perform Thin Plate Spline (TPS) Transformation using RBF
			rbf_x = Rbf(src_points[:,0], src_points[:,1], dst_points[:,0],
						function='thin_plate', smooth=smoothness)
			rbf_y = Rbf(src_points[:,0], src_points[:,1], dst_points[:,1],
						function='thin_plate', smooth=smoothness)

			# Apply transformation to grid points
			warped_x = rbf_x(grid_points[:,0], grid_points[:,1])
			warped_y = rbf_y(grid_points[:,0], grid_points[:,1])

			return warped_x, warped_y
		except Exception as e:
			click.secho(f"[ERROR] Error estimating TPS transformation: {e}", fg='red')
			return None, None
		
	def estimate_transformations(self):
		if len(self.point_pairs) < 3:
			click.secho("[WARNING] Not enough points to estimate transformations. At least 3 pairs are needed.", fg='yellow', italic=True)
			return None, None

		# Separate point pairs into source and destination arrays
		src_points = np.array([pair[0] for pair in self.point_pairs])
		dst_points = np.array([pair[1] for pair in self.point_pairs])

		# Estimate the affine transformation matrix from image1 to image2
		transformation_matrix_1to2, _ = cv2.estimateAffine2D(src_points, dst_points)

		# Estimate the affine transformation matrix from image2 to image1
		transformation_matrix_2to1, _ = cv2.estimateAffine2D(dst_points, src_points)

		return transformation_matrix_1to2, transformation_matrix_2to1
	

	def estimate_transformation_mls(self, grid_points, src_points, dst_points, weight_radius, poly_degree):
		"""
		Estimate MLS transformation for the grid points.

		Parameters:
		- grid_points: Nx2 array of grid points.
		- src_points: Nx2 array of source control points.
		- dst_points: Nx2 array of destination control points.
		- weight_radius: Weight radius for MLS.
		- poly_degree: Polynomial degree for MLS.

		Returns:
		- Transformed grid points as two separate arrays: warped_x, warped_y
		"""
		warped_grid = np.zeros_like(grid_points, dtype=np.float32)

		for i, p in enumerate(grid_points):
			# Compute weights
			distances = np.linalg.norm(src_points - p, axis=1)
			weights = np.exp(-(distances**2) / (2 * (weight_radius**2)))
			if np.sum(weights) == 0:
				warped_grid[i] = p
				continue

			# Compute weighted centroids
			p_star = np.sum(src_points * weights[:, np.newaxis], axis=0) / np.sum(weights)
			q_star = np.sum(dst_points * weights[:, np.newaxis], axis=0) / np.sum(weights)

			# Compute deformations
			src_centered = src_points - p_star  # (N, 2)
			dst_centered = dst_points - q_star  # (N, 2)

			# Compute covariance matrix A
			A = np.zeros((2, 2))
			for j in range(len(src_points)):
				A += weights[j] * np.outer(src_centered[j], src_centered[j])

			# Handle singular matrix
			if np.linalg.det(A) < 1e-8:
				warped_grid[i] = p
				continue

			# Compute transformation matrix M
			M = np.linalg.inv(A).dot(np.dot((dst_centered * weights[:, np.newaxis]).T, src_centered))

			# Apply transformation correctly
			warped_p = q_star + np.dot(p - p_star, M)
			warped_grid[i] = warped_p

			# Optional: Print progress for large images
			if i % 100000 == 0 and i > 0:
				click.secho(f"Processed {i} / {len(grid_points)} grid points...")

		warped_x = warped_grid[:,0]
		warped_y = warped_grid[:,1]

		return warped_x, warped_y

	def interpolate_transformation_map(self, grid_x, grid_y, warped_x, warped_y, image_shape):
		height, width = image_shape

		# Create grid for interpolation
		unique_grid_y = np.unique(grid_y)
		unique_grid_x = np.unique(grid_x)
		num_grid_y = len(unique_grid_y)
		num_grid_x = len(unique_grid_x)

		# Ensure that the number of warped points matches the grid dimensions
		try:
			warped_x_grid = warped_x.reshape((num_grid_y, num_grid_x))
			warped_y_grid = warped_y.reshape((num_grid_y, num_grid_x))
		except ValueError as e:
			click.secho(f"Reshape Error: {e}", fg='red')
			click.secho(f"Expected shape: ({num_grid_y}, {num_grid_x}), "
				f"but got array of size {warped_x.size}", fg='red')
			return None, None

		# Use cv2's resize to interpolate the grid transformations
		map_x = cv2.resize(warped_x_grid, (width, height), interpolation=cv2.INTER_CUBIC)
		map_y = cv2.resize(warped_y_grid, (width, height), interpolation=cv2.INTER_CUBIC)

		return map_x.astype(np.float32), map_y.astype(np.float32)


	def estimate_transformation_tps_grid(self, grid_spacing, smoothness):
		height, width = self.image2.shape[:2]
		grid_x, grid_y = np.meshgrid(np.arange(0, width, grid_spacing),
									np.arange(0, height, grid_spacing))
		grid_points = np.vstack([grid_x.ravel(), grid_y.ravel()]).T

		# Estimate TPS transformation on grid points
		warped_x, warped_y = self.estimate_transformation_tps(grid_points, smoothness)
		if warped_x is None or warped_y is None:
			return None, None

		# Interpolate the transformation map
		map_x, map_y = self.interpolate_transformation_map(grid_x.ravel(), grid_y.ravel(),
														warped_x, warped_y,
														self.image2.shape[:2])

		return map_x, map_y


	def estimate_transformation_mls_grid(self, grid_spacing, weight_radius, poly_degree):
		"""
		Estimate MLS transformation for a grid of points.

		Parameters:
		- grid_spacing: Spacing between grid points.
		- weight_radius: Weight radius for MLS.
		- poly_degree: Polynomial degree for MLS.

		Returns:
		- map_x: Full transformation map for x-coordinates.
		- map_y: Full transformation map for y-coordinates.
		"""
		height, width = self.image2.shape[:2]
		grid_x, grid_y = np.meshgrid(np.arange(0, width, grid_spacing),
									 np.arange(0, height, grid_spacing))
		grid_points = np.vstack([grid_x.ravel(), grid_y.ravel()]).T

		# Retrieve source and destination points from point_pairs
		src_points = np.array([pair[0] for pair in self.point_pairs])  # Image1
		dst_points = np.array([pair[1] for pair in self.point_pairs])  # Image2

		# Perform MLS warp on grid points
		warped_x, warped_y = self.estimate_transformation_mls(grid_points, src_points, dst_points, weight_radius, poly_degree)

		# Interpolate the transformation map
		map_x, map_y = self.interpolate_transformation_map(grid_x.ravel(), grid_y.ravel(),
														   warped_x, warped_y,
														   self.image2.shape[:2])

		return map_x, map_y
	
	def plot_transformed_images(self, transformation_matrix_1to2, transformation_matrix_2to1):
		if transformation_matrix_1to2 is None or transformation_matrix_2to1 is None:
			click.secho("[ERROR] Cannot plot transformed images. Transformations are not available.", fg='red')
			return

		# Warp image1 to image2 using the transformation_matrix_1to2
		image1_warped = cv2.warpAffine(self.image1, transformation_matrix_1to2, (self.image2.shape[1], self.image2.shape[0]))

		# Warp image2 to image1 using the transformation_matrix_2to1
		image2_warped = cv2.warpAffine(self.image2, transformation_matrix_2to1, (self.image1.shape[1], self.image1.shape[0]))

		# Plot the transformed images overlayed onto each other
		fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

		ax1.imshow(self.image1, cmap='gray', alpha=0.5)
		ax1.imshow(image2_warped, cmap='hot', alpha=0.5)
		ax1.set_title('Image 1 and Image 2 Warped to Image 1')

		ax2.imshow(self.image2, cmap='gray', alpha=0.5)
		ax2.imshow(image1_warped, cmap='hot', alpha=0.5)
		ax2.set_title('Image 2 and Image 1 Warped to Image 2')

		plt.show()

	def update_overlay(self, event=None):
		"""
		Update the overlay image based on selected transformation method and parameters.
		"""
		if len(self.point_pairs) < 3:
			# Not enough points to perform transformation
			self.ax3.clear()
			self.ax3.imshow(self.image2, cmap='gray')
			self.ax3.set_title('Overlay: Image 2 + Warped Image 1')
			self.fig.canvas.draw()
			return

		# Get current slider values
		transparency = self.slider_transparency.val
		grid_spacing = int(self.slider_grid_spacing.val)  # Updated to get grid spacing from the new slider

		if self.transformation_method == 'Affine':
			transformation_matrix_1to2, transformation_matrix_2to1 = self.estimate_transformations()
			if transformation_matrix_1to2 is None or transformation_matrix_2to1 is None:
				click.secho("[ERROR] Cannot plot transformed images. Transformations are not available.", fg='red')
				return

			# Warp image1 to image2 using the transformation_matrix_1to2
			warped_image1 = cv2.warpAffine(self.image1, transformation_matrix_1to2, (self.image2.shape[1], self.image2.shape[0]))
		
		else:
			if self.transformation_method == 'TPS':
				smoothness = self.slider_tps_smoothness.val
				# Estimate TPS transformation on grid points
				map_x, map_y = self.estimate_transformation_tps_grid(grid_spacing, smoothness)
			elif self.transformation_method == 'MLS':
				weight_radius = self.slider_mls_weight.val
				poly_degree = int(self.slider_mls_poly.val)
				# Estimate MLS transformation on grid points
				map_x, map_y = self.estimate_transformation_mls_grid(grid_spacing, weight_radius, poly_degree)

			if map_x is None or map_y is None:
				self.ax3.set_title(f'Overlay: Image 2 + Warped Image 1 ({self.transformation_method} Failed)')
				self.fig.canvas.draw()
				return

			# Warp the image using the full transformation map
			warped_image1 = cv2.remap(self.image1, map_x, map_y,
									interpolation=cv2.INTER_LINEAR,
									borderMode=cv2.BORDER_REFLECT)

		# Create an RGB overlay
		image2_rgb = self.image2
		warped_image1_rgb = warped_image1

		# Blend the images using the transparency slider
		overlay = cv2.addWeighted(image2_rgb, 1 - transparency, warped_image1_rgb, transparency, 0)

		# Update the third axis
		self.ax3.clear()
		self.ax3.imshow(overlay)
		self.ax3.set_title(f'Overlay: Image 2 + Warped Image 1 ({self.transformation_method})')

		# Optionally, redraw point pairs on the overlay
		for ((x1, y1), (x2, y2), color) in self.point_pairs:
			self.ax3.plot(x2, y2, 'o', markeredgecolor='white',
						markerfacecolor=color, markersize=8)

		self.fig.canvas.draw()

	
	def get_maps(self):
		"""
		Return the transformation maps for x and y coordinates, as well as the transformation type.
		"""
		if self.transformation_method == 'TPS' and len(self.point_pairs) >= 3:
			smoothness = self.slider_tps_smoothness.val
			map_x, map_y = self.estimate_transformation_tps_grid(self.grid_spacing, smoothness)
		elif self.transformation_method == 'MLS' and len(self.point_pairs) >= 3:
			weight_radius = self.slider_mls_weight.val
			poly_degree = int(self.slider_mls_poly.val)
			map_x, map_y = self.estimate_transformation_mls_grid(self.grid_spacing, weight_radius, poly_degree)
		else:
			self.display_message("Not enough points to perform transformation or transformation method not set.", color='red')
			return None, None, None

		return map_x, map_y, self.transformation_method
	
	def get_params(self) -> dict:
		"""
		Return the current parameters for the transformation method.
		"""
		if self.transformation_method == 'TPS':
			return {
				'method': 'TPS',
				'smoothness': self.slider_tps_smoothness.val
			}
		elif self.transformation_method == 'MLS':
			return {
				'method': 'MLS',
				'weight_radius': self.slider_mls_weight.val,
				'poly_degree': int(self.slider_mls_poly.val)
			}
		else:
			return {
				'method': 'None'
			}
		

	def save_warped_image(self, event):
		"""
		Save the warped image to the specified filepath.

		Parameters:
		- filepath: Path to save the warped image.
		"""
		timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
		filepath = f'warped_image_{timestamp}.png'
		click.secho(f"Saving warped image to {filepath}...")
		if self.transformation_method == 'TPS' and len(self.point_pairs) >= 3:
			smoothness = self.slider_tps_smoothness.val
			map_x, map_y = self.estimate_transformation_tps_grid(self.grid_spacing, smoothness)
			if map_x is not None and map_y is not None:
				warped_image1 = cv2.remap(self.image1, map_x, map_y,
										 interpolation=cv2.INTER_LINEAR,
										 borderMode=cv2.BORDER_REFLECT)
				cv2.imwrite(filepath, warped_image1)
		elif self.transformation_method == 'MLS' and len(self.point_pairs) >= 3:
			weight_radius = self.slider_mls_weight.val
			poly_degree = int(self.slider_mls_poly.val)
			map_x, map_y = self.estimate_transformation_mls_grid(self.grid_spacing, weight_radius, poly_degree)
			if map_x is not None and map_y is not None:
				warped_image1 = cv2.remap(self.image1, map_x, map_y,
										 interpolation=cv2.INTER_LINEAR,
										 borderMode=cv2.BORDER_REFLECT)
				cv2.imwrite(filepath, warped_image1)
		else:
			self.display_message("Not enough points to perform transformation or transformation method not set.", color='red')
			return
		
		# Create overlay image:
		overlay = cv2.addWeighted(self.image2, 1 - self.transparency, warped_image1, self.transparency, 0)
		cv2.imwrite(f'overlay_{filepath}', overlay)
		self.display_message(f"Warped image saved to {filepath}", color='green')


	def save_point_pairs(self, x, filepath):
		"""
		Save selected point pairs to a JSON file.

		Parameters:
		- filepath: Path to save the JSON file.
		"""
		import json
		data = [{'source': pair[0], 'destination': pair[1]} for pair in self.point_pairs]
		with open(filepath, 'w') as f:
			json.dump(data, f)
		click.secho(f"Point pairs saved to {filepath}")


	def load_point_pairs(self, filepath):
		"""
		Load point pairs from a JSON file.

		Parameters:
		- filepath: Path to load the JSON file from.
		"""
		import json
		with open(filepath, 'r') as f:
			data = json.load(f)
		self.point_pairs = [(
			(pt['source'][0], pt['source'][1]),
			(pt['destination'][0], pt['destination'][1]),
			'blue'  # Assign a default color or handle accordingly
		) for pt in data]
		self.redraw_points()
		self.update_overlay()
		click.secho(f"Point pairs loaded from {filepath}")


	def redraw_points(self):
		"""
		Redraw all point pairs on the images.
		"""
		self.ax1.clear()
		self.ax2.clear()
		self.ax3.clear()
		self.ax1.imshow(self.image1, cmap='gray')
		self.ax2.imshow(self.image2, cmap='gray')
		self.ax3.imshow(self.image2, cmap='gray')
		self.ax1.set_title('Image 1')
		self.ax2.set_title('Image 2')
		self.ax3.set_title('Overlay: Image 2 + Warped Image 1')

		if self.hints is not None:
			self.set_hints()

		for ((x1, y1), (x2, y2), color) in self.point_pairs:
			self.ax1.plot(x1, y1, 'o', markeredgecolor='white',
						 markerfacecolor=color, markersize=8)
			self.ax2.plot(x2, y2, 'o', markeredgecolor='white',
						 markerfacecolor=color, markersize=8)

		self.fig.canvas.draw()

if __name__ == '__main__':

	 # TEST WITH EXAMPLE IMAGES
	# Generate dummy images for demonstration
	image1 = np.zeros((500, 500, 3), dtype=np.uint8)
	image2 = np.zeros((500, 500, 3), dtype=np.uint8)

	# Draw some circles to represent chromatophores
	cv2.circle(image1, (100, 100), 20, (255, 0, 0), -1)
	cv2.circle(image1, (300, 300), 30, (255, 0, 0), -1)
	cv2.circle(image1, (400, 200), 40, (255, 0, 0), -1)
	cv2.circle(image1, (200, 400), 50, (255, 0, 0), -1)

	cv2.circle(image2, (120, 120), 20, (0, 0, 255), -1)
	cv2.circle(image2, (320, 320), 30, (0, 0, 255), -1)
	cv2.circle(image2, (420, 220), 40, (0, 0, 255), -1)
	cv2.circle(image2, (220, 420), 50, (0, 0, 255), -1)

	# Initialize the selector
	selector = ImagePointSelector(image1, image2)
