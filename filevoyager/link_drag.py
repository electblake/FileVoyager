"""Native move/link drags, with an explicit drag-to-select mode."""

from pathlib import Path
from tempfile import TemporaryDirectory

from comtypes import CoInitializeEx, CoUninitialize, COINIT_MULTITHREADED
from comtypes.client import CreateObject
from PySide6.QtCore import QEvent, QMimeData, QObject, QUrl, Qt
from PySide6.QtGui import QDrag
from PySide6.QtWidgets import QApplication
from filevoyager.selection import selected_rows
from filevoyager.item_actions import transfer_items


def create_shortcuts(paths, destination):
    CoInitializeEx(COINIT_MULTITHREADED)
    shell = CreateObject("WScript.Shell", dynamic=True)
    with TemporaryDirectory(prefix=".filevoyager-links-", dir=destination) as scratch:
        for path in paths:
            source = Path(path).resolve(strict=True)
            name = source.name + " - Shortcut.lnk"
            staged = Path(scratch) / name
            shortcut = shell.CreateShortcut(str(staged))
            shortcut.TargetPath = str(source)
            shortcut.WorkingDirectory = str(source.parent)
            shortcut.Save()
            del shortcut
            # Windows rename fails on an existing name, preserving that shortcut.
            staged.rename(Path(destination) / name)
    del shell
    CoUninitialize()


class LinkDrag(QObject):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
        self.views = {view.viewport(): view for view in (window.details, window.grid, window.tree)}
        self.press = None
        self.deferred_press = None
        self.dragged = False
        self.drag_paths = ()
        self.drag_sources = set()
        self.drag_parents = set()
        for viewport, view in self.views.items():
            view.setDragDropMode(view.DragDropMode.DropOnly)
            viewport.setAcceptDrops(True)
            viewport.installEventFilter(self)

    def item_path(self, view, index):
        if view is self.window.tree:
            return self.window.folders.file_path(index)
        return self.window.files.filePath(self.window.model.mapToSource(index))

    def destination(self, view, point):
        index = view.indexAt(point)
        if view is self.window.tree:
            return self.window.folders.navigation_path(index) if index.isValid() else ""
        if not index.isValid():
            return self.window.current_path
        source = self.window.model.mapToSource(index)
        return self.window.files.navigation_path(source)

    def eventFilter(self, viewport, event):
        kind = event.type()
        if kind not in (QEvent.Type.MouseButtonPress, QEvent.Type.MouseButtonRelease, QEvent.Type.MouseMove,
                        QEvent.Type.DragEnter, QEvent.Type.DragMove, QEvent.Type.DragLeave, QEvent.Type.Drop):
            return False
        view = viewport.parentWidget()
        if kind == QEvent.Type.MouseButtonPress:
            self.dragged = False
            self.deferred_press = None
            self.press = (viewport, event.position().toPoint()) if (
                event.button() == Qt.MouseButton.LeftButton and view.indexAt(event.position().toPoint()).isValid()) else None
            if (self.press is not None and not self.window.select_mode.isChecked()
                    and event.modifiers() == Qt.KeyboardModifier.NoModifier
                    and view.selectionModel().isSelected(view.indexAt(self.press[1]))):
                view.setFocus()
                self.deferred_press = event.clone()
                return True
        elif kind == QEvent.Type.MouseButtonRelease:
            self.press = None
            if self.dragged:
                self.dragged = False
                return True
            if self.deferred_press is not None:
                view.mousePressEvent(self.deferred_press)
                self.deferred_press = None
        elif (kind == QEvent.Type.MouseMove and event.buttons() & Qt.MouseButton.LeftButton
              and (event.modifiers() == Qt.KeyboardModifier.AltModifier
                   or (not self.window.select_mode.isChecked()
                       and event.modifiers() in (Qt.KeyboardModifier.NoModifier, Qt.KeyboardModifier.ShiftModifier)))):
            if (self.press is None or self.press[0] is not viewport or self.window.action_future is not None
                    or (event.position().toPoint() - self.press[1]).manhattanLength() < QApplication.startDragDistance()):
                return True
            self.press = None
            self.deferred_press = None
            self.dragged = True
            paths = [self.item_path(view, index) for index in selected_rows(view.selectionModel())]
            if paths:
                mime = QMimeData()
                mime.setUrls([QUrl.fromLocalFile(path) for path in paths])
                drag = QDrag(view)
                drag.setMimeData(mime)
                action = (Qt.DropAction.LinkAction if event.modifiers() == Qt.KeyboardModifier.AltModifier
                          else Qt.DropAction.MoveAction)
                drag.exec(action, action)
                drag.deleteLater()
                return True
        elif kind == QEvent.Type.DragLeave:
            self.drag_paths = ()
            self.drag_sources.clear()
            self.drag_parents.clear()
        elif kind in (QEvent.Type.DragEnter, QEvent.Type.DragMove, QEvent.Type.Drop):
            if kind == QEvent.Type.DragEnter:
                urls = event.mimeData().urls()
                self.drag_paths = tuple(url.toLocalFile() for url in urls) if (
                    urls and all(url.isLocalFile() for url in urls)) else ()
                self.drag_sources = {Path(path) for path in self.drag_paths}
                self.drag_parents = {path.parent for path in self.drag_sources}
            destination = self.destination(view, event.position().toPoint())
            action = Qt.DropAction.IgnoreAction
            if event.modifiers() == Qt.KeyboardModifier.AltModifier:
                action = Qt.DropAction.LinkAction
            elif event.modifiers() in (Qt.KeyboardModifier.NoModifier, Qt.KeyboardModifier.ShiftModifier):
                action = Qt.DropAction.MoveAction
            if (event.possibleActions() & action
                    and self.drag_paths
                    and destination and self.window.action_future is None
                    and (action == Qt.DropAction.LinkAction or (
                        not any(path in self.drag_sources for path in (Path(destination), *Path(destination).parents))
                        and self.drag_parents != {Path(destination)}))):
                event.setDropAction(action)
                event.accept()
                if kind == QEvent.Type.Drop:
                    if action == Qt.DropAction.LinkAction:
                        self.window.start_item_action("Creating shortcuts…", create_shortcuts,
                                                      self.drag_paths, Path(destination),
                                                      refresh_paths=(destination,))
                    else:
                        paths = tuple(Path(path) for path in self.drag_paths)
                        self.window.start_item_action("Moving items…", transfer_items,
                                                      paths, Path(destination), False, self.window.folder_merge.ask,
                                                      refresh_paths=(destination, *paths, *(path.parent for path in paths)))
            else:
                event.ignore()
            if kind == QEvent.Type.Drop:
                self.drag_paths = ()
                self.drag_sources.clear()
                self.drag_parents.clear()
            return True
        return False
