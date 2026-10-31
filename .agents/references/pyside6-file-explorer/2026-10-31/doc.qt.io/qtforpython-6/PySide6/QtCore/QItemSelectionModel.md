<!--
source: https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html
retrieved: 2026-10-31T21:18:28.194310+00:00
final_url: https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html
content_type: text/html
-->

# PySide6.QtCore.QItemSelectionModel - Qt for Python

[Skip to content](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#furo-main-content)

[Qt for Python](https://doc.qt.io/qtforpython-6/index.html)

[Back to top](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html)

# PySide6.QtCore.QItemSelectionModel[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#pyside6-qtcore-qitemselectionmodel)

class QItemSelectionModel[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel)

The ``[QItemSelectionModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel)  class keeps track of a view’s selected items.

Details

A ``[QItemSelectionModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel)  keeps track of the selected items in a view, or in several views onto the same model. It also keeps track of the currently selected item in a view.

The ``[QItemSelectionModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel)  class is one of the Model/View Classes and is part of Qt’s model/view framework.

The selected items are stored using ranges. Whenever you want to modify the selected items use ``[select()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.select)  and provide either a ``[QItemSelection](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelection.html#PySide6.QtCore.QItemSelection)  , or a ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)  and a ``[SelectionFlag](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.SelectionFlag)  .

The ``[QItemSelectionModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel)  takes a two layer approach to selection management, dealing with both selected items that have been committed and items that are part of the current selection. The current selected items are part of the current interactive selection (for example with rubber-band selection or keyboard-shift selections).

To update the currently selected items, use the bitwise OR of ``[Current](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.SelectionFlag)  and any of the other `SelectionFlags` . If you omit the ``[Current](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.SelectionFlag)  command, a new current selection will be created, and the previous one added to the whole selection. All functions operate on both layers; for example, selecteditems() will return items from both layers.

Note

Since 5.5, ``[model()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id2)  , ``[hasSelection()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id1)  , and ``[currentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id0)  are meta-object properties.

See also

``[QAbstractItemModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel)

Inheritance diagram of PySide6.QtCore.QItemSelectionModel

## Synopsis[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#synopsis)

### Properties[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#properties)

- 

``[currentIndexᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.currentIndex)

- 

``[hasSelectionᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.hasSelection)

- 

``[modelᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.model)

- 

``[selectedIndexesᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selectedIndexes)

- 

``[selectionᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selection)

### Methods[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#methods)

- 

def ``[__init__()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.__init__)

- 

def ``[columnIntersectsSelection()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.columnIntersectsSelection)

- 

def ``[currentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id0)

- 

def ``[emitSelectionChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.emitSelectionChanged)

- 

def ``[hasSelection()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id1)

- 

def ``[isColumnSelected()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.isColumnSelected)

- 

def ``[isRowSelected()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.isRowSelected)

- 

def ``[isSelected()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.isSelected)

- 

def ``[model()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id2)

- 

def ``[rowIntersectsSelection()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.rowIntersectsSelection)

- 

def ``[selectedColumns()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selectedColumns)

- 

def ``[selectedIndexes()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id3)

- 

def ``[selectedRows()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selectedRows)

- 

def ``[selection()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id4)

- 

def ``[setModel()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.setModel)

### Virtual methods[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#virtual-methods)

- 

def ``[clear()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.clear)

- 

def ``[clearCurrentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.clearCurrentIndex)

- 

def ``[reset()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.reset)

- 

def ``[select()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.select)

- 

def ``[setCurrentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.setCurrentIndex)

### Slots[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#slots)

- 

def ``[clearSelection()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.clearSelection)

### Signals[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#signals)

- 

def ``[currentChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.currentChanged)

- 

def ``[currentColumnChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.currentColumnChanged)

- 

def ``[currentRowChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.currentRowChanged)

- 

def ``[modelChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.modelChanged)

- 

def ``[selectionChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selectionChanged)

Note

This documentation may contain snippets that were automatically translated from C++ to Python. We always welcome contributions to the snippet translation. If you see an issue with the translation, you can also let us know by creating a ticket on [https:/bugreports.qt.io/projects/PYSIDE](https://doc.qt.io/bugreports.qt.io/projects/PYSIDE)

class SelectionFlag[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.SelectionFlag)

(inherits `enum.Flag`) This enum describes the way the selection model will be updated.

> 

Constant

Description

QItemSelectionModel.SelectionFlag.NoUpdate

No selection will be made.

QItemSelectionModel.SelectionFlag.Clear

The complete selection will be cleared.

QItemSelectionModel.SelectionFlag.Select

All specified indexes will be selected.

QItemSelectionModel.SelectionFlag.Deselect

All specified indexes will be deselected.

QItemSelectionModel.SelectionFlag.Toggle

All specified indexes will be selected or deselected depending on their current state.

QItemSelectionModel.SelectionFlag.Current

The current selection will be updated.

QItemSelectionModel.SelectionFlag.Rows

All indexes will be expanded to span rows.

QItemSelectionModel.SelectionFlag.Columns

All indexes will be expanded to span columns.

QItemSelectionModel.SelectionFlag.SelectCurrent

A combination of Select and Current, provided for convenience.

QItemSelectionModel.SelectionFlag.ToggleCurrent

A combination of Toggle and Current, provided for convenience.

QItemSelectionModel.SelectionFlag.ClearAndSelect

A combination of Clear and Select, provided for convenience.

Note

Properties can be used directly when `from __feature__ import true_property` is used or via accessor functions otherwise.

property currentIndexᅟ :[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.currentIndex) Access functions:

- 

``[currentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id0)

- 

Signal ``[currentChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.currentChanged)

property hasSelectionᅟ : bool[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.hasSelection) Access functions:

- 

``[hasSelection()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id1)

- 

Signal ``[selectionChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selectionChanged)

property modelᅟ :[QAbstractItemModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel)[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.model) Access functions:

- 

``[model()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id2)

- 

``[setModel()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.setModel)

- 

Signal ``[modelChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.modelChanged)

property selectedIndexesᅟ : list of QModelIndex[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selectedIndexes) Access functions:

- 

``[selectedIndexes()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id3)

- 

Signal ``[selectionChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selectionChanged)

property selectionᅟ :[QItemSelection](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelection.html#PySide6.QtCore.QItemSelection)[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selection) Access functions:

- 

``[selection()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id4)

- 

Signal ``[selectionChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selectionChanged)

__init__ ([model=None ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.__init__) Parameters :

model  – ``[QAbstractItemModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel)

Constructs a selection model that operates on the specified item `model`.

__init__ (model , parent ) Parameters :

- 

model  – ``[QAbstractItemModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel)

- 

parent  – ``[QObject](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QObject.html#PySide6.QtCore.QObject)

Constructs a selection model that operates on the specified item `model` with `parent`.

clear ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.clear)

Clears the selection model. Emits ``[selectionChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selectionChanged)  and ``[currentChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.currentChanged)  .

clearCurrentIndex ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.clearCurrentIndex)

Clears the current index. Emits ``[currentChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.currentChanged)  .

clearSelection ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.clearSelection)

Clears the selection in the selection model. Emits ``[selectionChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selectionChanged)  .

columnIntersectsSelection (column [, parent=QModelIndex() ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.columnIntersectsSelection) Parameters :

- 

column  – int

- 

parent  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Return type :

bool

Returns `true` if there are any items selected in the `column` with the given `parent`.

Note

Since Qt 5.15, the default argument for `parent` is an empty model index.

currentChanged (current , previous )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.currentChanged) Parameters :

- 

current  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

- 

previous  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

This signal is emitted whenever the current item changes. The `previous` model item index is replaced by the `current` index as the selection’s current item.

Note that this signal will not be emitted when the item model is reset.

> 

See also

``[currentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id0)``[setCurrentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.setCurrentIndex)``[selectionChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selectionChanged)

Notification signal of property ``[currentIndexᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.currentIndex)  .

currentColumnChanged (current , previous )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.currentColumnChanged) Parameters :

- 

current  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

- 

previous  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

This signal is emitted if the `current` item changes and its column is different to the column of the `previous` current item.

Note that this signal will not be emitted when the item model is reset.

> 

See also

``[currentChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.currentChanged)``[currentRowChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.currentRowChanged)``[currentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id0)``[setCurrentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.setCurrentIndex)

currentIndex ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id0) Return type :

``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Returns the model item index for the current item, or an invalid index if there is no current item.

> 

See also

``[setCurrentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.setCurrentIndex)

Getter of property ``[currentIndexᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.currentIndex)  .

currentRowChanged (current , previous )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.currentRowChanged) Parameters :

- 

current  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

- 

previous  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

This signal is emitted if the `current` item changes and its row is different to the row of the `previous` current item.

Note that this signal will not be emitted when the item model is reset.

> 

See also

``[currentChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.currentChanged)``[currentColumnChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.currentColumnChanged)``[currentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id0)``[setCurrentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.setCurrentIndex)

emitSelectionChanged (newSelection , oldSelection )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.emitSelectionChanged) Parameters :

