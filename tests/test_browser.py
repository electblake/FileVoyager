"""Qt integration tests use synthetic image results, never a production fallback."""

from pathlib import Path
import threading
import time
import unittest
import json
import configparser
from unittest.mock import patch

import qt_themes
from PySide6.QtCore import QItemSelection, QItemSelectionModel, QSettings, Qt
from PySide6.QtGui import QImage
from PySide6.QtTest import QSignalSpy, QTest
from PySide6.QtWidgets import QDialogButtonBox, QLineEdit, QMessageBox, QWidget
from support import QtCase

from filevoyager.thumbnails import ThumbnailCache, ThumbnailKey
from filevoyager.window import ExplorerWindow
from filevoyager.directory_tree import path_key, scan_directories
from filevoyager.preferences import FolderPreferences


def image_result(path, width, height):
    image = QImage(width, height, QImage.Format.Format_ARGB32_Premultiplied)
    image.fill(Qt.GlobalColor.darkCyan)
    return image


class BrowserTests(QtCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
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

    def open_window(self, loader=image_result):
        preferences = FolderPreferences(QSettings(str(self.root / (self.id() + ".ini")), QSettings.Format.IniFormat))
        preferences.save(str(self.first), preferences.load(str(self.first), False))
        window = ExplorerWindow(str(self.first), loader, preferences=preferences)
        window.show()
        self.addCleanup(window.close)
        self.wait_for(lambda: window.current_path == str(self.first))
        self.wait_for(lambda: window.model.rowCount(window.details.rootIndex()) == 601)
        return window

    def test_help_and_quit_menu_lifecycle(self):
        window = self.open_window()
        window.menuBar().actions()[3].menu().actions()[0].trigger()
        dialog = window.update_dialog
        self.assertTrue(dialog.isVisible())
        self.assertIsNone(dialog.future)
        self.assertTrue(dialog.check_button.isEnabled())
        dialog.reject()
        window.menuBar().actions()[3].menu().actions()[0].trigger()
        self.assertIsNot(window.update_dialog, dialog)
        self.assertTrue(window.update_dialog.isVisible())
        window.update_dialog.reject()
        menus = window.menuBar().actions()
        self.assertEqual([action.text() for action in menus], ["&File", "&Edit", "&View", "&Help"])
        settings = window.preferences.settings
        settings.setValue("quit-test", "saved")
        with patch.object(settings, "sync", wraps=settings.sync) as sync:
            menus[0].menu().actions()[0].trigger()
            self.assertGreaterEqual(sync.call_count, 1)
        self.assertFalse(window.isVisible())
        self.assertIn("quit-test=saved", Path(settings.fileName()).read_text())

    def test_theme_apply_close_and_restore(self):
        window = self.open_window()
        initial = self.app.palette()
        window.menuBar().actions()[2].menu().actions()[0].trigger()
        dialog = window.theme_dialog
        self.assertTrue(dialog.isVisible())
        self.assertEqual(dialog.theme.count(), len(qt_themes.get_themes()))
        dialog.theme.setCurrentText("nord")
        self.assertEqual(self.app.palette(), initial)
        self.assertFalse(window.preferences.settings.contains("appearance/theme"))
        QTest.mouseClick(dialog.buttons.button(QDialogButtonBox.StandardButton.Apply),
                         Qt.MouseButton.LeftButton)
        self.app.processEvents()
        self.assertTrue(dialog.isVisible())
        self.assertEqual(qt_themes.get_theme(), qt_themes.get_theme("nord"))
        self.assertNotEqual(self.app.palette(), initial)
        for widget in (window.tree, window.details, window.grid, window.preview_dock,
                       window.similarity_dock, dialog.theme):
            self.assertEqual(widget.palette(), self.app.palette())
        self.assertEqual(self.app.styleSheet(), "")
        self.assertTrue(all(widget.styleSheet() == "" for widget in window.findChildren(QWidget)))
        stored = QSettings(window.preferences.settings.fileName(), QSettings.Format.IniFormat)
        self.assertEqual(stored.value("appearance/theme"), "nord")
        dialog.theme.setCurrentText("github_light")
        QTest.mouseClick(dialog.buttons.button(QDialogButtonBox.StandardButton.Close),
                         Qt.MouseButton.LeftButton)
        window.show_theme()
        self.assertEqual(window.theme_dialog.theme.currentText(), "nord")
        window.theme_dialog.reject()
        window.close()
        qt_themes.set_theme("github_light")
        reopened = ExplorerWindow(str(self.first), image_result, preferences=FolderPreferences(stored))
        self.addCleanup(reopened.close)
        self.assertEqual(qt_themes.get_theme(), qt_themes.get_theme("nord"))

    def test_theme_switching_preserves_browser_state_and_style(self):
        window = self.open_window()
        window.view_actions[window.grid].trigger()
        self.wait_for(lambda: window.grid.layout_complete and not window.pending_restore)
        index = window.model.index(300, 0, window.grid.rootIndex())
        window.selection.select(index, QItemSelectionModel.SelectionFlag.ClearAndSelect
                                | QItemSelectionModel.SelectionFlag.Rows)
        window.grid.scrollTo(index)
        self.app.processEvents()
        window.show_theme()
        self.app.processEvents()
        dialog = window.theme_dialog
        position = window.grid.verticalScrollBar().value()
        selected = window.selection.selectedIndexes()
        generation = window.thumbnails.generation
        style = self.app.style()
        resets = QSignalSpy(window.model.modelReset)
        for name in sorted(window.themes):
            with self.subTest(theme=name):
                dialog.theme.setCurrentText(name)
                QTest.mouseClick(dialog.buttons.button(QDialogButtonBox.StandardButton.Apply),
                                 Qt.MouseButton.LeftButton)
                self.app.processEvents()
                self.assertEqual(qt_themes.get_theme(), window.themes[name])
                self.assertEqual(window.grid.verticalScrollBar().value(), position)
                self.assertEqual(window.selection.selectedIndexes(), selected)
                self.assertEqual(window.thumbnails.generation, generation)
                self.assertEqual(resets.count(), 0)
                self.assertIs(self.app.style(), style)
        dialog.reject()

    def test_app_state_restores_after_reopening(self):
        window = self.open_window()
        window.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, window.similarity_dock)
        window.preview_dock.hide()
        window.resize(760, 600)
        window.move(10, 50)
        window.centralWidget().setSizes([180, 520])
        window.details.setColumnWidth(0, 275)
        window.details.horizontalHeader().moveSection(1, 2)
        window.details.sortByColumn(0, Qt.SortOrder.DescendingOrder)
        window.similarity_dock.eps.setValue(0.4321)
        window.similarity_dock.min_samples.setValue(7)
        weights = [0.5, 0.0, 1.5, 2.0, 2.5, 3.0]
        for spin, value in zip(window.similarity_dock.weights, weights):
            spin.setValue(value)
        window.navigate(str(self.second))
        self.wait_for(lambda: window.current_path == str(self.second) and not window.pending_restore)
        window.travel(-1)
        self.wait_for(lambda: window.current_path == str(self.first) and not window.pending_restore)
        geometry = window.geometry()
        splitter_sizes = window.centralWidget().sizes()
        filename = window.preferences.settings.fileName()
        window.close()

        preferences = FolderPreferences(QSettings(filename, QSettings.Format.IniFormat))
        reopened = ExplorerWindow(None, image_result, preferences=preferences)
        reopened.show()
        self.addCleanup(reopened.close)
        self.wait_for(lambda: reopened.current_path == str(self.first) and not reopened.pending_restore)
        self.assertEqual(reopened.geometry(), geometry)
        self.assertEqual(reopened.centralWidget().sizes(), splitter_sizes)
        self.assertEqual(reopened.dockWidgetArea(reopened.similarity_dock), Qt.DockWidgetArea.LeftDockWidgetArea)
        self.assertFalse(reopened.preview_dock.isVisible())
        self.assertEqual(reopened.details.columnWidth(0), 275)
        self.assertEqual(reopened.details.horizontalHeader().visualIndex(1), 2)
        self.assertEqual(reopened.details.horizontalHeader().sortIndicatorSection(), 0)
        self.assertEqual(reopened.details.horizontalHeader().sortIndicatorOrder(), Qt.SortOrder.DescendingOrder)
        self.wait_for(lambda: reopened.model.rowCount(reopened.details.rootIndex()) == 601)
        names = [reopened.model.index(row, 0, reopened.details.rootIndex()).data()
                 for row in range(601)]
        self.assertLess(names.index("image-0599.png"), names.index("image-0000.png"))
        self.assertEqual(reopened.similarity_dock.eps.value(), 0.4321)
        self.assertEqual(reopened.similarity_dock.min_samples.value(), 7)
        self.assertEqual([spin.value() for spin in reopened.similarity_dock.weights], weights)
        self.assertEqual(reopened.history, [str(self.first), str(self.second)])
        self.assertEqual(reopened.history_position, 0)
        self.assertTrue(reopened.forward_action.isEnabled())
        reopened.travel(1)
        self.wait_for(lambda: reopened.current_path == str(self.second))

    def test_keyboard_shortcuts_menu_persists_and_rebinds_rename(self):
        window = self.open_window()
        help_menu = window.menuBar().actions()[3].menu()
        help_menu.actions()[1].trigger()
        dialog = window.shortcuts_dialog
        self.assertTrue(dialog.isVisible())
        self.assertEqual(dialog.model.columnCount(), 3)
        dialog.search.setText("Rename")
        self.assertEqual(dialog.proxy.rowCount(), 1)
        self.assertEqual(dialog.proxy.index(0, 1).data(), "F2")
        dialog.proxy.setData(dialog.proxy.index(0, 2), "Ctrl+Alt+R")
        dialog.accept()
        filename = window.preferences.settings.fileName()
        window.close()
        reopened = ExplorerWindow(str(self.first), image_result, preferences=FolderPreferences(
            QSettings(filename, QSettings.Format.IniFormat)))
        reopened.show()
        self.addCleanup(reopened.close)
        self.wait_for(lambda: reopened.current_path == str(self.first) and not reopened.pending_restore)
        self.wait_for(lambda: reopened.model.rowCount(reopened.details.rootIndex()) == 601)
        for view in (reopened.details, reopened.grid):
            with self.subTest(view=type(view).__name__):
                reopened.switch_view(view)
                self.wait_for(lambda: not reopened.pending_restore)
                index = reopened.model.index(1, 0, view.rootIndex())
                reopened.selection.setCurrentIndex(index, QItemSelectionModel.SelectionFlag.ClearAndSelect
                                                    | QItemSelectionModel.SelectionFlag.Rows)
                reopened.activateWindow()
                view.setFocus()
                self.wait_for(view.hasFocus)
                QTest.keyClick(view, Qt.Key.Key_F2)
                self.assertIsNone(view.findChild(QLineEdit))
                QTest.keyClick(view, Qt.Key.Key_R,
                               Qt.KeyboardModifier.ControlModifier | Qt.KeyboardModifier.AltModifier)
                editor = view.findChild(QLineEdit)
                self.assertTrue(editor.isVisible())
                QTest.keyClick(editor, Qt.Key.Key_Escape)
                self.wait_for(lambda: view.findChild(QLineEdit) is None)
    def test_maximized_window_state_restores(self):
        window = self.open_window()
        window.showMaximized()
        self.wait_for(window.isMaximized)
        filename = window.preferences.settings.fileName()
        window.close()
        preferences = FolderPreferences(QSettings(filename, QSettings.Format.IniFormat))
        reopened = ExplorerWindow(None, image_result, preferences=preferences)
        reopened.show()
        self.addCleanup(reopened.close)
        self.wait_for(lambda: reopened.current_path == str(self.first))
        self.assertTrue(reopened.isMaximized())

    def test_large_selection_updates_without_expanding_selected_rows(self):
        window = self.open_window()
        root = window.details.rootIndex()
        first = window.model.index(0, 0, root)
        last = window.model.index(600, 3, root)
        window.selection.setCurrentIndex(first, QItemSelectionModel.SelectionFlag.NoUpdate)
        with patch.object(window.selection, "selectedRows", side_effect=AssertionError("Expanded entire selection")):
            window.selection.select(QItemSelection(first, last), QItemSelectionModel.SelectionFlag.Select)
            self.assertIn("601 selected", window.status.text())
            self.assertTrue(window.pack_action.isEnabled())
            self.assertFalse(window.flatten_action.isEnabled())
            self.assertTrue(all(not action.isEnabled() for action in window.rename_actions.values()))
            self.assertIsNone(window.similarity_dock.reference)
            window.selection.select(QItemSelection(window.model.index(2, 0, root), last),
                                    QItemSelectionModel.SelectionFlag.Deselect)
            self.assertIn("2 selected", window.status.text())
            self.assertEqual(Path(window.similarity_dock.reference).name, "image-0000.png")
            window.selection.select(first, QItemSelectionModel.SelectionFlag.Deselect
                                     | QItemSelectionModel.SelectionFlag.Rows)
            self.assertIn("1 selected", window.status.text())
            self.assertTrue(all(action.isEnabled() for action in window.rename_actions.values()))
            self.assertEqual(Path(window.preview_dock.path).name, "image-0000.png")

    def test_modifier_click_selection_in_details_and_grid(self):
        window = self.open_window()
        window.preview_dock.hide()
        window.similarity_dock.hide()
        modifiers = Qt.KeyboardModifier
        for view in (window.details, window.grid):
            window.switch_view(view)
            self.wait_for(lambda: not window.pending_restore)
            # Cross grid rows, then shrink/reverse the range and add another.
            for row, modifier, expected in (
                (1, modifiers.NoModifier, {1}),
                (8, modifiers.ControlModifier, {1, 8}),
                (8, modifiers.ControlModifier, {1}),
                (2, modifiers.NoModifier, {2}),
                (9, modifiers.ShiftModifier, set(range(2, 10))),
                (5, modifiers.ShiftModifier, set(range(2, 6))),
                (0, modifiers.ShiftModifier, {0, 1, 2}),
                (7, modifiers.ControlModifier, {0, 1, 2, 7}),
                (10, modifiers.ControlModifier | modifiers.ShiftModifier,
                 {0, 1, 2, 7, 8, 9, 10}),
                (4, modifiers.NoModifier, {4}),
            ):
                with self.subTest(view=type(view).__name__, row=row, modifier=modifier):
                    index = window.model.index(row, 0, view.rootIndex())
                    view.scrollTo(index)
                    point = view.visualRect(index).center()
                    self.assertEqual(view.indexAt(point), index)
                    QTest.mouseClick(view.viewport(), Qt.MouseButton.LeftButton, modifier, point)
                    self.assertEqual({item.row() for item in window.selection.selectedRows(0)}, expected)
                    self.assertEqual(window.selection.currentIndex().row(), row)

    def test_f2_renames_and_escape_cancels_in_details_and_grid(self):
        folder = self.root / "rename"
        folder.mkdir()
        original = folder / "original.txt"
        original.write_text("rename contents", encoding="utf-8")
        window = self.open_window()
        window.navigate(str(folder))
        self.wait_for(lambda: window.current_path == str(folder) and not window.pending_restore)
        self.wait_for(lambda: window.model.rowCount(window.details.rootIndex()) == 1)
        for number, view in enumerate((window.details, window.grid)):
            with self.subTest(view=type(view).__name__):
                window.switch_view(view)
                self.wait_for(lambda: not window.pending_restore)
                index = window.model.index(0, 0, view.rootIndex())
                window.selection.setCurrentIndex(index, QItemSelectionModel.SelectionFlag.ClearAndSelect
                                                 | QItemSelectionModel.SelectionFlag.Rows)
                window.activateWindow()
                view.setFocus()
                self.wait_for(view.hasFocus)
                QTest.keyClick(view, Qt.Key.Key_F2)
                editor = view.findChild(QLineEdit)
                self.assertTrue(editor.isVisible())
                editor.selectAll()
                QTest.keyClicks(editor, "cancelled.txt")
                QTest.keyClick(editor, Qt.Key.Key_Escape)
                self.assertTrue(original.exists())
                self.assertFalse((folder / "cancelled.txt").exists())
                self.wait_for(lambda: view.findChild(QLineEdit) is None)
                QTest.keyClick(view, Qt.Key.Key_F2)
                editor = view.findChild(QLineEdit)
                editor.selectAll()
                renamed = folder / f"renamed-{number}.txt"
                QTest.keyClicks(editor, renamed.name)
                QTest.keyClick(editor, Qt.Key.Key_Return)
                self.wait_for(renamed.exists)
                self.assertFalse(original.exists())
                self.assertEqual(renamed.read_text(encoding="utf-8"), "rename contents")
                self.wait_for(lambda: window.model.index(0, 0, view.rootIndex()).data() == renamed.name)
                self.assertEqual(Path(window.preview_dock.path), renamed)
                original = renamed

    def test_folder_rename_conflict_prompts_before_merging(self):
        folder = self.root / "folder-rename-conflict"
        source, destination = folder / "Bust", folder / "Busts"
        source.mkdir(parents=True)
        destination.mkdir()
        (source / "source.txt").write_text("source")
        (destination / "destination.txt").write_text("destination")
        window = self.open_window()
        window.navigate(str(folder))
        self.wait_for(lambda: window.current_path == str(folder) and not window.pending_restore)
        self.wait_for(lambda: window.model.rowCount(window.details.rootIndex()) == 2)
        for view, answer in ((window.details, QMessageBox.StandardButton.No),
                             (window.grid, QMessageBox.StandardButton.Yes)):
            window.switch_view(view)
            self.wait_for(lambda: not window.pending_restore)
            index = window.model.mapFromSource(window.files.index(str(source)))
            window.selection.setCurrentIndex(index, QItemSelectionModel.SelectionFlag.ClearAndSelect
                                             | QItemSelectionModel.SelectionFlag.Rows)
            window.activateWindow()
            view.setFocus()
            self.wait_for(view.hasFocus)
            QTest.keyClick(view, Qt.Key.Key_F2)
            editor = view.findChild(QLineEdit)
            editor.selectAll()
            QTest.keyClicks(editor, destination.name)
            QTest.keyClick(editor, Qt.Key.Key_Return)
            self.wait_for(lambda: window.folder_merge.dialog is not None
                          and window.folder_merge.dialog.isVisible())
            self.assertEqual(window.folder_merge.dialog.windowTitle(), "Confirm Folder Replace")
            self.assertTrue((source / "source.txt").exists())
            self.assertFalse((destination / "source.txt").exists())
            window.folder_merge.dialog.button(answer).click()
            self.wait_for(lambda: window.action_future is None)
            window.folder_merge.dialog = None
        self.assertFalse(source.exists())
        self.assertEqual((destination / "source.txt").read_text(), "source")
        self.assertEqual((destination / "destination.txt").read_text(), "destination")
        self.wait_for(lambda: window.model.rowCount(window.details.rootIndex()) == 1)

    def test_f2_requires_one_selection_and_item_view_focus(self):
        window = self.open_window()
        window.activateWindow()
        for view in (window.details, window.grid):
            with self.subTest(view=type(view).__name__):
                window.switch_view(view)
                self.wait_for(lambda: not window.pending_restore)
                view.setFocus()
                self.wait_for(view.hasFocus)
                window.selection.clearSelection()
                QTest.keyClick(view, Qt.Key.Key_F2)
                self.assertIsNone(view.findChild(QLineEdit))
                for row in (1, 2):
                    index = window.model.index(row, 0, view.rootIndex())
                    window.selection.select(index, QItemSelectionModel.SelectionFlag.Select
                                             | QItemSelectionModel.SelectionFlag.Rows)
                QTest.keyClick(view, Qt.Key.Key_F2)
                self.assertIsNone(view.findChild(QLineEdit))
                window.selection.setCurrentIndex(index, QItemSelectionModel.SelectionFlag.ClearAndSelect
                                                 | QItemSelectionModel.SelectionFlag.Rows)
                window.address.setFocus()
                self.wait_for(window.address.hasFocus)
                QTest.keyClick(window.address, Qt.Key.Key_F2)
                self.assertIsNone(view.findChild(QLineEdit))

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

        # Read the persisted INI directly rather than starting another Python/Qt.
        saved = configparser.ConfigParser()
        saved.read(filename, encoding="utf-8")
        key = window.preferences.key(str(self.first)).split("/", 1)[1]
        state = json.loads(json.loads(saved["folders"][key]))
        self.assertEqual(state["grid"][0], 20000)
        self.assertEqual(state["details"][0], 120)

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

    def test_reopening_current_grid_preserves_layout_and_scroll(self):
        window = self.open_window()
        window.switch_view(window.grid)
        self.wait_for(lambda: window.grid.layout_complete and not window.pending_restore)
        window.grid.verticalScrollBar().setValue(200)
        self.app.processEvents()
        position = window.grid.verticalScrollBar().value()
        with patch.object(window.grid, 'doItemsLayout', wraps=window.grid.doItemsLayout) as layout:
            window.navigate(str(self.first))
            self.wait_for(lambda: window.navigation_future is None and not window.pending_restore)
            QTest.qWait(50)
            self.assertEqual(window.grid.verticalScrollBar().value(), position)
            self.assertTrue(window.grid.layout_complete)
            layout.assert_not_called()

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
