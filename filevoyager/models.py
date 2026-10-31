from PySide6.QtCore import QIdentityProxyModel, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFileIconProvider, QFileSystemModel


class SimpleIconProvider(QFileIconProvider):
    """Avoid native per-file Shell icon lookups during enumeration."""

    def __init__(self, folder_icon, file_icon):
        super().__init__()
        self.folder_icon = folder_icon
        self.file_icon = file_icon

    def icon(self, info):
        if isinstance(info, QFileIconProvider.IconType):
            return self.folder_icon if info == self.IconType.Folder else self.file_icon
        return self.folder_icon if info.isDir() else self.file_icon

    def type(self, info):
        if info.isDir():
            return "Folder"
        suffix = info.suffix().upper()
        return f"{suffix} file" if suffix else "File"


class FileModel(QFileSystemModel):
    def __init__(self, folder_icon, file_icon, parent=None):
        super().__init__(parent)
        self.provider = SimpleIconProvider(folder_icon, file_icon)
        self.setIconProvider(self.provider)
        self.setOption(self.Option.DontUseCustomDirectoryIcons, True)


MEDIA_SUFFIXES = frozenset({
    ".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff",
    ".gif", ".avif", ".heic", ".heif", ".jxl",
    ".mp4", ".m4v", ".mkv", ".webm", ".mov", ".avi", ".wmv",
    ".mpg", ".mpeg", ".ts", ".mts", ".m2ts",
})


class ThumbnailModel(QIdentityProxyModel):
    """Paint only from memory. Thumbnail requests happen in the controller."""

    def __init__(self, source, cache, parent=None):
        super().__init__(parent)
        self.cache = cache
        self.keys = {}
        self.setSourceModel(source)

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
