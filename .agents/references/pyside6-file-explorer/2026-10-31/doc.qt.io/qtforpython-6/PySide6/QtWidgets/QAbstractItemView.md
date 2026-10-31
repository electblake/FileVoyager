<!--
source: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html
retrieved: 2026-10-31T21:18:30.315688+00:00
final_url: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html
content_type: text/html
-->

# PySide6.QtWidgets.QAbstractItemView - Qt for Python

[Skip to content](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#furo-main-content)

[Qt for Python](https://doc.qt.io/qtforpython-6/index.html)

[Back to top](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html)

# PySide6.QtWidgets.QAbstractItemView[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#pyside6-qtwidgets-qabstractitemview)

class QAbstractItemView[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView)

The ``[QAbstractItemView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView)  class provides the basic functionality for item view classes.

Details

Warning

This section contains snippets that were automatically translated from C++ to Python and may contain errors.

``[QAbstractItemView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView)  class is the base class for every standard view that uses a QAbstractItemModel. ``[QAbstractItemView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView)  is an abstract class and cannot itself be instantiated. It provides a standard interface for interoperating with models through the signals and slots mechanism, enabling subclasses to be kept up-to-date with changes to their models. This class provides standard support for keyboard and mouse navigation, viewport scrolling, item editing, and selections. The keyboard navigation implements this functionality:

> 

Keys

Functionality

Arrow keys

Changes the current item and selects it.

Ctrl+Arrow keys

Changes the current item but does not select it.

Shift+Arrow keys

Changes the current item and selects it. The previously selected item(s) is not deselected.

Ctrl+Space

Toggles selection of the current item.

Tab/Backtab

Changes the current item to the next/previous item.

Home/End

Selects the first/last item in the model.

Page up/Page down

Scrolls the rows shown up/down by the number of visible rows in the view.

Ctrl+A

Selects all items in the model.

Note that the above table assumes that the ``[selection mode](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id11)  allows the operations. For instance, you cannot select items if the selection mode is ``[NoSelection](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.SelectionMode)  .

The ``[QAbstractItemView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView)  class is one of the [Model/View Classes](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  and is part of Qt’s [model/view framework](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  .

The view classes that inherit ``[QAbstractItemView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView)  only need to implement their own view-specific functionality, such as drawing items, returning the geometry of items, finding items, etc.

``[QAbstractItemView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView)  provides common slots such as ``[edit()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.edit)  and ``[setCurrentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setCurrentIndex)  . Many protected slots are also provided, including ``[dataChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dataChanged)  , ``[rowsInserted()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.rowsInserted)  , ``[rowsAboutToBeRemoved()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.rowsAboutToBeRemoved)  , ``[selectionChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionChanged)  , and ``[currentChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.currentChanged)  .

The root item is returned by ``[rootIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.rootIndex)  , and the current item by ``[currentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.currentIndex)  . To make sure that an item is visible use ``[scrollTo()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.scrollTo)  .

Some of ``[QAbstractItemView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView)  ‘s functions are concerned with scrolling, for example ``[setHorizontalScrollMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setHorizontalScrollMode)  and ``[setVerticalScrollMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setVerticalScrollMode)  . To set the range of the scroll bars, you can, for example, reimplement the view’s `resizeEvent()` function:

> 

```
def resizeEvent(self, event):
    horizontalScrollBar().setRange(0, realWidth - width())
    ...
```

Note that the range is not updated until the widget is shown.

Several other functions are concerned with selection control; for example ``[setSelectionMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelectionMode)  , and ``[setSelectionBehavior()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelectionBehavior)  . This class provides a default selection model to work with ( ``[selectionModel()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionModel)  ), but this can be replaced by using ``[setSelectionModel()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelectionModel)  with an instance of QItemSelectionModel.

For complete control over the display and editing of items you can specify a delegate with ``[setItemDelegate()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setItemDelegate)  .

``[QAbstractItemView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView)  provides a lot of protected functions. Some are concerned with editing, for example, ``[edit()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.edit)  , and ``[commitData()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.commitData)  , whilst others are keyboard and mouse event handlers.

Note

If you inherit ``[QAbstractItemView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView)  and intend to update the contents of the viewport, you should use viewport-> ``[update()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.update)  instead of ``[update()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget.update)  as all painting operations take place on the viewport.

See also

[View Classes](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)[Model/View Programming](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)``[QAbstractItemModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel)

Inheritance diagram of PySide6.QtWidgets.QAbstractItemView

Inherited by:``[QTreeView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeView.html#PySide6.QtWidgets.QTreeView) , ``[QTreeWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeWidget.html#PySide6.QtWidgets.QTreeWidget) , ``[QHelpContentWidget](https://doc.qt.io/qtforpython-6/PySide6/QtHelp/QHelpContentWidget.html#PySide6.QtHelp.QHelpContentWidget) , ``[QTableView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableView.html#PySide6.QtWidgets.QTableView) , ``[QTableWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableWidget.html#PySide6.QtWidgets.QTableWidget) , ``[QListView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListView.html#PySide6.QtWidgets.QListView) , ``[QUndoView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QUndoView.html#PySide6.QtWidgets.QUndoView) , ``[QListWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListWidget.html#PySide6.QtWidgets.QListWidget) , ``[QHelpIndexWidget](https://doc.qt.io/qtforpython-6/PySide6/QtHelp/QHelpIndexWidget.html#PySide6.QtHelp.QHelpIndexWidget) , ``[QHeaderView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QHeaderView.html#PySide6.QtWidgets.QHeaderView) , ``[QColumnView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QColumnView.html#PySide6.QtWidgets.QColumnView)

## Synopsis[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#synopsis)

### Properties[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#properties)

- 

``[alternatingRowColorsᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.alternatingRowColors)  - Whether to draw the background using alternating colors

- 

``[autoScrollᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.autoScroll)  - Whether autoscrolling in drag move events is enabled

- 

``[autoScrollMarginᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.autoScrollMargin)  - The size of the area when auto scrolling is triggered

- 

``[defaultDropActionᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.defaultDropAction)  - The drop action that will be used by default in QAbstractItemView::drag()

- 

``[dragDropModeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dragDropMode)  - The drag and drop event the view will act upon

- 

``[dragDropOverwriteModeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dragDropOverwriteMode)  - The view’s drag and drop behavior

- 

``[dragEnabledᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dragEnabled)  - Whether the view supports dragging of its own items

- 

``[editTriggersᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.editTriggers)  - Which actions will initiate item editing

- 

``[horizontalScrollModeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.horizontalScrollMode)  - How the view scrolls its contents in the horizontal direction

- 

``[iconSizeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.iconSize)  - The size of items’ icons

- 

``[keyboardSearchFlagsᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.keyboardSearchFlags)

- 

``[selectionBehaviorᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionBehavior)  - Which selection behavior the view uses

- 

``[selectionModeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionMode)  - Which selection mode the view operates in

- 

``[showDropIndicatorᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.showDropIndicator)  - Whether the drop indicator is shown when dragging items and dropping

- 

``[tabKeyNavigationᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.tabKeyNavigation)  - Whether item navigation with tab and backtab is enabled

- 

``[textElideModeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.textElideMode)  - The position of the “…” in elided text

- 

``[updateThresholdᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.updateThreshold)

- 

``[verticalScrollModeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.verticalScrollMode)  - How the view scrolls its contents in the vertical direction

### Methods[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#methods)

- 

def ``[__init__()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.__init__)

- 

def ``[alternatingRowColors()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id0)

- 

def ``[autoScrollMargin()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id1)

- 

def ``[closePersistentEditor()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.closePersistentEditor)

- 

def ``[currentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.currentIndex)

- 

def ``[defaultDropAction()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id2)

- 

def ``[dirtyRegionOffset()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dirtyRegionOffset)

- 

def ``[doAutoScroll()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.doAutoScroll)

- 

def ``[dragDropMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id3)

- 

def ``[dragDropOverwriteMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id4)

- 

def ``[dragEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id5)

- 

def ``[dropIndicatorPosition()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dropIndicatorPosition)

- 

def ``[editTriggers()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id6)

- 

def ``[executeDelayedItemsLayout()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.executeDelayedItemsLayout)

- 

def ``[hasAutoScroll()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.hasAutoScroll)

- 

def ``[horizontalScrollMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id7)

- 

def ``[iconSize()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id8)

- 

def ``[indexWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.indexWidget)

- 

def ``[isPersistentEditorOpen()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.isPersistentEditorOpen)

- 

def ``[itemDelegate()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegate)

- 

def ``[itemDelegateForColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegateForColumn)

- 

def ``[itemDelegateForRow()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegateForRow)

- 

def ``[keyboardSearchFlags()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id9)

- 

def ``[model()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.model)

- 

def ``[openPersistentEditor()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.openPersistentEditor)

- 

def ``[resetHorizontalScrollMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.resetHorizontalScrollMode)

- 

def ``[resetVerticalScrollMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.resetVerticalScrollMode)

- 

def ``[rootIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.rootIndex)

- 

def ``[scheduleDelayedItemsLayout()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.scheduleDelayedItemsLayout)

- 

def ``[scrollDirtyRegion()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.scrollDirtyRegion)

- 

def ``[selectionBehavior()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id10)

- 

def ``[selectionMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id11)

- 

def ``[selectionModel()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionModel)

- 

def ``[setAlternatingRowColors()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setAlternatingRowColors)

- 

def ``[setAutoScroll()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setAutoScroll)

- 

def ``[setAutoScrollMargin()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setAutoScrollMargin)

- 

def ``[setDefaultDropAction()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDefaultDropAction)

- 

def ``[setDirtyRegion()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDirtyRegion)

- 

def ``[setDragDropMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDragDropMode)

- 

def ``[setDragDropOverwriteMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDragDropOverwriteMode)

- 

def ``[setDragEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDragEnabled)

- 

def ``[setDropIndicatorShown()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDropIndicatorShown)

- 

def ``[setEditTriggers()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setEditTriggers)

- 

def ``[setHorizontalScrollMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setHorizontalScrollMode)

- 

def ``[setIconSize()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setIconSize)

- 

def ``[setIndexWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setIndexWidget)

- 

def ``[setItemDelegate()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setItemDelegate)

- 

def ``[setItemDelegateForColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setItemDelegateForColumn)

- 

def ``[setItemDelegateForRow()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setItemDelegateForRow)

- 

def ``[setKeyboardSearchFlags()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setKeyboardSearchFlags)

- 

def ``[setSelectionBehavior()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelectionBehavior)

- 

def ``[setSelectionMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelectionMode)

- 

def ``[setState()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setState)

- 

def ``[setTabKeyNavigation()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setTabKeyNavigation)

- 

def ``[setTextElideMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setTextElideMode)

- 

def ``[setUpdateThreshold()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setUpdateThreshold)

- 

def ``[setVerticalScrollMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setVerticalScrollMode)

- 

def ``[showDropIndicator()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id12)

- 

def ``[sizeHintForIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.sizeHintForIndex)

- 

def ``[startAutoScroll()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.startAutoScroll)

- 

def ``[state()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.state)

- 

def ``[stopAutoScroll()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.stopAutoScroll)

- 

def ``[tabKeyNavigation()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id13)

- 

def ``[textElideMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id14)

- 

def ``[updateThreshold()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id15)

- 

def ``[verticalScrollMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id16)

### Virtual methods[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#virtual-methods)

- 

def ``[closeEditor()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.closeEditor)

- 

def ``[commitData()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.commitData)

- 

def ``[currentChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.currentChanged)

- 

def ``[dataChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dataChanged)

- 

def ``[doItemsLayout()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.doItemsLayout)

- 

def ``[edit()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.edit)

- 

def ``[editorDestroyed()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.editorDestroyed)

- 

def ``[horizontalOffset()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.horizontalOffset)

- 

def ``[horizontalScrollbarAction()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.horizontalScrollbarAction)

- 

def ``[horizontalScrollbarValueChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.horizontalScrollbarValueChanged)

- 

def ``[indexAt()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.indexAt)

- 

def ``[initViewItemOption()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.initViewItemOption)

- 

def ``[isIndexHidden()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.isIndexHidden)

- 

def ``[itemDelegateForIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegateForIndex)

- 

def ``[keyboardSearch()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.keyboardSearch)

- 

def ``[moveCursor()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.moveCursor)

- 

def ``[reset()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.reset)

- 

def ``[rowsAboutToBeRemoved()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.rowsAboutToBeRemoved)

- 

def ``[rowsInserted()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.rowsInserted)

- 

def ``[scrollTo()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.scrollTo)

- 

def ``[selectAll()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectAll)

- 

def ``[selectedIndexes()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectedIndexes)

- 

def ``[selectionChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionChanged)

- 

def ``[selectionCommand()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionCommand)

- 

def ``[setModel()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setModel)

- 

def ``[setRootIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setRootIndex)

- 

def ``[setSelection()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelection)

- 

def ``[setSelectionModel()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelectionModel)

- 

def ``[sizeHintForColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.sizeHintForColumn)

- 

def ``[sizeHintForRow()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.sizeHintForRow)

- 

def ``[startDrag()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.startDrag)

- 

def ``[updateEditorData()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.updateEditorData)

- 

def ``[updateEditorGeometries()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.updateEditorGeometries)

- 

def ``[updateGeometries()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.updateGeometries)

- 

def ``[verticalOffset()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.verticalOffset)

- 

def ``[verticalScrollbarAction()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.verticalScrollbarAction)

- 

def ``[verticalScrollbarValueChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.verticalScrollbarValueChanged)

- 

def ``[visualRect()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.visualRect)

- 

def ``[visualRegionForSelection()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.visualRegionForSelection)

### Slots[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#slots)

- 

def ``[clearSelection()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.clearSelection)

- 

def ``[edit()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.edit)

- 

def ``[scrollToBottom()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.scrollToBottom)

- 

def ``[scrollToTop()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.scrollToTop)

- 

def ``[setCurrentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setCurrentIndex)

- 

def ``[update()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.update)

### Signals[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#signals)

- 

def ``[activated()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.activated)

- 

def ``[clicked()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.clicked)

- 

def ``[doubleClicked()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.doubleClicked)

- 

def ``[entered()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.entered)

- 

def ``[iconSizeChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.iconSizeChanged)

- 

def ``[pressed()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.pressed)

- 

def ``[viewportEntered()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.viewportEntered)

Note

This documentation may contain snippets that were automatically translated from C++ to Python. We always welcome contributions to the snippet translation. If you see an issue with the translation, you can also let us know by creating a ticket on [https:/bugreports.qt.io/projects/PYSIDE](https://doc.qt.io/bugreports.qt.io/projects/PYSIDE)

class SelectionMode[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.SelectionMode)

This enum indicates how the view responds to user selections:

> 

Constant

Description

QAbstractItemView.SelectionMode.SingleSelection

When the user selects an item, any already-selected item becomes unselected. It is possible for the user to deselect the selected item by pressing the Ctrl key when clicking the selected item.

QAbstractItemView.SelectionMode.ContiguousSelection

When the user selects an item in the usual way, the selection is cleared and the new item selected. However, if the user presses the Shift key while clicking on an item, all items between the current item and the clicked item are selected or unselected, depending on the state of the clicked item.

QAbstractItemView.SelectionMode.ExtendedSelection

When the user selects an item in the usual way, the selection is cleared and the new item selected. However, if the user presses the Ctrl key when clicking on an item, the clicked item gets toggled and all other items are left untouched. If the user presses the Shift key while clicking on an item, all items between the current item and the clicked item are selected or unselected, depending on the state of the clicked item. Multiple items can be selected by dragging the mouse over them.

QAbstractItemView.SelectionMode.MultiSelection

When the user selects an item in the usual way, the selection status of that item is toggled and the other items are left alone. Multiple items can be toggled by dragging the mouse over them.

QAbstractItemView.SelectionMode.NoSelection

Items cannot be selected.

The most commonly used modes are SingleSelection and ExtendedSelection.

class SelectionBehavior[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.SelectionBehavior)

Constant

Description

QAbstractItemView.SelectionBehavior.SelectItems

Selecting single items.

QAbstractItemView.SelectionBehavior.SelectRows

Selecting only rows.

QAbstractItemView.SelectionBehavior.SelectColumns

Selecting only columns.

class ScrollHint[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.ScrollHint)

Constant

Description

QAbstractItemView.ScrollHint.EnsureVisible

Scroll to ensure that the item is visible.

QAbstractItemView.ScrollHint.PositionAtTop

Scroll to position the item at the top of the viewport.

QAbstractItemView.ScrollHint.PositionAtBottom

Scroll to position the item at the bottom of the viewport.

QAbstractItemView.ScrollHint.PositionAtCenter

Scroll to position the item at the center of the viewport.

class EditTrigger[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.EditTrigger)

(inherits `enum.Flag`) This enum describes actions which will initiate item editing.

> 

Constant

Description

QAbstractItemView.EditTrigger.NoEditTriggers

No editing possible.

QAbstractItemView.EditTrigger.CurrentChanged

Editing start whenever current item changes.

QAbstractItemView.EditTrigger.DoubleClicked

Editing starts when an item is double clicked.

QAbstractItemView.EditTrigger.SelectedClicked

Editing starts when clicking on an already selected item.

QAbstractItemView.EditTrigger.EditKeyPressed

Editing starts when the platform edit key has been pressed over an item.

QAbstractItemView.EditTrigger.AnyKeyPressed

Editing starts when any key is pressed over an item.

QAbstractItemView.EditTrigger.AllEditTriggers

Editing starts for all above actions.

class ScrollMode[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.ScrollMode)

Describes how the scrollbar should behave. When setting the scroll mode to ScrollPerPixel the single step size will adjust automatically unless it was set explicitly using ``[setSingleStep()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractSlider.html#PySide6.QtWidgets.QAbstractSlider.setSingleStep)  . The automatic adjustment can be restored by setting the single step size to -1.

> 

Constant

Description

QAbstractItemView.ScrollMode.ScrollPerItem

The view will scroll the contents one item at a time.

QAbstractItemView.ScrollMode.ScrollPerPixel

The view will scroll the contents one pixel at a time.

class DragDropMode[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.DragDropMode)

Describes the various drag and drop events the view can act upon. By default the view does not support dragging or dropping (`NoDragDrop`).

> 

Constant

Description

QAbstractItemView.DragDropMode.NoDragDrop

Does not support dragging or dropping.

QAbstractItemView.DragDropMode.DragOnly

The view supports dragging of its own items

QAbstractItemView.DragDropMode.DropOnly

The view accepts drops

QAbstractItemView.DragDropMode.DragDrop

The view supports both dragging and dropping

QAbstractItemView.DragDropMode.InternalMove

The view accepts move (not copy ) operations only from itself.

Note that the model used needs to provide support for drag and drop operations.

> 

See also

``[setDragDropMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDragDropMode)[Using drag and drop with item views](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)

class CursorAction[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.CursorAction)

This enum describes the different ways to navigate between items,

> 

Constant

Description

QAbstractItemView.CursorAction.MoveUp

Move to the item above the current item.

QAbstractItemView.CursorAction.MoveDown

Move to the item below the current item.

QAbstractItemView.CursorAction.MoveLeft

Move to the item left of the current item.

QAbstractItemView.CursorAction.MoveRight

Move to the item right of the current item.

QAbstractItemView.CursorAction.MoveHome

Move to the top-left corner item.

QAbstractItemView.CursorAction.MoveEnd

Move to the bottom-right corner item.

QAbstractItemView.CursorAction.MovePageUp

Move one page up above the current item.

QAbstractItemView.CursorAction.MovePageDown

Move one page down below the current item.

QAbstractItemView.CursorAction.MoveNext

Move to the item after the current item.

QAbstractItemView.CursorAction.MovePrevious

Move to the item before the current item.

See also

``[moveCursor()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.moveCursor)

class State[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.State)

Describes the different states the view can be in. This is usually only interesting when reimplementing your own view.

> 

Constant

Description

QAbstractItemView.State.NoState

The is the default state.

QAbstractItemView.State.DraggingState

The user is dragging items.

QAbstractItemView.State.DragSelectingState

The user is selecting items.

QAbstractItemView.State.EditingState

The user is editing an item in a widget editor.

QAbstractItemView.State.ExpandingState

The user is opening a branch of items.

QAbstractItemView.State.CollapsingState

The user is closing a branch of items.

QAbstractItemView.State.AnimatingState

The item view is performing an animation.

class DropIndicatorPosition[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.DropIndicatorPosition)

This enum indicates the position of the drop indicator in relation to the index at the current mouse position:

> 

Constant

Description

QAbstractItemView.DropIndicatorPosition.OnItem

The item will be dropped on the index.

QAbstractItemView.DropIndicatorPosition.AboveItem

The item will be dropped above the index.

QAbstractItemView.DropIndicatorPosition.BelowItem

The item will be dropped below the index.

QAbstractItemView.DropIndicatorPosition.OnViewport

The item will be dropped onto a region of the viewport with no items. The way each view handles items dropped onto the viewport depends on the behavior of the underlying model in use.

Note

Properties can be used directly when `from __feature__ import true_property` is used or via accessor functions otherwise.

property alternatingRowColorsᅟ : bool[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.alternatingRowColors)

This property holds whether to draw the background using alternating colors.

If this property is `true`, the item background will be drawn using QPalette::Base and QPalette::AlternateBase; otherwise the background will be drawn using the QPalette::Base color.

By default, this property is `false`.

Access functions:

- 

``[alternatingRowColors()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id0)

- 

``[setAlternatingRowColors()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setAlternatingRowColors)

property autoScrollᅟ : bool[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.autoScroll)

This property holds whether autoscrolling in drag move events is enabled.

If this property is set to true (the default), the ``[QAbstractItemView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView)  automatically scrolls the contents of the view if the user drags within 16 pixels of the viewport edge. If the current item changes, then the view will scroll automatically to ensure that the current item is fully visible.

This property only works if the viewport accepts drops. Autoscroll is switched off by setting this property to false.

Access functions:

- 

``[hasAutoScroll()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.hasAutoScroll)

- 

``[setAutoScroll()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setAutoScroll)

property autoScrollMarginᅟ : int[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.autoScrollMargin)

This property holds the size of the area when auto scrolling is triggered.

This property controls the size of the area at the edge of the viewport that triggers autoscrolling. The default value is 16 pixels.

Access functions:

- 

``[autoScrollMargin()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id1)

- 

``[setAutoScrollMargin()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setAutoScrollMargin)

property defaultDropActionᅟ :[Qt.DropAction](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.DropAction)[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.defaultDropAction)

This property holds the drop action that will be used by default in QAbstractItemView::drag()..

If the property is not set, the drop action is CopyAction when the supported actions support CopyAction.

> 

See also

``[showDropIndicator()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id12)``[dragDropOverwriteMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id4)

Access functions:

- 

``[defaultDropAction()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id2)

- 

``[setDefaultDropAction()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDefaultDropAction)

property dragDropModeᅟ :[QAbstractItemView.DragDropMode](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.DragDropMode)[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dragDropMode)

This property holds the drag and drop event the view will act upon.

> 

See also

``[showDropIndicator()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id12)``[dragDropOverwriteMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id4)

Access functions:

- 

``[dragDropMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id3)

- 

``[setDragDropMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDragDropMode)

property dragDropOverwriteModeᅟ : bool[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dragDropOverwriteMode)

This property holds the view’s drag and drop behavior.

If its value is `true`, the selected data will overwrite the existing item data when dropped, while moving the data will clear the item. If its value is `false`, the selected data will be inserted as a new item when the data is dropped. When the data is moved, the item is removed as well.

The default value is `false`, as in the ``[QListView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListView.html#PySide6.QtWidgets.QListView)  and ``[QTreeView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeView.html#PySide6.QtWidgets.QTreeView)  subclasses. In the ``[QTableView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableView.html#PySide6.QtWidgets.QTableView)  subclass, on the other hand, the property has been set to `true`.

Note: This is not intended to prevent overwriting of items. The model’s implementation of flags() should do that by not returning Qt::ItemIsDropEnabled.

> 

See also

``[dragDropMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id3)

Access functions:

- 

``[dragDropOverwriteMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id4)

- 

``[setDragDropOverwriteMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDragDropOverwriteMode)

property dragEnabledᅟ : bool[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dragEnabled)

This property holds whether the view supports dragging of its own items.

> 

See also

``[showDropIndicator()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id12)``[DragDropMode](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.DragDropMode)``[dragDropOverwriteMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id4)`acceptDrops()`

Access functions:

- 

``[dragEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id5)

- 

``[setDragEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDragEnabled)

property editTriggersᅟ : Combination of QAbstractItemView.EditTrigger[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.editTriggers)

This property holds which actions will initiate item editing.

This property is a selection of flags defined by ``[EditTrigger](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.EditTrigger)  , combined using the OR operator. The view will only initiate the editing of an item if the action performed is set in this property.

The default value is:

> 

- 

for ``[QTableView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableView.html#PySide6.QtWidgets.QTableView)  : ``[DoubleClicked](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.EditTrigger)  | ``[AnyKeyPressed](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.EditTrigger)

- 

for all other views: ``[DoubleClicked](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.EditTrigger)  | ``[EditKeyPressed](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.EditTrigger)

Access functions:

- 

``[editTriggers()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id6)

- 

``[setEditTriggers()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setEditTriggers)

property horizontalScrollModeᅟ :[QAbstractItemView.ScrollMode](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.ScrollMode)[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.horizontalScrollMode)

This property holds how the view scrolls its contents in the horizontal direction.

This property controls how the view scroll its contents horizontally. Scrolling can be done either per pixel or per item. Its default value comes from the style via the ``[SH_ItemView_ScrollMode](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyle.html#PySide6.QtWidgets.QStyle.StyleHint)  style hint.

Access functions:

- 

``[horizontalScrollMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id7)

- 

``[setHorizontalScrollMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setHorizontalScrollMode)

- 

``[resetHorizontalScrollMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.resetHorizontalScrollMode)

property iconSizeᅟ :[QSize](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSize.html#PySide6.QtCore.QSize)[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.iconSize)

This property holds the size of items’ icons.

Setting this property when the view is visible will cause the items to be laid out again.

Access functions:

- 

``[iconSize()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id8)

- 

``[setIconSize()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setIconSize)

- 

Signal ``[iconSizeChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.iconSizeChanged)

property keyboardSearchFlagsᅟ : Combination of Qt.MatchFlag[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.keyboardSearchFlags)

This property determines how the default implementation of ``[keyboardSearch()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.keyboardSearch)  matches the given string against the model’s data.

The default value is `Qt::MatchStartsWith|Qt::MatchWrap`.

> 

See also

``[keyboardSearch()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.keyboardSearch)``[match()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel.match)

Access functions:

- 

``[keyboardSearchFlags()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id9)

- 

``[setKeyboardSearchFlags()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setKeyboardSearchFlags)

property selectionBehaviorᅟ :[QAbstractItemView.SelectionBehavior](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.SelectionBehavior)[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionBehavior)

This property holds which selection behavior the view uses.

This property holds whether selections are done in terms of single items, rows or columns.

> 

See also

``[SelectionMode](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.SelectionMode)``[SelectionBehavior](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.SelectionBehavior)

Access functions:

- 

``[selectionBehavior()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id10)

- 

``[setSelectionBehavior()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelectionBehavior)

property selectionModeᅟ :[QAbstractItemView.SelectionMode](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.SelectionMode)[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionMode)

This property holds which selection mode the view operates in.

This property controls whether the user can select one or many items and, in many-item selections, whether the selection must be a continuous range of items.

> 

See also

``[SelectionMode](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.SelectionMode)``[SelectionBehavior](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.SelectionBehavior)

Access functions:

- 

``[selectionMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id11)

- 

``[setSelectionMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelectionMode)

property showDropIndicatorᅟ : bool[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.showDropIndicator)

This property holds whether the drop indicator is shown when dragging items and dropping..

> 

See also

``[dragEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id5)``[DragDropMode](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.DragDropMode)``[dragDropOverwriteMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id4)`acceptDrops()`

Access functions:

- 

``[showDropIndicator()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id12)

- 

``[setDropIndicatorShown()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDropIndicatorShown)

property tabKeyNavigationᅟ : bool[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.tabKeyNavigation)

This property holds whether item navigation with tab and backtab is enabled..

Access functions:

- 

``[tabKeyNavigation()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id13)

- 

``[setTabKeyNavigation()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setTabKeyNavigation)

property textElideModeᅟ :[Qt.TextElideMode](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.TextElideMode)[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.textElideMode)

This property holds the position of the “…” in elided text..

The default value for all item views is Qt::ElideRight.

Access functions:

- 

``[textElideMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id14)

- 

``[setTextElideMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setTextElideMode)

property updateThresholdᅟ : int[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.updateThreshold)

This property holds the amount of changed indexes to directly trigger a full update of the view inside ``[dataChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dataChanged)  .

The algorithm inside ``[dataChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dataChanged)  tries to minimize a full update of the view by calculating if the changed indexes are visible or not. For very large models, with a lot of large changes, this might take longer than the actual update so it’s counter-productive. This property gives the ability to control the algorithm to skip the check and directly trigger a full update when the amount of changed indexes exceeds the given value.

The default value is 200.

> 

See also

``[dataChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dataChanged)

Access functions:

- 

``[updateThreshold()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id15)

- 

``[setUpdateThreshold()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setUpdateThreshold)

property verticalScrollModeᅟ :[QAbstractItemView.ScrollMode](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.ScrollMode)[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.verticalScrollMode)

This property holds how the view scrolls its contents in the vertical direction.

This property controls how the view scroll its contents vertically. Scrolling can be done either per pixel or per item. Its default value comes from the style via the ``[SH_ItemView_ScrollMode](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyle.html#PySide6.QtWidgets.QStyle.StyleHint)  style hint.

Access functions:

- 

``[verticalScrollMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id16)

- 

``[setVerticalScrollMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setVerticalScrollMode)

- 

``[resetVerticalScrollMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.resetVerticalScrollMode)

__init__ ([parent=None ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.__init__) Parameters :

parent  – ``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

Constructs an abstract item view with the given `parent`.

activated (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.activated) Parameters :

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

This signal is emitted when the item specified by `index` is activated by the user. How to activate items depends on the platform; e.g., by single- or double-clicking the item, or by pressing the Return or Enter key when the item is current.

> 

See also

``[clicked()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.clicked)``[doubleClicked()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.doubleClicked)``[entered()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.entered)``[pressed()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.pressed)

alternatingRowColors ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id0) Return type :

bool

See also

``[setAlternatingRowColors()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setAlternatingRowColors)

Getter of property ``[alternatingRowColorsᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.alternatingRowColors)  .

autoScrollMargin ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id1) Return type :

int

See also

``[setAutoScrollMargin()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setAutoScrollMargin)

Getter of property ``[autoScrollMarginᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.autoScrollMargin)  .

clearSelection ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.clearSelection)

Deselects all selected items. The current index will not be changed.

> 

See also

``[setSelection()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelection)``[selectAll()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectAll)

clicked (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.clicked) Parameters :

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

This signal is emitted when a mouse button is left-clicked. The item the mouse was clicked on is specified by `index`. The signal is only emitted when the index is valid.

> 

See also

``[activated()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.activated)``[doubleClicked()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.doubleClicked)``[entered()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.entered)``[pressed()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.pressed)

closeEditor (editor , hint )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.closeEditor) Parameters :

- 

editor  – ``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

- 

hint  – ``[EndEditHint](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate.EndEditHint)

Closes the given `editor`, and releases it. The `hint` is used to specify how the view should respond to the end of the editing operation. For example, the hint may indicate that the next item in the view should be opened for editing.

> 

See also

``[edit()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.edit)``[commitData()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.commitData)

closePersistentEditor (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.closePersistentEditor) Parameters :

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Closes the persistent editor for the item at the given `index`.

> 

See also

``[openPersistentEditor()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.openPersistentEditor)``[isPersistentEditorOpen()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.isPersistentEditorOpen)

commitData (editor )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.commitData) Parameters :

editor  – ``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

Commit the data in the `editor` to the model.

> 

See also

``[closeEditor()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.closeEditor)

currentChanged (current , previous )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.currentChanged) Parameters :

- 

current  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

- 

previous  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

This slot is called when a new item becomes the current item. The previous current item is specified by the `previous` index, and the new item by the `current` index.

If you want to know about changes to items see the ``[dataChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dataChanged)  signal.

currentIndex ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.currentIndex) Return type :

``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Returns the model index of the current item.

> 

See also

``[setCurrentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setCurrentIndex)

dataChanged (topLeft , bottomRight [, roles=list() ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dataChanged) Parameters :

- 

topLeft  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

- 

bottomRight  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

- 

roles  – .list of int

This slot is called when items with the given `roles` are changed in the model. The changed items are those from `topLeft` to `bottomRight` inclusive. If just one item is changed `topLeft` == `bottomRight`.

The `roles` which have been changed can either be an empty container (meaning everything has changed), or a non-empty container with the subset of roles which have changed.

Note

: Qt::ToolTipRole is not honored by dataChanged() in the views provided by Qt.

defaultDropAction ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id2) Return type :

``[DropAction](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.DropAction)

See also

``[setDefaultDropAction()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDefaultDropAction)

Getter of property ``[defaultDropActionᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.defaultDropAction)  .

dirtyRegionOffset ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dirtyRegionOffset) Return type :

``[QPoint](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QPoint.html#PySide6.QtCore.QPoint)

Returns the offset of the dirty regions in the view.

If you use ``[scrollDirtyRegion()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.scrollDirtyRegion)  and implement a `paintEvent()` in a subclass of ``[QAbstractItemView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView)  , you should translate the area given by the paint event with the offset returned from this function.

> 

See also

``[scrollDirtyRegion()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.scrollDirtyRegion)``[setDirtyRegion()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDirtyRegion)

doAutoScroll ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.doAutoScroll) doItemsLayout ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.doItemsLayout) doubleClicked (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.doubleClicked) Parameters :

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

This signal is emitted when a mouse button is double-clicked. The item the mouse was double-clicked on is specified by `index`. The signal is only emitted when the index is valid.

> 

See also

``[clicked()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.clicked)``[activated()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.activated)

dragDropMode ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id3) Return type :

``[DragDropMode](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.DragDropMode)

See also

``[setDragDropMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDragDropMode)

Getter of property ``[dragDropModeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dragDropMode)  .

dragDropOverwriteMode ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id4) Return type :

bool

See also

``[setDragDropOverwriteMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDragDropOverwriteMode)

Getter of property ``[dragDropOverwriteModeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dragDropOverwriteMode)  .

dragEnabled ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id5) Return type :

bool

See also

``[setDragEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDragEnabled)

Getter of property ``[dragEnabledᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dragEnabled)  .

dropIndicatorPosition ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dropIndicatorPosition) Return type :

