<!--
source: https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html
retrieved: 2026-10-31T21:18:27.346912+00:00
final_url: https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html
content_type: text/html
-->

# PySide6.QtCore.QSortFilterProxyModel - Qt for Python

[Skip to content](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#furo-main-content)

[Qt for Python](https://doc.qt.io/qtforpython-6/index.html)

[Back to top](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html)

# PySide6.QtCore.QSortFilterProxyModel[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#pyside6-qtcore-qsortfilterproxymodel)

class QSortFilterProxyModel[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel)

The ``[QSortFilterProxyModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel)  class provides support for sorting and filtering data passed between another model and a view. [More](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#more) …

Inheritance diagram of PySide6.QtCore.QSortFilterProxyModel

## Synopsis[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#synopsis)

### Properties[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#properties)

- 

``[autoAcceptChildRowsᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.autoAcceptChildRows)  - If true the proxy model will not filter out children of accepted rows, even if they themselves would be filtered out otherwise

- 

``[dynamicSortFilterᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.dynamicSortFilter)  - Whether the proxy model is dynamically sorted and filtered whenever the contents of the source model change

- 

``[filterCaseSensitivityᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterCaseSensitivity)  - The case sensitivity of the QRegularExpression pattern used to filter the contents of the source model

- 

``[filterKeyColumnᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterKeyColumn)  - The column where the key used to filter the contents of the source model is read from

- 

``[filterRegularExpressionᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterRegularExpression)  - The QRegularExpression used to filter the contents of the source model

- 

``[filterRoleᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterRole)  - The item role that is used to query the source model’s data when filtering items

- 

``[isSortLocaleAwareᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.isSortLocaleAware)  - The local aware setting used for comparing strings when sorting

- 

``[recursiveFilteringEnabledᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.recursiveFilteringEnabled)  - Whether the filter to be applied recursively on children, and for any matching child, its parents will be visible as well

- 

``[sortCaseSensitivityᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortCaseSensitivity)  - The case sensitivity setting used for comparing strings when sorting

- 

``[sortRoleᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortRole)  - The item role that is used to query the source model’s data when sorting items

### Methods[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#methods)

- 

def ``[__init__()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.__init__)

- 

def ``[autoAcceptChildRows()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id0)

- 

def ``[beginFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.beginFilterChange)

- 

def ``[dataChangeRelevanceFlags()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.dataChangeRelevanceFlags)

- 

def ``[dynamicSortFilter()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id1)

- 

def ``[endFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.endFilterChange)

- 

def ``[filterCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id2)

- 

def ``[filterKeyColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id3)

- 

def ``[filterRegularExpression()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id4)

- 

def ``[filterRole()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id5)

- 

def ``[invalidateColumnsFilter()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.invalidateColumnsFilter)

- 

def ``[invalidateFilter()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.invalidateFilter)

- 

def ``[invalidateRowsFilter()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.invalidateRowsFilter)

- 

def ``[isRecursiveFilteringEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.isRecursiveFilteringEnabled)

- 

def ``[isSortLocaleAware()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id6)

- 

def ``[setAutoAcceptChildRows()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setAutoAcceptChildRows)

- 

def ``[setDynamicSortFilter()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setDynamicSortFilter)

- 

def ``[setFilterCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterCaseSensitivity)

- 

def ``[setFilterKeyColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterKeyColumn)

- 

def ``[setFilterRole()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterRole)

- 

def ``[setRecursiveFilteringEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setRecursiveFilteringEnabled)

- 

def ``[setSortCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setSortCaseSensitivity)

- 

def ``[setSortLocaleAware()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setSortLocaleAware)

- 

def ``[setSortRole()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setSortRole)

- 

def ``[sortCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id7)

- 

def ``[sortColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortColumn)

- 

def ``[sortOrder()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortOrder)

- 

def ``[sortRole()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id8)

### Virtual methods[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#virtual-methods)

- 

def ``[filterAcceptsColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsColumn)

- 

def ``[filterAcceptsRow()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsRow)

- 

def ``[lessThan()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.lessThan)

### Slots[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#slots)

- 

def ``[invalidate()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.invalidate)

- 

def ``[setFilterFixedString()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterFixedString)

- 

def ``[setFilterRegularExpression()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterRegularExpression)

- 

def ``[setFilterWildcard()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterWildcard)

### Signals[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#signals)

- 

def ``[autoAcceptChildRowsChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.autoAcceptChildRowsChanged)

- 

def ``[dynamicSortFilterChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.dynamicSortFilterChanged)

- 

def ``[filterCaseSensitivityChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterCaseSensitivityChanged)

- 

def ``[filterRoleChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterRoleChanged)

- 

def ``[recursiveFilteringEnabledChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.recursiveFilteringEnabledChanged)

- 

def ``[sortCaseSensitivityChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortCaseSensitivityChanged)

- 

def ``[sortLocaleAwareChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortLocaleAwareChanged)

- 

def ``[sortRoleChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortRoleChanged)

Note

This documentation may contain snippets that were automatically translated from C++ to Python. We always welcome contributions to the snippet translation. If you see an issue with the translation, you can also let us know by creating a ticket on [https:/bugreports.qt.io/projects/PYSIDE](https://doc.qt.io/bugreports.qt.io/projects/PYSIDE)

## Detailed Description[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#detailed-description)

Warning

This section contains snippets that were automatically translated from C++ to Python and may contain errors.

``[QSortFilterProxyModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel)  can be used for sorting items, filtering out items, or both. The model transforms the structure of a source model by mapping the model indexes it supplies to new indexes, corresponding to different locations, for views to use. This approach allows a given source model to be restructured as far as views are concerned without requiring any transformations on the underlying data, and without duplicating the data in memory.

Let’s assume that we want to sort and filter the items provided by a custom model. The code to set up the model and the view, without  sorting and filtering, would look like this:

> 

```
        treeView = QTreeView()
//! [0]
        model = MyItemModel(self)
        treeView.setModel(model)
```

To add sorting and filtering support to `MyItemModel`, we need to create a ``[QSortFilterProxyModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel)  , call `setSourceModel()` with the `MyItemModel` as argument, and install the ``[QSortFilterProxyModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel)  on the view:

> 

```
treeView = QTreeView()
sourceModel = MyItemModel(self)
proxyModel = QSortFilterProxyModel(self)
proxyModel.setSourceModel(sourceModel)
treeView.setModel(proxyModel)
```

At this point, neither sorting nor filtering is enabled; the original data is displayed in the view. Any changes made through the ``[QSortFilterProxyModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel)  are applied to the original model.

The ``[QSortFilterProxyModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel)  acts as a wrapper for the original model. If you need to convert source ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)  es to sorted/filtered model indexes or vice versa, use `mapToSource()` , `mapFromSource()` , `mapSelectionToSource()` , and `mapSelectionFromSource()` .

Note

By default, the model dynamically re-sorts and re-filters data whenever the original model changes. This behavior can be changed by setting the ``[dynamicSortFilter()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id1)  property.

The Basic Sort/Filter Model and Custom Sort/Filter Model examples illustrate how to use ``[QSortFilterProxyModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel)  to perform basic sorting and filtering and how to subclass it to implement custom behavior.

> 

### Sorting[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#sorting)

QTableView and QTreeView have a sortingEnabled property that controls whether the user can sort the view by clicking the view’s horizontal header. For example:

> 

```
treeView.setSortingEnabled(True)
```

When this feature is on (the default is off), clicking on a header section sorts the items according to that column. By clicking repeatedly, the user can alternate between ascending and descending order.

> 

Behind the scene, the view calls the `sort()` virtual function on the model to reorder the data in the model. To make your data sortable, you can either implement `sort()` in your model, or use a ``[QSortFilterProxyModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel)  to wrap your model – ``[QSortFilterProxyModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel)  provides a generic `sort()` reimplementation that operates on the ``[sortRole()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id8)  ( ``[DisplayRole](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.ItemDataRole)  by default) of the items and that understands several data types, including `int`, `QString` , and ``[QDateTime](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QDateTime.html#PySide6.QtCore.QDateTime)  . For hierarchical models, sorting is applied recursively to all child items. String comparisons are case sensitive by default; this can be changed by setting the ``[sortCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id7)  property.

Custom sorting behavior is achieved by subclassing ``[QSortFilterProxyModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel)  and reimplementing ``[lessThan()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.lessThan)  , which is used to compare items. For example:

> 

```
bool MySortFilterProxyModel.lessThan(QModelIndex left,
                                      QModelIndex right)

    leftData = sourceModel().data(left)
    rightData = sourceModel().data(right)
//! [4]
//! [6]
    if leftData.userType() == QMetaType.QDateTime:
        return leftData.toDateTime() < rightData.toDateTime()
    emailPattern = QRegularExpression("[\\w\\.]*@[\\w\\.]*")
    leftString = leftData.toString()
    if left.column() == 1:
        match = emailPattern.match(leftString)
        if match.hasMatch():
            leftString = match.captured(0)

    rightString = rightData.toString()
    if right.column() == 1:
        match = emailPattern.match(rightString)
        if match.hasMatch():
            rightString = match.captured(0)

    return QString.localeAwareCompare(leftString, rightString) < 0
```

(This code snippet comes from the Custom Sort/Filter Model example.)

An alternative approach to sorting is to disable sorting on the view and to impose a certain order to the user. This is done by explicitly calling `sort()` with the desired column and order as arguments on the ``[QSortFilterProxyModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel)  (or on the original model if it implements `sort()` ). For example:

> 

```
proxyModel.sort(2, Qt.AscendingOrder)
```

``[QSortFilterProxyModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel)  can be sorted by column -1, in which case it returns to the sort order of the underlying source model.

Note

``[sortColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortColumn)  returns the most recently used sort column. The default value is -1, which means that this proxy model does not sort. Also, note that `sort()` sets the ``[sortColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortColumn)  to the most recently used sort column.

### Filtering[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#filtering)

In addition to sorting, ``[QSortFilterProxyModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel)  can be used to hide items that do not match a certain filter. The filter is specified using a ``[QRegularExpression](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QRegularExpression.html#PySide6.QtCore.QRegularExpression)  object and is applied to the ``[filterRole()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id5)  ( ``[DisplayRole](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.ItemDataRole)  by default) of each item, for a given column. The ``[QRegularExpression](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QRegularExpression.html#PySide6.QtCore.QRegularExpression)  object can be used to match a regular expression, a wildcard pattern, or a fixed string. For example:

> 

```
proxyModel.setFilterRegularExpression(QRegularExpression("\\.png", QRegularExpression.CaseInsensitiveOption))
proxyModel.setFilterKeyColumn(1)
```

For hierarchical models, the filter is applied recursively to all children. If a parent item doesn’t match the filter, none of its children will be shown.

A common use case is to let the user specify the filter regular expression, wildcard pattern, or fixed string in a QLineEdit. To do this, connect the QLineEdit::textChanged() or textEdited() signal to either ``[setFilterRegularExpression()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterRegularExpression)  , ``[setFilterWildcard()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterWildcard)  , or ``[setFilterFixedString()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterFixedString)  .

Custom filtering behavior can be achieved by reimplementing the ``[filterAcceptsRow()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsRow)  and ``[filterAcceptsColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsColumn)  functions. For example (from the Custom Sort/Filter Model example), the following implementation ignores the ``[filterKeyColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id3)  property and performs filtering on columns 0, 1, and 2:

> 

```
bool MySortFilterProxyModel.filterAcceptsRow(int sourceRow,
                                              QModelIndex sourceParent)

    index0 = sourceModel().index(sourceRow, 0, sourceParent)
    index1 = sourceModel().index(sourceRow, 1, sourceParent)
    index2 = sourceModel().index(sourceRow, 2, sourceParent)
    return (sourceModel().data(index0).toString().contains(filterRegularExpression())
            def sourceModel().data(index1).toString().contains(filterRegularExpression())):
            def dateInRange(sourceModel().data(index2).toDate()):
```

(This code snippet comes from the Custom Sort/Filter Model example.)

If you are working with large amounts of filtering and have to invoke ``[beginFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.beginFilterChange)  / ``[endFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.endFilterChange)  repeatedly, using `beginResetModel()` / `endResetModel()` may be more efficient, depending on the implementation of your model. However, `beginResetModel()` / `endResetModel()` returns the proxy model to its original state, losing selection information, and will cause the proxy model to be repopulated.

> 

### Subclassing[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#subclassing)

Since ``[QAbstractProxyModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractProxyModel.html#PySide6.QtCore.QAbstractProxyModel)  and its subclasses are derived from ``[QAbstractItemModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel)  , much of the same advice about subclassing normal models also applies to proxy models. In addition, it is worth noting that many of the default implementations of functions in this class are written so that they call the equivalent functions in the relevant source model. This simple proxying mechanism may need to be overridden for source models with more complex behavior; for example, if the source model provides a custom `hasChildren()` implementation, you should also provide one in the proxy model.

Note

Some general guidelines for subclassing models are available in the Model Subclassing Reference.

See also

``[QAbstractProxyModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractProxyModel.html#PySide6.QtCore.QAbstractProxyModel)``[QAbstractItemModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel)``[QIdentityProxyModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QIdentityProxyModel.html#PySide6.QtCore.QIdentityProxyModel)

class Direction[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.Direction)

(inherits `enum.Flag`) This enum is used to specify the direction to which a custom filter applies when the filter parameters are changed.

> 

Constant

Description

QSortFilterProxyModel.Direction.Direction.Rows

The filter applies to ``[rows](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsRow)

QSortFilterProxyModel.Direction.Direction.Columns

The filter applies to ``[columns](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsColumn)

QSortFilterProxyModel.Direction.Direction.Both

The filter applies to both rows and columns

See also

``[beginFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.beginFilterChange)``[endFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.endFilterChange)

Added in version 6.10.

class DataChangeRelevanceFlag[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.DataChangeRelevanceFlag)

(inherits `enum.Flag`) This enum is used to specify the operation for which a source change is relevant.

> 

Constant

Description

QSortFilterProxyModel.DataChangeRelevanceFlag.DataChangeRelevanceFlag.NotRelevant

The change is irrelevant for both filtering and sorting

QSortFilterProxyModel.DataChangeRelevanceFlag.DataChangeRelevanceFlag.RelevantForFiltering

The change is relevant for filtering

QSortFilterProxyModel.DataChangeRelevanceFlag.DataChangeRelevanceFlag.RelevantForSorting

The change is relevant for sorting

QSortFilterProxyModel.DataChangeRelevanceFlag.DataChangeRelevanceFlag.RelevantForFilteringAndSorting

The change is relevant for both filtering and sorting

See also

``[dataChangeRelevanceFlags()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.dataChangeRelevanceFlags)

Added in version 6.12.

Note

Properties can be used directly when `from __feature__ import true_property` is used or via accessor functions otherwise.

property autoAcceptChildRowsᅟ : bool[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.autoAcceptChildRows)

This property holds if true the proxy model will not filter out children of accepted rows, even if they themselves would be filtered out otherwise..

The default value is false.

> 

See also

`recursiveFilteringEnabled()```[filterAcceptsRow()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsRow)

Access functions:

- 

``[autoAcceptChildRows()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id0)

- 

``[setAutoAcceptChildRows()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setAutoAcceptChildRows)

- 

Signal ``[autoAcceptChildRowsChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.autoAcceptChildRowsChanged)

property dynamicSortFilterᅟ : bool[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.dynamicSortFilter)

This property holds whether the proxy model is dynamically sorted and filtered whenever the contents of the source model change.

Note that you should not update the source model through the proxy model when dynamicSortFilter is true. For instance, if you set the proxy model on a QComboBox, then using functions that update the model, e.g., addItem(), will not work as expected. An alternative is to set dynamicSortFilter to false and call `sort()` after adding items to the QComboBox.

The default value is true.

> 

See also

``[sortColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortColumn)

Access functions:

- 

``[dynamicSortFilter()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id1)

- 

``[setDynamicSortFilter()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setDynamicSortFilter)

property filterCaseSensitivityᅟ :[Qt.CaseSensitivity](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.CaseSensitivity)[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterCaseSensitivity)

This property holds the case sensitivity of the ``[QRegularExpression](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QRegularExpression.html#PySide6.QtCore.QRegularExpression)  pattern used to filter the contents of the source model..

By default, the filter is case sensitive.

Note

Setting this property propagates the new case sensitivity to the ``[filterRegularExpression()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id4)  property, and so breaks its binding. Likewise explicitly setting ``[filterRegularExpression()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id4)  changes the current case sensitivity, thereby breaking its binding.

See also

``[filterRegularExpression()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id4)``[sortCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id7)

Access functions:

- 

``[filterCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id2)

- 

``[setFilterCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterCaseSensitivity)

- 

Signal ``[filterCaseSensitivityChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterCaseSensitivityChanged)

property filterKeyColumnᅟ : int[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterKeyColumn)

This property holds the column where the key used to filter the contents of the source model is read from..

The default value is 0. If the value is -1, the keys will be read from all columns.

Access functions:

- 

``[filterKeyColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id3)

- 

``[setFilterKeyColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterKeyColumn)

property filterRegularExpressionᅟ :[QRegularExpression](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QRegularExpression.html#PySide6.QtCore.QRegularExpression)[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterRegularExpression)

This property holds the ``[QRegularExpression](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QRegularExpression.html#PySide6.QtCore.QRegularExpression)  used to filter the contents of the source model.

Setting this property through the ``[QRegularExpression](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QRegularExpression.html#PySide6.QtCore.QRegularExpression)  overload overwrites the current ``[filterCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id2)  . By default, the ``[QRegularExpression](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QRegularExpression.html#PySide6.QtCore.QRegularExpression)  is an empty string matching all contents.

If no ``[QRegularExpression](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QRegularExpression.html#PySide6.QtCore.QRegularExpression)  or an empty string is set, everything in the source model will be accepted.

The regular expression is matched against every row in the source model, so a complex or malformed pattern can slow down or freeze the entire application, especially when used with large models. Application developers are advised to measure the performance and scalability of the regular expression before using it. If the regular expression comes from a potentially untrusted input, consider sanitizing it before passing to this method or using ``[setFilterFixedString()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterFixedString)  instead.

Note

Setting this property propagates the case sensitivity of the new regular expression to the ``[filterCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id2)  property, and so breaks its binding. Likewise explicitly setting ``[filterCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id2)  changes the case sensitivity of the current regular expression, thereby breaking its binding.

See also

``[filterCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id2)``[setFilterWildcard()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterWildcard)``[setFilterFixedString()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterFixedString)

Access functions:

- 

``[filterRegularExpression()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id4)

- 

``[setFilterRegularExpression()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterRegularExpression)

property filterRoleᅟ : int[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterRole)

This property holds the item role that is used to query the source model’s data when filtering items..

The default value is ``[DisplayRole](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.ItemDataRole)  .

> 

See also

``[filterAcceptsRow()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsRow)

Access functions:

- 

``[filterRole()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id5)

- 

``[setFilterRole()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterRole)

- 

Signal ``[filterRoleChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterRoleChanged)

property isSortLocaleAwareᅟ : bool[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.isSortLocaleAware)

This property holds the local aware setting used for comparing strings when sorting.

By default, sorting is not local aware.

> 

See also

``[sortCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id7)``[lessThan()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.lessThan)

Access functions:

- 

``[isSortLocaleAware()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id6)

- 

``[setSortLocaleAware()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setSortLocaleAware)

- 

Signal ``[sortLocaleAwareChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortLocaleAwareChanged)

property recursiveFilteringEnabledᅟ : bool[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.recursiveFilteringEnabled)

This property holds whether the filter to be applied recursively on children, and for any matching child, its parents will be visible as well..

The default value is false.

> 

See also

``[autoAcceptChildRows()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id0)``[filterAcceptsRow()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsRow)

Access functions:

- 

``[isRecursiveFilteringEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.isRecursiveFilteringEnabled)

- 

``[setRecursiveFilteringEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setRecursiveFilteringEnabled)

- 

Signal ``[recursiveFilteringEnabledChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.recursiveFilteringEnabledChanged)

property sortCaseSensitivityᅟ :[Qt.CaseSensitivity](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.CaseSensitivity)[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortCaseSensitivity)

This property holds the case sensitivity setting used for comparing strings when sorting.

By default, sorting is case sensitive.

> 

See also

``[filterCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id2)``[lessThan()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.lessThan)

Access functions:

- 

``[sortCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id7)

- 

``[setSortCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setSortCaseSensitivity)

- 

Signal ``[sortCaseSensitivityChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortCaseSensitivityChanged)

property sortRoleᅟ : int[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortRole)

This property holds the item role that is used to query the source model’s data when sorting items..

The default value is ``[DisplayRole](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.ItemDataRole)  .

> 

See also

``[lessThan()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.lessThan)

Access functions:

- 

``[sortRole()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id8)

- 

``[setSortRole()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setSortRole)

- 

Signal ``[sortRoleChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortRoleChanged)

__init__ ([parent=None ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.__init__) Parameters :

parent  – ``[QObject](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QObject.html#PySide6.QtCore.QObject)

Constructs a sorting filter model with the given `parent`.

autoAcceptChildRows ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id0) Return type :

bool

See also

``[setAutoAcceptChildRows()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setAutoAcceptChildRows)

Getter of property ``[autoAcceptChildRowsᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.autoAcceptChildRows)  .

autoAcceptChildRowsChanged (autoAcceptChildRows )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.autoAcceptChildRowsChanged) Parameters :

autoAcceptChildRows  – bool

This signals is emitted when the value of the `autoAcceptChildRows` property is changed.

> 

See also

``[autoAcceptChildRows()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id0)

Notification signal of property ``[autoAcceptChildRowsᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.autoAcceptChildRows)  .

beginFilterChange ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.beginFilterChange)

Warning

This section contains snippets that were automatically translated from C++ to Python and may contain errors.

Prepares a change of the filter.

This function should be called if you are implementing custom filtering (e.g. ``[filterAcceptsRow()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsRow)  ), and your filter parameter is about to be changed.

> 

```
def setFilterMaximumDate(self, date):

    beginFilterChange()
    maxDate = date
    endFilterChange(QSortFilterProxyModel.Direction.Rows)
```

Once the filter has been changed, call ``[endFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.endFilterChange)  with ``[Rows](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.Direction)  for row-filters, ``[Columns](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.Direction)  for column-filters, or ``[Columns](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.Direction)  | ``[Rows](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.Direction)  if both rows and columns are filtered.

> 

See also

``[endFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.endFilterChange)

dataChangeRelevanceFlags (sourceTopLeft , sourceBottomRight , roles )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.dataChangeRelevanceFlags) Parameters :

- 

sourceTopLeft  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

- 

sourceBottomRight  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

- 

roles  – .list of int

Return type :

Combination of ``[DataChangeRelevanceFlag](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.DataChangeRelevanceFlag)

Reimplement this slot in a subclass to indicate when a source model change is relevant for filtering or sorting. It is used as a performance optimization to avoid unnecessary ``[filterAcceptsRow()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsRow)  and ``[lessThan()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.lessThan)  calls upon source model changes that do not affect the sorting and filtering results. The `sourceTopLeft`, `sourceBottomRight` and `roles` parameters are those emitted by the source model’s `dataChanged()` signal corresponding to the change being evaluated for relevance.

Note

Because of binary compatibility constraints, this method can’t be virtual until Qt 7. Meanwhile, redeclare it in a subclass as a slot or `Q_INVOKABLE()` method and ``[QSortFilterProxyModel](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel)  will dynamically detect and invoke it.

Note

The default implementation assumes that any change is relevant for filtering, and only changes in the source sort column are relevant for sorting.

See also

`DataChangeRelevanceFlags```[filterAcceptsRow()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsRow)``[lessThan()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.lessThan)

dynamicSortFilter ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id1) Return type :

bool

See also

``[setDynamicSortFilter()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setDynamicSortFilter)

Getter of property ``[dynamicSortFilterᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.dynamicSortFilter)  .

dynamicSortFilterChanged (dynamicSortFilter )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.dynamicSortFilterChanged) Parameters :

dynamicSortFilter  – bool

endFilterChange ([directions=QSortFilterProxyModel.Direction.Both ] )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.endFilterChange) Parameters :

directions  – Combination of ``[Direction](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.Direction)

Invalidates the current filtering after the filter parameter has changed.

This function should be called if you implement custom filtering (e.g. ``[filterAcceptsRow()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsRow)  ), and your filter parameters have changed. The `directions` parameter specifies whether the custom filter impacts rows, columns, or both.

Call ``[beginFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.beginFilterChange)  when the filter parameter is about to change, and follow with a call to this function once the filter parameters have been changed. Call with `directions` set to ``[Rows](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.Direction)  for row-filters (i.e. ``[filterAcceptsRow()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsRow)  is implemented), ``[Columns](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.Direction)  for column-filters (i.e. ``[filterAcceptsColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsColumn)  is implemented), or `Direction::Both` if both filter functions are implemented.

filterAcceptsColumn (source_column , source_parent )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsColumn) Parameters :

- 

source_column  – int

- 

source_parent  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Return type :

bool

Returns `true` if the item in the column indicated by the given `source_column` and `source_parent` should be included in the model; otherwise returns `false`.

Note

The default implementation always returns `true`. You must reimplement this method to get the described behavior.

See also

``[filterAcceptsRow()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsRow)``[setFilterFixedString()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterFixedString)``[setFilterRegularExpression()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterRegularExpression)``[setFilterWildcard()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterWildcard)

filterAcceptsRow (source_row , source_parent )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsRow) Parameters :

- 

source_row  – int

- 

source_parent  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Return type :

bool

Returns `true` if the item in the row indicated by the given `source_row` and `source_parent` should be included in the model; otherwise returns false.

The default implementation returns `true` if the value held by the relevant item matches the filter string, wildcard string or regular expression.

Note

By default, the ``[DisplayRole](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.ItemDataRole)  is used to determine if the row should be accepted or not. This can be changed by setting the ``[filterRole()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id5)  property.

See also

``[filterAcceptsColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsColumn)``[setFilterFixedString()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterFixedString)``[setFilterRegularExpression()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterRegularExpression)``[setFilterWildcard()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterWildcard)

filterCaseSensitivity ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id2) Return type :

``[CaseSensitivity](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.CaseSensitivity)

See also

``[setFilterCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterCaseSensitivity)

Getter of property ``[filterCaseSensitivityᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterCaseSensitivity)  .

filterCaseSensitivityChanged (filterCaseSensitivity )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterCaseSensitivityChanged) Parameters :

filterCaseSensitivity  – ``[CaseSensitivity](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.CaseSensitivity)

This signal is emitted when the case sensitivity of the filter changes to `filterCaseSensitivity`.

Notification signal of property ``[filterCaseSensitivityᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterCaseSensitivity)  .

filterKeyColumn ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id3) Return type :

int

See also

``[setFilterKeyColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterKeyColumn)

Getter of property ``[filterKeyColumnᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterKeyColumn)  .

filterRegularExpression ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id4) Return type :

``[QRegularExpression](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QRegularExpression.html#PySide6.QtCore.QRegularExpression)

See also

``[setFilterRegularExpression()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterRegularExpression)

Getter of property ``[filterRegularExpressionᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterRegularExpression)  .

filterRole ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id5) Return type :

int

See also

``[setFilterRole()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterRole)

Getter of property ``[filterRoleᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterRole)  .

filterRoleChanged (filterRole )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterRoleChanged) Parameters :

