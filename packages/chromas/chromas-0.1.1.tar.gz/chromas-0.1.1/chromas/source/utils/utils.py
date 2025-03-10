""" Utility functions. """

import numpy as np
import scipy.ndimage
import moving_least_squares
import skimage.segmentation
import skimage.measure
import skimage.morphology
from collections import namedtuple
from scipy.interpolate import griddata
from tqdm import tqdm
import skimage.feature
import itertools
from skimage import transform
from typing import Optional, List
import logging as log
import cv2
import matplotlib.pyplot as plt
import skimage.measure
import sklearn.neighbors



Coords = namedtuple('Coordinates', ['x', 'y'])

def clear_edges(x: np.ndarray, clear_edge: int=40) -> np.ndarray:
	x[:clear_edge] = 0
	x[-clear_edge:] = 0
	x[:, :clear_edge] = 0
	x[:, -clear_edge:] = 0
	return x


def interpolate_coordinate_mapping(x, x_sample, y_sample):
	assert x_sample.shape == y_sample.shape, 'x_sample and y_sample must have the same shape.'

	return moving_least_squares.similarity(y_sample.astype(np.float32), x_sample.astype(np.float32), x.astype(np.float32))


def compute_queenframe(target_masterframe: np.ndarray, source_masterframes: list[np.ndarray], coord_maps: list[np.ndarray], **kwargs) -> np.ndarray:
	assert len(source_masterframes) == len(coord_maps) and len(source_masterframes) > 0, 'The same amount of source_masterframes and coord_maps must be povided and at least one.'
	assert all([source_masterframe.shape == target_masterframe.shape for source_masterframe in source_masterframes]), 'All source_masterframes must have the same shape as the target_masterframe.'
	assert all([coord_map.shape == ((2,) + target_masterframe.shape) for coord_map in coord_maps]), f'All coord_maps must have the same shape (2, w, h), if target_masterframe has shape (w, h).'
	
	queenframe = target_masterframe.astype(float)
	for source_masterframe, coord_map in zip(source_masterframes, coord_maps):
		queenframe += scipy.ndimage.map_coordinates(source_masterframe, coord_map, **kwargs)
	return queenframe


def rotate_and_scale_coordinates(coordinates, angle_deg, scale_factor):
	center_x = coordinates[:, 0].mean()
	center_y = coordinates[:, 1].mean()
	translated_coordinates = coordinates - [center_x, center_y]

	angle_rad = np.deg2rad(angle_deg)
	rotated_scaled_coordinates = np.dot(translated_coordinates, np.array([[np.cos(angle_rad), -np.sin(angle_rad)],
																		  [np.sin(angle_rad), np.cos(angle_rad)]]))
	rotated_scaled_coordinates *= scale_factor
	rotated_scaled_coordinates += [center_x, center_y]

	return rotated_scaled_coordinates


def create_circular_mask(shape, center=None, radius=None):
	"""
	Create a circular mask with the given shape, center, and radius.
	
	Parameters:
	shape (tuple): Shape of the output mask (height, width).
	center (tuple, optional): Coordinates of the circle's center (y, x).
	radius (float, optional): Radius of the circle.
	
	Returns:
	np.ndarray: Boolean mask with the same shape as the input, where True represents the circle.
	"""
	h, w = shape[:2]
	if center is None:  # use the middle of the image
		center = (int(w / 2), int(h / 2))
	if radius is None:  # use the smallest distance between the center and image walls
		radius = min(center[0], center[1], w - center[0], h - center[1])

	Y, X = np.ogrid[:h, :w]
	dist_from_center = np.sqrt((X - center[0])**2 + (Y - center[1])**2)

	mask = dist_from_center <= radius
	return mask

# Function to apply the warp based on point correspondences
def apply_warp(image, points_src, points_dst):
	h, w = image.shape
	grid_x, grid_y = np.meshgrid(np.arange(w), np.arange(h))
	grid_z = np.vstack((grid_x.flatten(), grid_y.flatten())).T

	# Interpolate the warping map
	map_x = griddata(points_dst, points_src[:, 0], grid_z, method='cubic').reshape((h, w))
	map_y = griddata(points_dst, points_src[:, 1], grid_z, method='cubic').reshape((h, w))

	# Warp the image
	warped_image = transform.warp(image, np.array([map_y, map_x]), mode='edge')
	return warped_image

