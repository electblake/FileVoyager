from concurrent.futures import Future
from ctypes import WinDLL, create_unicode_buffer
from ctypes.wintypes import HMODULE, DWORD, LPWSTR
from pathlib import Path
from threading import Event, get_ident
import tempfile
from unittest.mock import patch

from PIL import Image
from PySide6.QtCore import QItemSelectionModel, QSettings, Qt
from PySide6.QtGui import QImage
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtTest import QTest
from support import QtCase

from filevoyager.media_runtime import FFMPEG_BIN, FFMPEG_LIBRARIES
from filevoyager.preferences import FolderPreferences
from filevoyager.preview_dock import PreviewDock
from filevoyager.window import ExplorerWindow


class PreviewDockTests(QtCase):
    def thumbnail(self, path, width, height):
        image = QImage(width, height // 2, QImage.Format.Format_RGB32)
        image.fill(Qt.GlobalColor.red)
        return image

    def test_native_metadata_and_window_selection(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "image.png"
            Image.new("RGB", (640, 480)).save(path)
            preferences = FolderPreferences(QSettings(
                str(Path(directory) / "settings.ini"), QSettings.Format.IniFormat))
            window = ExplorerWindow(directory, self.thumbnail, preferences=preferences)
            window.show()
            self.wait_for(lambda: window.current_path == directory and not window.pending_restore)
            dock = window.preview_dock
            self.assertEqual(window.dockWidgetArea(dock), Qt.DockWidgetArea.RightDockWidgetArea)
            self.assertLess(dock.y(), window.similarity_dock.y())
            index = window.model.mapFromSource(window.files.index(str(path)))
            window.selection.setCurrentIndex(index, QItemSelectionModel.SelectionFlag.ClearAndSelect
                                             | QItemSelectionModel.SelectionFlag.Rows)
            self.wait_for(lambda: dock.form.rowCount() > 6)
            rows = {dock.form.itemAt(row, dock.form.ItemRole.LabelRole).widget().text():
                    dock.form.itemAt(row, dock.form.ItemRole.FieldRole).widget().text()
                    for row in range(dock.form.rowCount())}
            self.assertEqual(rows["Width"], "640")
            self.assertEqual(rows["Height"], "480")
            self.assertFalse(dock.preview.pixmap().isNull())
            window.switch_view(window.details)
            self.assertEqual(dock.path, str(path).replace("\\", "/"))
            dock.setFloating(True)
            self.assertTrue(dock.isFloating())
            dock.setFloating(False)
            dock.close()
            dock.toggleViewAction().trigger()
            self.assertTrue(dock.isVisible())
            window.selection.clearSelection()
            self.assertEqual(dock.form.rowCount(), 0)
            self.assertEqual(dock.path, "")
            window.close()

    def test_rapid_selection_keeps_only_latest_request_and_discards_stale_result(self):
        started = Event()
        release = Event()
        calls = []
        threads = []

        def thumbnail(path, width, height):
            calls.append(path)
            threads.append(get_ident())
            started.set()
            release.wait(5)
            return self.thumbnail(path, width, height)

        dock = PreviewDock(thumbnail)
        with patch("filevoyager.preview_dock.load_properties", return_value=[("Name", "latest")]):
            dock.set_item("first.png", True)
            self.wait_for(started.is_set)
            for number in range(1000):
                dock.set_item(f"{number}.png", True)
            self.assertEqual(calls, ["first.png"])
            self.assertEqual(dock.pending[1], "999.png")
            dock.debounce.stop()
            dock.timer.stop()
            release.set()
            dock.future.result(timeout=5)
            dock.poll()
            self.assertEqual(dock.form.rowCount(), 0)
            self.wait_for(lambda: dock.future is None)
            self.assertEqual(calls, ["first.png", "999.png"])
            self.assertEqual(dock.form.rowCount(), 1)
            self.assertTrue(all(thread != get_ident() for thread in threads))
        dock.shutdown()

    def test_clear_discards_inflight_result_and_failure_propagates(self):
        dock = PreviewDock(self.thumbnail)
        dock.set_item("old.png", True)
        dock.request = dock.pending
        dock.future = Future()
        dock.future.set_result((self.thumbnail("", 192, 192), [("Name", "old")]))
        dock.set_item("")
        dock.poll()
        self.assertEqual(dock.form.rowCount(), 0)
        failure = OSError("preview failed")
        dock.future = Future()
        dock.future.set_exception(failure)
        with self.assertRaises(OSError) as raised:
            dock.poll()
        self.assertIs(raised.exception, failure)
        self.assertIsNone(dock.future)
        self.assertFalse(dock.timer.isActive())
        dock.shutdown()

    def test_video_seek_play_pause_and_selection_cleanup(self):
        path = str(Path(__file__).parent / "fixtures" / "preview-video.mp4")
        dock = PreviewDock(self.thumbnail)
        self.addCleanup(dock.close)
        self.addCleanup(dock.shutdown)
        dock.resize(360, 500)
        dock.show()
        frame_times = []
        dock.video.videoSink().videoFrameChanged.connect(
            lambda frame: frame_times.append(frame.startTime()) if frame.isValid() else None)
        with patch("filevoyager.preview_dock.load_properties", return_value=[("Name", "video")]):
            dock.set_item(path, True)
            self.wait_for(lambda: dock.play_button.isEnabled() and dock.seek_slider.isEnabled()
                          and dock.future is None and not dock.debounce.isActive())
            self.assertTrue(dock.controls.isVisible())
            self.assertIs(dock.display.currentWidget(), dock.preview)
            self.assertEqual(dock.player.playbackState(), QMediaPlayer.PlaybackState.StoppedState)
            self.assertEqual(dock.seek_slider.maximum(), 3000)
            # A keyboard seek from the poster must decode a frame without playing.
            QTest.keyClick(dock.seek_slider, Qt.Key.Key_Right)
            self.wait_for(lambda: frame_times and 900_000 <= frame_times[-1] <= 1_100_000)
            # Verify the actual loaded modules after Qt has decoded a frame.
            module_path = WinDLL("kernel32").GetModuleFileNameW
            module_path.argtypes = [HMODULE, LPWSTR, DWORD]
            module_path.restype = DWORD
            for library in FFMPEG_LIBRARIES:
                buffer = create_unicode_buffer(32768)
                self.assertGreater(module_path(library._handle, buffer, len(buffer)), 0)
                self.assertEqual(Path(buffer.value).parent, FFMPEG_BIN)
            self.assertEqual(dock.player.position(), 1000)
            self.assertIs(dock.display.currentWidget(), dock.video)
            self.assertEqual(dock.player.playbackState(), QMediaPlayer.PlaybackState.PausedState)
            dock.play_button.click()
            self.wait_for(lambda: dock.player.position() > 1100)
            self.assertEqual(dock.play_button.toolTip(), "Pause")
            dock.play_button.click()
            position = dock.player.position()
            QTest.qWait(100)
            self.assertEqual(dock.player.position(), position)
            self.assertEqual(dock.play_button.toolTip(), "Play")
            self.assertEqual(dock.seek_slider.value(), position)
            # Dragging holds the thumb steady and defers decoding until release.
            dock.seek_slider.setSliderDown(True)
            dock.seek_slider.setSliderPosition(2000)
            self.assertEqual(dock.player.position(), position)
            dock.update_position(position)
            self.assertEqual(dock.seek_slider.sliderPosition(), 2000)
            dock.seek_slider.setSliderDown(False)
            self.wait_for(lambda: 1_900_000 <= frame_times[-1] <= 2_100_000)
            self.assertEqual(dock.player.position(), 2000)
            dock.play_button.click()
            dock.hide()
            self.assertEqual(dock.player.playbackState(), QMediaPlayer.PlaybackState.PausedState)
            dock.show()
            self.assertEqual(dock.player.playbackState(), QMediaPlayer.PlaybackState.PausedState)
            dock.set_item("image.png", True)
            self.assertTrue(dock.player.source().isEmpty())
            self.assertTrue(dock.controls.isHidden())
            self.assertIs(dock.display.currentWidget(), dock.preview)
            self.assertEqual(dock.seek_slider.maximum(), 0)
            dock.set_item("")

    def test_video_source_is_debounced_and_released_on_shutdown(self):
        path = str(Path(__file__).parent / "fixtures" / "preview-video.mp4")
        dock = PreviewDock(self.thumbnail)
        self.addCleanup(dock.shutdown)
        with patch("filevoyager.preview_dock.load_properties", return_value=[]):
            for number in range(1000):
                dock.set_item(f"{number}.mp4", True)
            self.assertTrue(dock.player.source().isEmpty())
            dock.set_item(path, True)
            self.wait_for(lambda: dock.play_button.isEnabled() and dock.future is None
                          and not dock.debounce.isActive())
            self.assertEqual(dock.player.source().toLocalFile(), path.replace("\\", "/"))
            dock.shutdown()
            self.assertTrue(dock.player.source().isEmpty())
