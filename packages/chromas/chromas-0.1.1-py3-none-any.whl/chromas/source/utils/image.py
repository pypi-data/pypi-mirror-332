""" Utility functions to manipulate image data. """
import cv2
import numpy as np
import dask.array as da

def normalize(image: np.ndarray) -> np.ndarray:
	""" 
	Normalize an image to the range [0, 1].
	
	Parameters:
		image (np.ndarray): The input image.
		
	Returns:
		np.ndarray: The normalized image.    
	"""
	return (image - np.min(image)) / (np.max(image) - np.min(image))


def denormalize(image: np.ndarray, min_value: float, max_value: float) -> np.ndarray:
	""" 
	Denormalize an image to the range [min_value, max_value].
	
	Parameters:
		image (np.ndarray): The input image.
		min_value (float): The minimum value of the output image.
		max_value (float): The maximum value of the output image.
		
	Returns:
		np.ndarray: The denormalized image.    
	"""
	return (image * (max_value - min_value)) + min_value


def rgb2bgr(rgb: np.ndarray) -> np.ndarray:
	""" 
	Convert an RGB image to BGR.
	
	Parameters:
		rgb (np.ndarray): The RGB image.
		
	Returns:
		np.ndarray: The BGR image of same datatype as input image.    
	"""
	return rgb[..., ::-1]


def bgr2rgb(bgr: np.ndarray) -> np.ndarray:
	""" 
	Convert a BGR image to RGB.
	
	Parameters:
		bgr (np.ndarray): The BGR image.
		
	Returns:
		np.ndarray: The RGB image of same datatype as input image.    
	"""
	return bgr[..., ::-1]


def grayscale(rgb: np.ndarray) -> np.ndarray:
	""" 
	Convert an RGB image to grayscale.
	
	Parameters:
		rgb (np.ndarray): The RGB image.
		
	Returns:
		np.ndarray: The grayscale image of same datatype as input image.    
	"""
	result = ((rgb[..., 0] * 0.2125) +
			  (rgb[..., 1] * 0.7154) +
			  (rgb[..., 2] * 0.0721))
	return result.astype(rgb.dtype)


def warp_frame(image: np.ndarray, maps: np.ndarray, border_value: int=255) -> np.ndarray:
	if isinstance(image, np.ndarray) or isinstance(image, da.Array):
		return cv2.remap(image, maps, None, interpolation=cv2.INTER_NEAREST, borderMode=cv2.BORDER_CONSTANT, borderValue=border_value)
	elif isinstance(image, tuple) and isinstance(image[0], np.ndarray):
		return tuple(cv2.remap(i, maps, None, interpolation=cv2.INTER_NEAREST, borderMode=cv2.BORDER_CONSTANT, borderValue=border_value) for i in image)
	else:
		raise ValueError(f'Invalid input type of image {type(image)}.')