``[DropIndicatorPosition](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.DropIndicatorPosition)

Returns the position of the drop indicator in relation to the closest item.

edit (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.edit) Parameters :

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Starts editing the item corresponding to the given `index` if it is editable.

Note that this function does not change the current index. Since the current index defines the next and previous items to edit, users may find that keyboard navigation does not work as expected. To provide consistent navigation behavior, call ``[setCurrentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setCurrentIndex)  before this function with the same model index.

> 

See also

``[flags()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex.flags)

edit (index , trigger , event ) Parameters :

- 

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

- 

trigger  – ``[EditTrigger](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.EditTrigger)

- 

event  – ``[QEvent](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QEvent.html#PySide6.QtCore.QEvent)

Return type :

bool

Starts editing the item at `index`, creating an editor if necessary, and returns `true` if the view’s ``[State](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.State)  is now ``[EditingState](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.State)  ; otherwise returns `false`.

The action that caused the editing process is described by `trigger`, and the associated event is specified by `event`.

Editing can be forced by specifying the `trigger` to be ``[AllEditTriggers](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.EditTrigger)  .

> 

See also

``[closeEditor()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.closeEditor)

editTriggers ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id6) Return type :

Combination of ``[EditTrigger](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.EditTrigger)

See also

``[setEditTriggers()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setEditTriggers)

