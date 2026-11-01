"""Shared file-operation conflict dialogs and folder rename merging."""

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from threading import Event

from PySide6.QtCore import QObject, Qt, Signal
from PySide6.QtWidgets import QMessageBox

from filevoyager.item_actions import transfer_contents


@dataclass
class MergeQuestion:
    source: Path
    destination: Path
    folder: bool
    source_created: str
    destination_created: str
    answered: Event = field(default_factory=Event)
    answer: str = ""


class FolderMerge(QObject):
    question = Signal(object)

    def __init__(self, parent):
        super().__init__(parent)
        self.question.connect(self.show_question)
        self.dialog = None

    def ask(self, source, destination, folder):
        question = MergeQuestion(
            source, destination, folder,
            datetime.fromtimestamp(source.stat().st_birthtime).strftime("%Y-%m-%d %I:%M %p"),
            datetime.fromtimestamp(destination.stat().st_birthtime).strftime("%Y-%m-%d %I:%M %p"),
        )
        self.question.emit(question)
        question.answered.wait()
        return question.answer

    def show_question(self, question):
        dialog = QMessageBox(self.parent())
        self.dialog = dialog
        dialog.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        dialog.setTextFormat(Qt.TextFormat.PlainText)
        dialog.setIcon(QMessageBox.Icon.Warning)
        if question.folder:
            dialog.setWindowTitle("Confirm Folder Replace")
            dialog.setText(f"This destination already contains a folder named '{question.destination.name}'.")
            dialog.setInformativeText(
                "If any files have the same names, you will be asked if you want to replace those files.\n\n"
                f"Do you still want to merge this folder\n\n{question.destination}\n"
                f"Date created: {question.destination_created}\n\nwith this one?\n\n{question.source}\n"
                f"Date created: {question.source_created}")
            yes = dialog.addButton(QMessageBox.StandardButton.Yes)
            no = dialog.addButton(QMessageBox.StandardButton.No)
            dialog.setDefaultButton(no)
            dialog.setEscapeButton(no)

            def answered():
                question.answer = "merge" if dialog.clickedButton() is yes else "cancel"
                question.answered.set()
        else:
            dialog.setWindowTitle("Replace or Skip File")
            dialog.setText(f"The destination already contains a file named '{question.destination.name}'.")
            dialog.setInformativeText(
                f"Replace this file?\n\n{question.destination}\nDate created: {question.destination_created}"
                f"\n\nWith this file:\n\n{question.source}\nDate created: {question.source_created}")
            replace = dialog.addButton("&Replace", QMessageBox.ButtonRole.AcceptRole)
            skip = dialog.addButton("&Skip", QMessageBox.ButtonRole.NoRole)
            cancel = dialog.addButton(QMessageBox.StandardButton.Cancel)
            dialog.setDefaultButton(skip)
            dialog.setEscapeButton(cancel)

            def answered():
                clicked = dialog.clickedButton()
                question.answer = "replace" if clicked is replace else "skip" if clicked is skip else "cancel"
                question.answered.set()
        dialog.finished.connect(answered)
        dialog.open()

    def merge(self, source, destination):
        source, destination = Path(source), Path(destination)
        if self.ask(source, destination, True) != "merge":
            return "Folder merge cancelled"
        complete = self.merge_contents(source, destination)
        if not complete:
            return "Folder merge stopped; remaining items kept in source"
        return "Folder merge complete; skipped items kept in source" if source.exists() else "Folder merge complete"

    def merge_contents(self, source, destination):
        return transfer_contents(source, destination, False, self.ask, remove_source=True)
