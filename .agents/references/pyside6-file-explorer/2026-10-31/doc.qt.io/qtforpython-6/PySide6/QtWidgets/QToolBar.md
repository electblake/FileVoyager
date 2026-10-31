<!--
source: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html
retrieved: 2026-10-31T21:18:35.941128+00:00
final_url: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html
content_type: text/html
-->

# PySide6.QtWidgets.QToolBar - Qt for Python

[Skip to content](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#furo-main-content)

[Qt for Python](https://doc.qt.io/qtforpython-6/index.html)

[Back to top](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html)

# PySide6.QtWidgets.QToolBar[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#pyside6-qtwidgets-qtoolbar)

class QToolBar[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar)

The ``[QToolBar](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar)  class provides a movable panel that contains a set of controls.

Details

A toolbar is typically created by calling `addToolBar(const QString &title)` , but it can also be added as the first widget in a ``[QVBoxLayout](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QVBoxLayout.html#PySide6.QtWidgets.QVBoxLayout)  , for example.

Toolbar buttons are added by adding actions , using `addAction()` or `insertAction()` . Groups of buttons can be separated using ``[addSeparator()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.addSeparator)  or ``[insertSeparator()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.insertSeparator)  . If a toolbar button is not appropriate, a widget can be inserted instead using ``[addWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.addWidget)  or ``[insertWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.insertWidget)  . Examples of suitable widgets are ``[QSpinBox](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QSpinBox.html#PySide6.QtWidgets.QSpinBox)  , ``[QDoubleSpinBox](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDoubleSpinBox.html#PySide6.QtWidgets.QDoubleSpinBox)  , and ``[QComboBox](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QComboBox.html#PySide6.QtWidgets.QComboBox)  . When a toolbar button is pressed, it emits the ``[actionTriggered()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.actionTriggered)  signal.

A toolbar can be fixed in place in a particular area (e.g., at the top of the window), or it can be movable between toolbar areas; see ``[setMovable()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setMovable)  , ``[isMovable()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.isMovable)  , ``[allowedAreas()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id0)  and ``[isAreaAllowed()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.isAreaAllowed)  .

When a toolbar is resized in such a way that it is too small to show all the items it contains, an extension button will appear as the last item in the toolbar. Pressing the extension button will pop up a menu containing the items that do not currently fit in the toolbar.

When a ``[QToolBar](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar)  is not a child of a ``[QMainWindow](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMainWindow.html#PySide6.QtWidgets.QMainWindow)  , it loses the ability to populate the extension pop up with widgets added to the toolbar using ``[addWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.addWidget)  . Please use widget actions created by inheriting ``[QWidgetAction](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidgetAction.html#PySide6.QtWidgets.QWidgetAction)  and implementing ``[createWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidgetAction.html#PySide6.QtWidgets.QWidgetAction.createWidget)  instead.

> 

See also

``[QToolButton](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolButton.html#PySide6.QtWidgets.QToolButton)``[QMenu](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMenu.html#PySide6.QtWidgets.QMenu)``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

Inheritance diagram of PySide6.QtWidgets.QToolBar

## Synopsis[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#synopsis)

### Properties[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#properties)

- 

``[allowedAreasᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.allowedAreas)  - Areas where the toolbar may be placed

- 

``[floatableᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.floatable)  - Whether the toolbar can be dragged and dropped as an independent window

- 

``[floatingᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.floating)  - Whether the toolbar is an independent window

- 

``[iconSizeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.iconSize)  - Size of icons in the toolbar

- 

``[movableᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.movable)  - Whether the user can move the toolbar within the toolbar area, or between toolbar areas

- 

``[orientationᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.orientation)  - Of the toolbar

- 

``[toolButtonStyleᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.toolButtonStyle)  - The style of toolbar buttons

### Methods[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#methods)

- 

def ``[__init__()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.__init__)

- 

def ``[actionAt()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.actionAt)

- 

def ``[actionGeometry()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.actionGeometry)

- 

def ``[addSeparator()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.addSeparator)

- 

def ``[addWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.addWidget)

- 

def ``[allowedAreas()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id0)

- 

def ``[clear()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.clear)

- 

def ``[iconSize()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id1)

- 

def ``[insertSeparator()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.insertSeparator)

- 

def ``[insertWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.insertWidget)

- 

def ``[isAreaAllowed()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.isAreaAllowed)

- 

def ``[isFloatable()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.isFloatable)

- 

def ``[isFloating()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.isFloating)

- 

def ``[isMovable()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.isMovable)

- 

def ``[orientation()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id2)

- 

def ``[setAllowedAreas()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setAllowedAreas)

- 

def ``[setFloatable()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setFloatable)

- 

def ``[setMovable()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setMovable)

- 

def ``[setOrientation()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setOrientation)

- 

def ``[toggleViewAction()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.toggleViewAction)

- 

def ``[toolButtonStyle()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id3)

- 

def ``[widgetForAction()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.widgetForAction)

### Virtual methods[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#virtual-methods)

- 

def ``[initStyleOption()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.initStyleOption)

### Slots[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#slots)

- 

def ``[setIconSize()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setIconSize)

- 

def ``[setToolButtonStyle()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setToolButtonStyle)

### Signals[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#signals)

- 

def ``[actionTriggered()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.actionTriggered)

- 

def ``[allowedAreasChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.allowedAreasChanged)

- 

def ``[iconSizeChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.iconSizeChanged)

- 

def ``[movableChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.movableChanged)

- 

def ``[orientationChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.orientationChanged)

- 

def ``[toolButtonStyleChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.toolButtonStyleChanged)

- 

def ``[topLevelChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.topLevelChanged)

- 

def ``[visibilityChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.visibilityChanged)

Note

This documentation may contain snippets that were automatically translated from C++ to Python. We always welcome contributions to the snippet translation. If you see an issue with the translation, you can also let us know by creating a ticket on [https:/bugreports.qt.io/projects/PYSIDE](https://doc.qt.io/bugreports.qt.io/projects/PYSIDE)

Note

Properties can be used directly when `from __feature__ import true_property` is used or via accessor functions otherwise.

property allowedAreasᅟ : Combination of Qt.ToolBarArea[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.allowedAreas)

This property holds areas where the toolbar may be placed.

The default is Qt::AllToolBarAreas.

This property only makes sense if the toolbar is in a ``[QMainWindow](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMainWindow.html#PySide6.QtWidgets.QMainWindow)  .

> 

See also

`movable()`

Access functions:

- 

``[allowedAreas()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id0)

- 

``[setAllowedAreas()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setAllowedAreas)

- 

Signal ``[allowedAreasChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.allowedAreasChanged)

property floatableᅟ : bool[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.floatable)

This property holds whether the toolbar can be dragged and dropped as an independent window..

The default is true.

Access functions:

- 

``[isFloatable()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.isFloatable)

- 

``[setFloatable()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setFloatable)

property floatingᅟ : bool[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.floating)

This property holds whether the toolbar is an independent window..

By default, this property is `true`.

> 

See also

``[isWindow()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget.isWindow)

Access functions:

- 

``[isFloating()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.isFloating)

property iconSizeᅟ :[QSize](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSize.html#PySide6.QtCore.QSize)[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.iconSize)

This property holds size of icons in the toolbar..

The default size is determined by the application’s style and is derived from the ``[PM_ToolBarIconSize](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyle.html#PySide6.QtWidgets.QStyle.PixelMetric)  pixel metric. It is the maximum size an icon can have. Icons of smaller size will not be scaled up.

Access functions:

- 

``[iconSize()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id1)

- 

``[setIconSize()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setIconSize)

- 

Signal ``[iconSizeChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.iconSizeChanged)

property movableᅟ : bool[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.movable)

This property holds whether the user can move the toolbar within the toolbar area, or between toolbar areas..

The default value is style dependent (determined by the ``[SH_ToolBar_Movable](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyle.html#PySide6.QtWidgets.QStyle.StyleHint)  style hint), and is `true` for most styles.

This property only makes sense if the toolbar is in a ``[QMainWindow](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMainWindow.html#PySide6.QtWidgets.QMainWindow)  .

> 

See also

``[allowedAreas()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id0)

Access functions:

- 

``[isMovable()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.isMovable)

- 

``[setMovable()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setMovable)

- 

Signal ``[movableChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.movableChanged)

property orientationᅟ :[Qt.Orientation](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.Orientation)[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.orientation)

This property holds orientation of the toolbar.

The default is Qt::Horizontal.

This function should not be used when the toolbar is managed by ``[QMainWindow](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMainWindow.html#PySide6.QtWidgets.QMainWindow)  . You can use ``[addToolBar()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMainWindow.html#PySide6.QtWidgets.QMainWindow.addToolBar)  or ``[insertToolBar()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMainWindow.html#PySide6.QtWidgets.QMainWindow.insertToolBar)  if you wish to move a toolbar that is already added to a main window to another Qt::ToolBarArea.

Access functions:

- 

``[orientation()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id2)

- 

``[setOrientation()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setOrientation)

- 

Signal ``[orientationChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.orientationChanged)

property toolButtonStyleᅟ :[Qt.ToolButtonStyle](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.ToolButtonStyle)[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.toolButtonStyle)

This property holds the style of toolbar buttons.

This property defines the style of all tool buttons that are added as QActions. Note that if you add a ``[QToolButton](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolButton.html#PySide6.QtWidgets.QToolButton)  with the ``[addWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.addWidget)  method, it will not get this button style.

To have the style of toolbuttons follow the system settings, set this property to Qt::ToolButtonFollowStyle. On Unix, the user settings from the desktop environment will be used. On other platforms, Qt::ToolButtonFollowStyle means icon only.

The default is Qt::ToolButtonIconOnly.

Access functions:

- 

``[toolButtonStyle()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id3)

- 

``[setToolButtonStyle()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setToolButtonStyle)

- 

Signal ``[toolButtonStyleChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.toolButtonStyleChanged)

__init__ ([parent=None ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.__init__) Parameters :

parent  – ``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

Constructs a ``[QToolBar](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar)  with the given `parent`.

__init__ (title [, parent=None ] ) Parameters :

- 

title  – str

- 

parent  – ``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

Constructs a ``[QToolBar](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar)  with the given `parent`.

The given window `title` identifies the toolbar and is shown in the context menu provided by ``[QMainWindow](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMainWindow.html#PySide6.QtWidgets.QMainWindow)  .

> 

See also

`setWindowTitle()`

actionAt (p )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.actionAt) Parameters :

p  – ``[QPoint](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QPoint.html#PySide6.QtCore.QPoint)

Return type :

``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

Returns the action at point `p`. This function returns zero if no action was found.

> 

See also

``[childAt()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget.childAt)

actionAt (x , y ) Parameters :

- 

x  – int

- 

y  – int

Return type :

``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

Returns the action at the point `x`, `y`. This function returns zero if no action was found.

actionGeometry (action )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.actionGeometry) Parameters :

action  – ``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

Return type :

``[QRect](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QRect.html#PySide6.QtCore.QRect)

actionTriggered (action )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.actionTriggered) Parameters :

action  – ``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

This signal is emitted when an action in this toolbar is triggered. This happens when the action’s tool button is pressed, or when the action is triggered in some other way outside the toolbar. The parameter holds the triggered `action`.

addSeparator ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.addSeparator) Return type :

``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

Adds a separator to the end of the toolbar.

> 

See also

``[insertSeparator()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.insertSeparator)

addWidget (widget )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.addWidget) Parameters :

widget  – ``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

Return type :

``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

Adds the given `widget` to the toolbar as the toolbar’s last item.

The toolbar takes ownership of `widget`.

If you add a ``[QToolButton](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolButton.html#PySide6.QtWidgets.QToolButton)  with this method, the toolbar’s Qt::ToolButtonStyle will not be respected.

Note

You should use QAction::setVisible() to change the visibility of the widget. Using ``[setVisible()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget.setVisible)  , ``[show()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget.show)  and ``[hide()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget.hide)  does not work.

See also

``[insertWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.insertWidget)

allowedAreas ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id0) Return type :

Combination of ``[ToolBarArea](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.ToolBarArea)

See also

``[setAllowedAreas()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setAllowedAreas)

Getter of property ``[allowedAreasᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.allowedAreas)  .

allowedAreasChanged (allowedAreas )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.allowedAreasChanged) Parameters :

allowedAreas  – Combination of ``[ToolBarArea](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.ToolBarArea)

This signal is emitted when the collection of allowed areas for the toolbar is changed. The new areas in which the toolbar can be positioned are specified by `allowedAreas`.

> 

See also

``[allowedAreas()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id0)

Notification signal of property ``[allowedAreasᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.allowedAreas)  .

clear ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.clear)

Removes all actions from the toolbar.

> 

See also

`removeAction()`

iconSize ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id1) Return type :

``[QSize](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSize.html#PySide6.QtCore.QSize)

See also

``[setIconSize()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setIconSize)

Getter of property ``[iconSizeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.iconSize)  .

iconSizeChanged (iconSize )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.iconSizeChanged) Parameters :

iconSize  – ``[QSize](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSize.html#PySide6.QtCore.QSize)

This signal is emitted when the icon size is changed. The `iconSize` parameter holds the toolbar’s new icon size.

> 

See also

``[iconSize()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id1)``[iconSize()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMainWindow.html#id2)

Notification signal of property ``[iconSizeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.iconSize)  .

initStyleOption (option )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.initStyleOption) Parameters :

option  – ``[QStyleOptionToolBar](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyleOptionToolBar.html#PySide6.QtWidgets.QStyleOptionToolBar)

insertSeparator (before )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.insertSeparator) Parameters :

before  – ``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

Return type :

``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

Inserts a separator into the toolbar in front of the toolbar item associated with the `before` action.

> 

See also

``[addSeparator()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.addSeparator)

insertWidget (before , widget )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.insertWidget) Parameters :

- 

before  – ``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

- 

widget  – ``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

Return type :

``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

Inserts the given `widget` in front of the toolbar item associated with the `before` action.

Note: You should use QAction::setVisible() to change the visibility of the widget. Using ``[setVisible()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget.setVisible)  , ``[show()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget.show)  and ``[hide()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget.hide)  does not work.

> 

See also

``[addWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.addWidget)

isAreaAllowed (area )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.isAreaAllowed) Parameters :

area  – ``[ToolBarArea](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.ToolBarArea)

Return type :

bool

Returns `true` if this toolbar is dockable in the given `area`; otherwise returns `false`.

isFloatable ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.isFloatable) Return type :

bool

Getter of property ``[floatableᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.floatable)  .

isFloating ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.isFloating) Return type :

bool

Getter of property ``[floatingᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.floating)  .

isMovable ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.isMovable) Return type :

bool

Getter of property ``[movableᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.movable)  .

movableChanged (movable )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.movableChanged) Parameters :

movable  – bool

This signal is emitted when the toolbar becomes movable or fixed. If the toolbar can be moved, `movable` is true; otherwise it is false.

> 

See also

`movable()`

Notification signal of property ``[movableᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.movable)  .

orientation ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id2) Return type :

``[Orientation](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.Orientation)

See also

``[setOrientation()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setOrientation)

Getter of property ``[orientationᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.orientation)  .

orientationChanged (orientation )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.orientationChanged) Parameters :

orientation  – ``[Orientation](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.Orientation)

This signal is emitted when the orientation of the toolbar changes. The `orientation` parameter holds the toolbar’s new orientation.

> 

See also

``[orientation()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id2)

Notification signal of property ``[orientationᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.orientation)  .

setAllowedAreas (areas )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setAllowedAreas) Parameters :

areas  – Combination of ``[ToolBarArea](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.ToolBarArea)

See also

``[allowedAreas()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id0)

Setter of property ``[allowedAreasᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.allowedAreas)  .

setFloatable (floatable )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setFloatable) Parameters :

floatable  – bool

See also

``[isFloatable()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.isFloatable)

Setter of property ``[floatableᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.floatable)  .

setIconSize (iconSize )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setIconSize) Parameters :

iconSize  – ``[QSize](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSize.html#PySide6.QtCore.QSize)

See also

``[iconSize()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id1)

Setter of property ``[iconSizeᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.iconSize)  .

setMovable (movable )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setMovable) Parameters :

movable  – bool

See also

``[isMovable()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.isMovable)

Setter of property ``[movableᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.movable)  .

setOrientation (orientation )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setOrientation) Parameters :

