"""Convert owned Shell pixels on the thumbnail worker; create no GUI objects."""

import os

from PySide6.QtGui import QImage

# Import during startup, before dispatching workers (comtypes initializes this thread).
from filevoyager.shell_thumbnails import load_cached_thumbnail


def load_thumbnail_image(path: str, width: int, height: int) -> QImage:
    result = load_cached_thumbnail(os.path.normpath(path), width, height)
    view = QImage(result.pixels, result.width, result.height, result.stride,
                  QImage.Format.Format_BGR888)
    # Conversion produces owned, detached 32-bit storage. It also makes the cache's
    # byte accounting match the displayed QPixmap's 32-bit pixel payload.
    return view.convertToFormat(QImage.Format.Format_RGB32)
