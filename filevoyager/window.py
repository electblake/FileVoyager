from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path

import qt_themes
from PySide6.QtCore import QDir, QEvent, QItemSelectionModel, QSignalBlocker, QTimer, Qt
from PySide6.QtGui import QAction, QActionGroup
from PySide6.QtWidgets import (
    QAbstractItemView, QCheckBox, QComboBox, QHeaderView, QInputDialog, QLabel, QLineEdit,
    QMainWindow, QMenu, QSplitter, QStackedWidget, QStyle, QTableView, QToolBar, QTreeView,
)

from filevoyager.grid import ThumbnailGrid
from filevoyager.models import FileModel, MEDIA_EXTENSIONS, ThumbnailModel
from filevoyager.preferences import FolderPreferences
from filevoyager.directory_tree import DirectoryTreeModel, path_key
from filevoyager.thumbnails import ThumbnailCache, ThumbnailController
from filevoyager.similarity_dock import SimilarityDock
from filevoyager.preview_dock import PreviewDock
from filevoyager.shortcuts import KeyboardShortcutsDialog, Shortcuts, install_item_shortcuts
from filevoyager.item_actions import PackToFolderDialog, flatten_folders, join_to_folder, pack_to_folder
from filevoyager.folder_merge import FolderMerge
from filevoyager.link_drag import LinkDrag
from filevoyager.selection import selected_row_count, selected_rows
from filevoyager.themes import ThemeDialog
from filevoyager.clipboard import CutItemDelegate, FileClipboard


def resolve_directory(path):
    """Resolve and identify media folders on the navigation worker."""
    resolved = Path(path).expanduser().resolve(strict=True)
    with os.scandir(resolved) as entries:
        media = any(entry.name.rpartition(".")[2].lower() in MEDIA_EXTENSIONS
                    and entry.is_file() for entry in entries)
    return str(resolved), media


def execute_item_action(operation, args, refresh_paths, preview_future):
    if preview_future is not None:
        preview_future.result()
    result = operation(*args)
    return result, {path for path in refresh_paths if Path(path).is_dir()}


