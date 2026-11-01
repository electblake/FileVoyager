from functools import partial
from pathlib import Path
from threading import Event
import tempfile
import unittest
from unittest.mock import patch

from PySide6.QtGui import QColor, QImage
from filevoyager.models import MEDIA_SUFFIXES

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

    def test_mixed_media_uses_thumbnail_pixels_for_clustering_and_comparison(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            colors = {"a.mp4": "red", "b.png": "blue", "c.MKV": "red", "d.mov": "blue", "e.webp": "green"}
            for name in colors:
                (root / name).write_bytes(b"original media must not be decoded")
            (root / "text.txt").touch()
            (root / "folder.mp4").mkdir()
            calls = []

            def thumbnail(path, width, height):
                calls.append((Path(path).name, width, height))
                # Odd width exercises padded RGB888 rows during conversion.
                image = QImage(41, 20, QImage.Format.Format_RGB888)
                image.fill(QColor(colors[Path(path).name]))
                return image

            settings = AnalysisSettings(eps=0.001, min_samples=2)
            with patch("PIL.Image.open", side_effect=AssertionError("original decoded")):
                result = analyze_folder(directory, settings, None, Event(), AnalysisProgress(), thumbnail)
                self.assertEqual([Path(result.paths[i]).name for i in result.order], ["a.mp4", "c.MKV", "b.png", "d.mov", "e.webp"])
                self.assertEqual((result.clusters, result.noise), (2, 1))
                self.assertEqual(calls, [(name, 128, 128) for name in colors])
                nearest = analyze_folder(directory, settings, (root / "c.MKV").as_posix(), Event(), AnalysisProgress(), thumbnail)
                self.assertEqual([Path(nearest.paths[i]).name for i in nearest.order[:2]], ["a.mp4", "c.MKV"])
                self.assertEqual(nearest.distances[0], 0)
                self.assertGreater(nearest.distances[1], 0)
                geometry = analyze_folder(directory, AnalysisSettings(weights=(0, 0, 0, 0, 0, 1), eps=0.001),
                                          None, Event(), AnalysisProgress(), thumbnail)
                self.assertEqual((geometry.clusters, geometry.noise), (1, 0))
            for name in colors:
                (root / name).unlink()

    def test_analysis_covers_every_grid_media_suffix(self):
        with tempfile.TemporaryDirectory() as directory:
            for suffix in MEDIA_SUFFIXES:
                (Path(directory) / ("media" + suffix.upper())).touch()
            calls = []

            def thumbnail(path, width, height):
                calls.append(Path(path).suffix.lower())
                image = QImage(20, 10, QImage.Format.Format_RGB32)
                image.fill(QColor("red"))
                return image

            result = analyze_folder(directory, AnalysisSettings(), None, Event(), AnalysisProgress(), thumbnail)
            self.assertEqual(set(calls), MEDIA_SUFFIXES)
            self.assertEqual(len(result.paths), len(MEDIA_SUFFIXES))
            self.assertEqual(result.clusters, 1)

    def test_cache_miss_surfaces_without_original_decode_or_substitute(self):
        failure = OSError("cached thumbnail unavailable")
        with tempfile.TemporaryDirectory() as directory:
            (Path(directory) / "video.mp4").touch()
            with patch("PIL.Image.open", side_effect=AssertionError("original decoded")), patch(
                    "filevoyager.shell_bridge.load_cached_thumbnail", side_effect=failure) as native:
                from filevoyager.shell_bridge import load_thumbnail_image
                with self.assertRaises(OSError) as raised:
                    analyze_folder(directory, AnalysisSettings(), None, Event(), AnalysisProgress(), load_thumbnail_image)
                self.assertIs(raised.exception, failure)
                native.assert_called_once()
