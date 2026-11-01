"""Qt integration tests use synthetic image results, never a production fallback."""

from pathlib import Path
import tempfile
import threading
import time
import unittest
import json
import subprocess
import sys
from unittest.mock import patch

from PySide6.QtCore import QEventLoop, QItemSelectionModel, QSettings, QTimer, Qt
from PySide6.QtGui import QImage
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication

from filevoyager.thumbnails import ThumbnailCache, ThumbnailKey
from filevoyager.window import ExplorerWindow
from filevoyager.directory_tree import path_key, scan_directories
from filevoyager.preferences import FolderPreferences


def image_result(path, width, height):
    image = QImage(width, height, QImage.Format.Format_ARGB32_Premultiplied)
    image.fill(Qt.GlobalColor.darkCyan)
    return image


class BrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])
        cls.temp = tempfile.TemporaryDirectory(prefix="filevoyager-test-")
        cls.root = Path(cls.temp.name)
        cls.first = cls.root / "first"
        cls.second = cls.root / "second"
        cls.first.mkdir()
        cls.second.mkdir()
        cls.videos = cls.root / "videos"
        cls.videos.mkdir()
        for extension in [".mp4", ".MP4", ".mkv"]:
            (cls.videos / f"video{extension}").touch()
        (cls.first / "folder.png").mkdir()
        for number in range(600):
            (cls.first / f"image-{number:04}.png").touch()
        for number in range(20):
            (cls.second / f"image-{number:04}.png").touch()

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def wait_for(self, condition, seconds=10):
        if condition():
            return
        loop = QEventLoop()
        poll = QTimer()
        poll.setInterval(10)
        poll.timeout.connect(lambda: loop.quit() if condition() else None)
        timeout = QTimer()
        timeout.setSingleShot(True)
        timeout.timeout.connect(loop.quit)
        poll.start()
        timeout.start(round(seconds * 1000))
        loop.exec()
        poll.stop()
        timeout.stop()
        self.assertTrue(condition(), "Qt condition did not become true")

    def open_window(self, loader=image_result):
        preferences = FolderPreferences(QSettings(str(self.root / (self.id() + ".ini")), QSettings.Format.IniFormat))
        preferences.save(str(self.first), preferences.load(str(self.first), False))
        window = ExplorerWindow(str(self.first), loader, preferences=preferences)
        window.show()
        self.addCleanup(window.close)
        self.wait_for(lambda: window.current_path == str(self.first))
        self.wait_for(lambda: window.model.rowCount(window.details.rootIndex()) == 601)
        return window

    def test_file_quit_saves_settings_before_closing(self):
        window = self.open_window()
        menus = window.menuBar().actions()
        self.assertEqual([action.text() for action in menus], ["&File", "&Help"])
        settings = window.preferences.settings
        settings.setValue("quit-test", "saved")
        with patch.object(settings, "sync", wraps=settings.sync) as sync:
            menus[0].menu().actions()[0].trigger()
            self.assertGreaterEqual(sync.call_count, 1)
        self.assertFalse(window.isVisible())
        self.assertIn("quit-test=saved", Path(settings.fileName()).read_text())

    def test_help_opens_update_dialog_without_starting_network_request(self):
        window = self.open_window()
        window.menuBar().actions()[1].menu().actions()[0].trigger()
        dialog = window.update_dialog
        self.assertTrue(dialog.isVisible())
        self.assertIsNone(dialog.future)
        self.assertTrue(dialog.check_button.isEnabled())
        dialog.reject()
        window.menuBar().actions()[1].menu().actions()[0].trigger()
        self.assertIsNot(window.update_dialog, dialog)
        self.assertTrue(window.update_dialog.isVisible())
        window.update_dialog.reject()

    def test_shared_selection_sort_and_history(self):
        window = self.open_window()
        index = window.model.index(5, 0, window.details.rootIndex())
        selected_path = window.files.filePath(window.model.mapToSource(index))
        window.selection.setCurrentIndex(index, QItemSelectionModel.SelectionFlag.ClearAndSelect
                                         | QItemSelectionModel.SelectionFlag.Rows)
        window.switch_view(window.grid)
        self.assertIs(window.grid.selectionModel(), window.details.selectionModel())
        window.details.sortByColumn(0, Qt.SortOrder.DescendingOrder)
        QTest.qWait(50)
        self.assertEqual(window.files.filePath(window.model.mapToSource(window.selection.currentIndex())),
                         selected_path)
        window.navigate(str(self.second))
        self.wait_for(lambda: window.current_path == str(self.second))
        window.travel(-1)
        self.wait_for(lambda: window.current_path == str(self.first))
        self.assertEqual(len(window.history), 2)
        self.assertTrue(window.forward_action.isEnabled())

    def test_folder_tree_only_inserts_directories_and_tracks_changes(self):
        window = self.open_window()
        self.wait_for(lambda: window.folders.file_path(window.tree.currentIndex()) == str(self.first))
        root = window.folders.index_for_path(str(self.first))
        window.tree.expand(root)
        self.wait_for(lambda: window.folders.rowCount(root) == 1)
        self.assertEqual(window.folders.columnCount(root), 1)
        self.assertEqual(window.model.rowCount(window.details.rootIndex()), 601)
        folder = self.first / "new folder"
        folder.mkdir()
        self.wait_for(lambda: window.folders.rowCount(root) == 2)
        self.wait_for(lambda: window.model.rowCount(window.details.rootIndex()) == 602)
        tree_index = window.folders.index_for_path(str(folder))
        window.tree.clicked.emit(tree_index)
        self.wait_for(lambda: window.current_path == str(folder))
        self.assertLessEqual(window.folders.peak_batch, 128)
        window.navigate(str(self.first))
        self.wait_for(lambda: window.current_path == str(self.first))
        folder.rmdir()
        self.wait_for(lambda: window.folders.rowCount(root) == 1)
        self.wait_for(lambda: window.model.rowCount(window.details.rootIndex()) == 601)

    def test_folder_tree_reveal_uses_latest_target_after_worker_completes(self):
        started = threading.Event()
        release = threading.Event()
        worker_threads = []

        def scan(path):
            worker_threads.append(threading.get_ident())
            if path == str(self.root):
                started.set()
                release.wait(10)
            return scan_directories(path)

        with patch("filevoyager.directory_tree.scan_directories", side_effect=scan):
            window = self.open_window()
            self.wait_for(started.is_set)
            window.navigate(str(self.second))
            self.wait_for(lambda: window.current_path == str(self.second))
            release.set()
            self.wait_for(lambda: window.folders.file_path(window.tree.currentIndex()) == str(self.second))
        self.assertTrue(worker_threads)
        self.assertTrue(all(worker != threading.get_ident() for worker in worker_threads))

    def test_deleted_tree_subfolder_cancels_its_queued_scan(self):
        window = self.open_window()
        self.wait_for(lambda: window.folders.file_path(window.tree.currentIndex()) == str(self.first))
        root = window.folders.index_for_path(str(self.first))
        window.tree.expand(root)
        self.wait_for(lambda: window.folders.rowCount(root) == 1)
        parent = self.first / "queued-parent"
        child = parent / "queued-child"
        child.mkdir(parents=True)
        self.wait_for(lambda: window.folders.rowCount(root) == 2)
        parent_index = window.folders.index_for_path(str(parent))
        window.tree.expand(parent_index)
        self.wait_for(lambda: path_key(str(child)) in window.folders.nodes
                      and window.folders.active_key is None)
        started, release = threading.Event(), threading.Event()
        calls = []

        def scan(path):
            calls.append(path)
            if path == str(parent):
                started.set()
                release.wait(10)
            return scan_directories(path)

        with patch("filevoyager.directory_tree.scan_directories", side_effect=scan):
            window.folders.request_scan(str(parent))
            self.wait_for(started.is_set)
            window.folders.request_scan(str(child))
            child.rmdir()
            release.set()
            self.wait_for(lambda: window.folders.active_key is None and not window.folders.queue)
        self.assertNotIn(str(child), calls)
        self.assertNotIn(path_key(str(child)), window.folders.nodes)
        self.assertEqual(window.folders.rowCount(parent_index), 0)
        parent.rmdir()
        self.wait_for(lambda: window.folders.rowCount(root) == 1)

    def test_thumbnail_work_is_visible_bounded_and_off_ui_thread(self):
        calls = []
        main_thread = threading.get_ident()

        def loader(path, width, height):
            calls.append((path, threading.get_ident()))
            return image_result(path, width, height)

        window = self.open_window(loader)
        window.switch_view(window.grid)
        self.wait_for(lambda: window.thumbnails.completed >= 4)
        self.wait_for(lambda: not window.thumbnails.active and not window.thumbnails.pending)
        self.assertLess(len(calls), 80)
        self.assertTrue(all(thread != main_thread for _, thread in calls))
        self.assertLessEqual(window.thumbnails.peak_active, 2)
        self.assertLessEqual(window.thumbnails.peak_pending, 128)
        self.assertLessEqual(window.cache.bytes_used, window.cache.budget)
        self.assertTrue(all(not path.endswith("folder.png") for path, _ in calls))
        initial_calls = len(calls)
        window.switch_view(window.details)
        window.switch_view(window.grid)
        QTest.qWait(150)
        self.assertEqual(len(calls), initial_calls)
        window.grid.verticalScrollBar().setValue(window.grid.verticalScrollBar().maximum())
        self.wait_for(lambda: len(calls) > initial_calls)

    def test_navigation_discards_inflight_thumbnail_results(self):
        gate = threading.Event()

        def loader(path, width, height):
            gate.wait(2)
            return image_result(path, width, height)

        window = self.open_window(loader)
        window.switch_view(window.grid)
        self.wait_for(lambda: len(window.thumbnails.active) == 2)
        window.navigate(str(self.second))
        self.wait_for(lambda: window.current_path == str(self.second))
        gate.set()
        self.wait_for(lambda: window.thumbnails.stale_results == 2)
        self.assertTrue(all(str(self.first) not in key.path for key in window.cache.entries))
        self.wait_for(lambda: window.thumbnails.completed > 0)

    def test_cache_eviction_is_byte_bounded(self):
        cache = ThumbnailCache(budget=2 * 32 * 32 * 4)
        image = image_result("", 32, 32)
        keys = [ThumbnailKey(str(i), 0, 0, 32, 1.0) for i in range(3)]
        cache.put(keys[0], image)
        cache.put(keys[1], image)
        cache.get(keys[0])
        cache.put(keys[2], image)
        self.assertIsNone(cache.get(keys[1]))
        self.assertIsNotNone(cache.get(keys[0]))
        self.assertEqual(cache.bytes_used, cache.budget)

    def test_video_grid_uses_the_same_thumbnail_service(self):
        calls = []

        def loader(path, width, height):
            calls.append(path)
            return image_result(path, width, height)

        window = self.open_window(loader)
        window.navigate(str(self.videos))
        self.wait_for(lambda: window.current_path == str(self.videos))
        # Windows treats the .mp4 and .MP4 fixture paths as the same file.
        self.wait_for(lambda: window.model.rowCount(window.details.rootIndex()) == 2)
        window.switch_view(window.grid)
        self.wait_for(lambda: window.thumbnails.completed == 2)
        self.assertEqual({Path(path).suffix.lower() for path in calls}, {".mp4", ".mkv"})
        for row in range(2):
            index = window.model.index(row, 0, window.grid.rootIndex())
            self.assertFalse(window.model.thumbnail_decoration(index).isNull())

    def test_latest_navigation_request_wins(self):
        window = self.open_window()
        window.navigate(str(self.second))
        window.navigate(str(self.first))
        window.navigate(str(self.second))
        self.wait_for(lambda: window.current_path == str(self.second)
                      and window.navigation_future is None)
        self.assertEqual(window.history, [str(self.first), str(self.second)])

    def test_unsaved_media_folders_default_to_grid(self):
        preferences = FolderPreferences(QSettings(str(self.root / "defaults.ini"), QSettings.Format.IniFormat))
        window = ExplorerWindow(str(self.first), image_result, preferences=preferences)
        window.show()
        self.addCleanup(window.close)
        self.wait_for(lambda: window.current_path == str(self.first) and not window.pending_restore)
        self.assertIs(window.views.currentWidget(), window.grid)
        window.navigate(str(self.root))
        self.wait_for(lambda: window.current_path == str(self.root) and not window.pending_restore)
        self.assertIs(window.views.currentWidget(), window.details)
        window.navigate(str(self.videos))
        self.wait_for(lambda: window.current_path == str(self.videos) and not window.pending_restore)
        self.assertIs(window.views.currentWidget(), window.grid)

    def test_folder_preferences_restore_on_navigation_and_new_window(self):
        filename = str(self.root / "persistent-views.ini")

        def preferences():
            return FolderPreferences(QSettings(filename, QSettings.Format.IniFormat))

        window = ExplorerWindow(str(self.first), image_result, preferences=preferences())
        window.show()
        self.addCleanup(window.close)
        self.wait_for(lambda: window.current_path == str(self.first) and not window.pending_restore)
        window.icon_size.setCurrentIndex(2)
        self.wait_for(lambda: window.grid.verticalScrollBar().maximum() > 20000)
        window.grid.verticalScrollBar().setValue(20000)
        window.switch_view(window.details)
        self.wait_for(lambda: not window.pending_restore)
        window.details.verticalScrollBar().setValue(120)
        window.switch_view(window.grid)
        self.wait_for(lambda: not window.pending_restore)
        self.assertEqual(window.grid.verticalScrollBar().value(), 20000)
        window.navigate(str(self.second))
        self.wait_for(lambda: window.current_path == str(self.second) and not window.pending_restore)
        window.icon_size.setCurrentIndex(0)
        window.switch_view(window.details)
        self.wait_for(lambda: not window.pending_restore)
        window.navigate(str(self.first))
        self.wait_for(lambda: window.current_path == str(self.first) and not window.pending_restore)
        self.assertIs(window.views.currentWidget(), window.grid)
        self.assertEqual(window.icon_size.currentData(), 192)
        self.assertEqual(window.grid.verticalScrollBar().value(), 20000)
        window.close()

        # A separate interpreter proves that state reached disk, not only Qt's cache.
        command = ("import json,sys; from PySide6.QtCore import QSettings; "
                   "from filevoyager.preferences import FolderPreferences; "
                   "p=FolderPreferences(QSettings(sys.argv[1],QSettings.Format.IniFormat)); "
                   "print(json.dumps(p.load(sys.argv[2],True)))")
        saved = json.loads(subprocess.check_output([sys.executable, "-c", command, filename, str(self.first)], text=True))
        self.assertEqual(saved["grid"][0], 20000)
        self.assertEqual(saved["details"][0], 120)

        reopened = ExplorerWindow(str(self.first), image_result, preferences=preferences())
        reopened.show()
        self.addCleanup(reopened.close)
        self.wait_for(lambda: reopened.current_path == str(self.first) and not reopened.pending_restore)
        self.assertIs(reopened.views.currentWidget(), reopened.grid)
        self.assertEqual(reopened.icon_size.currentData(), 192)
        self.assertEqual(reopened.grid.verticalScrollBar().value(), 20000)
        reopened.switch_view(reopened.details)
        self.wait_for(lambda: not reopened.pending_restore)
        self.assertEqual(reopened.details.verticalScrollBar().value(), 120)
        reopened.navigate(str(self.second))
        self.wait_for(lambda: reopened.current_path == str(self.second) and not reopened.pending_restore)
        self.assertIs(reopened.views.currentWidget(), reopened.details)
        self.assertEqual(reopened.icon_size.currentData(), 80)

    def test_failed_requests_surface_once_without_automatic_retry(self):
        calls = []
        failure = OSError("expected service failure")

        def loader(path, width, height):
            calls.append(path)
            raise failure

        window = self.open_window(loader)
        controller = window.thumbnails
        controller.enabled = True
        controller.refresh()
        controller.poll_timer.stop()
        controller.pending.clear()
        futures = list(controller.active)
        for future in futures:
            while not future.done():
                time.sleep(.001)
        for _ in futures:
            with self.assertRaises(OSError) as raised:
                controller.poll()
            self.assertIs(raised.exception, failure)
        attempted = set(controller.requested)
        self.assertEqual(len(attempted), len(futures))
        controller.refresh()
        self.assertTrue(attempted.isdisjoint(key for _, key in controller.active.values()))
        controller.poll_timer.stop()
        controller.pending.clear()
        # Observe the other viewport requests too, without letting Qt swallow test exceptions.
        for future in list(controller.active):
            with self.assertRaises(OSError):
                future.result()
        controller.active.clear()


if __name__ == "__main__":
    unittest.main()
