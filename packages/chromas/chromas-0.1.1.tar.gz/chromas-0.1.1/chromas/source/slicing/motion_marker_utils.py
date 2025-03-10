import click
import numpy as np
from skimage.measure import regionprops


def max_consecutive_zero_streak(arr):
    """Return the maximum number of consecutive zeros in a 1D array."""
    max_streak = 0
    current_streak = 0
    for val in arr:
        if val == 0:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0
    return max_streak

def compute_stats(areas: np.ndarray, masterframe: np.ndarray, cleanqueen: np.ndarray,):
    # Transpose so shape = (N_chromatophores, N_frames)
    areas_t = areas.T

    eccentricity = {x.label: x.eccentricity for x in regionprops((masterframe > 0) * cleanqueen)}
    # Make numpy array for eccentricity:
    eccentricity = np.array([eccentricity.get(i, 0) for i in range(areas_t.shape[0])])

    # zero-area filters
    zero_area = np.mean(areas_t == 0, axis=1)   # fraction of frames = 0
    zero_cons = np.apply_along_axis(max_consecutive_zero_streak, 1, areas_t)
    max_area = np.max(areas_t, axis=1)
    cv = np.std(areas_t, axis=1) / np.mean(areas_t, axis=1)

    return {
        "Max eccentricity:": eccentricity,
        "Max area:": max_area,
        "Max CV:": cv,
        "Zero proportion:": zero_area,
        "Zero consecutive:": zero_cons,
    }


def stats2mms(stats: dict, param: dict, debug: bool = False) -> np.ndarray:
    cond = np.ones(stats["Max eccentricity:"].shape, dtype=bool)
    for key, data in param.items():
        if data['active']:
            cond &= stats[key] <= data['value']

    motion_markers = np.argwhere(cond)[:, 0]

    if debug:
        click.secho(f'[DEBUG][MM] Found {len(motion_markers)} chromatophores out of {len(cond)} ({100*len(motion_markers)/len(cond):.2f}%).', fg='yellow')
    return motion_markers
