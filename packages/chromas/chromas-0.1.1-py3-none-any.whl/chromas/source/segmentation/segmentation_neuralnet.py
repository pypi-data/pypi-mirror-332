""" Chromatophore Segmentation.

Accurate identification and isolation of individual chromatophores in video frames are crucial for detailed analysis. \
The process of "segmentation" involves creating a binarized image where each pixel is classified as either part of a \
chromatophore or the background. Chromatophore color classification is also supported, allowing classification into \
categories such as dark, orange, and yellow.

Segmentation is powered by deep learning models trained on manually annotated datasets. Two pre-trained models are \
available: one for binary segmentation (presence or absence of chromatophores) and another for chromatophore color \
segmentation. These models were developed using annotated data from Sepia officinalis and Euprymna berryi captured \
under diverse lighting conditions and camera setups. They can also be fine-tuned for custom datasets or used as a \
starting point to train new models for research on other species.

Available model architectures include Fully Convolutional Networks (FCN), DeepLabV3, and U-Net, with backbone networks \
such as ResNet50, ResNet101, or MobileNetv3-Large. Alternatively, segmentation can be performed using a Random Forest \
Classifier or a hybrid approach combining both methods, followed by a majority vote for improved accuracy.
"""

from pathlib import Path

import click
import cv2
import dask.array as da
import numpy as np
import torch
import xarray as xr
from kornia.contrib import combine_tensor_patches, extract_tensor_patches
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from skimage.segmentation import mark_boundaries
from torchvision import transforms

from ..utils.decorators import error_handler
from ..utils.image import warp_frame
from .neuralnet_utils import get_model

import decord  # ITS VERY IMPORTANT TO IMPORT DECORD AFTER TORCHVISION TO AVOID SEGMENTATION FAULTS!


def load(frame_idx: list[int], video_file: str) -> torch.Tensor:
	""" Load frames from a video file.

	Args:
		frame_idx (list[int]): List of frame indices to load.
		video_file (str): Path to the video file.

	Returns:
		torch.Tensor: Loaded frames.

	Raises:
		ValueError: If the video file cannot be opened or a frame cannot be read.

	Example:
		>>> frames = load([0, 10, 20], 'video.mp4')

	Notes:
		- The video file is opened using OpenCV.
	"""
	# Open the video file
	cap = cv2.VideoCapture(video_file)
	if not cap.isOpened():
		raise ValueError(f"Failed to open video file: {video_file}")

	frames = []
	for idx in frame_idx:
		# print(f'Loading frame {idx}.\tGPU_MEM: {torch.cuda.memory_allocated()}')
		cap.set(cv2.CAP_PROP_POS_FRAMES, idx)  # Set the frame position
		ret, frame = cap.read()
		if not ret:
			raise ValueError(f"Failed to read frame at index {idx}")
		# Convert BGR to RGB
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		frames.append(frame)

	cap.release()

	# Convert frames to torch.Tensor
	frames = np.stack(frames)  # Stack into a single numpy array
	frames_tensor = torch.from_numpy(frames).float()
	del frames, cap
	# print(f'Loaded frames.\tGPU_MEM: {torch.cuda.memory_allocated()}')
	return frames_tensor


def predict(img: torch.Tensor, model: torch.nn.Module, window_size: int = 256, stride: int = 220) -> np.ndarray:
	""" Predict segmentation masks for a batch of frames.

	Args:
		img (torch.Tensor): Batch of frames.
		model (torch.nn.Module): Segmentation model.
		window_size (int): Patch size. Default is 256.
		stride (int): Stride for patch extraction. Default is 220.

	Returns:
		np.ndarray: Segmentation masks.

	Notes:
		- The input tensor should have shape (n_frames, height, width, channels).
		- The output tensor has shape (n_frames, height, width).

	Example:
		>>> img = torch.rand(3, 256, 256, 3)
		>>> model = get_model()
		>>> masks = predict(img, model)
	"""
	img_size = img.shape[1:3]
	normalize = transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])

	# Normalize and move to GPU
	img_normalized = normalize(img.half().permute(0, 3, 1, 2) / 255).cuda()

	# Extract patches
	batch = extract_tensor_patches(img_normalized, window_size, stride, allow_auto_padding=True)
	batch = batch.view(-1, *batch.shape[2:])  # Reshape for model input

	# Run model inference
	with torch.no_grad():
		out = model(batch)['out']

	# Reshape output to match input frames
	out = out.view(img.shape[0], -1, *out.shape[1:])

	# Combine patches and compute final masks
	img_combined = combine_tensor_patches(out, img_size, window_size, stride, allow_auto_unpadding=True)
	img_cpu = torch.argmax(img_combined, 1).cpu().numpy().astype(np.uint8)

	# Explicit memory cleanup
	del img_normalized, batch, out, img_combined, normalize
	return img_cpu



