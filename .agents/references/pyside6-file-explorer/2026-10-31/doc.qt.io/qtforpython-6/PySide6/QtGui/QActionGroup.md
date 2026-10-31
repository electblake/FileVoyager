<!--
source: https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html
retrieved: 2026-10-31T21:18:38.747039+00:00
final_url: https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html
content_type: text/html
-->

# PySide6.QtGui.QActionGroup - Qt for Python

[Skip to content](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#furo-main-content)

[Qt for Python](https://doc.qt.io/qtforpython-6/index.html)

[Back to top](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html)

# PySide6.QtGui.QActionGroup[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#pyside6-qtgui-qactiongroup)

class QActionGroup[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup)

The ``[QActionGroup](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup)  class groups actions together.

Details

``[QActionGroup](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup)  is a base class for classes grouping classes inhheriting ``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)  objects together.

In some situations it is useful to group ``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)  objects together. For example, if you have a Left Align action, a Right Align action, a Justify action, and a Center action, only one of these actions should be active at any one time. One simple way of achieving this is to group the actions together in an action group, inheriting ``[QActionGroup](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup)  .

> 

See also

``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

Inheritance diagram of PySide6.QtGui.QActionGroup

## Synopsis[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#synopsis)

### Properties[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#properties)

- 

``[enabledᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.enabled)  - Whether the action group is enabled

- 

``[exclusionPolicyᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.exclusionPolicy)  - This property holds the group exclusive checking policy

- 

``[visibleᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.visible)  - Whether the action group is visible

### Methods[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#methods)

- 

def ``[__init__()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.__init__)

- 

def ``[actions()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.actions)

- 

def ``[addAction()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.addAction)

- 

def ``[checkedAction()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.checkedAction)

- 

def ``[exclusionPolicy()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#id0)

- 

def ``[isEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.isEnabled)

- 

def ``[isExclusive()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.isExclusive)

- 

def ``[isVisible()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.isVisible)

- 

def ``[removeAction()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.removeAction)

### Slots[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#slots)

- 

def ``[setDisabled()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.setDisabled)

- 

def ``[setEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.setEnabled)

- 

def ``[setExclusionPolicy()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.setExclusionPolicy)

- 

def ``[setExclusive()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.setExclusive)

- 

def ``[setVisible()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.setVisible)

### Signals[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#signals)

- 

def ``[hovered()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.hovered)

- 

def ``[triggered()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.triggered)

Note

This documentation may contain snippets that were automatically translated from C++ to Python. We always welcome contributions to the snippet translation. If you see an issue with the translation, you can also let us know by creating a ticket on [https:/bugreports.qt.io/projects/PYSIDE](https://doc.qt.io/bugreports.qt.io/projects/PYSIDE)

class ExclusionPolicy[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.ExclusionPolicy)

This enum specifies the different policies that can be used to control how the group performs exclusive checking on checkable actions.

> 

Constant

Description

QActionGroup.ExclusionPolicy.ExclusionPolicy.None_

The actions in the group can be checked independently of each other.

QActionGroup.ExclusionPolicy.ExclusionPolicy.Exclusive

Exactly one action can be checked at any one time. This is the default policy.

QActionGroup.ExclusionPolicy.ExclusionPolicy.ExclusiveOptional

At most one action can be checked at any one time. The actions can also be all unchecked.

See also

``[exclusionPolicy()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#id0)

Note

Properties can be used directly when `from __feature__ import true_property` is used or via accessor functions otherwise.

property enabledᅟ : bool[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.enabled)

This property holds whether the action group is enabled.

Each action in the group will be enabled or disabled unless it has been explicitly disabled.

> 

See also

``[setEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction.setEnabled)

Access functions:

- 

``[isEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.isEnabled)

- 

``[setEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.setEnabled)

property exclusionPolicyᅟ :[QActionGroup.ExclusionPolicy](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.ExclusionPolicy)[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.exclusionPolicy)

This property holds This property holds the group exclusive checking policy.

If exclusionPolicy is set to Exclusive, only one checkable action in the action group can ever be active at any time. If the user chooses another checkable action in the group, the one they chose becomes active and the one that was active becomes inactive. If exclusionPolicy is set to ExclusionOptional the group is exclusive but the active checkable action in the group can be unchecked leaving the group with no actions checked.

> 

See also

`checkable()`

Access functions:

- 

``[exclusionPolicy()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#id0)

- 

``[setExclusionPolicy()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.setExclusionPolicy)

property visibleᅟ : bool[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.visible)

This property holds whether the action group is visible.

Each action in the action group will match the visible state of this group unless it has been explicitly hidden.

> 

See also

``[setEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction.setEnabled)

Access functions:

- 

``[isVisible()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.isVisible)

- 

``[setVisible()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.setVisible)

__init__ (parent )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.__init__) Parameters :

parent  – ``[QObject](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QObject.html#PySide6.QtCore.QObject)

Constructs an action group for the `parent` object.

The action group is exclusive by default. Call ``[setExclusive()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.setExclusive)  (false) to make the action group non-exclusive. To make the group exclusive but allow unchecking the active action call instead ``[setExclusionPolicy()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.setExclusionPolicy)  ( ``[ExclusiveOptional](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.ExclusionPolicy)  )

actions ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.actions) Return type :

.list of [QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

Returns the list of this groups’s actions. This may be empty.

addAction (a )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.addAction) Parameters :

a  – ``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

Return type :

``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

Adds the `action` to this group, and returns it.

Normally an action is added to a group by creating it with the group as its parent, so this function is not usually used.

> 

See also

``[setActionGroup()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction.setActionGroup)

addAction (text ) Parameters :

text  – str

Return type :

``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

Creates and returns an action with `text`. The newly created action is a child of this action group.

Normally an action is added to a group by creating it with the group as parent, so this function is not usually used.

> 

See also

``[setActionGroup()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction.setActionGroup)

addAction (icon , text ) Parameters :

- 

icon  – ``[QIcon](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QIcon.html#PySide6.QtGui.QIcon)

- 

text  – str

Return type :

``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

Creates and returns an action with `text` and an `icon`. The newly created action is a child of this action group.

Normally an action is added to a group by creating it with the group as its parent, so this function is not usually used.

> 

See also

``[setActionGroup()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction.setActionGroup)

checkedAction ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.checkedAction) Return type :

``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

Returns the currently checked action in the group, or `None` if none are checked.

exclusionPolicy ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#id0) Return type :

``[ExclusionPolicy](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.ExclusionPolicy)

See also

``[setExclusionPolicy()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.setExclusionPolicy)

Getter of property ``[exclusionPolicyᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.exclusionPolicy)  .

hovered (action )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.hovered) Parameters :

action  – ``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

This signal is emitted when the given `action` in the action group is highlighted by the user; for example, when the user pauses with the cursor over a menu option or a toolbar button, or presses an action’s shortcut key combination.

> 

See also

``[activate()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction.activate)

isEnabled ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.isEnabled) Return type :

bool

Getter of property ``[enabledᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.enabled)  .

isExclusive ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.isExclusive) Return type :

