from pathlib import Path
from concurrent.futures import Future
from threading import Event, get_ident
import tempfile
import unittest
from unittest.mock import patch

from PySide6.QtGui import QColor, QImage
from PySide6.QtCore import QItemSelectionModel, QSettings, Qt
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication

from filevoyager.preferences import FolderPreferences
from filevoyager.window import ExplorerWindow


class SimilarityDockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.images = self.root / "images"
        self.images.mkdir()
        for name, color in [("a.mp4", "red"), ("b.mkv", "blue"), ("c.MOV", "red"), ("d.webm", "blue"), ("e.avi", "green")]:
            (self.images / name).write_bytes(b"media original must not be read")
        (self.images / "folder").mkdir()
        (self.images / "text.txt").touch()
        preferences = FolderPreferences(QSettings(str(self.root / "settings.ini"), QSettings.Format.IniFormat))
        self.thumbnail_threads = []
        colors = {"a.mp4": "red", "b.mkv": "blue", "c.MOV": "red", "d.webm": "blue", "e.avi": "green"}

        def thumbnail(path, width, height):
            self.thumbnail_threads.append(get_ident())
            image = QImage(41, 20, QImage.Format.Format_RGB888)
            image.fill(QColor(colors[Path(path).name]))
            return image

        self.window = ExplorerWindow(str(self.images), thumbnail, preferences=preferences)
        self.window.show()
        self.addCleanup(self.window.close)
        self.wait_for(lambda: self.window.model.rowCount(self.window.details.rootIndex()) == 7)
        self.wait_for(lambda: not self.window.pending_restore)

    def wait_for(self, condition):
        for _ in range(1000):
            if condition():
                return
            QTest.qWait(10)
        self.assertTrue(condition())

    def names(self):
        window = self.window
        return [window.model.index(row, 0, window.details.rootIndex()).data() for row in range(7)]

    def test_right_dock_clusters_and_preserves_selection_across_views(self):
        window = self.window
        dock = window.similarity_dock
        self.assertEqual(window.dockWidgetArea(dock), Qt.DockWidgetArea.RightDockWidgetArea)
        index = window.model.mapFromSource(window.files.index(str(self.images / "c.MOV")))
        window.selection.setCurrentIndex(index, QItemSelectionModel.SelectionFlag.ClearAndSelect | QItemSelectionModel.SelectionFlag.Rows)
        dock.eps.setValue(0.001)
        dock.min_samples.setValue(2)
        dock.cluster_button.click()
        self.assertFalse(dock.cluster_button.isEnabled())
        self.wait_for(lambda: dock.future is None)
        self.assertEqual(self.names(), ["folder", "a.mp4", "c.MOV", "b.mkv", "d.webm", "e.avi", "text.txt"])
        self.assertEqual(window.selection.currentIndex().data(), "c.MOV")
        self.assertIs(window.grid.model(), window.details.model())
        self.assertIn("2 clusters", dock.status.text())
        self.assertIn("5 media items", dock.status.text())
        self.assertTrue(dock.compare_button.isEnabled())
        self.assertTrue(all(thread != get_ident() for thread in self.thumbnail_threads))
        dock.compare_button.click()
        self.wait_for(lambda: dock.future is None)
        self.assertEqual(self.names()[1:3], ["a.mp4", "c.MOV"])
        dock.clear_button.click()
        self.assertEqual(self.names(), ["folder", "a.mp4", "b.mkv", "c.MOV", "d.webm", "e.avi", "text.txt"])
        window.details.sortByColumn(0, Qt.SortOrder.DescendingOrder)
        self.assertIsNone(window.model.ranks)
        dock.setFloating(True)
        self.assertTrue(dock.isFloating())
        dock.setFloating(False)
        dock.close()
        dock.toggleViewAction().trigger()
        self.assertTrue(dock.isVisible())

    def test_navigation_cancels_worker_and_never_applies_stale_order(self):
        window = self.window
        dock = window.similarity_dock
        started = Event()
        thread_ids = []

        def analyze(folder, settings, reference, cancel, progress, load_thumbnail):
            thread_ids.append(get_ident())
            started.set()
            cancel.wait(10)
            return None

        with patch("filevoyager.similarity_dock.analyze_folder", side_effect=analyze):
            dock.cluster_button.click()
            self.wait_for(started.is_set)
            window.navigate(str(self.images / "folder"))
            self.wait_for(lambda: window.current_path == str(self.images / "folder") and dock.future is None)
        self.assertNotEqual(thread_ids[0], get_ident())
        self.assertIsNone(window.model.ranks)
        self.assertEqual(window.model.rowCount(window.details.rootIndex()), 0)

    def test_no_enabled_features_disables_analysis(self):
        dock = self.window.similarity_dock
        for spin in dock.weights:
            spin.setValue(0)
        self.assertFalse(dock.cluster_button.isEnabled())
        self.assertFalse(dock.compare_button.isEnabled())

    def test_failed_future_surfaces_once_without_applying_order(self):
        dock = self.window.similarity_dock
        failure = OSError("image read failed")
        future = Future()
        future.set_exception(failure)
        dock.future = future
        with self.assertRaises(OSError) as raised:
            dock.poll()
        self.assertIs(raised.exception, failure)
        self.assertIsNone(dock.future)
        self.assertFalse(dock.timer.isActive())
        self.assertIsNone(self.window.model.ranks)
