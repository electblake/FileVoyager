"""Worker-sorted directory snapshots with bounded GUI-thread row publication."""

from collections import OrderedDict, deque
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field, replace
import os
import stat
from pathlib import Path

from PySide6.QtCore import (
    QAbstractItemModel, QCollator, QDateTime, QFileSystemWatcher, QModelIndex, QTimer, Qt, Signal,
)
from filevoyager.windows_shortcuts import folder_shortcut_targets


def path_key(path):
    return os.path.normcase(os.path.normpath(path))


@dataclass(frozen=True, slots=True)
class FileRecord:
    path: str
    name: str
    directory: bool
    size: int
    modified: int
    kind: str
    modified_text: str
    folder_target: str = ""


def directory_snapshot(path, previous, column, descending, scan):
    records = []
    if scan:
        shortcuts = []
        with os.scandir(path) as entries:
            for entry in entries:
                metadata = entry.stat()
                if metadata.st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN:
                    continue
                directory = entry.is_dir()
                suffix = os.path.splitext(entry.name)[1][1:].upper()
                if not directory and suffix == "LNK":
                    shortcuts.append(len(records))
                modified = metadata.st_mtime_ns // 1_000_000
                records.append(FileRecord(entry.path, entry.name, directory, metadata.st_size,
                                          modified,
                                          "Folder" if directory else f"{suffix} file" if suffix else "File",
                                          QDateTime.fromMSecsSinceEpoch(modified).toString("yyyy-MM-dd HH:mm")))
        targets = folder_shortcut_targets(records[row].path for row in shortcuts)
        for row in shortcuts:
            record = records[row]
            target = targets[record.path]
            records[row] = replace(record, folder_target=target,
                                   kind="Folder shortcut" if target else "Shortcut")
    else:
        records = list(previous)
    collator = QCollator()
    collator.setNumericMode(True)
    collator.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)

    def key(record):
        name = collator.sortKey(record.name)
        if column == 0:
            return (not (record.directory or record.folder_target), name)
        if column == 1:
            return (not (record.directory or record.folder_target), record.size, name)
        if column == 2:
            return (collator.sortKey(record.kind), name)
        return (record.modified, name)

    records.sort(key=key, reverse=descending)
    old = {record.path: record for record in previous}
    new = {record.path: record for record in records}
    removed = [row for row in reversed(range(len(previous))) if previous[row].path not in new]
    added = [record for record in records if record.path not in old]
    changed = [record for record in records if record.path in old and record != old[record.path]]
    retained = [record.path for record in previous if record.path in new]
    reordered = retained + [record.path for record in added] != [record.path for record in records]
    return tuple(records), deque(removed), deque(added), deque(changed), reordered


@dataclass(eq=False, slots=True)
class FileNode:
    path: str
    row: int
    parent: object = None
    record: FileRecord | None = None
    children: list = field(default_factory=list)
    lookup: dict = field(default_factory=dict)
    records: tuple = ()
    loaded: bool = False
    revision: int = 0


