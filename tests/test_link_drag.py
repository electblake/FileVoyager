from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import unittest
from unittest.mock import patch

from comtypes.client import CreateObject
from PySide6.QtCore import QMimeData, QPoint, QPointF, QSettings, QUrl, Qt
from PySide6.QtGui import QDragEnterEvent, QDragMoveEvent, QDropEvent, QMouseEvent
from PySide6.QtTest import QTest

from support import QtCase
from test_browser import image_result
from filevoyager.link_drag import create_shortcuts
from filevoyager.preferences import FolderPreferences
from filevoyager.window import ExplorerWindow


class CountedMimeData(QMimeData):
    reads = 0

    def urls(self):
        self.reads += 1
        return super().urls()


class LinkDragTests(QtCase):
    def test_native_shortcuts_preserve_targets_and_existing_links(self):
        root = self.root / "native"
        root.mkdir()
        source = root / "file with spaces.txt"
        source.write_text("contents")
        folder = root / "folder"
        folder.mkdir()
        with ThreadPoolExecutor(max_workers=1) as worker:
            worker.submit(create_shortcuts, (source, folder), root).result()
            shell = CreateObject("WScript.Shell", dynamic=True)
            for path in (source, folder):
                shortcut = root / (path.name + " - Shortcut.lnk")
                self.assertEqual(Path(shell.CreateShortcut(str(shortcut)).TargetPath), path)
                self.assertFalse(shortcut.is_symlink())
            original = (root / "file with spaces.txt - Shortcut.lnk").read_bytes()
            with self.assertRaises(FileExistsError):
                worker.submit(create_shortcuts, (source,), root).result()
            self.assertEqual((root / "file with spaces.txt - Shortcut.lnk").read_bytes(), original)
        self.assertEqual(source.read_text(), "contents")
        self.assertTrue(folder.is_dir())

    def test_alt_drag_cursor_action_and_drops_in_all_views(self):
        root = self.root / "drag"
        root.mkdir()
        destination = root / "destination"
        destination.mkdir()
        source = root / "source.txt"
        source.write_text("contents")
        window = ExplorerWindow(str(root), image_result, preferences=FolderPreferences(
            QSettings(str(self.root / "drag.ini"), QSettings.Format.IniFormat)))
        window.show()
        self.addCleanup(window.close)
        self.wait_for(lambda: window.current_path == str(root) and not window.pending_restore)
        self.wait_for(lambda: window.model.rowCount(window.details.rootIndex()) == 2)
        mime = CountedMimeData()
        mime.setUrls([QUrl.fromLocalFile(str(source))])
        actions = Qt.DropAction.LinkAction | Qt.DropAction.CopyAction | Qt.DropAction.MoveAction
        for number, view in enumerate((window.details, window.grid, window.tree)):
            with self.subTest(view=type(view).__name__):
                incoming = self.root / f"incoming-{number}.txt"
                incoming.write_text("contents")
                mime.setUrls([QUrl.fromLocalFile(str(incoming))])
                if view is window.tree:
                    self.wait_for(lambda: window.folders.file_path(view.currentIndex()) == str(root))
                    parent = view.currentIndex()
                    view.expand(parent)
                    self.wait_for(lambda: window.folders.file_path(window.folders.index(0, 0, parent)) == str(destination))
                    index = window.folders.index(0, 0, parent)
                else:
                    window.switch_view(view)
                    self.wait_for(lambda: not window.pending_restore)
                    index = window.model.mapFromSource(window.files.index(str(destination)))
                view.scrollTo(index)
                point = view.visualRect(index).center()
                self.assertEqual(view.indexAt(point), index)
                with patch("filevoyager.link_drag.QDrag.exec", return_value=Qt.DropAction.IgnoreAction) as execute:
                    QTest.mousePress(view.viewport(), Qt.MouseButton.LeftButton,
                                     Qt.KeyboardModifier.AltModifier, point)
                    move = QMouseEvent(QMouseEvent.Type.MouseMove, QPointF(point + QPoint(30, 0)),
                                       QPointF(view.viewport().mapToGlobal(point + QPoint(30, 0))),
                                       Qt.MouseButton.NoButton, Qt.MouseButton.LeftButton, Qt.KeyboardModifier.AltModifier)
                    self.app.sendEvent(view.viewport(), move)
                    execute.assert_called_once_with(Qt.DropAction.LinkAction, Qt.DropAction.LinkAction)
                    QTest.mouseRelease(view.viewport(), Qt.MouseButton.LeftButton, pos=point)
                for modifier in (Qt.KeyboardModifier.NoModifier, Qt.KeyboardModifier.ControlModifier):
                    enter = QDragEnterEvent(QPointF(point), actions, mime, Qt.MouseButton.LeftButton, modifier)
                    self.app.sendEvent(view.viewport(), enter)
                    self.assertFalse(enter.isAccepted())
                enter = QDragEnterEvent(QPointF(point), actions, mime, Qt.MouseButton.LeftButton, Qt.KeyboardModifier.AltModifier)
                self.app.sendEvent(view.viewport(), enter)
                self.assertTrue(enter.isAccepted(), (window.current_path, window.action_future,
                                window.link_drag.destination(view, point), view.viewport().acceptDrops()))
                self.assertEqual(enter.dropAction(), Qt.DropAction.LinkAction)
                reads = mime.reads
                released = QDragMoveEvent(QPointF(point), actions, mime, Qt.MouseButton.LeftButton, Qt.KeyboardModifier.NoModifier)
                self.app.sendEvent(view.viewport(), released)
                self.assertFalse(released.isAccepted())
                held = QDragMoveEvent(QPointF(point), actions, mime, Qt.MouseButton.LeftButton, Qt.KeyboardModifier.AltModifier)
                self.app.sendEvent(view.viewport(), held)
                self.assertTrue(held.isAccepted())
                self.assertEqual(held.dropAction(), Qt.DropAction.LinkAction)
                drop = QDropEvent(QPointF(point), actions, mime, Qt.MouseButton.LeftButton, Qt.KeyboardModifier.AltModifier)
                self.app.sendEvent(view.viewport(), drop)
                self.assertTrue(drop.isAccepted())
                self.assertEqual(mime.reads, reads)
                self.assertEqual(window.link_drag.drag_paths, ())
                self.wait_for(lambda: window.action_future is None)
                link = destination / (incoming.name + " - Shortcut.lnk")
                self.assertEqual(Path(CreateObject("WScript.Shell", dynamic=True).CreateShortcut(str(link)).TargetPath), incoming)
                self.assertEqual(incoming.read_text(), "contents")


if __name__ == "__main__":
    unittest.main()