Getter of property ``[editTriggersᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.editTriggers)  .

editorDestroyed (editor )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.editorDestroyed) Parameters :

editor  – ``[QObject](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QObject.html#PySide6.QtCore.QObject)

This function is called when the given `editor` has been destroyed.

> 

See also

``[closeEditor()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.closeEditor)

entered (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.entered) Parameters :

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

This signal is emitted when the mouse cursor enters the item specified by `index`. Mouse tracking needs to be enabled for this feature to work.

> 

See also

``[viewportEntered()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.viewportEntered)``[activated()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.activated)``[clicked()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.clicked)``[doubleClicked()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.doubleClicked)``[pressed()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.pressed)

executeDelayedItemsLayout ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.executeDelayedItemsLayout)

Executes the scheduled layouts without waiting for the event processing to begin.

> 

See also

``[scheduleDelayedItemsLayout()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.scheduleDelayedItemsLayout)

hasAutoScroll ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.hasAutoScroll) Return type :

bool

Getter of property ``[autoScrollᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.autoScroll)  .

abstract horizontalOffset ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.horizontalOffset) Return type :

int

Returns the horizontal offset of the view.

In the base class this is a pure virtual function.

> 

See also

``[verticalOffset()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.verticalOffset)

horizontalScrollMode ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id7) Return type :

