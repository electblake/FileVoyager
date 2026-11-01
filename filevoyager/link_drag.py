"""Alt-only native Qt link drags and Windows .lnk creation."""

from pathlib import Path
from tempfile import TemporaryDirectory

from comtypes import CoInitializeEx, CoUninitialize, COINIT_MULTITHREADED
from comtypes.client import CreateObject
from PySide6.QtCore import QEvent, QMimeData, QObject, QUrl, Qt
from PySide6.QtGui import QDrag
from PySide6.QtWidgets import QApplication
from filevoyager.selection import selected_rows


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
        self.drag_paths = ()
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
            return self.item_path(view, index) if index.isValid() else ""
        if not index.isValid():
            return self.window.current_path
        source = self.window.model.mapToSource(index)
        return self.window.files.filePath(source) if self.window.files.isDir(source) else ""

    def eventFilter(self, viewport, event):
        kind = event.type()
        if kind not in (QEvent.Type.MouseButtonPress, QEvent.Type.MouseButtonRelease, QEvent.Type.MouseMove,
                        QEvent.Type.DragEnter, QEvent.Type.DragMove, QEvent.Type.DragLeave, QEvent.Type.Drop):
            return False
        view = viewport.parentWidget()
        if kind == QEvent.Type.MouseButtonPress:
            self.press = (viewport, event.position().toPoint()) if (
                event.button() == Qt.MouseButton.LeftButton and view.indexAt(event.position().toPoint()).isValid()) else None
        elif kind == QEvent.Type.MouseButtonRelease:
            self.press = None
        elif (kind == QEvent.Type.MouseMove and self.press is not None
              and self.press[0] is viewport and event.buttons() & Qt.MouseButton.LeftButton
              and event.modifiers() == Qt.KeyboardModifier.AltModifier
              and self.window.action_future is None
              and (event.position().toPoint() - self.press[1]).manhattanLength() >= QApplication.startDragDistance()):
            self.press = None
            paths = [self.item_path(view, index) for index in selected_rows(view.selectionModel())]
            if paths:
                mime = QMimeData()
                mime.setUrls([QUrl.fromLocalFile(path) for path in paths])
                drag = QDrag(view)
                drag.setMimeData(mime)
                # Qt supplies the platform's link cursor, and the forbidden cursor
                # whenever the target rejects the drag or Alt is released.
                drag.exec(Qt.DropAction.LinkAction, Qt.DropAction.LinkAction)
                drag.deleteLater()
                return True
        elif kind == QEvent.Type.DragLeave:
            self.drag_paths = ()
        elif kind in (QEvent.Type.DragEnter, QEvent.Type.DragMove, QEvent.Type.Drop):
            if kind == QEvent.Type.DragEnter:
                urls = event.mimeData().urls()
                self.drag_paths = tuple(url.toLocalFile() for url in urls) if (
                    urls and all(url.isLocalFile() for url in urls)) else ()
            destination = self.destination(view, event.position().toPoint())
            if (event.modifiers() == Qt.KeyboardModifier.AltModifier
                    and event.possibleActions() & Qt.DropAction.LinkAction
                    and self.drag_paths
                    and destination and self.window.action_future is None):
                event.setDropAction(Qt.DropAction.LinkAction)
                event.accept()
                if kind == QEvent.Type.Drop:
                    self.window.start_item_action("Creating shortcuts…", create_shortcuts,
                                                  self.drag_paths, Path(destination))
            else:
                event.ignore()
            if kind == QEvent.Type.Drop:
                self.drag_paths = ()
            return True
        return False
