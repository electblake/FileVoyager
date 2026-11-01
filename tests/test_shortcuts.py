import unittest

from PySide6.QtCore import QSettings, Qt
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QDialogButtonBox, QKeySequenceEdit, QWidget

from support import QtCase
from filevoyager.shortcuts import KeyboardShortcutsDialog, Shortcuts


class ShortcutTests(QtCase):
    def test_edit_sorted_filtered_shortcut_save_reload_and_clear(self):
        parent = QWidget()
        parent.show()
        self.addCleanup(parent.close)
        filename = str(self.root / "shortcuts.ini")
        shortcuts = Shortcuts(QSettings(filename, QSettings.Format.IniFormat))
        rename_actions = [QAction(parent), QAction(parent)]
        shortcuts.add("rename", "Rename", "F2", *rename_actions)
        shortcuts.add("back", "Back", "Alt+Left", QAction(parent))
        dialog = KeyboardShortcutsDialog(shortcuts, parent)
        dialog.open()
        self.addCleanup(dialog.close)
        dialog.activateWindow()
        self.wait_for(dialog.isActiveWindow)
        self.assertEqual(dialog.proxy.index(0, 0).data(), "Back")
        dialog.table.sortByColumn(0, Qt.SortOrder.DescendingOrder)
        self.assertEqual(dialog.proxy.index(0, 0).data(), "Rename")
        dialog.search.setText("f2")
        self.assertEqual(dialog.proxy.rowCount(), 1)
        self.assertEqual(dialog.proxy.index(0, 0).data(), "Rename")
        custom = dialog.proxy.index(0, 2)
        dialog.table.setCurrentIndex(custom)
        dialog.table.edit(custom)
        editor = dialog.table.findChild(QKeySequenceEdit)
        self.assertTrue(editor.isVisible())
        QTest.keyClick(editor, Qt.Key.Key_R, Qt.KeyboardModifier.ControlModifier | Qt.KeyboardModifier.AltModifier)
        self.assertEqual(editor.keySequence(), QKeySequence("Ctrl+Alt+R"))
        QTest.mouseClick(dialog.buttons.button(QDialogButtonBox.StandardButton.Ok), Qt.MouseButton.LeftButton)
        self.assertFalse(dialog.isVisible())
        self.assertTrue(all(action.shortcut() == QKeySequence("Ctrl+Alt+R") for action in rename_actions))
        stored = QSettings(filename, QSettings.Format.IniFormat)
        self.assertEqual(stored.value("shortcuts/rename"), "Ctrl+Alt+R")
        reloaded = Shortcuts(stored)
        action = QAction(parent)
        reloaded.add("rename", "Rename", "F2", action)
        self.assertEqual(action.shortcut(), QKeySequence("Ctrl+Alt+R"))
        reopened = KeyboardShortcutsDialog(reloaded, parent)
        reopened.open()
        self.addCleanup(reopened.close)
        reopened.activateWindow()
        self.wait_for(reopened.isActiveWindow)
        reopened.search.setText("ctrl+alt+r")
        self.assertEqual(reopened.proxy.rowCount(), 1)
        reopened.table.edit(reopened.proxy.index(0, 2))
        editor = reopened.table.findChild(QKeySequenceEdit)
        editor.clear()
        QTest.mouseClick(reopened.buttons.button(QDialogButtonBox.StandardButton.Ok), Qt.MouseButton.LeftButton)
        self.assertEqual(action.shortcut(), QKeySequence("F2"))
        self.assertFalse(stored.contains("shortcuts/rename"))

    def test_cancel_leaves_actions_and_settings_unchanged(self):
        parent = QWidget()
        self.addCleanup(parent.close)
        settings = QSettings(str(self.root / "cancel.ini"), QSettings.Format.IniFormat)
        shortcuts = Shortcuts(settings)
        action = QAction(parent)
        shortcuts.add("rename", "Rename", "F2", action)
        dialog = KeyboardShortcutsDialog(shortcuts, parent)
        dialog.open()
        self.addCleanup(dialog.close)
        dialog.model.item(0, 2).setText("Ctrl+Alt+R")
        QTest.mouseClick(dialog.buttons.button(QDialogButtonBox.StandardButton.Cancel), Qt.MouseButton.LeftButton)
        self.assertEqual(action.shortcut(), QKeySequence("F2"))
        self.assertFalse(settings.contains("shortcuts/rename"))


if __name__ == "__main__":
    unittest.main()