``[ScrollMode](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.ScrollMode)

See also

``[setHorizontalScrollMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setHorizontalScrollMode)

Getter of property ``[horizontalScrollModeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.horizontalScrollMode)  .

horizontalScrollbarAction (action )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.horizontalScrollbarAction) Parameters :

action  – int

horizontalScrollbarValueChanged (value )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.horizontalScrollbarValueChanged) Parameters :

value  – int

iconSize ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id8) Return type :

``[QSize](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSize.html#PySide6.QtCore.QSize)

See also

``[setIconSize()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setIconSize)

Getter of property ``[iconSizeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.iconSize)  .

iconSizeChanged (size )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.iconSizeChanged) Parameters :

size  – ``[QSize](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSize.html#PySide6.QtCore.QSize)

Notification signal of property ``[iconSizeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.iconSize)  .

abstract indexAt (point )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.indexAt) Parameters :

point  – ``[QPoint](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QPoint.html#PySide6.QtCore.QPoint)

Return type :

``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Returns the model index of the item at the viewport coordinates `point`.

In the base class this is a pure virtual function.

> 

See also

``[visualRect()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.visualRect)

indexWidget (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.indexWidget) Parameters :

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Return type :

``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

Returns the widget for the item at the given `index`.

> 

See also

``[setIndexWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setIndexWidget)

initViewItemOption (option )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.initViewItemOption) Parameters :