filterRole  – int

This signal is emitted when the filter role changes to `filterRole`.

Notification signal of property ``[filterRoleᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterRole)  .

invalidate ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.invalidate)

Invalidates the current sorting and filtering.

> 

See also

``[beginFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.beginFilterChange)``[endFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.endFilterChange)

invalidateColumnsFilter ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.invalidateColumnsFilter)

Note

This function is deprecated.

use ``[beginFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.beginFilterChange)  and ``[endFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.endFilterChange)  ( ``[Rows](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.Direction)  ) instead.

Invalidates the current filtering for the columns.

This function should be called if you are implementing custom filtering (by ``[filterAcceptsColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsColumn)  ), and your filter parameters have changed. This differs from ``[invalidateFilter()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.invalidateFilter)  in that it will not invoke ``[filterAcceptsRow()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsRow)  , but only ``[filterAcceptsColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsColumn)  . You can use this instead of ``[invalidateFilter()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.invalidateFilter)  if you want to hide or show a column where the rows don’t change.

Before your filter parameters change, call ``[beginFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.beginFilterChange)  .

> 

See also

``[invalidate()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.invalidate)``[invalidateRowsFilter()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.invalidateRowsFilter)``[beginFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.beginFilterChange)

invalidateFilter ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.invalidateFilter)

