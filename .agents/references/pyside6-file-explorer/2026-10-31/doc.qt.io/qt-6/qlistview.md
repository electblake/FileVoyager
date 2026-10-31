<!--
source: https://doc.qt.io/qt-6/qlistview.html
retrieved: 2026-10-31T21:19:03.639034+00:00
final_url: https://doc.qt.io/qt-6/qlistview.html
content_type: text/html
-->

# QListView Class | Qt Widgets | Qt 6.12.0

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

- QListView

On this page

# QListView Class

The QListView class provides a list or icon view onto a model. [More...](https://doc.qt.io/qt-6/qlistview.html#details)

 Header:`#include <QListView>` CMake:`find_package(Qt6 REQUIRED COMPONENTS Widgets)`
`target_link_libraries(mytarget PRIVATE Qt6::Widgets)` qmake:`QT += widgets` Inherits:[QAbstractItemView](https://doc.qt.io/qt-6/qabstractitemview.html)  Inherited By:

[QHelpIndexWidget](https://doc.qt.io/qt-6/qhelpindexwidget.html) , [QListWidget](https://doc.qt.io/qt-6/qlistwidget.html) , and [QUndoView](https://doc.qt.io/qt-6/qundoview.html)

- [List of all members, including inherited members](https://doc.qt.io/qt-6/qlistview-members.html)

## Public Types[https://doc.qt.io/qt-6/qlistview.html#public-types](https://doc.qt.io/qt-6/qlistview.html#public-types)

 enum [Flow](https://doc.qt.io/qt-6/qlistview.html#Flow-enum)  { LeftToRight, TopToBottom }  enum [LayoutMode](https://doc.qt.io/qt-6/qlistview.html#LayoutMode-enum)  { SinglePass, Batched }  enum [Movement](https://doc.qt.io/qt-6/qlistview.html#Movement-enum)  { Static, Free, Snap }  enum [ResizeMode](https://doc.qt.io/qt-6/qlistview.html#ResizeMode-enum)  { Fixed, Adjust }  enum [ViewMode](https://doc.qt.io/qt-6/qlistview.html#ViewMode-enum)  { ListMode, IconMode }

## Properties[https://doc.qt.io/qt-6/qlistview.html#properties](https://doc.qt.io/qt-6/qlistview.html#properties)

- [batchSize](https://doc.qt.io/qt-6/qlistview.html#batchSize-prop)  : int

- [flow](https://doc.qt.io/qt-6/qlistview.html#flow-prop)  : Flow

- [gridSize](https://doc.qt.io/qt-6/qlistview.html#gridSize-prop)  : QSize

- [isWrapping](https://doc.qt.io/qt-6/qlistview.html#isWrapping-prop)  : bool

- [itemAlignment](https://doc.qt.io/qt-6/qlistview.html#itemAlignment-prop)  : Qt::Alignment

- [layoutMode](https://doc.qt.io/qt-6/qlistview.html#layoutMode-prop)  : LayoutMode

- [modelColumn](https://doc.qt.io/qt-6/qlistview.html#modelColumn-prop)  : int

- [movement](https://doc.qt.io/qt-6/qlistview.html#movement-prop)  : Movement

- [resizeMode](https://doc.qt.io/qt-6/qlistview.html#resizeMode-prop)  : ResizeMode

- [selectionRectVisible](https://doc.qt.io/qt-6/qlistview.html#selectionRectVisible-prop)  : bool

- [spacing](https://doc.qt.io/qt-6/qlistview.html#spacing-prop)  : int

- [uniformItemSizes](https://doc.qt.io/qt-6/qlistview.html#uniformItemSizes-prop)  : bool

- [viewMode](https://doc.qt.io/qt-6/qlistview.html#viewMode-prop)  : ViewMode

- [wordWrap](https://doc.qt.io/qt-6/qlistview.html#wordWrap-prop)  : bool

## Public Functions[https://doc.qt.io/qt-6/qlistview.html#public-functions](https://doc.qt.io/qt-6/qlistview.html#public-functions)

[QListView](https://doc.qt.io/qt-6/qlistview.html#QListView) (QWidget * parent  = nullptr)  virtual [~QListView](https://doc.qt.io/qt-6/qlistview.html#dtor.QListView) ()  int [batchSize](https://doc.qt.io/qt-6/qlistview.html#batchSize-prop) () const  void [clearPropertyFlags](https://doc.qt.io/qt-6/qlistview.html#clearPropertyFlags) ()  QListView::Flow [flow](https://doc.qt.io/qt-6/qlistview.html#flow-prop) () const  QSize [gridSize](https://doc.qt.io/qt-6/qlistview.html#gridSize-prop) () const  bool [isRowHidden](https://doc.qt.io/qt-6/qlistview.html#isRowHidden) (int row ) const  bool [isSelectionRectVisible](https://doc.qt.io/qt-6/qlistview.html#selectionRectVisible-prop) () const  bool [isWrapping](https://doc.qt.io/qt-6/qlistview.html#isWrapping-prop) () const  Qt::Alignment [itemAlignment](https://doc.qt.io/qt-6/qlistview.html#itemAlignment-prop) () const  QListView::LayoutMode [layoutMode](https://doc.qt.io/qt-6/qlistview.html#layoutMode-prop) () const  int [modelColumn](https://doc.qt.io/qt-6/qlistview.html#modelColumn-prop) () const  QListView::Movement [movement](https://doc.qt.io/qt-6/qlistview.html#movement-prop) () const  QListView::ResizeMode [resizeMode](https://doc.qt.io/qt-6/qlistview.html#resizeMode-prop) () const  void [setBatchSize](https://doc.qt.io/qt-6/qlistview.html#batchSize-prop) (int batchSize )  void [setFlow](https://doc.qt.io/qt-6/qlistview.html#flow-prop) (QListView::Flow flow )  void [setGridSize](https://doc.qt.io/qt-6/qlistview.html#gridSize-prop) (const QSize & size )  void [setItemAlignment](https://doc.qt.io/qt-6/qlistview.html#itemAlignment-prop) (Qt::Alignment alignment )  void [setLayoutMode](https://doc.qt.io/qt-6/qlistview.html#layoutMode-prop) (QListView::LayoutMode mode )  void [setModelColumn](https://doc.qt.io/qt-6/qlistview.html#modelColumn-prop) (int column )  void [setMovement](https://doc.qt.io/qt-6/qlistview.html#movement-prop) (QListView::Movement movement )  void [setResizeMode](https://doc.qt.io/qt-6/qlistview.html#resizeMode-prop) (QListView::ResizeMode mode )  void [setRowHidden](https://doc.qt.io/qt-6/qlistview.html#setRowHidden) (int row , bool hide )  void [setSelectionRectVisible](https://doc.qt.io/qt-6/qlistview.html#selectionRectVisible-prop) (bool show )  void [setSpacing](https://doc.qt.io/qt-6/qlistview.html#spacing-prop) (int space )  void [setUniformItemSizes](https://doc.qt.io/qt-6/qlistview.html#uniformItemSizes-prop) (bool enable )  void [setViewMode](https://doc.qt.io/qt-6/qlistview.html#viewMode-prop) (QListView::ViewMode mode )  void [setWordWrap](https://doc.qt.io/qt-6/qlistview.html#wordWrap-prop) (bool on )  void [setWrapping](https://doc.qt.io/qt-6/qlistview.html#isWrapping-prop) (bool enable )  int [spacing](https://doc.qt.io/qt-6/qlistview.html#spacing-prop) () const  bool [uniformItemSizes](https://doc.qt.io/qt-6/qlistview.html#uniformItemSizes-prop) () const  QListView::ViewMode [viewMode](https://doc.qt.io/qt-6/qlistview.html#viewMode-prop) () const  bool [wordWrap](https://doc.qt.io/qt-6/qlistview.html#wordWrap-prop) () const

## Reimplemented Public Functions[https://doc.qt.io/qt-6/qlistview.html#reimplemented-public-functions](https://doc.qt.io/qt-6/qlistview.html#reimplemented-public-functions)

 virtual QModelIndex [indexAt](https://doc.qt.io/qt-6/qlistview.html#indexAt) (const QPoint & p ) const override  virtual void [scrollTo](https://doc.qt.io/qt-6/qlistview.html#scrollTo) (const QModelIndex & index , QAbstractItemView::ScrollHint hint  = EnsureVisible) override  virtual void [setRootIndex](https://doc.qt.io/qt-6/qlistview.html#setRootIndex) (const QModelIndex & index ) override  virtual QRect [visualRect](https://doc.qt.io/qt-6/qlistview.html#visualRect) (const QModelIndex & index ) const override

## Signals[https://doc.qt.io/qt-6/qlistview.html#signals](https://doc.qt.io/qt-6/qlistview.html#signals)

 void [indexesMoved](https://doc.qt.io/qt-6/qlistview.html#indexesMoved) (const QModelIndexList & indexes )

## Protected Functions[https://doc.qt.io/qt-6/qlistview.html#protected-functions](https://doc.qt.io/qt-6/qlistview.html#protected-functions)

 QRect [rectForIndex](https://doc.qt.io/qt-6/qlistview.html#rectForIndex) (const QModelIndex & index ) const  void [setPositionForIndex](https://doc.qt.io/qt-6/qlistview.html#setPositionForIndex) (const QPoint & position , const QModelIndex & index )

## Reimplemented Protected Functions[https://doc.qt.io/qt-6/qlistview.html#reimplemented-protected-functions](https://doc.qt.io/qt-6/qlistview.html#reimplemented-protected-functions)

 virtual void [currentChanged](https://doc.qt.io/qt-6/qlistview.html#currentChanged) (const QModelIndex & current , const QModelIndex & previous ) override  virtual void [dataChanged](https://doc.qt.io/qt-6/qlistview.html#dataChanged) (const QModelIndex & topLeft , const QModelIndex & bottomRight , const QList<int> & roles  = QList<int>()) override  virtual void [dragLeaveEvent](https://doc.qt.io/qt-6/qlistview.html#dragLeaveEvent) (QDragLeaveEvent * e ) override  virtual void [dragMoveEvent](https://doc.qt.io/qt-6/qlistview.html#dragMoveEvent) (QDragMoveEvent * e ) override  virtual void [dropEvent](https://doc.qt.io/qt-6/qlistview.html#dropEvent) (QDropEvent * event ) override  virtual bool [event](https://doc.qt.io/qt-6/qlistview.html#event) (QEvent * e ) override  virtual int [horizontalOffset](https://doc.qt.io/qt-6/qlistview.html#horizontalOffset) () const override  virtual void [initViewItemOption](https://doc.qt.io/qt-6/qlistview.html#initViewItemOption) (QStyleOptionViewItem * option ) const override  virtual bool [isIndexHidden](https://doc.qt.io/qt-6/qlistview.html#isIndexHidden) (const QModelIndex & index ) const override  virtual void [mouseMoveEvent](https://doc.qt.io/qt-6/qlistview.html#mouseMoveEvent) (QMouseEvent * e ) override  virtual void [mouseReleaseEvent](https://doc.qt.io/qt-6/qlistview.html#mouseReleaseEvent) (QMouseEvent * e ) override  virtual QModelIndex [moveCursor](https://doc.qt.io/qt-6/qlistview.html#moveCursor) (QAbstractItemView::CursorAction cursorAction , Qt::KeyboardModifiers modifiers ) override  virtual void [paintEvent](https://doc.qt.io/qt-6/qlistview.html#paintEvent) (QPaintEvent * e ) override  virtual void [resizeEvent](https://doc.qt.io/qt-6/qlistview.html#resizeEvent) (QResizeEvent * e ) override  virtual void [rowsAboutToBeRemoved](https://doc.qt.io/qt-6/qlistview.html#rowsAboutToBeRemoved) (const QModelIndex & parent , int start , int end ) override  virtual void [rowsInserted](https://doc.qt.io/qt-6/qlistview.html#rowsInserted) (const QModelIndex & parent , int start , int end ) override  virtual void [scrollContentsBy](https://doc.qt.io/qt-6/qlistview.html#scrollContentsBy) (int dx , int dy ) override  virtual QModelIndexList [selectedIndexes](https://doc.qt.io/qt-6/qlistview.html#selectedIndexes) () const override  virtual void [selectionChanged](https://doc.qt.io/qt-6/qlistview.html#selectionChanged) (const QItemSelection & selected , const QItemSelection & deselected ) override  virtual void [setSelection](https://doc.qt.io/qt-6/qlistview.html#setSelection) (const QRect & rect , QItemSelectionModel::SelectionFlags command ) override  virtual void [startDrag](https://doc.qt.io/qt-6/qlistview.html#startDrag) (Qt::DropActions supportedActions ) override  virtual void [timerEvent](https://doc.qt.io/qt-6/qlistview.html#timerEvent) (QTimerEvent * e ) override  virtual void [updateGeometries](https://doc.qt.io/qt-6/qlistview.html#updateGeometries) () override  virtual int [verticalOffset](https://doc.qt.io/qt-6/qlistview.html#verticalOffset) () const override  virtual QSize [viewportSizeHint](https://doc.qt.io/qt-6/qlistview.html#viewportSizeHint) () const override  virtual QRegion [visualRegionForSelection](https://doc.qt.io/qt-6/qlistview.html#visualRegionForSelection) (const QItemSelection & selection ) const override  virtual void [wheelEvent](https://doc.qt.io/qt-6/qlistview.html#wheelEvent) (QWheelEvent * e ) override

## Detailed Description[https://doc.qt.io/qt-6/qlistview.html#details](https://doc.qt.io/qt-6/qlistview.html#details)

A QListView presents items stored in a model, either as a simple non-hierarchical list, or as a collection of icons. This class is used to provide lists and icon views that were previously provided by the `QListBox` and `QIconView` classes, but using the more flexible approach provided by Qt's model/view architecture.

The QListView class is one of the [Model/View Classes](https://doc.qt.io/qt-6/model-view-programming.html#the-model-view-classes)  and is part of Qt's [model/view framework](https://doc.qt.io/qt-6/model-view-programming.html) .

This view does not display horizontal or vertical headers; to display a list of items with a horizontal header, use [QTreeView](https://doc.qt.io/qt-6/qtreeview.html)  instead.

QListView implements the interfaces defined by the [QAbstractItemView](https://doc.qt.io/qt-6/qabstractitemview.html)  class to allow it to display data provided by models derived from the [QAbstractItemModel](https://doc.qt.io/qt-6/qabstractitemmodel.html)  class.

Items in a list view can be displayed using one of two view modes: In [ListMode](https://doc.qt.io/qt-6/qlistview.html#ViewMode-enum) , the items are displayed in the form of a simple list; in [IconMode](https://doc.qt.io/qt-6/qlistview.html#ViewMode-enum) , the list view takes the form of an icon view  in which the items are displayed with icons like files in a file manager. By default, the list view is in [ListMode](https://doc.qt.io/qt-6/qlistview.html#ViewMode-enum) . To change the view mode, use the [setViewMode](https://doc.qt.io/qt-6/qlistview.html#viewMode-prop) () function, and to determine the current view mode, use [viewMode](https://doc.qt.io/qt-6/qlistview.html#viewMode-prop) ().

Items in these views are laid out in the direction specified by the [flow](https://doc.qt.io/qt-6/qlistview.html#flow-prop) () of the list view. The items may be fixed in place, or allowed to move, depending on the view's [movement](https://doc.qt.io/qt-6/qlistview.html#movement-prop) () state.

If the items in the model cannot be completely laid out in the direction of flow, they can be wrapped at the boundary of the view widget; this depends on [isWrapping](https://doc.qt.io/qt-6/qlistview.html#isWrapping-prop) (). This property is useful when the items are being represented by an icon view.

The [resizeMode](https://doc.qt.io/qt-6/qlistview.html#resizeMode-prop) () and [layoutMode](https://doc.qt.io/qt-6/qlistview.html#layoutMode-prop) () govern how and when the items are laid out. Items are spaced according to their [spacing](https://doc.qt.io/qt-6/qlistview.html#spacing-prop) (), and can exist within a notional grid of size specified by [gridSize](https://doc.qt.io/qt-6/qlistview.html#gridSize-prop) (). The items can be rendered as large or small icons depending on their [iconSize](https://doc.qt.io/qt-6/qabstractitemview.html#iconSize-prop) ().

### Improving Performance[https://doc.qt.io/qt-6/qlistview.html#improving-performance](https://doc.qt.io/qt-6/qlistview.html#improving-performance)

It is possible to give the view hints about the data it is handling in order to improve its performance when displaying large numbers of items. One approach that can be taken for views that are intended to display items with equal sizes is to set the [uniformItemSizes](https://doc.qt.io/qt-6/qlistview.html#uniformItemSizes-prop)  property to true.

See also [View Classes](https://doc.qt.io/qt-6/model-view-programming.html#view-classes) , [QTreeView](https://doc.qt.io/qt-6/qtreeview.html) , [QTableView](https://doc.qt.io/qt-6/qtableview.html) , and [QListWidget](https://doc.qt.io/qt-6/qlistwidget.html) .

## Member Type Documentation

### enum QListView:: Flow[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n38](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n38)[https://doc.qt.io/qt-6/qlistview.html#Flow-enum](https://doc.qt.io/qt-6/qlistview.html#Flow-enum)

Constant Value Description`QListView::LeftToRight``0`The items are laid out in the view from the left to the right.`QListView::TopToBottom``1`The items are laid out in the view from the top to the bottom.

### enum QListView:: LayoutMode[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n42](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n42)[https://doc.qt.io/qt-6/qlistview.html#LayoutMode-enum](https://doc.qt.io/qt-6/qlistview.html#LayoutMode-enum)

Constant Value Description`QListView::SinglePass``0`The items are laid out all at once.`QListView::Batched``1`The items are laid out in batches of [batchSize](https://doc.qt.io/qt-6/qlistview.html#batchSize-prop)  items.

See also [batchSize](https://doc.qt.io/qt-6/qlistview.html#batchSize-prop) .

### enum QListView:: Movement[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n36](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n36)[https://doc.qt.io/qt-6/qlistview.html#Movement-enum](https://doc.qt.io/qt-6/qlistview.html#Movement-enum)

Constant Value Description`QListView::Static``0`The items cannot be moved by the user.`QListView::Free``1`The items can be moved freely by the user.`QListView::Snap``2`The items snap to the specified grid when moved; see [setGridSize](https://doc.qt.io/qt-6/qlistview.html#gridSize-prop) ().

### enum QListView:: ResizeMode[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n40](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n40)[https://doc.qt.io/qt-6/qlistview.html#ResizeMode-enum](https://doc.qt.io/qt-6/qlistview.html#ResizeMode-enum)

Constant Value Description`QListView::Fixed``0`The items will only be laid out the first time the view is shown.`QListView::Adjust``1`The items will be laid out every time the view is resized.

### enum QListView:: ViewMode[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n44](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n44)[https://doc.qt.io/qt-6/qlistview.html#ViewMode-enum](https://doc.qt.io/qt-6/qlistview.html#ViewMode-enum)

Constant Value Description`QListView::ListMode``0`The items are laid out using [TopToBottom](https://doc.qt.io/qt-6/qlistview.html#Flow-enum)  flow, with Small size and Static movement`QListView::IconMode``1`The items are laid out using [LeftToRight](https://doc.qt.io/qt-6/qlistview.html#Flow-enum)  flow, with Large size and Free movement

## Property Documentation

### batchSize  : int[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n30](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n30)[https://doc.qt.io/qt-6/qlistview.html#batchSize-prop](https://doc.qt.io/qt-6/qlistview.html#batchSize-prop)

This property holds the number of items laid out in each batch if [layoutMode](https://doc.qt.io/qt-6/qlistview.html#layoutMode-prop)  is set to [Batched](https://doc.qt.io/qt-6/qlistview.html#LayoutMode-enum) .

The default value is 100.

Access functions:

 int batchSize () const  void setBatchSize (int batchSize )

### flow  : [Flow](https://doc.qt.io/qt-6/qlistview.html#Flow-enum)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n21](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n21)[https://doc.qt.io/qt-6/qlistview.html#flow-prop](https://doc.qt.io/qt-6/qlistview.html#flow-prop)

This property holds which direction the items layout should flow.

If this property is [LeftToRight](https://doc.qt.io/qt-6/qlistview.html#Flow-enum) , the items will be laid out left to right. If the [isWrapping](https://doc.qt.io/qt-6/qlistview.html#isWrapping-prop)  property is `true`, the layout will wrap when it reaches the right side of the visible area. If this property is [TopToBottom](https://doc.qt.io/qt-6/qlistview.html#Flow-enum) , the items will be laid out from the top of the visible area, wrapping when it reaches the bottom.

Setting this property when the view is visible will cause the items to be laid out again.

By default, this property is set to [TopToBottom](https://doc.qt.io/qt-6/qlistview.html#Flow-enum) .

Access functions:

 QListView::Flow flow () const  void setFlow (QListView::Flow flow )

See also [viewMode](https://doc.qt.io/qt-6/qlistview.html#viewMode-prop) .

### gridSize  : [QSize](https://doc.qt.io/qt-6/qsize.html)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n26](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n26)[https://doc.qt.io/qt-6/qlistview.html#gridSize-prop](https://doc.qt.io/qt-6/qlistview.html#gridSize-prop)

This property holds the size of the layout grid

This property is the size of the grid in which the items are laid out. The default is an empty size which means that there is no grid and the layout is not done in a grid. Setting this property to a non-empty size switches on the grid layout. (When a grid layout is in force the [spacing](https://doc.qt.io/qt-6/qlistview.html#spacing-prop)  property is ignored.)

Setting this property when the view is visible will cause the items to be laid out again.

Access functions:

 QSize gridSize () const  void setGridSize (const QSize & size )

See also [viewMode](https://doc.qt.io/qt-6/qlistview.html#viewMode-prop) .

### isWrapping  : bool[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n22](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n22)[https://doc.qt.io/qt-6/qlistview.html#isWrapping-prop](https://doc.qt.io/qt-6/qlistview.html#isWrapping-prop)

This property holds whether the items layout should wrap.

This property holds whether the layout should wrap when there is no more space in the visible area. The point at which the layout wraps depends on the [flow](https://doc.qt.io/qt-6/qlistview.html#flow-prop)  property.

Setting this property when the view is visible will cause the items to be laid out again.

By default, this property is `false`.

Access functions:

 bool isWrapping () const  void setWrapping (bool enable )

See also [viewMode](https://doc.qt.io/qt-6/qlistview.html#viewMode-prop) .

### itemAlignment  : [Qt::Alignment](https://doc.qt.io/qt-6/qt.html#AlignmentFlag-enum)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n33](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n33)[https://doc.qt.io/qt-6/qlistview.html#itemAlignment-prop](https://doc.qt.io/qt-6/qlistview.html#itemAlignment-prop)

This property holds the alignment of each item in its cell

This is only supported in [ListMode](https://doc.qt.io/qt-6/qlistview.html#ViewMode-enum)  with [TopToBottom](https://doc.qt.io/qt-6/qlistview.html#Flow-enum)  flow and with wrapping enabled. The default alignment is 0, which means that an item fills its cell entirely.

Access functions:

 Qt::Alignment itemAlignment () const  void setItemAlignment (Qt::Alignment alignment )

### layoutMode  : [LayoutMode](https://doc.qt.io/qt-6/qlistview.html#LayoutMode-enum)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n24](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n24)[https://doc.qt.io/qt-6/qlistview.html#layoutMode-prop](https://doc.qt.io/qt-6/qlistview.html#layoutMode-prop)

determines whether the layout of items should happen immediately or be delayed.

This property holds the layout mode for the items. When the mode is [SinglePass](https://doc.qt.io/qt-6/qlistview.html#LayoutMode-enum)  (the default), the items are laid out all in one go. When the mode is [Batched](https://doc.qt.io/qt-6/qlistview.html#LayoutMode-enum) , the items are laid out in batches of [batchSize](https://doc.qt.io/qt-6/qlistview.html#batchSize-prop)  items, while processing events. This makes it possible to instantly view and interact with the visible items while the rest are being laid out.

Access functions:

 QListView::LayoutMode layoutMode () const  void setLayoutMode (QListView::LayoutMode mode )

See also [viewMode](https://doc.qt.io/qt-6/qlistview.html#viewMode-prop) .

### modelColumn  : int[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n28](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n28)[https://doc.qt.io/qt-6/qlistview.html#modelColumn-prop](https://doc.qt.io/qt-6/qlistview.html#modelColumn-prop)

This property holds the column in the model that is visible

By default, this property contains 0, indicating that the first column in the model will be shown.

Access functions:

 int modelColumn () const  void setModelColumn (int column )

### movement  : [Movement](https://doc.qt.io/qt-6/qlistview.html#Movement-enum)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n20](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n20)[https://doc.qt.io/qt-6/qlistview.html#movement-prop](https://doc.qt.io/qt-6/qlistview.html#movement-prop)

This property holds whether the items can be moved freely, are snapped to a grid, or cannot be moved at all.

This property determines how the user can move the items in the view. [Static](https://doc.qt.io/qt-6/qlistview.html#Movement-enum)  means that the items can't be moved by the user. [Free](https://doc.qt.io/qt-6/qlistview.html#Movement-enum)  means that the user can drag and drop the items to any position in the view. [Snap](https://doc.qt.io/qt-6/qlistview.html#Movement-enum)  means that the user can drag and drop the items, but only to the positions in a notional grid signified by the [gridSize](https://doc.qt.io/qt-6/qlistview.html#gridSize-prop)  property.

Setting this property when the view is visible will cause the items to be laid out again.

By default, this property is set to [Static](https://doc.qt.io/qt-6/qlistview.html#Movement-enum) .

Access functions:

 QListView::Movement movement () const  void setMovement (QListView::Movement movement )

See also [gridSize](https://doc.qt.io/qt-6/qlistview.html#gridSize-prop) , [resizeMode](https://doc.qt.io/qt-6/qlistview.html#resizeMode-prop) , and [viewMode](https://doc.qt.io/qt-6/qlistview.html#viewMode-prop) .

### resizeMode  : [ResizeMode](https://doc.qt.io/qt-6/qlistview.html#ResizeMode-enum)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n23](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n23)[https://doc.qt.io/qt-6/qlistview.html#resizeMode-prop](https://doc.qt.io/qt-6/qlistview.html#resizeMode-prop)

This property holds whether the items are laid out again when the view is resized.

If this property is [Adjust](https://doc.qt.io/qt-6/qlistview.html#ResizeMode-enum) , the items will be laid out again when the view is resized. If the value is [Fixed](https://doc.qt.io/qt-6/qlistview.html#ResizeMode-enum) , the items will not be laid out when the view is resized.

By default, this property is set to [Fixed](https://doc.qt.io/qt-6/qlistview.html#ResizeMode-enum) .

Access functions:

 QListView::ResizeMode resizeMode () const  void setResizeMode (QListView::ResizeMode mode )

See also [movement](https://doc.qt.io/qt-6/qlistview.html#movement-prop) , [gridSize](https://doc.qt.io/qt-6/qlistview.html#gridSize-prop) , and [viewMode](https://doc.qt.io/qt-6/qlistview.html#viewMode-prop) .

### selectionRectVisible  : bool[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n32](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n32)[https://doc.qt.io/qt-6/qlistview.html#selectionRectVisible-prop](https://doc.qt.io/qt-6/qlistview.html#selectionRectVisible-prop)

if the selection rectangle should be visible

If this property is `true` then the selection rectangle is visible; otherwise it will be hidden.

Note: The selection rectangle will only be visible if the selection mode is in a mode where more than one item can be selected; i.e., it will not draw a selection rectangle if the selection mode is [QAbstractItemView::SingleSelection](https://doc.qt.io/qt-6/qabstractitemview.html#SelectionMode-enum) .

By default, this property is `false`.

Access functions:

 bool isSelectionRectVisible () const  void setSelectionRectVisible (bool show )

### spacing  : int[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n25](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n25)[https://doc.qt.io/qt-6/qlistview.html#spacing-prop](https://doc.qt.io/qt-6/qlistview.html#spacing-prop)

This property holds the space around the items in the layout

This property is the size of the empty space that is padded around an item in the layout.

Setting this property when the view is visible will cause the items to be laid out again.

By default, this property contains a value of 0.

Access functions:

 int spacing () const  void setSpacing (int space )

See also [viewMode](https://doc.qt.io/qt-6/qlistview.html#viewMode-prop) .

### uniformItemSizes  : bool[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n29](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n29)[https://doc.qt.io/qt-6/qlistview.html#uniformItemSizes-prop](https://doc.qt.io/qt-6/qlistview.html#uniformItemSizes-prop)

This property holds whether all items in the listview have the same size

This property should only be set to true if it is guaranteed that all items in the view have the same size. This enables the view to do some optimizations for performance purposes.

By default, this property is `false`.

Access functions:

 bool uniformItemSizes () const  void setUniformItemSizes (bool enable )

### viewMode  : [ViewMode](https://doc.qt.io/qt-6/qlistview.html#ViewMode-enum)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n27](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n27)[https://doc.qt.io/qt-6/qlistview.html#viewMode-prop](https://doc.qt.io/qt-6/qlistview.html#viewMode-prop)

This property holds the view mode of the [QListView](https://doc.qt.io/qt-6/qlistview.html) .

This property will change the other unset properties to conform with the set view mode. [QListView](https://doc.qt.io/qt-6/qlistview.html) -specific properties that have already been set will not be changed, unless [clearPropertyFlags](https://doc.qt.io/qt-6/qlistview.html#clearPropertyFlags) () has been called.

Setting the view mode will enable or disable drag and drop based on the selected movement. For [ListMode](https://doc.qt.io/qt-6/qlistview.html#ViewMode-enum) , the default movement is [Static](https://doc.qt.io/qt-6/qlistview.html#Movement-enum)  (drag and drop disabled); for [IconMode](https://doc.qt.io/qt-6/qlistview.html#ViewMode-enum) , the default movement is [Free](https://doc.qt.io/qt-6/qlistview.html#Movement-enum)  (drag and drop enabled).

Access functions:

 QListView::ViewMode viewMode () const  void setViewMode (QListView::ViewMode mode )

See also [isWrapping](https://doc.qt.io/qt-6/qlistview.html#isWrapping-prop) , [spacing](https://doc.qt.io/qt-6/qlistview.html#spacing-prop) , [gridSize](https://doc.qt.io/qt-6/qlistview.html#gridSize-prop) , [flow](https://doc.qt.io/qt-6/qlistview.html#flow-prop) , [movement](https://doc.qt.io/qt-6/qlistview.html#movement-prop) , and [resizeMode](https://doc.qt.io/qt-6/qlistview.html#resizeMode-prop) .

### wordWrap  : bool[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n31](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n31)[https://doc.qt.io/qt-6/qlistview.html#wordWrap-prop](https://doc.qt.io/qt-6/qlistview.html#wordWrap-prop)

This property holds the item text word-wrapping policy

If this property is `true` then the item text is wrapped where necessary at word-breaks; otherwise it is not wrapped at all. This property is `false` by default.

Please note that even if wrapping is enabled, the cell will not be expanded to make room for the text. It will print ellipsis for text that cannot be shown, according to the view's [textElideMode](https://doc.qt.io/qt-6/qabstractitemview.html#textElideMode-prop) .

Access functions:

 bool wordWrap () const  void setWordWrap (bool on )

## Member Function Documentation

### `[explicit]` QListView:: QListView ([QWidget](https://doc.qt.io/qt-6/qwidget.html)  * parent  = nullptr)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n47](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n47)[https://doc.qt.io/qt-6/qlistview.html#QListView](https://doc.qt.io/qt-6/qlistview.html#QListView)

Creates a new QListView with the given parent  to view a model. Use [setModel](https://doc.qt.io/qt-6/qabstractitemview.html#setModel) () to set the model.

### `[virtual noexcept]` QListView:: ~QListView ()[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n48](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n48)[https://doc.qt.io/qt-6/qlistview.html#dtor.QListView](https://doc.qt.io/qt-6/qlistview.html#dtor.QListView)

Destroys the view.

### void  QListView:: clearPropertyFlags ()[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n77](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n77)[https://doc.qt.io/qt-6/qlistview.html#clearPropertyFlags](https://doc.qt.io/qt-6/qlistview.html#clearPropertyFlags)

Clears the [QListView](https://doc.qt.io/qt-6/qlistview.html) -specific property flags. See [viewMode](https://doc.qt.io/qt-6/qlistview.html#viewMode-prop) .

Properties inherited from [QAbstractItemView](https://doc.qt.io/qt-6/qabstractitemview.html)  are not covered by the property flags. Specifically, [dragEnabled](https://doc.qt.io/qt-6/qabstractitemview.html#dragEnabled-prop)  and [acceptsDrops](https://doc.qt.io/qt-6/qwidget.html#acceptDrops-prop)  are computed by [QListView](https://doc.qt.io/qt-6/qlistview.html)  when calling [setMovement](https://doc.qt.io/qt-6/qlistview.html#movement-prop) () or [setViewMode](https://doc.qt.io/qt-6/qlistview.html#viewMode-prop) ().

### `[override virtual protected]`void  QListView:: currentChanged (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & current , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & previous )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n156](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n156)[https://doc.qt.io/qt-6/qlistview.html#currentChanged](https://doc.qt.io/qt-6/qlistview.html#currentChanged)

Reimplements: [QAbstractItemView::currentChanged](https://doc.qt.io/qt-6/qabstractitemview.html#currentChanged) (const QModelIndex &current, const QModelIndex &previous).

### `[override virtual protected]`void  QListView:: dataChanged (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & topLeft , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & bottomRight , const [QList](https://doc.qt.io/qt-6/qlist.html) < int > & roles  = QList<int>())[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n118](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n118)[https://doc.qt.io/qt-6/qlistview.html#dataChanged](https://doc.qt.io/qt-6/qlistview.html#dataChanged)

Reimplements: [QAbstractItemView::dataChanged](https://doc.qt.io/qt-6/qabstractitemview.html#dataChanged) (const QModelIndex &topLeft, const QModelIndex &bottomRight, const QList<int> &roles).

### `[override virtual protected]`void  QListView:: dragLeaveEvent ([QDragLeaveEvent](https://doc.qt.io/qt-6/qdragleaveevent.html)  * e )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n133](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n133)[https://doc.qt.io/qt-6/qlistview.html#dragLeaveEvent](https://doc.qt.io/qt-6/qlistview.html#dragLeaveEvent)

Reimplements: [QAbstractItemView::dragLeaveEvent](https://doc.qt.io/qt-6/qabstractitemview.html#dragLeaveEvent) (QDragLeaveEvent *event).

### `[override virtual protected]`void  QListView:: dragMoveEvent ([QDragMoveEvent](https://doc.qt.io/qt-6/qdragmoveevent.html)  * e )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n132](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n132)[https://doc.qt.io/qt-6/qlistview.html#dragMoveEvent](https://doc.qt.io/qt-6/qlistview.html#dragMoveEvent)

Reimplements: [QAbstractItemView::dragMoveEvent](https://doc.qt.io/qt-6/qabstractitemview.html#dragMoveEvent) (QDragMoveEvent *event).

### `[override virtual protected]`void  QListView:: dropEvent ([QDropEvent](https://doc.qt.io/qt-6/qdropevent.html)  * event )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n134](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n134)[https://doc.qt.io/qt-6/qlistview.html#dropEvent](https://doc.qt.io/qt-6/qlistview.html#dropEvent)

Reimplements: [QAbstractItemView::dropEvent](https://doc.qt.io/qt-6/qabstractitemview.html#dropEvent) (QDropEvent *event).

### `[override virtual protected]`bool  QListView:: event ([QEvent](https://doc.qt.io/qt-6/qevent.html)  * e )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n111](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n111)[https://doc.qt.io/qt-6/qlistview.html#event](https://doc.qt.io/qt-6/qlistview.html#event)

Reimplements: [QAbstractItemView::event](https://doc.qt.io/qt-6/qabstractitemview.html#event) (QEvent *event).

### `[override virtual protected]`int  QListView:: horizontalOffset () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n141](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n141)[https://doc.qt.io/qt-6/qlistview.html#horizontalOffset](https://doc.qt.io/qt-6/qlistview.html#horizontalOffset)

Reimplements: [QAbstractItemView::horizontalOffset](https://doc.qt.io/qt-6/qabstractitemview.html#horizontalOffset) () const.

### `[override virtual]`[QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  QListView:: indexAt (const [QPoint](https://doc.qt.io/qt-6/qpoint.html)  & p ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n99](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n99)[https://doc.qt.io/qt-6/qlistview.html#indexAt](https://doc.qt.io/qt-6/qlistview.html#indexAt)

Reimplements: [QAbstractItemView::indexAt](https://doc.qt.io/qt-6/qabstractitemview.html#indexAt) (const QPoint &point) const.

### `[signal]`void  QListView:: indexesMoved (const [QModelIndexList](https://doc.qt.io/qt-6/qmodelindex.html#QModelIndexList-typedef)  & indexes )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n106](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n106)[https://doc.qt.io/qt-6/qlistview.html#indexesMoved](https://doc.qt.io/qt-6/qlistview.html#indexesMoved)

This signal is emitted when the specified indexes  are moved in the view.

### `[override virtual protected]`void  QListView:: initViewItemOption ([QStyleOptionViewItem](https://doc.qt.io/qt-6/qstyleoptionviewitem.html)  * option ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n138](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n138)[https://doc.qt.io/qt-6/qlistview.html#initViewItemOption](https://doc.qt.io/qt-6/qlistview.html#initViewItemOption)

Reimplements: [QAbstractItemView::initViewItemOption](https://doc.qt.io/qt-6/qabstractitemview.html#initViewItemOption) (QStyleOptionViewItem *option) const.

### `[override virtual protected]`bool  QListView:: isIndexHidden (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n153](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n153)[https://doc.qt.io/qt-6/qlistview.html#isIndexHidden](https://doc.qt.io/qt-6/qlistview.html#isIndexHidden)

Reimplements: [QAbstractItemView::isIndexHidden](https://doc.qt.io/qt-6/qabstractitemview.html#isIndexHidden) (const QModelIndex &index) const.

### bool  QListView:: isRowHidden (int row ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n79](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n79)[https://doc.qt.io/qt-6/qlistview.html#isRowHidden](https://doc.qt.io/qt-6/qlistview.html#isRowHidden)

Returns `true` if the row  is hidden; otherwise returns `false`.

### `[override virtual protected]`void  QListView:: mouseMoveEvent ([QMouseEvent](https://doc.qt.io/qt-6/qmouseevent.html)  * e )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n123](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n123)[https://doc.qt.io/qt-6/qlistview.html#mouseMoveEvent](https://doc.qt.io/qt-6/qlistview.html#mouseMoveEvent)

Reimplements: [QAbstractItemView::mouseMoveEvent](https://doc.qt.io/qt-6/qabstractitemview.html#mouseMoveEvent) (QMouseEvent *event).

### `[override virtual protected]`void  QListView:: mouseReleaseEvent ([QMouseEvent](https://doc.qt.io/qt-6/qmouseevent.html)  * e )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n124](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n124)[https://doc.qt.io/qt-6/qlistview.html#mouseReleaseEvent](https://doc.qt.io/qt-6/qlistview.html#mouseReleaseEvent)

Reimplements: [QAbstractItemView::mouseReleaseEvent](https://doc.qt.io/qt-6/qabstractitemview.html#mouseReleaseEvent) (QMouseEvent *event).

### `[override virtual protected]`[QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  QListView:: moveCursor ([QAbstractItemView::CursorAction](https://doc.qt.io/qt-6/qabstractitemview.html#CursorAction-enum) cursorAction , [Qt::KeyboardModifiers](https://doc.qt.io/qt-6/qt.html#KeyboardModifier-enum) modifiers )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n143](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n143)[https://doc.qt.io/qt-6/qlistview.html#moveCursor](https://doc.qt.io/qt-6/qlistview.html#moveCursor)

Reimplements: [QAbstractItemView::moveCursor](https://doc.qt.io/qt-6/qabstractitemview.html#moveCursor) (QAbstractItemView::CursorAction cursorAction, Qt::KeyboardModifiers modifiers).

### `[override virtual protected]`void  QListView:: paintEvent ([QPaintEvent](https://doc.qt.io/qt-6/qpaintevent.html)  * e )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n139](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n139)[https://doc.qt.io/qt-6/qlistview.html#paintEvent](https://doc.qt.io/qt-6/qlistview.html#paintEvent)

Reimplements: [QAbstractScrollArea::paintEvent](https://doc.qt.io/qt-6/qabstractscrollarea.html#paintEvent) (QPaintEvent *event).

### `[protected]`[QRect](https://doc.qt.io/qt-6/qrect.html)  QListView:: rectForIndex (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n144](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n144)[https://doc.qt.io/qt-6/qlistview.html#rectForIndex](https://doc.qt.io/qt-6/qlistview.html#rectForIndex)

Returns the rectangle of the item at position index  in the model. The rectangle is in contents coordinates.

See also [visualRect](https://doc.qt.io/qt-6/qlistview.html#visualRect) ().

### `[override virtual protected]`void  QListView:: resizeEvent ([QResizeEvent](https://doc.qt.io/qt-6/qresizeevent.html)  * e )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n130](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n130)[https://doc.qt.io/qt-6/qlistview.html#resizeEvent](https://doc.qt.io/qt-6/qlistview.html#resizeEvent)

Reimplements: [QAbstractItemView::resizeEvent](https://doc.qt.io/qt-6/qabstractitemview.html#resizeEvent) (QResizeEvent *event).

### `[override virtual protected]`void  QListView:: rowsAboutToBeRemoved (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent , int start , int end )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n121](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n121)[https://doc.qt.io/qt-6/qlistview.html#rowsAboutToBeRemoved](https://doc.qt.io/qt-6/qlistview.html#rowsAboutToBeRemoved)

Reimplements: [QAbstractItemView::rowsAboutToBeRemoved](https://doc.qt.io/qt-6/qabstractitemview.html#rowsAboutToBeRemoved) (const QModelIndex &parent, int start, int end).

### `[override virtual protected]`void  QListView:: rowsInserted (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent , int start , int end )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n120](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n120)[https://doc.qt.io/qt-6/qlistview.html#rowsInserted](https://doc.qt.io/qt-6/qlistview.html#rowsInserted)

Reimplements: [QAbstractItemView::rowsInserted](https://doc.qt.io/qt-6/qabstractitemview.html#rowsInserted) (const QModelIndex &parent, int start, int end).

### `[override virtual protected]`void  QListView:: scrollContentsBy (int dx , int dy )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n113](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n113)[https://doc.qt.io/qt-6/qlistview.html#scrollContentsBy](https://doc.qt.io/qt-6/qlistview.html#scrollContentsBy)

Reimplements: [QAbstractScrollArea::scrollContentsBy](https://doc.qt.io/qt-6/qabstractscrollarea.html#scrollContentsBy) (int dx, int dy).

Scroll the view contents by dx  and dy .

### `[override virtual]`void  QListView:: scrollTo (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index , [QAbstractItemView::ScrollHint](https://doc.qt.io/qt-6/qabstractitemview.html#ScrollHint-enum) hint  = EnsureVisible)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n98](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n98)[https://doc.qt.io/qt-6/qlistview.html#scrollTo](https://doc.qt.io/qt-6/qlistview.html#scrollTo)

Reimplements: [QAbstractItemView::scrollTo](https://doc.qt.io/qt-6/qabstractitemview.html#scrollTo) (const QModelIndex &index, QAbstractItemView::ScrollHint hint).

### `[override virtual protected]`[QModelIndexList](https://doc.qt.io/qt-6/qmodelindex.html#QModelIndexList-typedef)  QListView:: selectedIndexes () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n149](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n149)[https://doc.qt.io/qt-6/qlistview.html#selectedIndexes](https://doc.qt.io/qt-6/qlistview.html#selectedIndexes)

Reimplements: [QAbstractItemView::selectedIndexes](https://doc.qt.io/qt-6/qabstractitemview.html#selectedIndexes) () const.

### `[override virtual protected]`void  QListView:: selectionChanged (const [QItemSelection](https://doc.qt.io/qt-6/qitemselection.html)  & selected , const [QItemSelection](https://doc.qt.io/qt-6/qitemselection.html)  & deselected )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n155](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n155)[https://doc.qt.io/qt-6/qlistview.html#selectionChanged](https://doc.qt.io/qt-6/qlistview.html#selectionChanged)

Reimplements: [QAbstractItemView::selectionChanged](https://doc.qt.io/qt-6/qabstractitemview.html#selectionChanged) (const QItemSelection &selected, const QItemSelection &deselected).

### `[protected]`void  QListView:: setPositionForIndex (const [QPoint](https://doc.qt.io/qt-6/qpoint.html)  & position , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n145](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n145)[https://doc.qt.io/qt-6/qlistview.html#setPositionForIndex](https://doc.qt.io/qt-6/qlistview.html#setPositionForIndex)

Sets the contents position of the item at index  in the model to the given position . If the list view's movement mode is Static or its view mode is [ListView](https://doc.qt.io/qt-6/qml-qtquick-listview.html) , this function will have no effect.

### `[override virtual]`void  QListView:: setRootIndex (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n103](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n103)[https://doc.qt.io/qt-6/qlistview.html#setRootIndex](https://doc.qt.io/qt-6/qlistview.html#setRootIndex)

Reimplements: [QAbstractItemView::setRootIndex](https://doc.qt.io/qt-6/qabstractitemview.html#setRootIndex) (const QModelIndex &index).

### void  QListView:: setRowHidden (int row , bool hide )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n80](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n80)[https://doc.qt.io/qt-6/qlistview.html#setRowHidden](https://doc.qt.io/qt-6/qlistview.html#setRowHidden)

If hide  is true, the given row  will be hidden; otherwise the row  will be shown.

See also [isRowHidden](https://doc.qt.io/qt-6/qlistview.html#isRowHidden) ().

### `[override virtual protected]`void  QListView:: setSelection (const [QRect](https://doc.qt.io/qt-6/qrect.html)  & rect , [QItemSelectionModel::SelectionFlags](https://doc.qt.io/qt-6/qitemselectionmodel.html#SelectionFlag-enum) command )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n147](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n147)[https://doc.qt.io/qt-6/qlistview.html#setSelection](https://doc.qt.io/qt-6/qlistview.html#setSelection)

Reimplements: [QAbstractItemView::setSelection](https://doc.qt.io/qt-6/qabstractitemview.html#setSelection) (const QRect &rect, QItemSelectionModel::SelectionFlags flags).

### `[override virtual protected]`void  QListView:: startDrag ([Qt::DropActions](https://doc.qt.io/qt-6/qt.html#DropAction-enum) supportedActions )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n135](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n135)[https://doc.qt.io/qt-6/qlistview.html#startDrag](https://doc.qt.io/qt-6/qlistview.html#startDrag)

Reimplements: [QAbstractItemView::startDrag](https://doc.qt.io/qt-6/qabstractitemview.html#startDrag) (Qt::DropActions supportedActions).

### `[override virtual protected]`void  QListView:: timerEvent ([QTimerEvent](https://doc.qt.io/qt-6/qtimerevent.html)  * e )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n129](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n129)[https://doc.qt.io/qt-6/qlistview.html#timerEvent](https://doc.qt.io/qt-6/qlistview.html#timerEvent)

Reimplements: [QAbstractItemView::timerEvent](https://doc.qt.io/qt-6/qabstractitemview.html#timerEvent) (QTimerEvent *event).

### `[override virtual protected]`void  QListView:: updateGeometries ()[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n151](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n151)[https://doc.qt.io/qt-6/qlistview.html#updateGeometries](https://doc.qt.io/qt-6/qlistview.html#updateGeometries)

Reimplements: [QAbstractItemView::updateGeometries](https://doc.qt.io/qt-6/qabstractitemview.html#updateGeometries) ().

### `[override virtual protected]`int  QListView:: verticalOffset () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n142](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n142)[https://doc.qt.io/qt-6/qlistview.html#verticalOffset](https://doc.qt.io/qt-6/qlistview.html#verticalOffset)

Reimplements: [QAbstractItemView::verticalOffset](https://doc.qt.io/qt-6/qabstractitemview.html#verticalOffset) () const.

### `[override virtual protected]`[QSize](https://doc.qt.io/qt-6/qsize.html)  QListView:: viewportSizeHint () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n158](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n158)[https://doc.qt.io/qt-6/qlistview.html#viewportSizeHint](https://doc.qt.io/qt-6/qlistview.html#viewportSizeHint)

Reimplements: [QAbstractItemView::viewportSizeHint](https://doc.qt.io/qt-6/qabstractitemview.html#viewportSizeHint) () const.

### `[override virtual]`[QRect](https://doc.qt.io/qt-6/qrect.html)  QListView:: visualRect (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n97](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n97)[https://doc.qt.io/qt-6/qlistview.html#visualRect](https://doc.qt.io/qt-6/qlistview.html#visualRect)

Reimplements: [QAbstractItemView::visualRect](https://doc.qt.io/qt-6/qabstractitemview.html#visualRect) (const QModelIndex &index) const.

### `[override virtual protected]`[QRegion](https://doc.qt.io/qt-6/qregion.html)  QListView:: visualRegionForSelection (const [QItemSelection](https://doc.qt.io/qt-6/qitemselection.html)  & selection ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n148](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n148)[https://doc.qt.io/qt-6/qlistview.html#visualRegionForSelection](https://doc.qt.io/qt-6/qlistview.html#visualRegionForSelection)

Reimplements: [QAbstractItemView::visualRegionForSelection](https://doc.qt.io/qt-6/qabstractitemview.html#visualRegionForSelection) (const QItemSelection &selection) const.

Since 4.7, the returned region only contains rectangles intersecting (or included in) the viewport.

### `[override virtual protected]`void  QListView:: wheelEvent ([QWheelEvent](https://doc.qt.io/qt-6/qwheelevent.html)  * e )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n126](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qlistview.h?h=6.12#n126)[https://doc.qt.io/qt-6/qlistview.html#wheelEvent](https://doc.qt.io/qt-6/qlistview.html#wheelEvent)

Reimplements: [QAbstractScrollArea::wheelEvent](https://doc.qt.io/qt-6/qabstractscrollarea.html#wheelEvent) (QWheelEvent *e).

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