option  – ``[QStyleOptionViewItem](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyleOptionViewItem.html#PySide6.QtWidgets.QStyleOptionViewItem)

Initialize the `option` structure with the view’s palette, font, state, alignments etc.

Note

Implementations of this methods should check the [version](https://doc.qt.io/qt-6/qstyleoption.html#version-var)  of the structure received, populate all members the implementation is familiar with, and set the version member to the one supported by the implementation before returning.

abstract isIndexHidden (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.isIndexHidden) Parameters :

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Return type :

bool

Returns `true` if the item referred to by the given `index` is hidden in the view, otherwise returns `false`.

Hiding is a view specific feature. For example in TableView a column can be marked as hidden or a row in the TreeView.

In the base class this is a pure virtual function.

isPersistentEditorOpen (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.isPersistentEditorOpen) Parameters :

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Return type :

bool

Returns whether a persistent editor is open for the item at index `index`.

> 

See also

``[openPersistentEditor()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.openPersistentEditor)``[closePersistentEditor()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.closePersistentEditor)

itemDelegate ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegate) Return type :

``[QAbstractItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate)

Returns the item delegate used by this view and model. This is either one set with ``[setItemDelegate()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setItemDelegate)  , or the default one.

> 

See also

``[setItemDelegate()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setItemDelegate)

itemDelegate (index ) Parameters :

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Return type :

``[QAbstractItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate)

Note

This function is deprecated.

Use ``[itemDelegateForIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegateForIndex)  instead. Returns the item delegate used by this view and model for the given `index`.

itemDelegateForColumn (column )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegateForColumn) Parameters :

