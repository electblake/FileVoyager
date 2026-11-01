from unittest.mock import Mock, patch

from PySide6.QtCore import QItemSelectionModel, QMimeData, QSettings, QUrl, Qt
from PySide6.QtTest import QTest

from support import QtCase
from test_browser import image_result
from filevoyager.clipboard import DROP_EFFECT
from filevoyager.preferences import FolderPreferences
from filevoyager.window import ExplorerWindow


class ClipboardTests(QtCase):
    def setUp(self):
        self.folder = self.root / self._testMethodName
        self.folder.mkdir()
        self.source = self.folder / "source.txt"
        self.source.write_text("contents")
        self.destination = self.folder / "destination"
        self.destination.mkdir()
        self.window = ExplorerWindow(str(self.folder), image_result, preferences=FolderPreferences(
            QSettings(str(self.root / f"{self._testMethodName}.ini"), QSettings.Format.IniFormat)))
        self.window.show()
        self.addCleanup(self.window.close)
        self.window.activateWindow()
        self.wait_for(lambda: self.window.current_path == str(self.folder) and not self.window.pending_restore)
        self.wait_for(lambda: self.window.model.rowCount(self.window.details.rootIndex()) == 2)
        self.clip = self.window.file_clipboard
        self.clip.clipboard.clear()
        self.addCleanup(self.clip.clipboard.clear)

    def select(self, view, path):
        index = self.window.model.mapFromSource(self.window.files.index(str(path)))
        self.window.selection.setCurrentIndex(index, QItemSelectionModel.SelectionFlag.ClearAndSelect
                                             | QItemSelectionModel.SelectionFlag.Rows)
        view.setFocus()
        return index

    def paste(self, destination):
        self.clip.paste(destination)
        self.wait_for(lambda: self.window.action_future is None)

    def test_copy_shortcuts_in_both_views_and_same_folder_duplicates(self):
        for view in (self.window.details, self.window.grid):
            self.window.switch_view(view)
            self.select(view, self.source)
            QTest.keyClick(view, Qt.Key.Key_C, Qt.KeyboardModifier.ControlModifier)
            self.assertEqual(self.clip.snapshot(), ((self.source,), False))
            self.assertEqual(bytes(self.clip.clipboard.mimeData().data(DROP_EFFECT)), b"\x01\0\0\0")
            QTest.keyClick(view, Qt.Key.Key_V, Qt.KeyboardModifier.ControlModifier)
            self.wait_for(lambda: self.window.action_future is None)
        self.assertEqual((self.folder / "source - Copy.txt").read_text(), "contents")
        self.assertEqual((self.folder / "source - Copy (2).txt").read_text(), "contents")
        self.assertEqual(self.source.read_text(), "contents")

    def test_cut_shortcut_moves_and_clears_clipboard_after_success(self):
        view = self.window.details
        self.select(view, self.source)
        QTest.keyClick(view, Qt.Key.Key_X, Qt.KeyboardModifier.ControlModifier)
        self.assertTrue(self.source.exists())
        self.assertEqual(self.clip.snapshot(), ((self.source,), True))
        self.paste(self.destination)
        self.assertFalse(self.source.exists())
        self.assertEqual((self.destination / self.source.name).read_text(), "contents")
        self.assertEqual(self.clip.snapshot(), ((), False))

    def test_external_file_urls_and_conflict_skip_replace_cancel(self):
        target = self.destination / self.source.name
        target.write_text("old")
        mime = QMimeData()
        mime.setUrls([QUrl.fromLocalFile(str(self.source))])
        mime.setData(DROP_EFFECT, b"\x02\0\0\0")
        self.clip.clipboard.setMimeData(mime)
        for choice in ("skip", "cancel", "replace"):
            self.window.folder_merge.ask = Mock(return_value=choice)
            self.paste(self.destination)
            self.window.folder_merge.ask.assert_called_once_with(self.source, target, False)
            if choice != "replace":
                self.assertTrue(self.source.exists())
                self.assertEqual(target.read_text(), "old")
                self.assertEqual(self.clip.snapshot(), ((self.source,), True))
        self.assertEqual(target.read_text(), "contents")
        self.assertEqual(self.clip.snapshot(), ((), False))

    def test_folder_and_background_context_menu_paste_destinations(self):
        self.clip.put((self.source,), False)
        view = self.window.details
        index = self.select(view, self.destination)
        self.window.show_item_menu(view, view.visualRect(index).center())
        menu = self.window.item_menus[view]
        self.assertTrue(menu.actions()[2].isEnabled())
        menu.actions()[2].trigger()
        menu.close()
        self.wait_for(lambda: self.window.action_future is None)
        self.assertEqual((self.destination / self.source.name).read_text(), "contents")
        self.window.show_item_menu(view, view.viewport().rect().bottomRight())
        menu = self.window.background_menus[view]
        self.assertTrue(menu.isVisible())
        self.assertEqual(menu.actions(), [self.clip.actions[view][2]])
        menu.actions()[0].trigger()
        menu.close()
        self.wait_for(lambda: self.window.action_future is None)
        self.assertTrue((self.folder / "source - Copy.txt").exists())

    def test_text_clipboard_and_recursive_folder_paste_are_disabled(self):
        self.clip.clipboard.setText("text")
        self.assertFalse(self.clip.actions[self.window.details][2].isEnabled())
        self.clip.put((self.folder,), False)
        self.assertFalse(self.clip.can_paste(self.destination))
        self.assertFalse(self.clip.actions[self.window.details][2].isEnabled())

    def test_address_text_shortcuts_do_not_cut_files(self):
        self.select(self.window.details, self.source)
        address = self.window.address
        address.setFocus()
        address.selectAll()
        QTest.keyClick(address, Qt.Key.Key_C, Qt.KeyboardModifier.ControlModifier)
        self.assertEqual(self.clip.clipboard.text(), str(self.folder))
        self.assertEqual(self.clip.snapshot(), ((), False))

    def test_new_clipboard_content_is_preserved_when_move_finishes(self):
        self.clip.put((self.source,), True)
        self.clip.paste(self.destination)
        self.clip.clipboard.setText("new clipboard")
        self.wait_for(lambda: self.window.action_future is None)
        self.assertEqual(self.clip.clipboard.text(), "new clipboard")

    def test_tree_shortcuts_copy_folder_and_paste_into_selected_tree_folder(self):
        tree = self.window.tree
        self.wait_for(lambda: self.window.folders.file_path(tree.currentIndex()) == str(self.folder))
        tree.setFocus()
        QTest.keyClick(tree, Qt.Key.Key_C, Qt.KeyboardModifier.ControlModifier)
        self.assertEqual(self.clip.snapshot(), ((self.folder,), False))
        self.clip.put((self.source,), False)
        tree.expand(tree.currentIndex())
        parent = tree.currentIndex()
        self.wait_for(lambda: self.window.folders.rowCount(parent) == 1
                      and self.window.folders.file_path(self.window.folders.index(0, 0, parent))
                      == str(self.destination))
        tree.setCurrentIndex(self.window.folders.index(0, 0, parent))
        QTest.keyClick(tree, Qt.Key.Key_V, Qt.KeyboardModifier.ControlModifier)
        self.wait_for(lambda: self.window.action_future is None)
        self.assertTrue((self.destination / self.source.name).exists())
        self.assertTrue(self.source.exists())

    def test_copy_folder_merge_uses_shared_rules_and_keeps_source(self):
        source = self.folder / "nested"
        source.mkdir()
        (source / "file.txt").write_text("new")
        target = self.destination / source.name
        target.mkdir()
        (target / "file.txt").write_text("old")
        self.window.folder_merge.ask = Mock(side_effect=["merge", "replace"])
        self.clip.put((source,), False)
        self.paste(self.destination)
        self.assertEqual(self.window.folder_merge.ask.call_count, 2)
        self.assertEqual((source / "file.txt").read_text(), "new")
        self.assertEqual((target / "file.txt").read_text(), "new")

    def test_action_state_updates_do_not_expand_file_selection(self):
        self.select(self.window.details, self.source)
        with patch.object(self.window, "selected_item_paths", side_effect=AssertionError("expanded selection")):
            self.clip.update()
        self.assertTrue(self.clip.actions[self.window.details][0].isEnabled())

    def test_move_previously_opened_folder_does_not_rescan_deleted_source(self):
        source = self.folder / "visited"
        source.mkdir()
        (source / "child.txt").write_text("contents")
        self.window.navigate(str(source))
        self.wait_for(lambda: self.window.current_path == str(source) and not self.window.pending_restore)
        self.wait_for(lambda: self.window.files.current.loaded)
        self.window.navigate(str(self.folder))
        self.wait_for(lambda: self.window.current_path == str(self.folder) and not self.window.pending_restore)
        self.clip.put((source,), True)
        with patch.object(self.window.files, "request", wraps=self.window.files.request) as request:
            self.paste(self.destination)
            self.assertFalse(any(call.args[0].path == str(source) for call in request.call_args_list))
        self.assertFalse(source.exists())
        self.assertEqual((self.destination / "visited/child.txt").read_text(), "contents")

    def test_move_current_folder_navigates_to_parent(self):
        source = self.folder / "current"
        source.mkdir()
        self.window.navigate(str(source))
        self.wait_for(lambda: self.window.current_path == str(source) and not self.window.pending_restore)
        self.wait_for(lambda: self.window.files.current.loaded)
        self.clip.put((source,), True)
        self.paste(self.destination)
        self.wait_for(lambda: self.window.current_path == str(self.folder) and not self.window.pending_restore)
