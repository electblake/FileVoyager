# Reference summary

## Version and provenance

- Reference date: 2026-10-31, America/Toronto.
- Platform: Qt Widgets through PySide6 (Qt for Python).
- Captured Qt C++ class pages identify **Qt 6.12.0**; the captured PySide6 release notes begin with **6.12.0**. These are documentation versions, not evidence of the locally installed package or a chosen application pin.
- The rolling `/qt-6/` and `/qtforpython-6/` URLs can change. Retrieval timestamps and final URLs are recorded in each mirrored page; retain this dated snapshot.
- The [Getting Started page](doc.qt.io/qtforpython-6/gettingstarted.md) specifies Python 3.10+. Project `mise.toml` requests Python 3.12. Actual runtime and wheel compatibility have not been tested.
- The [release notes](doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.md) record a 6.12 deployment change: pyside6-deploy defaults to standalone output; `--onefile` requests the former default. This affects future packaging, not widget composition.
- [QSortFilterProxyModel](doc.qt.io/qt-6/qsortfilterproxymodel.md) marks `beginFilterChange()` as introduced in 6.9 and `endFilterChange()` in 6.10. Its older filter invalidation methods are marked until 6.13. Check the selected runtime before adopting version-specific APIs.
- Python docs warn that some examples are translated from C++. Use Python API signatures and scoped enums when implementing.

## Official documentation findings

1. [QFileSystemModel](doc.qt.io/qt-6/qfilesystemmodel.md) populates asynchronously after `setRootPath()`, caches filesystem information, and watches changes. Its owning thread needs an event loop. A zero row count during population does not establish an empty directory.
2. `setRootPath()` starts population and watching; it does not constrain what a view displays. Set each content view's root index separately.
3. [QTreeView](doc.qt.io/qt-6/qtreeview.md) supplies hierarchical and multicolumn presentation. [QListView](doc.qt.io/qt-6/qlistview.md) supplies list and icon modes, cell sizing, wrapping, and batched layout.
4. [Shared selection](doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.md) requires views attached to the same model. Proxy indexes must be mapped to source indexes before calling filesystem-specific methods.
5. [QStyledItemDelegate](doc.qt.io/qt-6/qstyleditemdelegate.md) accepts QIcon, QPixmap, and QImage through DecorationRole. Native thumbnail acquisition and cache policy remain application integration work.
6. QFileSystemModel is read-only by default. Its filesystem mutation APIs do not establish Windows Shell operation parity.

## Application interpretation

Use the built-in model/view stack as the foundation. Windows Explorer fidelity still requires navigation history, breadcrumbs, command wiring, view presets, selection conventions, file operations, and Windows Shell integration. A filesystem hierarchy alone does not implement the whole Explorer shell namespace or its special locations.

The [widget guide](WIDGET_GUIDE.md) records the proposed composition separately from the vendor API facts. Third-party release dates, licenses, and compatibility statements from the user's pasted text remain unverified user context. There is no supplied PySide6 runtime observation in this task.
