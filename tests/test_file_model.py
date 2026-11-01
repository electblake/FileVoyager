import threading
from unittest.mock import patch

from PySide6.QtCore import QPersistentModelIndex, Qt
from PySide6.QtGui import QIcon
from PySide6.QtTest import QAbstractItemModelTester

from support import QtCase
from filevoyager.file_model import FileModel, directory_snapshot
from filevoyager.directory_tree import DirectoryTreeModel


class FileModelTests(QtCase):
    def setUp(self):
        self.folder = self.root / self._testMethodName
        self.folder.mkdir()
        self.model = FileModel(QIcon(), QIcon())
        self.addCleanup(self.model.close)
        self.tester = QAbstractItemModelTester(
            self.model, QAbstractItemModelTester.FailureReportingMode.Fatal)

    def load(self, folder):
        index = self.model.setRootPath(str(folder))
        self.wait_for(lambda: self.model.is_loaded(str(folder)))
        return index

    def settled(self):
        self.wait_for(lambda: self.model.future is None and self.model.applying is None
                      and not self.model.pending)

    def test_worker_scan_natural_sort_and_persistent_selection(self):
        for name in ('file10.txt', 'file2.txt', 'file1.txt'):
            (self.folder / name).write_text(name)
        (self.folder / 'directory').mkdir()
        threads = []
        def scan(*args):
            threads.append(threading.get_ident())
            return directory_snapshot(*args)
        with patch('filevoyager.file_model.directory_snapshot', scan):
            root = self.load(self.folder)
            self.assertEqual([self.model.index(i, 0, root).data() for i in range(4)],
                             ['directory', 'file1.txt', 'file2.txt', 'file10.txt'])
            selected = QPersistentModelIndex(self.model.index(str(self.folder / 'file2.txt')))
            self.model.sort(0, Qt.SortOrder.DescendingOrder)
            self.settled()
        self.assertTrue(all(t != threading.get_ident() for t in threads))
        self.assertEqual(selected.data(), 'file2.txt')
        self.assertEqual(selected.row(), 1)

    def test_watcher_inserts_removes_and_preserves_surviving_index(self):
        for name in ('a.txt', 'c.txt', 'd.txt'):
            (self.folder / name).write_text(name)
        self.load(self.folder)
        selected = QPersistentModelIndex(self.model.index(str(self.folder / 'c.txt')))
        (self.folder / 'a.txt').unlink()
        (self.folder / 'b.txt').write_text('new')
        self.wait_for(lambda: self.model.index(str(self.folder / 'b.txt')).isValid()
                      and not self.model.index(str(self.folder / 'a.txt')).isValid())
        self.settled()
        self.assertEqual(selected.data(), 'c.txt')
        self.assertEqual(selected.row(), 1)
        self.assertEqual(self.model.file_metadata(self.model.index(str(self.folder / 'b.txt')))[1], 3)
        (self.folder / 'b.txt').write_text('updated content')
        self.wait_for(lambda: self.model.file_metadata(
            self.model.index(str(self.folder / 'b.txt')))[1] == 15)

    def test_cache_eviction_and_revisit(self):
        (self.folder / 'retained.txt').touch()
        root = QPersistentModelIndex(self.load(self.folder))
        for number in range(4):
            other = self.folder / str(number)
            other.mkdir()
            self.load(other)
        self.assertFalse(self.model.is_loaded(str(self.folder)))
        self.assertEqual(self.model.rowCount(root), 0)
        self.assertTrue(root.isValid())
        self.load(self.folder)
        self.assertEqual(self.model.rowCount(root), 5)
        self.assertEqual(len(self.model.recent), 4)

    def test_empty_cached_folder_is_rescanned_after_eviction(self):
        empty = self.folder / 'empty'
        empty.mkdir()
        root = self.load(empty)
        for number in range(4):
            other = self.folder / str(number)
            other.mkdir()
            self.load(other)
        (empty / 'new.txt').touch()
        self.assertFalse(self.model.is_loaded(str(empty)))
        self.load(empty)
        self.assertEqual(self.model.rowCount(root), 1)

    def test_rename_during_publication_rescans_without_duplicates(self):
        for number in range(600):
            (self.folder / f'item{number}.txt').touch()
        renamed = []
        def rename_first(parent, first, last):
            if parent.isValid() and not renamed:
                renamed.append(True)
                # Schedule after the insertion signal's model transaction.
                from PySide6.QtCore import QTimer
                QTimer.singleShot(0, lambda: self.model.rename_path(
                    str(self.folder / 'item0.txt'), 'renamed.txt'))
        self.model.rowsInserted.connect(rename_first)
        root = self.load(self.folder)
        self.settled()
        self.assertEqual(self.model.rowCount(root), 600)
        self.assertTrue(self.model.index(str(self.folder / 'renamed.txt')).isValid())
        self.assertFalse(self.model.index(str(self.folder / 'item0.txt')).isValid())
        self.assertLessEqual(self.model.peak_batch, 512)

    def test_tree_comparison_runs_on_scan_worker(self):
        from filevoyager.directory_tree import directory_changes
        threads = []
        def compare(*args):
            threads.append(threading.get_ident())
            return directory_changes(*args)
        with patch('filevoyager.directory_tree.directory_changes', compare):
            tree = DirectoryTreeModel(QIcon())
            self.addCleanup(tree.close)
            self.wait_for(lambda: tree.active_key is None)
        self.assertTrue(threads)
        self.assertTrue(all(t != threading.get_ident() for t in threads))

    def test_revealing_drive_during_scan_does_not_duplicate_it(self):
        drive = self.folder.anchor
        with patch('filevoyager.directory_tree.scan_directories', return_value=[(drive, drive, "")]):
            tree = DirectoryTreeModel(QIcon())
            self.addCleanup(tree.close)
            tree.reveal_path(drive)
            self.wait_for(lambda: tree.active_key is None)
        self.assertEqual(tree.rowCount(), 1)
        self.assertEqual(tree.file_path(tree.index(0, 0)), drive)
