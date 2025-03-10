import copy
import threading

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import to_rgb
from matplotlib.widgets import Button, Slider
from skimage.segmentation import find_boundaries

from .motion_marker_utils import compute_stats, stats2mms

mpl.rcParams['axes.spines.top']    = False
mpl.rcParams['axes.spines.right']  = False
mpl.rcParams['axes.spines.left']   = False
mpl.rcParams['axes.spines.bottom'] = False


BROWN = "#f76700"
BROWN_RGB = (np.array(to_rgb(BROWN)) * 255).astype(int)
GREEN = '#5ff700'
GREEN_RGB = (np.array(to_rgb(GREEN)) * 255).astype(int)


class InteractiveMotionMarkerTuner:
    def __init__(
        self,
        areas: np.ndarray,
        masterframe: np.ndarray,
        chunkaverage: np.ndarray,
        cleanqueen: np.ndarray,
        # Default parameters
        max_eccentricity: float = 0.6,
        max_area: float = 2000,
        max_cv: float = 1.0,
        zero_proportion: float = 0.5,
        zero_consecutive: int = 10,
        params: dict = None,
        debug: bool = False
    ):
        """
        Create an interactive tuner for the 'motion marker' detection parameters.
        """
        self.debug = debug
        self.masterframe = masterframe
        self.chunkaverage = chunkaverage
        self.cleanqueen = cleanqueen
        self.num_chromatophores = areas.shape[1]  # or areas.shape[0], depending on orientation

        self.cleanqueen_borders = find_boundaries(cleanqueen, mode='inner')

        
        self.param_default = {
            "Max eccentricity:": {'start': 0.0, 'end': 2.0, 'step': 0.01, 'value': max_eccentricity, 'active': True},
            "Max area:": {'start': 0.0, 'end': 10000.0, 'step': 1, 'value': max_area, 'active': True},
            "Max CV:": {'start': 0.0, 'end': 1.0, 'step': 0.01, 'value': max_cv, 'active': True},
            "Zero proportion:": {'start': 0.0, 'end': 1.0, 'step': 0.01, 'value': zero_proportion, 'active': True},
            "Zero consecutive:": {'start': 0, 'end': 100, 'step': 1, 'value': zero_consecutive, 'active': True},
        }
        if params is not None:
            self.param_default = params
        self.param = copy.deepcopy(self.param_default)

        # Will store the final indices of motion markers
        self.current_motion_markers = np.array([], dtype=int)

        # Matplotlib objects we’ll create in self.run()

        self.fig = None
        self.ax_main = None
        self.im_handle = None

        self.sliders = {}
        self.buttons = {}
        self.reset_button = None

        # Debounce-related
        self._debounce_timer = None
        self._debounce_delay = 0.3  # seconds

        self.stats = compute_stats(areas, masterframe, cleanqueen)

    def run(self):
        """
        Initialize the interactive window, block until closed,
        and return final motion markers.
        """
        # --- Create figure with enough space for sliders + checkboxes ---
        self.fig = plt.figure(figsize=(8, 8))
        if hasattr(self.fig.canvas.manager, 'set_window_title'):
            self.fig.canvas.manager.set_window_title("Interactive Motion Marker Tuner")

        # We'll define a grid layout:
        #   row 0: main image
        #   rows 1..5: slider + checkbox pairs
        #   row 6: reset button
        # Adjust as needed for aesthetics
        gs = self.fig.add_gridspec(nrows=7, ncols=1, left=0.1, right=0.95, top=0.92, bottom=0.08, wspace=0.1, hspace=0.08,
                                   height_ratios=[20, 1, 1, 1, 1, 1, 1])
        top_gs = gs[0].subgridspec(1, 2, width_ratios=[1, 1])
        bottom_gs = gs[1:].subgridspec(6, 2, width_ratios=[9, 1])

        self.ax_left_image = self.fig.add_subplot(top_gs[0, 0])
        self.ax_left_image.set_xticks([])
        self.ax_left_image.set_yticks([])
        self.ax_right_image = self.fig.add_subplot(top_gs[0, 1])
        self.ax_right_image.set_xticks([])
        self.ax_right_image.set_yticks([])   

        plot_masterframe, plot_chunkaverage = self._make_plotframes()
        self.left_image_handle = self.ax_left_image.imshow(plot_masterframe)
        self.right_image_handle = self.ax_right_image.imshow(plot_chunkaverage)
    
        for row, (key, data) in enumerate(self.param.items()):
            ax_slider = self.fig.add_subplot(bottom_gs[row, 0])
            ax_button  = self.fig.add_subplot(bottom_gs[row, 1])

            # Remove ticks from the checkbox subplot
            ax_button.set_xticks([])
            ax_button.set_yticks([])

            # Create slider
            slider = Slider(
                ax_slider, key, data['start'], data['end'],
                valinit=data['value'],
                valstep=data['step'],
                initcolor='lightgrey',
                track_color='lightgrey',
                handle_style={
                    'facecolor': BROWN,
                    'edgecolor': 'white',
                    'size': 12
                },
                color=BROWN,
            )
            slider.on_changed(self._on_slider_changed)
            self.sliders[key] = slider

            # -- Create a toggle Button --
            # We'll default everything to "active=True" for demonstration
            button = Button(ax_button, '')
            self.buttons[key] = button
            self._set_button_appearance(key, button)
            button.on_clicked(lambda event, k=key, b=button: self._on_button_changed(k, b))


        # Finally row 6: reset button across 2 columns
        ax_reset = self.fig.add_subplot(gs[6, :])
        ax_reset.set_xticks([])
        ax_reset.set_yticks([])
        self.reset_button = Button(ax_reset, 'Reset All', color='lightgrey', hovercolor=BROWN)
        self.reset_button.label.set_color(BROWN)
        self.reset_button.label.set_fontsize(12)
        self.reset_button.on_clicked(self._on_reset)

        # On close event, we store final data
        self.fig.canvas.mpl_connect('close_event', self._on_close)

        # Do an initial update
        self._update_plot()

        # Show the window and block until closed
        plt.show()

        # Return final result
        return self.current_motion_markers

    # -----------------------
    # Internal helper methods
    # -----------------------
    def _on_slider_changed(self, val):
        """
        Called whenever the slider moves. We schedule the 'real'
        update after a delay. If the user moves the slider again
        before the timer fires, we cancel and reschedule.
        """
        # Cancel any existing timer
        if self._debounce_timer is not None:
            self._debounce_timer.cancel()

        # Start a new timer
        self._debounce_timer = threading.Timer(self._debounce_delay, self._on_slider_debounced)
        self._debounce_timer.start()

    def _on_slider_debounced(self):
        """
        Fires only if the user hasn't moved the slider for
        self._debounce_delay seconds.
        """
        self.fig.canvas.manager.window.after(0, lambda: self._update_plot())


    def _set_button_appearance(self, param_key, button):
        """
        Chooses facecolor, hovercolor, text, and text color
        based on whether param_key is active.
        """
        active = self.param[param_key]['active']
        if active:
            label_text = "Selected"
            face_color = BROWN
            text_color = "white"
            hover_color = "lightgrey"

        else:
            label_text = "Select"
            face_color = "white"
            text_color = BROWN
            hover_color = "lightgrey"

        # Update the button
        button.label.set_text(label_text)
        button.label.set_color(text_color)
        button.label.set_fontsize(12)
        button.hovercolor = hover_color
        button.edgecolor = "none"
        button.color = face_color


    def _make_plotframes(self):
        """Create the background image as an RGB frame. 
           You can adapt your logic to highlight the masterframe as needed."""
        masterframe = self.masterframe
        norm = masterframe / (masterframe.max() if masterframe.max() != 0 else 1)
        # invert for demonstration
        frame = np.stack((255 - 255*norm,)*3, axis=-1).astype(np.uint8)

        chunkaverage = self.chunkaverage.copy()
        chunkaverage[self.cleanqueen_borders] = 255
        return frame, chunkaverage

    def _on_button_changed(self, param_key, button):
        self.param[param_key]['active'] = not self.param[param_key]['active']
        self._set_button_appearance(param_key, button)
        self._update_plot()

    def _on_reset(self, event):
        self.param = copy.deepcopy(self.param_default)
        # Update the actual slider + checkbox controls
        # Sliders
        for key, slider in self.sliders.items():
            slider.set_val(self.param[key]['value'])
        # Buttons
        for key, button in self.buttons.items():
            self._set_button_appearance(key, button)
        # Recompute
        self._update_plot()

    def _on_close(self, event):
        # The figure is closing.
        # If desired, you can store final parameters or do cleanup here.
        pass
        

    def _update_plot(self, *args, **kwargs):
        """Recompute motion markers and update the displayed image + title."""
        for key, slider in self.sliders.items():
            self.param[key]['value'] = slider.val

        # Call the compute function
        mm = stats2mms(self.stats, self.param, self.debug)
        self.current_motion_markers = mm

        # Rebuild the background frame
        new_masterframe, new_chunkaverage = self._make_plotframes()

        # Color those markers in red
        mask = np.isin(self.cleanqueen, mm)
        new_masterframe[mask & (self.masterframe > 0.1)] = BROWN_RGB

        new_chunkaverage[mask & ~(self.masterframe > 0.1)] = GREEN_RGB
        new_chunkaverage[self.cleanqueen_borders] = 255

        # Update image
        self.left_image_handle.set_data(new_masterframe)
        self.right_image_handle.set_data(new_chunkaverage)

        # Update title: "X motion markers (Y chromatophores, Z%)"
        num_mm = len(mm)
        pct = 100.0 * num_mm / self.num_chromatophores
        self.fig.suptitle(f"{num_mm} motion markers ({self.num_chromatophores} chromatophores, {pct:.1f}%)", color=BROWN, fontsize=16)

        self.fig.canvas.draw_idle()
