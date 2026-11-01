import os
from pathlib import Path
import shutil

from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import (
    QCheckBox, QDialog, QDialogButtonBox, QLabel, QLineEdit, QVBoxLayout,
)


def copy_item(source, destination):
    if source.is_dir():
        destination.mkdir()
        with os.scandir(source) as entries:
            for entry in entries:
                copy_item(Path(entry.path), destination / entry.name)
    else:
        with source.open("rb") as incoming, destination.open("xb") as outgoing:
            shutil.copyfileobj(incoming, outgoing)
    shutil.copystat(source, destination)


def pack_to_folder(paths, destination, copy_mode):
    destination.mkdir()
    for source in paths:
        target = destination / source.name
        if copy_mode:
            copy_item(source, target)
        else:
            source.rename(target)


def flatten_contents(folder, destination):
    with os.scandir(folder) as entries:
        for entry in entries:
            source = Path(entry.path)
            if entry.is_dir(follow_symlinks=False) and not source.is_junction():
                flatten_contents(source, destination)
                source.rmdir()
            elif folder != destination:
                source.rename(destination / source.name)


def flatten_folders(paths):
    for folder in paths:
        flatten_contents(folder, folder)


class PackToFolderDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Pack to Folder")
        self.setMinimumWidth(480)
        layout = QVBoxLayout(self)
        label = QLabel("Enter the &name of the new folder:")
        layout.addWidget(label)
        self.folder_name = QLineEdit()
        self.folder_name.setValidator(QRegularExpressionValidator(
            QRegularExpression(r'(?!(?:\.|\.\.)$)[^<>:"/\\|?*\x00-\x1f]*[^<>:"/\\|?*\x00-\x1f. ]'), self))
        label.setBuddy(self.folder_name)
        layout.addWidget(self.folder_name)
        self.copy_mode = QCheckBox("&Copy mode (keep the files in the source folders)")
        layout.addWidget(self.copy_mode)
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        self.buttons.button(QDialogButtonBox.StandardButton.Ok).setEnabled(False)
        self.folder_name.textChanged.connect(lambda: self.buttons.button(
            QDialogButtonBox.StandardButton.Ok).setEnabled(self.folder_name.hasAcceptableInput()))
        layout.addWidget(self.buttons)
        self.folder_name.setFocus()
