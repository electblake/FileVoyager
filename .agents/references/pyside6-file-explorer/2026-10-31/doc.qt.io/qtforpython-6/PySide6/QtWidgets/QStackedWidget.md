<!--
source: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html
retrieved: 2026-10-31T21:18:35.113174+00:00
final_url: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html
content_type: text/html
-->

# PySide6.QtWidgets.QStackedWidget - Qt for Python

[Skip to content](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#furo-main-content)

[Qt for Python](https://doc.qt.io/qtforpython-6/index.html)

[Back to top](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html)

# PySide6.QtWidgets.QStackedWidget[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#pyside6-qtwidgets-qstackedwidget)

class QStackedWidget[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget)

The ``[QStackedWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget)  class provides a stack of widgets where only one widget is visible at a time.

Details

Warning

This section contains snippets that were automatically translated from C++ to Python and may contain errors.

``[QStackedWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget)  can be used to create a user interface similar to the one provided by ``[QTabWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTabWidget.html#PySide6.QtWidgets.QTabWidget)  . It is a convenience layout widget built on top of the ``[QStackedLayout](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedLayout.html#PySide6.QtWidgets.QStackedLayout)  class.

Like ``[QStackedLayout](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedLayout.html#PySide6.QtWidgets.QStackedLayout)  , ``[QStackedWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget)  can be constructed and populated with a number of child widgets (“pages”):

> 

```
firstPageWidget = QWidget()
secondPageWidget = QWidget()
thirdPageWidget = QWidget()
stackedWidget = QStackedWidget()
stackedWidget.addWidget(firstPageWidget)
stackedWidget.addWidget(secondPageWidget)
stackedWidget.addWidget(thirdPageWidget)
layout = QVBoxLayout()
layout.addWidget(stackedWidget)
setLayout(layout)
```

``[QStackedWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget)  provides no intrinsic means for the user to switch page. This is typically done through a ``[QComboBox](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QComboBox.html#PySide6.QtWidgets.QComboBox)  or a ``[QListWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListWidget.html#PySide6.QtWidgets.QListWidget)  that stores the titles of the ``[QStackedWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget)  ‘s pages. For example:

> 

```
pageComboBox = QComboBox()
pageComboBox.addItem(tr("Page 1"))
pageComboBox.addItem(tr("Page 2"))
pageComboBox.addItem(tr("Page 3"))
pageComboBox.activated.connect(
        stackedWidget.setCurrentIndex)
```

When populating a stacked widget, the widgets are added to an internal list. The ``[indexOf()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.indexOf)  function returns the index of a widget in that list. The widgets can either be added to the end of the list using the ``[addWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.addWidget)  function, or inserted at a given index using the ``[insertWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.insertWidget)  function. The ``[removeWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.removeWidget)  function removes a widget from the stacked widget. The number of widgets contained in the stacked widget can be obtained using the ``[count()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#id0)  function.

The ``[widget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.widget)  function returns the widget at a given index position. The index of the widget that is shown on screen is given by ``[currentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#id1)  and can be changed using ``[setCurrentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.setCurrentIndex)  . In a similar manner, the currently shown widget can be retrieved using the ``[currentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.currentWidget)  function, and altered using the ``[setCurrentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.setCurrentWidget)  function.

Whenever the current widget in the stacked widget changes or a widget is removed from the stacked widget, the ``[currentChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.currentChanged)  and ``[widgetRemoved()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.widgetRemoved)  signals are emitted respectively.

> 

See also

``[QStackedLayout](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedLayout.html#PySide6.QtWidgets.QStackedLayout)``[QTabWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTabWidget.html#PySide6.QtWidgets.QTabWidget)

Inheritance diagram of PySide6.QtWidgets.QStackedWidget

## Synopsis[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#synopsis)

### Properties[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#properties)

- 

``[countᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.count)  - The number of widgets contained by this stacked widget

- 

``[currentIndexᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.currentIndex)  - The index position of the widget that is visible

### Methods[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#methods)

- 

def ``[__init__()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.__init__)

- 

def ``[addWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.addWidget)

- 

def ``[count()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#id0)

- 

def ``[currentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#id1)

- 

def ``[currentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.currentWidget)

- 

def ``[indexOf()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.indexOf)

- 

def ``[insertWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.insertWidget)

- 

def ``[removeWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.removeWidget)

- 

def ``[widget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.widget)

### Slots[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#slots)

- 

def ``[setCurrentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.setCurrentIndex)

- 

def ``[setCurrentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.setCurrentWidget)

### Signals[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#signals)

- 

def ``[currentChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.currentChanged)

- 

def ``[widgetAdded()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.widgetAdded)

- 

def ``[widgetRemoved()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.widgetRemoved)

Note

This documentation may contain snippets that were automatically translated from C++ to Python. We always welcome contributions to the snippet translation. If you see an issue with the translation, you can also let us know by creating a ticket on [https:/bugreports.qt.io/projects/PYSIDE](https://doc.qt.io/bugreports.qt.io/projects/PYSIDE)

Note

Properties can be used directly when `from __feature__ import true_property` is used or via accessor functions otherwise.

property countᅟ : int[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.count)

This property holds the number of widgets contained by this stacked widget.

By default, this property contains a value of 0.

> 

See also

``[currentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#id1)``[widget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.widget)

Access functions:

- 

``[count()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#id0)

property currentIndexᅟ : int[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.currentIndex)

This property holds the index position of the widget that is visible.

The current index is -1 if there is no current widget.

By default, this property contains a value of -1 because the stack is initially empty.

> 

See also

``[currentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.currentWidget)``[indexOf()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.indexOf)

Access functions:

- 

``[currentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#id1)

- 

``[setCurrentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.setCurrentIndex)

- 

Signal ``[currentChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.currentChanged)

__init__ ([parent=None ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.__init__) Parameters :

parent  – ``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

Constructs a ``[QStackedWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget)  with the given `parent`.

> 

See also

``[addWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.addWidget)``[insertWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.insertWidget)

addWidget (w )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.addWidget) Parameters :

w  – ``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

Return type :

int

Appends the given `widget` to the ``[QStackedWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget)  and returns the index position. Ownership of `widget` is passed on to the ``[QStackedWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget)  .

If the ``[QStackedWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget)  is empty before this function is called, `widget` becomes the current widget.

> 

See also

``[insertWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.insertWidget)``[removeWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.removeWidget)``[setCurrentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.setCurrentWidget)

count ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#id0) Return type :

int

Getter of property ``[countᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.count)  .

currentChanged (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.currentChanged) Parameters :

index  – int

This signal is emitted whenever the current widget changes.

The parameter holds the `index` of the new current widget, or -1 if there isn’t a new one (for example, if there are no widgets in the ``[QStackedWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget)  ).

> 

See also

``[currentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.currentWidget)``[setCurrentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.setCurrentWidget)

Notification signal of property ``[currentIndexᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.currentIndex)  .

currentIndex ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#id1) Return type :

int

See also

``[setCurrentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.setCurrentIndex)

Getter of property ``[currentIndexᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.currentIndex)  .

currentWidget ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.currentWidget) Return type :

``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

Returns the current widget, or `None` if there are no child widgets.

> 

See also

``[currentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#id1)``[setCurrentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.setCurrentWidget)

indexOf (widget )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.indexOf) Parameters :

widget  – ``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

Return type :

int

Returns the index of the given `widget`, or -1 if the given `widget` is not a child of the ``[QStackedWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget)  .

> 

See also

``[currentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#id1)``[widget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.widget)

insertWidget (index , w )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.insertWidget) Parameters :

- 

index  – int

- 

w  – ``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

Return type :

int

Inserts the given `widget` at the given `index` in the ``[QStackedWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget)  . Ownership of `widget` is passed on to the ``[QStackedWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget)  . If `index` is out of range, the `widget` is appended (in which case it is the actual index of the `widget` that is returned).

If the ``[QStackedWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget)  was empty before this function is called, the given `widget` becomes the current widget.

Inserting a new widget at an index less than or equal to the current index will increment the current index, but keep the current widget.

> 

See also

``[addWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.addWidget)``[removeWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.removeWidget)``[setCurrentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.setCurrentWidget)

removeWidget (w )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.removeWidget) Parameters :

w  – ``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

Removes `widget` from the ``[QStackedWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget)  . i.e., `widget` is not  deleted but simply removed from the stacked layout, causing it to be hidden.

Note

Parent object and parent widget of `widget` will remain the ``[QStackedWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget)  . If the application wants to reuse the removed `widget`, then it is recommended to re-parent it.

See also

``[addWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.addWidget)``[insertWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.insertWidget)``[currentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.currentWidget)

setCurrentIndex (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.setCurrentIndex) Parameters :

index  – int

See also

``[currentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#id1)

Setter of property ``[currentIndexᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.currentIndex)  .

setCurrentWidget (w )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.setCurrentWidget) Parameters :

w  – ``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

Sets the current widget to be the specified `widget`. The new current widget must already be contained in this stacked widget.

> 

See also

``[currentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.currentWidget)``[setCurrentIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.setCurrentIndex)

widget (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.widget) Parameters :

index  – int

Return type :

``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

Returns the widget at the given `index`, or `None` if there is no such widget.

> 

See also

``[currentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.currentWidget)``[indexOf()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.indexOf)

widgetAdded (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.widgetAdded) Parameters :

index  – int

This signal is emitted whenever a widget is added or inserted. The widget’s `index` is passed as parameter.

> 

See also

``[addWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.addWidget)``[insertWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.insertWidget)

widgetRemoved (index )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.widgetRemoved) Parameters :

index  – int

This signal is emitted whenever a widget is removed. The widget’s `index` is passed as parameter.

> 

See also

``[removeWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStackedWidget.html#PySide6.QtWidgets.QStackedWidget.removeWidget)