Note

This function is deprecated.

Warning

This section contains snippets that were automatically translated from C++ to Python and may contain errors.

use ``[beginFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.beginFilterChange)  and ``[endFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.endFilterChange)  instead.

Invalidates the current filtering.

This function should be called if you are implementing custom filtering (e.g. ``[filterAcceptsRow()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsRow)  ), and your filter parameters have changed.

Before your filter parameters change, call ``[beginFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.beginFilterChange)  .

> 

```
def setFilterMaximumDate(self, date):

    beginFilterChange()
    maxDate = date
    endFilterChange(QSortFilterProxyModel.Direction.Rows)
```

See also

``[invalidate()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.invalidate)``[invalidateColumnsFilter()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.invalidateColumnsFilter)``[invalidateRowsFilter()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.invalidateRowsFilter)``[beginFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.beginFilterChange)

invalidateRowsFilter ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.invalidateRowsFilter)

Note

This function is deprecated.

use ``[beginFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.beginFilterChange)  and ``[endFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.endFilterChange)  ( ``[Columns](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.Direction)  ) instead.

Invalidates the current filtering for the rows.

This function should be called if you are implementing custom filtering (by ``[filterAcceptsRow()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsRow)  ), and your filter parameters have changed. This differs from ``[invalidateFilter()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.invalidateFilter)  in that it will not invoke ``[filterAcceptsColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsColumn)  , but only ``[filterAcceptsRow()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterAcceptsRow)  . You can use this instead of ``[invalidateFilter()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.invalidateFilter)  if you want to hide or show a row where the columns don’t change.