class FileModel(QAbstractItemModel):
    directoryLoaded = Signal(str)
    fileRenamed = Signal(str, str, str)
    folderMergeRequested = Signal(str, str)

    def __init__(self, folder_icon, file_icon, parent=None):
        super().__init__(parent)
        self.folder_icon, self.file_icon = folder_icon, file_icon
        self.roots = []
        self.by_path = {}
        self.recent = OrderedDict()
        self.current = None
        self.read_only = False
        self.item_flags = Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable
        self.editable_flags = self.item_flags | Qt.ItemFlag.ItemIsEditable
        self.column, self.order = 0, Qt.SortOrder.AscendingOrder
        self.executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="file-list")
        self.pending = OrderedDict()
        self.future = None
        self.applying = None
        self.closed = False
        self.peak_batch = 0
        self.timer = QTimer(self)
        self.timer.setInterval(5)
        self.timer.timeout.connect(self.poll)
        self.batch_timer = QTimer(self)
        self.batch_timer.setSingleShot(True)
        self.batch_timer.timeout.connect(self.apply_batch)
        self.watcher = QFileSystemWatcher(self)
        self.watcher.directoryChanged.connect(self.directory_changed)

    def root_index(self, node):
        return self.createIndex(node.row, 0, node)

    def index(self, row, column=0, parent=QModelIndex()):
        if isinstance(row, str):
            key = path_key(row)
            for root in reversed(self.recent.values()):
                if key in root.lookup:
                    node = root.lookup[key]
                    return self.createIndex(node.row, column, node)
            return self.root_index(self.by_path[key]) if key in self.by_path else QModelIndex()
        # Avoid hasIndex's C++ -> Python rowCount/columnCount round trips for
        # every cell visited by QListView's batched layout.
        if row < 0 or column < 0 or column >= 4 or parent.column() > 0:
            return QModelIndex()
        children = parent.internalPointer().children if parent.isValid() else self.roots
        if row >= len(children):
            return QModelIndex()
        return self.createIndex(row, column, children[row])

    def parent(self, index):
        if not index.isValid() or index.internalPointer().parent is None:
            return QModelIndex()
        return self.root_index(index.internalPointer().parent)

    def rowCount(self, parent=QModelIndex()):
        if not parent.isValid():
            return len(self.roots)
        return len(parent.internalPointer().children) if parent.column() == 0 else 0

    def columnCount(self, parent=QModelIndex()):
        return 4

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        node = index.internalPointer()
        record = node.record
        if role in (Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole):
            if record is None:
                return Path(node.path).name if index.column() == 0 else ""
            if index.column() == 0:
                return record.name
            if index.column() == 1:
                return "" if record.directory else f"{record.size:,} bytes"
            if index.column() == 2:
                return record.kind
            return record.modified_text
        if role == Qt.ItemDataRole.DecorationRole and index.column() == 0:
            return self.folder_icon if self.isDir(index) or record.folder_target else self.file_icon
        if role == Qt.ItemDataRole.ToolTipRole and record is not None and record.folder_target:
            return record.folder_target

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return ("Name", "Size", "Type", "Date Modified")[section]

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags
        if index.column() == 0 and not self.read_only:
            return self.editable_flags
        return self.item_flags

    def filePath(self, index):
        return index.internalPointer().path.replace("\\", "/") if index.isValid() else ""

    def isDir(self, index):
        node = index.internalPointer()
        return node.record is None or node.record.directory

    def navigation_path(self, index):
        record = index.internalPointer().record
        if self.isDir(index):
            return self.filePath(index)
        return record.folder_target

    def file_metadata(self, index):
        record = index.internalPointer().record
        return record.modified, record.size

    def is_loaded(self, path):
        return self.by_path[path_key(path)].loaded

    def setReadOnly(self, value):
        self.read_only = value

    def setRootPath(self, path):
        path = os.path.normpath(path)
        key = path_key(path)
        if key not in self.by_path:
            row = len(self.roots)
            self.beginInsertRows(QModelIndex(), row, row)
            self.by_path[key] = FileNode(path, row)
            self.roots.append(self.by_path[key])
            self.endInsertRows()
        root = self.by_path[key]
        self.current = root
        self.recent[key] = root
        self.recent.move_to_end(key)
        if not root.loaded:
            if root.path not in self.watcher.directories():
                self.watcher.addPath(root.path)
            self.request(root, True)
        else:
            QTimer.singleShot(0, lambda: self.directoryLoaded.emit(path))
        # Keep at most four directory snapshots; root indexes remain stable.
        if len(self.recent) > 4:
            _, expired = self.recent.popitem(last=False)
            if expired.children:
                self.beginRemoveRows(self.root_index(expired), 0, len(expired.children) - 1)
                expired.children.clear()
                expired.lookup.clear()
                self.endRemoveRows()
            expired.records = ()
            expired.loaded = False
            expired.revision += 1
            self.pending.pop(expired, None)
            self.watcher.removePath(expired.path)
        return self.root_index(root)

    def request(self, root, scan):
        root.revision += 1
        self.pending[root] = scan or self.pending.get(root, False)
        self.dispatch()

    def dispatch(self):
        if self.future is not None or self.applying is not None or not self.pending or self.closed:
            return
        root = self.current if self.current in self.pending else next(iter(self.pending))
        scan = self.pending.pop(root)
        self.active = root, root.revision
        self.future = self.executor.submit(directory_snapshot, root.path, root.records,
                                           self.column, self.order == Qt.SortOrder.DescendingOrder, scan)
        self.timer.start()

    def poll(self):
        if not self.future.done():
            return
        result = self.future.result()
        self.future = None
        self.timer.stop()
        root, revision = self.active
        if revision != root.revision:
            self.dispatch()
            return
        self.applying = root, result
        self.batch_timer.start(0)

    def apply_batch(self):
        root, (records, removed, added, changed, reordered) = self.applying
        if path_key(root.path) not in self.recent:
            self.applying = None
            self.dispatch()
            return
        parent = self.root_index(root)
        work = 0
        while removed and work < 512:
            last = first = removed.popleft()
            while removed and removed[0] == first - 1 and work + last - first + 1 < 512:
                first = removed.popleft()
            self.beginRemoveRows(parent, first, last)
            for node in root.children[first:last + 1]:
                del root.lookup[path_key(node.path)]
            del root.children[first:last + 1]
            for position in range(first, len(root.children)):
                root.children[position].row = position
            self.endRemoveRows()
            work += last - first + 1
        if added and work < 512:
            batch = [added.popleft() for _ in range(min(512 - work, len(added)))]
            first = len(root.children)
            self.beginInsertRows(parent, first, first + len(batch) - 1)
            for record in batch:
                node = FileNode(record.path, len(root.children), root, record)
                root.children.append(node)
                root.lookup[path_key(node.path)] = node
            self.endInsertRows()
            work += len(batch)
        while changed and work < 512:
            record = changed.popleft()
            node = root.lookup[path_key(record.path)]
            node.record = record
            self.dataChanged.emit(self.createIndex(node.row, 0, node), self.createIndex(node.row, 3, node))
            work += 1
        self.peak_batch = max(self.peak_batch, work)
        if removed or added or changed:
            self.batch_timer.start(0)
            return
        if reordered:
            self.layoutAboutToBeChanged.emit()
            old = self.persistentIndexList()
            root.children = [root.lookup[path_key(record.path)] for record in records]
            for row, node in enumerate(root.children):
                node.row = row
            self.changePersistentIndexList(old, [self.createIndex(index.internalPointer().row, index.column(),
                                                                  index.internalPointer()) for index in old])
            self.layoutChanged.emit()
        root.records = records
        root.loaded = True
        self.applying = None
        if root.path not in self.watcher.directories():
            self.watcher.addPath(root.path)
        self.directoryLoaded.emit(root.path)
        self.dispatch()

    def sort(self, column, order=Qt.SortOrder.AscendingOrder):
        if (column, order) == (self.column, self.order):
            return
        self.column, self.order = column, order
        for root in self.recent.values():
            self.request(root, not root.loaded)

    def directory_changed(self, path):
        root = self.by_path[path_key(path)]
        if path not in self.watcher.directories():
            root.revision += 1
            self.pending.pop(root, None)
            if self.applying is not None and self.applying[0] is root:
                self.batch_timer.stop()
                self.applying = None
            if root.children:
                self.beginRemoveRows(self.root_index(root), 0, len(root.children) - 1)
                root.children.clear()
                root.lookup.clear()
                self.endRemoveRows()
            root.records = ()
            root.loaded = False
            self.dispatch()
            return
        self.request(root, True)

    def rename_path(self, path, name):
        source = Path(path)
        destination = source.with_name(name)
        if path_key(source) == path_key(destination) and source.name == name:
            return True
        if source.is_dir() and path_key(source) != path_key(destination) and destination.is_dir():
            self.folderMergeRequested.emit(str(source), str(destination))
            return False
        index = self.index(str(source))
        source.rename(destination)
        if index.isValid() and index.internalPointer().record is not None:
            node = index.internalPointer()
            root = node.parent
            if self.applying is not None and self.applying[0] is root:
                self.batch_timer.stop()
                self.applying = None
            del root.lookup[path_key(node.path)]
            node.path = str(destination)
            node.record = replace(node.record, path=str(destination), name=name)
            root.lookup[path_key(destination)] = node
            root.records = tuple(child.record for child in root.children)
            self.dataChanged.emit(index, index.siblingAtColumn(3))
            self.request(root, True)
        self.fileRenamed.emit(str(source.parent), source.name, name)
        return True

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.EditRole and index.column() == 0 and not self.read_only:
            return self.rename_path(self.filePath(index), value)
        return False

    def close(self):
        self.closed = True
        self.timer.stop()
        self.batch_timer.stop()
        self.executor.shutdown(wait=True, cancel_futures=True)
        if self.future is not None:
            self.future.result()
