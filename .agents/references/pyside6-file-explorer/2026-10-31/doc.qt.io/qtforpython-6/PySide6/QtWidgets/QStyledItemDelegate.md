<!--
source: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html
retrieved: 2026-10-31T21:18:29.330097+00:00
final_url: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html
content_type: text/html
-->

# PySide6.QtWidgets.QStyledItemDelegate - Qt for Python

[Skip to content](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#furo-main-content)

[Qt for Python](https://doc.qt.io/qtforpython-6/index.html)

[Back to top](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html)

# PySide6.QtWidgets.QStyledItemDelegate[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#pyside6-qtwidgets-qstyleditemdelegate)

class QStyledItemDelegate[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)

The ``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)  class provides display and editing facilities for data items from a model. [More](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#more) …

Inheritance diagram of PySide6.QtWidgets.QStyledItemDelegate

## Synopsis[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#synopsis)

### Methods[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#methods)

- 

def ``[__init__()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate.__init__)

- 

def ``[itemEditorFactory()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate.itemEditorFactory)

- 

def ``[setItemEditorFactory()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate.setItemEditorFactory)

### Virtual methods[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#virtual-methods)

- 

def ``[displayText()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate.displayText)

- 

def ``[initStyleOption()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate.initStyleOption)

Note

This documentation may contain snippets that were automatically translated from C++ to Python. We always welcome contributions to the snippet translation. If you see an issue with the translation, you can also let us know by creating a ticket on [https:/bugreports.qt.io/projects/PYSIDE](https://doc.qt.io/bugreports.qt.io/projects/PYSIDE)

## Detailed Description[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#detailed-description)

Warning

This section contains snippets that were automatically translated from C++ to Python and may contain errors.

When displaying data from models in Qt item views, e.g., a ``[QTableView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableView.html#PySide6.QtWidgets.QTableView)  , the individual items are drawn by a delegate. Also, when an item is edited, it provides an editor widget, which is placed on top of the item view while editing takes place. ``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)  is the default delegate for all Qt item views, and is installed upon them when they are created.

The ``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)  class is one of the [Model/View Classes](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  and is part of Qt’s [model/view framework](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  . The delegate allows the display and editing of items to be developed independently from the model and view.

The data of items in models are assigned an ItemDataRole; each item can store a QVariant for each role. ``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)  implements display and editing for the most common datatypes expected by users, including booleans, integers, and strings.

The data will be drawn differently depending on which role they have in the model. The following table describes the roles and the data types the delegate can handle for each of them. It is often sufficient to ensure that the model returns appropriate data for each of the roles to determine the appearance of items in views.

> 

Role

Accepted Types

Qt::BackgroundRole

QBrush

Qt::CheckStateRole

Qt::CheckState

Qt::DecorationRole

QIcon, QPixmap, QImage and QColor

Qt::DisplayRole

QString and types with a string representation

Qt::EditRole

See ``[QItemEditorFactory](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QItemEditorFactory.html#PySide6.QtWidgets.QItemEditorFactory)  for details

Qt::FontRole

QFont

Qt::SizeHintRole

QSize

Qt::TextAlignmentRole

Qt::Alignment

Qt::ForegroundRole

QBrush

Editors are created with a ``[QItemEditorFactory](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QItemEditorFactory.html#PySide6.QtWidgets.QItemEditorFactory)  ; a default static instance provided by ``[QItemEditorFactory](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QItemEditorFactory.html#PySide6.QtWidgets.QItemEditorFactory)  is installed on all item delegates. You can set a custom factory using ``[setItemEditorFactory()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate.setItemEditorFactory)  or set a new default factory with ``[setDefaultFactory()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QItemEditorFactory.html#PySide6.QtWidgets.QItemEditorFactory.setDefaultFactory)  .

> 

```
//! [2]
    editorFactory = QItemEditorFactory()
    creator = QStandardItemEditorCreator()<MyFancyDateTimeEdit>()
    editorFactory.registerEditor(QMetaType.QDateTime, creator)
//! [2]
    QItemEditorFactory.setDefaultFactory(editorFactory)
```

After the new factory has been set, all standard item delegates will use it (i.e, also delegates that were created before the new default factory was set).

It is the data stored in the item model with the EditRole that is edited. See the ``[QItemEditorFactory](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QItemEditorFactory.html#PySide6.QtWidgets.QItemEditorFactory)  class for a more high-level introduction to item editor factories.

> 

### Subclassing QStyledItemDelegate[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#subclassing-qstyleditemdelegate)

If the delegate does not support painting of the data types you need or you want to customize the drawing of items, you need to subclass ``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)  , and reimplement `paint()` and possibly `sizeHint()` . The `paint()` function is called individually for each item, and with `sizeHint()` , you can specify the hint for each of them.

When reimplementing `paint()` , one would typically handle the datatypes one would like to draw and use the superclass implementation for other types.

The painting of check box indicators are performed by the current style. The style also specifies the size and the bounding rectangles in which to draw the data for the different data roles. The bounding rectangle of the item itself is also calculated by the style. When drawing already supported datatypes, it is therefore a good idea to ask the style for these bounding rectangles. The ``[QStyle](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyle.html#PySide6.QtWidgets.QStyle)  class description describes this in more detail.

If you wish to change any of the bounding rectangles calculated by the style or the painting of check box indicators, you can subclass ``[QStyle](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyle.html#PySide6.QtWidgets.QStyle)  . Note, however, that the size of the items can also be affected by reimplementing `sizeHint()` .

It is possible for a custom delegate to provide editors without the use of an editor item factory. In this case, the following virtual functions must be reimplemented:

> 

- 

`createEditor()` returns the widget used to change data from the model and can be reimplemented to customize editing behavior.

- 

`setEditorData()` provides the widget with data to manipulate.

- 

`updateEditorGeometry()` ensures that the editor is displayed correctly with respect to the item view.

- 

`setModelData()` returns updated data to the model.

The Star Delegate  example creates editors by reimplementing these methods.

> 

### QStyledItemDelegate vs. QItemDelegate[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#qstyleditemdelegate-vs-qitemdelegate)

Since Qt 4.4, there are two delegate classes: ``[QItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QItemDelegate.html#PySide6.QtWidgets.QItemDelegate)  and ``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)  . However, the default delegate is ``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)  . These two classes are independent alternatives to painting and providing editors for items in views. The difference between them is that ``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)  uses the current style to paint its items. We therefore recommend using ``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)  as the base class when implementing custom delegates or when working with Qt style sheets. The code required for either class should be equal unless the custom delegate needs to use the style for drawing.

If you wish to customize the painting of item views, you should implement a custom style. Please see the ``[QStyle](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyle.html#PySide6.QtWidgets.QStyle)  class documentation for details.

> 

See also

[Delegate Classes](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)``[QItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QItemDelegate.html#PySide6.QtWidgets.QItemDelegate)``[QAbstractItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate)``[QStyle](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyle.html#PySide6.QtWidgets.QStyle) Star-Delegate-Example

__init__ ([parent=None ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate.__init__) Parameters :

parent  – ``[QObject](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QObject.html#PySide6.QtCore.QObject)

Constructs an item delegate with the given `parent`.

displayText (value , locale )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate.displayText) Parameters :

- 

value  – object

- 

locale  – ``[QLocale](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QLocale.html#PySide6.QtCore.QLocale)

Return type :

str

This function returns the string that the delegate will use to display the Qt::DisplayRole of the model in `locale`. `value` is the value of the Qt::DisplayRole provided by the model.

The default implementation uses the QLocale::toString to convert `value` into a QString.

This function is not called for empty model indices, i.e., indices for which the model returns an invalid QVariant.

> 

See also

``[data()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel.data)

initStyleOption (option , index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate.initStyleOption) Parameters :

- 

option  – ``[QStyleOptionViewItem](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyleOptionViewItem.html#PySide6.QtWidgets.QStyleOptionViewItem)

- 

index  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Initialize `option` with the values using the index `index`. This method is useful for subclasses when they need a ``[QStyleOptionViewItem](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyleOptionViewItem.html#PySide6.QtWidgets.QStyleOptionViewItem)  , but don’t want to fill in all the information themselves.

> 

See also

``[initFrom()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyleOption.html#PySide6.QtWidgets.QStyleOption.initFrom)

itemEditorFactory ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate.itemEditorFactory) Return type :

``[QItemEditorFactory](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QItemEditorFactory.html#PySide6.QtWidgets.QItemEditorFactory)

Returns the editor factory used by the item delegate. If no editor factory is set, the function will return null.

> 

See also

``[setItemEditorFactory()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate.setItemEditorFactory)

setItemEditorFactory (factory )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate.setItemEditorFactory) Parameters :

factory  – ``[QItemEditorFactory](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QItemEditorFactory.html#PySide6.QtWidgets.QItemEditorFactory)

Sets the editor factory to be used by the item delegate to be the `factory` specified. If no editor factory is set, the item delegate will use the default editor factory.

> 

See also

``[itemEditorFactory()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate.itemEditorFactory)