Before your filter parameters change, call ``[beginFilterChange()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.beginFilterChange)  .

> 

See also

``[invalidate()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.invalidate)``[invalidateFilter()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.invalidateFilter)``[invalidateColumnsFilter()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.invalidateColumnsFilter)

isRecursiveFilteringEnabled ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.isRecursiveFilteringEnabled) Return type :

bool

Getter of property ``[recursiveFilteringEnabledᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.recursiveFilteringEnabled)  .

isSortLocaleAware ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id6) Return type :

bool

Getter of property ``[isSortLocaleAwareᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.isSortLocaleAware)  .

lessThan (source_left , source_right )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.lessThan) Parameters :

- 

source_left  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

- 

source_right  – ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)

Return type :

bool

Returns `true` if the value of the item referred to by the given index `source_left` is less than the value of the item referred to by the given index `source_right`, otherwise returns `false`.

This function is used as the `operator<` when sorting, and uses `compareData()` .

Comparison of `QString` s is case sensitive by default; this can be changed using the ``[sortCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id7)  property.

By default, the ``[DisplayRole](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.ItemDataRole)  associated with the ``[QModelIndex](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QModelIndex.html#PySide6.QtCore.QModelIndex)  es is used for comparisons. This can be changed by setting the ``[sortRole()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id8)  property.

Note

The indices passed in correspond to the source model.

See also

``[sortRole()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id8)``[sortCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id7)``[dynamicSortFilter()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id1)

recursiveFilteringEnabledChanged (recursiveFilteringEnabled )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.recursiveFilteringEnabledChanged) Parameters :

