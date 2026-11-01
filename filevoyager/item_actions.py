import os
from pathlib import Path
import shutil

from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import (
    QCheckBox, QDialog, QDialogButtonBox, QLabel, QLineEdit, QVBoxLayout,
)


def copy_item(source, destination, replace=False):
    if source.is_dir():
        destination.mkdir()
        with os.scandir(source) as entries:
            for entry in entries:
                copy_item(Path(entry.path), destination / entry.name)
    else:
        with source.open("rb") as incoming, destination.open("wb" if replace else "xb") as outgoing:
            shutil.copyfileobj(incoming, outgoing)
    shutil.copystat(source, destination)


def transfer_item(source, destination, copy_mode, ask, confirm_folder=True):
    if source == destination:
        return True
    exists = destination.exists()
    if exists:
        if (source.is_dir() and destination.is_dir()
                and not source.is_symlink() and not destination.is_symlink()
                and not source.is_junction() and not destination.is_junction()):
            if confirm_folder and ask(source, destination, True) != "merge":
                return False
            return transfer_contents(source, destination, copy_mode, ask, remove_source=not copy_mode)
        answer = ask(source, destination, False)
        if answer == "cancel":
            return False
        if answer == "skip":
            return True
    if copy_mode or source.stat().st_dev != destination.parent.stat().st_dev:
        copy_item(source, destination, replace=exists)
        if not copy_mode:
            if source.is_dir():
                shutil.rmtree(source)
            else:
                source.unlink()
    elif exists:
        source.replace(destination)
    else:
        source.rename(destination)
    return True


def transfer_contents(source, destination, copy_mode, ask, *, remove_source=False):
    with os.scandir(source) as entries:
        for entry in entries:
            if not transfer_item(Path(entry.path), destination / entry.name, copy_mode, ask,
                                 confirm_folder=False):
                return False
    if remove_source:
        with os.scandir(source) as remaining:
            empty = next(remaining, None) is None
        if empty:
            source.rmdir()
    return True


def prepare_destination(paths, destination, ask):
    if destination.is_dir():
        return ask(paths[0], destination, True) == "merge"
    destination.mkdir()
    return True


def transfer_items(paths, destination, copy_mode, ask):
    for source in paths:
        target = destination / source.name
        if copy_mode and source == target:
            stem, suffix = (source.name, "") if source.is_dir() else (source.stem, source.suffix)
            target = destination / f"{stem} - Copy{suffix}"
            number = 2
            while target.exists():
                target = destination / f"{stem} - Copy ({number}){suffix}"
                number += 1
        if not transfer_item(source, target, copy_mode, ask):
            return "Action stopped; remaining items kept in source"


def pack_to_folder(paths, destination, copy_mode, ask):
    if not prepare_destination(paths, destination, ask):
        return "Action cancelled"
    for source in paths:
        if source == destination:
            continue
        if not transfer_item(source, destination / source.name, copy_mode, ask):
            return "Action stopped; remaining items kept in source"


def join_to_folder(paths, destination, copy_mode, ask):
    if not prepare_destination(paths, destination, ask):
        return "Action cancelled"
    for folder in paths:
        if folder != destination and not transfer_contents(folder, destination, copy_mode, ask):
            return "Action stopped; remaining items kept in source"


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
