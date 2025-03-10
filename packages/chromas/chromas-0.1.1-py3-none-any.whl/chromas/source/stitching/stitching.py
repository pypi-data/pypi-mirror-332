import itertools
import click
import cv2
import matplotlib.pyplot as plt
import moving_least_squares
import numpy as np
import scipy.fftpack
import scipy.ndimage
import sklearn.linear_model
import xarray as xr
from tqdm import tqdm
import traceback
from ..stitching.libreg import cross_correlation_fft, match_template_brute
from ..utils.utils import clear_edges, cuttlefish_mask, get_props
from ..utils.decorators import error_handler
from ..stitching.image_point_selector import ImagePointSelector
from ..stitching.minimal_removal import find_minimal_removal_for_no_false

#######################
#### VISUALIZATION ####
#######################
def create_remap_animation(input_image: np.ndarray, final_dest_coords: np.ndarray, output_video_path: str, num_frames: int = 60) -> None:
	"""
	Create a video that gradually transforms the input image using the provided final destination coordinates.

	Parameters:
		input_image (np.ndarray): The input image as a NumPy array.
		final_dest_coords (np.ndarray): The final destination coordinates as a NumPy array.
		output_video_path (str): The file path to save the output video.
		num_frames (int): The number of frames in the animation. Default is 60.

	Returns:
		None
	"""
	assert isinstance(num_frames, int) and num_frames > 0, 'num_frames must be a positive integer.'
	assert isinstance(input_image, np.ndarray), 'input_image must be a NumPy array.'
	assert isinstance(final_dest_coords, np.ndarray), 'final_dest_coords must be a NumPy array.'
	assert isinstance(output_video_path, str), 'output_video_path must be a string.'

	# Generate intermediate destination coordinates
	dest_coords_list = []
	for i in range(num_frames):
		alpha = i / (num_frames - 1)
		dest_coords = final_dest_coords * alpha + (1 - alpha) * np.mgrid[:input_image.shape[0], :input_image.shape[1]].T
		dest_coords_list.append(dest_coords.astype('float32'))	

	# Create a video writer
	output_video = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), 10, (input_image.shape[1], input_image.shape[0]), isColor=False)

	for i, dest_coord in enumerate(dest_coords_list):
		remapped_image = cv2.remap(input_image.astype('float64'), dest_coord, None, cv2.INTER_LINEAR)
		remapped_image /= np.max(remapped_image)
		remapped_image *= 255
		output_video.write(remapped_image.astype('uint8'))
	output_video.release()