# MAIN FUNCTION:
@error_handler('Segmentation (neuralnet)', cluster=True)
def segmentation(dataset: str,
				 weights: str = '/gpfs/laur/data/renardm/training_data/240823-006/model/fcn_resnet50_100_best_model.pth',
				 n_classes: int = 2,
				 cluster_args: dict = None,
				 debug_args: dict = dict({'debug': False, 'debug_visual': False}),
				 architecture: str = 'fcn_resnet50',
				 window_size: int = 512,
				 stride: int = 480
				 ):
	""" Perform segmentation on a dataset of video chunks.

	Args:
		dataset (str): Path to the dataset.
		model_architecture (str): Model architecture.
		model_weights (str): Path to model weights.
		n_classes (int): Number of classes. Default is 2.
		cluster_args (dict): Dask cluster arguments. Default is {'n_workers': 1}.
		window_size (int): Patch size. Default is 512.
		stride (int): Stride for patch extraction. Default is 480.

	Raises:
		ValueError: If the dataset is not a directory.
	"""
	chunking_dataset = xr.open_zarr(dataset, group='chunking')

	video_file = str(chunking_dataset.chunk_paths[0].data.compute())
	cap = cv2.VideoCapture(video_file)
	if not cap.isOpened():
		raise ValueError(f"Failed to open video file: {video_file}")
	img_size = (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
	cap.release()

	with click.progressbar(enumerate(zip(chunking_dataset.chunk_times.compute(), chunking_dataset.chunk_paths.compute())),
						label='Segment chunks', show_percent=True, show_pos=True) as bar:
		for chunk_idx, (chunk_time, chunk_path) in bar:
			start, end = chunk_time.data
			video_file = str(chunk_path.data)

			def _segment_frames(frame_idxs):
				model = get_model(architecture, num_classes=n_classes, weights=weights)
				model.eval()
				model.cuda()
				frames = load(frame_idxs, video_file)
				predictions = predict(frames, model, window_size, stride)
				del frames, model
				return predictions

			# Create a Dask array of frame indices
			frames = (da.arange(end - start, chunks=(1,)))
			# Rechunk dask array frames to (3,-1):
			blocksize = 1
			frames = frames.rechunk((blocksize, -1))
			predictions = da.map_blocks(_segment_frames, frames, dtype=np.uint8, chunks=(blocksize, *img_size), new_axis=[1, 2])
			predictions = predictions.rechunk((1, *img_size))

			predictions = xr.DataArray(predictions, dims=['frame', 'x', 'y'], name='segmentation',
													coords={'frame': np.arange(len(predictions))},
													attrs={'chunk_path': video_file,
														'chunk_idx': chunk_idx, 'start': start, 'end': end,
														'img_size': img_size, 'model_architecture': architecture,
														'model_weights': weights})
			predictions.to_zarr(dataset, group=f'chunk_{chunk_idx}', mode='w')


########################################################################################################################!
#################### VISUALIZATION AND TESTING FUNCTIONS ###############################################################!
########################################################################################################################!
@error_handler('Show segmentation', cluster=False)
def show_segmentation(dataset: str, chunk: int, frame: int, overlay: bool=True) -> None:
	""" Show the segmentation for a specific frame of a chunk.

	Args:
		dataset (str): Path to the dataset.
		chunk (int): Chunk number.
		frame (int): Frame number.
		overlay (bool): Overlay the segmentation on the original frame. Default is True.

	Raises:
		ValueError: If the dataset is not a directory.

	Example:
		>>> show_segmentation('dataset.zarr', 0, 10)

	Notes:
		- Displays the segmentation in an interactive window using matplotlib.
	"""
	# Check that dataset is a directory
	overlay = False
	chunk_nr = int(chunk)
	assert Path(dataset).is_dir(), f'{dataset} is not a valid dataset. Show-segmentation does not take videos as input, but datasets geneated through e.g. segmentation.'
	chunk = xr.open_zarr(dataset, group=f'chunk_{chunk}')
	if not overlay:
		chunk.segmentation.isel(frame=frame).plot.imshow(yincrease=False, cmap=ListedColormap([[126/255, 36/255, 10/255], [255/255, 179/255, 0], [1, 1, 1]]), add_colorbar=False)
	else:
		cap = cv2.VideoCapture(chunk.segmentation.attrs['chunk_path'])
		if not cap.isOpened():
			raise ValueError
		cap.set(cv2.CAP_PROP_POS_FRAMES, max(0, frame-1))
		_, img = cap.read()
		segmentation = chunk.segmentation.isel(frame=frame).data.compute()
		img = mark_boundaries(img, segmentation==1, color=(0, 1, 0))
		img = mark_boundaries(img, segmentation==2, color=(1, 0, 0))
		img = mark_boundaries(img, segmentation==3, color=(0, 0, 1))
		plt.imshow(img)
		plt.title(f'Segmentation for frame {frame} of chunk {chunk_nr}.')

	fig = plt.gcf()
	fig.canvas.manager.set_window_title('CHROMAS - Visualizing Segmentation')
	plt.show()


@error_handler('Generate overlay video', cluster=False)
def generate_overlay_video(dataset: str, chunk: int, output: str=None, fps: int=None, start: int=None, end: int=None) -> None:
	""" Generate an overlay video with segmentation for a chunk.

	Args:
		dataset (str): Path to the dataset.
		chunk (int): Chunk number.
		output (str): Path to the output video file. Default is None.
		fps (int): Frames per second. Default is None.
		start (int): Start frame. Default is None.
		end (int): End frame. Default is None.

	Raises:
		ValueError: If the dataset is not a directory.

	Example:
		>>> generate_overlay_video('dataset.zarr', 0, 'output.mp4', fps=30, start=0, end=100)

	Notes:
		- The output video will have the same resolution as the original video.
		- The segmentation will be overlaid on the original video frames.
		- The segmentation colors are red, green, and blue for classes 1, 2, and 3 respectively.
	"""
	assert Path(dataset).is_dir(), f'{dataset} is not a valid dataset. Show-segmentation does not take videos as input, but datasets geneated through e.g. segmentation.'

	if output is not None:
		assert Path(output).suffix == '.mp4', 'Output must be an mp4 file.'
		assert Path(output).parent.exists(), f'Output directory {Path(output).parent} does not exist.'
		assert not Path(output).exists(), f'Output file {output} already exists.'
	else:
		output = str(Path(dataset).with_suffix(f'.chunk_{chunk}_segmentation_overlay.mp4'))

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

	output_reg = str(Path(output).with_suffix('.registered.mp4'))
	vw_reg = cv2.VideoWriter(output_reg, cv2.VideoWriter_fourcc(*'mp4v'), fps, (chunk.segmentation.shape[2], chunk.segmentation.shape[1]))

	with click.progressbar(range(start, end), label='Generating overlay video', show_percent=True, show_pos=True) as bar:
		for i in bar:
			img = vr.get_batch([i]).asnumpy()[0]
			segmentation = chunk.segmentation.isel(frame=i).data.compute()
			pullback_map = chunk.pullbacks.isel(frame=i).data.compute()

			img = mark_boundaries(img, segmentation==1, color=(1, 0, 0))
			img = mark_boundaries(img, segmentation==2, color=(0, 1, 0))
			img = mark_boundaries(img, segmentation==3, color=(0, 0, 1))

			vw.write((img * 255).astype(np.uint8)[..., ::-1])

			img = warp_frame(img, pullback_map)
			vw_reg.write((img * 255).astype(np.uint8)[..., ::-1])
	vw.release()
	vw_reg.release()
	click.secho(f'\nOverlay video saved to {output}\n')


@error_handler('Test segmentation', cluster=False)
def test_segmentation(video_path: str, model_architecture: str, model_weights: str, frame_idx: int=0, overlay: bool=True):
	""" Test the segmentation model on a single frame.

	Args:
		video_path (str): Path to the video file.
		model_architecture (str): Model architecture.
		model_weights (str): Path to model weights.
		frame_idx (int): Frame index. Default is 0.
		overlay (bool): Overlay the segmentation on the original frame. Default is True.

	Example:
		>>> test_segmentation('video.mp4', 'fcn_resnet50', 'weights.pth', frame_idx=10, overlay=True)

	Notes:
		- Displays the segmentation in an interactive window using matplotlib.
	"""
	model = get_model(model_architecture, num_classes=3, weights=model_weights)
	model.eval()
	model = model.cuda()

	frame = load([frame_idx], video_path)
	prediction = predict(frame, model)[0]

	if not overlay:
		plt.imshow(prediction, cmap=ListedColormap([[126/255, 36/255, 10/255], [255/255, 179/255, 0], [1, 1, 1]]))
	else:
		vr = decord.VideoReader(video_path)
		decord.bridge.set_bridge('native')
		img = vr.get_batch([frame_idx]).asnumpy()[0]
		img = mark_boundaries(img, prediction==1, color=(1, 0, 0))
		img = mark_boundaries(img, prediction==2, color=(0, 1, 0))
		img = mark_boundaries(img, prediction==3, color=(0, 0, 1))
		plt.imshow(img)
	plt.title(f'Segmentation for frame {frame_idx}')
	plt.gca().invert_yaxis()
	plt.gcf().canvas.manager.set_window_title('CHROMAS - Testing Segmentation')
	plt.show()