recursiveFilteringEnabled  – bool

This signal is emitted when the recursive filter setting is changed to `recursiveFilteringEnabled`.

Notification signal of property ``[recursiveFilteringEnabledᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.recursiveFilteringEnabled)  .

setAutoAcceptChildRows (accept )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setAutoAcceptChildRows) Parameters :

accept  – bool

See also

``[autoAcceptChildRows()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id0)

Setter of property ``[autoAcceptChildRowsᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.autoAcceptChildRows)  .

setDynamicSortFilter (enable )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setDynamicSortFilter) Parameters :

enable  – bool

See also

``[dynamicSortFilter()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id1)

Setter of property ``[dynamicSortFilterᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.dynamicSortFilter)  .

setFilterCaseSensitivity (cs )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterCaseSensitivity) Parameters :

cs  – ``[CaseSensitivity](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.CaseSensitivity)

See also

``[filterCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id2)

Setter of property ``[filterCaseSensitivityᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterCaseSensitivity)  .

setFilterFixedString (pattern )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterFixedString) Parameters :

pattern  – str

Sets the fixed string used to filter the contents of the source model to the given `pattern`.

This method will reset the regular expression options but respect case sensitivity.

Note

Calling this method updates the regular expression, thereby breaking the binding for ``[filterRegularExpression()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id4)  . However it has no effect on the ``[filterCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id2)  bindings.