def apply_non_rigid_warp(image, mask, points_src, points_dst):
	image_coords = np.moveaxis(np.indices(image.shape[:2]), 0, -1).reshape(-1, 2)
	# Take only these image coordinates where the mask is True:
	image_coords = image_coords[mask.flatten('C')]

	# Swicth (x, y) to (y, x) for the points_src and points_dst:
	points_src = np.flip(points_src, axis=1)
	points_dst = np.flip(points_dst, axis=1)
	mask_coords_warped = interpolate_coordinate_mapping(image_coords, points_src, points_dst)

	#  Add coordinates back where mask is false, use dummy (0, 0) coordinates:
	image_coords_warped = np.zeros((image.shape[0] * image.shape[1], 2))
	image_coords_warped[mask.flatten('C')] = mask_coords_warped

	# Transform image_coords_warped from (w*h, 2) to (2, w, h):
	image_coords_warped = np.moveaxis(image_coords_warped.reshape(*image.shape[:2], 2), -1, 0)
	image_warped = scipy.ndimage.map_coordinates(image, image_coords_warped, order=1, mode='constant', cval=0.0)
	return image_warped, image_coords_warped, mask_coords_warped

def get_square_cutout(array, center, radius):
	"""
	Extract a square cutout from a 2D or 3D array centered at the specified coordinates.

	Parameters:
	- array (np.ndarray): Input 2D or 3D array.
	- center (tuple): Center coordinates (row, col) for 2D or (row, col, depth) for 3D array.
	- radius (int): Radius to define the size of the square cutout.

	Returns:
	- np.ndarray: Cutout of the input array.
	"""
	row, col = center
	row_min = int(max(row - radius, 0))
	row_max = int(min(row + radius + 1, array.shape[0]))
	col_min = int(max(col - radius, 0))
	col_max = int(min(col + radius + 1, array.shape[1]))
	cutout = array[row_min:row_max, col_min:col_max]
	return cutout


