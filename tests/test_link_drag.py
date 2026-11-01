from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import unittest
from unittest.mock import Mock, patch

from comtypes.client import CreateObject
from PySide6.QtCore import QItemSelectionModel, QMimeData, QPoint, QPointF, QSettings, QUrl, Qt
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
                    self.assertEqual(enter.isAccepted(), modifier == Qt.KeyboardModifier.NoModifier)
                enter = QDragEnterEvent(QPointF(point), actions, mime, Qt.MouseButton.LeftButton, Qt.KeyboardModifier.AltModifier)
                self.app.sendEvent(view.viewport(), enter)
                self.assertTrue(enter.isAccepted(), (window.current_path, window.action_future,
                                window.link_drag.destination(view, point), view.viewport().acceptDrops()))
                self.assertEqual(enter.dropAction(), Qt.DropAction.LinkAction)
                reads = mime.reads
                released = QDragMoveEvent(QPointF(point), actions, mime, Qt.MouseButton.LeftButton, Qt.KeyboardModifier.NoModifier)
                self.app.sendEvent(view.viewport(), released)
                self.assertTrue(released.isAccepted())
                self.assertEqual(released.dropAction(), Qt.DropAction.MoveAction)
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

    def test_select_toggle_controls_native_move_drags_and_preserves_batch(self):
        root = self.root / "select-toggle"
        root.mkdir()
        for name in ("one.txt", "two.txt", "three.txt"):
            (root / name).write_text(name)
        settings = QSettings(str(self.root / "select-toggle.ini"), QSettings.Format.IniFormat)
        window = ExplorerWindow(str(root), image_result, preferences=FolderPreferences(settings))
        window.show()
        self.addCleanup(window.close)
        self.wait_for(lambda: window.current_path == str(root) and not window.pending_restore)
        self.wait_for(lambda: window.model.rowCount(window.details.rootIndex()) == 3)
        self.assertFalse(window.select_mode.isChecked())
        for view in (window.details, window.grid):
            window.switch_view(view)
            self.wait_for(lambda: not window.pending_restore)
            for selecting in (False, True):
                window.select_mode.setChecked(selecting)
                window.selection.clearSelection()
                indexes = [window.model.index(row, 0, view.rootIndex()) for row in range(3)]
                for index in indexes[:2]:
                    window.selection.select(index, QItemSelectionModel.SelectionFlag.Select
                                             | QItemSelectionModel.SelectionFlag.Rows)
                point = view.visualRect(indexes[0]).center()
                end = view.visualRect(indexes[2]).center()
                with patch("filevoyager.link_drag.QDrag.exec", return_value=Qt.DropAction.IgnoreAction) as execute:
                    QTest.mousePress(view.viewport(), Qt.MouseButton.LeftButton, pos=point)
                    move = QMouseEvent(QMouseEvent.Type.MouseMove, QPointF(end),
                                       QPointF(view.viewport().mapToGlobal(end)), Qt.MouseButton.NoButton,
                                       Qt.MouseButton.LeftButton, Qt.KeyboardModifier.NoModifier)
                    self.app.sendEvent(view.viewport(), move)
                    if selecting:
                        execute.assert_not_called()
                        self.assertTrue(window.selection.isSelected(indexes[2]))
                    else:
                        execute.assert_called_once_with(Qt.DropAction.MoveAction, Qt.DropAction.MoveAction)
                        self.assertEqual(window.selection.selectedRows(), indexes[:2])
                    QTest.mouseRelease(view.viewport(), Qt.MouseButton.LeftButton, pos=end)
        self.assertTrue(settings.value("interaction/select_mode", type=bool))

    def test_move_drops_use_shared_conflicts_in_all_views_without_changing_clipboard(self):
        root = self.root / "move-drop"
        root.mkdir()
        destination = root / "destination"
        destination.mkdir()
        window = ExplorerWindow(str(root), image_result, preferences=FolderPreferences(
            QSettings(str(self.root / "move-drop.ini"), QSettings.Format.IniFormat)))
        window.show()
        self.addCleanup(window.close)
        self.wait_for(lambda: window.current_path == str(root) and not window.pending_restore)
        self.wait_for(lambda: window.model.rowCount(window.details.rootIndex()) == 1)
        window.file_clipboard.clipboard.setText("clipboard stays")
        self.addCleanup(window.file_clipboard.clipboard.clear)
        for number, view in enumerate((window.details, window.grid, window.tree)):
            incoming = self.root / f"move-incoming-{number}.txt"
            incoming.write_text("new")
            target = destination / incoming.name
            target.write_text("old")
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
            point = view.visualRect(index).center()
            mime = CountedMimeData()
            mime.setUrls([QUrl.fromLocalFile(str(incoming))])
            for answer in ("skip", "cancel", "replace"):
                window.folder_merge.ask = Mock(return_value=answer)
                enter = QDragEnterEvent(QPointF(point), Qt.DropAction.MoveAction, mime,
                                       Qt.MouseButton.LeftButton, Qt.KeyboardModifier.NoModifier)
                self.app.sendEvent(view.viewport(), enter)
                self.assertTrue(enter.isAccepted())
                drop = QDropEvent(QPointF(point), Qt.DropAction.MoveAction, mime,
                                  Qt.MouseButton.LeftButton, Qt.KeyboardModifier.NoModifier)
                self.app.sendEvent(view.viewport(), drop)
                self.assertTrue(drop.isAccepted())
                self.wait_for(lambda: window.action_future is None)
                window.folder_merge.ask.assert_called_once_with(incoming, target, False)
                self.assertEqual(incoming.exists(), answer != "replace")
                self.assertEqual(target.read_text(), "new" if answer == "replace" else "old")
                self.assertEqual(window.file_clipboard.clipboard.text(), "clipboard stays")
            self.assertEqual(mime.reads, 3)

    def test_background_folder_move_and_rejected_recursive_targets(self):
        root = self.root / "background-move"
        root.mkdir()
        source = self.root / "incoming-folder"
        (source / "nested").mkdir(parents=True)
        (source / "nested/file.txt").write_text("contents")
        window = ExplorerWindow(str(root), image_result, preferences=FolderPreferences(
            QSettings(str(self.root / "background-move.ini"), QSettings.Format.IniFormat)))
        window.show()
        self.addCleanup(window.close)
        self.wait_for(lambda: window.current_path == str(root) and not window.pending_restore)
        view = window.details
        point = view.viewport().rect().bottomRight()
        mime = QMimeData()
        for path in (root, self.root):
            mime.setUrls([QUrl.fromLocalFile(str(path))])
            enter = QDragEnterEvent(QPointF(point), Qt.DropAction.MoveAction, mime,
                                   Qt.MouseButton.LeftButton, Qt.KeyboardModifier.NoModifier)
            self.app.sendEvent(view.viewport(), enter)
            self.assertFalse(enter.isAccepted())
        mime.setUrls([QUrl.fromLocalFile(str(source))])
        enter = QDragEnterEvent(QPointF(point), Qt.DropAction.MoveAction, mime,
                               Qt.MouseButton.LeftButton, Qt.KeyboardModifier.NoModifier)
        self.app.sendEvent(view.viewport(), enter)
        self.assertTrue(enter.isAccepted())
        drop = QDropEvent(QPointF(point), Qt.DropAction.MoveAction, mime,
                          Qt.MouseButton.LeftButton, Qt.KeyboardModifier.NoModifier)
        self.app.sendEvent(view.viewport(), drop)
        self.assertTrue(drop.isAccepted())
        self.wait_for(lambda: window.action_future is None)
        self.assertFalse(source.exists())
        self.assertEqual((root / source.name / "nested/file.txt").read_text(), "contents")
        self.assertEqual(window.link_drag.drag_sources, set())
        self.assertEqual(window.link_drag.drag_parents, set())

    def test_drag_mode_preserves_single_click_and_double_click(self):
        root = self.root / "drag-clicks"
        root.mkdir()
        for name in ("one", "two"):
            (root / name).mkdir()
        window = ExplorerWindow(str(root), image_result, preferences=FolderPreferences(
            QSettings(str(self.root / "drag-clicks.ini"), QSettings.Format.IniFormat)))
        window.show()
        self.addCleanup(window.close)
        self.wait_for(lambda: window.current_path == str(root) and not window.pending_restore)
        self.wait_for(lambda: window.model.rowCount(window.details.rootIndex()) == 2)
        for view in (window.details, window.grid):
            window.switch_view(view)
            self.wait_for(lambda: not window.pending_restore)
            indexes = [window.model.index(row, 0, view.rootIndex()) for row in range(2)]
            for index in indexes:
                window.selection.select(index, QItemSelectionModel.SelectionFlag.Select
                                         | QItemSelectionModel.SelectionFlag.Rows)
            point = view.visualRect(indexes[0]).center()
            QTest.mouseClick(view.viewport(), Qt.MouseButton.LeftButton, pos=point)
            self.assertEqual(window.selection.selectedRows(), indexes[:1])
            with patch.object(window, "navigate") as navigate:
                QTest.mouseDClick(view.viewport(), Qt.MouseButton.LeftButton, pos=point)
                navigate.assert_called_once()
                self.assertEqual(Path(navigate.call_args.args[0]), root / "one")


if __name__ == "__main__":
    unittest.main()