See also

``[setFilterCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterCaseSensitivity)``[setFilterRegularExpression()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterRegularExpression)``[setFilterWildcard()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterWildcard)``[filterRegularExpression()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id4)

setFilterKeyColumn (column )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterKeyColumn) Parameters :

column  – int

See also

``[filterKeyColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id3)

Setter of property ``[filterKeyColumnᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterKeyColumn)  .

setFilterRegularExpression (regularExpression )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterRegularExpression) Parameters :

regularExpression  – ``[QRegularExpression](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QRegularExpression.html#PySide6.QtCore.QRegularExpression)

See also

``[filterRegularExpression()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id4)

Setter of property ``[filterRegularExpressionᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterRegularExpression)  .

setFilterRegularExpression (pattern ) Parameters :

pattern  – str

Sets the regular expression used to filter the contents of the source model to `pattern`.

This method should be preferred for new code as it will use ``[QRegularExpression](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QRegularExpression.html#PySide6.QtCore.QRegularExpression)  internally.

This method will reset the regular expression options but respect case sensitivity.

Note

Calling this method updates the regular expression, thereby breaking the binding for ``[filterRegularExpression()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id4)  . However it has no effect on the ``[filterCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id2)  bindings.

See also

``[setFilterCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterCaseSensitivity)``[setFilterWildcard()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterWildcard)``[setFilterFixedString()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterFixedString)``[filterRegularExpression()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id4)

setFilterRole (role )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterRole) Parameters :

role  – int

See also

``[filterRole()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id5)

Setter of property ``[filterRoleᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.filterRole)  .

setFilterWildcard (pattern )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterWildcard) Parameters :

