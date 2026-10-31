<!--
source: https://doc.qt.io/qt-6/qtreeview.html
retrieved: 2026-10-31T21:19:02.936479+00:00
final_url: https://doc.qt.io/qt-6/qtreeview.html
content_type: text/html
-->

# QTreeView Class | Qt Widgets | Qt 6.12.0

[Back to Qt.io](https://www.qt.io/)

[Contact Us](https://www.qt.io/contact-us/)[Blog](https://blog.qt.io/)[Download Qt](https://www.qt.io/download/)

[https://doc.qt.io/](https://doc.qt.io/)

- 

  - English

- 

- [Qt Academy](https://www.qt.io/academy)

- [Archives](https://doc.qt.io/archives)

- [Snapshots](https://doc-snapshots.qt.io/)

Search

- [Qt 6.12](https://doc.qt.io/qt-6/index.html)

- [Qt Widgets](https://doc.qt.io/qt-6/qtwidgets-index.html)

- [C++ Classes](https://doc.qt.io/qt-6/qtwidgets-module.html)

- QTreeView

On this page

# QTreeView Class

The QTreeView class provides a default model/view implementation of a tree view. [More...](https://doc.qt.io/qt-6/qtreeview.html#details)

 Header:`#include <QTreeView>` CMake:`find_package(Qt6 REQUIRED COMPONENTS Widgets)`
`target_link_libraries(mytarget PRIVATE Qt6::Widgets)` qmake:`QT += widgets` Inherits:[QAbstractItemView](https://doc.qt.io/qt-6/qabstractitemview.html)  Inherited By:

[QHelpContentWidget](https://doc.qt.io/qt-6/qhelpcontentwidget.html)  and [QTreeWidget](https://doc.qt.io/qt-6/qtreewidget.html)

- [List of all members, including inherited members](https://doc.qt.io/qt-6/qtreeview-members.html)

## Properties[https://doc.qt.io/qt-6/qtreeview.html#properties](https://doc.qt.io/qt-6/qtreeview.html#properties)

- [allColumnsShowFocus](https://doc.qt.io/qt-6/qtreeview.html#allColumnsShowFocus-prop)  : bool

- [animated](https://doc.qt.io/qt-6/qtreeview.html#animated-prop)  : bool

- [autoExpandDelay](https://doc.qt.io/qt-6/qtreeview.html#autoExpandDelay-prop)  : int

- [expandsOnDoubleClick](https://doc.qt.io/qt-6/qtreeview.html#expandsOnDoubleClick-prop)  : bool

- [headerHidden](https://doc.qt.io/qt-6/qtreeview.html#headerHidden-prop)  : bool

- [indentation](https://doc.qt.io/qt-6/qtreeview.html#indentation-prop)  : int

- [itemsExpandable](https://doc.qt.io/qt-6/qtreeview.html#itemsExpandable-prop)  : bool

- [rootIsDecorated](https://doc.qt.io/qt-6/qtreeview.html#rootIsDecorated-prop)  : bool

- [sortingEnabled](https://doc.qt.io/qt-6/qtreeview.html#sortingEnabled-prop)  : bool

- [uniformRowHeights](https://doc.qt.io/qt-6/qtreeview.html#uniformRowHeights-prop)  : bool

- [wordWrap](https://doc.qt.io/qt-6/qtreeview.html#wordWrap-prop)  : bool

## Public Functions[https://doc.qt.io/qt-6/qtreeview.html#public-functions](https://doc.qt.io/qt-6/qtreeview.html#public-functions)

[QTreeView](https://doc.qt.io/qt-6/qtreeview.html#QTreeView) (QWidget * parent  = nullptr)  virtual [~QTreeView](https://doc.qt.io/qt-6/qtreeview.html#dtor.QTreeView) ()  bool [allColumnsShowFocus](https://doc.qt.io/qt-6/qtreeview.html#allColumnsShowFocus-prop) () const  int [autoExpandDelay](https://doc.qt.io/qt-6/qtreeview.html#autoExpandDelay-prop) () const  int [columnAt](https://doc.qt.io/qt-6/qtreeview.html#columnAt) (int x ) const  int [columnViewportPosition](https://doc.qt.io/qt-6/qtreeview.html#columnViewportPosition) (int column ) const  int [columnWidth](https://doc.qt.io/qt-6/qtreeview.html#columnWidth) (int column ) const  bool [expandsOnDoubleClick](https://doc.qt.io/qt-6/qtreeview.html#expandsOnDoubleClick-prop) () const  QHeaderView *[header](https://doc.qt.io/qt-6/qtreeview.html#header) () const  int [indentation](https://doc.qt.io/qt-6/qtreeview.html#indentation-prop) () const  QModelIndex [indexAbove](https://doc.qt.io/qt-6/qtreeview.html#indexAbove) (const QModelIndex & index ) const  QModelIndex [indexBelow](https://doc.qt.io/qt-6/qtreeview.html#indexBelow) (const QModelIndex & index ) const  bool [isAnimated](https://doc.qt.io/qt-6/qtreeview.html#animated-prop) () const  bool [isColumnHidden](https://doc.qt.io/qt-6/qtreeview.html#isColumnHidden) (int column ) const  bool [isExpanded](https://doc.qt.io/qt-6/qtreeview.html#isExpanded) (const QModelIndex & index ) const  bool [isFirstColumnSpanned](https://doc.qt.io/qt-6/qtreeview.html#isFirstColumnSpanned) (int row , const QModelIndex & parent ) const  bool [isHeaderHidden](https://doc.qt.io/qt-6/qtreeview.html#headerHidden-prop) () const  bool [isRowHidden](https://doc.qt.io/qt-6/qtreeview.html#isRowHidden) (int row , const QModelIndex & parent ) const  bool [isSortingEnabled](https://doc.qt.io/qt-6/qtreeview.html#sortingEnabled-prop) () const`(since 6.12)` QRect [itemDecorationRect](https://doc.qt.io/qt-6/qtreeview.html#itemDecorationRect) (const QModelIndex & index ) const  bool [itemsExpandable](https://doc.qt.io/qt-6/qtreeview.html#itemsExpandable-prop) () const  void [resetIndentation](https://doc.qt.io/qt-6/qtreeview.html#indentation-prop) ()  bool [rootIsDecorated](https://doc.qt.io/qt-6/qtreeview.html#rootIsDecorated-prop) () const  void [setAllColumnsShowFocus](https://doc.qt.io/qt-6/qtreeview.html#allColumnsShowFocus-prop) (bool enable )  void [setAnimated](https://doc.qt.io/qt-6/qtreeview.html#animated-prop) (bool enable )  void [setAutoExpandDelay](https://doc.qt.io/qt-6/qtreeview.html#autoExpandDelay-prop) (int delay )  void [setColumnHidden](https://doc.qt.io/qt-6/qtreeview.html#setColumnHidden) (int column , bool hide )  void [setColumnWidth](https://doc.qt.io/qt-6/qtreeview.html#setColumnWidth) (int column , int width )  void [setExpanded](https://doc.qt.io/qt-6/qtreeview.html#setExpanded) (const QModelIndex & index , bool expanded )  void [setExpandsOnDoubleClick](https://doc.qt.io/qt-6/qtreeview.html#expandsOnDoubleClick-prop) (bool enable )  void [setFirstColumnSpanned](https://doc.qt.io/qt-6/qtreeview.html#setFirstColumnSpanned) (int row , const QModelIndex & parent , bool span )  void [setHeader](https://doc.qt.io/qt-6/qtreeview.html#setHeader) (QHeaderView * header )  void [setHeaderHidden](https://doc.qt.io/qt-6/qtreeview.html#headerHidden-prop) (bool hide )  void [setIndentation](https://doc.qt.io/qt-6/qtreeview.html#indentation-prop) (int i )  void [setItemsExpandable](https://doc.qt.io/qt-6/qtreeview.html#itemsExpandable-prop) (bool enable )  void [setRootIsDecorated](https://doc.qt.io/qt-6/qtreeview.html#rootIsDecorated-prop) (bool show )  void [setRowHidden](https://doc.qt.io/qt-6/qtreeview.html#setRowHidden) (int row , const QModelIndex & parent , bool hide )  void [setSortingEnabled](https://doc.qt.io/qt-6/qtreeview.html#sortingEnabled-prop) (bool enable )  void [setTreePosition](https://doc.qt.io/qt-6/qtreeview.html#setTreePosition) (int index )  void [setUniformRowHeights](https://doc.qt.io/qt-6/qtreeview.html#uniformRowHeights-prop) (bool uniform )  void [setWordWrap](https://doc.qt.io/qt-6/qtreeview.html#wordWrap-prop) (bool on )  int [treePosition](https://doc.qt.io/qt-6/qtreeview.html#treePosition) () const  bool [uniformRowHeights](https://doc.qt.io/qt-6/qtreeview.html#uniformRowHeights-prop) () const  bool [wordWrap](https://doc.qt.io/qt-6/qtreeview.html#wordWrap-prop) () const

## Reimplemented Public Functions[https://doc.qt.io/qt-6/qtreeview.html#reimplemented-public-functions](https://doc.qt.io/qt-6/qtreeview.html#reimplemented-public-functions)

 virtual void [dataChanged](https://doc.qt.io/qt-6/qtreeview.html#dataChanged) (const QModelIndex & topLeft , const QModelIndex & bottomRight , const QList<int> & roles  = QList<int>()) override  virtual QModelIndex [indexAt](https://doc.qt.io/qt-6/qtreeview.html#indexAt) (const QPoint & point ) const override  virtual void [keyboardSearch](https://doc.qt.io/qt-6/qtreeview.html#keyboardSearch) (const QString & search ) override  virtual void [reset](https://doc.qt.io/qt-6/qtreeview.html#reset) () override  virtual void [scrollTo](https://doc.qt.io/qt-6/qtreeview.html#scrollTo) (const QModelIndex & index , QAbstractItemView::ScrollHint hint  = EnsureVisible) override  virtual void [selectAll](https://doc.qt.io/qt-6/qtreeview.html#selectAll) () override  virtual void [setModel](https://doc.qt.io/qt-6/qtreeview.html#setModel) (QAbstractItemModel * model ) override  virtual void [setRootIndex](https://doc.qt.io/qt-6/qtreeview.html#setRootIndex) (const QModelIndex & index ) override  virtual void [setSelectionModel](https://doc.qt.io/qt-6/qtreeview.html#setSelectionModel) (QItemSelectionModel * selectionModel ) override  virtual QRect [visualRect](https://doc.qt.io/qt-6/qtreeview.html#visualRect) (const QModelIndex & index ) const override

## Public Slots[https://doc.qt.io/qt-6/qtreeview.html#public-slots](https://doc.qt.io/qt-6/qtreeview.html#public-slots)

 void [collapse](https://doc.qt.io/qt-6/qtreeview.html#collapse) (const QModelIndex & index )  void [collapseAll](https://doc.qt.io/qt-6/qtreeview.html#collapseAll) ()  void [expand](https://doc.qt.io/qt-6/qtreeview.html#expand) (const QModelIndex & index )  void [expandAll](https://doc.qt.io/qt-6/qtreeview.html#expandAll) ()  void [expandRecursively](https://doc.qt.io/qt-6/qtreeview.html#expandRecursively) (const QModelIndex & index , int depth  = -1)  void [expandToDepth](https://doc.qt.io/qt-6/qtreeview.html#expandToDepth) (int depth )  void [hideColumn](https://doc.qt.io/qt-6/qtreeview.html#hideColumn) (int column )  void [resizeColumnToContents](https://doc.qt.io/qt-6/qtreeview.html#resizeColumnToContents) (int column )  void [showColumn](https://doc.qt.io/qt-6/qtreeview.html#showColumn) (int column )  void [sortByColumn](https://doc.qt.io/qt-6/qtreeview.html#sortByColumn) (int column , Qt::SortOrder order )

## Signals[https://doc.qt.io/qt-6/qtreeview.html#signals](https://doc.qt.io/qt-6/qtreeview.html#signals)

 void [collapsed](https://doc.qt.io/qt-6/qtreeview.html#collapsed) (const QModelIndex & index )  void [expanded](https://doc.qt.io/qt-6/qtreeview.html#expanded) (const QModelIndex & index )

## Protected Functions[https://doc.qt.io/qt-6/qtreeview.html#protected-functions](https://doc.qt.io/qt-6/qtreeview.html#protected-functions)

 virtual void [drawBranches](https://doc.qt.io/qt-6/qtreeview.html#drawBranches) (QPainter * painter , const QRect & rect , const QModelIndex & index ) const  virtual void [drawRow](https://doc.qt.io/qt-6/qtreeview.html#drawRow) (QPainter * painter , const QStyleOptionViewItem & option , const QModelIndex & index ) const  void [drawTree](https://doc.qt.io/qt-6/qtreeview.html#drawTree) (QPainter * painter , const QRegion & region ) const  int [indexRowSizeHint](https://doc.qt.io/qt-6/qtreeview.html#indexRowSizeHint) (const QModelIndex & index ) const  int [rowHeight](https://doc.qt.io/qt-6/qtreeview.html#rowHeight) (const QModelIndex & index ) const

## Reimplemented Protected Functions[https://doc.qt.io/qt-6/qtreeview.html#reimplemented-protected-functions](https://doc.qt.io/qt-6/qtreeview.html#reimplemented-protected-functions)

 virtual void [changeEvent](https://doc.qt.io/qt-6/qtreeview.html#changeEvent) (QEvent * event ) override  virtual void [currentChanged](https://doc.qt.io/qt-6/qtreeview.html#currentChanged) (const QModelIndex & current , const QModelIndex & previous ) override  virtual void [dragMoveEvent](https://doc.qt.io/qt-6/qtreeview.html#dragMoveEvent) (QDragMoveEvent * event ) override  virtual int [horizontalOffset](https://doc.qt.io/qt-6/qtreeview.html#horizontalOffset) () const override  virtual bool [isIndexHidden](https://doc.qt.io/qt-6/qtreeview.html#isIndexHidden) (const QModelIndex & index ) const override  virtual void [keyPressEvent](https://doc.qt.io/qt-6/qtreeview.html#keyPressEvent) (QKeyEvent * event ) override  virtual void [mouseDoubleClickEvent](https://doc.qt.io/qt-6/qtreeview.html#mouseDoubleClickEvent) (QMouseEvent * event ) override  virtual void [mouseMoveEvent](https://doc.qt.io/qt-6/qtreeview.html#mouseMoveEvent) (QMouseEvent * event ) override  virtual void [mousePressEvent](https://doc.qt.io/qt-6/qtreeview.html#mousePressEvent) (QMouseEvent * event ) override  virtual void [mouseReleaseEvent](https://doc.qt.io/qt-6/qtreeview.html#mouseReleaseEvent) (QMouseEvent * event ) override  virtual QModelIndex [moveCursor](https://doc.qt.io/qt-6/qtreeview.html#moveCursor) (QAbstractItemView::CursorAction cursorAction , Qt::KeyboardModifiers modifiers ) override  virtual void [paintEvent](https://doc.qt.io/qt-6/qtreeview.html#paintEvent) (QPaintEvent * event ) override  virtual void [rowsAboutToBeRemoved](https://doc.qt.io/qt-6/qtreeview.html#rowsAboutToBeRemoved) (const QModelIndex & parent , int start , int end ) override  virtual void [rowsInserted](https://doc.qt.io/qt-6/qtreeview.html#rowsInserted) (const QModelIndex & parent , int start , int end ) override  virtual void [scrollContentsBy](https://doc.qt.io/qt-6/qtreeview.html#scrollContentsBy) (int dx , int dy ) override  virtual QModelIndexList [selectedIndexes](https://doc.qt.io/qt-6/qtreeview.html#selectedIndexes) () const override  virtual void [selectionChanged](https://doc.qt.io/qt-6/qtreeview.html#selectionChanged) (const QItemSelection & selected , const QItemSelection & deselected ) override  virtual void [setSelection](https://doc.qt.io/qt-6/qtreeview.html#setSelection) (const QRect & rect , QItemSelectionModel::SelectionFlags command ) override  virtual int [sizeHintForColumn](https://doc.qt.io/qt-6/qtreeview.html#sizeHintForColumn) (int column ) const override  virtual void [timerEvent](https://doc.qt.io/qt-6/qtreeview.html#timerEvent) (QTimerEvent * event ) override  virtual void [updateGeometries](https://doc.qt.io/qt-6/qtreeview.html#updateGeometries) () override  virtual int [verticalOffset](https://doc.qt.io/qt-6/qtreeview.html#verticalOffset) () const override  virtual bool [viewportEvent](https://doc.qt.io/qt-6/qtreeview.html#viewportEvent) (QEvent * event ) override  virtual QSize [viewportSizeHint](https://doc.qt.io/qt-6/qtreeview.html#viewportSizeHint) () const override  virtual QRegion [visualRegionForSelection](https://doc.qt.io/qt-6/qtreeview.html#visualRegionForSelection) (const QItemSelection & selection ) const override

## Protected Slots[https://doc.qt.io/qt-6/qtreeview.html#protected-slots](https://doc.qt.io/qt-6/qtreeview.html#protected-slots)

 void [columnCountChanged](https://doc.qt.io/qt-6/qtreeview.html#columnCountChanged) (int oldCount , int newCount )  void [columnMoved](https://doc.qt.io/qt-6/qtreeview.html#columnMoved) ()  void [columnResized](https://doc.qt.io/qt-6/qtreeview.html#columnResized) (int column , int oldSize , int newSize )  void [rowsRemoved](https://doc.qt.io/qt-6/qtreeview.html#rowsRemoved) (const QModelIndex & parent , int start , int end )

## Detailed Description[https://doc.qt.io/qt-6/qtreeview.html#details](https://doc.qt.io/qt-6/qtreeview.html#details)

A QTreeView implements a tree representation of items from a model. This class is used to provide standard hierarchical lists that were previously provided by the `QListView` class, but using the more flexible approach provided by Qt's model/view architecture.

The QTreeView class is one of the [Model/View Classes](https://doc.qt.io/qt-6/model-view-programming.html#the-model-view-classes)  and is part of Qt's [model/view framework](https://doc.qt.io/qt-6/model-view-programming.html) .

QTreeView implements the interfaces defined by the [QAbstractItemView](https://doc.qt.io/qt-6/qabstractitemview.html)  class to allow it to display data provided by models derived from the [QAbstractItemModel](https://doc.qt.io/qt-6/qabstractitemmodel.html)  class.

It is simple to construct a tree view displaying data from a model. In the following example, the contents of a directory are supplied by a [QFileSystemModel](https://doc.qt.io/qt-6/qfilesystemmodel.html)  and displayed as a tree:

[https://doc.qt.io/qt-6/qfilesystemmodel.html](https://doc.qt.io/qt-6/qfilesystemmodel.html)[https://doc.qt.io/qt-6/qfilesystemmodel.html](https://doc.qt.io/qt-6/qfilesystemmodel.html)[https://doc.qt.io/qt-6/qdir.html](https://doc.qt.io/qt-6/qdir.html)[https://doc.qt.io/qt-6/qtreeview.html](https://doc.qt.io/qt-6/qtreeview.html)[https://doc.qt.io/qt-6/qtreeview.html](https://doc.qt.io/qt-6/qtreeview.html)```
QFileSystemModel *model = new QFileSystemModel;
model->setRootPath(QDir::currentPath());
QTreeView *tree = new QTreeView(splitter);
tree->setModel(model);
```

The model/view architecture ensures that the contents of the tree view are updated as the model changes.

Items that have children can be in an expanded (children are visible) or collapsed (children are hidden) state. When this state changes a [collapsed](https://doc.qt.io/qt-6/qtreeview.html#collapsed) () or [expanded](https://doc.qt.io/qt-6/qtreeview.html#expanded) () signal is emitted with the model index of the relevant item.

The amount of indentation used to indicate levels of hierarchy is controlled by the [indentation](https://doc.qt.io/qt-6/qtreeview.html#indentation-prop)  property.

Headers in tree views are constructed using the [QHeaderView](https://doc.qt.io/qt-6/qheaderview.html)  class and can be hidden using `header()->hide()`. Note that each header is configured with its [stretchLastSection](https://doc.qt.io/qt-6/qheaderview.html#stretchLastSection-prop)  property set to true, ensuring that the view does not waste any of the space assigned to it for its header. If this value is set to true, this property will override the resize mode set on the last section in the header.

By default, all columns in a tree view are movable except the first. To disable movement of these columns, use [QHeaderView](https://doc.qt.io/qt-6/qheaderview.html) 's [setSectionsMovable](https://doc.qt.io/qt-6/qheaderview.html#setSectionsMovable) () function. For more information about rearranging sections, see [Moving Header Sections](https://doc.qt.io/qt-6/qheaderview.html#moving-header-sections) .

### Key Bindings[https://doc.qt.io/qt-6/qtreeview.html#key-bindings](https://doc.qt.io/qt-6/qtreeview.html#key-bindings)

QTreeView supports a set of key bindings that enable the user to navigate in the view and interact with the contents of items:

Key Action Up Moves the cursor to the item in the same column on the previous row. If the parent of the current item has no more rows to navigate to, the cursor moves to the relevant item in the last row of the sibling that precedes the parent. Down Moves the cursor to the item in the same column on the next row. If the parent of the current item has no more rows to navigate to, the cursor moves to the relevant item in the first row of the sibling that follows the parent. Left Hides the children of the current item (if present) by collapsing a branch. Minus Same as Left. Right Reveals the children of the current item (if present) by expanding a branch. Plus Same as Right. Asterisk Expands the current item and all its children (if present). PageUp Moves the cursor up one page. PageDown Moves the cursor down one page. Home Moves the cursor to an item in the same column of the first row of the first top-level item in the model. End Moves the cursor to an item in the same column of the last row of the last top-level item in the model. F2 In editable models, this opens the current item for editing. The Escape key can be used to cancel the editing process and revert any changes to the data displayed.

### Improving Performance[https://doc.qt.io/qt-6/qtreeview.html#improving-performance](https://doc.qt.io/qt-6/qtreeview.html#improving-performance)

It is possible to give the view hints about the data it is handling in order to improve its performance when displaying large numbers of items. One approach that can be taken for views that are intended to display items with equal heights is to set the [uniformRowHeights](https://doc.qt.io/qt-6/qtreeview.html#uniformRowHeights-prop)  property to true.

See also [QListView](https://doc.qt.io/qt-6/qlistview.html) , [QTreeWidget](https://doc.qt.io/qt-6/qtreewidget.html) , [View Classes](https://doc.qt.io/qt-6/model-view-programming.html#view-classes) , [QAbstractItemModel](https://doc.qt.io/qt-6/qabstractitemmodel.html) , and [QAbstractItemView](https://doc.qt.io/qt-6/qabstractitemview.html) .

## Property Documentation

### allColumnsShowFocus  : bool[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n30](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n30)[https://doc.qt.io/qt-6/qtreeview.html#allColumnsShowFocus-prop](https://doc.qt.io/qt-6/qtreeview.html#allColumnsShowFocus-prop)

This property holds whether items should show keyboard focus using all columns

If this property is `true` all columns will show focus, otherwise only one column will show focus.

The default is false.

Access functions:

 bool allColumnsShowFocus () const  void setAllColumnsShowFocus (bool enable )

### animated  : bool[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n29](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n29)[https://doc.qt.io/qt-6/qtreeview.html#animated-prop](https://doc.qt.io/qt-6/qtreeview.html#animated-prop)

This property holds whether animations are enabled

If this property is `true` the treeview will animate expansion and collapsing of branches. If this property is `false`, the treeview will expand or collapse branches immediately without showing the animation.

By default, this property is `false`.

Access functions:

 bool isAnimated () const  void setAnimated (bool enable )

### autoExpandDelay  : int[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n23](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n23)[https://doc.qt.io/qt-6/qtreeview.html#autoExpandDelay-prop](https://doc.qt.io/qt-6/qtreeview.html#autoExpandDelay-prop)

This property holds the delay time before items in a tree are opened during a drag and drop operation.

This property holds the amount of time in milliseconds that the user must wait over a node before that node will automatically open. If the time is set to less then 0 then it will not be activated.

By default, this property has a value of -1, meaning that auto-expansion is disabled.

Access functions:

 int autoExpandDelay () const  void setAutoExpandDelay (int delay )

### expandsOnDoubleClick  : bool[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n33](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n33)[https://doc.qt.io/qt-6/qtreeview.html#expandsOnDoubleClick-prop](https://doc.qt.io/qt-6/qtreeview.html#expandsOnDoubleClick-prop)

This property holds whether the items can be expanded by double-clicking.

This property holds whether the user can expand and collapse items by double-clicking. The default value is true.

Access functions:

 bool expandsOnDoubleClick () const  void setExpandsOnDoubleClick (bool enable )

See also [itemsExpandable](https://doc.qt.io/qt-6/qtreeview.html#itemsExpandable-prop) .

### headerHidden  : bool[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n32](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n32)[https://doc.qt.io/qt-6/qtreeview.html#headerHidden-prop](https://doc.qt.io/qt-6/qtreeview.html#headerHidden-prop)

This property holds whether the header is shown or not.

If this property is `true`, the header is not shown otherwise it is. The default value is false.

Access functions:

 bool isHeaderHidden () const  void setHeaderHidden (bool hide )

See also [header](https://doc.qt.io/qt-6/qtreeview.html#header) ().

### indentation  : int[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n24](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n24)[https://doc.qt.io/qt-6/qtreeview.html#indentation-prop](https://doc.qt.io/qt-6/qtreeview.html#indentation-prop)

indentation of the items in the tree view.

This property holds the indentation measured in pixels of the items for each level in the tree view. For top-level items, the indentation specifies the horizontal distance from the viewport edge to the items in the first column; for child items, it specifies their indentation from their parent items.

By default, the value of this property is style dependent. Thus, when the style changes, this property updates from it. Calling setIndentation() stops the updates, calling resetIndentation() will restore default behavior.

Access functions:

 int indentation () const  void setIndentation (int i )  void resetIndentation ()

### itemsExpandable  : bool[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n27](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n27)[https://doc.qt.io/qt-6/qtreeview.html#itemsExpandable-prop](https://doc.qt.io/qt-6/qtreeview.html#itemsExpandable-prop)

This property holds whether the items are expandable by the user.

This property holds whether the user can expand and collapse items interactively.

By default, this property is `true`.

Access functions:

 bool itemsExpandable () const  void setItemsExpandable (bool enable )

### rootIsDecorated  : bool[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n25](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n25)[https://doc.qt.io/qt-6/qtreeview.html#rootIsDecorated-prop](https://doc.qt.io/qt-6/qtreeview.html#rootIsDecorated-prop)

This property holds whether to show controls for expanding and collapsing top-level items

Items with children are typically shown with controls to expand and collapse them, allowing their children to be shown or hidden. If this property is false, these controls are not shown for top-level items. This can be used to make a single level tree structure appear like a simple list of items.

By default, this property is `true`.

Access functions:

 bool rootIsDecorated () const  void setRootIsDecorated (bool show )

### sortingEnabled  : bool[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n28](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n28)[https://doc.qt.io/qt-6/qtreeview.html#sortingEnabled-prop](https://doc.qt.io/qt-6/qtreeview.html#sortingEnabled-prop)

This property holds whether sorting is enabled

If this property is `true`, sorting is enabled for the tree; if the property is false, sorting is not enabled. The default value is false.

Note: In order to avoid performance issues, it is recommended that sorting is enabled after  inserting the items into the tree. Alternatively, you could also insert the items into a list before inserting the items into the tree.

Access functions:

 bool isSortingEnabled () const  void setSortingEnabled (bool enable )

See also [sortByColumn](https://doc.qt.io/qt-6/qtreeview.html#sortByColumn) ().

### uniformRowHeights  : bool[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n26](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n26)[https://doc.qt.io/qt-6/qtreeview.html#uniformRowHeights-prop](https://doc.qt.io/qt-6/qtreeview.html#uniformRowHeights-prop)

This property holds whether all items in the treeview have the same height

This property should only be set to true if it is guaranteed that all items in the view has the same height. This enables the view to do some optimizations.

The height is obtained from the first item in the view. It is updated when the data changes on that item.

Note: If the editor size hint is bigger than the cell size hint, then the size hint of the editor will be used.

By default, this property is `false`.

Access functions:

 bool uniformRowHeights () const  void setUniformRowHeights (bool uniform )

### wordWrap  : bool[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n31](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n31)[https://doc.qt.io/qt-6/qtreeview.html#wordWrap-prop](https://doc.qt.io/qt-6/qtreeview.html#wordWrap-prop)

This property holds the item text word-wrapping policy

If this property is `true` then the item text is wrapped where necessary at word-breaks; otherwise it is not wrapped at all. This property is `false` by default.

Note that even if wrapping is enabled, the cell will not be expanded to fit all text. Ellipsis will be inserted according to the current [textElideMode](https://doc.qt.io/qt-6/qabstractitemview.html#textElideMode-prop) .

Access functions:

 bool wordWrap () const  void setWordWrap (bool on )

## Member Function Documentation

### `[explicit]` QTreeView:: QTreeView ([QWidget](https://doc.qt.io/qt-6/qwidget.html)  * parent  = nullptr)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n36](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n36)[https://doc.qt.io/qt-6/qtreeview.html#QTreeView](https://doc.qt.io/qt-6/qtreeview.html#QTreeView)

Constructs a tree view with a parent  to represent a model's data. Use [setModel](https://doc.qt.io/qt-6/qtreeview.html#setModel) () to set the model.

See also [QAbstractItemModel](https://doc.qt.io/qt-6/qabstractitemmodel.html) .

### `[virtual noexcept]` QTreeView:: ~QTreeView ()[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n37](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n37)[https://doc.qt.io/qt-6/qtreeview.html#dtor.QTreeView](https://doc.qt.io/qt-6/qtreeview.html#dtor.QTreeView)

Destroys the tree view.

### `[override virtual protected]`void  QTreeView:: changeEvent ([QEvent](https://doc.qt.io/qt-6/qevent.html)  * event )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n154](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n154)[https://doc.qt.io/qt-6/qtreeview.html#changeEvent](https://doc.qt.io/qt-6/qtreeview.html#changeEvent)

Reimplements: [QFrame::changeEvent](https://doc.qt.io/qt-6/qframe.html#changeEvent) (QEvent *ev).

### `[slot]`void  QTreeView:: collapse (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n124](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n124)[https://doc.qt.io/qt-6/qtreeview.html#collapse](https://doc.qt.io/qt-6/qtreeview.html#collapse)

Collapses the model item specified by the index .

See also [collapsed](https://doc.qt.io/qt-6/qtreeview.html#collapsed) ().

### `[slot]`void  QTreeView:: collapseAll ()[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n129](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n129)[https://doc.qt.io/qt-6/qtreeview.html#collapseAll](https://doc.qt.io/qt-6/qtreeview.html#collapseAll)

Collapses all expanded items.

See also [expandAll](https://doc.qt.io/qt-6/qtreeview.html#expandAll) (), [expand](https://doc.qt.io/qt-6/qtreeview.html#expand) (), [collapse](https://doc.qt.io/qt-6/qtreeview.html#collapse) (), and [setExpanded](https://doc.qt.io/qt-6/qtreeview.html#setExpanded) ().

### `[signal]`void  QTreeView:: collapsed (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n118](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n118)[https://doc.qt.io/qt-6/qtreeview.html#collapsed](https://doc.qt.io/qt-6/qtreeview.html#collapsed)

This signal is emitted when the item specified by index  is collapsed.

### int  QTreeView:: columnAt (int x ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n68](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n68)[https://doc.qt.io/qt-6/qtreeview.html#columnAt](https://doc.qt.io/qt-6/qtreeview.html#columnAt)

Returns the column in the tree view whose header covers the x  coordinate given.

### `[protected slot]`void  QTreeView:: columnCountChanged (int oldCount , int newCount )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n134](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n134)[https://doc.qt.io/qt-6/qtreeview.html#columnCountChanged](https://doc.qt.io/qt-6/qtreeview.html#columnCountChanged)

Informs the tree view that the number of columns in the tree view has changed from oldCount  to newCount .

### `[protected slot]`void  QTreeView:: columnMoved ()[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n135](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n135)[https://doc.qt.io/qt-6/qtreeview.html#columnMoved](https://doc.qt.io/qt-6/qtreeview.html#columnMoved)

This slot is called whenever a column has been moved.

### `[protected slot]`void  QTreeView:: columnResized (int column , int oldSize , int newSize )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n133](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n133)[https://doc.qt.io/qt-6/qtreeview.html#columnResized](https://doc.qt.io/qt-6/qtreeview.html#columnResized)

This function is called whenever column 's size is changed in the header. oldSize  and newSize  give the previous size and the new size in pixels.

See also [setColumnWidth](https://doc.qt.io/qt-6/qtreeview.html#setColumnWidth) ().

### int  QTreeView:: columnViewportPosition (int column ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n65](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n65)[https://doc.qt.io/qt-6/qtreeview.html#columnViewportPosition](https://doc.qt.io/qt-6/qtreeview.html#columnViewportPosition)

Returns the horizontal position of the column  in the viewport.

### int  QTreeView:: columnWidth (int column ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n66](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n66)[https://doc.qt.io/qt-6/qtreeview.html#columnWidth](https://doc.qt.io/qt-6/qtreeview.html#columnWidth)

Returns the width of the column .

See also [resizeColumnToContents](https://doc.qt.io/qt-6/qtreeview.html#resizeColumnToContents) () and [setColumnWidth](https://doc.qt.io/qt-6/qtreeview.html#setColumnWidth) ().

### `[override virtual protected]`void  QTreeView:: currentChanged (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & current , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & previous )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n189](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n189)[https://doc.qt.io/qt-6/qtreeview.html#currentChanged](https://doc.qt.io/qt-6/qtreeview.html#currentChanged)

Reimplements: [QAbstractItemView::currentChanged](https://doc.qt.io/qt-6/qabstractitemview.html#currentChanged) (const QModelIndex &current, const QModelIndex &previous).

### `[override virtual]`void  QTreeView:: dataChanged (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & topLeft , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & bottomRight , const [QList](https://doc.qt.io/qt-6/qlist.html) < int > & roles  = QList<int>())[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n112](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n112)[https://doc.qt.io/qt-6/qtreeview.html#dataChanged](https://doc.qt.io/qt-6/qtreeview.html#dataChanged)

Reimplements: [QAbstractItemView::dataChanged](https://doc.qt.io/qt-6/qabstractitemview.html#dataChanged) (const QModelIndex &topLeft, const QModelIndex &bottomRight, const QList<int> &roles).

### `[override virtual protected]`void  QTreeView:: dragMoveEvent ([QDragMoveEvent](https://doc.qt.io/qt-6/qdragmoveevent.html)  * event )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n172](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n172)[https://doc.qt.io/qt-6/qtreeview.html#dragMoveEvent](https://doc.qt.io/qt-6/qtreeview.html#dragMoveEvent)

Reimplements: [QAbstractItemView::dragMoveEvent](https://doc.qt.io/qt-6/qabstractitemview.html#dragMoveEvent) (QDragMoveEvent *event).

### `[virtual protected]`void  QTreeView:: drawBranches ([QPainter](https://doc.qt.io/qt-6/qpainter.html)  * painter , const [QRect](https://doc.qt.io/qt-6/qrect.html)  & rect , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n162](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n162)[https://doc.qt.io/qt-6/qtreeview.html#drawBranches](https://doc.qt.io/qt-6/qtreeview.html#drawBranches)

Draws the branches in the tree view on the same row as the model item index , using the painter  given. The branches are drawn in the rectangle specified by rect .

### `[virtual protected]`void  QTreeView:: drawRow ([QPainter](https://doc.qt.io/qt-6/qpainter.html)  * painter , const [QStyleOptionViewItem](https://doc.qt.io/qt-6/qstyleoptionviewitem.html)  & option , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n159](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n159)[https://doc.qt.io/qt-6/qtreeview.html#drawRow](https://doc.qt.io/qt-6/qtreeview.html#drawRow)

Draws the row in the tree view that contains the model item index , using the painter  given. The option  controls how the item is displayed.

See also [setAlternatingRowColors](https://doc.qt.io/qt-6/qabstractitemview.html#alternatingRowColors-prop) ().

### `[protected]`void  QTreeView:: drawTree ([QPainter](https://doc.qt.io/qt-6/qpainter.html)  * painter , const [QRegion](https://doc.qt.io/qt-6/qregion.html)  & region ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n158](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n158)[https://doc.qt.io/qt-6/qtreeview.html#drawTree](https://doc.qt.io/qt-6/qtreeview.html#drawTree)

Draws the part of the tree intersecting the given region  using the specified painter .

See also [paintEvent](https://doc.qt.io/qt-6/qtreeview.html#paintEvent) ().

### `[slot]`void  QTreeView:: expand (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n123](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n123)[https://doc.qt.io/qt-6/qtreeview.html#expand](https://doc.qt.io/qt-6/qtreeview.html#expand)

Expands the model item specified by the index .

See also [expanded](https://doc.qt.io/qt-6/qtreeview.html#expanded) ().

### `[slot]`void  QTreeView:: expandAll ()[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n127](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n127)[https://doc.qt.io/qt-6/qtreeview.html#expandAll](https://doc.qt.io/qt-6/qtreeview.html#expandAll)

Expands all expandable items.

Note: This function will not try to [fetch more](https://doc.qt.io/qt-6/qabstractitemmodel.html#fetchMore)  data.

Warning: If the model contains a large number of items, this function will take some time to execute.

See also [collapseAll](https://doc.qt.io/qt-6/qtreeview.html#collapseAll) (), [expand](https://doc.qt.io/qt-6/qtreeview.html#expand) (), [collapse](https://doc.qt.io/qt-6/qtreeview.html#collapse) (), and [setExpanded](https://doc.qt.io/qt-6/qtreeview.html#setExpanded) ().

### `[slot]`void  QTreeView:: expandRecursively (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index , int depth  = -1)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n128](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n128)[https://doc.qt.io/qt-6/qtreeview.html#expandRecursively](https://doc.qt.io/qt-6/qtreeview.html#expandRecursively)

Expands the item at the given index  and all its children to the given depth . The depth  is relative to the given index . A depth  of -1 will expand all children, a depth  of 0 will only expand the given index .

Note: This function will not try to [fetch more](https://doc.qt.io/qt-6/qabstractitemmodel.html#fetchMore)  data.

Warning: If the model contains a large number of items, this function will take some time to execute.

See also [expandAll](https://doc.qt.io/qt-6/qtreeview.html#expandAll) ().

### `[slot]`void  QTreeView:: expandToDepth (int depth )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n130](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n130)[https://doc.qt.io/qt-6/qtreeview.html#expandToDepth](https://doc.qt.io/qt-6/qtreeview.html#expandToDepth)

Expands all expandable items to the given depth .

Note: This function will not try to [fetch more](https://doc.qt.io/qt-6/qabstractitemmodel.html#fetchMore)  data.

See also [expandAll](https://doc.qt.io/qt-6/qtreeview.html#expandAll) (), [collapseAll](https://doc.qt.io/qt-6/qtreeview.html#collapseAll) (), [expand](https://doc.qt.io/qt-6/qtreeview.html#expand) (), [collapse](https://doc.qt.io/qt-6/qtreeview.html#collapse) (), and [setExpanded](https://doc.qt.io/qt-6/qtreeview.html#setExpanded) ().

### `[signal]`void  QTreeView:: expanded (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n117](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n117)[https://doc.qt.io/qt-6/qtreeview.html#expanded](https://doc.qt.io/qt-6/qtreeview.html#expanded)

This signal is emitted when the item specified by index  is expanded.

See also [setExpanded](https://doc.qt.io/qt-6/qtreeview.html#setExpanded) ().

### [QHeaderView](https://doc.qt.io/qt-6/qheaderview.html)  *QTreeView:: header () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n43](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n43)[https://doc.qt.io/qt-6/qtreeview.html#header](https://doc.qt.io/qt-6/qtreeview.html#header)

Returns the header for the tree view.

See also [setHeader](https://doc.qt.io/qt-6/qtreeview.html#setHeader) () and [QAbstractItemModel::headerData](https://doc.qt.io/qt-6/qabstractitemmodel.html#headerData) ().

### `[slot]`void  QTreeView:: hideColumn (int column )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n121](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n121)[https://doc.qt.io/qt-6/qtreeview.html#hideColumn](https://doc.qt.io/qt-6/qtreeview.html#hideColumn)

Hides the column  given.

Note: This function should only be called after the model has been initialized, as the view needs to know the number of columns in order to hide column .

See also [showColumn](https://doc.qt.io/qt-6/qtreeview.html#showColumn) () and [setColumnHidden](https://doc.qt.io/qt-6/qtreeview.html#setColumnHidden) ().

### `[override virtual protected]`int  QTreeView:: horizontalOffset () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n147](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n147)[https://doc.qt.io/qt-6/qtreeview.html#horizontalOffset](https://doc.qt.io/qt-6/qtreeview.html#horizontalOffset)

Reimplements: [QAbstractItemView::horizontalOffset](https://doc.qt.io/qt-6/qabstractitemview.html#horizontalOffset) () const.

Returns the horizontal offset of the items in the treeview.

Note that the tree view uses the horizontal header section positions to determine the positions of columns in the view.

See also [verticalOffset](https://doc.qt.io/qt-6/qtreeview.html#verticalOffset) ().

### [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  QTreeView:: indexAbove (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n106](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n106)[https://doc.qt.io/qt-6/qtreeview.html#indexAbove](https://doc.qt.io/qt-6/qtreeview.html#indexAbove)

Returns the model index of the item above index .

### `[override virtual]`[QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  QTreeView:: indexAt (const [QPoint](https://doc.qt.io/qt-6/qpoint.html)  & point ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n105](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n105)[https://doc.qt.io/qt-6/qtreeview.html#indexAt](https://doc.qt.io/qt-6/qtreeview.html#indexAt)

Reimplements: [QAbstractItemView::indexAt](https://doc.qt.io/qt-6/qabstractitemview.html#indexAt) (const QPoint &point) const.

### [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  QTreeView:: indexBelow (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n107](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n107)[https://doc.qt.io/qt-6/qtreeview.html#indexBelow](https://doc.qt.io/qt-6/qtreeview.html#indexBelow)

Returns the model index of the item below index .

### `[protected]`int  QTreeView:: indexRowSizeHint (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n181](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n181)[https://doc.qt.io/qt-6/qtreeview.html#indexRowSizeHint](https://doc.qt.io/qt-6/qtreeview.html#indexRowSizeHint)

Returns the size hint for the row indicated by index .

See also [sizeHintForColumn](https://doc.qt.io/qt-6/qtreeview.html#sizeHintForColumn) () and [uniformRowHeights](https://doc.qt.io/qt-6/qtreeview.html#uniformRowHeights-prop) ().

### bool  QTreeView:: isColumnHidden (int column ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n70](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n70)[https://doc.qt.io/qt-6/qtreeview.html#isColumnHidden](https://doc.qt.io/qt-6/qtreeview.html#isColumnHidden)

Returns `true` if the column  is hidden; otherwise returns `false`.

See also [hideColumn](https://doc.qt.io/qt-6/qtreeview.html#hideColumn) () and [isRowHidden](https://doc.qt.io/qt-6/qtreeview.html#isRowHidden) ().

### bool  QTreeView:: isExpanded (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n82](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n82)[https://doc.qt.io/qt-6/qtreeview.html#isExpanded](https://doc.qt.io/qt-6/qtreeview.html#isExpanded)

Returns `true` if the model item index  is expanded; otherwise returns false.

See also [expand](https://doc.qt.io/qt-6/qtreeview.html#expand) (), [expanded](https://doc.qt.io/qt-6/qtreeview.html#expanded) (), and [setExpanded](https://doc.qt.io/qt-6/qtreeview.html#setExpanded) ().

### bool  QTreeView:: isFirstColumnSpanned (int row , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n79](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n79)[https://doc.qt.io/qt-6/qtreeview.html#isFirstColumnSpanned](https://doc.qt.io/qt-6/qtreeview.html#isFirstColumnSpanned)

Returns `true` if the item in first column in the given row  of the parent  is spanning all the columns; otherwise returns `false`.

See also [setFirstColumnSpanned](https://doc.qt.io/qt-6/qtreeview.html#setFirstColumnSpanned) ().

### `[override virtual protected]`bool  QTreeView:: isIndexHidden (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n186](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n186)[https://doc.qt.io/qt-6/qtreeview.html#isIndexHidden](https://doc.qt.io/qt-6/qtreeview.html#isIndexHidden)

Reimplements: [QAbstractItemView::isIndexHidden](https://doc.qt.io/qt-6/qabstractitemview.html#isIndexHidden) (const QModelIndex &index) const.

### bool  QTreeView:: isRowHidden (int row , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n76](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n76)[https://doc.qt.io/qt-6/qtreeview.html#isRowHidden](https://doc.qt.io/qt-6/qtreeview.html#isRowHidden)

Returns `true` if the item in the given row  of the parent  is hidden; otherwise returns `false`.

See also [setRowHidden](https://doc.qt.io/qt-6/qtreeview.html#setRowHidden) () and [isColumnHidden](https://doc.qt.io/qt-6/qtreeview.html#isColumnHidden) ().

### `[since 6.12]`[QRect](https://doc.qt.io/qt-6/qrect.html)  QTreeView:: itemDecorationRect (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n103](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n103)[https://doc.qt.io/qt-6/qtreeview.html#itemDecorationRect](https://doc.qt.io/qt-6/qtreeview.html#itemDecorationRect)

Returns the rectangle occupied by the expand/collapse indicator of the item at index . If the item has no such indicator, for example because it has no children or because root decoration is disabled, the returned rectangle is invalid. An invalid index  also returns an invalid rectangle.

This function was introduced in Qt 6.12.

See also [visualRect](https://doc.qt.io/qt-6/qtreeview.html#visualRect) () and [QStyle::SE_TreeViewDisclosureItem](https://doc.qt.io/qt-6/qstyle.html#SubElement-enum) .

### `[override virtual protected]`void  QTreeView:: keyPressEvent ([QKeyEvent](https://doc.qt.io/qt-6/qkeyevent.html)  * event )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n170](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n170)[https://doc.qt.io/qt-6/qtreeview.html#keyPressEvent](https://doc.qt.io/qt-6/qtreeview.html#keyPressEvent)

Reimplements: [QAbstractItemView::keyPressEvent](https://doc.qt.io/qt-6/qabstractitemview.html#keyPressEvent) (QKeyEvent *event).

### `[override virtual]`void  QTreeView:: keyboardSearch (const [QString](https://doc.qt.io/qt-6/qstring.html)  & search )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n100](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n100)[https://doc.qt.io/qt-6/qtreeview.html#keyboardSearch](https://doc.qt.io/qt-6/qtreeview.html#keyboardSearch)

Reimplements: [QAbstractItemView::keyboardSearch](https://doc.qt.io/qt-6/qabstractitemview.html#keyboardSearch) (const QString &search).

### `[override virtual protected]`void  QTreeView:: mouseDoubleClickEvent ([QMouseEvent](https://doc.qt.io/qt-6/qmouseevent.html)  * event )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n168](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n168)[https://doc.qt.io/qt-6/qtreeview.html#mouseDoubleClickEvent](https://doc.qt.io/qt-6/qtreeview.html#mouseDoubleClickEvent)

Reimplements: [QAbstractItemView::mouseDoubleClickEvent](https://doc.qt.io/qt-6/qabstractitemview.html#mouseDoubleClickEvent) (QMouseEvent *event).

### `[override virtual protected]`void  QTreeView:: mouseMoveEvent ([QMouseEvent](https://doc.qt.io/qt-6/qmouseevent.html)  * event )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n169](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n169)[https://doc.qt.io/qt-6/qtreeview.html#mouseMoveEvent](https://doc.qt.io/qt-6/qtreeview.html#mouseMoveEvent)

Reimplements: [QAbstractItemView::mouseMoveEvent](https://doc.qt.io/qt-6/qabstractitemview.html#mouseMoveEvent) (QMouseEvent *event).

### `[override virtual protected]`void  QTreeView:: mousePressEvent ([QMouseEvent](https://doc.qt.io/qt-6/qmouseevent.html)  * event )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n166](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n166)[https://doc.qt.io/qt-6/qtreeview.html#mousePressEvent](https://doc.qt.io/qt-6/qtreeview.html#mousePressEvent)

Reimplements: [QAbstractItemView::mousePressEvent](https://doc.qt.io/qt-6/qabstractitemview.html#mousePressEvent) (QMouseEvent *event).

### `[override virtual protected]`void  QTreeView:: mouseReleaseEvent ([QMouseEvent](https://doc.qt.io/qt-6/qmouseevent.html)  * event )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n167](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n167)[https://doc.qt.io/qt-6/qtreeview.html#mouseReleaseEvent](https://doc.qt.io/qt-6/qtreeview.html#mouseReleaseEvent)

Reimplements: [QAbstractItemView::mouseReleaseEvent](https://doc.qt.io/qt-6/qabstractitemview.html#mouseReleaseEvent) (QMouseEvent *event).

### `[override virtual protected]`[QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  QTreeView:: moveCursor ([QAbstractItemView::CursorAction](https://doc.qt.io/qt-6/qabstractitemview.html#CursorAction-enum) cursorAction , [Qt::KeyboardModifiers](https://doc.qt.io/qt-6/qt.html#KeyboardModifier-enum) modifiers )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n146](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n146)[https://doc.qt.io/qt-6/qtreeview.html#moveCursor](https://doc.qt.io/qt-6/qtreeview.html#moveCursor)

Reimplements: [QAbstractItemView::moveCursor](https://doc.qt.io/qt-6/qabstractitemview.html#moveCursor) (QAbstractItemView::CursorAction cursorAction, Qt::KeyboardModifiers modifiers).

Move the cursor in the way described by cursorAction , using the information provided by the button modifiers .

### `[override virtual protected]`void  QTreeView:: paintEvent ([QPaintEvent](https://doc.qt.io/qt-6/qpaintevent.html)  * event )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n156](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n156)[https://doc.qt.io/qt-6/qtreeview.html#paintEvent](https://doc.qt.io/qt-6/qtreeview.html#paintEvent)

Reimplements: [QAbstractScrollArea::paintEvent](https://doc.qt.io/qt-6/qabstractscrollarea.html#paintEvent) (QPaintEvent *event).

### `[override virtual]`void  QTreeView:: reset ()[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n110](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n110)[https://doc.qt.io/qt-6/qtreeview.html#reset](https://doc.qt.io/qt-6/qtreeview.html#reset)

Reimplements: [QAbstractItemView::reset](https://doc.qt.io/qt-6/qabstractitemview.html#reset) ().

### `[slot]`void  QTreeView:: resizeColumnToContents (int column )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n125](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n125)[https://doc.qt.io/qt-6/qtreeview.html#resizeColumnToContents](https://doc.qt.io/qt-6/qtreeview.html#resizeColumnToContents)

Resizes the column  given to the size of its contents.

See also [columnWidth](https://doc.qt.io/qt-6/qtreeview.html#columnWidth) (), [setColumnWidth](https://doc.qt.io/qt-6/qtreeview.html#setColumnWidth) (), [sizeHintForColumn](https://doc.qt.io/qt-6/qtreeview.html#sizeHintForColumn) (), and [QHeaderView::resizeContentsPrecision](https://doc.qt.io/qt-6/qheaderview.html#resizeContentsPrecision) ().

### `[protected]`int  QTreeView:: rowHeight (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n182](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n182)[https://doc.qt.io/qt-6/qtreeview.html#rowHeight](https://doc.qt.io/qt-6/qtreeview.html#rowHeight)

Returns the height of the row indicated by the given index .

See also [indexRowSizeHint](https://doc.qt.io/qt-6/qtreeview.html#indexRowSizeHint) ().

### `[override virtual protected]`void  QTreeView:: rowsAboutToBeRemoved (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent , int start , int end )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n144](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n144)[https://doc.qt.io/qt-6/qtreeview.html#rowsAboutToBeRemoved](https://doc.qt.io/qt-6/qtreeview.html#rowsAboutToBeRemoved)

Reimplements: [QAbstractItemView::rowsAboutToBeRemoved](https://doc.qt.io/qt-6/qabstractitemview.html#rowsAboutToBeRemoved) (const QModelIndex &parent, int start, int end).

Informs the view that the rows from the start  row to the end  row inclusive are about to removed from the given parent  model item.

### `[override virtual protected]`void  QTreeView:: rowsInserted (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent , int start , int end )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n143](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n143)[https://doc.qt.io/qt-6/qtreeview.html#rowsInserted](https://doc.qt.io/qt-6/qtreeview.html#rowsInserted)

Reimplements: [QAbstractItemView::rowsInserted](https://doc.qt.io/qt-6/qabstractitemview.html#rowsInserted) (const QModelIndex &parent, int start, int end).

Informs the view that the rows from the start  row to the end  row inclusive have been inserted into the parent  model item.

### `[protected slot]`void  QTreeView:: rowsRemoved (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent , int start , int end )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n137](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n137)[https://doc.qt.io/qt-6/qtreeview.html#rowsRemoved](https://doc.qt.io/qt-6/qtreeview.html#rowsRemoved)

Informs the view that the rows from the start  row to the end  row inclusive have been removed from the given parent  model item.

### `[override virtual protected]`void  QTreeView:: scrollContentsBy (int dx , int dy )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n142](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n142)[https://doc.qt.io/qt-6/qtreeview.html#scrollContentsBy](https://doc.qt.io/qt-6/qtreeview.html#scrollContentsBy)

Reimplements: [QAbstractScrollArea::scrollContentsBy](https://doc.qt.io/qt-6/qabstractscrollarea.html#scrollContentsBy) (int dx, int dy).

Scrolls the contents of the tree view by (dx , dy ).

### `[override virtual]`void  QTreeView:: scrollTo (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index , [QAbstractItemView::ScrollHint](https://doc.qt.io/qt-6/qabstractitemview.html#ScrollHint-enum) hint  = EnsureVisible)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n104](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n104)[https://doc.qt.io/qt-6/qtreeview.html#scrollTo](https://doc.qt.io/qt-6/qtreeview.html#scrollTo)

Reimplements: [QAbstractItemView::scrollTo](https://doc.qt.io/qt-6/qabstractitemview.html#scrollTo) (const QModelIndex &index, QAbstractItemView::ScrollHint hint).

Scroll the contents of the tree view until the given model item index  is visible. The hint  parameter specifies more precisely where the item should be located after the operation. If any of the parents of the model item are collapsed, they will be expanded to ensure that the model item is visible.

### `[override virtual]`void  QTreeView:: selectAll ()[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n114](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n114)[https://doc.qt.io/qt-6/qtreeview.html#selectAll](https://doc.qt.io/qt-6/qtreeview.html#selectAll)

Reimplements: [QAbstractItemView::selectAll](https://doc.qt.io/qt-6/qabstractitemview.html#selectAll) ().

### `[override virtual protected]`[QModelIndexList](https://doc.qt.io/qt-6/qmodelindex.html#QModelIndexList-typedef)  QTreeView:: selectedIndexes () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n152](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n152)[https://doc.qt.io/qt-6/qtreeview.html#selectedIndexes](https://doc.qt.io/qt-6/qtreeview.html#selectedIndexes)

Reimplements: [QAbstractItemView::selectedIndexes](https://doc.qt.io/qt-6/qabstractitemview.html#selectedIndexes) () const.

### `[override virtual protected]`void  QTreeView:: selectionChanged (const [QItemSelection](https://doc.qt.io/qt-6/qitemselection.html)  & selected , const [QItemSelection](https://doc.qt.io/qt-6/qitemselection.html)  & deselected )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n187](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n187)[https://doc.qt.io/qt-6/qtreeview.html#selectionChanged](https://doc.qt.io/qt-6/qtreeview.html#selectionChanged)

Reimplements: [QAbstractItemView::selectionChanged](https://doc.qt.io/qt-6/qabstractitemview.html#selectionChanged) (const QItemSelection &selected, const QItemSelection &deselected).

### void  QTreeView:: setColumnHidden (int column , bool hide )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n71](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n71)[https://doc.qt.io/qt-6/qtreeview.html#setColumnHidden](https://doc.qt.io/qt-6/qtreeview.html#setColumnHidden)

If hide  is true the column  is hidden, otherwise the column  is shown.

See also [isColumnHidden](https://doc.qt.io/qt-6/qtreeview.html#isColumnHidden) (), [hideColumn](https://doc.qt.io/qt-6/qtreeview.html#hideColumn) (), and [setRowHidden](https://doc.qt.io/qt-6/qtreeview.html#setRowHidden) ().

### void  QTreeView:: setColumnWidth (int column , int width )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n67](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n67)[https://doc.qt.io/qt-6/qtreeview.html#setColumnWidth](https://doc.qt.io/qt-6/qtreeview.html#setColumnWidth)

Sets the width of the given column  to the width  specified.

See also [columnWidth](https://doc.qt.io/qt-6/qtreeview.html#columnWidth) () and [resizeColumnToContents](https://doc.qt.io/qt-6/qtreeview.html#resizeColumnToContents) ().

### void  QTreeView:: setExpanded (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index , bool expanded )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n83](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n83)[https://doc.qt.io/qt-6/qtreeview.html#setExpanded](https://doc.qt.io/qt-6/qtreeview.html#setExpanded)

Sets the item referred to by index  to either collapse or expanded, depending on the value of expanded .

See also [expanded](https://doc.qt.io/qt-6/qtreeview.html#expanded) (), [expand](https://doc.qt.io/qt-6/qtreeview.html#expand) (), and [isExpanded](https://doc.qt.io/qt-6/qtreeview.html#isExpanded) ().

### void  QTreeView:: setFirstColumnSpanned (int row , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent , bool span )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n80](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n80)[https://doc.qt.io/qt-6/qtreeview.html#setFirstColumnSpanned](https://doc.qt.io/qt-6/qtreeview.html#setFirstColumnSpanned)

If span  is true the item in the first column in the row  with the given parent  is set to span all columns, otherwise all items on the row  are shown.

See also [isFirstColumnSpanned](https://doc.qt.io/qt-6/qtreeview.html#isFirstColumnSpanned) ().

### void  QTreeView:: setHeader ([QHeaderView](https://doc.qt.io/qt-6/qheaderview.html)  * header )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n44](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n44)[https://doc.qt.io/qt-6/qtreeview.html#setHeader](https://doc.qt.io/qt-6/qtreeview.html#setHeader)

Sets the header for the tree view, to the given header .

The view takes ownership over the given header  and deletes it when a new header is set.

See also [QAbstractItemModel::headerData](https://doc.qt.io/qt-6/qabstractitemmodel.html#headerData) ().

### `[override virtual]`void  QTreeView:: setModel ([QAbstractItemModel](https://doc.qt.io/qt-6/qabstractitemmodel.html)  * model )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n39](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n39)[https://doc.qt.io/qt-6/qtreeview.html#setModel](https://doc.qt.io/qt-6/qtreeview.html#setModel)

Reimplements: [QAbstractItemView::setModel](https://doc.qt.io/qt-6/qabstractitemview.html#setModel) (QAbstractItemModel *model).

### `[override virtual]`void  QTreeView:: setRootIndex (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n40](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n40)[https://doc.qt.io/qt-6/qtreeview.html#setRootIndex](https://doc.qt.io/qt-6/qtreeview.html#setRootIndex)

Reimplements: [QAbstractItemView::setRootIndex](https://doc.qt.io/qt-6/qabstractitemview.html#setRootIndex) (const QModelIndex &index).

### void  QTreeView:: setRowHidden (int row , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent , bool hide )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n77](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n77)[https://doc.qt.io/qt-6/qtreeview.html#setRowHidden](https://doc.qt.io/qt-6/qtreeview.html#setRowHidden)

If hide  is true the row  with the given parent  is hidden, otherwise the row  is shown.

See also [isRowHidden](https://doc.qt.io/qt-6/qtreeview.html#isRowHidden) () and [setColumnHidden](https://doc.qt.io/qt-6/qtreeview.html#setColumnHidden) ().

### `[override virtual protected]`void  QTreeView:: setSelection (const [QRect](https://doc.qt.io/qt-6/qrect.html)  & rect , [QItemSelectionModel::SelectionFlags](https://doc.qt.io/qt-6/qitemselectionmodel.html#SelectionFlag-enum) command )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n150](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n150)[https://doc.qt.io/qt-6/qtreeview.html#setSelection](https://doc.qt.io/qt-6/qtreeview.html#setSelection)

Reimplements: [QAbstractItemView::setSelection](https://doc.qt.io/qt-6/qabstractitemview.html#setSelection) (const QRect &rect, QItemSelectionModel::SelectionFlags flags).

Applies the selection command  to the items in or touched by the rectangle, rect .

See also [selectionCommand](https://doc.qt.io/qt-6/qabstractitemview.html#selectionCommand) ().

### `[override virtual]`void  QTreeView:: setSelectionModel ([QItemSelectionModel](https://doc.qt.io/qt-6/qitemselectionmodel.html)  * selectionModel )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n41](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n41)[https://doc.qt.io/qt-6/qtreeview.html#setSelectionModel](https://doc.qt.io/qt-6/qtreeview.html#setSelectionModel)

Reimplements: [QAbstractItemView::setSelectionModel](https://doc.qt.io/qt-6/qabstractitemview.html#setSelectionModel) (QItemSelectionModel *selectionModel).

### void  QTreeView:: setTreePosition (int index )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n97](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n97)[https://doc.qt.io/qt-6/qtreeview.html#setTreePosition](https://doc.qt.io/qt-6/qtreeview.html#setTreePosition)

This specifies that the tree structure should be placed at logical index index . If  set to -1 then the tree will always follow visual index 0.

See also [treePosition](https://doc.qt.io/qt-6/qtreeview.html#treePosition) (), [QHeaderView::swapSections](https://doc.qt.io/qt-6/qheaderview.html#swapSections) (), and [QHeaderView::moveSection](https://doc.qt.io/qt-6/qheaderview.html#moveSection) ().

### `[slot]`void  QTreeView:: showColumn (int column )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n122](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n122)[https://doc.qt.io/qt-6/qtreeview.html#showColumn](https://doc.qt.io/qt-6/qtreeview.html#showColumn)

Shows the given column  in the tree view.

See also [hideColumn](https://doc.qt.io/qt-6/qtreeview.html#hideColumn) () and [setColumnHidden](https://doc.qt.io/qt-6/qtreeview.html#setColumnHidden) ().

### `[override virtual protected]`int  QTreeView:: sizeHintForColumn (int column ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n180](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n180)[https://doc.qt.io/qt-6/qtreeview.html#sizeHintForColumn](https://doc.qt.io/qt-6/qtreeview.html#sizeHintForColumn)

Reimplements: [QAbstractItemView::sizeHintForColumn](https://doc.qt.io/qt-6/qabstractitemview.html#sizeHintForColumn) (int column) const.

Returns the size hint for the column 's width or -1 if there is no model.

If you need to set the width of a given column to a fixed value, call [QHeaderView::resizeSection](https://doc.qt.io/qt-6/qheaderview.html#resizeSection) () on the view's header.

If you reimplement this function in a subclass, note that the value you return is only used when [resizeColumnToContents](https://doc.qt.io/qt-6/qtreeview.html#resizeColumnToContents) () is called. In that case, if a larger column width is required by either the view's header or the item delegate, that width will be used instead.

See also [QWidget::sizeHint](https://doc.qt.io/qt-6/qwidget.html#sizeHint-prop) , [header](https://doc.qt.io/qt-6/qtreeview.html#header) (), and [QHeaderView::resizeContentsPrecision](https://doc.qt.io/qt-6/qheaderview.html#resizeContentsPrecision) ().

### `[slot]`void  QTreeView:: sortByColumn (int column , [Qt::SortOrder](https://doc.qt.io/qt-6/qt.html#SortOrder-enum) order )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n126](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n126)[https://doc.qt.io/qt-6/qtreeview.html#sortByColumn](https://doc.qt.io/qt-6/qtreeview.html#sortByColumn)

Sorts the model by the values in the given column  and order .

column  may be -1, in which case no sort indicator will be shown and the model will return to its natural, unsorted order. Note that not all models support this and may even crash in this case.

See also [sortingEnabled](https://doc.qt.io/qt-6/qtreeview.html#sortingEnabled-prop) .

### `[override virtual protected]`void  QTreeView:: timerEvent ([QTimerEvent](https://doc.qt.io/qt-6/qtimerevent.html)  * event )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n155](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n155)[https://doc.qt.io/qt-6/qtreeview.html#timerEvent](https://doc.qt.io/qt-6/qtreeview.html#timerEvent)

Reimplements: [QAbstractItemView::timerEvent](https://doc.qt.io/qt-6/qabstractitemview.html#timerEvent) (QTimerEvent *event).

### int  QTreeView:: treePosition () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n98](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n98)[https://doc.qt.io/qt-6/qtreeview.html#treePosition](https://doc.qt.io/qt-6/qtreeview.html#treePosition)

Return the logical index the tree is set on. If the return value is -1 then the tree is placed on the visual index 0.

See also [setTreePosition](https://doc.qt.io/qt-6/qtreeview.html#setTreePosition) ().

### `[override virtual protected]`void  QTreeView:: updateGeometries ()[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n176](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n176)[https://doc.qt.io/qt-6/qtreeview.html#updateGeometries](https://doc.qt.io/qt-6/qtreeview.html#updateGeometries)

Reimplements: [QAbstractItemView::updateGeometries](https://doc.qt.io/qt-6/qabstractitemview.html#updateGeometries) ().

### `[override virtual protected]`int  QTreeView:: verticalOffset () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n148](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n148)[https://doc.qt.io/qt-6/qtreeview.html#verticalOffset](https://doc.qt.io/qt-6/qtreeview.html#verticalOffset)

Reimplements: [QAbstractItemView::verticalOffset](https://doc.qt.io/qt-6/qabstractitemview.html#verticalOffset) () const.

Returns the vertical offset of the items in the tree view.

See also [horizontalOffset](https://doc.qt.io/qt-6/qtreeview.html#horizontalOffset) ().

### `[override virtual protected]`bool  QTreeView:: viewportEvent ([QEvent](https://doc.qt.io/qt-6/qevent.html)  * event )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n174](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n174)[https://doc.qt.io/qt-6/qtreeview.html#viewportEvent](https://doc.qt.io/qt-6/qtreeview.html#viewportEvent)

Reimplements: [QAbstractItemView::viewportEvent](https://doc.qt.io/qt-6/qabstractitemview.html#viewportEvent) (QEvent *event).

### `[override virtual protected]`[QSize](https://doc.qt.io/qt-6/qsize.html)  QTreeView:: viewportSizeHint () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n178](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n178)[https://doc.qt.io/qt-6/qtreeview.html#viewportSizeHint](https://doc.qt.io/qt-6/qtreeview.html#viewportSizeHint)

Reimplements: [QAbstractItemView::viewportSizeHint](https://doc.qt.io/qt-6/qabstractitemview.html#viewportSizeHint) () const.

### `[override virtual]`[QRect](https://doc.qt.io/qt-6/qrect.html)  QTreeView:: visualRect (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n102](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n102)[https://doc.qt.io/qt-6/qtreeview.html#visualRect](https://doc.qt.io/qt-6/qtreeview.html#visualRect)

Reimplements: [QAbstractItemView::visualRect](https://doc.qt.io/qt-6/qabstractitemview.html#visualRect) (const QModelIndex &index) const.

Returns the rectangle on the viewport occupied by the item at index . If the index is not visible or explicitly hidden, the returned rectangle is invalid.

See also [itemDecorationRect](https://doc.qt.io/qt-6/qtreeview.html#itemDecorationRect) ().

### `[override virtual protected]`[QRegion](https://doc.qt.io/qt-6/qregion.html)  QTreeView:: visualRegionForSelection (const [QItemSelection](https://doc.qt.io/qt-6/qitemselection.html)  & selection ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n151](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qtreeview.h?h=6.12#n151)[https://doc.qt.io/qt-6/qtreeview.html#visualRegionForSelection](https://doc.qt.io/qt-6/qtreeview.html#visualRegionForSelection)

Reimplements: [QAbstractItemView::visualRegionForSelection](https://doc.qt.io/qt-6/qabstractitemview.html#visualRegionForSelection) (const QItemSelection &selection) const.

Returns the rectangle from the viewport of the items in the given selection .

Since 4.7, the returned region only contains rectangles intersecting (or included in) the viewport.

©  2026 The Qt Company Ltd. Documentation contributions included herein are the copyrights of their respective owners. The documentation provided herein is licensed under the terms of the [GNU Free Documentation License version 1.3](http://www.gnu.org/licenses/fdl.html)  as published by the Free Software Foundation. Qt and respective logos are [trademarks](https://doc.qt.io/qt/trademarks.html)  of The Qt Company Ltd. in Finland and/or other countries worldwide. All other trademarks are property of their respective owners. 

[https://www.qt.io/?hsLang=en](https://www.qt.io/?hsLang=en)

[https://twitter.com/qtproject](https://twitter.com/qtproject)[https://www.facebook.com/qt/](https://www.facebook.com/qt/)[https://www.youtube.com/user/QtStudios](https://www.youtube.com/user/QtStudios)[https://www.linkedin.com/company/qtgroup/](https://www.linkedin.com/company/qtgroup/)

[Contact Us](https://www.qt.io/contact-us?hsLang=en)

- [Qt Group](javascript:;)

  - [Our Story](https://www.qt.io/group)

  - [Brand](https://www.qt.io/brand)

  - [News](https://www.qt.io/newsroom)

  - [Careers](https://www.qt.io/careers)

  - [Investors](https://www.qt.io/investors)

  - [Qt Products](https://www.qt.io/product)

  - [Software Quality Products](https://www.qt.io/product/quality-assurance)

- [Licensing](javascript:;)

  - [License Agreement](https://www.qt.io/terms-conditions)

  - [Open Source](https://www.qt.io/licensing/open-source-lgpl-obligations)

  - [Plans and pricing](https://www.qt.io/pricing)

  - [Download](https://www.qt.io/download)

  - [FAQ](https://www.qt.io/faq/overview)

- [Learn Qt](javascript:;)

  - [For Learners](https://www.qt.io/academy)

  - [For Students and Teachers](https://www.qt.io/qt-educational-license)

  - [Qt Documentation](https://doc.qt.io/)

  - [Qt Forum](https://forum.qt.io/)

- [Support & Services](javascript:;)

  - [Professional Services](https://www.qt.io/qt-professional-services)

  - [Customer Success](https://www.qt.io/customer-success)

  - [Support Services](https://www.qt.io/qt-support/)

  - [Partners](https://www.qt.io/contact-us/partners)

  - [Qt World](https://www.qt.io/qt-world)

- [© 2026 The Qt Company](javascript:;)

- [Feedback](mailto:feedback@qt.io?Subject=Feedback%20about%20doc.qt.io%20site)

Qt Group includes The Qt Company Oy and its global subsidiaries and affiliates.
