<!--
source: https://doc.qt.io/qtforpython-6/examples/example_widgets_itemviews_dirview.html
retrieved: 2026-10-31T21:18:44.532713+00:00
final_url: https://doc.qt.io/qtforpython-6/examples/example_widgets_itemviews_dirview.html
content_type: text/html
-->

# Dir View Example - Qt for Python

[Skip to content](https://doc.qt.io/qtforpython-6/examples/example_widgets_itemviews_dirview.html#furo-main-content)

[Qt for Python](https://doc.qt.io/qtforpython-6/index.html)

[Back to top](https://doc.qt.io/qtforpython-6/examples/example_widgets_itemviews_dirview.html)

# Dir View Example[¶](https://doc.qt.io/qtforpython-6/examples/example_widgets_itemviews_dirview.html#dir-view-example)

The Dir View example shows a tree view of the local file system. It uses the QFileSystemModel class to provide file and directory information.

``[Download this example](https://doc.qt.io/qtforpython-6/_downloads/26354bdba2d91f68f4f60a5ec29876e0/dirview.zip)

 dirview.py

```
from __future__ import annotations

import sys
from argparse import ArgumentParser, RawTextHelpFormatter

from PySide6.QtWidgets import (QApplication, QFileSystemModel,
                               QFileIconProvider, QScroller, QTreeView)
from PySide6.QtCore import QDir

"""PySide6 port of the widgets/itemviews/dirview example from Qt v6.x"""

if __name__ == "__main__":
    app = QApplication(sys.argv)

    name = "Dir View"
    argument_parser = ArgumentParser(description=name,
                                     formatter_class=RawTextHelpFormatter)
    argument_parser.add_argument("--no-custom", "-c", action="store_true",
                                 help="Set QFileSystemModel.DontUseCustomDirectoryIcons")
    argument_parser.add_argument("--no-watch", "-w", action="store_true",
                                 help="Set QFileSystemModel.DontWatch")
    argument_parser.add_argument("directory",
                                 help="The directory to start in.",
                                 nargs='?', type=str)
    options = argument_parser.parse_args()
    root_path = options.directory

    model = QFileSystemModel()
    icon_provider = QFileIconProvider()
    model.setIconProvider(icon_provider)
    model.setRootPath("")
    if options.no_custom:
        model.setOption(QFileSystemModel.DontUseCustomDirectoryIcons)
    if options.no_watch:
        model.setOption(QFileSystemModel.DontWatchForChanges)
    tree = QTreeView()
    tree.setModel(model)
    if root_path:
        root_index = model.index(QDir.cleanPath(root_path))
        if root_index.isValid():
            tree.setRootIndex(root_index)

    # Demonstrating look and feel features
    tree.setAnimated(False)
    tree.setIndentation(20)
    tree.setSortingEnabled(True)
    availableSize = tree.screen().availableGeometry().size()
    tree.resize(availableSize / 2)
    tree.setColumnWidth(0, tree.width() / 3)

    # Make it flickable on touchscreens
    QScroller.grabGesture(tree, QScroller.ScrollerGestureType.TouchGesture)

    tree.setWindowTitle(name)
    tree.show()

    sys.exit(app.exec())
```
