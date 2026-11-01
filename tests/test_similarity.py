from functools import partial
from pathlib import Path
from threading import Event
import tempfile
import unittest

import numpy as np
from sklearn.cluster import DBSCAN

from filevoyager.image_processors import (
    EUCLIDEAN_COMPARISON, SIMILARITY_COMPARISON, VectorClusterer, dbscan_labels,
)
from filevoyager.similarity_jobs import AnalysisProgress, AnalysisSettings, analyze_folder


class SimilarityTests(unittest.TestCase):
    def test_comparison_contract(self):
        vectors = np.array([[0., 0.], [3., 4.], [0., 10.]])
        np.testing.assert_allclose(EUCLIDEAN_COMPARISON(vectors[0], vectors), [0, 5, 10])
        np.testing.assert_allclose(SIMILARITY_COMPARISON(vectors[0], vectors), [1, 1 / 6, 1 / 11])

    def test_dbscan_matches_sklearn_clusters_noise_and_duplicates(self):
        random = np.random.default_rng(14)
        datasets = [
            np.concatenate([random.normal(center, 0.03, (40, 4)) for center in [0, 1, 2]]
                           + [np.full((1, 4), 7)]),
            np.array([[0.], [0.], [0.1], [0.2], [0.3], [4.], [4.], [8.]]),
            np.array([[0.], [0.09], [0.10], [0.11], [0.20], [0.29], [0.30], [0.31]]),
            np.zeros((50, 219)),
        ]
        for vectors in datasets:
            for eps in [0.05, 0.15, 1.5]:
                for minimum in [1, 3, 6]:
                    with self.subTest(shape=vectors.shape, eps=eps, minimum=minimum):
                        expected = DBSCAN(eps=eps, min_samples=minimum, algorithm="ball_tree").fit_predict(vectors)
                        actual = VectorClusterer("test", partial(dbscan_labels, eps=eps, min_samples=minimum))(vectors)
                        np.testing.assert_array_equal(actual, expected)

    def test_cancellation_and_progress(self):
        event = Event()
        completed = []

        def progress(count, total):
            completed.append((count, total))
            event.set()

        result = dbscan_labels(np.zeros((100, 8)), cancel=event, progress=progress)
        self.assertIsNone(result)
        self.assertEqual(completed, [(1, 100)])

    def test_folder_jobs_use_configured_weights_and_release_images(self):
        from PIL import Image
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, color in [("a.png", "red"), ("b.png", "blue"), ("c.png", "red"), ("d.png", "blue"), ("e.png", "green")]:
                with Image.new("RGB", (40, 20), color) as image:
                    image.save(root / name)
            (root / "text.txt").write_text("other file")
            (root / "folder.png").mkdir()
            settings = AnalysisSettings(eps=0.001, min_samples=2)
            result = analyze_folder(directory, settings, None, Event(), AnalysisProgress())
            self.assertEqual([Path(result.paths[i]).name for i in result.order], ["a.png", "c.png", "b.png", "d.png", "e.png"])
            self.assertEqual((result.clusters, result.noise), (2, 1))
            reference = (root / "c.png").as_posix()
            nearest = analyze_folder(directory, settings, reference, Event(), AnalysisProgress())
            self.assertEqual([Path(nearest.paths[i]).name for i in nearest.order[:2]], ["a.png", "c.png"])
            geometry = analyze_folder(directory, AnalysisSettings(weights=(0, 0, 0, 0, 0, 1), eps=0.001),
                                      None, Event(), AnalysisProgress())
            self.assertEqual((geometry.clusters, geometry.noise), (1, 0))
            for file in root.glob("*.png"):
                if file.is_file():
                    file.unlink()

    def test_worker_failure_surfaces_without_substitute(self):
        from PIL import UnidentifiedImageError
        with tempfile.TemporaryDirectory() as directory:
            (Path(directory) / "broken.png").write_bytes(b"not an image")
            with self.assertRaises(UnidentifiedImageError):
                analyze_folder(directory, AnalysisSettings(), None, Event(), AnalysisProgress())
