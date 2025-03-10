""" Chunking videos into usable segments. 

Analyzing lengthy video recordings of cephalopod skin behavior can be challenging due to issues such as motion blur, defocusing, and obstructions. \
To address these challenges, the video is divided into continuous segments called "chunks." Each chunk consists of consecutive frames where the \
animals mantle, or a portion of it, is both visible and in focus. A region is considered in focus when the edges of its chromatophores are \
sharply defined.

Chunks are identified using focus statistics, which are numerical measures of image sharpness. A common technique employed is the difference \
of Gaussians, which enhances edges by subtracting a heavily blurred version of the image, created using a Gaussian kernel with a larger standard \
deviation, from a less blurred version, created with a smaller standard deviation. This method emphasizes sharp intensity transitions, such as \
chromatophore boundaries, while suppressing gradual intensity variations. The Gaussian kernel parameters are selected to match the typical size \
of chromatophores, improving edge visibility.

Once focus statistics are computed, the video is segmented into smaller clips, or chunks. This process can be further customized to exclude \
frames with other undesirable attributes, such as low brightness, lack of a fluorescent tag, or significant motion blur.
"""

import itertools
import os
import shutil
import subprocess
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from pathlib import Path
import sys

import click
import cv2
from matplotlib import pyplot as plt
import numpy as np
import xarray as xr
import zarr
from tqdm import tqdm

from ..utils.decorators import error_handler


######################################################################################################################################!
################ FOCUS STATISTICS ####################################################################################################!
######################################################################################################################################!
def difference_of_gaussian(img: np.ndarray, sigma_1: float, sigma_2: float, size_1: float, size_2: float, threshold: float) -> float:
	""" Calculate the focus of an image by Difference of Gaussian.

	Args:
		img (np.ndarray): A single image of shape (width, height, channels).
		sigma_1 (float): Standard deviation of the first Gaussian filter.
		sigma_2 (float): Standard deviation of the second Gaussian filter.
		size_1 (float): Size of the first Gaussian filter.
		size_2 (float): Size of the second Gaussian filter.
		threshold (float): Threshold to determine in-focus frames.

	Returns:
		A single value representing the DoG-focus-score of the image.	
	"""
	red_frame= np.single(img[:,:,2])

	blur1 = cv2.GaussianBlur(red_frame, (size_1, size_1), sigma_1)
	blur2 = cv2.GaussianBlur(red_frame, (size_2, size_2), sigma_2)

	blur_diff = blur1 - blur2
	return np.mean(blur_diff > threshold)


######################################################################################################################################!
################ CHUNKING ############################################################################################################!
######################################################################################################################################!
def calculate_focus_score(video_file: str, focus_func: Callable) -> np.ndarray:
	""" Calculate focus scores for all frames in a video.
	
	Args:
		video_file (str): Path to the video file.
		focus_func (Callable): Function to calculate focus score for a single frame.
		
	Returns:
		np.ndarray: Array of focus scores for all frames in the video.
		
	Raises:
		AssertionError: If the video file can't be opened.
		Warnings: If some focus values are not calculated and set to NaN.
		
	Notes:
		- Uses concurrent.futures.ThreadPoolExecutor to parallelize focus calculation.
	"""
	cap = cv2.VideoCapture(video_file)
	assert cap.isOpened(), f"Can't open video {video_file}."

	frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	focus = [None] * frame_count  # Pre-allocate list with None
	progress_bar = tqdm(total=frame_count, desc='Calculating Focus', unit='frames', file=sys.stdout)

	def process_frame(index, frame):
		return index, focus_func(frame)

	with ThreadPoolExecutor() as executor:
		futures = []
		for index in range(frame_count):
			ret, frame = cap.read()
			if not ret:
				break
			futures.append(executor.submit(process_frame, index, frame))
			progress_bar.update(1)

		for future in futures:
			index, focus_value = future.result()
			focus[index] = focus_value

	cap.release()
	if None in focus:
		click.secho(f'[WARNING] Video {video_file} has {frame_count} frames, but some focus values were not calculated and set to NaN.', fg='yellow', bold=True)
	return np.array(focus)
	