pattern  – str

Sets the wildcard expression used to filter the contents of the source model to the given `pattern`.

This method will reset the regular expression options but respect case sensitivity.

Note

Calling this method updates the regular expression, thereby breaking the binding for ``[filterRegularExpression()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id4)  . However it has no effect on the ``[filterCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id2)  bindings.

See also

``[setFilterCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterCaseSensitivity)``[setFilterRegularExpression()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterRegularExpression)``[setFilterFixedString()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setFilterFixedString)``[filterRegularExpression()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id4)

setRecursiveFilteringEnabled (recursive )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setRecursiveFilteringEnabled) Parameters :

recursive  – bool

See also

``[isRecursiveFilteringEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.isRecursiveFilteringEnabled)

Setter of property ``[recursiveFilteringEnabledᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.recursiveFilteringEnabled)  .

setSortCaseSensitivity (cs )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setSortCaseSensitivity) Parameters :

cs  – ``[CaseSensitivity](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.CaseSensitivity)

See also

``[sortCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id7)

Setter of property ``[sortCaseSensitivityᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortCaseSensitivity)  .

setSortLocaleAware (on )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setSortLocaleAware) Parameters :

on  – bool

See also

``[isSortLocaleAware()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id6)

Setter of property ``[isSortLocaleAwareᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.isSortLocaleAware)  .