column  – int

Return type :

``[QAbstractItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate)

Returns the item delegate used by this view and model for the given `column`. You can call ``[itemDelegate()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegate)  to get a pointer to the current delegate for a given index.

> 

See also

``[setItemDelegateForColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setItemDelegateForColumn)``[itemDelegateForRow()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegateForRow)``[itemDelegate()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegate)

itemDelegateForIndex (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegateForIndex) Parameters :

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Return type :

``[QAbstractItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate)

Returns the item delegate used by this view and model for the given `index`.

> 

See also

``[setItemDelegate()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setItemDelegate)``[setItemDelegateForRow()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setItemDelegateForRow)``[setItemDelegateForColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setItemDelegateForColumn)

itemDelegateForRow (row )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegateForRow) Parameters :

row  – int

Return type :

``[QAbstractItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate)

Returns the item delegate used by this view and model for the given `row`, or `None` if no delegate has been assigned. You can call ``[itemDelegate()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegate)  to get a pointer to the current delegate for a given index.

> 

See also

``[setItemDelegateForRow()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setItemDelegateForRow)``[itemDelegateForColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegateForColumn)``[setItemDelegate()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setItemDelegate)

keyboardSearch (search )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.keyboardSearch) Parameters :

search  – str

Moves to and selects the item best matching the string `search`. If no item is found nothing happens.

In the default implementation, the search is reset if `search` is empty, or the time interval since the last search has exceeded ``[keyboardInputInterval()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QApplication.html#id3)  .

keyboardSearchFlags ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id9) Return type :

Combination of ``[MatchFlag](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.MatchFlag)

See also

``[setKeyboardSearchFlags()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setKeyboardSearchFlags)

Getter of property ``[keyboardSearchFlagsᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.keyboardSearchFlags)  .

model ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.model) Return type :

``[QAbstractItemModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel)

Returns the model that this view is presenting.

> 

See also

``[setModel()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setModel)

abstract moveCursor (cursorAction , modifiers )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.moveCursor) Parameters :

- 

cursorAction  – ``[CursorAction](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.CursorAction)

- 

modifiers  – Combination of ``[KeyboardModifier](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.KeyboardModifier)

Return type :

``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Returns a QModelIndex object pointing to the next object in the view, based on the given `cursorAction` and keyboard modifiers specified by `modifiers`.

In the base class this is a pure virtual function.

openPersistentEditor (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.openPersistentEditor) Parameters :

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Opens a persistent editor on the item at the given `index`. If no editor exists, the delegate will create a new editor.

> 

See also

``[closePersistentEditor()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.closePersistentEditor)``[isPersistentEditorOpen()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.isPersistentEditorOpen)

pressed (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.pressed) Parameters :

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

This signal is emitted when a mouse button is pressed. The item the mouse was pressed on is specified by `index`. The signal is only emitted when the index is valid.

Use the QGuiApplication::mouseButtons() function to get the state of the mouse buttons.

> 

See also

``[activated()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.activated)``[clicked()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.clicked)``[doubleClicked()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.doubleClicked)``[entered()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.entered)

reset ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.reset)

Reset the internal state of the view.

Warning

This function will reset open editors, scroll bar positions, selections, etc. Existing changes will not be committed. If you would like to save your changes when resetting the view, you can reimplement this function, commit your changes, and then call the superclass’ implementation.

resetHorizontalScrollMode ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.resetHorizontalScrollMode)

Reset function of property ``[horizontalScrollModeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.horizontalScrollMode)  .

resetVerticalScrollMode ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.resetVerticalScrollMode)

Reset function of property ``[verticalScrollModeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.verticalScrollMode)  .

rootIndex ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.rootIndex) Return type :

``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Returns the model index of the model’s root item. The root item is the parent item to the view’s toplevel items. The root can be invalid.

> 

See also

``[setRootIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setRootIndex)

rowsAboutToBeRemoved (parent , start , end )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.rowsAboutToBeRemoved) Parameters :

- 

parent  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

- 

start  – int

- 

end  – int

This slot is called when rows are about to be removed. The deleted rows are those under the given `parent` from `start` to `end` inclusive.

> 

See also

``[rowsInserted()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.rowsInserted)

rowsInserted (parent , start , end )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.rowsInserted) Parameters :

- 

parent  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

- 

start  – int

- 

end  – int

This slot is called when rows are inserted. The new rows are those under the given `parent` from `start` to `end` inclusive. The base class implementation calls fetchMore() on the model to check for more data.

> 

See also

``[rowsAboutToBeRemoved()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.rowsAboutToBeRemoved)

scheduleDelayedItemsLayout ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.scheduleDelayedItemsLayout)

Schedules a layout of the items in the view to be executed when the event processing starts.

Even if scheduleDelayedItemsLayout() is called multiple times before events are processed, the view will only do the layout once.

> 

See also

``[executeDelayedItemsLayout()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.executeDelayedItemsLayout)

scrollDirtyRegion (dx , dy )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.scrollDirtyRegion) Parameters :

- 

dx  – int

- 

dy  – int

Prepares the view for scrolling by (`dx`,``dy``) pixels by moving the dirty regions in the opposite direction. You only need to call this function if you are implementing a scrolling viewport in your view subclass.

If you implement ``[scrollContentsBy()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractScrollArea.html#PySide6.QtWidgets.QAbstractScrollArea.scrollContentsBy)  in a subclass of ``[QAbstractItemView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView)  , call this function before you call ``[scroll()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget.scroll)  on the viewport. Alternatively, just call ``[update()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.update)  .

> 

See also

``[scrollContentsBy()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractScrollArea.html#PySide6.QtWidgets.QAbstractScrollArea.scrollContentsBy)``[dirtyRegionOffset()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dirtyRegionOffset)``[setDirtyRegion()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDirtyRegion)

abstract scrollTo (index [, hint=QAbstractItemView.ScrollHint.EnsureVisible ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.scrollTo) Parameters :

- 

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

- 

hint  – ``[ScrollHint](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.ScrollHint)

Scrolls the view if necessary to ensure that the item at `index` is visible. The view will try to position the item according to the given `hint`.

In the base class this is a pure virtual function.

scrollToBottom ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.scrollToBottom)

Scrolls the view to the bottom.

> 

See also

``[scrollTo()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.scrollTo)``[scrollToTop()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.scrollToTop)

scrollToTop ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.scrollToTop)

Scrolls the view to the top.

> 

See also

``[scrollTo()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.scrollTo)``[scrollToBottom()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.scrollToBottom)

selectAll ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectAll)

Selects all items in the view. This function will use the selection behavior set on the view when selecting.

> 

See also

``[setSelection()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelection)``[selectedIndexes()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectedIndexes)``[clearSelection()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.clearSelection)

selectedIndexes ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectedIndexes) Return type :

.list of [QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

This convenience function returns a list of all selected and non-hidden item indexes in the view. The list contains no duplicates, and is not sorted.

> 

See also

``[selectedIndexes()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id3)

selectionBehavior ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id10) Return type :

``[SelectionBehavior](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.SelectionBehavior)

See also

``[setSelectionBehavior()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelectionBehavior)

Getter of property ``[selectionBehaviorᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionBehavior)  .

selectionChanged (selected , deselected )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionChanged) Parameters :

- 

