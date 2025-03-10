import sys
import click
import dask.array as da
from matplotlib import pyplot as plt
import numpy as np
import torch
from tqdm import tqdm
import xarray as xr
from kornia.contrib import combine_tensor_patches, extract_tensor_patches
import zarr
import time
import os
import shutil
from torchaudio.io import StreamReader
from .neuralnet_utils import get_model
from ..utils.decorators import error_handler


def yuv_to_rgb(yuv_batch: torch.Tensor) -> torch.Tensor:
	yuv_batch = yuv_batch.to(torch.half)
	Y = yuv_batch[..., 0, :, :]
	U = yuv_batch[..., 1, :, :]
	V = yuv_batch[..., 2, :, :]

	Y /= 255
	U = U / 255 - 0.5
	V = V / 255 - 0.5
	R = Y + 1.14 * V
	G = Y - 0.396 * U - 0.581 * V
	B = Y + 2.029 * U

	rgb_batch = (torch.stack([R, G, B], dim=1) * 255).clamp(0, 255)
	return rgb_batch


def extract_pict_config(src):
	r = StreamReader(src)
	video_info = r.get_src_stream_info(0)
	return {
		"height": video_info.height,
		"width": video_info.width,
		"frame_rate": int(video_info.frame_rate),
		"format": video_info.format,
		"num_frames": video_info.num_frames
	}


def segment_chunk_gpu(src, zarr_args, video_length, frames_per_chunk=1, zarr_path="output.zarr", pict_config=None, model=None,
					  debug_args: dict={'debug': False, 'debug_visual': False}):
	r = StreamReader(src)
	r.add_video_stream(frames_per_chunk, decoder='h264_cuvid', decoder_option={}, hw_accel="cuda",
					   buffer_chunk_size=-1)  # IMPORTANT: buffer_chunk_size is 3 by default, which discards the first 3 frames!

	# Create Zarr store compatible with xarray
	zarr_store = zarr.open(
		zarr_path,
		mode='w',
		shape=(0, pict_config['height'], pict_config['width']),
		chunks=(frames_per_chunk, pict_config['height'], pict_config['width']),
		dtype=np.uint8,
		fill_value=None,
	)

	# Add metadata for xarray
	zarr_store.attrs.update({
		"_ARRAY_DIMENSIONS": ("frame", "x", "y"),
		**zarr_args
	})

	mean = torch.tensor([0.485, 0.456, 0.406], device='cuda', dtype=torch.half).view(1, -1, 1, 1)
	std = torch.tensor([0.229, 0.224, 0.225], device='cuda', dtype=torch.half).view(1, -1, 1, 1)

	num_frames = 0
	t0 = time.monotonic()


	for (chunk,) in tqdm(r.stream(), total=video_length//frames_per_chunk, desc='Segmenting', unit='frames', file=sys.stdout):
		num_frames += chunk.shape[0]
		img_size = chunk.shape[1:4]

		if debug_args['debug_visual']:
			# Copy chunk and move to CPU:
			yuv_cpu = chunk[0].to('cpu', non_blocking=True).numpy().astype(np.uint8).transpose(1, 2, 0)
		
		chunk = yuv_to_rgb(chunk)

		if debug_args['debug_visual']:
			rgb_cpu = chunk[0].to('cpu', non_blocking=True).numpy().astype(np.uint8).transpose(1, 2, 0)	
		
		chunk = (chunk / 255 - mean) / std
		
		if debug_args['debug_visual']:
			img_cpu = chunk[0].to('cpu', non_blocking=True).numpy().transpose(1, 2, 0)[..., 0]

		X, DX = 512, 480
		batch = extract_tensor_patches(chunk, X, DX, allow_auto_padding=True)[0]

		with torch.no_grad():
			out = model(batch)['out']

		out = torch.argmax(out, 1).to(torch.uint8)[None, :, None, :, :]
		
		out = combine_tensor_patches(out, img_size[1:], X, DX, allow_auto_unpadding=True).to('cpu', non_blocking=True).numpy()[0]

		zarr_store.append(out)

		if debug_args['debug_visual']:
			pred_cpu = out[0]
			fig, ax = plt.subplots(1, 4, sharex=True, sharey=True)
			ax[0].imshow(yuv_cpu)
			ax[0].set_title('Image read on GPU in YUV format')
			ax[1].imshow(rgb_cpu)
			ax[1].set_title('Converted to RGB')
			ax[2].imshow(img_cpu)
			ax[2].set_title('Normalized and scaled to [0, 1]')
			ax[3].imshow(pred_cpu, cmap='binary')
			ax[3].set_title('Prediction')
			fig.suptitle(f'Frame {num_frames}')
			plt.show()

	r.remove_stream(0)
	del r

	elapsed = time.monotonic() - t0
	fps = num_frames / elapsed
	print(f"Processed {num_frames} frames in {elapsed:.2f} seconds. ({fps:.2f} fps)")


@error_handler('Segmentation (neuralnet-gpu)', cluster=False)
def segmentation(dataset: str,
				 weights: str = '/gpfs/laur/data/renardm/training_data/240823-006/model/fcn_resnet50_100_best_model.pth',
				 num_classes: int = 2,
				 cluster_args: dict = None,
				 debug_args: dict = dict({'debug': False, 'debug_visual': False}),
				 architecture: str = 'fcn_resnet50',
				 ):

	# LOAD MODEL:
	model = get_model(architecture, num_classes=num_classes, weights=weights)
	model.eval()
	model = model.cuda()

	# LOAD CHUNKING DATA:
	chunking_dataset = xr.open_zarr(dataset, group='chunking')

	# SEGMENT CHUNKS:
	with click.progressbar(enumerate(zip(chunking_dataset.chunk_times.compute(), chunking_dataset.chunk_paths.compute())),
						   label='Segment chunks (GPU-enabled)', show_percent=True, show_pos=True) as bar:
		for chunk_idx, (chunk_time, chunk_path) in bar:
			video_file = str(chunk_path.data)

			pict_config = extract_pict_config(video_file)
			click.secho("Video info:", bold=True)
			for k, v in pict_config.items():
				click.secho(f'\t{k}: {v}')

			zarr_args = {
				"chunk_idx": str(chunk_idx),
				"chunk_path": str(video_file),
				"model_architecture": str(architecture),
				"model_weights": str(weights),
			}

			video_length = pict_config['num_frames']

			# Create empty xArray dataset stored in Zarr format:
			segmentation_path = f'{dataset}/chunk_{chunk_idx}/segmentation'
			predictions = xr.DataArray(da.zeros((video_length, pict_config['width'], pict_config['height']),
									   			chunks = (1, pict_config['width'], pict_config['height']),
												dtype=np.uint8),
							  		   dims=['frame', 'x', 'y'],
									   name='segmentation',
									   coords={'frame': np.arange(video_length)},
									   attrs=zarr_args)
			predictions.to_zarr(dataset, group=f'chunk_{chunk_idx}', mode='w')

			# Os remove segmentation_path directory if it exists:
			if os.path.exists(segmentation_path):
				# Remove non-empty directory:
				shutil.rmtree(segmentation_path)
			else:
				raise FileNotFoundError(f"Directory {segmentation_path} does not exist.")

			segment_chunk_gpu(video_file, zarr_args, video_length, zarr_path=segmentation_path, pict_config=pict_config, model=model, debug_args=debug_args)