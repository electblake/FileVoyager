"""Viewport-driven thumbnail scheduling; native retrieval belongs to the service."""

from collections import OrderedDict, deque
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass

from PySide6.QtCore import QObject, QTimer, Signal
from PySide6.QtGui import QIcon, QPixmap

from filevoyager.models import MEDIA_EXTENSIONS


@dataclass(frozen=True)
class ThumbnailKey:
    path: str
    modified_ms: int
    file_size: int
    pixels: int
    device_ratio: float


class ThumbnailCache:
    """LRU bounded by the retained 32-bit pixel payload, not entry count."""

    def __init__(self, budget=64 * 1024 * 1024):
        self.budget = budget
        self.bytes_used = 0
        self.entries = OrderedDict()

    def get(self, key):
        if key not in self.entries:
            return None
        self.entries.move_to_end(key)
        return self.entries[key][0]

    def put(self, key, image):
        cost = image.sizeInBytes()
        if key in self.entries:
            self.bytes_used -= self.entries.pop(key)[1]
        if cost > self.budget:
            return
        while self.bytes_used + cost > self.budget:
            self.bytes_used -= self.entries.popitem(last=False)[1][1]
        pixmap = QPixmap.fromImage(image)
        pixmap.setDevicePixelRatio(key.device_ratio)
        self.entries[key] = (QIcon(pixmap), cost)
        self.bytes_used += cost


class ThumbnailController(QObject):
    updated = Signal()
    requestFinished = Signal(object)

    def __init__(self, grid, model, load_image, parent=None):
        super().__init__(parent)
        self.grid = grid
        self.model = model
        self.load_image = load_image
        self.executor = ThreadPoolExecutor(max_workers=2, thread_name_prefix="thumbnail")
        self.active = {}
        self.pending = deque()
        self.requested = set()
        self.generation = 0
        self.completed = 0
        self.stale_results = 0
        self.peak_active = 0
        self.peak_pending = 0
        self.enabled = False
        self.closed = False
        self.refresh_timer = QTimer(self)
        self.refresh_timer.setSingleShot(True)
        self.refresh_timer.setInterval(40)
        self.refresh_timer.timeout.connect(self.refresh)
        self.poll_timer = QTimer(self)
        self.poll_timer.setInterval(16)
        self.poll_timer.timeout.connect(self.poll)
        grid.viewportChanged.connect(self.schedule)
        source = model.sourceModel()
        source.rowsInserted.connect(self.schedule)
        source.rowsRemoved.connect(self.schedule)
        source.layoutChanged.connect(self.schedule)
        source.dataChanged.connect(self.schedule)
        source.directoryLoaded.connect(self.schedule)

    def schedule(self, *args):
        if self.enabled and not self.closed and not self.refresh_timer.isActive():
            self.refresh_timer.start()

    def invalidate(self):
        self.generation += 1
        self.pending.clear()
        self.requested.clear()
        self.model.keys.clear()
        self.schedule()

    def set_enabled(self, enabled):
        self.enabled = enabled
        self.generation += 1
        self.pending.clear()
        self.requested.clear()
        if enabled:
            self.schedule()
        else:
            self.refresh_timer.stop()

    def refresh(self):
        if not self.enabled or self.closed:
            return
        source = self.model.sourceModel()
        ratio = self.grid.devicePixelRatioF()
        pixels = round(self.grid.iconSize().width() * ratio)
        root = self.grid.rootIndex()
        active_keys = {key for generation, key in self.active.values()
                       if generation == self.generation}
        requests = []
        for row in self.grid.candidate_rows():
            index = self.model.index(row, 0, root)
            source_index = self.model.mapToSource(index)
            path = source.filePath(source_index)
            if path.rpartition(".")[2].lower() not in MEDIA_EXTENSIONS or source.isDir(source_index):
                continue
            info = source.fileInfo(source_index)
            key = ThumbnailKey(path, info.lastModified().toMSecsSinceEpoch(),
                               info.size(), pixels, ratio)
            self.model.keys[path] = key
            if (self.model.cache.get(key) is None and key not in active_keys
                    and key not in self.requested):
                requests.append(key)
        # Replace stale viewport work; the executor itself never has a backlog.
        self.pending = deque(requests)
        self.peak_pending = max(self.peak_pending, len(self.pending))
        self.dispatch()
        self.grid.viewport().update()

    def dispatch(self):
        while self.pending and len(self.active) < 2:
            key = self.pending.popleft()
            self.requested.add(key)
            future = self.executor.submit(self.load_image, key.path, key.pixels, key.pixels)
            self.active[future] = (self.generation, key)
        self.peak_active = max(self.peak_active, len(self.active))
        if self.active:
            self.poll_timer.start()

    def poll(self):
        changed = []
        source = self.model.sourceModel()
        for future in list(self.active):
            if not future.done():
                continue
            generation, key = self.active.pop(future)
            self.requestFinished.emit(future)
            # Service exceptions surface unchanged. No catches, retries or substitution.
            image = future.result()
            if generation != self.generation:
                self.stale_results += 1
                continue
            self.requested.discard(key)
            self.model.cache.put(key, image)
            self.completed += 1
            index = self.model.mapFromSource(source.index(key.path))
            if index.isValid() and self.model.keys.get(key.path) == key:
                changed.append(index)
        # Thumbnail geometry never changes. Repaint cells without model notifications,
        # which can cause QListView to schedule another layout of the whole directory.
        for index in changed:
            rect = self.grid.visualRect(index)
            if rect.intersects(self.grid.viewport().rect()):
                self.grid.viewport().update(rect)
        if changed:
            self.updated.emit()
        if self.enabled:
            self.dispatch()
        if not self.active:
            self.poll_timer.stop()

    def close(self):
        self.closed = True
        self.enabled = False
        self.refresh_timer.stop()
        self.poll_timer.stop()
        self.pending.clear()
        self.executor.shutdown(wait=True, cancel_futures=True)
        for future in self.active:
            future.result()
        self.active.clear()