def nonrigid_gridbased_registration(start_image: np.ndarray, target_image: np.ndarray, grid_size: int, mask: np.ndarray=None, desc: str='Match templates'):
	assert start_image.shape == target_image.shape, 'Start image and target image must have the same shape'
	assert isinstance(grid_size, int) and grid_size > 0, 'Grid size must be a positive integer'
	assert mask is None or mask.shape == start_image.shape, 'Mask must have the same shape as the input images'

	shape = Coords(*start_image.shape)

	gridpoints = np.array(list(itertools.product(range(grid_size, shape.x+1, grid_size), range(grid_size, shape.y+1, grid_size))))
	if mask is not None:
		gridpoints = np.array([gp for gp in gridpoints if mask[*gp]])
	target_padded = np.pad(target_image, ((grid_size, grid_size), (grid_size, grid_size)), mode='constant', constant_values=0)

	dys = np.zeros_like(gridpoints)
	for i, gp in tqdm(enumerate(gridpoints), total=len(gridpoints), desc=desc):
		template = start_image[gp[0]-grid_size:gp[0]+grid_size, gp[1]-grid_size:gp[1]+grid_size]
		search_area = target_padded[gp[0]-grid_size:gp[0]+3*grid_size, gp[1]-grid_size:gp[1]+3*grid_size]

		m = skimage.feature.match_template(search_area, template)
		dys[i] = np.unravel_index(np.argmax(m, axis=None), m.shape) - np.array(search_area.shape[0]//2) + np.array(template.shape[0]//2)
	
	image_coords = np.moveaxis(np.indices((shape)), 0, -1).reshape(-1, 2)
	image_coords_warped = interpolate_coordinate_mapping(image_coords, gridpoints, gridpoints+dys).reshape(shape.x, shape.y, 2)
	# Transform image_coords_warped from (w*h, 2) to (2, w, h):
	image_coords_warped = np.moveaxis(image_coords_warped, -1, 0)
	transformed = scipy.ndimage.map_coordinates(start_image, image_coords_warped, order=1, mode='constant', cval=0.0)
	assert transformed.shape == start_image.shape
	return transformed, image_coords_warped, gridpoints, gridpoints+dys


def compose_image_maps(*coords_list):
	"""
	Compose a series of image maps (coordinates).

	Parameters:
	- coords_list (tuple of np.ndarray): List of coordinates mappings, each of shape (2, w, h).

	Returns:
	- composed_coords (np.ndarray): Composed coordinates mapping of shape (2, w, h).
	"""
	if len(coords_list) < 2:
		raise ValueError("At least two coordinate maps are required for composition.")

	# Initialize the composed coordinates with the first map
	composed_coords = coords_list[0]

	# Iterate over each subsequent map in the list
	for next_coords in coords_list[1:]:
		if composed_coords.shape != next_coords.shape:
			raise ValueError("All coordinate maps must have the same shape.")

		new_composed_coords = np.zeros_like(composed_coords)

		# Apply the current composed coordinates to the next coordinates
		for i in range(2):  # Iterate over the x and y coordinates
			new_composed_coords[i] = scipy.ndimage.map_coordinates(next_coords[i], composed_coords, order=1, mode='nearest')

		composed_coords = new_composed_coords

	return composed_coords


map_coordinates = lambda image, coords: scipy.ndimage.map_coordinates(image, coords, order=1, mode='constant', cval=0.0)


def custom_loss(y_true, y_pred, alpha):
	return 0


#####################
#### COMPUTATION ####
#####################

def cuttlefish_mask(masterframe: np.ndarray, inner: bool=False, dilation_iterations: int=5,
					debug_args: dict={'debug': False, 'debug_visual': False}) -> np.ndarray:
	""" Generates a mask for the cuttlefish in the masterframe. """
	# Remove noise:
	masterframe_norm = masterframe / np.max(masterframe)
	masterframe[masterframe_norm < 0.75] = 0
	# Dilation
	kernel = np.ones((10, 10), np.uint8)
	try:
		dilation = cv2.dilate(masterframe, kernel, iterations=dilation_iterations)
	except cv2.error as e:
		raise ValueError(f'Error in cv2.dilate: {e}. {masterframe.shape=}, {kernel.shape=}, {dilation_iterations=}, {masterframe.dtype=}, {masterframe.max()=}, {masterframe.min()=}')
	# Fill holes
	fill = scipy.ndimage.binary_fill_holes(dilation)
	# Take largest connected component
	labels = skimage.measure.label(fill)
	mask = labels == np.argmax(np.bincount(labels.flat)[1:])+1
	if not inner:
		# Dilation
		mask = cv2.dilate(mask.astype('uint8'), kernel, iterations=1)
	else:
		# Erosion
		mask = cv2.erode(mask.astype('uint8'), kernel, iterations=12)
	if debug_args['debug_visual']:
		fig, ax = plt.subplots(1, 5, figsize=(25, 5))
		ax[0].imshow(masterframe, cmap='gray')
		ax[0].set_title('Masterframe >= 75%')
		ax[1].imshow(dilation, cmap='gray')
		ax[1].set_title('Dilation')
		ax[2].imshow(fill, cmap='gray')
		ax[2].set_title('Fill holes')
		ax[3].imshow(mask, cmap='gray')
		ax[3].set_title('Largest connected component')
		ax[4].imshow(mask, cmap='gray')
		ax[4].set_title(f'Final mask after {"dilation" if not inner else "erosion"}')
		plt.show()
	return mask.astype(bool)

def get_props(masterframe: np.ndarray, threshold: float = 0.0,
			  path: Optional[str] = None, iteration: int = 0, inner: bool = False, visual: bool = False) -> List['RegionProperties']:
	"""
	Returns the properties, such as size, circularity or maximum diameter, of the chromatophores in the (master)frame.

	Args:
		masterframe_probs (np.ndarray): The masterframe probabilities.
		chunkaverage (Optional[np.ndarray], optional): The chunk average. Defaults to None.
		threshold (float, optional): The threshold for segmentation. Defaults to 0.0.
		path (Optional[str], optional): The path to save visualizations. Defaults to None.
		iteration (int, optional): The current iteration. Defaults to 0.
		inner (bool, optional): Whether to use inner mask. Defaults to False.
		visual (bool, optional): Whether to visualize the results. Defaults to False.

	Returns:
		List['RegionProperties']: List of region properties.

	Raises:
		AssertionError: If the input values are not in the expected range.
	"""
	masterframe = (masterframe.astype(float) / masterframe.max())

	assert (threshold >= 0.0) and (threshold <= 1.0), 'Threshold should be in [0, 1]'
	if threshold > 1 - 1/2**6:
		threshold = 1 # To prevent infinite runtime in 'turtle' style.

	skinny_masterframe = masterframe >= threshold
	
	labeled_image, _ = skimage.measure.label(skinny_masterframe, return_num=True, connectivity=1)
	masterframe[~skinny_masterframe] = 0

	if (masterframe == 0).all():
		return []
	
	props = skimage.measure.regionprops(labeled_image, masterframe)
	centers, coords, bboxes, labels, convex_areas, areas = [], [], [], [], [], []
	for prop in props:
		centers.append(prop.centroid)
		bboxes.append(prop.bbox)
		labels.append(prop.label)
		coords.append(prop.coords)
		convex_areas.append(prop.convex_area)
		areas.append(prop.area)

	densities = [area / convex_area for area, convex_area in zip(areas, convex_areas)]
	singular_labels = [label for label, density in zip(labels, densities) if density > 0.95]
	singular_props = [prop for prop, density in zip(props, densities) if density > 0.95]

	if path or visual:
		fig = plt.figure(figsize=(10, 10))
		plt.imshow(masterframe, cmap='gray')
		plt.scatter(np.array(centers)[:, 1], np.array(centers)[:, 0], s=1)
		plt.axis('off')
		plt.tight_layout()
		plt.gca().invert_yaxis()
		# Plot bounding boxes:
		for bbox in bboxes:
			plt.plot([bbox[1], bbox[1]], [bbox[0], bbox[2]], color='red')
			plt.plot([bbox[1], bbox[3]], [bbox[2], bbox[2]], color='red')
			plt.plot([bbox[3], bbox[3]], [bbox[2], bbox[0]], color='red')
			plt.plot([bbox[3], bbox[1]], [bbox[0], bbox[0]], color='red')
		plt.title(f'Chromatophores in masterframe (threshold: {threshold})')
		plt.savefig(f'{path}_get_centers_{iteration}.png') if path else plt.show()

	iteration += 1
	masterframe[np.isin(labeled_image, singular_labels)] = 0

	if threshold < 0.6:
		threshold += 0.05
	elif threshold < 0.95: # was 0.95
		threshold += 0.02
	elif threshold < 1:
		threshold = 1
	else:
		return props
	return get_props(masterframe, threshold, path, iteration, visual=visual) + singular_props


def calc_mapping(p: np.ndarray, q: np.ndarray, alpha: float, grid_size: int, shape: 'tuple[int]') -> np.ndarray:
	""" Calculates the mapping from p to q using moving least squares. """
	identity_maps = np.dstack(np.meshgrid(
			*tuple(np.arange(0, s + grid_size, grid_size)
				  for s in shape))).astype('float32')
	coords = identity_maps.reshape((-1, 2))
	mapped_coords = moving_least_squares.similarity(p.astype('float32'), q.astype('float32'), coords, alpha=alpha)
	maps = mapped_coords.reshape(identity_maps.shape)
	t = np.array([[grid_size, 0, 0], [0, grid_size, 0]], 'float32')
	maps = cv2.warpAffine(maps, t, shape)
	return maps


def warp_image(img: np.ndarray, p: np.ndarray=None, q: np.ndarray=None, alpha: float=None, grid_size: int=None, maps: np.ndarray=None) -> np.ndarray:
	""" Warps an image using moving least squares. """
	if maps is None and (p is None or q is None or alpha is None or grid_size is None):
		raise ValueError('Either `maps` or `p`, `q`, `alpha` and `grid_size` should be given.')
	elif maps is None:
		maps = calc_mapping(p, q, alpha, grid_size, img.shape[1::-1])
	return cv2.remap(img, maps, None, interpolation=cv2.INTER_LINEAR)


def estimate_affine(src_mask: np.ndarray, trg_mask: np.ndarray, mode: str='rotation') -> 'tuple[np.ndarray, np.ndarray]':
	""" Estimates the affine transformation between two masks. 
		Mode can be 'rotation', 'similarity' or 'full'."""
	
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
	rotation = (src_ellipse[2] - trg_ellipse[2]) / 180. * np.pi
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
	shift_src = src_ellipse[0]
	shift_trg = trg_ellipse[0]
	
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


def skeleton(frame: np.ndarray, radius: int=7) -> np.ndarray:
	""" Replace each connected component with a dot of radius `radius` at its center. """
	props = get_props(frame)
	centers = [p.centroid for p in props]
	out = np.zeros_like(frame)
	for c in centers:
		cv2.circle(out, (int(c[1]), int(c[0])), radius, 255, -1)
	mask = cuttlefish_mask(frame)
	out[~mask] = 0
	return out


def match(points_source_fine: np.ndarray, points_target_fine: np.ndarray, max_quotient: float) -> 'tuple[np.ndarray, np.ndarray, np.ndarray]':
	""" Matches points_source_fine to points_target_fine. Returns the matched points,
		the corresponding points in points_target_fine and the quotients of distances
		to nearest and second-nearest neighbor."""
	tree = sklearn.neighbors.KDTree(points_target_fine)
	dist, ind = tree.query(points_source_fine, k=2)
	# Consider only those points as matched, where the quotient of distances to nearest and second-nearest neighbor is < max_qoutient:
	quotients = dist[:, 0] / dist[:, 1]
	valid = quotients < max_quotient

	matched_source = points_source_fine[valid, :]
	matched_target = points_target_fine[ind[valid, 0], :]
	quotients = quotients[valid]
	# If the same points appears more than once in matched, keep only the one with the smallest quotient:
	unique, counts = np.unique(matched_target, return_counts=True, axis=0)
	multiple = unique[counts > 1, :]
	# For each of these values, keep only the one with the smallest quotient:
	for m in multiple:
		# Get indices of all occurences of m in matched:
		indices = np.where(np.all(matched_target == m, axis=1))[0]
		# Keep only the one with the smallest quotient:
		best = np.argmin(quotients[indices])
		# Set all others to False and delete them:
		indices = np.delete(indices, best)
		matched_target = np.delete(matched_target, indices, axis=0)
		matched_source = np.delete(matched_source, indices, axis=0)
		quotients = np.delete(quotients, indices)
	return matched_source, matched_target, quotients


def get_colors(num_colors: int, cmap: str) -> list:
	if cmap == 'tab':
		colors = [plt.cm.get_cmap('tab20')(v) for v in range(20)] + [plt.cm.get_cmap('tab20b')(v) for v in range(20) if v % 3] + [plt.cm.get_cmap('tab20c')(v) for v in range(20) if v % 3]
	
	else:
		colors = [plt.cm.get_cmap(cmap)(v) for v in np.linspace(0.05, 0.95, num_colors)]
		# Shuffle colors as np.array:
		colors = np.array(colors)
		np.random.shuffle(colors)
		# Convert back to list:
		colors = [tuple(c) for c in colors]
	return colors


class Triangle:
	def __init__(self, v1: 'np.ndarray|list|tuple', v2: 'np.ndarray|list|tuple', v3: 'np.ndarray|list|tuple'):
		if v1 is None or v2 is None or v3 is None:
			raise ValueError('None is not allowed as a vertex of a Triangle.')
		self.v1 = np.array(v1)
		self.v2 = np.array(v2)
		self.v3 = np.array(v3)

	def get_relative_coords(self, point: 'np.ndarray|list|tuple') -> 'list[float]':
		if point is None:
			raise ValueError('None is not allowed as a point.')
		point = np.array(point)
		v1, v2, v3 = self.v1, self.v2, self.v3
		a = np.array([[v1[0] - v3[0], v2[0] - v3[0]], 
					  [v1[1] - v3[1], v2[1] - v3[1]]])
		b = np.array([point[0] - v3[0], point[1] - v3[1]])
		l1, l2 = np.linalg.solve(a, b)
		l3 = 1 - l1 - l2
		return [l1, l2, l3]
	
	def get_absolute_coords(self, relative_coords: 'np.ndarray|list|tuple') -> np.ndarray:
		if relative_coords is None:
			raise ValueError('None is not allowed as relative_coords.')
		if len(relative_coords) != 3:
			raise ValueError('relative_coords must be a list, tuple or array of length 3.')
		l1, l2, l3 = relative_coords
		v1, v2, v3 = self.v1, self.v2, self.v3
		coords = np.dot([l1, l2, l3], [v1, v2, v3])
		return coords
	
	def get_orientation(self) -> np.ndarray:
		return self.v1 - (self.v2 + self.v3) / 2


def euclidean_distance(point1: 'np.ndarray|list', point2: 'np.ndarray|list') -> float:
	return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)



