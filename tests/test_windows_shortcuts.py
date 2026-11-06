from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import shutil
import threading
from unittest.mock import patch

from comtypes.client import CreateObject

from PySide6.QtCore import QPersistentModelIndex, QSettings, Qt
from PySide6.QtTest import QTest
from PySide6.QtGui import QIcon

from support import QtCase
from test_browser import image_result
from filevoyager.link_drag import create_shortcuts
from filevoyager.directory_tree import DirectoryTreeModel, path_key, scan_directories
from filevoyager.preferences import FolderPreferences
from filevoyager.window import ExplorerWindow
from filevoyager.file_model import directory_snapshot
from filevoyager.windows_shortcuts import folder_shortcut_targets


class WindowsShortcutTests(QtCase):
    def test_deleted_shortcut_target_remains_a_file_not_a_folder(self):
        root = self.root / "broken-link"
        root.mkdir()
        target = root / "target"
        target.mkdir()
        with ThreadPoolExecutor(max_workers=1) as worker:
            worker.submit(create_shortcuts, (target,), root).result()
            target.rmdir()
            records = worker.submit(directory_snapshot, str(root), (), 0, False, True).result()[0]
            self.assertEqual(len(records), 1)
            self.assertEqual(records[0].kind, "Shortcut")
            self.assertEqual(records[0].folder_target, "")
            self.assertEqual(worker.submit(scan_directories, str(root)).result(), [])
            target.mkdir()
            records = worker.submit(directory_snapshot, str(root), (), 0, False, True).result()[0]
            link = next(record for record in records if record.name.endswith(".lnk"))
            self.assertEqual(link.folder_target, str(target))

    def test_shortcut_cache_reuses_unchanged_links_and_plain_files_use_no_shell(self):
        root = self.root / "batch"
        root.mkdir()
        target = root / "folder"
        target.mkdir()
        with ThreadPoolExecutor(max_workers=1) as worker:
            worker.submit(create_shortcuts, (target,), root).result()
            original = root / "folder - Shortcut.lnk"
            for number in range(10):
                shutil.copyfile(original, root / f"copy-{number}.lnk")
            threads = []
            def create(*args, **kwargs):
                threads.append(threading.get_ident())
                return CreateObject(*args, **kwargs)
            with patch("filevoyager.windows_shortcuts.CreateObject", side_effect=create) as shell:
                records = worker.submit(directory_snapshot, str(root), (), 0, False, True).result()[0]
                self.assertEqual(shell.call_count, 11)
                self.assertEqual(sum(bool(record.folder_target) for record in records), 11)
                worker.submit(directory_snapshot, str(root), (), 0, False, True).result()
                self.assertEqual(shell.call_count, 11)
                worker.submit(directory_snapshot, str(target), (), 0, False, True).result()
                self.assertEqual(shell.call_count, 11)
            self.assertTrue(all(thread != threading.get_ident() for thread in threads))
            original.unlink()
            with self.assertRaises(FileNotFoundError):
                worker.submit(folder_shortcut_targets, [str(original)]).result()

    def test_retarget_shortcut_replaces_subtree_and_releases_old_watch(self):
        root = self.root / "retarget"
        root.mkdir()
        first, second = root / "first", root / "second"
        (first / "old child").mkdir(parents=True)
        (second / "new child").mkdir(parents=True)
        with ThreadPoolExecutor(max_workers=1) as worker:
            worker.submit(create_shortcuts, (first,), root).result()
        link = root / "first - Shortcut.lnk"
        window = ExplorerWindow(str(root), image_result, preferences=FolderPreferences(
            QSettings(str(root / "prefs.ini"), QSettings.Format.IniFormat)))
        window.show()
        self.addCleanup(window.close)
        self.wait_for(lambda: path_key(root) in window.folders.nodes)
        window.tree.expand(window.folders.index_for_path(str(root)))
        self.wait_for(lambda: path_key(link) in window.folders.nodes)
        window.tree.expand(window.folders.index_for_path(str(link)))
        self.wait_for(lambda: path_key(link / "old child") in window.folders.nodes)
        old = QPersistentModelIndex(window.folders.index_for_path(str(link / "old child")))
        shortcut = CreateObject("WScript.Shell", dynamic=True).CreateShortcut(str(link))
        shortcut.TargetPath = str(second)
        shortcut.Save()
        del shortcut
        window.refresh_action.trigger()
        self.wait_for(lambda: window.folders.navigation_path(window.folders.index_for_path(str(link))) == str(second))
        self.wait_for(lambda: window.files.navigation_path(window.files.index(str(link))) == str(second))
        self.assertFalse(old.isValid())
        self.assertNotIn(path_key(first), window.folders.watched_nodes)
        window.tree.expand(window.folders.index_for_path(str(link)))
        self.wait_for(lambda: path_key(link / "new child") in window.folders.nodes)

    def test_shortcut_paste_drop_copy_and_folder_only_actions(self):
        root = self.root / "actions"
        root.mkdir()
        target = self.root / "action-target"
        target.mkdir()
        with ThreadPoolExecutor(max_workers=1) as worker:
            worker.submit(create_shortcuts, (target,), root).result()
        link = root / "action-target - Shortcut.lnk"
        window = ExplorerWindow(str(root), image_result, preferences=FolderPreferences(
            QSettings(str(root / "prefs.ini"), QSettings.Format.IniFormat)))
        window.show()
        self.addCleanup(window.close)
        self.wait_for(lambda: window.files.index(str(link)).isValid())
        self.wait_for(lambda: path_key(root) in window.folders.nodes)
        window.tree.expand(window.folders.index_for_path(str(root)))
        self.wait_for(lambda: path_key(link) in window.folders.nodes)
        for number, view in enumerate((window.details, window.grid, window.tree)):
            incoming = self.root / f"paste-{number}.txt"
            incoming.write_text("payload")
            window.file_clipboard.put((incoming,), False)
            self.addCleanup(window.file_clipboard.clipboard.clear)
            if view is window.tree:
                index = window.folders.index_for_path(str(link))
            else:
                window.switch_view(view)
                self.wait_for(lambda: not window.pending_restore)
                index = window.model.mapFromSource(window.files.index(str(link)))
            view.setCurrentIndex(index)
            view.scrollTo(index)
            self.app.processEvents()
            point = view.visualRect(index).center()
            self.assertEqual(Path(window.link_drag.destination(view, point)), target)
            self.assertEqual(Path(window.link_drag.item_path(view, index)), link)
            if view is window.tree:
                window.show_tree_item_menu(point)
                self.assertFalse(window.tree_flatten_action.isEnabled())
                self.assertFalse(window.tree_join_action.isEnabled())
                self.assertTrue(window.tree_pack_action.isEnabled())
                self.assertEqual(window.file_clipboard.paths(view), (link,))
                self.assertEqual(window.file_clipboard.destination(view), target)
                window.tree_item_menu.hide()
                window.file_clipboard.actions[view][2].trigger()
            else:
                window.show_item_menu(view, point)
                paste = window.item_menus[view].actions()[2]
                self.assertTrue(paste.isEnabled())
                window.item_menus[view].hide()
                paste.trigger()
            self.wait_for(lambda: window.action_future is None)
            self.assertEqual((target / incoming.name).read_text(), "payload")
        renamed = root / "renamed.lnk"
        window.files.rename_path(str(link), renamed.name)
        self.wait_for(lambda: path_key(renamed) in window.folders.nodes)
        self.assertTrue(target.is_dir())
        self.assertTrue(renamed.is_file())

    def test_duplicate_and_nested_shortcut_branches_watch_independently(self):
        root = self.root / "duplicate-links"
        root.mkdir()
        target = root / "target"
        target.mkdir()
        (target / "child" / "grandchild").mkdir(parents=True)
        with ThreadPoolExecutor(max_workers=1) as worker:
            worker.submit(create_shortcuts, (target,), root).result()
            worker.submit(create_shortcuts, (target,), target).result()
        link = root / "target - Shortcut.lnk"
        duplicate = root / "duplicate.lnk"
        shutil.copyfile(link, duplicate)
        model = DirectoryTreeModel(QIcon())
        self.addCleanup(model.close)
        model.reveal_path(str(root))
        self.wait_for(lambda: path_key(root) in model.nodes)
        model.expanded(model.index_for_path(str(root)))
        self.wait_for(lambda: path_key(duplicate) in model.nodes)
        for branch in (target, link, duplicate):
            model.expanded(model.index_for_path(str(branch)))
            self.wait_for(lambda: path_key(branch / "child") in model.nodes)
            model.expanded(model.index_for_path(str(branch / "child")))
            self.wait_for(lambda: path_key(branch / "child" / "grandchild") in model.nodes)
        nested = link / "target - Shortcut.lnk"
        self.assertFalse(model.nodes[path_key(nested)].loaded)
        model.expanded(model.index_for_path(str(nested)))
        self.wait_for(lambda: path_key(nested / "child") in model.nodes)
        self.assertFalse(model.nodes[path_key(nested / "target - Shortcut.lnk")].loaded)
        link.unlink()
        self.wait_for(lambda: path_key(link) not in model.nodes)
        (target / "added").mkdir()
        self.wait_for(lambda: all(path_key(branch / "added") in model.nodes
                                  for branch in (target, duplicate)))
        self.assertLessEqual(model.peak_batch, model.batch_size)

    def test_folder_shortcuts_in_both_views_tree_and_history(self):
        root = self.root / "links"
        root.mkdir()
        target = self.root / "target folder"
        target.mkdir()
        (target / "child" / "grandchild").mkdir(parents=True)
        document = self.root / "document.txt"
        document.write_text("text")
        with ThreadPoolExecutor(max_workers=1) as worker:
            worker.submit(create_shortcuts, (target, document), root).result()
        link = root / "target folder - Shortcut.lnk"
        file_link = root / "document.txt - Shortcut.lnk"
        window = ExplorerWindow(str(root), image_result, preferences=FolderPreferences(
            QSettings(str(self.root / "settings.ini"), QSettings.Format.IniFormat)))
        window.show()
        self.addCleanup(window.close)
        self.wait_for(lambda: window.files.index(str(link)).isValid())
        source = window.files.index(str(link))
        self.assertEqual(source.siblingAtColumn(2).data(), "Folder shortcut")
        self.assertEqual(Path(window.files.filePath(source)), link)
        self.assertFalse(window.files.isDir(source))
        self.assertEqual(Path(window.files.navigation_path(source)), target)
        self.assertEqual(window.files.navigation_path(window.files.index(str(file_link))), "")
        for view in (window.details, window.grid):
            window.switch_view(view)
            source = window.files.index(str(link))
            index = window.model.mapFromSource(source)
            view.scrollTo(index)
            self.app.processEvents()
            QTest.mouseClick(view.viewport(), Qt.MouseButton.LeftButton,
                             pos=view.visualRect(index).center())
            QTest.mouseDClick(view.viewport(), Qt.MouseButton.LeftButton,
                             pos=view.visualRect(index).center())
            self.wait_for(lambda: window.current_path == str(target))
            self.wait_for(lambda: window.files.index(str(target / "child")).isValid())
            window.travel(-1)
            self.wait_for(lambda: window.current_path == str(root))
        self.wait_for(lambda: path_key(root) in window.folders.nodes)
        window.tree.expand(window.folders.index_for_path(str(root)))
        self.wait_for(lambda: path_key(link) in window.folders.nodes)
        tree_index = window.folders.index_for_path(str(link))
        self.assertEqual(Path(window.folders.file_path(tree_index)), link)
        self.assertEqual(Path(window.folders.navigation_path(tree_index)), target)
        self.assertTrue(window.folders.hasChildren(tree_index))
        window.tree.setCurrentIndex(tree_index)
        window.tree.expand(tree_index)
        self.wait_for(lambda: path_key(link / "child") in window.folders.nodes)
        child_index = window.folders.index_for_path(str(link / "child"))
        self.assertEqual(child_index.parent(), tree_index)
        self.assertEqual(Path(window.folders.file_path(child_index)), target / "child")
        window.tree.doubleClicked.emit(tree_index)
        self.wait_for(lambda: window.current_path == str(target))
        self.assertEqual(window.tree.currentIndex(), tree_index)
        window.tree.setCurrentIndex(child_index)
        window.tree.clicked.emit(child_index)
        self.wait_for(lambda: window.current_path == str(target / "child"))
        self.assertEqual(window.tree.currentIndex(), child_index)
        self.wait_for(lambda: window.files.index(str(target / "child" / "grandchild")).isValid())
        window.activate(window.model.mapFromSource(window.files.index(str(target / "child" / "grandchild"))))
        self.wait_for(lambda: window.current_path == str(target / "child" / "grandchild"))
        self.wait_for(lambda: window.tree.currentIndex().data(Qt.ItemDataRole.UserRole + 2)
                      == str(link / "child" / "grandchild"))
        window.travel(-1)
        self.wait_for(lambda: window.current_path == str(target / "child"))
        self.assertEqual(window.tree.currentIndex(), child_index)
        window.travel(1)
        self.wait_for(lambda: window.current_path == str(target / "child" / "grandchild"))
        window.up_action.trigger()
        self.wait_for(lambda: window.current_path == str(target / "child"))
        self.assertEqual(window.tree.currentIndex(), child_index)
        window.up_action.trigger()
        self.wait_for(lambda: window.current_path == str(target))
        self.assertEqual(window.tree.currentIndex(), tree_index)
        (target / "new child").mkdir()
        self.wait_for(lambda: path_key(link / "new child") in window.folders.nodes)
        (target / "new child").rmdir()
        self.wait_for(lambda: path_key(link / "new child") not in window.folders.nodes)
        self.assertTrue(link.is_file())
