"""Lazy folder-only tree: scan/sort on a worker, insert bounded GUI batches."""

from bisect import bisect_left
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
import os

from PySide6.QtCore import QFileSystemWatcher, QModelIndex, QTimer, Qt, Signal
from PySide6.QtGui import QStandardItem, QStandardItemModel
from filevoyager.windows_shortcuts import folder_shortcut_targets


def path_key(path):
    return os.path.normcase(os.path.normpath(path)) if path else ""


def scan_directories(path):
    if not path:
        return [(drive, drive, "") for drive in os.listdrives()]
    with os.scandir(path) as entries:
        directories = []
        shortcuts = []
        for entry in entries:
            if entry.is_dir():
                directories.append((entry.name, entry.path, ""))
            elif entry.name.lower().endswith(".lnk"):
                shortcuts.append((entry.name, entry.path))
    targets = folder_shortcut_targets(source for _, source in shortcuts)
    directories.extend((name, source, targets[source]) for name, source in shortcuts if targets[source])
    directories.sort(key=lambda entry: entry[0].casefold())
    return directories


def directory_changes(path, children, branch_path, targets):
    entries = [(name, os.path.join(branch_path, name) if branch_path else source, target, source)
               for name, source, target in scan_directories(path)]
    desired = {path_key(branch): target for _, branch, target, _ in entries}
    existing = set(children)
    replaced = {key for key in existing & desired.keys() if targets[key] != desired[key]}
    removals = deque(row for row in reversed(range(len(children)))
                     if children[row] not in desired or children[row] in replaced)
    additions = deque(entry for entry in entries
                      if path_key(entry[1]) not in existing or path_key(entry[1]) in replaced)
    return removals, additions


@dataclass
class DirectoryNode:
    path: str
    item: QStandardItem
    children: list[str] = field(default_factory=list)
    targets: dict[str, str] = field(default_factory=dict)
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
        self.watched_nodes = {}
        self.watcher.directoryChanged.connect(self.directory_changed)
        self.request_scan("")

    def file_path(self, index):
        return index.data(Qt.ItemDataRole.UserRole)

    def index_for_path(self, path):
        return self.nodes[path_key(path)].item.index()

    def navigation_path(self, index):
        return index.data(Qt.ItemDataRole.UserRole + 1) or self.file_path(index)

    def make_node(self, name, path, target="", source_path=None):
        item = QStandardItem(self.folder_icon, name)
        item.setEditable(False)
        item.setData(path if source_path is None else source_path, Qt.ItemDataRole.UserRole)
        item.setData(target, Qt.ItemDataRole.UserRole + 1)
        item.setData(path, Qt.ItemDataRole.UserRole + 2)
        if target:
            item.setToolTip(target)
        placeholder = QStandardItem("Loading…")
        placeholder.setEnabled(False)
        item.appendRow(placeholder)
        node = DirectoryNode(path, item)
        self.nodes[path_key(path)] = node
        return node

    def expanded(self, index):
        node = self.nodes[path_key(index.data(Qt.ItemDataRole.UserRole + 2))]
        if not node.loaded:
            self.request_scan(node.path)

    def directory_changed(self, path):
        watched = set(self.watcher.directories())
        for key in tuple(self.watched_nodes.get(path_key(path), ())):
            node = self.nodes[key]
            if path in watched:
                self.request_scan(node.path)
                continue
            # Refresh the surviving ancestor after Qt removes a deleted watch.
            item = node.item.parent()
            while item is not None and self.navigation_path(item.index()) not in watched:
                item = item.parent()
            ancestor = item.data(Qt.ItemDataRole.UserRole + 2) if item is not None else ""
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
            node = self.nodes[self.active_key]
            path = self.navigation_path(node.item.index()) if node.path else ""
            if path and path not in self.watcher.directories():
                self.watcher.addPath(path)
            if path:
                self.watched_nodes.setdefault(path_key(path), set()).add(self.active_key)
            self.future = self.executor.submit(directory_changes, path,
                                               tuple(node.children), node.path, node.targets.copy())
            self.poll_timer.start()

    def poll(self):
        if not self.future.done():
            return
        future = self.future
        self.future = None
        self.poll_timer.stop()
        self.removals, self.additions = future.result()
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
            del node.targets[key]
            self.remove_node_records(key)
            node.item.removeRow(row)
            work += 1
        additions = []
        while self.additions and work < self.batch_size:
            name, path, target, source_path = self.additions.popleft()
            key = path_key(path)
            # reveal_path can insert a drive while the drive scan is in flight.
            if key in self.nodes:
                continue
            child = self.make_node(name, path, target, source_path)
            node.targets[key] = target
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
        watched_path = self.navigation_path(node.item.index())
        watched_key = path_key(watched_path)
        if watched_key in self.watched_nodes:
            self.watched_nodes[watched_key].discard(key)
            if not self.watched_nodes[watched_key]:
                del self.watched_nodes[watched_key]
                if watched_path in self.watcher.directories():
                    self.watcher.removePath(watched_path)

    def reveal_path(self, path, preferred=QModelIndex()):
        path = os.path.normpath(path)
        candidate = preferred
        while candidate.isValid():
            target = self.navigation_path(candidate)
            key = path_key(target)
            if path_key(path) == key:
                self.target_chain = []
                self.pathReady.emit(candidate)
                return
            if path_key(path).startswith(key.rstrip(os.sep) + os.sep):
                chain = []
                ancestor = candidate
                while ancestor.isValid():
                    chain.append(path_key(ancestor.data(Qt.ItemDataRole.UserRole + 2)))
                    ancestor = ancestor.parent()
                self.target_chain = list(reversed(chain))
                current = candidate.data(Qt.ItemDataRole.UserRole + 2)
                for component in os.path.relpath(path, target).split(os.sep):
                    current = os.path.join(current, component)
                    self.target_chain.append(path_key(current))
                self.continue_reveal()
                return
            candidate = candidate.parent()
        drive, tail = os.path.splitdrive(path)
        anchor = drive + os.sep
        root_key = path_key(anchor)
        if root_key not in self.nodes:
            node = self.make_node(anchor, anchor)
            roots = self.nodes[""].children
            position = bisect_left(roots, root_key)
            roots.insert(position, root_key)
            self.nodes[""].targets[root_key] = ""
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
            index = self.nodes[self.target_chain[-1]].item.index()
            self.target_chain = []
            self.pathReady.emit(index)

    def close(self):
        self.closed = True
        self.poll_timer.stop()
        self.batch_timer.stop()
        self.queue.clear()
        self.executor.shutdown(wait=True, cancel_futures=True)
        if self.future is not None:
            self.future.result()