def max_consecutive_zeros_in_rows(arr: np.ndarray) -> np.ndarray:
	""" Returns the maximum number of consecutive zeros in each row of arr."""
	max_zeros = []
	for row in arr:
		max_count = 0
		current_count = 0

		for num in row:
			if num == 0:
				current_count += 1
				max_count = max(max_count, current_count)
			else:
				current_count = 0
		max_zeros.append(max_count)
	return np.array(max_zeros)


def plot_intensity(plot_frame: np.ndarray, center: np.ndarray, color: np.ndarray) -> np.ndarray:
	""" Plots a point (pixel-wise) with a given color and intensity at the given center. """
	if not isinstance(color, np.ndarray):
		color = np.array(color)
	if not isinstance(center, np.ndarray):
		center = np.array(center)
	for dx in range(-3, 4):
		for dy in range(-3, 4):
			x, y = int(center[0] + dx), int(center[1] + dy)
			if x < 0 or y < 0 or x >= plot_frame.shape[0] or y >= plot_frame.shape[1]:
				continue
			intensity = max(0, 1 - euclidean_distance((x, y), center) / np.sqrt(32))
			plot_frame[x, y] = intensity * color + (1 - intensity) * plot_frame[x, y]
	return plot_frame


def register(frame: np.ndarray, registration: np.ndarray, grid_size: int=None) -> np.ndarray:
	""" Registers the frame using the registration. """
	grid_size = frame.shape[0] / (registration.shape[1] - 1) if not grid_size else grid_size
	assert grid_size == int(grid_size), f'In registration: grid_size must be an integer, got {grid_size}! Check if grid_size is provided when calling `register`.'
	grid_size = int(grid_size)

	grow_t = np.array([[grid_size, 0., 0.], \
					   [0., grid_size, 0.]], 'float32')
	
	big_map = cv2.warpAffine(registration, grow_t, frame.shape[:2])
	frame_warped = cv2.remap(frame.astype('float64'), big_map, None, \
							 interpolation=cv2.INTER_NEAREST).astype('int64')
	return frame_warped