orientation  – ``[Orientation](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.Orientation)

See also

``[orientation()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id2)

Setter of property ``[orientationᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.orientation)  .

setToolButtonStyle (toolButtonStyle )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setToolButtonStyle) Parameters :

toolButtonStyle  – ``[ToolButtonStyle](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.ToolButtonStyle)

See also

``[toolButtonStyle()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id3)

Setter of property ``[toolButtonStyleᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.toolButtonStyle)  .

toggleViewAction ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.toggleViewAction) Return type :

``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

Returns a checkable action that can be used to show or hide this toolbar.

The action’s text is set to the toolbar’s window title.

> 

See also

``[windowTitle()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#id45)

toolButtonStyle ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id3) Return type :

``[ToolButtonStyle](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.ToolButtonStyle)

See also

``[setToolButtonStyle()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.setToolButtonStyle)

Getter of property ``[toolButtonStyleᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.toolButtonStyle)  .

toolButtonStyleChanged (toolButtonStyle )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.toolButtonStyleChanged) Parameters :

toolButtonStyle  – ``[ToolButtonStyle](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.ToolButtonStyle)

This signal is emitted when the tool button style is changed. The `toolButtonStyle` parameter holds the toolbar’s new tool button style.

> 

See also

``[toolButtonStyle()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#id3)``[toolButtonStyle()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMainWindow.html#id4)

Notification signal of property ``[toolButtonStyleᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.toolButtonStyle)  .

topLevelChanged (topLevel )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.topLevelChanged) Parameters :

topLevel  – bool

This signal is emitted when the `floating()` property changes. The `topLevel` parameter is true if the toolbar is now floating; otherwise it is false.

> 

See also

`isWindow()`

visibilityChanged (visible )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.visibilityChanged) Parameters :

visible  – bool

This signal is emitted when the toolbar becomes `visible` (or invisible). This happens when the widget is hidden or shown.

widgetForAction (action )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.widgetForAction) Parameters :

action  – ``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

Return type :

``[QWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.QWidget)

Returns the widget associated with the specified `action`.

> 

See also

``[addWidget()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolBar.html#PySide6.QtWidgets.QToolBar.addWidget)
