from concurrent.futures import ThreadPoolExecutor
import os
from pathlib import Path

from PySide6.QtCore import QDir, QItemSelectionModel, QSignalBlocker, QTimer, Qt
from PySide6.QtGui import QAction, QActionGroup, QKeySequence
from PySide6.QtWidgets import (
    QAbstractItemView, QComboBox, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QSplitter, QStackedWidget, QStyle, QToolBar, QTreeView,
)

from filevoyager.grid import ThumbnailGrid
from filevoyager.models import FileModel, MEDIA_EXTENSIONS, ThumbnailModel
from filevoyager.preferences import FolderPreferences
from filevoyager.directory_tree import DirectoryTreeModel
from filevoyager.thumbnails import ThumbnailCache, ThumbnailController


def resolve_directory(path):
    """Resolve and identify media folders on the navigation worker."""
    resolved = Path(path).expanduser().resolve(strict=True)
    with os.scandir(resolved) as entries:
        media = any(entry.name.rpartition(".")[2].lower() in MEDIA_EXTENSIONS
                    and entry.is_file() for entry in entries)
    return str(resolved), media


class ExplorerWindow(QMainWindow):
    def __init__(self, folder, load_image, parent=None, *, preferences=None):
        super().__init__(parent)
        self.setWindowTitle("FileVoyager")
        self.resize(1180, 780)
        self.current_path = ""
        self.preferences = FolderPreferences() if preferences is None else preferences
        self.folder_state = None
        self.pending_restore = False
        self.loaded_paths = set()
        self.restore_timer = QTimer(self)
        self.restore_timer.setSingleShot(True)
        self.restore_timer.timeout.connect(self.restore_scroll)
        self.history = []
        self.history_position = -1
        self.navigation_serial = 0
        self.navigation_future = None
        self.navigation_pending = None
        self.navigation_executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="navigation")
        self.navigation_timer = QTimer(self)
        self.navigation_timer.setInterval(16)
        self.navigation_timer.timeout.connect(self.finish_navigation)

        style = self.style()
        folder_icon = style.standardIcon(QStyle.StandardPixmap.SP_DirIcon)
        file_icon = style.standardIcon(QStyle.StandardPixmap.SP_FileIcon)
        self.files = FileModel(folder_icon, file_icon, self)
        self.files.setFilter(QDir.Filter.AllDirs | QDir.Filter.Files | QDir.Filter.NoDotAndDotDot)
        self.folders = DirectoryTreeModel(folder_icon, self)
        self.cache = ThumbnailCache()
        self.model = ThumbnailModel(self.files, self.cache, self)

        self.tree = QTreeView()
        self.tree.setModel(self.folders)
        self.tree.setHeaderHidden(True)
        self.tree.setUniformRowHeights(True)
        self.tree.setAnimated(False)
        self.tree.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree.clicked.connect(lambda index: self.navigate(
            self.folders.file_path(index)))
        self.tree.expanded.connect(self.folders.expanded)
        self.folders.pathReady.connect(self.select_tree_index)

        self.details = QTreeView()
        self.details.setModel(self.model)
        self.details.setRootIsDecorated(False)
        self.details.setItemsExpandable(False)
        self.details.setUniformRowHeights(True)
        self.details.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.details.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.details.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.details.setSortingEnabled(True)
        self.details.sortByColumn(0, Qt.SortOrder.AscendingOrder)
        self.details.header().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        self.details.header().setStretchLastSection(True)
        self.details.setColumnWidth(0, 380)
        self.details.setColumnWidth(1, 100)
        self.details.setColumnWidth(2, 130)
        self.details.setColumnWidth(3, 180)

        self.grid = ThumbnailGrid()
        self.grid.setModel(self.model)
        self.grid.layoutReady.connect(self.schedule_scroll_restore)
        for view in (self.details, self.grid):
            view.verticalScrollBar().rangeChanged.connect(self.schedule_scroll_restore)
            view.horizontalScrollBar().rangeChanged.connect(self.schedule_scroll_restore)
        self.selection = QItemSelectionModel(self.model, self)
        self.details.setSelectionModel(self.selection)
        self.grid.setSelectionModel(self.selection)
        self.details.activated.connect(self.activate)
        self.grid.activated.connect(self.activate)

        self.views = QStackedWidget()
        self.views.addWidget(self.details)
        self.views.addWidget(self.grid)
        splitter = QSplitter()
        splitter.addWidget(self.tree)
        splitter.addWidget(self.views)
        splitter.setSizes([240, 940])
        splitter.setCollapsible(0, False)
        splitter.setCollapsible(1, False)
        self.setCentralWidget(splitter)

        self.thumbnails = ThumbnailController(self.grid, self.model, load_image, self)
        self.build_toolbar()
        self.status = QLabel()
        self.statusBar().addWidget(self.status, 1)
        self.selection.selectionChanged.connect(self.update_status)
        self.files.rowsInserted.connect(self.update_status)
        self.files.rowsRemoved.connect(self.update_status)
        self.files.directoryLoaded.connect(self.directory_loaded)
        self.navigate(folder)

    def build_toolbar(self):
        toolbar = QToolBar("Navigation")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        self.back_action = QAction("Back", self)
        self.back_action.setShortcut(QKeySequence("Alt+Left"))
        self.back_action.triggered.connect(lambda: self.travel(-1))
        self.forward_action = QAction("Forward", self)
        self.forward_action.setShortcut(QKeySequence("Alt+Right"))
        self.forward_action.triggered.connect(lambda: self.travel(1))
        self.up_action = QAction("Up", self)
        self.up_action.setShortcut(QKeySequence("Alt+Up"))
        self.up_action.triggered.connect(lambda: self.navigate(str(Path(self.current_path).parent)))
        toolbar.addActions([self.back_action, self.forward_action, self.up_action])
        self.address = QLineEdit()
        self.address.setPlaceholderText("Folder path")
        self.address.setClearButtonEnabled(True)
        self.address.returnPressed.connect(lambda: self.navigate(self.address.text()))
        toolbar.addWidget(self.address)
        focus_address = QAction(self)
        focus_address.setShortcut(QKeySequence("Ctrl+L"))
        focus_address.triggered.connect(self.focus_address)
        self.addAction(focus_address)

        toolbar.addSeparator()
        group = QActionGroup(self)
        self.view_actions = {}
        for label, view in [("Details", self.details), ("Grid", self.grid)]:
            action = QAction(label, self)
            action.setCheckable(True)
            action.setChecked(view is self.details)
            action.triggered.connect(lambda checked, target=view: self.switch_view(target))
            group.addAction(action)
            self.view_actions[view] = action
            toolbar.addAction(action)
        self.icon_size = QComboBox()
        for label, pixels in [("Small", 80), ("Medium", 128), ("Large", 192)]:
            self.icon_size.addItem(label, pixels)
        self.icon_size.setCurrentIndex(1)
        self.icon_size.currentIndexChanged.connect(self.resize_thumbnails)
        self.icon_size.setEnabled(False)
        toolbar.addWidget(self.icon_size)
        self.update_navigation_actions()

    def focus_address(self):
        self.address.setFocus()
        self.address.selectAll()

    def navigate(self, path, history_position=None):
        self.navigation_serial += 1
        self.navigation_pending = (self.navigation_serial, path, history_position)
        self.start_navigation()

    def start_navigation(self):
        if self.navigation_future is None and self.navigation_pending is not None:
            self.navigation_request = self.navigation_pending
            self.navigation_pending = None
            self.navigation_future = self.navigation_executor.submit(
                resolve_directory, self.navigation_request[1])
            self.navigation_timer.start()
            self.status.setText("Opening folder…")

    def finish_navigation(self):
        if self.navigation_future is None or not self.navigation_future.done():
            return
        future = self.navigation_future
        self.navigation_future = None
        self.navigation_timer.stop()
        path, media_folder = future.result()
        serial, _, history_position = self.navigation_request
        if serial == self.navigation_serial:
            self.apply_directory(path, history_position, media_folder)
        self.start_navigation()

    def apply_directory(self, path, history_position, media_folder):
        self.save_folder_state()
        self.restore_timer.stop()
        self.thumbnails.set_enabled(False)
        if history_position is not None:
            self.history_position = history_position
        elif path != self.current_path:
            del self.history[self.history_position + 1:]
            self.history.append(path)
            self.history_position = len(self.history) - 1
        self.current_path = path
        self.folder_state = self.preferences.load(path, media_folder)
        self.pending_restore = True
        with QSignalBlocker(self.icon_size):
            self.icon_size.setCurrentIndex(self.icon_size.findData(self.folder_state["size"]))
        self.grid.set_thumbnail_size(self.folder_state["size"])
        self.address.setText(path)
        self.setWindowTitle(f"{path} — FileVoyager")
        self.thumbnails.invalidate()
        root = self.model.mapFromSource(self.files.setRootPath(path))
        self.selection.clear()
        self.details.setRootIndex(root)
        self.grid.setRootIndex(root)
        view = {"grid": self.grid, "details": self.details}[self.folder_state["view"]]
        self.views.setCurrentWidget(view)
        self.view_actions[view].setChecked(True)
        self.icon_size.setEnabled(view is self.grid)
        self.sync_tree()
        self.update_navigation_actions()
        self.update_status()
        self.schedule_scroll_restore()

    def travel(self, offset):
        position = self.history_position + offset
        self.navigate(self.history[position], position)

    def sync_tree(self, *args):
        if self.current_path:
            self.folders.reveal_path(self.current_path)

    def select_tree_index(self, index):
        self.tree.setCurrentIndex(index)
        self.tree.scrollTo(index, QAbstractItemView.ScrollHint.PositionAtCenter)

    def update_navigation_actions(self):
        self.back_action.setEnabled(self.history_position > 0)
        self.forward_action.setEnabled(self.history_position + 1 < len(self.history))
        self.up_action.setEnabled(bool(self.current_path) and str(Path(self.current_path).parent) != self.current_path)

    def activate(self, index):
        source_index = self.model.mapToSource(index)
        if self.files.isDir(source_index):
            self.navigate(self.files.filePath(source_index))

    def switch_view(self, view):
        self.capture_scroll()
        self.folder_state["view"] = "grid" if view is self.grid else "details"
        self.pending_restore = True
        self.thumbnails.set_enabled(False)
        self.view_actions[view].setChecked(True)
        self.views.setCurrentWidget(view)
        self.icon_size.setEnabled(view is self.grid)
        self.schedule_scroll_restore()

    def resize_thumbnails(self):
        self.folder_state["size"] = self.icon_size.currentData()
        self.grid.set_thumbnail_size(self.icon_size.currentData())
        self.thumbnails.invalidate()

    def directory_loaded(self, path):
        self.loaded_paths.add(QDir.cleanPath(path))
        if QDir.cleanPath(path) == QDir.cleanPath(self.current_path):
            self.update_status()
            self.thumbnails.schedule()
            self.schedule_scroll_restore()

    def capture_scroll(self):
        if self.folder_state is not None and not self.pending_restore:
            view = self.views.currentWidget()
            name = "grid" if view is self.grid else "details"
            self.folder_state[name] = [view.verticalScrollBar().value(),
                                       view.horizontalScrollBar().value()]

    def save_folder_state(self):
        if self.current_path:
            self.capture_scroll()
            self.preferences.save(self.current_path, self.folder_state)

    def schedule_scroll_restore(self, *args):
        if self.pending_restore:
            self.restore_timer.start(0)

    def restore_scroll(self):
        if not self.pending_restore:
            return
        if QDir.cleanPath(self.current_path) not in self.loaded_paths:
            return
        view = self.views.currentWidget()
        view.executeDelayedItemsLayout()
        if view is self.grid and not self.grid.layout_complete:
            return
        self.finish_scroll_restore()

    def finish_scroll_restore(self):
        if not self.pending_restore:
            return
        view = self.views.currentWidget()
        vertical, horizontal = self.folder_state[self.folder_state["view"]]
        # Qt clamps positions when a folder has shrunk since the saved visit.
        view.verticalScrollBar().setValue(vertical)
        view.horizontalScrollBar().setValue(horizontal)
        self.pending_restore = False
        self.thumbnails.set_enabled(view is self.grid)

    def update_status(self, *args):
        count = self.model.rowCount(self.details.rootIndex())
        selected = len(self.selection.selectedRows(0))
        self.status.setText(f"{count:,} items   ·   {selected:,} selected")

    def closeEvent(self, event):
        self.save_folder_state()
        self.restore_timer.stop()
        self.navigation_timer.stop()
        self.navigation_executor.shutdown(wait=True, cancel_futures=True)
        if self.navigation_future is not None:
            self.navigation_future.result()
        self.folders.close()
        self.thumbnails.close()
        super().closeEvent(event)
