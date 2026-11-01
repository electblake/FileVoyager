from concurrent.futures import Future
from pathlib import Path
import sys
import threading
import unittest
from unittest.mock import patch
import uuid
import winreg

from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QGroupBox, QWidget
from support import QtCase

from filevoyager import integrations
from filevoyager.explorer_install import ExplorerInstallDialog
from filevoyager.preferences import FolderPreferences
from filevoyager.window import ExplorerWindow


class RegistryTests(unittest.TestCase):
    def test_real_registry_commands_icons_and_reinstallation(self):
        scratch = rf"Software\FileVoyager-test-{uuid.uuid4()}"
        hive = winreg.HKEY_CURRENT_USER
        with winreg.CreateKeyEx(hive, scratch, 0, winreg.KEY_ALL_ACCESS) as sandbox:
            self.addCleanup(winreg.DeleteKey, hive, scratch)
            # Delete children before parents, including the temporary Classes tree.
            keys = {"Software", r"Software\Classes"}
            for root, _ in integrations.CONTEXTS:
                parts = (root + r"\FileVoyager\command").split("\\")
                keys.update("\\".join(parts[:i]) for i in range(3, len(parts) + 1))
            for key in sorted(keys, key=lambda value: value.count("\\")):
                self.addCleanup(winreg.DeleteKey, hive, scratch + "\\" + key)
            # Both distributions use an installed module, including paths with spaces.
            for executable, module in (
                (r"C:\Source Environment\Scripts\python.exe", r"C:\Source Project\filevoyager\integrations.py"),
                (r"C:\User Data\FileVoyager\venv\Scripts\python.exe",
                 r"C:\User Data\FileVoyager\venv\Lib\site-packages\filevoyager\integrations.py"),
            ):
                with patch.object(winreg, "HKEY_CURRENT_USER", sandbox), \
                        patch.object(sys, "executable", executable), \
                        patch.object(integrations, "__file__", module):
                    for _ in range(2):
                        self.assertEqual(integrations.install(), 0)
                        for root, target in integrations.CONTEXTS:
                            with winreg.OpenKey(sandbox, root + r"\FileVoyager") as key:
                                self.assertEqual(winreg.QueryValueEx(key, ""), ("Open in FileVoyager", winreg.REG_SZ))
                                self.assertEqual(winreg.QueryValueEx(key, "Icon")[0],
                                                 f'"{Path(module).with_name("FileVoyager.ico")}"')
                            with winreg.OpenKey(sandbox, root + r"\FileVoyager\command") as key:
                                self.assertEqual(winreg.QueryValueEx(key, "")[0],
                                                 f'"{executable}" "-I" "-m" "filevoyager" "{target}"')


class ExplorerInstallTests(QtCase):
    def test_worker_busy_controls_completion_and_reinstall(self):
        parent = QWidget()
        dialog = ExplorerInstallDialog(parent)
        self.addCleanup(parent.close)
        self.addCleanup(dialog.close)
        dialog.open()
        self.assertEqual(dialog.findChild(QGroupBox).title(), "File Explorer")
        release = threading.Event()
        worker_threads = []

        def install():
            worker_threads.append(threading.get_ident())
            release.wait(5)
            return 0

        with patch.object(integrations, "install", side_effect=install):
            dialog.install_button.click()
            self.assertFalse(dialog.install_button.isEnabled())
            self.assertEqual(dialog.status.text(), "Installing in File Explorer…")
            dialog.reject()
            self.assertTrue(dialog.isVisible())
            release.set()
            self.wait_for(lambda: dialog.future is None)
            self.assertTrue(dialog.install_button.isEnabled())
            self.assertEqual(dialog.status.text(), "Installed in File Explorer")
            dialog.install_button.click()
            self.wait_for(lambda: dialog.future is None)
        self.assertEqual(len(worker_threads), 2)
        self.assertTrue(all(worker != threading.get_ident() for worker in worker_threads))

    def test_original_failure_surfaces_without_success_status(self):
        parent = QWidget()
        dialog = ExplorerInstallDialog(parent)
        self.addCleanup(parent.close)
        self.addCleanup(dialog.close)
        pending = Future()
        with patch.object(dialog.executor, "submit", return_value=pending):
            dialog.install()
        failure = OSError("registry write failed")
        pending.set_exception(failure)
        with self.assertRaises(OSError) as raised:
            dialog.poll()
        self.assertIs(raised.exception, failure)
        self.assertNotEqual(dialog.status.text(), "Installed in File Explorer")

    def test_help_menu_startup_folder_and_busy_window_close(self):
        folder = self.root / "Selected folder with spaces"
        folder.mkdir()
        settings = QSettings(str(self.root / "explorer.ini"), QSettings.Format.IniFormat)
        settings.setValue("last_folder", str(self.root))
        window = ExplorerWindow(str(folder), None, preferences=FolderPreferences(settings))
        self.addCleanup(window.close)
        window.show()
        self.wait_for(lambda: window.address.text() == str(folder))
        self.assertIsNone(window.action_future)
        self.assertIsNone(window.similarity_dock.future)
        action = next(action for action in window.menuBar().actions()[2].menu().actions()
                      if action.text() == "Install in File Explorer")
        action.trigger()
        dialog = window.explorer_install_dialog
        self.assertTrue(dialog.isVisible())
        pending = Future()
        with patch.object(dialog.executor, "submit", return_value=pending):
            dialog.install_button.click()
        window.close()
        self.assertTrue(window.isVisible())
        pending.set_result(0)
        self.wait_for(lambda: dialog.future is None)
        dialog.reject()
        action.trigger()
        self.assertIsNot(window.explorer_install_dialog, dialog)
        window.explorer_install_dialog.reject()


if __name__ == "__main__":
    unittest.main()