def center_of_chromatophore(cleanqueen: np.ndarray, segmentation_frame: np.ndarray, chromatophore_id: np.ndarray) -> 'tuple[float]':
	""" Returns the center of the chromatophore with the given id in the given segmentation frame. """
	assert cleanqueen.shape == segmentation_frame.shape
	labeled, _ = scipy.ndimage.label(np.where(cleanqueen == chromatophore_id, segmentation_frame, 0))
	# Get the most common nonzero label representing the biggest connected component and thus the chromatophore:
	if np.all(labeled == 0):
		return None
	most_common_label = np.argmax(np.bincount(labeled[labeled > 0]))
	return scipy.ndimage.measurements.center_of_mass(labeled == most_common_label)


def get_borders(image: np.ndarray) -> np.ndarray:
	""" Returns the borders of the objects in the given image. """
	# Apply sobel filter to get the borders
	dx = scipy.ndimage.sobel(image, 0)  # horizontal derivative
	dy = scipy.ndimage.sobel(image, 1)  # vertical derivative
	mag = np.hypot(dx, dy)  # magnitude
	mag *= 255.0 / np.max(mag)  # normalize to [0, 255]
	return mag


def make_cleanqueen(queenframe: np.ndarray, threshold: float, dilation_iterations: int, remove_border: bool|int=False,
					min_area: float=200, debug_args: dict={'debug': False, 'debug_visual': False}) -> np.ndarray:
	"""
	Make a cleanqueen array from a (master/queen)frame using watershedding.

	Args:
		queenframe (np.ndarray): The queenframe probabilities.
		threshold (float): The threshold for segmentation.
		dilation_iterations (int): Number of dilation iterations.
		debug_visual (bool, optional): Whether to show debug visualizations. Defaults to False.
		remove_border (bool, optional): Whether to remove border objects. Defaults to False.

	Returns:
		np.ndarray: The cleanqueen array.
	
	Note:
		A cleanqueen is a 2D array that delineates individual chromatophore territories (the space the chromatophore can occupy).
	"""
	queenframe = queenframe.astype(float)
	queenframe /= queenframe.max()
	
	props = get_props(queenframe, threshold=threshold, visual=debug_args['debug_visual'])
	body = cuttlefish_mask((queenframe * 255).astype('uint8'), dilation_iterations=dilation_iterations, debug_args=debug_args)

	markers = np.zeros_like(queenframe, dtype=int)
	for i, prop in enumerate(props):
		markers[tuple(np.swapaxes(prop.coords, 0, 1))] = i+1

	clq_markers = skimage.segmentation.watershed(-(queenframe > 0).astype(float), markers, mask=(queenframe > 0))
	clq = skimage.segmentation.watershed(-(queenframe > 0).astype(float), clq_markers, mask=body)
	
	if remove_border:
		clq = skimage.segmentation.clear_border(clq, buffer_size=int(remove_border))
		clq = skimage.segmentation.relabel_sequential(clq)[0]
	
	# Remove small objects:
	clq = skimage.morphology.remove_small_objects(clq, min_size=min_area)

	if debug_args['debug_visual']:
		fig, ax = plt.subplots(1, 3, figsize=(15, 5), sharex=True, sharey=True)
		ax[0].imshow(queenframe, cmap='gray')
		ax[0].set_title('Queenframe with chromatophore centers')
		for prop in props:
			bbox = prop.bbox
			ax[0].plot([bbox[1], bbox[1]], [bbox[0], bbox[2]], color='red')
			ax[0].plot([bbox[1], bbox[3]], [bbox[2], bbox[2]], color='red')
			ax[0].plot([bbox[3], bbox[3]], [bbox[2], bbox[0]], color='red')
			ax[0].plot([bbox[3], bbox[1]], [bbox[0], bbox[0]], color='red')
		ax[1].imshow(body, cmap='gray')
		ax[1].set_title('Body and markers')
		ax[2].imshow(skimage.segmentation.mark_boundaries(queenframe, clq, color=(1, 0, 0)))
		for prop in props:
			# Plot centroid:
			ax[2].plot(prop.centroid[1], prop.centroid[0], 'ro')
		ax[2].set_title('Cleanqueen')
		plt.gca().invert_yaxis()
		plt.tight_layout()
		plt.show()
		if input('Press enter to continue or `q` to abort: ') == 'q':
			raise KeyboardInterrupt
		
	return clq



