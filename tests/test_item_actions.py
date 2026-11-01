from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import patch

from PySide6.QtCore import QItemSelectionModel, QSettings, Qt
from PySide6.QtGui import QContextMenuEvent
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QDialogButtonBox, QInputDialog, QLineEdit

from support import QtCase
from test_browser import image_result
from filevoyager.item_actions import flatten_folders, pack_to_folder
from filevoyager.preferences import FolderPreferences
from filevoyager.window import ExplorerWindow


class ItemOperationTests(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name)

    def test_pack_move_and_copy_files_and_folders(self):
        for copy_mode in (True, False):
            with self.subTest(copy_mode=copy_mode):
                source = self.root / str(copy_mode)
                source.mkdir()
                (source / "file.txt").write_text("file")
                (source / "folder" / "nested").mkdir(parents=True)
                (source / "folder" / "nested" / "child.txt").write_text("child")
                (source / "untouched.txt").write_text("untouched")
                paths = (source / "file.txt", source / "folder")
                target = source / "packed"
                pack_to_folder(paths, target, copy_mode)
                self.assertEqual((target / "file.txt").read_text(), "file")
                self.assertEqual((target / "folder/nested/child.txt").read_text(), "child")
                self.assertEqual([path.exists() for path in paths], [copy_mode, copy_mode])
                self.assertEqual((source / "untouched.txt").read_text(), "untouched")

    def test_flatten_multiple_selected_folders_leaves_root_and_others_alone(self):
        folders = [self.root / name for name in ("one", "two", "unselected")]
        for folder in folders:
            (folder / "nested/deeper").mkdir(parents=True)
            (folder / "empty").mkdir()
            (folder / "top.txt").write_text("top")
            (folder / "nested/deeper/child.txt").write_text(folder.name)
        flatten_folders(folders[:2])
        for folder in folders[:2]:
            self.assertEqual({path.name for path in folder.iterdir()}, {"top.txt", "child.txt"})
            self.assertEqual((folder / "child.txt").read_text(), folder.name)
        self.assertTrue((folders[2] / "nested/deeper/child.txt").is_file())
        self.assertEqual(set(self.root.iterdir()), set(folders))

    def test_collisions_surface_without_overwriting(self):
        nested = self.root / "nested"
        nested.mkdir()
        (self.root / "same.txt").write_text("original")
        (nested / "same.txt").write_text("nested")
        with self.assertRaises(FileExistsError):
            flatten_folders((self.root,))
        self.assertEqual((self.root / "same.txt").read_text(), "original")
        self.assertEqual((nested / "same.txt").read_text(), "nested")
        with self.assertRaises(FileExistsError):
            pack_to_folder((nested,), self.root, False)


