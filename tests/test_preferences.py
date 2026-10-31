from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from PySide6.QtCore import QSettings

from filevoyager.preferences import FolderPreferences, user_settings


class PreferencesTests(unittest.TestCase):
    def test_platformdirs_sets_qsettings_user_config_default(self):
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp) / "FileVoyager"
            directory.mkdir()
            with patch("filevoyager.preferences.user_config_path", return_value=directory) as config:
                settings = user_settings()
            config.assert_called_once_with("FileVoyager", appauthor=False, ensure_exists=True)
            self.assertEqual(Path(settings.fileName()), directory / "FileVoyager.ini")
            self.assertEqual(QSettings.defaultFormat(), QSettings.Format.IniFormat)
            self.assertEqual(settings.scope(), QSettings.Scope.UserScope)

    def test_windows_folder_keys_ignore_case_and_separator_variations(self):
        with tempfile.TemporaryDirectory() as temp:
            preferences = FolderPreferences(QSettings(str(Path(temp) / "test.ini"), QSettings.Format.IniFormat))
            preferences.save("C:/Pictures/Example", {"view": "details", "size": 80,
                                                    "grid": [123, 0], "details": [45, 0]})
            self.assertEqual(preferences.load("c:\\pictures\\example", True)["view"], "details")