selected  – ``[QItemSelection](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelection.html#PySide6.QtCore.QItemSelection)

- 

deselected  – ``[QItemSelection](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelection.html#PySide6.QtCore.QItemSelection)

This slot is called when the selection is changed. The previous selection (which may be empty), is specified by `deselected`, and the new selection by `selected`.

> 

See also

``[setSelection()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelection)

selectionCommand (index [, event=None ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionCommand) Parameters :

- 

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

- 

event  – ``[QEvent](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QEvent.html#PySide6.QtCore.QEvent)

Return type :

Combination of ``[SelectionFlag](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.SelectionFlag)

Returns the SelectionFlags to be used when updating a selection model for the specified `index`. The result depends on the current ``[selectionMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id11)  , and on the user input event `event`, which can be `None`.

Reimplement this function to define your own selection behavior.

> 

See also

``[setSelection()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelection)

selectionMode ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id11) Return type :

``[SelectionMode](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.SelectionMode)

See also

``[setSelectionMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelectionMode)

Getter of property ``[selectionModeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionMode)  .

selectionModel ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionModel) Return type :

``[QItemSelectionModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel)

Returns the current selection model.

> 

See also

``[setSelectionModel()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelectionModel)``[selectedIndexes()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectedIndexes)

setAlternatingRowColors (enable )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setAlternatingRowColors) Parameters :

enable  – bool

See also

``[alternatingRowColors()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id0)

Setter of property ``[alternatingRowColorsᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.alternatingRowColors)  .

setAutoScroll (enable )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setAutoScroll) Parameters :

enable  – bool

See also

``[hasAutoScroll()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.hasAutoScroll)

Setter of property ``[autoScrollᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.autoScroll)  .

setAutoScrollMargin (margin )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setAutoScrollMargin) Parameters :

margin  – int

See also

``[autoScrollMargin()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id1)

Setter of property ``[autoScrollMarginᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.autoScrollMargin)  .

setCurrentIndex (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setCurrentIndex) Parameters :

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Sets the current item to be the item at `index`.

Unless the current selection mode is ``[NoSelection](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.SelectionMode)  , the item is also selected. Note that this function also updates the starting position for any new selections the user performs.

To set an item as the current item without selecting it, call

`selectionModel()->setCurrentIndex(index, QItemSelectionModel::NoUpdate);`

> 

See also

``[currentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.currentIndex)``[currentChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.currentChanged)``[selectionMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id11)

setDefaultDropAction (dropAction )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDefaultDropAction) Parameters :

dropAction  – ``[DropAction](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.DropAction)

See also

``[defaultDropAction()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id2)

Setter of property ``[defaultDropActionᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.defaultDropAction)  .

setDirtyRegion (region )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDirtyRegion) Parameters :

region  – ``[QRegion](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QRegion.html#PySide6.QtGui.QRegion)

Marks the given `region` as dirty and schedules it to be updated. You only need to call this function if you are implementing your own view subclass.

> 

See also

``[scrollDirtyRegion()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.scrollDirtyRegion)``[dirtyRegionOffset()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dirtyRegionOffset)

setDragDropMode (behavior )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDragDropMode) Parameters :

behavior  – ``[DragDropMode](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.DragDropMode)

See also

``[dragDropMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id3)

Setter of property ``[dragDropModeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dragDropMode)  .

setDragDropOverwriteMode (overwrite )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDragDropOverwriteMode) Parameters :

overwrite  – bool

See also

``[dragDropOverwriteMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id4)

Setter of property ``[dragDropOverwriteModeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dragDropOverwriteMode)  .

setDragEnabled (enable )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDragEnabled) Parameters :

enable  – bool

See also

``[dragEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id5)

Setter of property ``[dragEnabledᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.dragEnabled)  .

setDropIndicatorShown (enable )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setDropIndicatorShown) Parameters :

enable  – bool

Setter of property ``[showDropIndicatorᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.showDropIndicator)  .

setEditTriggers (triggers )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setEditTriggers) Parameters :

triggers  – Combination of ``[EditTrigger](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.EditTrigger)

See also

``[editTriggers()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id6)

Setter of property ``[editTriggersᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.editTriggers)  .

setHorizontalScrollMode (mode )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setHorizontalScrollMode) Parameters :

mode  – ``[ScrollMode](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.ScrollMode)

See also

``[horizontalScrollMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id7)

Setter of property ``[horizontalScrollModeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.horizontalScrollMode)  .

setIconSize (size )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setIconSize) Parameters :

size  – ``[QSize](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSize.html#PySide6.QtCore.QSize)

See also

``[iconSize()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id8)

Setter of property ``[iconSizeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.iconSize)  .

setIndexWidget (index , widget )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setIndexWidget) Parameters :

- 

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

- 

widget  – ``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

Warning

This section contains snippets that were automatically translated from C++ to Python and may contain errors.

Sets the given `widget` on the item at the given `index`, passing the ownership of the widget to the viewport.

If `index` is invalid (e.g., if you pass the root index), this function will do nothing.

The given `widget`'s ``[autoFillBackground](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)  property must be set to true, otherwise the widget’s background will be transparent, showing both the model data and the item at the given `index`.

Note

The view takes ownership of the `widget`. This means if index widget A is replaced with index widget B, index widget A will be deleted. For example, in the code snippet below, the ``[QLineEdit](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QLineEdit.html#PySide6.QtWidgets.QLineEdit)  object will be deleted.

```
setIndexWidget(index, QLineEdit())
...
setIndexWidget(index, QTextEdit())
```

This function should only be used to display static content within the visible area corresponding to an item of data. If you want to display custom dynamic content or implement a custom editor widget, subclass ``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)  instead.

> 

See also

``[indexWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.indexWidget)[Delegate Classes](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)

setItemDelegate (delegate )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setItemDelegate) Parameters :

delegate  – ``[QAbstractItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate)

Sets the item delegate for this view and its model to `delegate`. This is useful if you want complete control over the editing and display of items.

Any existing delegate will be removed, but not deleted. ``[QAbstractItemView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView)  does not take ownership of `delegate`.

Warning

You should not share the same instance of a delegate between views. Doing so can cause incorrect or unintuitive editing behavior since each view connected to a given delegate may receive the ``[closeEditor()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate.closeEditor)  signal, and attempt to access, modify or close an editor that has already been closed.

See also

``[itemDelegate()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegate)

setItemDelegateForColumn (column , delegate )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setItemDelegateForColumn) Parameters :

- 

column  – int

- 

delegate  – ``[QAbstractItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate)

Sets the given item `delegate` used by this view and model for the given `column`. All items on `column` will be drawn and managed by `delegate` instead of using the default delegate (i.e., ``[itemDelegate()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegate)  ).

Any existing column delegate for `column` will be removed, but not deleted. ``[QAbstractItemView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView)  does not take ownership of `delegate`.

Note

If a delegate has been assigned to both a row and a column, the row delegate will take precedence and manage the intersecting cell index.

Warning

You should not share the same instance of a delegate between views. Doing so can cause incorrect or unintuitive editing behavior since each view connected to a given delegate may receive the ``[closeEditor()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate.closeEditor)  signal, and attempt to access, modify or close an editor that has already been closed.

See also

``[itemDelegateForColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegateForColumn)``[setItemDelegateForRow()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setItemDelegateForRow)``[itemDelegate()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegate)

setItemDelegateForRow (row , delegate )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setItemDelegateForRow) Parameters :

- 

row  – int

- 

delegate  – ``[QAbstractItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate)

Sets the given item `delegate` used by this view and model for the given `row`. All items on `row` will be drawn and managed by `delegate` instead of using the default delegate (i.e., ``[itemDelegate()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegate)  ).

Any existing row delegate for `row` will be removed, but not deleted. ``[QAbstractItemView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView)  does not take ownership of `delegate`.

Note

If a delegate has been assigned to both a row and a column, the row delegate (i.e., this delegate) will take precedence and manage the intersecting cell index.

Warning

You should not share the same instance of a delegate between views. Doing so can cause incorrect or unintuitive editing behavior since each view connected to a given delegate may receive the ``[closeEditor()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate.closeEditor)  signal, and attempt to access, modify or close an editor that has already been closed.

See also

``[itemDelegateForRow()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegateForRow)``[setItemDelegateForColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setItemDelegateForColumn)``[itemDelegate()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegate)

setKeyboardSearchFlags (searchFlags )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setKeyboardSearchFlags) Parameters :

searchFlags  – Combination of ``[MatchFlag](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.MatchFlag)

See also

``[keyboardSearchFlags()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id9)

Setter of property ``[keyboardSearchFlagsᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.keyboardSearchFlags)  .