class ExplorerWindow(QMainWindow):
    def __init__(self, folder, load_image, parent=None, *, preferences=None):
        super().__init__(parent)
        self.setWindowTitle("FileVoyager")
        self.resize(1180, 780)
        self.current_path = ""
        self.preferences = FolderPreferences() if preferences is None else preferences
        self.themes = qt_themes.get_themes()
        qt_themes.set_theme(self.themes[
            self.preferences.settings.value("appearance/theme", "github_light", type=str)])
        self.theme_dialog = None
        self.shortcuts = Shortcuts(self.preferences.settings)
        self.shortcuts_dialog = None
        self.folder_state = None
        self.pending_restore = False
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
        self.action_executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="item-actions")
        self.action_future = None
        self.action_timer = QTimer(self)
        self.action_timer.setInterval(50)
        self.action_timer.timeout.connect(self.finish_item_action)
        self.pack_dialog = None
        self.join_dialog = None
        self.folder_merge = FolderMerge(self)

        style = self.style()
        folder_icon = style.standardIcon(QStyle.StandardPixmap.SP_DirIcon)
        file_icon = style.standardIcon(QStyle.StandardPixmap.SP_FileIcon)
        self.files = FileModel(folder_icon, file_icon, self)
        self.files.folderMergeRequested.connect(self.merge_renamed_folder)
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
            self.folders.navigation_path(index)))
        self.tree.doubleClicked.connect(lambda index: self.navigate(
            self.folders.navigation_path(index)))
        self.tree.expanded.connect(self.folders.expanded)
        self.folders.pathReady.connect(self.select_tree_index)

        self.details = QTableView()
        self.details.setModel(self.model)
        self.details.setShowGrid(False)
        self.details.verticalHeader().hide()
        self.details.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        self.details.verticalHeader().setDefaultSectionSize(self.details.fontMetrics().height() + 4)
        self.details.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.details.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.details.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.details.setSortingEnabled(True)
        self.details.sortByColumn(0, Qt.SortOrder.AscendingOrder)
        self.details.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        self.details.horizontalHeader().setStretchLastSection(True)
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
        self.rename_actions = {view: install_item_shortcuts(view) for view in (self.details, self.grid)}
        self.shortcuts.add("rename", "Rename", "F2", *self.rename_actions.values())
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

        self.preview_dock = PreviewDock(load_image, self)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.preview_dock)
        self.selection.currentChanged.connect(self.update_preview_selection)
        self.selection.selectionChanged.connect(self.update_preview_selection)
        self.addAction(self.preview_dock.toggleViewAction())
        self.shortcuts.add("preview", "Toggle preview", "Ctrl+Shift+P", self.preview_dock.toggleViewAction())
        self.similarity_dock = SimilarityDock(load_image, self)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.similarity_dock)
        self.splitDockWidget(self.preview_dock, self.similarity_dock, Qt.Orientation.Vertical)
        self.resizeDocks([self.preview_dock, self.similarity_dock], [420, 300], Qt.Orientation.Vertical)
        self.similarity_dock.orderReady.connect(self.apply_image_order)
        self.similarity_dock.clearRequested.connect(self.clear_image_order)
        self.selection.selectionChanged.connect(self.update_similarity_selection)
        self.files.fileRenamed.connect(self.update_preview_selection)
        self.files.fileRenamed.connect(self.update_similarity_selection)
        self.addAction(self.similarity_dock.toggleViewAction())
        self.shortcuts.add("similarity", "Toggle media similarity", "Ctrl+Shift+S",
                           self.similarity_dock.toggleViewAction())

        self.thumbnails = ThumbnailController(self.grid, self.model, load_image, self)
        self.update_dialog = None
        self.explorer_install_dialog = None
        file_menu = self.menuBar().addMenu("&File")
        quit_action = file_menu.addAction("&Quit")
        self.shortcuts.add("quit", "Quit", "Ctrl+Q", quit_action)
        quit_action.triggered.connect(self.close)
        self.edit_menu = self.menuBar().addMenu("&Edit")
        view_menu = self.menuBar().addMenu("&View")
        view_menu.addAction("&Theme…", self.show_theme)
        help_menu = self.menuBar().addMenu("&Help")
        updates_action = help_menu.addAction("Check for updates…", self.show_updates)
        self.shortcuts.add("updates", "Check for updates", "", updates_action)
        shortcuts_action = help_menu.addAction("Keyboard Shortcuts…", self.show_shortcuts)
        self.shortcuts.add("keyboard_shortcuts", "Keyboard Shortcuts", "", shortcuts_action)
        help_menu.addAction("Install in File Explorer", self.show_explorer_install)
        self.build_toolbar()
        self.build_actions_toolbar()
        self.file_clipboard = FileClipboard(self)
        self.details.setItemDelegate(CutItemDelegate(self.details))
        self.tree.setItemDelegate(CutItemDelegate(self.tree))
        self.edit_menu.aboutToShow.connect(self.file_clipboard.show_edit_menu)
        self.file_clipboard.show_edit_menu()
        self.item_menus = {}
        self.background_menus = {}
        for view in (self.details, self.grid):
            menu = QMenu(view)
            menu.addActions(self.file_clipboard.actions[view][:2])
            self.file_clipboard.context_actions[view] = menu.addAction("&Paste", lambda: self.file_clipboard.paste(
                self.file_clipboard.context_destination()))
            menu.addAction(self.rename_actions[view])
            menu.addSeparator()
            menu.addActions([self.flatten_action, self.pack_action, self.join_action])
            self.item_menus[view] = menu
            background = QMenu(view)
            background.addAction(self.file_clipboard.actions[view][2])
            self.background_menus[view] = background
            view.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
            view.viewport().installEventFilter(self)
            view.customContextMenuRequested.connect(lambda point, target=view: self.show_item_menu(target, point))
        self.tree_item_menu = QMenu(self.tree)
        self.tree_item_menu.addActions(self.file_clipboard.actions[self.tree])
        self.tree_rename_action = self.tree_item_menu.addAction("Rename", self.rename_tree_item)
        self.tree_item_menu.addSeparator()
        self.tree_flatten_action = self.tree_item_menu.addAction("Flatten", lambda: self.start_item_action(
            "Flattening selected folders…", flatten_folders, (self.tree_action_path,),
            refresh_paths=(self.tree_action_path,)))
        self.tree_pack_action = self.tree_item_menu.addAction("Pack to Folder…", lambda: self.show_pack_dialog(
            paths=(self.tree_action_path,)))
        self.tree_join_action = self.tree_item_menu.addAction("Join to Folder…", lambda: self.show_join_dialog(
            paths=(self.tree_action_path,)))
        self.tree.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.show_tree_item_menu)
        self.link_drag = LinkDrag(self)
        self.status = QLabel()
        self.statusBar().addWidget(self.status, 1)
        self.selection.selectionChanged.connect(self.update_status)
        self.files.rowsInserted.connect(self.update_status)
        self.files.rowsRemoved.connect(self.update_status)
        self.files.directoryLoaded.connect(self.directory_loaded)
        self.restore_app_state()
        history_position = None
        if folder is None:
            folder = self.preferences.settings.value("last_folder", str(Path.home()), type=str)
            if self.preferences.settings.contains("navigation/history"):
                self.history = json.loads(self.preferences.settings.value("navigation/history", type=str))
                self.history_position = self.preferences.settings.value("navigation/position", type=int)
                history_position = self.history_position
        self.navigate(folder, history_position)

    def restore_app_state(self):
        settings = self.preferences.settings
        if settings.contains("window/geometry"):
            self.restoreGeometry(settings.value("window/geometry"))
        if settings.contains("window/state"):
            self.restoreState(settings.value("window/state"))
        if settings.contains("window/splitter"):
            self.centralWidget().restoreState(settings.value("window/splitter"))
        if settings.contains("details/header"):
            header = self.details.horizontalHeader()
            header.restoreState(settings.value("details/header"))
            self.details.sortByColumn(header.sortIndicatorSection(), header.sortIndicatorOrder())
        if settings.contains("similarity/eps"):
            self.similarity_dock.eps.setValue(settings.value("similarity/eps", type=float))
        if settings.contains("similarity/min_samples"):
            self.similarity_dock.min_samples.setValue(settings.value("similarity/min_samples", type=int))
        for index, spin in enumerate(self.similarity_dock.weights):
            key = f"similarity/weights/{index}"
            if settings.contains(key):
                spin.setValue(settings.value(key, type=float))

    def save_app_state(self):
        settings = self.preferences.settings
        settings.setValue("window/geometry", self.saveGeometry())
        settings.setValue("window/state", self.saveState())
        settings.setValue("window/splitter", self.centralWidget().saveState())
        settings.setValue("details/header", self.details.horizontalHeader().saveState())
        settings.setValue("similarity/eps", self.similarity_dock.eps.value())
        settings.setValue("similarity/min_samples", self.similarity_dock.min_samples.value())
        for index, spin in enumerate(self.similarity_dock.weights):
            settings.setValue(f"similarity/weights/{index}", spin.value())
        if self.current_path:
            settings.setValue("navigation/history", json.dumps(self.history))
            settings.setValue("navigation/position", self.history_position)

    def show_theme(self):
        if self.theme_dialog is not None:
            self.theme_dialog.deleteLater()
        self.theme_dialog = ThemeDialog(self.themes, self.preferences.settings, self)
        self.theme_dialog.open()

    def show_updates(self):
        from filevoyager.updates import UpdateDialog

        if self.update_dialog is not None:
            self.update_dialog.deleteLater()
        self.update_dialog = UpdateDialog(self)
        self.update_dialog.open()

    def show_explorer_install(self):
        from filevoyager.explorer_install import ExplorerInstallDialog

        if self.explorer_install_dialog is not None:
            self.explorer_install_dialog.deleteLater()
        self.explorer_install_dialog = ExplorerInstallDialog(self)
        self.explorer_install_dialog.open()

    def show_shortcuts(self):
        if self.shortcuts_dialog is not None:
            self.shortcuts_dialog.deleteLater()
        self.shortcuts_dialog = KeyboardShortcutsDialog(self.shortcuts, self)
        self.shortcuts_dialog.open()

    def build_toolbar(self):
        toolbar = QToolBar("Navigation")
        toolbar.setObjectName("navigationToolbar")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        style = self.style()
        self.back_action = QAction(style.standardIcon(QStyle.StandardPixmap.SP_ArrowBack), "Back", self)
        self.shortcuts.add("back", "Back", "Alt+Left", self.back_action)
        self.back_action.triggered.connect(lambda: self.travel(-1))
        self.forward_action = QAction(style.standardIcon(QStyle.StandardPixmap.SP_ArrowForward), "Forward", self)
        self.shortcuts.add("forward", "Forward", "Alt+Right", self.forward_action)
        self.forward_action.triggered.connect(lambda: self.travel(1))
        self.up_action = QAction(style.standardIcon(QStyle.StandardPixmap.SP_ArrowUp), "Up", self)
        self.shortcuts.add("up", "Up", "Alt+Up", self.up_action)
        self.up_action.triggered.connect(lambda: self.navigate(str(Path(self.current_path).parent)))
        self.refresh_action = QAction(style.standardIcon(QStyle.StandardPixmap.SP_BrowserReload), "Refresh", self)
        self.shortcuts.add("refresh", "Refresh", "F5", self.refresh_action)
        self.refresh_action.triggered.connect(lambda: self.files.request(self.files.current, True))
        self.refresh_action.triggered.connect(lambda: self.folders.directory_changed(self.current_path))
        toolbar.addActions([self.back_action, self.forward_action, self.up_action, self.refresh_action])
        self.address = QLineEdit()
        self.address.setPlaceholderText("Folder path")
        self.address.setClearButtonEnabled(True)
        self.address.returnPressed.connect(lambda: self.navigate(self.address.text()))
        toolbar.addWidget(self.address)
        focus_address = QAction(self)
        self.shortcuts.add("address", "Focus address bar", "Ctrl+L", focus_address)
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
            self.shortcuts.add(label.lower() + "_view", label + " view", "", action)
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

    def build_actions_toolbar(self):
        self.addToolBarBreak()
        toolbar = QToolBar("Selected items")
        toolbar.setObjectName("itemActionsToolbar")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        self.select_mode = QCheckBox("Select")
        self.select_mode.setToolTip("On: drag to select items. Off: drag items to move them. Alt-drag creates shortcuts.")
        self.select_mode.setChecked(self.preferences.settings.value("interaction/select_mode", False, type=bool))
        self.select_mode.toggled.connect(lambda checked: self.preferences.settings.setValue(
            "interaction/select_mode", checked))
        toolbar.addWidget(self.select_mode)
        toolbar.addSeparator()
        self.pack_action = toolbar.addAction("Pack to Folder…", self.show_pack_dialog)
        self.pack_action.setToolTip("Move or copy selected items into a new folder")
        self.join_action = toolbar.addAction("Join to Folder…", self.show_join_dialog)
        self.join_action.setToolTip("Move or copy the contents of selected folders into one new folder")
        self.flatten_action = toolbar.addAction("Flatten", self.flatten_selection)
        self.shortcuts.add("pack", "Pack to Folder", "", self.pack_action)
        self.shortcuts.add("join", "Join to Folder", "", self.join_action)
        self.shortcuts.add("flatten", "Flatten", "", self.flatten_action)
        self.flatten_action.setToolTip(
            "Move nested files into each selected folder and remove its emptied subfolders")
        self.action_status = QLabel()
        toolbar.addWidget(self.action_status)
        self.selection.selectionChanged.connect(self.update_item_actions)
        self.update_item_actions()

    def update_item_actions(self, *args):
        available = self.action_future is None and self.selection.hasSelection()
        self.pack_action.setEnabled(available)
        self.flatten_action.setEnabled(available and all(
            self.files.isDir(self.model.mapToSource(index)) for index in selected_rows(self.selection)))
        self.join_action.setEnabled(self.flatten_action.isEnabled())

    def selected_item_paths(self):
        return tuple(Path(self.files.filePath(self.model.mapToSource(index)))
                     for index in selected_rows(self.selection))

    def eventFilter(self, watched, event):
        if (event.type() in (QEvent.Type.MouseButtonPress, QEvent.Type.MouseButtonRelease)
                and event.button() == Qt.MouseButton.RightButton
                and watched in (self.details.viewport(), self.grid.viewport())
                and selected_row_count(self.selection) > 1):
            # Keep the selected batch before Qt's mouse handling can replace it.
            return True
        return super().eventFilter(watched, event)

    def show_item_menu(self, view, point):
        index = view.indexAt(point)
        if not index.isValid():
            self.selection.clearSelection()
            view.setFocus()
            self.file_clipboard.update()
            self.background_menus[view].popup(view.viewport().mapToGlobal(point))
            return
        if selected_row_count(self.selection) <= 1 and not self.selection.isSelected(index):
            self.selection.setCurrentIndex(index, QItemSelectionModel.SelectionFlag.ClearAndSelect
                                           | QItemSelectionModel.SelectionFlag.Rows)
        view.setFocus()
        self.file_clipboard.update()
        self.item_menus[view].popup(view.viewport().mapToGlobal(point))

    def show_tree_item_menu(self, point):
        index = self.tree.indexAt(point)
        if not index.isValid() or not index.data(Qt.ItemDataRole.UserRole):
            return
        self.tree_action_path = Path(self.folders.file_path(index))
        self.tree.setCurrentIndex(index)
        self.tree.setFocus()
        self.file_clipboard.update()
        available = self.action_future is None
        shortcut = bool(index.data(Qt.ItemDataRole.UserRole + 1))
        self.tree_flatten_action.setEnabled(available and not shortcut)
        self.tree_pack_action.setEnabled(available and self.tree_action_path.parent != self.tree_action_path)
        self.tree_join_action.setEnabled(self.tree_pack_action.isEnabled() and not shortcut)
        self.tree_rename_action.setEnabled(available and self.tree_action_path.parent != self.tree_action_path)
        self.tree_item_menu.popup(self.tree.viewport().mapToGlobal(point))

    def rename_tree_item(self):
        path = self.tree_action_path
        dialog = QInputDialog(self)
        dialog.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        dialog.setWindowTitle("Rename folder")
        dialog.setLabelText("New folder name:")
        dialog.setTextValue(path.name)
        dialog.textValueSelected.connect(lambda name: self.files.rename_path(str(path), name))
        dialog.open()

    def show_pack_dialog(self, *, paths=None):
        if paths is None:
            paths = self.selected_item_paths()
        parent = paths[0].parent
        if self.pack_dialog is not None:
            self.pack_dialog.deleteLater()
        dialog = PackToFolderDialog(self)
        self.pack_dialog = dialog
        dialog.accepted.connect(lambda: self.start_item_action(
            "Packing selected items…", pack_to_folder, paths,
            parent / dialog.folder_name.text(), dialog.copy_mode.isChecked(),
            self.folder_merge.ask,
            refresh_paths=(parent, *paths, parent / dialog.folder_name.text())))
        dialog.open()

    def show_join_dialog(self, *, paths=None):
        if paths is None:
            paths = self.selected_item_paths()
        parent = paths[0].parent
        if self.join_dialog is not None:
            self.join_dialog.deleteLater()
        dialog = PackToFolderDialog(self)
        dialog.setWindowTitle("Join to Folder")
        self.join_dialog = dialog
        dialog.accepted.connect(lambda: self.start_item_action(
            "Joining selected folder contents…", join_to_folder, paths,
            parent / dialog.folder_name.text(), dialog.copy_mode.isChecked(),
            self.folder_merge.ask,
            refresh_paths=(parent, *paths, parent / dialog.folder_name.text())))
        dialog.open()

    def flatten_selection(self):
        paths = self.selected_item_paths()
        self.start_item_action("Flattening selected folders…", flatten_folders,
                               paths, refresh_paths=paths)

    def merge_renamed_folder(self, source, destination):
        self.start_item_action("Merging folders…", self.folder_merge.merge, source, destination,
                               refresh_paths=(Path(source).parent, destination))

    def start_item_action(self, label, operation, *args, refresh_paths):
        self.action_refresh_paths = {path_key(path) for path in refresh_paths}
        self.files.setReadOnly(True)
        self.preview_dock.set_item("")
        self.action_future = self.action_executor.submit(execute_item_action, operation, args,
                                                         self.action_refresh_paths, self.preview_dock.future)
        self.file_clipboard.update()
        self.action_status.setText(label)
        self.update_item_actions()
        self.action_timer.start()

    def finish_item_action(self):
        if not self.action_future.done():
            return
        self.action_timer.stop()
        future = self.action_future
        self.action_future = None
        self.action_status.clear()
        self.files.setReadOnly(False)
        self.update_item_actions()
        result, refresh_paths = future.result()
        self.file_clipboard.finish()
        for key in self.action_refresh_paths - refresh_paths:
            if key in self.files.recent:
                root = self.files.recent.pop(key)
                self.files.watcher.removePath(root.path)
                self.files.directory_changed(root.path)
        if path_key(self.current_path) in self.action_refresh_paths - refresh_paths:
            self.navigate(str(next(path for path in Path(self.current_path).parents
                                   if path_key(path) in refresh_paths)))
        for key in refresh_paths:
            if key in self.files.recent:
                self.files.request(self.files.recent[key], True)
            for branch in self.folders.watched_nodes.get(key, ()):
                if self.folders.nodes[branch].loaded:
                    self.folders.request_scan(self.folders.nodes[branch].path)
        if path_key(self.current_path) not in self.action_refresh_paths:
            self.update_preview_selection()
        self.action_refresh_paths.clear()
        self.action_status.setText("Action complete" if result is None else result)

    def navigate(self, path, history_position=None):
        self.preview_dock.set_item("")
        self.similarity_dock.set_folder("")
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
        self.file_clipboard.update()
        if self.model.ranks is not None:
            self.clear_image_order()
        self.similarity_dock.set_folder(path)
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
            self.folders.reveal_path(self.current_path, self.tree.currentIndex())

    def select_tree_index(self, index):
        self.tree.setCurrentIndex(index)
        self.tree.scrollTo(index, QAbstractItemView.ScrollHint.PositionAtCenter)

    def update_navigation_actions(self):
        self.back_action.setEnabled(self.history_position > 0)
        self.forward_action.setEnabled(self.history_position + 1 < len(self.history))
        self.up_action.setEnabled(bool(self.current_path) and str(Path(self.current_path).parent) != self.current_path)
        self.refresh_action.setEnabled(bool(self.current_path))

    def activate(self, index):
        source_index = self.model.mapToSource(index)
        path = self.files.navigation_path(source_index)
        if path:
            self.navigate(path)

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
        if QDir.cleanPath(path) == QDir.cleanPath(self.current_path):
            self.update_status()
            self.update_preview_selection()
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
            self.preferences.settings.setValue("last_folder", self.current_path)
            self.preferences.save(self.current_path, self.folder_state)

    def schedule_scroll_restore(self, *args):
        if self.pending_restore:
            self.restore_timer.start(0)

    def restore_scroll(self):
        if not self.pending_restore:
            return
        if not self.files.is_loaded(self.current_path):
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
        selected = selected_row_count(self.selection)
        self.status.setText(f"{count:,} items   ·   {selected:,} selected")

    def update_preview_selection(self, *args):
        if self.action_future is not None:
            return
        index = self.selection.currentIndex()
        if not index.isValid() or not self.selection.isSelected(index):
            index = next(selected_rows(self.selection), None)
            if index is None:
                self.preview_dock.set_item("")
                return
        source = self.model.mapToSource(index.siblingAtColumn(0))
        path = self.files.filePath(source)
        media = (path.rpartition(".")[2].lower() in MEDIA_EXTENSIONS
                 and not self.files.isDir(source))
        self.preview_dock.set_item(path, media)

    def update_similarity_selection(self, *args):
        paths = []
        for index in selected_rows(self.selection):
            source = self.model.mapToSource(index)
            if not self.files.isDir(source):
                paths.append(self.files.filePath(source))
                # The dock only uses a reference when exactly one file is selected.
                if len(paths) == 2:
                    break
        self.similarity_dock.set_selection(paths)

    def apply_image_order(self, result):
        self.thumbnails.set_enabled(False)
        self.model.set_image_order(result.paths[index] for index in result.order)
        self.thumbnails.set_enabled(self.views.currentWidget() is self.grid)
        self.thumbnails.schedule()

    def clear_image_order(self):
        self.model.sort(0, Qt.SortOrder.AscendingOrder)
        with QSignalBlocker(self.details.horizontalHeader()):
            self.details.horizontalHeader().setSortIndicator(0, Qt.SortOrder.AscendingOrder)

    def closeEvent(self, event):
        if self.action_future is not None:
            event.ignore()
            return
        if self.update_dialog is not None and self.update_dialog.future is not None:
            event.ignore()
            return
        if self.explorer_install_dialog is not None and self.explorer_install_dialog.future is not None:
            event.ignore()
            return
        self.save_folder_state()
        self.preview_dock.shutdown()
        self.similarity_dock.shutdown()
        self.save_app_state()
        self.preferences.settings.sync()
        if self.update_dialog is not None:
            self.update_dialog.close()
        if self.explorer_install_dialog is not None:
            self.explorer_install_dialog.close()
        self.restore_timer.stop()
        self.navigation_timer.stop()
        self.navigation_executor.shutdown(wait=True, cancel_futures=True)
        self.action_timer.stop()
        self.action_executor.shutdown(wait=True)
        if self.navigation_future is not None:
            self.navigation_future.result()
        self.folders.close()
        self.thumbnails.close()
        self.files.close()
        super().closeEvent(event)
