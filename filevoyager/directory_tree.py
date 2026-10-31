"""Lazy folder-only tree: scan/sort on a worker, insert bounded GUI batches."""

from bisect import bisect_left
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
import os

from PySide6.QtCore import QFileSystemWatcher, QModelIndex, QTimer, Qt, Signal
from PySide6.QtGui import QStandardItem, QStandardItemModel


def path_key(path):
    return os.path.normcase(os.path.normpath(path)) if path else ""


def scan_directories(path):
    if not path:
        return [(drive, drive) for drive in os.listdrives()]
    with os.scandir(path) as entries:
        directories = [(entry.name, entry.path) for entry in entries if entry.is_dir()]
    directories.sort(key=lambda entry: entry[0].casefold())
    return directories


@dataclass
class DirectoryNode:
    path: str
    item: QStandardItem
    children: list[str] = field(default_factory=list)
    loaded: bool = False
    placeholder: bool = True


class DirectoryTreeModel(QStandardItemModel):
    pathReady = Signal(QModelIndex)
    directoryLoaded = Signal(str)

    def __init__(self, folder_icon, parent=None):
        super().__init__(parent)
        self.setColumnCount(1)
        self.folder_icon = folder_icon
        self.nodes = {"": DirectoryNode("", self.invisibleRootItem())}
        self.executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="folder-tree")
        self.queue = deque()
        self.queued = set()
        self.dirty = set()
        self.future = None
        self.active_key = None
        self.applying = False
        self.closed = False
        self.target_chain = []
        self.batch_size = 128
        self.peak_batch = 0
        self.poll_timer = QTimer(self)
        self.poll_timer.setInterval(16)
        self.poll_timer.timeout.connect(self.poll)
        self.batch_timer = QTimer(self)
        self.batch_timer.setSingleShot(True)
        self.batch_timer.timeout.connect(self.apply_batch)
        self.watcher = QFileSystemWatcher(self)
        self.watcher.directoryChanged.connect(self.directory_changed)
        self.request_scan("")

    def file_path(self, index):
        return index.data(Qt.ItemDataRole.UserRole)

    def index_for_path(self, path):
        return self.nodes[path_key(path)].item.index()

    def make_node(self, name, path):
        item = QStandardItem(self.folder_icon, name)
        item.setEditable(False)
        item.setData(path, Qt.ItemDataRole.UserRole)
        placeholder = QStandardItem("Loading…")
        placeholder.setEnabled(False)
        item.appendRow(placeholder)
        node = DirectoryNode(path, item)
        self.nodes[path_key(path)] = node
        return node

    def expanded(self, index):
        node = self.nodes[path_key(self.file_path(index))]
        if not node.loaded:
            self.request_scan(node.path)

    def directory_changed(self, path):
        key = path_key(path)
        if key not in self.nodes:
            return  # A queued notification for an already removed tree node.
        watched = set(self.watcher.directories())
        if path in watched:
            self.request_scan(path)
            return
        # Qt removes a deleted directory from its watch list before notifying us.
        # Refresh its surviving watched ancestor to remove the row, not the deleted
        # directory itself. No failed scan is caught or retried.
        item = self.nodes[key].item.parent()
        while item is not None and item.data(Qt.ItemDataRole.UserRole) not in watched:
            item = item.parent()
        ancestor = item.data(Qt.ItemDataRole.UserRole) if item is not None else ""
        self.request_scan(ancestor, priority=True)

    def request_scan(self, path, priority=False):
        key = path_key(path)
        if self.closed:
            return
        if key == self.active_key:
            self.dirty.add(key)
            return
        if key not in self.queued:
            if priority:
                self.queue.appendleft(key)
            else:
                self.queue.append(key)
            self.queued.add(key)
        elif priority:
            self.queue.remove(key)
            self.queue.appendleft(key)
        self.dispatch()

    def dispatch(self):
        if self.active_key is None and self.queue:
            self.active_key = self.queue.popleft()
            self.queued.remove(self.active_key)
            path = self.nodes[self.active_key].path
            if path and path not in self.watcher.directories():
                self.watcher.addPath(path)
            self.future = self.executor.submit(scan_directories, path)
            self.poll_timer.start()

    def poll(self):
        if not self.future.done():
            return
        future = self.future
        self.future = None
        self.poll_timer.stop()
        entries = future.result()
        node = self.nodes[self.active_key]
        desired = {path_key(path) for _, path in entries}
        existing = set(node.children)
        self.removals = deque(row for row in reversed(range(len(node.children)))
                              if node.children[row] not in desired)
        self.additions = deque((name, path) for name, path in entries
                               if path_key(path) not in existing)
        self.applying = True
        self.batch_timer.start(0)

    def apply_batch(self):
        node = self.nodes[self.active_key]
        if node.placeholder and node.path:
            node.item.removeRow(0)  # Remove the expansion placeholder once.
            node.placeholder = False
        work = 0
        while self.removals and work < self.batch_size:
            row = self.removals.popleft()
            key = node.children.pop(row)
            self.remove_node_records(key)
            node.item.removeRow(row)
            work += 1
        additions = []
        while self.additions and work < self.batch_size:
            name, path = self.additions.popleft()
            child = self.make_node(name, path)
            key = path_key(path)
            position = bisect_left(node.children, key)
            node.children.insert(position, key)
            additions.append((position, child.item))
            work += 1
        # Initial sorted results form one contiguous append per batch. Incremental
        # insertions preserve persistent indexes/expanded children already in the tree.
        if additions and all(position == node.item.rowCount() + offset
                             for offset, (position, _) in enumerate(additions)):
            node.item.appendRows([item for _, item in additions])
        else:
            for position, item in additions:
                node.item.insertRow(position, item)
        self.peak_batch = max(self.peak_batch, work)
        if self.removals or self.additions:
            self.batch_timer.start(0)
            return
        node.loaded = True
        self.applying = False
        completed_key = self.active_key
        self.active_key = None
        self.directoryLoaded.emit(node.path)
        if completed_key in self.dirty:
            self.dirty.remove(completed_key)
            self.request_scan(node.path)
        self.continue_reveal()
        self.dispatch()

    def remove_node_records(self, key):
        node = self.nodes.pop(key)
        if key in self.queued:
            self.queue.remove(key)
            self.queued.remove(key)
        self.dirty.discard(key)
        for child in node.children:
            self.remove_node_records(child)
        if node.path in self.watcher.directories():
            self.watcher.removePath(node.path)

    def reveal_path(self, path):
        path = os.path.normpath(path)
        drive, tail = os.path.splitdrive(path)
        anchor = drive + os.sep
        root_key = path_key(anchor)
        if root_key not in self.nodes:
            node = self.make_node(anchor, anchor)
            roots = self.nodes[""].children
            position = bisect_left(roots, root_key)
            roots.insert(position, root_key)
            self.invisibleRootItem().insertRow(position, node.item)
        self.target_chain = [root_key]
        current = anchor
        for component in tail.strip(os.sep).split(os.sep):
            if component:
                current = os.path.join(current, component)
                self.target_chain.append(path_key(current))
        self.continue_reveal()

    def continue_reveal(self):
        for key in self.target_chain[:-1]:
            node = self.nodes[key]
            if not node.loaded or key == self.active_key:
                if key != self.active_key:
                    self.request_scan(node.path)
                return
        if self.target_chain:
            self.pathReady.emit(self.nodes[self.target_chain[-1]].item.index())

    def close(self):
        self.closed = True
        self.poll_timer.stop()
        self.batch_timer.stop()
        self.queue.clear()
        self.executor.shutdown(wait=True, cancel_futures=True)
        if self.future is not None:
            self.future.result()
