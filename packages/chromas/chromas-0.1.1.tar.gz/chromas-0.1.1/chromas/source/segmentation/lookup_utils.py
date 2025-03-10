import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from skimage.segmentation import mark_boundaries

def convert(image_rgb, color_space):
    if color_space == 'Lab':
        image_preprocessed = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2Lab)
        l, a, b = cv2.split(image_preprocessed)
    
        # Contrast enhancement on L channel
        l_equalized = cv2.equalizeHist(l)
        image_preprocessed = cv2.merge((l_equalized, a, b))
        image_preprocessed = cv2.cvtColor(image_preprocessed, cv2.COLOR_Lab2RGB)
    
    elif color_space == 'HSV':
        image_preprocessed = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)
        h, s, v = cv2.split(image_preprocessed)
    
        # Normalize V channel and enhance yellow chromophores in H and S
        v_normalized = cv2.normalize(v, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
        s_normalized = cv2.normalize(s, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    
        # Increase saturation for more vivid colors and enhance contrast
        s_enhanced = cv2.equalizeHist(s_normalized)
        v_enhanced = cv2.equalizeHist(v_normalized)
    
        # Merge the enhanced channels back
        image_preprocessed = cv2.merge((h, s_enhanced, v_enhanced))
        image_preprocessed = cv2.cvtColor(image_preprocessed, cv2.COLOR_HSV2RGB)
    
    elif color_space == 'bin3':
        # Bin each value of R, G, and B into 3 bins
        image_preprocessed = image_rgb // 85 * 85
    
    elif color_space == 'pca':
        # Apply PCA to reduce the dimensionality of the image
        pixel_values = image_rgb.reshape((-1, 3)).astype(float)
        mean = np.mean(pixel_values, axis=0)
        pixel_values -= mean
        cov = np.cov(pixel_values, rowvar=False)
        _, _, v = np.linalg.svd(cov)
        pca_components = v[:3]  # Keep the first three principal components
        pixel_values_reduced = np.dot(pixel_values, pca_components.T)
        pixel_values_reconstructed = np.dot(pixel_values_reduced, pca_components) + mean
        image_preprocessed = pixel_values_reconstructed.reshape(image_rgb.shape).astype("uint8")
    
    elif color_space == 'custom':
        image_preprocessed = np.zeros_like(image_rgb)
        image_preprocessed[..., 0] = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
        image_preprocessed[..., 1] = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2XYZ)[..., 1]
        image_preprocessed[..., 2] = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2Lab)[..., 2]
    
    elif color_space == 'normal':
        # Divide channels by 255, then normalize by subtracting the mean and dividing by the standard deviation, then adjust s.t. mean = [0.485, 0.456, 0.406] and std = [0.229, 0.224, 0.225], then rescale to [0, 255]:
        image_preprocessed = image_rgb / 255
        image_preprocessed = (image_preprocessed - np.mean(image_preprocessed, axis=(0, 1))) / np.std(image_preprocessed, axis=(0, 1)) * np.array([0.229, 0.224, 0.225]) + np.array([0.485, 0.456, 0.406])
        image_preprocessed = np.clip(image_preprocessed * 255, 0, 255).astype(np.uint8)
    else:
        image_preprocessed = image_rgb

    return image_preprocessed


# Function to perform K-means clustering using predefined centers
def kmeans_with_manual_centers(image, initial_centers, n_points_per_cluster=1):
    # Reshape image data to a 2D array of pixels
    pixel_values = image.reshape((-1, 3)).astype(float)

    # Convert selected centers to the correct format for K-means
    initial_centers = np.array(initial_centers).astype(float)

    # Run K-means with predefined centers
    kmeans = KMeans(n_clusters=len(initial_centers), init=initial_centers, n_init=1)
    labels = kmeans.fit_predict(pixel_values)


    # Map each pixel to its cluster color
    segmented_image = kmeans.cluster_centers_[labels].reshape(image.shape).astype("uint8")
    labeled_image = labels.reshape(image.shape[:2])
    labeled_image = labeled_image // n_points_per_cluster

    return segmented_image, labeled_image, kmeans


# Function to build a lookup table based on quantized colors and cluster centers
def build_lookup_table(kmeans, preprocessing, n_points_per_cluster=1):
    """ Hello there x6! """
    lookup_table = np.zeros((16, 16, 16), dtype='uint8')

    for r in range(16):
        for g in range(16):
            for b in range(16):
                color = np.array([r, g, b]) * 16
                color = preprocessing(color)
                label = kmeans.predict(color.reshape(1, -1))[0] // n_points_per_cluster
                lookup_table[r, g, b] = label
    return lookup_table


# Segmentation function using the quantized lookup table
def segment_image_with_lookup(image, flat_lookup_table):
    # Quantize the image to match the lookup table resolution
    image = (image >> 4).astype(np.uint16)  # Equivalent to image // 16

    # Compute a single index for lookup
    indices = image[..., 0] << 8 | image[..., 1] << 4 | image[..., 2]

    # Get labels using the computed indices
    return flat_lookup_table[indices]