import hashlib
import json
import os

from platformdirs import user_config_path
from PySide6.QtCore import QSettings


def user_settings():
    directory = user_config_path("FileVoyager", appauthor=False, ensure_exists=True)
    QSettings.setDefaultFormat(QSettings.Format.IniFormat)
    QSettings.setPath(QSettings.Format.IniFormat, QSettings.Scope.UserScope, str(directory.parent))
    return QSettings(QSettings.Format.IniFormat, QSettings.Scope.UserScope,
                     "FileVoyager", "FileVoyager")


class FolderPreferences:
    def __init__(self, settings=None):
        self.settings = user_settings() if settings is None else settings
        self.settings.setFallbacksEnabled(False)

    def key(self, path):
        canonical = os.path.normcase(os.path.normpath(path))
        return "folders/" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()

    def load(self, path, media_folder):
        key = self.key(path)
        if self.settings.contains(key):
            return json.loads(self.settings.value(key, type=str))
        return {"view": "grid" if media_folder else "details", "size": 128,
                "grid": [0, 0], "details": [0, 0]}

    def save(self, path, state):
        self.settings.setValue(self.key(path), json.dumps(state))
        self.settings.sync()