def compute_chunks(video_file: str, focus_statistic: str|Callable, focus_threshold: float=0.001,
				   onset: int=0, min_chunk_duration: int=0, **kwargs) -> tuple[np.ndarray[float]]:
	"""
	Compute in-focus chunks of a video based on focus statistics.

	Args:
		video_file (str): Path to the video file.
		focus_statistic (str | Callable): Method to calculate focus. Can be 'dog' or 'difference of gaussian' for built-in method, or a custom callable function.
		focus_threshold (float, optional): Threshold to determine in-focus frames. Defaults to 0.001.
		onset (int, optional): Frame offset to apply to chunk onsets. Defaults to 0.
		min_chunk_duration (int, optional): Minimum duration (in frames) for a chunk to be considered valid. Defaults to 0.
		**kwargs: Additional keyword arguments to pass to the focus calculation function.

	Returns:
		tuple[np.ndarray[float]]: A tuple containing:
			- in_focus (np.ndarray[bool]): Boolean array indicating which frames are in focus.
			- chunk_times (np.ndarray[int]): 2D array of chunk start and end times.
			- chunk_durations (np.ndarray[int]): 1D array of chunk durations.

	Raises:
		ValueError: If focus_statistic is not 'dog', 'difference of gaussian', or a callable.
		AssertionError: If the video file can't be opened.

	Notes:
		- Uses dask for parallel computation of focus statistics.
		- Filters out chunks shorter than min_chunk_duration.
		- Returns None for chunk_times and chunk_durations if no valid chunks are found.
	"""
	# Load the focus statistic function:
	if isinstance(focus_statistic, str) and focus_statistic.lower() in ['dog', 'difference of gaussian']:
			focus_func = partial(difference_of_gaussian, **kwargs)
	elif isinstance(focus_statistic, Callable):
		focus_func = partial(focus_statistic, **kwargs)
	else:
		raise ValueError('focus_statistic must be in ["dog", "difference of gaussian"] or callable.')
	
	# Compute focus statistics for each frame:
	if focus_threshold > 0:
		click.echo(f'Computing focus statistics for video {video_file}...')
		statistic = calculate_focus_score(video_file, focus_func)
	else:
		click.echo('Focus threshold zero specified. All frames will be considered in-focus.')
		cap = cv2.VideoCapture(video_file)
		assert cap.isOpened(), f"Can't open video {video_file}."
		n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
		cap.release()
		statistic = np.ones(n_frames, dtype=float)
	
	# Compute in-focus frames:
	in_focus = statistic > focus_threshold
	click.echo(f'Found {np.mean(in_focus):.2f} ({np.sum(in_focus)}/{in_focus.size}) in-focus frames in video {video_file}.')

	# Check if there are enough in-focus frames to have at least one chunk:
	problem_solved = False
	while not problem_solved:
		if np.sum(in_focus) < min_chunk_duration:
			click.secho(f'[CHUNKING][ERROR] Video {video_file} has only {np.sum(in_focus)} in-focus frames in total, but a minimum of {min_chunk_duration} in-focus \
				frames per chunk are requested.', err=True, fg='red')
			
		elif max([len(list(g)) if k == 1 else 0 for k, g in itertools.groupby(in_focus)]) < min_chunk_duration:
			click.secho(f'[CHUNKING][ERROR] Video {video_file} has no chunk with at least {min_chunk_duration} in-focus frames.', err=True, fg='red')
		
		else:
			problem_solved = True
		
		if (np.sum(in_focus) < min_chunk_duration) or (max([len(list(g)) if k == 1 else 0 for k, g in itertools.groupby(in_focus)]) < min_chunk_duration):
			plt.plot(statistic)
			plt.title('Focus Statistics')
			plt.show()

			focus_threshold = float(input('Enter a new focus threshold (float, 0.xxx): '))
			in_focus = statistic > focus_threshold
			click.echo(f'Found {np.mean(in_focus):.2f} ({np.sum(in_focus)}/{in_focus.size}) in-focus frames in video {video_file}.')



	# Check chunk durations and filter out chunks that are too short:
	thresh_crosses = np.diff(in_focus.astype(int))
	onsets = np.where(thresh_crosses == 1)[0]
	offsets = np.where(thresh_crosses == -1)[0]

	if len(onsets) == 0:
		onsets=np.array([0])

	if len(offsets) == 0:
		offsets = np.array([len(in_focus)])

	if offsets[0] < onsets[0]:
		onsets = np.append([0], onsets)

	if offsets[-1] < onsets[-1]:
		offsets = np.append(offsets, [len(in_focus)-1])

	chunk_durations = offsets - onsets
	good_chunks = chunk_durations > min_chunk_duration
	onsets, offsets, chunk_durations = onsets[good_chunks], offsets[good_chunks], chunk_durations[good_chunks]

	onsets += onset + 1
	offsets -= onset + 1  
	chunk_durations = offsets - onsets

	chunk_times = np.array([onsets, offsets], dtype=int).T
	return in_focus, chunk_times, chunk_durations, statistic