setModel (model )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setModel) Parameters :

model  – ``[QAbstractItemModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel)

Warning

This section contains snippets that were automatically translated from C++ to Python and may contain errors.

Sets the `model` for the view to present.

This function will create and set a new selection model, replacing any model that was previously set with ``[setSelectionModel()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelectionModel)  . However, the old selection model will not be deleted as it may be shared between several views. We recommend that you delete the old selection model if it is no longer required. This is done with the following code:

> 

```
m = view.selectionModel()
view.setModel(model())
del m
```

If both the old model and the old selection model do not have parents, or if their parents are long-lived objects, it may be preferable to call their deleteLater() functions to explicitly delete them.

The view does not  take ownership of the model unless it is the model’s parent object because the model may be shared between many different views.

> 

See also

``[model()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.model)``[selectionModel()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionModel)``[setSelectionModel()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelectionModel)

setRootIndex (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setRootIndex) Parameters :

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Sets the root item to the item at the given `index`.

> 

See also

``[rootIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.rootIndex)

abstract setSelection (rect , command )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelection) Parameters :

- 

rect  – ``[QRect](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QRect.html#PySide6.QtCore.QRect)

- 

command  – Combination of ``[SelectionFlag](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.SelectionFlag)

Applies the selection `flags` to the items in or touched by the rectangle, `rect`.

When implementing your own itemview setSelection should call ``[selectionModel()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionModel)  ->select(selection, flags) where selection is either an empty QModelIndex or a QItemSelection that contains all items that are contained in `rect`.

> 

See also

``[selectionCommand()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionCommand)``[selectedIndexes()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectedIndexes)

setSelectionBehavior (behavior )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelectionBehavior) Parameters :

behavior  – ``[SelectionBehavior](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.SelectionBehavior)

See also

``[selectionBehavior()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id10)

Setter of property ``[selectionBehaviorᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionBehavior)  .

setSelectionMode (mode )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelectionMode) Parameters :

mode  – ``[SelectionMode](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.SelectionMode)

See also

``[selectionMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id11)

Setter of property ``[selectionModeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionMode)  .

setSelectionModel (selectionModel )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelectionModel) Parameters :

selectionModel  – ``[QItemSelectionModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel)

Sets the current selection model to the given `selectionModel`.

Note that, if you call ``[setModel()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setModel)  after this function, the given `selectionModel` will be replaced by one created by the view.

Note

It is up to the application to delete the old selection model if it is no longer needed; i.e., if it is not being used by other views. This will happen automatically when its parent object is deleted. However, if it does not have a parent, or if the parent is a long-lived object, it may be preferable to call its deleteLater() function to explicitly delete it.

See also

``[selectionModel()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionModel)``[setModel()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setModel)``[clearSelection()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.clearSelection)

setState (state )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setState) Parameters :

state  – ``[State](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.State)

Sets the item view’s state to the given `state`.

> 

See also

``[state()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.state)

setTabKeyNavigation (enable )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setTabKeyNavigation) Parameters :

enable  – bool

See also

``[tabKeyNavigation()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id13)

Setter of property ``[tabKeyNavigationᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.tabKeyNavigation)  .

setTextElideMode (mode )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setTextElideMode) Parameters :

mode  – ``[TextElideMode](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.TextElideMode)

See also

``[textElideMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id14)

Setter of property ``[textElideModeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.textElideMode)  .

setUpdateThreshold (threshold )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setUpdateThreshold) Parameters :

threshold  – int

See also

``[updateThreshold()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id15)

Setter of property ``[updateThresholdᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.updateThreshold)  .

setVerticalScrollMode (mode )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setVerticalScrollMode) Parameters :

mode  – ``[ScrollMode](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.ScrollMode)

See also

``[verticalScrollMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id16)

Setter of property ``[verticalScrollModeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.verticalScrollMode)  .

showDropIndicator ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id12) Return type :

bool

Getter of property ``[showDropIndicatorᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.showDropIndicator)  .

sizeHintForColumn (column )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.sizeHintForColumn) Parameters :

column  – int

Return type :

int

Returns the width size hint for the specified `column` or -1 if there is no model.

This function is used in views with a horizontal header to find the size hint for a header section based on the contents of the given `column`.

> 

See also

``[sizeHintForRow()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.sizeHintForRow)

sizeHintForIndex (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.sizeHintForIndex) Parameters :

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Return type :

``[QSize](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSize.html#PySide6.QtCore.QSize)

Returns the size hint for the item with the specified `index` or an invalid size for invalid indexes.

> 

See also

``[sizeHintForRow()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.sizeHintForRow)``[sizeHintForColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.sizeHintForColumn)

sizeHintForRow (row )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.sizeHintForRow) Parameters :

row  – int

Return type :

int

Returns the height size hint for the specified `row` or -1 if there is no model.

The returned height is calculated using the size hints of the given `row`'s items, i.e. the returned value is the maximum height among the items. Note that to control the height of a row, you must reimplement the ``[sizeHint()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate.sizeHint)  function.

This function is used in views with a vertical header to find the size hint for a header section based on the contents of the given `row`.

> 

See also

``[sizeHintForColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.sizeHintForColumn)

startAutoScroll ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.startAutoScroll) startDrag (supportedActions )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.startDrag) Parameters :

supportedActions  – Combination of ``[DropAction](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.DropAction)

Starts a drag by calling drag->exec() using the given `supportedActions`.

state ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.state) Return type :

``[State](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.State)

Returns the item view’s state.

> 

See also

``[setState()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setState)

stopAutoScroll ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.stopAutoScroll) tabKeyNavigation ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id13) Return type :

bool

See also

``[setTabKeyNavigation()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setTabKeyNavigation)

Getter of property ``[tabKeyNavigationᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.tabKeyNavigation)  .

textElideMode ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id14) Return type :

``[TextElideMode](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.TextElideMode)

See also

``[setTextElideMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setTextElideMode)

Getter of property ``[textElideModeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.textElideMode)  .

update (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.update) Parameters :

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Updates the area occupied by the given `index`.

updateEditorData ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.updateEditorData) updateEditorGeometries ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.updateEditorGeometries) updateGeometries ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.updateGeometries)

Updates the geometry of the child widgets of the view.

updateThreshold ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id15) Return type :

int

See also

``[setUpdateThreshold()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setUpdateThreshold)

Getter of property ``[updateThresholdᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.updateThreshold)  .

abstract verticalOffset ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.verticalOffset) Return type :

int

Returns the vertical offset of the view.

In the base class this is a pure virtual function.

> 

See also

``[horizontalOffset()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.horizontalOffset)

verticalScrollMode ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id16) Return type :

``[ScrollMode](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.ScrollMode)

See also

``[setVerticalScrollMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setVerticalScrollMode)

Getter of property ``[verticalScrollModeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.verticalScrollMode)  .

verticalScrollbarAction (action )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.verticalScrollbarAction) Parameters :

action  – int

verticalScrollbarValueChanged (value )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.verticalScrollbarValueChanged) Parameters :

value  – int

viewportEntered ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.viewportEntered)

This signal is emitted when the mouse cursor enters the viewport. Mouse tracking needs to be enabled for this feature to work.

> 

See also

``[entered()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.entered)

abstract visualRect (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.visualRect) Parameters :

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Return type :

``[QRect](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QRect.html#PySide6.QtCore.QRect)

Returns the rectangle on the viewport occupied by the item at `index`.

If your item is displayed in several areas then visualRect should return the primary area that contains index and not the complete area that index might encompasses, touch or cause drawing.

In the base class this is a pure virtual function.

> 

See also

``[indexAt()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.indexAt)``[visualRegionForSelection()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.visualRegionForSelection)

abstract visualRegionForSelection (selection )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.visualRegionForSelection) Parameters :

selection  – ``[QItemSelection](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelection.html#PySide6.QtCore.QItemSelection)

Return type :

``[QRegion](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QRegion.html#PySide6.QtGui.QRegion)

Returns the region from the viewport of the items in the given `selection`.

In the base class this is a pure virtual function.

> 

See also

``[visualRect()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.visualRect)``[selectedIndexes()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectedIndexes)