def center_of_chromatophore_biggest(cleanqueen: np.ndarray, segmentation_frame: np.ndarray, chromatophore_ids: np.ndarray|list[int],
									return_list: bool=False, debug_visual: bool=False) -> list[np.ndarray]:
	""" Returns the centers of the chromatophores with the given ids in the given segmentation frame.
   		Center is computed as the center of masss of the connected component in the territory of the chromatophore that has the biggest area. """
	centers = {} if not return_list else []
	for cid in chromatophore_ids:
		territory = segmentation_frame * (cleanqueen == cid)
		# Get biggest connected component in the territory of the chromatophore:
		labels, n_labels = scipy.ndimage.label(territory)
		if not n_labels:
			if return_list:
				centers.append(None)
			else:
				centers[cid] = None
			log.warning(f'Chromatophore {cid} has no connected components in the territory!')
			if debug_visual:
				border = get_array_borders(cleanqueen == cid)
				frame = np.stack([segmentation_frame] *3, axis=-1)
				frame[border == 1] = [0, 255, 0]
				plt.imshow(frame)
				plt.show()
			continue
		# Compute the area of each connected component:
		areas = np.bincount(labels.ravel())
		# Get the connected component with the biggest area:
		biggest_label = np.argmax(areas[1:]) + 1
		center = np.array(scipy.ndimage.center_of_mass(labels == biggest_label))
		if return_list:
			centers.append(center)
		else:
			centers[cid] = center
	return centers