bool

Returns true if the group is exclusive

The group is exclusive if the ``[ExclusionPolicy](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.ExclusionPolicy)  is either Exclusive or ExclusionOptional.

isVisible ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.isVisible) Return type :

bool

Getter of property ``[visibleᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.visible)  .

removeAction (a )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.removeAction) Parameters :

a  – ``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

Removes the `action` from this group. The action will have no parent as a result.

> 

See also

``[setActionGroup()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction.setActionGroup)

setDisabled (b )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.setDisabled) Parameters :

b  – bool

This is a convenience function for the `enabled()` property, that is useful for signals–slots connections. If `b` is true the action group is disabled; otherwise it is enabled.

setEnabled (arg__1 )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.setEnabled) Parameters :

arg__1  – bool

See also

``[isEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.isEnabled)

Setter of property ``[enabledᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.enabled)  .

setExclusionPolicy (policy )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.setExclusionPolicy) Parameters :

policy  – ``[ExclusionPolicy](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.ExclusionPolicy)

See also

``[exclusionPolicy()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#id0)

Setter of property ``[exclusionPolicyᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.exclusionPolicy)  .

setExclusive (b )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.setExclusive) Parameters :

b  – bool

Enable or disable the group exclusion checking

This is a convenience method that calls ``[setExclusionPolicy()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.setExclusionPolicy)  ( ``[Exclusive](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.ExclusionPolicy)  ) when `b` is true, else ``[setExclusionPolicy()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.setExclusionPolicy)  ( ``[None](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.ExclusionPolicy)  ).

> 

See also

``[isExclusive()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.isExclusive)``[exclusionPolicy()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#id0)

setVisible (arg__1 )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.setVisible) Parameters :

arg__1  – bool

See also

``[isVisible()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.isVisible)

Setter of property ``[visibleᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.visible)  .

triggered (action )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QActionGroup.html#PySide6.QtGui.QActionGroup.triggered) Parameters :

action  – ``[QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction)

This signal is emitted when the given `action` in the action group is activated by the user; for example, when the user clicks a menu option or a toolbar button, or presses an action’s shortcut key combination.

Connect to this signal for command actions.

> 

See also

``[activate()](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#PySide6.QtGui.QAction.activate)
