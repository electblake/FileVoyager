from PySide6.QtCore import QPoint, QSize, Qt, Signal
from PySide6.QtWidgets import QListView, QStyle, QStyledItemDelegate, QStyleOptionViewItem


class GridDelegate(QStyledItemDelegate):
    def sizeHint(self, option, index):
        return self.parent().gridSize()

    def paint(self, painter, option, index):
        styled = QStyleOptionViewItem(option)
        self.initStyleOption(styled, index)
        styled.icon = index.model().thumbnail_decoration(index)
        self.parent().style().drawControl(QStyle.ControlElement.CE_ItemViewItem,
                                         styled, painter, self.parent())


class ThumbnailGrid(QListView):
    viewportChanged = Signal()
    layoutReady = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout_complete = False
        self.setViewMode(self.ViewMode.IconMode)
        self.setFlow(self.Flow.LeftToRight)
        self.setWrapping(True)
        self.setMovement(self.Movement.Static)
        self.setResizeMode(self.ResizeMode.Adjust)
        self.setLayoutMode(self.LayoutMode.Batched)
        self.setBatchSize(512)
        self.setUniformItemSizes(True)
        self.setWordWrap(False)
        self.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.setSpacing(0)
        self.setVerticalScrollMode(self.ScrollMode.ScrollPerPixel)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setSelectionMode(self.SelectionMode.ExtendedSelection)
        self.setSelectionBehavior(self.SelectionBehavior.SelectRows)
        self.setEditTriggers(self.EditTrigger.NoEditTriggers)
        self.setItemDelegate(GridDelegate(self))
        self.set_thumbnail_size(128)

    def set_thumbnail_size(self, size):
        if self.iconSize() == QSize(size, size):
            return
        self.layout_complete = False
        self.setIconSize(QSize(size, size))
        self.setGridSize(QSize(size + 32, size + 48))
        self.viewportChanged.emit()

    def resizeEvent(self, event):
        self.layout_complete = False
        super().resizeEvent(event)
        self.viewportChanged.emit()

    def setRootIndex(self, index):
        if index == self.rootIndex():
            return
        self.layout_complete = False
        super().setRootIndex(index)

    def rowsInserted(self, parent, start, end):
        if parent == self.rootIndex():
            self.layout_complete = False
        super().rowsInserted(parent, start, end)

    def doItemsLayout(self):
        self.layout_complete = False
        super().doItemsLayout()
        self.check_layout_complete()

    def timerEvent(self, event):
        super().timerEvent(event)
        self.check_layout_complete()

    def check_layout_complete(self):
        if self.layout_complete or self.model() is None:
            return
        count = self.model().rowCount(self.rootIndex())
        if count:
            last = self.visualRect(self.model().index(count - 1, 0, self.rootIndex()))
            if not last.isValid():
                return
        self.updateGeometries()
        # A reused proxy root can have valid item rectangles before the batched
        # scrollbar extent catches up. Restore only after both describe the end.
        if count:
            last = self.visualRect(self.model().index(count - 1, 0, self.rootIndex()))
            if (last.bottom() + 1 + self.verticalScrollBar().value()
                    > self.verticalScrollBar().maximum() + self.viewport().height()):
                return
        self.layout_complete = True
        self.layoutReady.emit()

    def showEvent(self, event):
        super().showEvent(event)
        self.viewportChanged.emit()

    def scrollContentsBy(self, dx, dy):
        super().scrollContentsBy(dx, dy)
        self.viewportChanged.emit()

    def candidate_rows(self, limit=128):
        """Sample viewport geometry, not every row in a large directory."""
        rect = self.viewport().rect()
        cell = self.gridSize()
        visible = set()
        for y in range(0, rect.height(), max(1, cell.height() // 3)):
            for x in range(0, rect.width(), max(1, cell.width() // 3)):
                index = self.indexAt(QPoint(x, y))
                if index.isValid():
                    visible.add(index.row())
        if not visible:
            return []
        rows = sorted(visible)
        columns = max(1, rect.width() // cell.width())
        count = self.model().rowCount(self.rootIndex())
        prefetch = range(max(0, rows[0] - columns), min(count, rows[-1] + columns + 1))
        return (rows + [row for row in prefetch if row not in visible])[:limit]
