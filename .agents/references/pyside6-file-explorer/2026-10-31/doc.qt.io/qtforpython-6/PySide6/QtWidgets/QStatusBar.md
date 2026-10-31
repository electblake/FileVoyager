<!--
source: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html
retrieved: 2026-10-31T21:18:40.626342+00:00
final_url: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html
content_type: text/html
-->

# PySide6.QtWidgets.QStatusBar - Qt for Python

[Skip to content](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#furo-main-content)

[Qt for Python](https://doc.qt.io/qtforpython-6/index.html)

[Back to top](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html)

# PySide6.QtWidgets.QStatusBar[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#pyside6-qtwidgets-qstatusbar)

class QStatusBar[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar)

The ``[QStatusBar](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar)  class provides a horizontal bar suitable for presenting status information.

Details

Warning

This section contains snippets that were automatically translated from C++ to Python and may contain errors.

Each status indicator falls into one of three categories:

> 

- 

Temporary  - briefly occupies most of the status bar. Used to explain tool tip texts or menu entries, for example.

- 

Normal  - occupies part of the status bar and may be hidden by temporary messages. Used to display the page and line number in a word processor, for example.

- 

Permanent  - is never hidden. Used for important mode indications, for example, some applications put a Caps Lock indicator in the status bar.

``[QStatusBar](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar)  lets you display all three types of indicators.

Typically, a request for the status bar functionality occurs in relation to a ``[QMainWindow](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMainWindow.html#PySide6.QtWidgets.QMainWindow)  object. ``[QMainWindow](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMainWindow.html#PySide6.QtWidgets.QMainWindow)  provides a main application window, with a menu bar, tool bars, dock widgets and  a status bar around a large central widget. The status bar can be retrieved using the ``[statusBar()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMainWindow.html#PySide6.QtWidgets.QMainWindow.statusBar)  function, and replaced using the ``[setStatusBar()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMainWindow.html#PySide6.QtWidgets.QMainWindow.setStatusBar)  function.

Use the ``[showMessage()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.showMessage)  slot to display a temporary  message:

> 

```
statusBar().showMessage(tr("Ready"))
```

To remove a temporary message, use the ``[clearMessage()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.clearMessage)  slot, or set a time limit when calling ``[showMessage()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.showMessage)  . For example:

> 

```
statusBar().showMessage(tr("Ready"), 2000)
```

Use the ``[currentMessage()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.currentMessage)  function to retrieve the temporary message currently shown. The ``[QStatusBar](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar)  class also provide the ``[messageChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.messageChanged)  signal which is emitted whenever the temporary status message changes.

Normal  and Permanent  messages are displayed by creating a small widget ( ``[QLabel](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QLabel.html#PySide6.QtWidgets.QLabel)  , ``[QProgressBar](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QProgressBar.html#PySide6.QtWidgets.QProgressBar)  or even ``[QToolButton](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolButton.html#PySide6.QtWidgets.QToolButton)  ) and then adding it to the status bar using the ``[addWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.addWidget)  or the ``[addPermanentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.addPermanentWidget)  function. Use the ``[removeWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.removeWidget)  function to remove such messages from the status bar.

> 

```
statusBar().addWidget(MyReadWriteIndication())
```

By default ``[QStatusBar](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar)  provides a ``[QSizeGrip](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QSizeGrip.html#PySide6.QtWidgets.QSizeGrip)  in the lower-right corner. You can disable it using the ``[setSizeGripEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.setSizeGripEnabled)  function. Use the ``[isSizeGripEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.isSizeGripEnabled)  function to determine the current status of the size grip.

> 

See also

``[QMainWindow](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMainWindow.html#PySide6.QtWidgets.QMainWindow)``[QStatusTipEvent](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QStatusTipEvent.html#PySide6.QtGui.QStatusTipEvent)

Inheritance diagram of PySide6.QtWidgets.QStatusBar

## Synopsis[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#synopsis)

### Properties[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#properties)

- 

``[sizeGripEnabledᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.sizeGripEnabled)  - Whether the QSizeGrip in the bottom-right corner of the status bar is enabled

### Methods[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#methods)

- 

def ``[__init__()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.__init__)

- 

def ``[addPermanentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.addPermanentWidget)

- 

def ``[addWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.addWidget)

- 

def ``[currentMessage()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.currentMessage)

- 

def ``[hideOrShow()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.hideOrShow)

- 

def ``[insertPermanentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.insertPermanentWidget)

- 

def ``[insertWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.insertWidget)

- 

def ``[isSizeGripEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.isSizeGripEnabled)

- 

def ``[reformat()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.reformat)

- 

def ``[removeWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.removeWidget)

- 

def ``[setSizeGripEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.setSizeGripEnabled)

### Slots[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#slots)

- 

def ``[clearMessage()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.clearMessage)

- 

def ``[showMessage()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.showMessage)

### Signals[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#signals)

- 

def ``[messageChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.messageChanged)

Note

This documentation may contain snippets that were automatically translated from C++ to Python. We always welcome contributions to the snippet translation. If you see an issue with the translation, you can also let us know by creating a ticket on [https:/bugreports.qt.io/projects/PYSIDE](https://doc.qt.io/bugreports.qt.io/projects/PYSIDE)

Note

Properties can be used directly when `from __feature__ import true_property` is used or via accessor functions otherwise.

property sizeGripEnabledᅟ : bool[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.sizeGripEnabled)

This property holds whether the ``[QSizeGrip](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QSizeGrip.html#PySide6.QtWidgets.QSizeGrip)  in the bottom-right corner of the status bar is enabled.

The size grip is enabled by default.

Access functions:

- 

``[isSizeGripEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.isSizeGripEnabled)

- 

``[setSizeGripEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.setSizeGripEnabled)

__init__ ([parent=None ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.__init__) Parameters :

parent  – ``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

Constructs a status bar with a size grip and the given `parent`.

> 

See also

``[setSizeGripEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.setSizeGripEnabled)

addPermanentWidget (widget [, stretch=0 ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.addPermanentWidget) Parameters :

- 

widget  – ``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

- 

stretch  – int

Adds the given `widget` permanently to this status bar, reparenting the widget if it isn’t already a child of this ``[QStatusBar](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar)  object. The `stretch` parameter is used to compute a suitable size for the given `widget` as the status bar grows and shrinks. The default stretch factor is 0, i.e giving the widget a minimum of space.

Permanently means that the widget may not be obscured by temporary messages. It is located at the far right of the status bar.

> 

See also

``[insertPermanentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.insertPermanentWidget)``[removeWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.removeWidget)``[addWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.addWidget)

addWidget (widget [, stretch=0 ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.addWidget) Parameters :

- 

widget  – ``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

- 

stretch  – int

Adds the given `widget` to this status bar, reparenting the widget if it isn’t already a child of this ``[QStatusBar](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar)  object. The `stretch` parameter is used to compute a suitable size for the given `widget` as the status bar grows and shrinks. The default stretch factor is 0, i.e giving the widget a minimum of space.

The widget is located to the far left of the first permanent widget (see ``[addPermanentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.addPermanentWidget)  ) and may be obscured by temporary messages.

> 

See also

``[insertWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.insertWidget)``[removeWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.removeWidget)``[addPermanentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.addPermanentWidget)

clearMessage ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.clearMessage)

Removes any temporary message being shown.

> 

See also

``[currentMessage()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.currentMessage)``[showMessage()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.showMessage)``[removeWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.removeWidget)

currentMessage ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.currentMessage) Return type :

str

Returns the temporary message currently shown, or an empty string if there is no such message.

> 

See also

``[showMessage()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.showMessage)

hideOrShow ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.hideOrShow)

Ensures that the right widgets are visible.

Used by the ``[showMessage()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.showMessage)  and ``[clearMessage()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.clearMessage)  functions.

insertPermanentWidget (index , widget [, stretch=0 ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.insertPermanentWidget) Parameters :

- 

index  – int

- 

widget  – ``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

- 

stretch  – int

Return type :

int

Inserts the given `widget` at the given `index` permanently to this status bar, reparenting the widget if it isn’t already a child of this ``[QStatusBar](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar)  object. If `index` is out of range, the widget is appended (in which case it is the actual index of the widget that is returned).

The `stretch` parameter is used to compute a suitable size for the given `widget` as the status bar grows and shrinks. The default stretch factor is 0, i.e giving the widget a minimum of space.

Permanently means that the widget may not be obscured by temporary messages. It is located at the far right of the status bar.

> 

See also

``[addPermanentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.addPermanentWidget)``[removeWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.removeWidget)``[addWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.addWidget)

insertWidget (index , widget [, stretch=0 ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.insertWidget) Parameters :

- 

index  – int

- 

widget  – ``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

- 

stretch  – int

Return type :

int

Inserts the given `widget` at the given `index` to this status bar, reparenting the widget if it isn’t already a child of this ``[QStatusBar](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar)  object. If `index` is out of range, the widget is appended (in which case it is the actual index of the widget that is returned).

The `stretch` parameter is used to compute a suitable size for the given `widget` as the status bar grows and shrinks. The default stretch factor is 0, i.e giving the widget a minimum of space.

The widget is located to the far left of the first permanent widget (see ``[addPermanentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.addPermanentWidget)  ) and may be obscured by temporary messages.

> 

See also

``[addWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.addWidget)``[removeWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.removeWidget)``[addPermanentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.addPermanentWidget)

isSizeGripEnabled ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.isSizeGripEnabled) Return type :

bool

Getter of property ``[sizeGripEnabledᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.sizeGripEnabled)  .

messageChanged (text )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.messageChanged) Parameters :

text  – str

This signal is emitted whenever the temporary status message changes. The new temporary message is passed in the `message` parameter which is a null-string when the message has been removed.

> 

See also

``[showMessage()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.showMessage)``[clearMessage()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.clearMessage)

reformat ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.reformat)

Changes the status bar’s appearance to account for item changes.

Special subclasses may need this function, but geometry management will usually take care of any necessary rearrangements.

removeWidget (widget )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.removeWidget) Parameters :

widget  – ``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

Removes the specified `widget` from the status bar.

Note

This function does not delete the widget but hides  it. To add the widget again, you must call both the ``[addWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.addWidget)  and `show()` functions.

See also

``[addWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.addWidget)``[addPermanentWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.addPermanentWidget)``[clearMessage()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.clearMessage)

setSizeGripEnabled (arg__1 )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.setSizeGripEnabled) Parameters :

arg__1  – bool

See also

``[isSizeGripEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.isSizeGripEnabled)

Setter of property ``[sizeGripEnabledᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.sizeGripEnabled)  .

showMessage (text [, timeout=0 ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.showMessage) Parameters :

- 

text  – str

- 

timeout  – int

Hides the normal status indications and displays the given `message` for the specified number of milli-seconds (`timeout`). If `timeout` is 0 (default), the `message` remains displayed until the ``[clearMessage()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.clearMessage)  slot is called or until the showMessage() slot is called again to change the message.

Note that showMessage() is called to show temporary explanations of tool tip texts, so passing a `timeout` of 0 is not sufficient to display a `permanent message` .

> 

See also

``[messageChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.messageChanged)``[currentMessage()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.currentMessage)``[clearMessage()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStatusBar.html#PySide6.QtWidgets.QStatusBar.clearMessage)