def cut_video_into_chunks(input_video: str, chunk_times: np.ndarray, fps: int=20, output_dir: str|Path|None=None, copy: bool=False) -> np.ndarray[str]:
	"""
	Cut a video into chunks based on specified time intervals.

	Args:
		input_video (str): Path to the input video file.
		chunk_times (np.ndarray): 2D array of chunk start and end times in frames.
		fps (int, optional): Frame rate for output chunks. Defaults to 20.
		output_dir (str | Path | None, optional): Directory to save output chunks. If None, uses input video's directory. Defaults to None.
		copy (bool, optional): Whether to copy the input video to the output directory as a pseudo-chunk `chunk_0` (e.g. when focus_threshold=0). Defaults to False.

	Returns:
		np.ndarray[str]: Array of paths to the created video chunks.

	Raises:
		RuntimeError: If ffmpeg command fails to execute.

	Notes:
		- Uses ffmpeg to cut video chunks.
		- Adds metadata to each chunk including title, comment (original video path), and artist.
		- Creates output directory if it doesn't exist.
	"""
	output_dir = Path(output_dir) if output_dir else Path(input_video).parent
	chunk_paths = []
	if copy:
		# Copy the input video to the output directory as pseudo-chunk `chunk_0`:
		chunk_path = str(output_dir / f'{Path(input_video).stem}_chunk_0.mp4')
		if not os.path.exists(chunk_path):
			os.makedirs(Path(chunk_path).parent, exist_ok=True)
		click.echo(f'Copying video {input_video} to {chunk_path}...')
		try:
			shutil.copy(input_video, chunk_path)
		except Exception as e:
			raise RuntimeError(f"Error copying file: {e}")
		chunk_paths.append(chunk_path)
		return chunk_paths


	for i, (onset, offset) in tqdm(enumerate(chunk_times), total=len(chunk_times), desc='Cutting Chunks', unit='chunk', file=sys.stdout):
		chunk_path = str(output_dir / f'{Path(input_video).stem}_chunk_{i}.mp4')
		chunk_paths.append(chunk_path)
		# Check if all directories of chunk_path exist, if not create them:
		if not os.path.exists(chunk_path):
			os.makedirs(Path(chunk_path).parent, exist_ok=True)
		ffmpeg_command = fr"ffmpeg -y -i {input_video} -vf 'select=between(n\,{onset}\,{offset}),setpts=PTS-STARTPTS' -af 'aselect=between(n\,{onset}\,{offset}),setpts=PTS-STARTPTS' -r {fps} -metadata title='Chunk {i}' -metadata comment='original video: {input_video}' -metadata artist='j'  {chunk_path}"
		if os.name == 'nt':  # On Windows
			ffmpeg_command = 'powershell ' + ffmpeg_command
		result = subprocess.run(ffmpeg_command, stderr=subprocess.PIPE, shell=True, text=True)
		if result.returncode != 0:
			raise RuntimeError(result.stderr.decode('utf-8'))
	return chunk_paths