- 

newSelection  – ``[QItemSelection](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelection.html#PySide6.QtCore.QItemSelection)

- 

oldSelection  – ``[QItemSelection](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelection.html#PySide6.QtCore.QItemSelection)

Compares the two selections `newSelection` and `oldSelection` and emits ``[selectionChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selectionChanged)  with the deselected and selected items.

hasSelection ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id1) Return type :

bool

Returns `true` if the selection model contains any selected item, otherwise returns `false`.

Getter of property ``[hasSelectionᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.hasSelection)  .

isColumnSelected (column [, parent=QModelIndex() ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.isColumnSelected) Parameters :

- 

column  – int

- 

parent  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Return type :

bool

Returns `true` if all items are selected in the `column` with the given `parent`.

Note that this function is usually faster than calling ``[isSelected()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.isSelected)  on all items in the same column and that unselectable items are ignored.

Note

Since Qt 5.15, the default argument for `parent` is an empty model index.

isRowSelected (row [, parent=QModelIndex() ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.isRowSelected) Parameters :

- 

row  – int

- 

parent  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Return type :

bool

Returns `true` if all items are selected in the `row` with the given `parent`.

Note that this function is usually faster than calling ``[isSelected()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.isSelected)  on all items in the same row and that unselectable items are ignored.

Note

Since Qt 5.15, the default argument for `parent` is an empty model index.

isSelected (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.isSelected) Parameters :

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Return type :

bool

Returns `true` if the given model item `index` is selected.

model ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id2) Return type :

``[QAbstractItemModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel)

Returns the item model operated on by the selection model.

Getter of property ``[modelᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.model)  .

modelChanged (model )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.modelChanged) Parameters :

model  – ``[QAbstractItemModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel)

This signal is emitted when the `model` is successfully set with ``[setModel()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.setModel)  .

> 

See also

``[model()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id2)``[setModel()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.setModel)

Notification signal of property ``[modelᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.model)  .

reset ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.reset)