class ItemActionUiTests(QtCase):
    def test_item_context_menus_preserve_selection_and_reuse_actions(self):
        folder = self.root / "context-items"
        folder.mkdir()
        for name in ("one.txt", "two.txt", "three.txt"):
            (folder / name).write_text(name)
        window = ExplorerWindow(str(folder), image_result, preferences=FolderPreferences(
            QSettings(str(self.root / "context.ini"), QSettings.Format.IniFormat)))
        window.show()
        self.addCleanup(window.close)
        self.wait_for(lambda: window.current_path == str(folder) and not window.pending_restore)
        self.wait_for(lambda: window.model.rowCount(window.details.rootIndex()) == 3)
        window.activateWindow()
        for view in (window.details, window.grid):
            window.switch_view(view)
            self.wait_for(lambda: not window.pending_restore)
            window.selection.clearSelection()
            indexes = [window.model.index(row, 0, view.rootIndex()) for row in range(3)]
            for index in indexes[:2]:
                window.selection.select(index, QItemSelectionModel.SelectionFlag.Select
                                         | QItemSelectionModel.SelectionFlag.Rows)
            point = view.visualRect(indexes[0]).center()
            QTest.mouseClick(view.viewport(), Qt.MouseButton.RightButton, pos=point)
            self.app.sendEvent(view.viewport(), QContextMenuEvent(QContextMenuEvent.Reason.Mouse,
                               point, view.viewport().mapToGlobal(point)))
            menu = window.item_menus[view]
            self.assertTrue(menu.isVisible())
            self.assertEqual(menu.actions(), [window.flatten_action, window.pack_action, window.rename_actions[view]])
            self.assertEqual(len(window.selection.selectedRows()), 2)
            self.assertFalse(window.flatten_action.isEnabled())
            self.assertFalse(window.rename_actions[view].isEnabled())
            menu.close()
            point = view.visualRect(indexes[2]).center()
            QTest.mouseClick(view.viewport(), Qt.MouseButton.RightButton, pos=point)
            self.app.sendEvent(view.viewport(), QContextMenuEvent(QContextMenuEvent.Reason.Mouse,
                               point, view.viewport().mapToGlobal(point)))
            self.assertEqual(window.selection.selectedRows(), [indexes[2]])
            self.assertTrue(window.rename_actions[view].isEnabled())
            QTest.mouseClick(menu, Qt.MouseButton.LeftButton,
                             pos=menu.actionGeometry(window.rename_actions[view]).center())
            editor = view.findChild(QLineEdit)
            self.assertTrue(editor.isVisible())
            QTest.keyClick(editor, Qt.Key.Key_Escape)
            self.wait_for(lambda: view.findChild(QLineEdit) is None)
            view.customContextMenuRequested.emit(view.viewport().rect().bottomRight())
            self.assertFalse(menu.isVisible())

    def test_tree_context_menu_targets_clicked_folder(self):
        folder = self.root / "tree-context"
        source = folder / "one"
        (source / "nested").mkdir(parents=True)
        (source / "nested" / "file.txt").write_text("contents")
        window = ExplorerWindow(str(folder), image_result, preferences=FolderPreferences(
            QSettings(str(self.root / "tree-context.ini"), QSettings.Format.IniFormat)))
        window.show()
        self.addCleanup(window.close)
        self.wait_for(lambda: window.current_path == str(folder) and not window.pending_restore)
        self.wait_for(lambda: window.folders.file_path(window.tree.currentIndex()) == str(folder))
        parent = window.tree.currentIndex()
        window.tree.expand(parent)
        self.wait_for(lambda: window.folders.rowCount(parent) == 1
                      and window.folders.file_path(window.folders.index(0, 0, parent)) == str(source))
        index = window.folders.index(0, 0, parent)
        window.tree.scrollTo(index)
        point = window.tree.visualRect(index).center()
        window.tree.customContextMenuRequested.emit(point)
        self.assertTrue(window.tree_item_menu.isVisible())
        self.assertEqual(window.tree_action_path, source)
        window.tree_item_menu.close()
        window.tree_flatten_action.trigger()
        self.wait_for(lambda: window.action_future is None)
        self.assertEqual((source / "file.txt").read_text(), "contents")
        self.assertFalse((source / "nested").exists())
        window.tree_pack_action.trigger()
        window.pack_dialog.folder_name.setText("Packed")
        window.pack_dialog.copy_mode.setChecked(True)
        window.pack_dialog.accept()
        self.wait_for(lambda: window.action_future is None)
        self.assertEqual((folder / "Packed" / "one" / "file.txt").read_text(), "contents")
        window.tree_rename_action.trigger()
        dialog = window.findChild(QInputDialog)
        self.assertTrue(dialog.isVisible())
        dialog.setTextValue("renamed")
        dialog.accept()
        self.wait_for(lambda: (folder / "renamed").exists())
        self.assertFalse(source.exists())

    def test_selection_dialog_worker_and_navigation(self):
        folder = self.root / "items"
        folder.mkdir()
        (folder / "one").mkdir()
        (folder / "two").mkdir()
        (folder / "file.txt").write_text("text")
        preferences = FolderPreferences(QSettings(str(self.root / "actions.ini"), QSettings.Format.IniFormat))
        window = ExplorerWindow(str(folder), image_result, preferences=preferences)
        window.show()
        self.addCleanup(window.close)
        self.wait_for(lambda: window.current_path == str(folder) and
                      window.model.rowCount(window.details.rootIndex()) == 3)
        self.assertFalse(window.pack_action.isEnabled())
        self.assertFalse(window.flatten_action.isEnabled())
        flags = QItemSelectionModel.SelectionFlag.Select | QItemSelectionModel.SelectionFlag.Rows
        for name in ("one", "two"):
            index = window.model.mapFromSource(window.files.index(str(folder / name)))
            window.selection.select(index, flags)
        self.assertTrue(window.flatten_action.isEnabled())
        window.switch_view(window.grid)
        self.assertEqual(set(window.selected_item_paths()), {folder / "one", folder / "two"})
        index = window.model.mapFromSource(window.files.index(str(folder / "file.txt")))
        window.selection.select(index, flags)
        self.assertFalse(window.flatten_action.isEnabled())
        window.pack_action.trigger()
        dialog = window.pack_dialog
        self.assertTrue(dialog.isVisible())
        self.assertFalse(dialog.copy_mode.isChecked())
        self.assertFalse(dialog.buttons.button(QDialogButtonBox.StandardButton.Ok).isEnabled())
        dialog.reject()
        self.assertIsNone(window.action_future)
        window.pack_action.trigger()
        dialog = window.pack_dialog
        dialog.folder_name.setText("Packed")
        dialog.copy_mode.setChecked(True)
        self.assertTrue(dialog.buttons.button(QDialogButtonBox.StandardButton.Ok).isEnabled())
        started, release = threading.Event(), threading.Event()
        threads = []

        def pack(*args):
            threads.append(threading.get_ident())
            started.set()
            release.wait(5)
            pack_to_folder(*args)

        with patch("filevoyager.window.pack_to_folder", side_effect=pack):
            dialog.accept()
            self.wait_for(started.is_set)
            self.assertFalse(window.pack_action.isEnabled())
            self.assertFalse(window.flatten_action.isEnabled())
            window.navigate(str(self.root))
            self.wait_for(lambda: window.current_path == str(self.root))
            release.set()
            self.wait_for(lambda: window.action_future is None)
        self.assertNotEqual(threads, [threading.get_ident()])
        self.assertEqual((folder / "Packed/file.txt").read_text(), "text")
        self.assertTrue((folder / "file.txt").exists())
        self.assertEqual(window.action_status.text(), "Action complete")
