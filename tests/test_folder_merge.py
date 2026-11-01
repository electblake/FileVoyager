from concurrent.futures import ThreadPoolExecutor
import threading
import unittest

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox, QWidget

from support import QtCase
from filevoyager.folder_merge import FolderMerge


class FolderMergeTests(QtCase):
    def setUp(self):
        folder = self.root / self._testMethodName
        folder.mkdir()
        self.source, self.destination = folder / "Bust", folder / "Busts"
        self.source.mkdir()
        self.destination.mkdir()
        self.parent = QWidget()
        self.parent.show()
        self.addCleanup(self.parent.close)
        self.merge = FolderMerge(self.parent)
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.addCleanup(self.executor.shutdown)

    def run_merge(self, answers):
        remaining = list(answers)
        ui_thread = threading.get_ident()

        def answer(question):
            self.assertEqual(threading.get_ident(), ui_thread)
            dialog = self.merge.dialog
            self.assertEqual(dialog.textFormat(), Qt.TextFormat.PlainText)
            self.assertIn(str(question.source), dialog.informativeText())
            self.assertIn(str(question.destination), dialog.informativeText())
            choice = remaining.pop(0)
            if isinstance(choice, QMessageBox.StandardButton):
                dialog.button(choice).click()
            else:
                next(button for button in dialog.buttons() if button.text() == choice).click()

        self.merge.question.connect(answer)
        future = self.executor.submit(self.merge.merge, self.source, self.destination)
        self.wait_for(future.done)
        self.assertEqual(remaining, [])
        return future.result()

    def test_no_leaves_both_folders_untouched(self):
        (self.source / "source.txt").write_text("source")
        (self.destination / "destination.txt").write_text("destination")
        self.assertEqual(self.run_merge([QMessageBox.StandardButton.No]), "Folder merge cancelled")
        self.assertEqual((self.source / "source.txt").read_text(), "source")
        self.assertEqual((self.destination / "destination.txt").read_text(), "destination")

    def test_yes_merges_nested_folders_and_preserves_destination_files(self):
        for folder in (self.source, self.destination):
            (folder / "nested").mkdir()
        (self.source / "nested" / "source.txt").write_text("source")
        (self.destination / "nested" / "destination.txt").write_text("destination")
        self.assertEqual(self.run_merge([QMessageBox.StandardButton.Yes]), "Folder merge complete")
        self.assertFalse(self.source.exists())
        self.assertEqual((self.destination / "nested" / "source.txt").read_text(), "source")
        self.assertEqual((self.destination / "nested" / "destination.txt").read_text(), "destination")

    def test_replace_requires_confirmation_and_replaces_duplicate(self):
        (self.source / "same.txt").write_text("new")
        (self.destination / "same.txt").write_text("old")
        self.run_merge([QMessageBox.StandardButton.Yes, "&Replace"])
        self.assertFalse(self.source.exists())
        self.assertEqual((self.destination / "same.txt").read_text(), "new")

    def test_skip_retains_source_file_and_moves_nonconflicting_files(self):
        (self.source / "same.txt").write_text("new")
        (self.source / "unique.txt").write_text("unique")
        (self.destination / "same.txt").write_text("old")
        result = self.run_merge([QMessageBox.StandardButton.Yes, "&Skip"])
        self.assertIn("skipped items kept", result)
        self.assertEqual((self.source / "same.txt").read_text(), "new")
        self.assertEqual((self.destination / "same.txt").read_text(), "old")
        self.assertEqual((self.destination / "unique.txt").read_text(), "unique")

    def test_cancel_duplicate_retains_both_versions(self):
        (self.source / "same.txt").write_text("new")
        (self.destination / "same.txt").write_text("old")
        result = self.run_merge([QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.Cancel])
        self.assertIn("stopped", result)
        self.assertEqual((self.source / "same.txt").read_text(), "new")
        self.assertEqual((self.destination / "same.txt").read_text(), "old")


if __name__ == "__main__":
    unittest.main()