def get_array_borders(array: np.ndarray) -> np.ndarray:
	""" Find the borders between regions with different integer values in a 2D array.

	Args:
		array (np.ndarray): The 2D array containing integer values.

	Returns:
		np.ndarray: A binary array with 0s and 1s representing the border pixels.
				   1s indicate border pixels, and 0s indicate non-border pixels.
	"""
	assert isinstance(array, np.ndarray), type(array)
	if len(array.shape) != 2:
		raise ValueError("Input must be a 2D array")

	border_pixels = np.zeros_like(array, dtype=int)

	border_pixels[1:, :] |= array[1:, :] != array[:-1, :]
	border_pixels[:-1, :] |= array[:-1, :] != array[1:, :]
	border_pixels[:, 1:] |= array[:, 1:] != array[:, :-1]
	border_pixels[:, :-1] |= array[:, :-1] != array[:, 1:]

	return border_pixels

#######################
#### LOGGING & I/O ####
#######################
def save_image(image: np.ndarray, filename: str, bgr: bool=False, points: np.ndarray=None,
				  points_color: str="r", points_size: int=10, overlay: np.ndarray=None, overlay_alpha: float=0.5):
	""" Saves an image to a file. If points are given, they are plotted on the image.
		If overlay is given, it is plotted on the image. """
	fig, ax = plt.subplots(1, 1, figsize=(20, 20))
	ax.axis("off")
	if bgr:
		image = image.copy()[:,:,::-1]
	ax.imshow(image)
	if overlay is not None:
		ax.imshow(overlay, alpha=overlay_alpha)
	if points is not None:
		ax.scatter(points[:, 1], points[:, 0], c=points_color, s=points_size)
	fig.tight_layout()
	fig.savefig(filename)
	plt.close(fig)
	

def configure_logging():
	log.basicConfig(level=log.INFO, format='[%(asctime)s][%(levelname)s] %(message)s', datefmt='%D %H:%M')
	log.addLevelName(log.INFO, '\033[1;32m%s   \033[1;0m' % log.getLevelName(log.INFO))
	log.addLevelName(log.WARNING, '\033[1;33m%s\033[1;0m' % log.getLevelName(log.WARNING))
	log.addLevelName(log.ERROR, '\033[1;31m%s  \033[1;0m' % log.getLevelName(log.ERROR))
	log.addLevelName(log.CRITICAL, '\033[1;41m%s\033[1;0m' % log.getLevelName(log.CRITICAL))
	log.addLevelName(log.DEBUG, '\033[1;34m%s  \033[1;0m' % log.getLevelName(log.DEBUG))



AttributedData = namedtuple('AttributedData', ['name', 'data', 'attrs'])
		

class ConfigError(Exception):
	"""Raised when there is an error with the configuration file."""
	pass

class InputError(Exception):
	"""Raised when there is an error with the inputs."""
	pass
