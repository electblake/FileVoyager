"""Vector comparison and DBSCAN with one radius neighborhood retained at a time."""

from collections import deque
from collections.abc import Callable
from dataclasses import dataclass

import numpy as np


def euclidean_distances(reference, vectors):
    """Return distances from one vector to each row, with no all-pairs matrix."""
    return np.linalg.norm(vectors - reference, axis=1)


def similarity_scores(reference, vectors):
    """Return 1 / (1 + Euclidean distance); identical vectors score 1."""
    return 1 / (1 + euclidean_distances(reference, vectors))


@dataclass(frozen=True)
class VectorComparison:
    name: str
    compare: Callable

    def __call__(self, reference, vectors):
        return self.compare(reference, vectors)


EUCLIDEAN_COMPARISON = VectorComparison("euclidean", euclidean_distances)
SIMILARITY_COMPARISON = VectorComparison("inverse_euclidean", similarity_scores)


@dataclass(frozen=True)
class VectorClusterer:
    """Wrap a configured (vectors, *, cancel, progress) -> labels callable.

    labels are integers, -1 denotes noise. Cooperative cancellation returns None.
    progress receives (completed, total); cancel is a threading.Event or None.
    """

    name: str
    cluster: Callable

    def __call__(self, vectors, *, cancel=None, progress=None):
        return self.cluster(vectors, cancel=cancel, progress=progress)


def dbscan_labels(vectors, *, eps=0.25, min_samples=3, cancel=None, progress=None):
    """Euclidean DBSCAN; min_samples includes the point itself.

    Uses scikit-learn's BallTree neighbor index, retaining only one neighborhood
    and a deduplicated expansion queue. Additional storage is O(n * d + n),
    rather than storing all n neighborhoods. Labels follow input row order.
    """
    from sklearn.neighbors import NearestNeighbors

    neighbors = NearestNeighbors(radius=eps, algorithm="ball_tree", metric="euclidean", n_jobs=1).fit(vectors)
    labels = np.full(len(vectors), -1, dtype=np.intp)
    visited = np.zeros(len(vectors), dtype=bool)
    queued = np.zeros(len(vectors), dtype=bool)
    cluster = 0
    completed = 0
    for seed in range(len(vectors)):
        if cancel is not None and cancel.is_set():
            return None
        if visited[seed]:
            continue
        queue = deque([seed])
        queued[seed] = True
        expanding = False
        while queue:
            if cancel is not None and cancel.is_set():
                return None
            point = queue.popleft()
            if not visited[point]:
                visited[point] = True
                indices = neighbors.radius_neighbors(vectors[point:point + 1], return_distance=False)[0]
                completed += 1
                if len(indices) >= min_samples:
                    expanding = True
                    for index in indices:
                        if not queued[index]:
                            queue.append(int(index))
                            queued[index] = True
                        if labels[index] == -1:
                            labels[index] = cluster
                if progress is not None:
                    progress(completed, len(vectors))
            if expanding and labels[point] == -1:
                labels[point] = cluster
        if expanding:
            cluster += 1
    return labels
