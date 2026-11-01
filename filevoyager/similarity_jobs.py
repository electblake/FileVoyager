"""Background folder analysis; no Qt objects or image data retained in results."""

from dataclasses import dataclass
from functools import partial
from pathlib import Path
import os

IMAGE_SUFFIXES = frozenset({".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff",
                            ".gif", ".avif", ".heic", ".heif", ".jxl"})


@dataclass(frozen=True)
class AnalysisSettings:
    weights: tuple = (2.0, 1.5, 1.0, 0.5, 0.8, 0.25)
    eps: float = 0.25
    min_samples: int = 3


@dataclass
class AnalysisProgress:
    state: tuple = ("Starting", 0, 0)


@dataclass(frozen=True)
class AnalysisResult:
    paths: tuple
    order: tuple
    clusters: int
    noise: int
    distances: tuple


def analyze_folder(folder, settings, reference, cancel, progress):
    import numpy as np
    from PIL import Image
    from filevoyager.image_processors import ImageFeatureExtractor, extract_visual_features
    from filevoyager.image_processors.similarity import (
        EUCLIDEAN_COMPARISON, VectorClusterer, dbscan_labels,
    )

    with os.scandir(folder) as entries:
        paths = tuple(sorted((entry.path.replace("\\", "/") for entry in entries
                              if Path(entry.name).suffix.lower() in IMAGE_SUFFIXES and entry.is_file()),
                             key=lambda path: (path.casefold(), path)))
    if not paths:
        return AnalysisResult((), (), 0, 0, ())
    dimensions = sum(size for size, weight in zip((96, 48, 48, 21, 5, 1), settings.weights) if weight != 0)
    extractor = ImageFeatureExtractor("spectra.configured", dimensions,
                                     partial(extract_visual_features, feature_weights=settings.weights))
    vectors = np.empty((len(paths), dimensions), dtype=np.float64)
    for index, path in enumerate(paths):
        if cancel.is_set():
            return None
        progress.state = ("Extracting images", index, len(paths))
        with Image.open(path) as image:
            vectors[index] = extractor(image)
    if cancel.is_set():
        return None
    if reference is not None:
        progress.state = ("Comparing images", 0, len(paths))
        distances = EUCLIDEAN_COMPARISON(vectors[paths.index(reference)], vectors)
        order = np.argsort(distances, kind="stable")
        return AnalysisResult(paths, tuple(int(i) for i in order), 0, 0, tuple(distances))
    progress.state = ("Clustering images", 0, len(paths))

    def cluster_progress(completed, total):
        progress.state = ("Clustering images", completed, total)

    clusterer = VectorClusterer("dbscan.euclidean", partial(dbscan_labels, eps=settings.eps,
                                                           min_samples=settings.min_samples))
    labels = clusterer(vectors, cancel=cancel, progress=cluster_progress)
    if labels is None:
        return None
    clusters = len(set(labels) - {-1})
    # Cluster IDs follow alphabetical input; noise follows clustered images.
    order = np.argsort(np.where(labels == -1, clusters, labels), kind="stable")
    return AnalysisResult(paths, tuple(int(i) for i in order), clusters, int(np.sum(labels == -1)), ())