# MAIN FUNCTION:
@error_handler('Chunking')
def chunking(video_file: str, focus_statistic: str|Callable, focus_parameters: dict, focus_threshold: float=0.0, onset: int=0,
			 min_chunk_duration: int=0, output_dir: str|Path|None=None, output_name: str|Path|None=None, force_overwrite: bool=False,
			 cluster_args: None|str|dict={'processes': False, 'n_workers': 1, 'threads_per_worker': 4}) -> tuple[bool, str]:
	""" Chunk a video into in-focus segments based on focus statistics.

	Args:
		video_file (str): Path to the video file.
		focus_statistic (str | Callable): Method to calculate focus. Can be 'dog' or 'difference of gaussian' for built-in method, or a custom callable function.
		focus_parameters (dict): Parameters to pass to the focus calculation function.
		focus_threshold (float, optional): Threshold to determine in-focus frames. Defaults to 0.0.
		onset (int, optional): Frame offset to apply to chunk onsets. Defaults to 0.
		min_chunk_duration (int, optional): Minimum duration (in frames) for a chunk to be considered valid. Defaults to 0.
		output_dir (str | Path | None, optional): Directory to save output chunks. If None, uses input video's directory. Defaults to None.
		output_name (str | Path | None, optional): Path to save the output dataset. If None, uses the input video's name with .dataset extension. Defaults to None.
		force_overwrite (bool, optional): Whether to overwrite existing output files. Defaults to False.
		cluster_args (None | str | dict, optional): Arguments to pass to the Dask cluster. Defaults to {'processes': False, 'n_workers': 1, 'threads_per_worker': 4}.

	Returns:
		retval (bool): True if successful, False otherwise.
		output_name (str): Path to the output dataset.

	Raises:
		FileExistsError: If the output file already exists and force_overwrite is False.
		ValueError: If no valid chunks are found.

	Notes:
		- Saves the chunking information to a Zarr dataset.
		- Uses concurrent.futures.ThreadPoolExecutor for parallel computation of focus statistics.
	"""

	if output_dir is None and output_name is not None:
		output_dir = Path(output_name).parent
	elif output_dir is None:
		output_dir = Path(video_file).parent
	elif not Path(output_dir).is_dir():
		os.makedirs(output_dir)
		output_dir = Path(output_dir)
	else:
		assert Path(output_dir).is_dir(), 'Output directory does not exist.'
		output_dir = Path(output_dir)
	
	if output_name is None:
		output_name = output_dir / Path(video_file).with_suffix('.dataset').name
	else:
		output_name = Path(output_name)
		assert Path(output_name).parent.is_dir(), 'Parent directory of `output_name` does not exist.'

	if output_name.exists() and not force_overwrite:
		click.secho(f'WARNING: Output file {output_name} already exists. Aborting. Run with `force_overwrite=True` to overwrite.', fg='yellow', italic=True)
		raise FileExistsError(f'Output file {output_name} already exists. Aborting.')
	elif output_name.exists() and force_overwrite:
		click.secho(f'WARNING: Overwriting existing file {output_name}.', fg='yellow', italic=True)
		# Remove directory if it exists:
		if output_name.is_dir():	
			shutil.rmtree(output_name)
		else:
			os.remove(output_name)

	cap = cv2.VideoCapture(video_file)
	fps = int(cap.get(cv2.CAP_PROP_FPS)) 
	in_focus, chunk_times, chunk_durations, statistic = compute_chunks(video_file,
															focus_statistic=focus_statistic,
															focus_threshold=focus_threshold,
															onset=onset,
															min_chunk_duration=min_chunk_duration,
															**focus_parameters)
	
	if chunk_times is None:
		raise ValueError('No valid chunks found.')
	
	chunk_paths = cut_video_into_chunks(video_file, chunk_times, fps, output_dir, copy=focus_threshold==0)

	dataset = xr.Dataset(
		{
			'focus': (['frame'], in_focus),
			'focus_statistic': (['frame'], statistic),
			'chunk_paths': (['chunk'], chunk_paths),
			'chunk_times': (['chunk', 'boundary'], chunk_times),
			'chunk_durations': (['chunk'], chunk_durations),
		},
		coords={
			'frame': list(range(len(in_focus))),
			'chunk': list(range(len(chunk_paths))),
		},
		attrs={
			'nr_frames': len(chunk_durations),
			'focus_statistic': focus_statistic,
			'focus_threshold': focus_threshold,
			'min_chunk_duration': min_chunk_duration,
			'onset': onset,
			'original_video': video_file,
			**focus_parameters,
		}
	)	
	
	zarr_store = zarr.DirectoryStore(str(output_name))
	dataset.to_zarr(zarr_store, group='chunking', mode='w')

	return True, str(output_name)



# VISUALIZATION FUNCTIONS:
@error_handler('Show focus statistics', cluster=False)
def show_focus(dataset: str):
	chunking = xr.open_zarr(dataset, group='chunking')
	chunking.focus_statistic.plot.line()
	plt.show()
