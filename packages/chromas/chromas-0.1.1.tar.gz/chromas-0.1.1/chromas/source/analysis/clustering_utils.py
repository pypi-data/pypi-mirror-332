import numpy as np
import sklearn.cluster
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.spatial.distance import squareform


def cluster_correlation(corr: np.ndarray, method: str = 'AffinityPropagation', **kwargs) -> np.ndarray:
	match method.lower():
		case 'affinitypropagation':
			clusterer = sklearn.cluster.AffinityPropagation(affinity='precomputed', **kwargs)
			return clusterer.fit_predict(corr - 1)
		
		case 'hdbscan':
			clusterer = sklearn.cluster.HDBSCAN(metric='precomputed', **kwargs)
			return clusterer.fit_predict(1 - corr)
		
		case 'hierarchical':
			Z = linkage(squareform(1 - corr), method='ward')
			# Find the optimal number of clusters
			max_d = 0.5 * np.max(Z[:, 2])
			return fcluster(Z, max_d, criterion='distance') - 1