setSortRole (role )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setSortRole) Parameters :

role  – int

See also

``[sortRole()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id8)

Setter of property ``[sortRoleᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortRole)  .

sortCaseSensitivity ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id7) Return type :

``[CaseSensitivity](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.CaseSensitivity)

See also

``[setSortCaseSensitivity()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setSortCaseSensitivity)

Getter of property ``[sortCaseSensitivityᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortCaseSensitivity)  .

sortCaseSensitivityChanged (sortCaseSensitivity )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortCaseSensitivityChanged) Parameters :

sortCaseSensitivity  – ``[CaseSensitivity](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.CaseSensitivity)

This signal is emitted when the case sensitivity for sorting changes to `sortCaseSensitivity`.

Notification signal of property ``[sortCaseSensitivityᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortCaseSensitivity)  .

sortColumn ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortColumn) Return type :

int

Returns the column currently used for sorting

This returns the most recently used sort column. The default value is -1, which means that this proxy model does not sort.

> 

See also

`sort()`

sortLocaleAwareChanged (sortLocaleAware )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortLocaleAwareChanged) Parameters :

sortLocaleAware  – bool

This signal is emitted when the locale aware setting changes to `sortLocaleAware`.

Notification signal of property ``[isSortLocaleAwareᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.isSortLocaleAware)  .

sortOrder ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortOrder) Return type :

``[SortOrder](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.SortOrder)

Returns the order currently used for sorting

This returns the most recently used sort order. The default value is ``[AscendingOrder](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html#PySide6.QtCore.Qt.SortOrder)  .

> 

See also

`sort()`

sortRole ()[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#id8) Return type :

int

See also

``[setSortRole()](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.setSortRole)

Getter of property ``[sortRoleᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortRole)  .

sortRoleChanged (sortRole )[¶](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortRoleChanged) Parameters :

sortRole  – int

This signal is emitted when the sort role changes to `sortRole`.

Notification signal of property ``[sortRoleᅟ](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel.sortRole)  .
