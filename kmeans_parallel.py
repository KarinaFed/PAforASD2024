import numpy as np
from dask_ml.cluster import KMeans as DaskKMeans
import dask.array as da

class KMeansParallel:
    def __init__(self, n_clusters=10, max_iter=300):
        self.n_clusters = n_clusters
        self.max_iter = max_iter

    def fit(self, X):
        # Conversion to a Dask array for parallel processing
        dX = da.from_array(X, chunks=(X.shape[0] // 10 + 1, X.shape[1]))
        # Disk Key for clustering
        kmeans = DaskKMeans(n_clusters=self.n_clusters, max_iter=self.max_iter)
        kmeans.fit(dX)
        return kmeans.labels_