########################
#### CHUNKSTITCHING ####
########################
def estimate_affine(src_mask, trg_mask, mode='rotation'):
	'''
	Parameters:
	===========

	mode: rotation, similarity, full
	'''
	if int(cv2.__version__.split('.')[0]) == 3:
		_, src_cont, _ = cv2.findContours(src_mask.astype('uint8'), \
				cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
		_, trg_cont, _ = cv2.findContours(trg_mask.astype('uint8'), \
				cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	else:
		src_cont, _ = cv2.findContours(src_mask.astype('uint8'), \
				cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
		trg_cont, _ = cv2.findContours(trg_mask.astype('uint8'), \
				cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	src_ellipse = cv2.fitEllipse(src_cont[0])
	trg_ellipse = cv2.fitEllipse(trg_cont[0])

	rotation = (src_ellipse[2] - trg_ellipse[2]) / 180. * np.pi + 0.03 * np.pi  # TODO: REMOVE 0.2 * np.pi!!
	if mode == 'rotation':
		scale_x = scale_y = 1
	elif mode == 'similarity':
		scale_x = scale_y = (trg_ellipse[1][0] / src_ellipse[1][0] \
				+ trg_ellipse[1][1] / src_ellipse[1][1]) / 2
	elif mode == 'full':
		scale_x = trg_ellipse[1][0] / src_ellipse[1][0]
		scale_y = trg_ellipse[1][1] / src_ellipse[1][1]
	else:
		raise RuntimeError('mode %s not in ' \
				'[\'rotation\', \'similarity\', \'full\']' % mode)
	shift_src = np.array(src_ellipse[0])      * 1.01  # TODO: Remove * 1.03 
	shift_trg = np.array(trg_ellipse[0])      * 1.01  # TODO: Remove * 1.03 
	
	# Compute transformation matrices
	alpha = np.cos(rotation)
	beta = np.sin(rotation)
	t0 = np.array([[+alpha, +beta,   (1. - alpha) * shift_src[0] \
										   - beta * shift_src[1] \
								   + shift_trg[0] - shift_src[0]], \
				   [-beta, +alpha,           beta * shift_src[0] \
								   + (1. - alpha) * shift_src[1] \
								   + shift_trg[1] - shift_src[1]]], 'float32')

	alpha = scale_x * np.cos(np.pi + rotation)
	beta = scale_y * np.sin(np.pi + rotation)
	t1 = np.array([[+alpha, +beta,   (1. - alpha) * shift_src[0] \
										   - beta * shift_src[1] \
								   + shift_trg[0] - shift_src[0]], \
				   [-beta, +alpha,           beta * shift_src[0] \
								   + (1. - alpha) * shift_src[1] \
								   + shift_trg[1] - shift_src[1]]], 'float32')
	return t0, t1


def warp_image(img, p, q, alpha, grid_size):
	identity_maps = np.dstack(np.meshgrid( \
			*tuple(np.arange(0, s + grid_size, grid_size) \
				  for s in img.shape[1::-1]))).astype('float32')
	coords = identity_maps.reshape((-1, 2))
	mapped_coords = moving_least_squares.similarity(p, q, coords, alpha=alpha)
	maps = mapped_coords.reshape(identity_maps.shape)
	t = np.array([[grid_size, 0, 0], [0, grid_size, 0]], 'float32')
	maps = cv2.warpAffine(maps, t, img.shape[1::-1])
	return cv2.remap(img, maps, None, interpolation=cv2.INTER_LINEAR)


def draw_centers_on_masterframes(mf, mask, threshold=0.5):
	centers = [p['centroid'] for p in get_props(mf, threshold=threshold)]
	
	mf = np.zeros_like(mf)
	for center in centers:
		cv2.circle(mf, (int(center[1]), int(center[0])), 5, 1, -1)
	
	mf[mask == 0] = 0
	return mf


def norm(data):
	with np.errstate(invalid='ignore'):
		return (data - np.mean(data)) / np.std(data)
	

def get_patch_at(img, pos, patch_size):
	x, y = pos
	t = np.array([[1., 0., patch_size - x], \
					[0., 1., patch_size - y]], 'float32')
	patch = cv2.warpAffine(img, t, \
			(int(2 * patch_size + .5), int(2 * patch_size + .5)))
	return norm(patch)


def stitch_chunk2chunk(
		src_mf: np.ndarray, trg_mf: np.ndarray, src_mask: np.ndarray, trg_mask: np.ndarray,
		patch_size: int,
		coarse_scale: int,
		fine_scale: int,
		initial_estimate: str,
		search_space: tuple[tuple[int|None]],
		mls_alpha: float,
		ransac_tolerance: float,
		debug: bool=False,
		debug_visual: bool=False,
		initial_affine_transforms: np.ndarray=None
		) -> np.ndarray:
	
	(shift_space, d_shift), (angle_space, d_angle), (scale_space, d_scale), (shear_space, d_shear) = search_space

	# Coarse grid
	coarse_grid = np.mgrid[tuple(np.s_[: s : coarse_scale] for s in trg_mf.shape)]
	coarse_point_in_mask = trg_mask[coarse_grid[0], coarse_grid[1]]  # boolean
	coarse_trg_coords = np.float32(coarse_grid[:, coarse_point_in_mask].T[:, ::-1])
	
	def coarse_alignment(t_inv):
		t_ide = np.identity(3, 'float32')[: 2]

		coarse_src_coords = cv2.transform(coarse_trg_coords[:, None], t_inv)[:, 0]

		# Transform target for coarse grid search
		shape = tuple(int(s / d_shift) for s in src_mf.shape)
		trg_mf_t = cv2.warpAffine(trg_mf, t_inv / d_shift, shape[::-1])
		src_mf_t = cv2.warpAffine(src_mf, t_ide / d_shift, shape[::-1])

		def match_func(src_coord):
			template = get_patch_at(trg_mf_t, src_coord / d_shift, patch_size / d_shift)
			search_region = get_patch_at(src_mf_t, src_coord / d_shift, shift_space / d_shift)
			img_fft = scipy.fftpack.fft2(search_region)
			t_corr = match_template_brute(
				template, img_fft,
				rotation=slice(0, 1, 1) if angle_space is None else slice(-angle_space, +angle_space, d_angle),
				logscale_x=slice(0, 1, 1) if scale_space is None else slice(-scale_space, +scale_space, d_scale),
				logscale_y=slice(0, 1, 1) if scale_space is None else slice(-scale_space, +scale_space, d_scale),
				shear=slice(0, 1, 1) if shear_space is None else slice(-shear_space, +shear_space, d_shear),
				find_translation=cross_correlation_fft,
				return_rotation_shear=False
				)
			return t_corr

		# Coarse grid search
		t_corr_list = list(map(match_func, tqdm(coarse_src_coords, desc='Matching templates', disable=True)))

		dx = np.array([
			np.dot(t[:, :2], (patch_size / d_shift, patch_size / d_shift)) + t[:, 2] - (shift_space / d_shift, shift_space / d_shift) for t, _ in t_corr_list
			])
		coarse_src_coords_t = coarse_src_coords + dx * d_shift

		corr = np.array([corr for _, corr in t_corr_list], 'float32')

		return coarse_src_coords_t, coarse_src_coords, corr
	
	if initial_affine_transforms is None:	
		# Estimate initial affine transform
		try:
			t0, t1 = estimate_affine(src_mask, trg_mask, mode=initial_estimate)
		except RuntimeError as e:
			click.secho(f'[ERROR] Could not estimate affine transform!\n{e}', fg='red', bold=True)
			return None
		t0_inv = cv2.invertAffineTransform(t0)
		t1_inv = cv2.invertAffineTransform(t1)

		coarse_src_coords_0, coarse_src_coords_t0, coarse_corr_0 = coarse_alignment(t0_inv)
		coarse_src_coords_1, coarse_src_coords_t1, coarse_corr_1 = coarse_alignment(t1_inv)
		
		coarse_src_coords, coarse_corr = (coarse_src_coords_0, coarse_corr_0) if np.nanmean(coarse_corr_0) > np.nanmean(coarse_corr_1) else (coarse_src_coords_1, coarse_corr_1)
	else:
		coarse_src_coords, coarse_src_coords_t, coarse_corr = coarse_alignment(initial_affine_transforms)

	# Filter out points
	coarse_trg_coords_flt, coarse_src_coords_flt, _ = filter_points(ransac_tolerance, coarse_trg_coords, coarse_src_coords, debug=debug)

	# Warp trg_mf with the coarse grid transformation
	trg_mf_warped = warp_image(trg_mf, coarse_src_coords_flt, coarse_trg_coords_flt, mls_alpha, 32)

	# Fine grid
	fine_grid = np.mgrid[tuple(np.s_[: s + fine_scale : fine_scale] for s in trg_mf.shape)]
	fine_point_in_mask = np.zeros(fine_grid.shape[1:], 'bool')
	end_y = fine_grid.shape[1] - 1
	end_x = fine_grid.shape[2] - 1
	fine_point_in_mask[: end_y, : end_x] = trg_mask[fine_grid[0, : end_y, : end_x], fine_grid[1, : end_y, : end_x]]
	fine_coord_in_grid = fine_point_in_mask[np.ones(fine_grid.shape[1:], 'bool')]
	fine_trg_coords = np.ascontiguousarray(fine_grid.reshape((2, -1)).T[:, ::-1], 'float32')
	
	fine_src_coords = moving_least_squares.similarity(coarse_trg_coords_flt, coarse_src_coords_flt, fine_trg_coords, mls_alpha)

	# Estimate new shifts
	def shift_func(src_coord):
		src_patch = get_patch_at(trg_mf_warped, src_coord, patch_size)
		src_fft = scipy.fftpack.fft2(src_patch)
		trg_patch = get_patch_at(src_mf, src_coord, patch_size)
		trg_fft = scipy.fftpack.fft2(trg_patch)
		dx_corr = cross_correlation_fft(src_fft, trg_fft)
		return dx_corr

	dx_corr_list = list(map(shift_func, tqdm(fine_src_coords[fine_coord_in_grid], desc='Shifting patches', disable=True)))

	dx = np.array([dx for dx, _ in dx_corr_list], 'float32')

	fine_src_coords_dx = fine_src_coords.copy()
	fine_src_coords_dx[fine_coord_in_grid] += dx


	# Filter out points
	_, fine_src_coords_dx_flt, good_points = filter_points(ransac_tolerance, fine_trg_coords[fine_coord_in_grid], fine_src_coords_dx[fine_coord_in_grid], debug=debug)
	fine_src_coords_flt = fine_src_coords[fine_coord_in_grid][good_points]


	# Apply fine shifts
	small_map = np.empty(fine_grid.shape[1 : ] + (2, ), 'float32')
	small_map[np.ones(fine_grid.shape[1:], 'bool')] = fine_src_coords
	small_map[fine_point_in_mask].reshape((-1, 2))[good_points] = fine_src_coords_dx_flt

	if debug_visual:
		# Plot four images. 1. trg_mf with coarse_trg_coords in red and coarse_trg_coords_flt in green. 2. src_mf with coarse_src_coords0 3. src_mf with coarse_src_coords1 4. trg_mf_warped with coarse_trg_coords_flt
		fig, ax = plt.subplots(2, 4)
		ax[0, 0].imshow(trg_mf, cmap='binary')
		# Make cross:
		ax[0, 0].scatter(coarse_trg_coords[:, 0], coarse_trg_coords[:, 1], c='r', s=45, marker='+')
		ax[0, 0].scatter(coarse_trg_coords_flt[:, 0], coarse_trg_coords_flt[:, 1], c='g', s=50, marker='+')
		ax[0, 0].set_title('Target masterframe')
		ax[1, 0].imshow(trg_mf_warped, cmap='Wistia')
		ax[1, 0].imshow(src_mf, cmap='binary', alpha=0.5)
		ax[1, 0].set_title(f'Target masterframe (warped with {"t0" if np.nanmean(coarse_corr_0) > np.nanmean(coarse_corr_1) else "t1"})')

		if initial_affine_transforms is None:
			ax[0, 1].imshow(src_mf, cmap='binary')
			ax[0, 1].scatter(coarse_src_coords_t0[:, 0], coarse_src_coords_t0[:, 1], c='r', s=50, marker='+')
			ax[0, 1].set_title('Source masterframe (t0)')
			ax[1, 1].imshow(src_mf, cmap='binary')
			ax[1, 1].scatter(coarse_src_coords_t1[:, 0], coarse_src_coords_t1[:, 1], c='r', s=50, marker='+')
			ax[1, 1].set_title('Source masterframe (t1)')

			ax[0, 2].imshow(src_mf, cmap='binary')
			ax[0, 2].scatter(coarse_src_coords_t0[:, 0], coarse_src_coords_t0[:, 1], c='r', s=50, marker='+', alpha=0.5)
			ax[0, 2].plot([coarse_src_coords_t0[:, 0], coarse_src_coords[:, 0]], [coarse_src_coords_t0[:, 1], coarse_src_coords[:, 1]], 'r-', alpha=0.5)
			ax[0, 2].scatter(coarse_src_coords_0[:, 0], coarse_src_coords_0[:, 1], c='r', s=50, marker='+')
			ax[0, 2].set_title('Source masterframe (t0+dx)')
			ax[1, 2].imshow(src_mf, cmap='binary')
			ax[1, 2].scatter(coarse_src_coords_t1[:, 0], coarse_src_coords_t1[:, 1], c='r', s=50, marker='+', alpha=0.5)
			ax[1, 2].plot([coarse_src_coords_t1[:, 0], coarse_src_coords[:, 0]], [coarse_src_coords_t1[:, 1], coarse_src_coords[:, 1]], 'r-', alpha=0.5)
			ax[1, 2].scatter(coarse_src_coords_1[:, 0], coarse_src_coords_1[:, 1], c='r', s=50, marker='+')
			ax[1, 2].set_title('Source masterframe (t1+dx)')

		ax[0, 3].imshow(src_mf, cmap='binary')
		# Scatter fine_src_coords and fine_src_coords + dx
		ax[0, 3].quiver(fine_src_coords_flt[:, 0], fine_src_coords_flt[:, 1], dx[good_points, 0], dx[good_points, 1], color='r', scale=1, scale_units='xy')
		ax[0, 3].set_title('Source masterframe (fine grid)')

		ax[1, 3].imshow(np.linalg.norm(small_map, axis=-1), cmap='binary')
		ax[1, 3].set_title('Small map')	
		plt.show()

		np.savez('coords.npz', coarse_trg_coords=coarse_trg_coords, coarse_trg_coords_flt=coarse_trg_coords_flt, coarse_src_coords=coarse_src_coords, coarse_src_coords_flt=coarse_src_coords_flt, fine_trg_coords=fine_trg_coords,
		   					   fine_src_coords=fine_src_coords, fine_src_coords_dx=fine_src_coords_dx, fine_src_coords_flt=fine_src_coords_flt, small_map=small_map,
							   coarse_corr_0=coarse_corr_0, coarse_corr_1=coarse_corr_1, fine_src_coords_dx_flt=fine_src_coords_dx_flt, fine_coord_in_grid=fine_coord_in_grid,
							   coarse_src_coords_0=coarse_src_coords_0, coarse_src_coords_1=coarse_src_coords_1,
							   coarse_src_coords_t0=coarse_src_coords_t0, coarse_src_coords_t1=coarse_src_coords_t1, trg_mf_warped=trg_mf_warped,
							   trg_mf=trg_mf, src_mf=src_mf, src_mask=src_mask, trg_mask=trg_mask)
		exit()
							  
			
	return small_map


def filter_points(ransac_tolerance: float, coarse_trg_coords: np.ndarray, coarse_src_coords: np.ndarray, loss: str='squared_error', debug: bool=False) -> tuple[np.ndarray]:
	for _ in range(8):
		median_absolute_deviation = np.median(np.abs(coarse_src_coords - np.median(coarse_src_coords)))
		affine_model = sklearn.linear_model.RANSACRegressor(
			sklearn.linear_model.LinearRegression(), max_trials=2048, residual_threshold = ransac_tolerance*median_absolute_deviation, loss=loss
			)
		try:
			affine_model.fit(coarse_trg_coords, coarse_src_coords)
		except ValueError:
			continue
		else:
			break
	else:
		raise RuntimeError('RANSAC did not converge.')
	
	coarse_trg_coords_flt = np.ascontiguousarray(coarse_trg_coords[affine_model.inlier_mask_], 'float32')
	coarse_src_coords_flt = np.ascontiguousarray(coarse_src_coords[affine_model.inlier_mask_], 'float32')

	if debug:
		click.secho(f'[DEBUG] Number of inliers: {np.sum(affine_model.inlier_mask_)}/{len(affine_model.inlier_mask_)} ({100 * np.mean(affine_model.inlier_mask_):.2f}%)', fg='yellow')
	return coarse_trg_coords_flt, coarse_src_coords_flt, affine_model.inlier_mask_


def chunkstitching(mfs: np.ndarray, masks: np.ndarray, trg_chunk_idx: int,
				   patch_size: int=64,
				   grid_size: int=32,
				   coarse_grid_size: int=128,
				   initial_estimate: str='rotation',
				   mls_alpha: float=6,
				   ransac_tolerance: float=1,
				   search_space: tuple[tuple[int|None]]= ((512, 2), (0.35, 0.035), (None, None), (None, None)),
				   debug: bool=False,
				   debug_visual: bool=False,
				   initial_affine_transforms: np.ndarray=None) -> np.ndarray:
	
	height, width = mfs[trg_chunk_idx].shape
	trg_mask = masks[trg_chunk_idx]

	def func(source_chunk_idx: int):
		try:
			if(source_chunk_idx == trg_chunk_idx):
				small_map = np.nan
			else:
				small_map = stitch_chunk2chunk(
					mfs[source_chunk_idx], mfs[trg_chunk_idx],
					masks[source_chunk_idx], trg_mask,
					patch_size=patch_size,
					fine_scale=grid_size,
					coarse_scale=coarse_grid_size,
					initial_estimate=initial_estimate,
					search_space=search_space,
					mls_alpha=mls_alpha,
					ransac_tolerance=ransac_tolerance,
					debug=debug,
					debug_visual=debug_visual,
					initial_affine_transforms=initial_affine_transforms[trg_chunk_idx, source_chunk_idx] if initial_affine_transforms is not None else None,
					)
		except Exception as error:
			traceback.print_exc()
			click.secho(f'[ERROR] Stitching chunk {source_chunk_idx} into {trg_chunk_idx} failed!\n{error}', fg='red', bold=True)
			return np.nan, error
		return small_map, None

	stitching_mat_shape = (len(mfs), (height + 2 * grid_size - 1) // grid_size, (width  + 2 * grid_size - 1) // grid_size, 2)
	stitching_mat = np.empty(stitching_mat_shape, 'float32')

	for src_idx in tqdm(range(len(mfs)), total=len(mfs), desc='Stitching'):
		if debug:
			click.secho(f'[DEBUG] Stitching chunk {src_idx} into {trg_chunk_idx}', fg='yellow')
		small_map, error = func(src_idx)
		if error is not None:
			click.secho(f'[ERROR] Stitching chunk {src_idx} into {trg_chunk_idx} failed!\n{error}', fg='red', bold=True)
		stitching_mat[src_idx] = small_map

	if debug_visual:
		grow_t = np.array([[grid_size, 0., 0.], [0., grid_size, 0.]], 'float32')
		fig, ax = plt.subplots(1, len(mfs))
		for i, small_map in enumerate(stitching_mat):
			if i == trg_chunk_idx:
				ax[i].imshow(mfs[i], cmap='Wistia')
			else:
				maps = cv2.warpAffine(small_map, grow_t, mfs[0].shape[::-1])
				src_mf_warped = cv2.remap(mfs[i].astype('float64'), maps, None, interpolation=cv2.INTER_LINEAR).astype('float32')
				ax[i].imshow(mfs[trg_chunk_idx], cmap='Wistia')
				ax[i].imshow(src_mf_warped, cmap='binary', alpha=0.5)
			ax[i].axis('off')
			ax[i].set_title(f'Chunk {i}')
		plt.suptitle(f'Stitching into chunk {trg_chunk_idx}')
		plt.show()

	return stitching_mat


###################
#### STITCHING ####
###################
def get_reprojection(smat: np.ndarray, masks: np.ndarray, grid_size: int, dist_thresh: float=3) -> np.ndarray:
	n_chunks = len(masks)

	shrink_t = np.array([[1. / grid_size, 0., 0.],
						 [0., 1. / grid_size, 0.]], 'float32')

	small_masks = []
	for mask in masks:
		small_mask_padded = np.zeros(smat.shape[2:-1],dtype='bool')
		actual_h, actual_w = np.array(mask.shape) // grid_size + 1
		small_mask = cv2.warpAffine(mask.astype('uint8'), shrink_t, (actual_w, actual_h)).astype('bool')
		
		small_mask_padded[:actual_h, :actual_w] = small_mask
		small_masks.append(small_mask_padded)

	# Generate back forth mapping
	reprojection = np.zeros(smat.shape, 'float32')
	for i, j in tqdm(itertools.product(list(range(n_chunks)), list(range(n_chunks))), total=int(n_chunks ** 2), desc='Scoring mappings ...'):
		reprojection[i, j] = cv2.remap(smat[i, j], smat[j,i] / grid_size, None, interpolation=cv2.INTER_LINEAR)
		reprojection[i, j, ..., 1] -= grid_size * np.arange(reprojection.shape[2])[:, None]
		reprojection[i, j, ..., 0] -= grid_size * np.arange(reprojection.shape[3])[None, :]
		reprojection[i, j, ~small_masks[i]] = np.nan

	reprojection_error = np.linalg.norm(reprojection, axis=-1)
	with np.errstate(invalid='ignore'):
		good_size = np.sum(reprojection_error <= dist_thresh, axis=(2,3))
	mask_size = np.sum(np.isfinite(reprojection_error), axis=(2,3))
	return good_size / np.float32(mask_size)

# MAIN FUNCTION:
@error_handler('Stitching', cluster=False)
def stitching(dataset: str,
			  grid_size: int = 32,
			  patch_size: int = 64,
			  coarse_grid_size: int = 128,
			  initial_estimate: str = 'rotation',
			  search_space: str = '512;2,0.35;0.035,None;None,None;None',
			  clear_edge: int = 40,
			  center_threshold: float = 0.5,
			  mask_inner: bool = False,
			  mask_dilation_iterations: int = 5,
			  mls_alpha: float = 6,
			  ransac_tolerance: float = 1,
			  manual: bool=False,
			  tutorial: bool=False,
			  debug_args: dict={'debug': False, 'debug_visual': False}) -> None:
	# Load data:
	n_chunks = xr.open_zarr(dataset, group='chunking').sizes['chunk']
	mfs = [xr.open_zarr(dataset, group=f'chunk_{i}').masterframe.data.compute() for i in range(n_chunks)]

	if 'chunkaverage' in xr.open_zarr(dataset, group='chunk_0'):
		images = [xr.open_zarr(dataset, group=f'chunk_{i}').chunkaverage.data.compute() for i in range(n_chunks)]
	else:
		images = [np.stack(((mf > 0.5) * 255).astype('uint8'), axis=-1) for mf in mfs]

	# Load masks:
	if manual:
		click.secho('[WARNING] no-mask enabled. Using full masterframes.', fg='yellow')
		masks = [np.ones_like(mf, 'bool') for mf in mfs]
	else:
		masks = [cuttlefish_mask(mf.copy(), mask_inner, mask_dilation_iterations, debug_args) for mf in mfs]
	mfs_points = [draw_centers_on_masterframes(mf.copy(), mask.copy(), center_threshold) for mf, mask in zip(mfs, masks)]
	
	# Stitching is only necessary if there are more than one chunk:
	if n_chunks > 1:
		search_space = tuple(tuple(map(lambda x: None if x == 'None' else float(x), s.split(';'))) for s in search_space.split(','))
		click.secho(f'[INFO] Search space: {search_space}', fg='green')

		if debug_args['debug_visual']:
			fig, ax = plt.subplots(3, n_chunks)
			for chunk_idx, (mf, mask, mfp) in enumerate(zip(mfs, masks, mfs_points)):
				ax[0, chunk_idx].imshow(mf, cmap='binary')
				ax[0, chunk_idx].axis('off')
				ax[0, chunk_idx].set_title(f'Chunk {chunk_idx}')
				ax[1, chunk_idx].imshow(mask, cmap='binary')
				ax[1, chunk_idx].axis('off')
				ax[2, chunk_idx].imshow(mfp, cmap='binary')
				ax[2, chunk_idx].axis('off')
			fig.suptitle('Masterframes & masks to stitch')
			plt.show()

		if manual:
			initial_affine_transforms = np.zeros((n_chunks, n_chunks, 2, 3), 'float32')
			# Itertools pick all combinations of two chunks
			for i, j in itertools.combinations(range(n_chunks), 2):
				if tutorial:
					hints = np.load('tutorials/image_points_hints.npz')[f'{i}_{j}']
					selector = ImagePointSelector(images[i], images[j], hints=hints)
				else:
					selector = ImagePointSelector(images[i], images[j])
				selector.get_point_pairs()

				# Estimate transformations from image1 to image2 and vice versa
				transformation_matrix_i2j, transformation_matrix_j2i = selector.estimate_transformations()
				selector.plot_transformed_images(transformation_matrix_i2j, transformation_matrix_j2i)

				initial_affine_transforms[i, j] = transformation_matrix_i2j
				initial_affine_transforms[j, i] = transformation_matrix_j2i

		else:
			initial_affine_transforms = None

		stitching_matrix = []
		for trg_chunk_idx in range(n_chunks):
			smat = chunkstitching(mfs_points, masks, trg_chunk_idx, patch_size, grid_size, coarse_grid_size, initial_estimate,
								mls_alpha, ransac_tolerance, search_space, debug_args['debug'], debug_args['debug_visual'], initial_affine_transforms)
			stitching_matrix.append(smat)
		stitching_matrix = np.array(stitching_matrix)
		if debug_args['debug']:
			click.secho(f'[DEBUG] {stitching_matrix.shape=}', fg='yellow')

		reprojection_matrix = get_reprojection(stitching_matrix, masks, grid_size)
		ref_chunk = np.argmax(np.mean(reprojection_matrix, axis=0))
		click.secho(f'[INFO] Reference chunk: {ref_chunk}', fg='green')

		queenframe = mfs[ref_chunk].copy()
		for chunk_idx, mf in enumerate(mfs):
			if chunk_idx == ref_chunk:
				continue
			grow_t = np.array([[grid_size, 0., 0.], [0., grid_size, 0.]], 'float32')
			maps = cv2.warpAffine(stitching_matrix[ref_chunk, chunk_idx], grow_t, mfs[0].shape[::-1])
			warped_masterframe = cv2.remap(mfs[chunk_idx].astype('float64'), maps, None, interpolation=cv2.INTER_LINEAR).astype('float32')
			queenframe += warped_masterframe

			if debug_args['debug_visual']:
				fig, ax = plt.subplots(1, 2)
				ax[0].imshow(mfs[ref_chunk], cmap='binary')
				ax[0].imshow(warped_masterframe, cmap='binary', alpha=0.5)
				ax[0].axis('off')
				ax[0].set_title(f'Chunk {chunk_idx} warped into chunk {ref_chunk}')
				ax[1].imshow(queenframe, cmap='binary')
				ax[1].axis('off')
				ax[1].set_title('Queenframe')
				plt.show()

		queenframe = clear_edges(queenframe, clear_edge) / n_chunks
		
		stitching_matrix = xr.DataArray(stitching_matrix, dims=['src_chunk', 'trg_chunk', 'x_small', 'y_small', 'coord'], name='stitching_matrix',
							coords={'src_chunk': np.arange(len(mfs)), 'trg_chunk': np.arange(len(mfs))},
							attrs={'grid_size': grid_size, 'ref_chunk': ref_chunk})
		reps = xr.DataArray(reprojection_matrix, dims=['src_chunk', 'trg_chunk'], name='reprojection_error')
	else:
		queenframe = clear_edges(mfs[0], clear_edge)

	# Save data:
	queenframe = xr.DataArray(queenframe, dims=['x', 'y'], name='queenframe')
	queenframe.to_zarr(dataset, group='stitching', mode='a')

	if n_chunks > 1:
		stitching_matrix.to_zarr(dataset, group='stitching', mode='a')
		reps.to_zarr(dataset, group='stitching', mode='a')



@error_handler('Redo queenframe', cluster=False)
def redo_queenframe(dataset: str,
					clear_edge: int = 40,
					min_reprojection: float = 0.5,
			  		debug_args: dict={'debug': False, 'debug_visual': True}) -> None:
	# Load data:
	n_chunks = xr.open_zarr(dataset, group='chunking').sizes['chunk']
	if n_chunks < 2:
		return
	
	mfs = [xr.open_zarr(dataset, group=f'chunk_{i}').masterframe.data.compute() for i in range(n_chunks)]

	stitching = xr.open_zarr(dataset, 'stitching')
	reprojection_matrix = stitching.reprojection_error.data.compute()
	ref_chunk = stitching.stitching_matrix.attrs['ref_chunk']
	grid_size = stitching.stitching_matrix.attrs['grid_size']
	stitching_matrix = stitching.stitching_matrix.data.compute()
	
	click.secho(f'[INFO] Reference chunk: {ref_chunk}', fg='green')

	np.fill_diagonal(reprojection_matrix, 1.0)

	valid_reprojection = reprojection_matrix > min_reprojection

	_, chunk_idxs, chunk_mask = find_minimal_removal_for_no_false(valid_reprojection)
	print(f'{chunk_idxs=}\n\n{chunk_mask=}, {chunk_mask.dtype=}')

	if ref_chunk not in chunk_idxs:
		click.secho(f'[WARNING] Reference chunk {ref_chunk} is not in the set of good chunks: {list(chunk_idxs)}!', bold=True, fg='yellow')
		ref_chunk = chunk_idxs[0]

	queenframe = mfs[ref_chunk].copy()
	for chunk_idx, mf in zip(chunk_idxs, [mfs[c] for c in chunk_idxs]):
		if chunk_idx == ref_chunk:
			continue
		grow_t = np.array([[grid_size, 0., 0.], [0., grid_size, 0.]], 'float32')
		maps = cv2.warpAffine(stitching_matrix[ref_chunk, chunk_idx], grow_t, mfs[0].shape[::-1])
		warped_masterframe = cv2.remap(mf.astype('float64'), maps, None, interpolation=cv2.INTER_LINEAR).astype('float32')
		queenframe += warped_masterframe

		if debug_args['debug_visual']:
			fig, ax = plt.subplots(1, 2)
			ax[0].imshow(mfs[ref_chunk], cmap='binary')
			ax[0].imshow(warped_masterframe, cmap='binary', alpha=0.5)
			ax[0].axis('off')
			ax[0].set_title(f'Chunk {chunk_idx} warped into chunk {ref_chunk}')
			ax[1].imshow(queenframe, cmap='binary')
			ax[1].axis('off')
			ax[1].set_title('Queenframe')
			plt.show()

	queenframe = clear_edges(queenframe, clear_edge) / len(chunk_idxs)

	queenframe = xr.DataArray(queenframe, dims=['x', 'y'], name='queenframe')
	queenframe.to_zarr(dataset, group='stitching', mode='a')
	xr.DataArray(chunk_mask, dims='chunk', name='chunk_mask').to_zarr(dataset, group='stitching', mode='a')

########################################################################################################!
###################### VISUALIZATION ###################################################################!
########################################################################################################!
def show_queenframe(datagroup: str, peaks: bool=False) -> None:
	data = xr.open_zarr(datagroup, group='stitching')
	if peaks:
		qf = data.queenframe.data.compute()
		df = np.stack((qf,) * 3, -1)
		df[qf == 1] = [1, 0, 0]
		plt.imshow(df)
	else:
		data.queenframe.plot.imshow(yincrease=False, cmap='binary')
	plt.title('Queenframe')
	plt.show()


def plot_matrix(matrix):
	"""
	Plots a square (or rectangular) matrix in 2D with each cell ("superpixel") colored
	according to its value, and the numeric value written on top in white.
	The axes are labeled from 0 to n-1, where n is the dimension of the matrix.
	
	Parameters
	----------
	matrix : 2D array-like
		The matrix to be plotted.
	"""
	matrix = np.array(matrix)  # Ensure we have a NumPy array
	
	# Create a figure and an axis
	fig, ax = plt.subplots()
	
	# Plot the matrix using imshow. You can choose a different cmap if desired.
	# 'origin="upper"' ensures the top row of the array is at the top of the plot.
	cax = ax.imshow(matrix, cmap='RdYlGn', origin='upper', vmin=0, vmax=1)
	
	# Add text annotations for each cell
	rows, cols = matrix.shape
	for i in range(rows):
		for j in range(cols):
			# Format the value to a short string, or just str(matrix[i,j]) if you like
			ax.text(j, i, f"{round(100*matrix[i,j])}%", 
					ha="center", va="center", color="black", fontsize=9,
					)
	
	# Set up the ticks and tick labels
	ax.set_xticks(np.arange(cols))
	ax.set_yticks(np.arange(rows))
	ax.set_xticklabels(np.arange(cols))
	ax.set_yticklabels(np.arange(rows))

	ax.set_xlabel('Chunk')
	ax.set_ylabel('Chunk')
	
	# Optionally place a colorbar to the right
	plt.colorbar(cax, ax=ax)
	
	# Show the final plot
	plt.show()


def show_reprojection_error(datagroup: str) -> None:
	data = xr.open_zarr(datagroup, group='stitching')

	r_error = data.reprojection_error.data.compute()

	plot_matrix(r_error)


