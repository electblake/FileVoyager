"""File clipboard commands for the item views and folder tree."""

from pathlib import Path

from PySide6.QtCore import QMimeData, QObject, QUrl, Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QStyle, QStyledItemDelegate

from filevoyager.directory_tree import path_key
from filevoyager.item_actions import transfer_items
from filevoyager.selection import selected_row_count, selected_rows


DROP_EFFECT = 'application/x-qt-windows-mime;value="Preferred DropEffect"'


class CutItemDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        view = self.parent()
        window = view.window()
        if not window.file_clipboard.cut_paths:
            return
        path = (window.folders.file_path(index) if view is window.tree else
                window.files.filePath(window.model.mapToSource(index)))
        if path_key(path) in window.file_clipboard.cut_paths:
            option.state &= ~QStyle.StateFlag.State_Enabled


class FileClipboard(QObject):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
        self.clipboard = QApplication.clipboard()
        self.pending = None
        self.cut_paths = set()
        self.context_actions = {}
        self.edit_view = window.details
        self.actions = {}
        for view in (window.details, window.grid, window.tree):
            cut = QAction("Cu&t", view)
            copy = QAction("&Copy", view)
            paste = QAction("&Paste", view)
            cut.triggered.connect(lambda checked=False, target=view: self.put(self.paths(target), True))
            copy.triggered.connect(lambda checked=False, target=view: self.put(self.paths(target), False))
            paste.triggered.connect(lambda checked=False, target=view: self.paste(self.destination(target)))
            for action in (cut, copy, paste):
                action.setShortcutContext(Qt.ShortcutContext.WidgetShortcut)
                view.addAction(action)
            self.actions[view] = (cut, copy, paste)
        window.selection.selectionChanged.connect(self.update)
        window.tree.selectionModel().selectionChanged.connect(self.update)
        for number, (key, label, shortcut) in enumerate((
                ("cut", "Cut", "Ctrl+X"), ("copy", "Copy", "Ctrl+C"), ("paste", "Paste", "Ctrl+V"))):
            window.shortcuts.add(key, label, shortcut, *(actions[number] for actions in self.actions.values()))
        self.clipboard.dataChanged.connect(self.clipboard_changed)
        QApplication.instance().focusChanged.connect(self.focus_changed)
        self.clipboard_changed()

    def focus_changed(self, old, current):
        for view in self.actions:
            if current is view or current is view.viewport():
                self.edit_view = view

    def show_edit_menu(self):
        self.window.edit_menu.clear()
        self.window.edit_menu.addActions(self.actions[self.edit_view])
        self.update()

    def clipboard_changed(self):
        paths, cut = self.snapshot()
        self.clipboard_sources = set(paths)
        self.clipboard_cut = cut
        self.clipboard_parents = {path.parent for path in paths}
        self.cut_paths = {path_key(path) for path in paths} if cut else set()
        for view in self.actions:
            view.viewport().update()
        self.update()

    def context_destination(self):
        if selected_row_count(self.window.selection) == 1:
            index = next(selected_rows(self.window.selection))
            destination = self.window.files.navigation_path(self.window.model.mapToSource(index))
            if destination:
                return Path(destination)
        return Path(self.window.current_path)

    def paths(self, view):
        if view is self.window.tree:
            return tuple(Path(self.window.folders.file_path(index))
                         for index in selected_rows(view.selectionModel())
                         if index.data(Qt.ItemDataRole.UserRole))
        return self.window.selected_item_paths()

    def destination(self, view):
        if view is self.window.tree:
            return Path(self.window.folders.navigation_path(view.currentIndex()))
        return Path(self.window.current_path)

    def put(self, paths, cut):
        mime = QMimeData()
        mime.setUrls([QUrl.fromLocalFile(str(path)) for path in paths])
        mime.setData(DROP_EFFECT, (2 if cut else 1).to_bytes(4, "little"))
        self.clipboard.setMimeData(mime)

    def snapshot(self):
        mime = self.clipboard.mimeData()
        if mime is None:
            return (), False
        urls = mime.urls()
        paths = tuple(Path(url.toLocalFile()) for url in urls) if (
            urls and all(url.isLocalFile() for url in urls)) else ()
        return paths, bytes(mime.data(DROP_EFFECT)) == (2).to_bytes(4, "little")

    def can_paste(self, destination):
        return (self.window.action_future is None and bool(self.clipboard_sources)
                and not (self.clipboard_cut and self.clipboard_parents == {destination})
                and not any(path in self.clipboard_sources for path in (destination, *destination.parents)))

    def update(self, *args):
        for view, (cut, copy, paste) in self.actions.items():
            tree = view is self.window.tree
            paths = self.paths(view) if tree else ()
            selected = bool(paths) if tree else self.window.selection.hasSelection()
            available = self.window.action_future is None and selected
            cut.setEnabled(available and (not tree or all(path.parent != path for path in paths)))
            copy.setEnabled(available)
            destination_available = selected if tree else bool(self.window.current_path)
            paste.setEnabled(destination_available and self.can_paste(self.destination(view)))
        for paste in self.context_actions.values():
            paste.setEnabled(bool(self.window.current_path) and self.can_paste(self.context_destination()))

    def paste(self, destination):
        paths, cut = self.snapshot()
        self.pending = (paths, cut)
        self.window.start_item_action(
            "Moving items…" if cut else "Copying items…", self.transfer, paths, destination, cut,
            refresh_paths=(destination, *paths, *(path.parent for path in paths)))

    def transfer(self, paths, destination, cut):
        result = transfer_items(paths, destination, not cut, self.window.folder_merge.ask)
        self.remaining = tuple(path for path in paths if path.exists()) if cut else paths
        return result

    def finish(self):
        if self.pending is not None:
            if self.pending[1] and self.snapshot() == self.pending:
                if self.remaining:
                    self.put(self.remaining, True)
                else:
                    self.clipboard.clear()
            self.pending = None
        self.update()
