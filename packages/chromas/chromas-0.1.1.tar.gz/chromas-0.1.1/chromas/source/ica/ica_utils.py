import click
import numpy as np
from sklearn.decomposition import FastICA, PCA
from scipy import signal
from scipy.ndimage import gaussian_filter1d
from kneed import KneeLocator
import warnings


def compute_pca_ica(matrix, sigma=2, max_iter=1000):
	# Convert nan and inf to zero:
	matrix = np.nan_to_num(matrix, posinf=0, neginf=0)
	detrended_matrix = signal.detrend(matrix, axis=0)

	pca = PCA()
	pca.fit_transform(detrended_matrix.copy())
	explained_variance = pca.explained_variance_ratio_

	kneedle = KneeLocator(
		range(1, len(explained_variance) + 1),
		explained_variance,
		curve='convex',
		direction='decreasing'
	)
	
	elbow_point = kneedle.elbow - 1  # Correct the elbow point by subtracting 1
	if elbow_point is None:
		elbow_point = len(explained_variance)
	else:
		elbow_point = max(1, elbow_point)  # Ensure at least one component

	diff_matrix = np.diff(detrended_matrix, axis=0)
	expansion_matrix = np.where(diff_matrix > 0, diff_matrix, 0)

	smoothed_matrix = gaussian_filter1d(expansion_matrix, sigma=sigma, axis=1, mode='wrap')
	smoothed_matrix = np.nan_to_num(smoothed_matrix, posinf=0, neginf=0)

	n_slices = smoothed_matrix.shape[1]
	n_components = min(elbow_point, n_slices)

	with warnings.catch_warnings(record=True) as caught_warnings:
		warnings.simplefilter("always")
		ica = FastICA(n_components=n_components, max_iter=max_iter) 
		ica_sources = ica.fit_transform(smoothed_matrix)
		if caught_warnings:
			click.secho(f'Did not converge for {n_components=}.', fg='yellow')
			for warning in caught_warnings:
				click.secho(f'\t{warning.message}', fg='yellow')
		
	mixing_matrix = ica.mixing_ # Transpose to match expected shape

	abs_mixing_matrix = np.absolute(mixing_matrix)
	sum_per_slice = np.sum(abs_mixing_matrix, axis=1, keepdims=True)
	percentage_influence = (abs_mixing_matrix / sum_per_slice) * 100

	return elbow_point, explained_variance, ica_sources, mixing_matrix, percentage_influence
