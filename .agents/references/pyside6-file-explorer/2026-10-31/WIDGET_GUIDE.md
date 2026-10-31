# FileVoyager widget guide

Design target: familiar Windows File Explorer behavior using PySide6 Qt Widgets. This is an implementation reference, not an implemented or tested UI.

## Core components

| Component / Python module | Explorer responsibility | APIs and decisions to start with |
|---|---|---|
| [QFileSystemModel](doc.qt.io/qtforpython-6/PySide6/QtWidgets/QFileSystemModel.md), QtWidgets | Files, directories, metadata | `setRootPath`, `index`, `filePath`, `isDir`, `directoryLoaded`, `setFilter`, `sort`; default columns are name, size, type, modified time |
| [QTreeView](doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeView.md), QtWidgets | Left folder tree | Show the name column; keep expansion and selection independent of the content pane |
| QTreeView, QtWidgets | Details listing | Set the current directory as root; configure flat rows with `setRootIsDecorated(False)` and `setItemsExpandable(False)`; enable sortable headers |
| [QListView](doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListView.md), QtWidgets | Icons and compact list | `setViewMode`, `setIconSize`, `setGridSize`, `setWrapping`, `setFlow`, `setResizeMode`, `setMovement`, `setLayoutMode` |
| [QSortFilterProxyModel](doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.md), QtCore | Content sort/filter | `setSourceModel`, `sort`, `lessThan`, `filterAcceptsRow`, `mapToSource`, `mapFromSource` |
| [QItemSelectionModel](doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.md), QtCore | Shared grid/Details selection | Construct against the shared content model, then assign it to both views after `setModel` |
| [QAbstractItemView](doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.md), QtWidgets | Selection and interaction conventions | `ExtendedSelection`, `SelectRows`, edit triggers, activation, context-menu and drag/drop wiring |
| [QHeaderView](doc.qt.io/qtforpython-6/PySide6/QtWidgets/QHeaderView.md), QtWidgets | Details columns | Section sizing, movement, visibility, sort indicators, `saveState` / `restoreState` |
| [QStyledItemDelegate](doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.md), QtWidgets | Thumbnail/icon and text rendering | DecorationRole for images; custom `paint` / `sizeHint` only when the required presentation exceeds standard rendering |
| [QFileIconProvider](doc.qt.io/qtforpython-6/PySide6/QtWidgets/QFileIconProvider.md), QtWidgets | File and folder icons | Filesystem-model icon provider; keep icon lookup distinct from the Windows thumbnail pipeline |

## Window and commands

| Component | Intended use | Local reference |
|---|---|---|
| QMainWindow | Toolbar, central browser area, status bar | [API](doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMainWindow.md) |
| QSplitter | Resizable navigation/content panes | [API](doc.qt.io/qtforpython-6/PySide6/QtWidgets/QSplitter.md) |
| QStackedWidget | Switch the shared-model grid and Details views | [API](doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.md) |
| QToolBar | Back, Forward, Up, and view commands | [API](doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.md) |
| QLineEdit | Editable address and search fields; breadcrumb buttons require composition | [API](doc.qt.io/qtforpython-6/PySide6/QtWidgets/QLineEdit.md) |
| QMenu | View, Sort, and context menus | [API](doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMenu.md) |
| QAction / QActionGroup (QtGui) | Shared commands and mutually exclusive view/sort choices | [QAction](doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.md), [QActionGroup](doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.md) |
| QStatusBar | Item count and current selection information | [API](doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.md) |
| QSettings (QtCore) | Window geometry, pane widths, columns, and view preferences | [API](doc.qt.io/qtforpython-6/PySide6/QtCore/QSettings.md) |
| QDir (QtCore) | Directory filters and path operations | [API](doc.qt.io/qtforpython-6/PySide6/QtCore/QDir.md) |

## Model ownership and navigation

Proposed composition:

```text
QFileSystemModel
  -> directory-only navigation proxy -> folder QTreeView (own selection)
  -> content sort/filter proxy        -> Details QTreeView
                                      -> icon/list QListView
                                         shared QItemSelectionModel
```

The directory-only proxy is application logic. Do not apply a directory-only filter to the shared filesystem source, since that would also remove files from the content pane.

Keep current directory and Back/Forward history in a navigation controller. Resolve a path to a source index, map it through the content proxy, and call `setRootIndex()` on both content views. Translate view indexes back through their proxy before invoking `filePath()` or `isDir()` on the filesystem model. Maintain ancestor visibility when filtering a hierarchical source so filtering does not remove the current root or the route to it.

The [model/view overview](doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.md) explains shared selection and model/view separation. The [official dirview example](doc.qt.io/qtforpython-6/examples/example_widgets_itemviews_dirview.md) demonstrates basic filesystem browsing; it is not a full Explorer implementation.

## View and Sort behavior

- Icons: use `QListView.ViewMode.IconMode`, explicitly configure fixed item movement, wrapping, resize adjustment, and batched layout. Map small/medium/large presets to both icon and cell sizes; these dimensions are product choices, not Explorer-compatible Qt defaults.
- Compact list: use `ListMode` and explicitly reset flow, wrapping, grid size, spacing, and movement for the intended layout. Changing only the mode does not necessarily reset properties already set by the application.
- Details: display one directory's children in the configured tree view. Let the header drive the shared content proxy's sort order so grid and Details agree.
- Sorting: route menu actions to `sort(column, Qt.SortOrder.AscendingOrder/DescendingOrder)`. Custom analysis sorting needs typed source data/roles or extra columns. A generic proxy does not guarantee Explorer's natural filename ordering or folders-first policy; specify and implement those comparisons deliberately.
- Selection: normalize selected file identities using column zero. Details row selection can produce indexes for several columns of the same file. Keep current index, selection, and scroll position as separate state concepts.
- Search: a name filter over loaded model rows is not Windows indexed recursive search. Define which behavior the search field promises before wiring it.

## Thumbnails and file operations

Expose completed thumbnails through `Qt.ItemDataRole.DecorationRole` and emit `dataChanged` for affected indexes and roles when the image changes. The [delegate behavioral reference](doc.qt.io/qt-6/qstyleditemdelegate.md) lists supported image types. Keep thumbnail acquisition out of synchronous painting/data access; model updates belong on the owning UI thread. Thumbnail size, cache invalidation, and native image ownership need an explicit implementation contract.

The existing [Windows thumbnail reference bundle](../../windows-shell-thumbnails/2026-10-31/README.md) covers the native side separately. Its presence is not evidence that a loader has been implemented.

Rename, clipboard, copy/move/delete, recycle-bin semantics, drag/drop, undo, file opening, native context menus, and special Shell locations require explicit application behavior. Enabling editing or drag/drop in a Qt view alone does not provide those Explorer semantics. Follow the project's fail-fast policy when implementing the requested path; do not introduce recovery providers or silent substitutions.
