from PySide6.QtCore import QSortFilterProxyModel, Qt
from PySide6.QtGui import QIcon

from filevoyager.file_model import FileModel


MEDIA_SUFFIXES = frozenset({
    ".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff",
    ".gif", ".avif", ".heic", ".heif", ".jxl",
    ".mp4", ".m4v", ".mkv", ".webm", ".mov", ".avi", ".wmv",
    ".mpg", ".mpeg", ".ts", ".mts", ".m2ts",
})


class ThumbnailModel(QSortFilterProxyModel):
    """Paint only from memory. Thumbnail requests happen in the controller."""

    def __init__(self, source, cache, parent=None):
        super().__init__(parent)
        self.cache = cache
        self.keys = {}
        self.ranks = None
        self.order_keys = {}
        source.rowsAboutToBeRemoved.connect(self.clear_order_keys)
        source.modelAboutToBeReset.connect(self.clear_order_keys)
        source.dataChanged.connect(self.clear_order_keys)
        self.setSourceModel(source)

    def clear_order_keys(self, *args):
        self.order_keys.clear()

    def sort(self, column, order=Qt.SortOrder.AscendingOrder):
        self.ranks = None
        self.order_keys.clear()
        super().sort(-1)
        self.sourceModel().sort(column, order)

    def set_image_order(self, paths):
        self.ranks = {path: rank for rank, path in enumerate(paths)}
        self.order_keys.clear()
        self.invalidate()
        super().sort(0, Qt.SortOrder.AscendingOrder)

    def lessThan(self, left, right):
        return self.order_key(left) < self.order_key(right)

    def order_key(self, index):
        # Source indexes identify stable nodes across layout changes.
        # Clear before removal/reset and on metadata changes to avoid stale keys.
        identity = index.internalId()
        if identity not in self.order_keys:
            source = self.sourceModel()
            path = source.filePath(index)
            if source.navigation_path(index):
                key = (0, 0, path.casefold(), path)
            elif path in self.ranks:
                key = (1, self.ranks[path], "", "")
            else:
                key = (2, 0, path.casefold(), path)
            self.order_keys[identity] = key
        return self.order_keys[identity]

    def thumbnail_decoration(self, index):
        source_index = self.mapToSource(index)
        path = self.sourceModel().filePath(source_index)
        if (path.rpartition(".")[2].lower() in MEDIA_EXTENSIONS
                and not self.sourceModel().isDir(source_index)):
            icon = self.cache.get(self.keys.get(path))
            # Pending media stay undecorated; failures propagate from the service.
            return icon if icon is not None else QIcon()
        return self.data(index, Qt.ItemDataRole.DecorationRole)


MEDIA_EXTENSIONS = frozenset(suffix[1:] for suffix in MEDIA_SUFFIXES)
