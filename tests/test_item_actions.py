from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import patch

from PySide6.QtCore import QItemSelectionModel, QPersistentModelIndex, QSettings, QSignalBlocker, Qt
from PySide6.QtGui import QContextMenuEvent
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QDialogButtonBox, QInputDialog, QLineEdit, QToolBar

from support import QtCase
from test_browser import image_result
from filevoyager.item_actions import flatten_folders, join_to_folder, pack_to_folder
from filevoyager.preferences import FolderPreferences
from filevoyager.window import ExplorerWindow
from filevoyager.file_model import directory_snapshot
from filevoyager.directory_tree import path_key


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

    def test_join_moves_or_copies_contents_without_nesting_selected_folders(self):
        for copy_mode in (False, True):
            source = self.root / str(copy_mode)
            first, second = source / "one", source / "two"
            (first / "nested").mkdir(parents=True)
            second.mkdir()
            (first / "a.txt").write_text("a")
            (first / "nested/child.txt").write_text("child")
            (second / "b.txt").write_text("b")
            (source / "unselected.txt").write_text("untouched")
            destination = source / "Joined"
            join_to_folder((first, second), destination, copy_mode)
            self.assertEqual({item.name for item in destination.iterdir()}, {"a.txt", "b.txt", "nested"})
            self.assertEqual((destination / "nested/child.txt").read_text(), "child")
            self.assertEqual((destination / "a.txt").read_text(), "a")
            self.assertEqual((destination / "b.txt").read_text(), "b")
            self.assertTrue(first.is_dir() and second.is_dir())
            self.assertEqual(bool(list(first.iterdir())), copy_mode)
            self.assertEqual(bool(list(second.iterdir())), copy_mode)
            self.assertEqual((source / "unselected.txt").read_text(), "untouched")

    def test_join_collision_does_not_overwrite_either_file(self):
        first, second = self.root / "one", self.root / "two"
        first.mkdir()
        second.mkdir()
        (first / "same.txt").write_text("one")
        (second / "same.txt").write_text("two")
        destination = self.root / "Joined"
        with self.assertRaises(FileExistsError):
            join_to_folder((first, second), destination, False)
        self.assertEqual((destination / "same.txt").read_text(), "one")
        self.assertEqual((second / "same.txt").read_text(), "two")

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
    def test_pack_refreshes_loaded_views_once_without_watcher_notifications(self):
        folder = self.root / "refresh-pack"
        folder.mkdir()
        for number in range(1200):
            (folder / f"{number:04}.txt").touch()
        window = ExplorerWindow(str(folder), image_result, preferences=FolderPreferences(
            QSettings(str(self.root / "refresh-pack.ini"), QSettings.Format.IniFormat)))
        window.show()
        self.addCleanup(window.close)
        self.wait_for(lambda: window.current_path == str(folder) and not window.pending_restore)
        self.wait_for(lambda: window.model.rowCount(window.details.rootIndex()) == 1200)
        self.wait_for(lambda: path_key(folder) in window.folders.nodes)
        tree_root = window.folders.index_for_path(str(folder))
        window.tree.expand(tree_root)
        self.wait_for(lambda: window.folders.nodes[path_key(folder)].loaded
                      and window.folders.active_key is None)
        survivor = QPersistentModelIndex(window.files.index(str(folder / "1199.txt")))
        resets, scans = [], []
        window.files.modelReset.connect(lambda: resets.append(True))

        def scan(*args):
            scans.append((args[0], threading.get_ident()))
            return directory_snapshot(*args)

        paths = tuple(folder / f"{number:04}.txt" for number in range(1000))
        with QSignalBlocker(window.files.watcher), QSignalBlocker(window.folders.watcher), patch(
                "filevoyager.file_model.directory_snapshot", side_effect=scan):
            window.show_pack_dialog(paths=paths)
            window.pack_dialog.folder_name.setText("Packed")
            window.pack_dialog.accept()
            self.wait_for(lambda: window.action_future is None)
            self.wait_for(lambda: window.model.rowCount(window.details.rootIndex()) == 201)
            self.wait_for(lambda: path_key(folder / "Packed") in window.folders.nodes)
            self.wait_for(lambda: window.files.future is None and window.files.applying is None
                          and not window.files.pending)
        self.assertEqual([path_key(path) for path, _ in scans], [path_key(folder)])
        self.assertTrue(all(thread != threading.get_ident() for _, thread in scans))
        self.assertFalse(resets)
        self.assertTrue(survivor.isValid())
        self.assertEqual(survivor.data(), "1199.txt")
        self.assertLessEqual(window.files.peak_batch, 512)
        window.switch_view(window.grid)
        self.wait_for(lambda: not window.pending_restore)
        self.assertEqual(window.model.rowCount(window.grid.rootIndex()), 201)

    def test_join_refreshes_cached_source_after_navigation_without_notifications(self):
        folder = self.root / "refresh-join"
        source = folder / "source"
        source.mkdir(parents=True)
        (source / "file.txt").write_text("content")
        other = self.root / "refresh-unrelated"
        other.mkdir()
        window = ExplorerWindow(str(source), image_result, preferences=FolderPreferences(
            QSettings(str(self.root / "refresh-join.ini"), QSettings.Format.IniFormat)))
        window.show()
        self.addCleanup(window.close)
        self.wait_for(lambda: window.current_path == str(source) and not window.pending_restore)
        self.wait_for(lambda: window.files.rowCount(window.files.index(str(source))) == 1)
        window.navigate(str(other))
        self.wait_for(lambda: window.current_path == str(other) and not window.pending_restore)
        self.wait_for(lambda: window.files.future is None and window.files.applying is None)
        scans = []

        def scan(*args):
            scans.append(path_key(args[0]))
            return directory_snapshot(*args)

        with QSignalBlocker(window.files.watcher), QSignalBlocker(window.folders.watcher), patch(
                "filevoyager.file_model.directory_snapshot", side_effect=scan):
            window.show_join_dialog(paths=(source,))
            window.join_dialog.folder_name.setText("Joined")
            window.join_dialog.accept()
            self.wait_for(lambda: window.action_future is None)
            self.wait_for(lambda: window.files.rowCount(window.files.index(str(source))) == 0)
            self.wait_for(lambda: window.files.future is None and window.files.applying is None)
        self.assertEqual(scans, [path_key(source)])
        self.assertEqual(window.current_path, str(other))
        self.assertEqual((folder / "Joined/file.txt").read_text(), "content")

    def test_join_selected_folders_from_toolbar_and_menu(self):
        for view_name in ("details", "grid"):
            for trigger in ("toolbar", "menu"):
                with self.subTest(view=view_name, trigger=trigger):
                    folder = self.root / f"join-{view_name}-{trigger}"
                    for name in ("one", "two", "unselected"):
                        (folder / name).mkdir(parents=True)
                        (folder / name / f"{name}.txt").write_text(name)
                    window = ExplorerWindow(str(folder), image_result, preferences=FolderPreferences(
                        QSettings(str(self.root / f"{folder.name}.ini"), QSettings.Format.IniFormat)))
                    window.show()
                    self.addCleanup(window.close)
                    self.wait_for(lambda: window.current_path == str(folder) and not window.pending_restore)
                    self.wait_for(lambda: window.model.rowCount(window.details.rootIndex()) == 3)
                    self.assertFalse(window.join_action.isEnabled())
                    view = getattr(window, view_name)
                    window.switch_view(view)
                    self.wait_for(lambda: not window.pending_restore)
                    for name in ("one", "two"):
                        index = window.model.mapFromSource(window.files.index(str(folder / name)))
                        window.selection.select(index, QItemSelectionModel.SelectionFlag.Select
                                                 | QItemSelectionModel.SelectionFlag.Rows)
                    self.assertTrue(window.join_action.isEnabled())
                    if trigger == "toolbar":
                        toolbar = window.findChild(QToolBar, "itemActionsToolbar")
                        QTest.mouseClick(toolbar.widgetForAction(window.join_action), Qt.MouseButton.LeftButton)
                    else:
                        point = view.visualRect(index).center()
                        QTest.mouseClick(view.viewport(), Qt.MouseButton.RightButton, pos=point)
                        self.app.sendEvent(view.viewport(), QContextMenuEvent(QContextMenuEvent.Reason.Mouse,
                                           point, view.viewport().mapToGlobal(point)))
                        menu = window.item_menus[view]
                        QTest.mouseClick(menu, Qt.MouseButton.LeftButton,
                                         pos=menu.actionGeometry(window.join_action).center())
                    dialog = window.join_dialog
                    self.assertTrue(dialog.isVisible())
                    self.assertEqual(dialog.windowTitle(), "Join to Folder")
                    dialog.folder_name.setText("Joined")
                    QTest.mouseClick(dialog.buttons.button(QDialogButtonBox.StandardButton.Ok),
                                     Qt.MouseButton.LeftButton)
                    self.assertFalse(window.join_action.isEnabled())
                    self.wait_for(lambda: window.action_future is None)
                    self.assertEqual({item.name for item in (folder / "Joined").iterdir()},
                                     {"one.txt", "two.txt"})
                    self.assertEqual((folder / "unselected/unselected.txt").read_text(), "unselected")
                    window.close()

    def test_pack_moves_mouse_selected_files_from_toolbar_and_context_menu(self):
        for view_name in ("details", "grid"):
            for trigger in ("toolbar", "menu", "menu-outside-selection"):
                with self.subTest(view=view_name, trigger=trigger):
                    folder = self.root / f"pack-{view_name}-{trigger}"
                    folder.mkdir()
                    for number in range(5):
                        (folder / f"{number}.txt").write_text(str(number))
                    window = ExplorerWindow(str(folder), image_result, preferences=FolderPreferences(
                        QSettings(str(self.root / f"{folder.name}.ini"), QSettings.Format.IniFormat)))
                    window.show()
                    self.addCleanup(window.close)
                    self.wait_for(lambda: window.current_path == str(folder) and not window.pending_restore)
                    self.wait_for(lambda: window.model.rowCount(window.details.rootIndex()) == 5)
                    window.preview_dock.hide()
                    window.similarity_dock.hide()
                    view = getattr(window, view_name)
                    window.switch_view(view)
                    self.wait_for(lambda: not window.pending_restore)
                    window.activateWindow()
                    for row, modifiers in ((0, Qt.KeyboardModifier.NoModifier),
                                           (2, Qt.KeyboardModifier.ShiftModifier),
                                           (4, Qt.KeyboardModifier.ControlModifier)):
                        index = window.model.index(row, 0, view.rootIndex())
                        view.scrollTo(index)
                        QTest.mouseClick(view.viewport(), Qt.MouseButton.LeftButton,
                                         modifiers, view.visualRect(index).center())
                    expected = {folder / f"{row}.txt" for row in (0, 1, 2, 4)}
                    self.assertEqual(set(window.selected_item_paths()), expected)
                    if trigger == "toolbar":
                        toolbar = window.findChild(QToolBar, "itemActionsToolbar")
                        QTest.mouseClick(toolbar.widgetForAction(window.pack_action), Qt.MouseButton.LeftButton)
                    else:
                        row = 3 if trigger == "menu-outside-selection" else 1
                        point = view.visualRect(window.model.index(row, 0, view.rootIndex())).center()
                        QTest.mouseClick(view.viewport(), Qt.MouseButton.RightButton, pos=point)
                        self.app.sendEvent(view.viewport(), QContextMenuEvent(QContextMenuEvent.Reason.Mouse,
                                           point, view.viewport().mapToGlobal(point)))
                        menu = window.item_menus[view]
                        QTest.mouseClick(menu, Qt.MouseButton.LeftButton,
                                         pos=menu.actionGeometry(window.pack_action).center())
                    dialog = window.pack_dialog
                    self.assertTrue(dialog.isVisible())
                    dialog.folder_name.setText("Packed")
                    QTest.mouseClick(dialog.buttons.button(QDialogButtonBox.StandardButton.Ok),
                                     Qt.MouseButton.LeftButton)
                    self.wait_for(lambda: window.action_future is None)
                    self.assertEqual({path.name for path in (folder / "Packed").iterdir()},
                                     {path.name for path in expected})
                    self.assertTrue(all(not path.exists() for path in expected))
                    self.assertTrue((folder / "3.txt").exists())
                    window.close()

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
            self.assertEqual(menu.actions(), [window.flatten_action, window.pack_action,
                                             window.join_action, window.rename_actions[view]])
            self.assertEqual(len(window.selection.selectedRows()), 2)
            self.assertFalse(window.flatten_action.isEnabled())
            self.assertFalse(window.rename_actions[view].isEnabled())
            menu.close()
            point = view.visualRect(indexes[2]).center()
            QTest.mouseClick(view.viewport(), Qt.MouseButton.RightButton, pos=point)
            self.app.sendEvent(view.viewport(), QContextMenuEvent(QContextMenuEvent.Reason.Mouse,
                               point, view.viewport().mapToGlobal(point)))
            self.assertEqual(window.selection.selectedRows(), indexes[:2])
            self.assertFalse(window.rename_actions[view].isEnabled())
            menu.close()
            QTest.mouseClick(view.viewport(), Qt.MouseButton.LeftButton, pos=point)
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
