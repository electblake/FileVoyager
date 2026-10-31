<!--
source: https://doc.qt.io/qt-6/qstyleditemdelegate.html
retrieved: 2026-10-31T21:19:04.895020+00:00
final_url: https://doc.qt.io/qt-6/qstyleditemdelegate.html
content_type: text/html
-->

# QStyledItemDelegate Class | Qt Widgets | Qt 6.12.0

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

- QStyledItemDelegate

On this page

# QStyledItemDelegate Class

The QStyledItemDelegate class provides display and editing facilities for data items from a model. [More...](https://doc.qt.io/qt-6/qstyleditemdelegate.html#details)

 Header:`#include <QStyledItemDelegate>` CMake:`find_package(Qt6 REQUIRED COMPONENTS Widgets)`
`target_link_libraries(mytarget PRIVATE Qt6::Widgets)` qmake:`QT += widgets` Inherits:[QAbstractItemDelegate](https://doc.qt.io/qt-6/qabstractitemdelegate.html)  Inherited By:

[QSqlRelationalDelegate](https://doc.qt.io/qt-6/qsqlrelationaldelegate.html)

- [List of all members, including inherited members](https://doc.qt.io/qt-6/qstyleditemdelegate-members.html)

## Public Functions[https://doc.qt.io/qt-6/qstyleditemdelegate.html#public-functions](https://doc.qt.io/qt-6/qstyleditemdelegate.html#public-functions)

[QStyledItemDelegate](https://doc.qt.io/qt-6/qstyleditemdelegate.html#QStyledItemDelegate) (QObject * parent  = nullptr)  virtual [~QStyledItemDelegate](https://doc.qt.io/qt-6/qstyleditemdelegate.html#dtor.QStyledItemDelegate) ()  virtual QString [displayText](https://doc.qt.io/qt-6/qstyleditemdelegate.html#displayText) (const QVariant & value , const QLocale & locale ) const  QItemEditorFactory *[itemEditorFactory](https://doc.qt.io/qt-6/qstyleditemdelegate.html#itemEditorFactory) () const  void [setItemEditorFactory](https://doc.qt.io/qt-6/qstyleditemdelegate.html#setItemEditorFactory) (QItemEditorFactory * factory )

## Reimplemented Public Functions[https://doc.qt.io/qt-6/qstyleditemdelegate.html#reimplemented-public-functions](https://doc.qt.io/qt-6/qstyleditemdelegate.html#reimplemented-public-functions)

 virtual QWidget *[createEditor](https://doc.qt.io/qt-6/qstyleditemdelegate.html#createEditor) (QWidget * parent , const QStyleOptionViewItem & option , const QModelIndex & index ) const override  virtual void [paint](https://doc.qt.io/qt-6/qstyleditemdelegate.html#paint) (QPainter * painter , const QStyleOptionViewItem & option , const QModelIndex & index ) const override  virtual void [setEditorData](https://doc.qt.io/qt-6/qstyleditemdelegate.html#setEditorData) (QWidget * editor , const QModelIndex & index ) const override  virtual void [setModelData](https://doc.qt.io/qt-6/qstyleditemdelegate.html#setModelData) (QWidget * editor , QAbstractItemModel * model , const QModelIndex & index ) const override  virtual QSize [sizeHint](https://doc.qt.io/qt-6/qstyleditemdelegate.html#sizeHint) (const QStyleOptionViewItem & option , const QModelIndex & index ) const override  virtual void [updateEditorGeometry](https://doc.qt.io/qt-6/qstyleditemdelegate.html#updateEditorGeometry) (QWidget * editor , const QStyleOptionViewItem & option , const QModelIndex & index ) const override

## Protected Functions[https://doc.qt.io/qt-6/qstyleditemdelegate.html#protected-functions](https://doc.qt.io/qt-6/qstyleditemdelegate.html#protected-functions)

 virtual void [initStyleOption](https://doc.qt.io/qt-6/qstyleditemdelegate.html#initStyleOption) (QStyleOptionViewItem * option , const QModelIndex & index ) const

## Reimplemented Protected Functions[https://doc.qt.io/qt-6/qstyleditemdelegate.html#reimplemented-protected-functions](https://doc.qt.io/qt-6/qstyleditemdelegate.html#reimplemented-protected-functions)

 virtual bool [editorEvent](https://doc.qt.io/qt-6/qstyleditemdelegate.html#editorEvent) (QEvent * event , QAbstractItemModel * model , const QStyleOptionViewItem & option , const QModelIndex & index ) override  virtual bool [eventFilter](https://doc.qt.io/qt-6/qstyleditemdelegate.html#eventFilter) (QObject * object , QEvent * event ) override

## Detailed Description[https://doc.qt.io/qt-6/qstyleditemdelegate.html#details](https://doc.qt.io/qt-6/qstyleditemdelegate.html#details)

When displaying data from models in Qt item views, e.g., a [QTableView](https://doc.qt.io/qt-6/qtableview.html) , the individual items are drawn by a delegate. Also, when an item is edited, it provides an editor widget, which is placed on top of the item view while editing takes place. QStyledItemDelegate is the default delegate for all Qt item views, and is installed upon them when they are created.

The QStyledItemDelegate class is one of the [Model/View Classes](https://doc.qt.io/qt-6/model-view-programming.html#the-model-view-classes)  and is part of Qt's [model/view framework](https://doc.qt.io/qt-6/model-view-programming.html) . The delegate allows the display and editing of items to be developed independently from the model and view.

The data of items in models are assigned an [ItemDataRole](https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum) ; each item can store a [QVariant](https://doc.qt.io/qt-6/qvariant.html)  for each role. QStyledItemDelegate implements display and editing for the most common datatypes expected by users, including booleans, integers, and strings.

The data will be drawn differently depending on which role they have in the model. The following table describes the roles and the data types the delegate can handle for each of them. It is often sufficient to ensure that the model returns appropriate data for each of the roles to determine the appearance of items in views.

Role Accepted Types[Qt::BackgroundRole](https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum)[QBrush](https://doc.qt.io/qt-6/qbrush.html)[Qt::CheckStateRole](https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum)[Qt::CheckState](https://doc.qt.io/qt-6/qt.html#CheckState-enum)[Qt::DecorationRole](https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum)[QIcon](https://doc.qt.io/qt-6/qicon.html) , [QPixmap](https://doc.qt.io/qt-6/qpixmap.html) , [QImage](https://doc.qt.io/qt-6/qimage.html)  and [QColor](https://doc.qt.io/qt-6/qcolor.html)[Qt::DisplayRole](https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum)[QString](https://doc.qt.io/qt-6/qstring.html)  and types with a string representation[Qt::EditRole](https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum) See [QItemEditorFactory](https://doc.qt.io/qt-6/qitemeditorfactory.html)  for details[Qt::FontRole](https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum)[QFont](https://doc.qt.io/qt-6/qfont.html)[Qt::SizeHintRole](https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum)[QSize](https://doc.qt.io/qt-6/qsize.html)[Qt::TextAlignmentRole](https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum)[Qt::Alignment](https://doc.qt.io/qt-6/qt.html#AlignmentFlag-enum)[Qt::ForegroundRole](https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum)[QBrush](https://doc.qt.io/qt-6/qbrush.html)

Editors are created with a [QItemEditorFactory](https://doc.qt.io/qt-6/qitemeditorfactory.html) ; a default static instance provided by [QItemEditorFactory](https://doc.qt.io/qt-6/qitemeditorfactory.html)  is installed on all item delegates. You can set a custom factory using [setItemEditorFactory](https://doc.qt.io/qt-6/qstyleditemdelegate.html#setItemEditorFactory) () or set a new default factory with [QItemEditorFactory::setDefaultFactory](https://doc.qt.io/qt-6/qitemeditorfactory.html#setDefaultFactory) ().

[https://doc.qt.io/qt-6/qitemeditorfactory.html](https://doc.qt.io/qt-6/qitemeditorfactory.html)[https://doc.qt.io/qt-6/qitemeditorfactory.html](https://doc.qt.io/qt-6/qitemeditorfactory.html)[https://doc.qt.io/qt-6/qitemeditorcreatorbase.html](https://doc.qt.io/qt-6/qitemeditorcreatorbase.html)[https://doc.qt.io/qt-6/qstandarditemeditorcreator.html](https://doc.qt.io/qt-6/qstandarditemeditorcreator.html)[https://doc.qt.io/qt-6/qmetatype.html](https://doc.qt.io/qt-6/qmetatype.html)[https://doc.qt.io/qt-6/qdatetime.html](https://doc.qt.io/qt-6/qdatetime.html)[https://doc.qt.io/qt-6/qitemeditorfactory.html](https://doc.qt.io/qt-6/qitemeditorfactory.html)```
QItemEditorFactory *editorFactory = new QItemEditorFactory;
QItemEditorCreatorBase *creator = new QStandardItemEditorCreator<MyFancyDateTimeEdit>();
editorFactory->registerEditor(QMetaType::QDateTime, creator);

QItemEditorFactory::setDefaultFactory(editorFactory);
```

After the new factory has been set, all standard item delegates will use it (i.e, also delegates that were created before the new default factory was set).

It is the data stored in the item model with the [EditRole](https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum)  that is edited. See the [QItemEditorFactory](https://doc.qt.io/qt-6/qitemeditorfactory.html)  class for a more high-level introduction to item editor factories.

### Subclassing QStyledItemDelegate[https://doc.qt.io/qt-6/qstyleditemdelegate.html#subclassing-qstyleditemdelegate](https://doc.qt.io/qt-6/qstyleditemdelegate.html#subclassing-qstyleditemdelegate)

If the delegate does not support painting of the data types you need or you want to customize the drawing of items, you need to subclass QStyledItemDelegate, and reimplement [paint](https://doc.qt.io/qt-6/qstyleditemdelegate.html#paint) () and possibly [sizeHint](https://doc.qt.io/qt-6/qstyleditemdelegate.html#sizeHint) (). The [paint](https://doc.qt.io/qt-6/qstyleditemdelegate.html#paint) () function is called individually for each item, and with [sizeHint](https://doc.qt.io/qt-6/qstyleditemdelegate.html#sizeHint) (), you can specify the hint for each of them.

When reimplementing [paint](https://doc.qt.io/qt-6/qstyleditemdelegate.html#paint) (), one would typically handle the datatypes one would like to draw and use the superclass implementation for other types.

The painting of check box indicators are performed by the current style. The style also specifies the size and the bounding rectangles in which to draw the data for the different data roles. The bounding rectangle of the item itself is also calculated by the style. When drawing already supported datatypes, it is therefore a good idea to ask the style for these bounding rectangles. The [QStyle](https://doc.qt.io/qt-6/qstyle.html)  class description describes this in more detail.

If you wish to change any of the bounding rectangles calculated by the style or the painting of check box indicators, you can subclass [QStyle](https://doc.qt.io/qt-6/qstyle.html) . Note, however, that the size of the items can also be affected by reimplementing [sizeHint](https://doc.qt.io/qt-6/qstyleditemdelegate.html#sizeHint) ().

It is possible for a custom delegate to provide editors without the use of an editor item factory. In this case, the following virtual functions must be reimplemented:

- [createEditor](https://doc.qt.io/qt-6/qstyleditemdelegate.html#createEditor) () returns the widget used to change data from the model and can be reimplemented to customize editing behavior.

- [setEditorData](https://doc.qt.io/qt-6/qstyleditemdelegate.html#setEditorData) () provides the widget with data to manipulate.

- [updateEditorGeometry](https://doc.qt.io/qt-6/qstyleditemdelegate.html#updateEditorGeometry) () ensures that the editor is displayed correctly with respect to the item view.

- [setModelData](https://doc.qt.io/qt-6/qstyleditemdelegate.html#setModelData) () returns updated data to the model.

The [Star Delegate](https://doc.qt.io/qt-6/qtwidgets-itemviews-stardelegate-example.html)  example creates editors by reimplementing these methods.

### QStyledItemDelegate vs. QItemDelegate[https://doc.qt.io/qt-6/qstyleditemdelegate.html#qstyleditemdelegate-vs-qitemdelegate](https://doc.qt.io/qt-6/qstyleditemdelegate.html#qstyleditemdelegate-vs-qitemdelegate)

Since Qt 4.4, there are two delegate classes: [QItemDelegate](https://doc.qt.io/qt-6/qitemdelegate.html)  and QStyledItemDelegate. However, the default delegate is QStyledItemDelegate. These two classes are independent alternatives to painting and providing editors for items in views. The difference between them is that QStyledItemDelegate uses the current style to paint its items. We therefore recommend using QStyledItemDelegate as the base class when implementing custom delegates or when working with Qt style sheets. The code required for either class should be equal unless the custom delegate needs to use the style for drawing.

If you wish to customize the painting of item views, you should implement a custom style. Please see the [QStyle](https://doc.qt.io/qt-6/qstyle.html)  class documentation for details.

See also [Delegate Classes](https://doc.qt.io/qt-6/model-view-programming.html#delegate-classes) , [QItemDelegate](https://doc.qt.io/qt-6/qitemdelegate.html) , [QAbstractItemDelegate](https://doc.qt.io/qt-6/qabstractitemdelegate.html) , [QStyle](https://doc.qt.io/qt-6/qstyle.html) , and [Star Delegate Example](https://doc.qt.io/qt-6/qtwidgets-itemviews-stardelegate-example.html) .

## Member Function Documentation

### `[explicit]` QStyledItemDelegate:: QStyledItemDelegate ([QObject](https://doc.qt.io/qt-6/qobject.html)  * parent  = nullptr)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n26](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n26)[https://doc.qt.io/qt-6/qstyleditemdelegate.html#QStyledItemDelegate](https://doc.qt.io/qt-6/qstyleditemdelegate.html#QStyledItemDelegate)

Constructs an item delegate with the given parent .

### `[virtual noexcept]` QStyledItemDelegate:: ~QStyledItemDelegate ()[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n27](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n27)[https://doc.qt.io/qt-6/qstyleditemdelegate.html#dtor.QStyledItemDelegate](https://doc.qt.io/qt-6/qstyleditemdelegate.html#dtor.QStyledItemDelegate)

Destroys the item delegate.

### `[override virtual]`[QWidget](https://doc.qt.io/qt-6/qwidget.html)  *QStyledItemDelegate:: createEditor ([QWidget](https://doc.qt.io/qt-6/qwidget.html)  * parent , const [QStyleOptionViewItem](https://doc.qt.io/qt-6/qstyleoptionviewitem.html)  & option , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n36](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n36)[https://doc.qt.io/qt-6/qstyleditemdelegate.html#createEditor](https://doc.qt.io/qt-6/qstyleditemdelegate.html#createEditor)

Reimplements: [QAbstractItemDelegate::createEditor](https://doc.qt.io/qt-6/qabstractitemdelegate.html#createEditor) (QWidget *parent, const QStyleOptionViewItem &option, const QModelIndex &index) const.

Returns the widget used to edit the item specified by index  for editing. The parent  widget and style option  are used to control how the editor widget appears.

See also [QAbstractItemDelegate::createEditor](https://doc.qt.io/qt-6/qabstractitemdelegate.html#createEditor) ().

### `[virtual]`[QString](https://doc.qt.io/qt-6/qstring.html)  QStyledItemDelegate:: displayText (const [QVariant](https://doc.qt.io/qt-6/qvariant.html)  & value , const [QLocale](https://doc.qt.io/qt-6/qlocale.html)  & locale ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n53](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n53)[https://doc.qt.io/qt-6/qstyleditemdelegate.html#displayText](https://doc.qt.io/qt-6/qstyleditemdelegate.html#displayText)

This function returns the string that the delegate will use to display the [Qt::DisplayRole](https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum)  of the model in locale . value  is the value of the [Qt::DisplayRole](https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum)  provided by the model.

The default implementation uses the [QLocale::toString](https://doc.qt.io/qt-6/qlocale.html#toString)  to convert value  into a [QString](https://doc.qt.io/qt-6/qstring.html) .

This function is not called for empty model indices, i.e., indices for which the model returns an invalid [QVariant](https://doc.qt.io/qt-6/qvariant.html) .

See also [QAbstractItemModel::data](https://doc.qt.io/qt-6/qabstractitemmodel.html#data) ().

### `[override virtual protected]`bool  QStyledItemDelegate:: editorEvent ([QEvent](https://doc.qt.io/qt-6/qevent.html)  * event , [QAbstractItemModel](https://doc.qt.io/qt-6/qabstractitemmodel.html)  * model , const [QStyleOptionViewItem](https://doc.qt.io/qt-6/qstyleoptionviewitem.html)  & option , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n60](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n60)[https://doc.qt.io/qt-6/qstyleditemdelegate.html#editorEvent](https://doc.qt.io/qt-6/qstyleditemdelegate.html#editorEvent)

Reimplements: [QAbstractItemDelegate::editorEvent](https://doc.qt.io/qt-6/qabstractitemdelegate.html#editorEvent) (QEvent *event, QAbstractItemModel *model, const QStyleOptionViewItem &option, const QModelIndex &index).

### `[override virtual protected]`bool  QStyledItemDelegate:: eventFilter ([QObject](https://doc.qt.io/qt-6/qobject.html)  * object , [QEvent](https://doc.qt.io/qt-6/qevent.html)  * event )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n59](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n59)[https://doc.qt.io/qt-6/qstyleditemdelegate.html#eventFilter](https://doc.qt.io/qt-6/qstyleditemdelegate.html#eventFilter)

Reimplements: [QObject::eventFilter](https://doc.qt.io/qt-6/qobject.html#eventFilter) (QObject *watched, QEvent *event).

See details in [QAbstractItemDelegate::handleEditorEvent](https://doc.qt.io/qt-6/qabstractitemdelegate.html#handleEditorEvent) ().

### `[virtual protected]`void  QStyledItemDelegate:: initStyleOption ([QStyleOptionViewItem](https://doc.qt.io/qt-6/qstyleoptionviewitem.html)  * option , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n56](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n56)[https://doc.qt.io/qt-6/qstyleditemdelegate.html#initStyleOption](https://doc.qt.io/qt-6/qstyleditemdelegate.html#initStyleOption)

Initialize option  with the values using the index index . This method is useful for subclasses when they need a [QStyleOptionViewItem](https://doc.qt.io/qt-6/qstyleoptionviewitem.html) , but don't want to fill in all the information themselves.

See also [QStyleOption::initFrom](https://doc.qt.io/qt-6/qstyleoption.html#initFrom) ().

### [QItemEditorFactory](https://doc.qt.io/qt-6/qitemeditorfactory.html)  *QStyledItemDelegate:: itemEditorFactory () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n50](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n50)[https://doc.qt.io/qt-6/qstyleditemdelegate.html#itemEditorFactory](https://doc.qt.io/qt-6/qstyleditemdelegate.html#itemEditorFactory)

Returns the editor factory used by the item delegate. If no editor factory is set, the function will return null.

See also [setItemEditorFactory](https://doc.qt.io/qt-6/qstyleditemdelegate.html#setItemEditorFactory) ().

### `[override virtual]`void  QStyledItemDelegate:: paint ([QPainter](https://doc.qt.io/qt-6/qpainter.html)  * painter , const [QStyleOptionViewItem](https://doc.qt.io/qt-6/qstyleoptionviewitem.html)  & option , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n30](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n30)[https://doc.qt.io/qt-6/qstyleditemdelegate.html#paint](https://doc.qt.io/qt-6/qstyleditemdelegate.html#paint)

Reimplements: [QAbstractItemDelegate::paint](https://doc.qt.io/qt-6/qabstractitemdelegate.html#paint) (QPainter *painter, const QStyleOptionViewItem &option, const QModelIndex &index) const.

Renders the delegate using the given painter  and style option  for the item specified by index .

This function paints the item using the view's [QStyle](https://doc.qt.io/qt-6/qstyle.html) .

When reimplementing paint in a subclass. Use the [initStyleOption](https://doc.qt.io/qt-6/qstyleditemdelegate.html#initStyleOption) () to set up the option  in the same way as the [QStyledItemDelegate](https://doc.qt.io/qt-6/qstyleditemdelegate.html) .

Whenever possible, use the option  while painting. Especially its [rect](https://doc.qt.io/qt-6/qstyleoption.html#rect-var)  variable to decide where to draw and its [state](https://doc.qt.io/qt-6/qstyleoption.html#state-var)  to determine if it is enabled or selected.

After painting, you should ensure that the painter is returned to the state it was supplied in when this function was called. For example, it may be useful to call [QPainter::save](https://doc.qt.io/qt-6/qpainter.html#save) () before painting and [QPainter::restore](https://doc.qt.io/qt-6/qpainter.html#restore) () afterwards.

See also [QItemDelegate::paint](https://doc.qt.io/qt-6/qitemdelegate.html#paint) (), [QStyle::drawControl](https://doc.qt.io/qt-6/qstyle.html#drawControl) (), and [QStyle::CE_ItemViewItem](https://doc.qt.io/qt-6/qstyle.html#ControlElement-enum) .

### `[override virtual]`void  QStyledItemDelegate:: setEditorData ([QWidget](https://doc.qt.io/qt-6/qwidget.html)  * editor , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n40](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n40)[https://doc.qt.io/qt-6/qstyleditemdelegate.html#setEditorData](https://doc.qt.io/qt-6/qstyleditemdelegate.html#setEditorData)

Reimplements: [QAbstractItemDelegate::setEditorData](https://doc.qt.io/qt-6/qabstractitemdelegate.html#setEditorData) (QWidget *editor, const QModelIndex &index) const.

Sets the data to be displayed and edited by the editor  from the data model item specified by the model index .

The default implementation stores the data in the editor  widget's [user property](https://doc.qt.io/qt-6/properties.html) .

See also [QMetaProperty::isUser](https://doc.qt.io/qt-6/qmetaproperty.html#isUser) ().

### void  QStyledItemDelegate:: setItemEditorFactory ([QItemEditorFactory](https://doc.qt.io/qt-6/qitemeditorfactory.html)  * factory )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n51](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n51)[https://doc.qt.io/qt-6/qstyleditemdelegate.html#setItemEditorFactory](https://doc.qt.io/qt-6/qstyleditemdelegate.html#setItemEditorFactory)

Sets the editor factory to be used by the item delegate to be the factory  specified. If no editor factory is set, the item delegate will use the default editor factory.

See also [itemEditorFactory](https://doc.qt.io/qt-6/qstyleditemdelegate.html#itemEditorFactory) ().

### `[override virtual]`void  QStyledItemDelegate:: setModelData ([QWidget](https://doc.qt.io/qt-6/qwidget.html)  * editor , [QAbstractItemModel](https://doc.qt.io/qt-6/qabstractitemmodel.html)  * model , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n41](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n41)[https://doc.qt.io/qt-6/qstyleditemdelegate.html#setModelData](https://doc.qt.io/qt-6/qstyleditemdelegate.html#setModelData)

Reimplements: [QAbstractItemDelegate::setModelData](https://doc.qt.io/qt-6/qabstractitemdelegate.html#setModelData) (QWidget *editor, QAbstractItemModel *model, const QModelIndex &index) const.

Gets data from the editor  widget and stores it in the specified model  at the item index .

The default implementation gets the value to be stored in the data model from the editor  widget's [user property](https://doc.qt.io/qt-6/properties.html) .

See also [QMetaProperty::isUser](https://doc.qt.io/qt-6/qmetaproperty.html#isUser) ().

### `[override virtual]`[QSize](https://doc.qt.io/qt-6/qsize.html)  QStyledItemDelegate:: sizeHint (const [QStyleOptionViewItem](https://doc.qt.io/qt-6/qstyleoptionviewitem.html)  & option , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n32](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n32)[https://doc.qt.io/qt-6/qstyleditemdelegate.html#sizeHint](https://doc.qt.io/qt-6/qstyleditemdelegate.html#sizeHint)

Reimplements: [QAbstractItemDelegate::sizeHint](https://doc.qt.io/qt-6/qabstractitemdelegate.html#sizeHint) (const QStyleOptionViewItem &option, const QModelIndex &index) const.

Returns the size needed by the delegate to display the item specified by index , taking into account the style information provided by option .

This function uses the view's [QStyle](https://doc.qt.io/qt-6/qstyle.html)  to determine the size of the item.

See also [QStyle::sizeFromContents](https://doc.qt.io/qt-6/qstyle.html#sizeFromContents) () and [QStyle::CT_ItemViewItem](https://doc.qt.io/qt-6/qstyle.html#ContentsType-enum) .

### `[override virtual]`void  QStyledItemDelegate:: updateEditorGeometry ([QWidget](https://doc.qt.io/qt-6/qwidget.html)  * editor , const [QStyleOptionViewItem](https://doc.qt.io/qt-6/qstyleoptionviewitem.html)  & option , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n45](https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/itemviews/qstyleditemdelegate.h?h=6.12#n45)[https://doc.qt.io/qt-6/qstyleditemdelegate.html#updateEditorGeometry](https://doc.qt.io/qt-6/qstyleditemdelegate.html#updateEditorGeometry)

Reimplements: [QAbstractItemDelegate::updateEditorGeometry](https://doc.qt.io/qt-6/qabstractitemdelegate.html#updateEditorGeometry) (QWidget *editor, const QStyleOptionViewItem &option, const QModelIndex &index) const.

Updates the editor  for the item specified by index  according to the style option  given.

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