Clears the selection model. Does not emit any signals.

rowIntersectsSelection (row [, parent=QModelIndex() ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.rowIntersectsSelection) Parameters :

- 

row  – int

- 

parent  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Return type :

bool

Returns `true` if there are any items selected in the `row` with the given `parent`.

Note

Since Qt 5.15, the default argument for `parent` is an empty model index.

select (selection , command )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.select) Parameters :

- 

selection  – ``[QItemSelection](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelection.html#PySide6.QtCore.QItemSelection)

- 

command  – Combination of ``[SelectionFlag](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.SelectionFlag)

Selects the item `selection` using the specified `command`, and emits ``[selectionChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selectionChanged)  .

> 

See also

``[SelectionFlag](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.SelectionFlag)

select (index , command ) Parameters :

- 

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

- 

command  – Combination of ``[SelectionFlag](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.SelectionFlag)

Selects the model item `index` using the specified `command`, and emits ``[selectionChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selectionChanged)  .

> 

See also

`SelectionFlags`

selectedColumns ([row=0 ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selectedColumns) Parameters :

row  – int

Return type :

.list of [QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Returns the indexes in the given `row` for columns where all rows are selected.

> 

See also

``[selectedIndexes()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id3)``[selectedRows()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selectedRows)

selectedIndexes ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id3) Return type :

.list of [QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Returns a list of all selected model item indexes. The list contains no duplicates, and is not sorted.

Getter of property ``[selectedIndexesᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selectedIndexes)  .

selectedRows ([column=0 ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selectedRows) Parameters :

column  – int

Return type :

.list of [QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Returns the indexes in the given `column` for the rows where all columns are selected.

> 

See also

``[selectedIndexes()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id3)``[selectedColumns()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selectedColumns)

selection ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id4) Return type :

``[QItemSelection](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelection.html#PySide6.QtCore.QItemSelection)

Returns the selection ranges stored in the selection model.

Getter of property ``[selectionᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selection)  .

selectionChanged (selected , deselected )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.selectionChanged) Parameters :

- 

selected  – ``[QItemSelection](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelection.html#PySide6.QtCore.QItemSelection)

- 

deselected  – ``[QItemSelection](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelection.html#PySide6.QtCore.QItemSelection)

This signal is emitted whenever the selection changes. The change in the selection is represented as an item selection of `deselected` items and an item selection of `selected` items.

Note the that the current index changes independently from the selection. Also note that this signal will not be emitted when the item model is reset.

Items which stay selected but change their index are not included in `selected` and `deselected`. Thus, this signal might be emitted with both `selected` and `deselected` empty, if only the indices of selected items change.

Note

It is not permitted to modify the model (e.g., by calling setData()) from within a slot connected directly to this signal. This signal may be emitted while the model is in the process of being modified, for example during row or column removal, or a model reset. Attempting to perform additional changes at such times can lead to undefined behavior. In particular, nested modifications can corrupt internal state, such as the mapping structures maintained by ``[QSortFilterProxyModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel)  .

See also

``[select()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.select)``[currentChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.currentChanged)

Notification signal of property ``[hasSelectionᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.hasSelection)  .

setCurrentIndex (index , command )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.setCurrentIndex) Parameters :

- 

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

- 

command  – Combination of ``[SelectionFlag](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.SelectionFlag)

Sets the model item `index` to be the current item, and emits ``[currentChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.currentChanged)  . The current item is used for keyboard navigation and focus indication; it is independent of any selected items, although a selected item can also be the current item.

Depending on the specified `command`, the `index` can also become part of the current selection.

> 

See also

``[currentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id0)``[select()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.select)

setModel (model )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.setModel) Parameters :

model  – ``[QAbstractItemModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel)

Sets the model to `model`. The ``[modelChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.modelChanged)  signal will be emitted.

> 

See also

``[model()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#id2)``[modelChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.modelChanged)

Setter of property ``[modelᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel.model)  .
