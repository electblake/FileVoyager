<!--
source: https://doc.qt.io/qt-6/qsortfilterproxymodel.html
retrieved: 2026-10-31T21:19:04.313800+00:00
final_url: https://doc.qt.io/qt-6/qsortfilterproxymodel.html
content_type: text/html
-->

# QSortFilterProxyModel Class | Qt Core | Qt 6.12.0

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

- [Qt Core](https://doc.qt.io/qt-6/qtcore-index.html)

- [C++ Classes](https://doc.qt.io/qt-6/qtcore-module.html)

- QSortFilterProxyModel

On this page

# QSortFilterProxyModel Class

The QSortFilterProxyModel class provides support for sorting and filtering data passed between another model and a view. [More...](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#details)

 Header:`#include <QSortFilterProxyModel>` CMake:`find_package(Qt6 REQUIRED COMPONENTS Core)`
`target_link_libraries(mytarget PRIVATE Qt6::Core)` qmake:`QT += core` Inherits:[QAbstractProxyModel](https://doc.qt.io/qt-6/qabstractproxymodel.html)

- [List of all members, including inherited members](https://doc.qt.io/qt-6/qsortfilterproxymodel-members.html)

## Public Types[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#public-types](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#public-types)

`(since 6.12)` enum class [DataChangeRelevanceFlag](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#DataChangeRelevanceFlag-enum)  { NotRelevant, RelevantForFiltering, RelevantForSorting, RelevantForFilteringAndSorting }  flags [DataChangeRelevanceFlags](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#DataChangeRelevanceFlag-enum)`(since 6.10)` enum class [Direction](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#Direction-enum)  { Rows, Columns, Both }  flags [Directions](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#Direction-enum)

## Properties[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#properties](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#properties)

- `(since 6.0)`[autoAcceptChildRows](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#autoAcceptChildRows-prop)  : bool

- [dynamicSortFilter](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#dynamicSortFilter-prop)  : bool

- [filterCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivity-prop)  : Qt::CaseSensitivity

- [filterKeyColumn](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterKeyColumn-prop)  : int

- [filterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRegularExpression-prop)  : QRegularExpression

- [filterRole](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRole-prop)  : int

- [isSortLocaleAware](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#isSortLocaleAware-prop)  : bool

- [recursiveFilteringEnabled](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#recursiveFilteringEnabled-prop)  : bool

- [sortCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortCaseSensitivity-prop)  : Qt::CaseSensitivity

- [sortRole](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortRole-prop)  : int

## Public Functions[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#public-functions](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#public-functions)

[QSortFilterProxyModel](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#QSortFilterProxyModel) (QObject * parent  = nullptr)  virtual [~QSortFilterProxyModel](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#dtor.QSortFilterProxyModel) ()  bool [autoAcceptChildRows](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#autoAcceptChildRows-prop) () const  QBindable<bool> [bindableAutoAcceptChildRows](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#autoAcceptChildRows-prop) ()  QBindable<bool> [bindableDynamicSortFilter](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#dynamicSortFilter-prop) ()  QBindable<Qt::CaseSensitivity> [bindableFilterCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivity-prop) ()  QBindable<int> [bindableFilterKeyColumn](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterKeyColumn-prop) ()  QBindable<QRegularExpression> [bindableFilterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRegularExpression-prop) ()  QBindable<int> [bindableFilterRole](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRole-prop) ()  QBindable<bool> [bindableIsSortLocaleAware](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#isSortLocaleAware-prop) ()  QBindable<bool> [bindableRecursiveFilteringEnabled](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#recursiveFilteringEnabled-prop) ()  QBindable<Qt::CaseSensitivity> [bindableSortCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortCaseSensitivity-prop) ()  QBindable<int> [bindableSortRole](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortRole-prop) ()  bool [dynamicSortFilter](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#dynamicSortFilter-prop) () const  Qt::CaseSensitivity [filterCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivity-prop) () const  int [filterKeyColumn](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterKeyColumn-prop) () const  QRegularExpression [filterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRegularExpression-prop) () const  int [filterRole](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRole-prop) () const  bool [isRecursiveFilteringEnabled](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#recursiveFilteringEnabled-prop) () const  bool [isSortLocaleAware](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#isSortLocaleAware-prop) () const  void [setAutoAcceptChildRows](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#autoAcceptChildRows-prop) (bool accept )  void [setDynamicSortFilter](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#dynamicSortFilter-prop) (bool enable )  void [setFilterCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivity-prop) (Qt::CaseSensitivity cs )  void [setFilterKeyColumn](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterKeyColumn-prop) (int column )  void [setFilterRole](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRole-prop) (int role )  void [setRecursiveFilteringEnabled](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#recursiveFilteringEnabled-prop) (bool recursive )  void [setSortCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortCaseSensitivity-prop) (Qt::CaseSensitivity cs )  void [setSortLocaleAware](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#isSortLocaleAware-prop) (bool on )  void [setSortRole](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortRole-prop) (int role )  Qt::CaseSensitivity [sortCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortCaseSensitivity-prop) () const  int [sortColumn](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortColumn) () const  Qt::SortOrder [sortOrder](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortOrder) () const  int [sortRole](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortRole-prop) () const

## Reimplemented Public Functions[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#reimplemented-public-functions](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#reimplemented-public-functions)

 virtual QModelIndex [buddy](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#buddy) (const QModelIndex & index ) const override  virtual bool [canFetchMore](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#canFetchMore) (const QModelIndex & parent ) const override  virtual int [columnCount](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#columnCount) (const QModelIndex & parent  = QModelIndex()) const override  virtual QVariant [data](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#data) (const QModelIndex & index , int role  = Qt::DisplayRole) const override  virtual bool [dropMimeData](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#dropMimeData) (const QMimeData * data , Qt::DropAction action , int row , int column , const QModelIndex & parent ) override  virtual void [fetchMore](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#fetchMore) (const QModelIndex & parent ) override  virtual Qt::ItemFlags [flags](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#flags) (const QModelIndex & index ) const override  virtual bool [hasChildren](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#hasChildren) (const QModelIndex & parent  = QModelIndex()) const override  virtual QVariant [headerData](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#headerData) (int section , Qt::Orientation orientation , int role  = Qt::DisplayRole) const override  virtual QModelIndex [index](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#index) (int row , int column , const QModelIndex & parent  = QModelIndex()) const override  virtual bool [insertColumns](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#insertColumns) (int column , int count , const QModelIndex & parent  = QModelIndex()) override  virtual bool [insertRows](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#insertRows) (int row , int count , const QModelIndex & parent  = QModelIndex()) override  virtual QModelIndex [mapFromSource](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapFromSource) (const QModelIndex & sourceIndex ) const override  virtual QItemSelection [mapSelectionFromSource](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapSelectionFromSource) (const QItemSelection & sourceSelection ) const override  virtual QItemSelection [mapSelectionToSource](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapSelectionToSource) (const QItemSelection & proxySelection ) const override  virtual QModelIndex [mapToSource](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapToSource) (const QModelIndex & proxyIndex ) const override  virtual QModelIndexList [match](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#match) (const QModelIndex & start , int role , const QVariant & value , int hits  = 1, Qt::MatchFlags flags  = Qt::MatchFlags(Qt::MatchStartsWith|Qt::MatchWrap)) const override  virtual QMimeData *[mimeData](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mimeData) (const QModelIndexList & indexes ) const override  virtual QStringList [mimeTypes](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mimeTypes) () const override  virtual QModelIndex [parent](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#parent) (const QModelIndex & child ) const override  virtual bool [removeColumns](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#removeColumns) (int column , int count , const QModelIndex & parent  = QModelIndex()) override  virtual bool [removeRows](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#removeRows) (int row , int count , const QModelIndex & parent  = QModelIndex()) override  virtual int [rowCount](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#rowCount) (const QModelIndex & parent  = QModelIndex()) const override  virtual bool [setData](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setData) (const QModelIndex & index , const QVariant & value , int role  = Qt::EditRole) override  virtual bool [setHeaderData](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setHeaderData) (int section , Qt::Orientation orientation , const QVariant & value , int role  = Qt::EditRole) override  virtual void [setSourceModel](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setSourceModel) (QAbstractItemModel * sourceModel ) override  virtual QModelIndex [sibling](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sibling) (int row , int column , const QModelIndex & idx ) const override  virtual void [sort](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sort) (int column , Qt::SortOrder order  = Qt::AscendingOrder) override  virtual QSize [span](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#span) (const QModelIndex & index ) const override  virtual Qt::DropActions [supportedDropActions](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#supportedDropActions) () const override

## Public Slots[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#public-slots](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#public-slots)

 void [invalidate](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidate) ()  void [setFilterFixedString](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterFixedString) (const QString & pattern )  void [setFilterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterRegularExpression) (const QString & pattern )  void [setFilterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRegularExpression-prop) (const QRegularExpression & regularExpression )  void [setFilterWildcard](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterWildcard) (const QString & pattern )

## Signals[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#signals](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#signals)

`(since 6.0)` void [autoAcceptChildRowsChanged](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#autoAcceptChildRowsChanged) (bool autoAcceptChildRows )  void [filterCaseSensitivityChanged](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivityChanged) (Qt::CaseSensitivity filterCaseSensitivity )  void [filterRoleChanged](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRoleChanged) (int filterRole )  void [recursiveFilteringEnabledChanged](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#recursiveFilteringEnabledChanged) (bool recursiveFilteringEnabled )  void [sortCaseSensitivityChanged](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortCaseSensitivityChanged) (Qt::CaseSensitivity sortCaseSensitivity )  void [sortLocaleAwareChanged](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortLocaleAwareChanged) (bool sortLocaleAware )  void [sortRoleChanged](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortRoleChanged) (int sortRole )

## Protected Functions[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#protected-functions](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#protected-functions)

`(since 6.9)` void [beginFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#beginFilterChange) ()`(since 6.12)` QSortFilterProxyModel::DataChangeRelevanceFlags [dataChangeRelevanceFlags](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#dataChangeRelevanceFlags) (const QModelIndex & sourceTopLeft , const QModelIndex & sourceBottomRight , const QList<int> & roles ) const`(since 6.10)` void [endFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#endFilterChange) (QSortFilterProxyModel::Directions directions  = Direction::Both)  virtual bool [filterAcceptsColumn](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsColumn) (int source_column , const QModelIndex & source_parent ) const  virtual bool [filterAcceptsRow](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsRow) (int source_row , const QModelIndex & source_parent ) const`(since 6.0, until 6.13)` void [invalidateColumnsFilter](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidateColumnsFilter) ()`(until 6.13)` void [invalidateFilter](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidateFilter) ()`(since 6.0, until 6.13)` void [invalidateRowsFilter](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidateRowsFilter) ()  virtual bool [lessThan](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#lessThan) (const QModelIndex & source_left , const QModelIndex & source_right ) const

## Detailed Description[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#details](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#details)

QSortFilterProxyModel can be used for sorting items, filtering out items, or both. The model transforms the structure of a source model by mapping the model indexes it supplies to new indexes, corresponding to different locations, for views to use. This approach allows a given source model to be restructured as far as views are concerned without requiring any transformations on the underlying data, and without duplicating the data in memory.

Let's assume that we want to sort and filter the items provided by a custom model. The code to set up the model and the view, without  sorting and filtering, would look like this:

[https://doc.qt.io/qt-6/qtreeview.html](https://doc.qt.io/qt-6/qtreeview.html)[https://doc.qt.io/qt-6/qtreeview.html](https://doc.qt.io/qt-6/qtreeview.html)```
        QTreeView *treeView = new QTreeView;
        MyItemModel *model = new MyItemModel(this);

        treeView->setModel(model);
```

To add sorting and filtering support to `MyItemModel`, we need to create a QSortFilterProxyModel, call [setSourceModel](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setSourceModel) () with the `MyItemModel` as argument, and install the QSortFilterProxyModel on the view:

[https://doc.qt.io/qt-6/qtreeview.html](https://doc.qt.io/qt-6/qtreeview.html)[https://doc.qt.io/qt-6/qtreeview.html](https://doc.qt.io/qt-6/qtreeview.html)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html](https://doc.qt.io/qt-6/qsortfilterproxymodel.html)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html](https://doc.qt.io/qt-6/qsortfilterproxymodel.html)```
        QTreeView *treeView = new QTreeView;
        MyItemModel *sourceModel = new MyItemModel(this);
        QSortFilterProxyModel *proxyModel = new QSortFilterProxyModel(this);

        proxyModel->setSourceModel(sourceModel);
        treeView->setModel(proxyModel);
```

At this point, neither sorting nor filtering is enabled; the original data is displayed in the view. Any changes made through the QSortFilterProxyModel are applied to the original model.

The QSortFilterProxyModel acts as a wrapper for the original model. If you need to convert source [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html) es to sorted/filtered model indexes or vice versa, use [mapToSource](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapToSource) (), [mapFromSource](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapFromSource) (), [mapSelectionToSource](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapSelectionToSource) (), and [mapSelectionFromSource](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapSelectionFromSource) ().

Note: By default, the model dynamically re-sorts and re-filters data whenever the original model changes. This behavior can be changed by setting the [dynamicSortFilter](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#dynamicSortFilter-prop)  property.

The [Basic Sort/Filter Model](https://doc.qt.io/qt-6/qtwidgets-itemviews-basicsortfiltermodel-example.html)  and [Custom Sort/Filter Model](https://doc.qt.io/qt-6/qtwidgets-itemviews-customsortfiltermodel-example.html)  examples illustrate how to use QSortFilterProxyModel to perform basic sorting and filtering and how to subclass it to implement custom behavior.

### Sorting[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sorting](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sorting)

[QTableView](https://doc.qt.io/qt-6/qtableview.html)  and [QTreeView](https://doc.qt.io/qt-6/qtreeview.html)  have a [sortingEnabled](https://doc.qt.io/qt-6/qtreeview.html#sortingEnabled-prop)  property that controls whether the user can sort the view by clicking the view's horizontal header. For example:

```
        treeView->setSortingEnabled(true);
```

When this feature is on (the default is off), clicking on a header section sorts the items according to that column. By clicking repeatedly, the user can alternate between ascending and descending order.

Behind the scene, the view calls the [sort](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sort) () virtual function on the model to reorder the data in the model. To make your data sortable, you can either implement [sort](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sort) () in your model, or use a QSortFilterProxyModel to wrap your model – QSortFilterProxyModel provides a generic [sort](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sort) () reimplementation that operates on the [sortRole](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortRole-prop) () ([Qt::DisplayRole](https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum)  by default) of the items and that understands several data types, including `int`, [QString](https://doc.qt.io/qt-6/qstring.html) , and [QDateTime](https://doc.qt.io/qt-6/qdatetime.html) . For hierarchical models, sorting is applied recursively to all child items. String comparisons are case sensitive by default; this can be changed by setting the [sortCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortCaseSensitivity-prop)  property.

Custom sorting behavior is achieved by subclassing QSortFilterProxyModel and reimplementing [lessThan](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#lessThan) (), which is used to compare items. For example:

[https://doc.qt.io/qt-6/qmodelindex.html](https://doc.qt.io/qt-6/qmodelindex.html)[https://doc.qt.io/qt-6/qmodelindex.html](https://doc.qt.io/qt-6/qmodelindex.html)[https://doc.qt.io/qt-6/qvariant.html](https://doc.qt.io/qt-6/qvariant.html)[https://doc.qt.io/qt-6/qvariant.html](https://doc.qt.io/qt-6/qvariant.html)[https://doc.qt.io/qt-6/qmetatype.html](https://doc.qt.io/qt-6/qmetatype.html)[https://doc.qt.io/qt-6/qdatetime.html](https://doc.qt.io/qt-6/qdatetime.html)[https://doc.qt.io/qt-6/qregularexpression.html](https://doc.qt.io/qt-6/qregularexpression.html)[https://doc.qt.io/qt-6/qstring.html](https://doc.qt.io/qt-6/qstring.html)[https://doc.qt.io/qt-6/qregularexpressionmatch.html](https://doc.qt.io/qt-6/qregularexpressionmatch.html)[https://doc.qt.io/qt-6/qstring.html](https://doc.qt.io/qt-6/qstring.html)[https://doc.qt.io/qt-6/qregularexpressionmatch.html](https://doc.qt.io/qt-6/qregularexpressionmatch.html)[https://doc.qt.io/qt-6/qstring.html](https://doc.qt.io/qt-6/qstring.html)```
bool MySortFilterProxyModel::lessThan(const QModelIndex &left,
                                      const QModelIndex &right) const
{
    QVariant leftData = sourceModel()->data(left);
    QVariant rightData = sourceModel()->data(right);

    if (leftData.userType() == QMetaType::QDateTime)
        return leftData.toDateTime() < rightData.toDateTime();

    static const QRegularExpression emailPattern(u"[\\w\\.]*@[\\w\\.]*"_s);

    QString leftString = leftData.toString();
    if (left.column() == 1) {
        const QRegularExpressionMatch match = emailPattern.match(leftString);
        if (match.hasMatch())
            leftString = match.captured(0);
    }
    QString rightString = rightData.toString();
    if (right.column() == 1) {
        const QRegularExpressionMatch match = emailPattern.match(rightString);
        if (match.hasMatch())
            rightString = match.captured(0);
    }

    return QString::localeAwareCompare(leftString, rightString) < 0;
}
```

(This code snippet comes from the [Custom Sort/Filter Model](https://doc.qt.io/qt-6/qtwidgets-itemviews-customsortfiltermodel-example.html)  example.)

An alternative approach to sorting is to disable sorting on the view and to impose a certain order to the user. This is done by explicitly calling [sort](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sort) () with the desired column and order as arguments on the QSortFilterProxyModel (or on the original model if it implements [sort](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sort) ()). For example:

```
        proxyModel->sort(2, Qt::AscendingOrder);
```

QSortFilterProxyModel can be sorted by column -1, in which case it returns to the sort order of the underlying source model.

Note: [sortColumn](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortColumn) () returns the most recently used sort column. The default value is -1, which means that this proxy model does not sort. Also, note that [sort](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sort) () sets the [sortColumn](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortColumn) () to the most recently used sort column.

### Filtering[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filtering](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filtering)

In addition to sorting, QSortFilterProxyModel can be used to hide items that do not match a certain filter. The filter is specified using a [QRegularExpression](https://doc.qt.io/qt-6/qregularexpression.html)  object and is applied to the [filterRole](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRole-prop) () ([Qt::DisplayRole](https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum)  by default) of each item, for a given column. The [QRegularExpression](https://doc.qt.io/qt-6/qregularexpression.html)  object can be used to match a regular expression, a wildcard pattern, or a fixed string. For example:

[https://doc.qt.io/qt-6/qregularexpression.html](https://doc.qt.io/qt-6/qregularexpression.html)[https://doc.qt.io/qt-6/qregularexpression.html](https://doc.qt.io/qt-6/qregularexpression.html)```
        proxyModel->setFilterRegularExpression(QRegularExpression("\\.png", QRegularExpression::CaseInsensitiveOption));
        proxyModel->setFilterKeyColumn(1);
```

For hierarchical models, the filter is applied recursively to all children. If a parent item doesn't match the filter, none of its children will be shown.

A common use case is to let the user specify the filter regular expression, wildcard pattern, or fixed string in a [QLineEdit](https://doc.qt.io/qt-6/qlineedit.html) . To do this, connect the [QLineEdit::textChanged](https://doc.qt.io/qt-6/qlineedit.html#textChanged) () or [textEdited](https://doc.qt.io/qt-6/qlineedit.html#textEdited) () signal to either [setFilterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterRegularExpression) (), [setFilterWildcard](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterWildcard) (), or [setFilterFixedString](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterFixedString) ().

Custom filtering behavior can be achieved by reimplementing the [filterAcceptsRow](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsRow) () and [filterAcceptsColumn](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsColumn) () functions. For example (from the [Custom Sort/Filter Model](https://doc.qt.io/qt-6/qtwidgets-itemviews-customsortfiltermodel-example.html)  example), the following implementation ignores the [filterKeyColumn](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterKeyColumn-prop)  property and performs filtering on columns 0, 1, and 2:

[https://doc.qt.io/qt-6/qmodelindex.html](https://doc.qt.io/qt-6/qmodelindex.html)[https://doc.qt.io/qt-6/qmodelindex.html](https://doc.qt.io/qt-6/qmodelindex.html)[https://doc.qt.io/qt-6/qmodelindex.html](https://doc.qt.io/qt-6/qmodelindex.html)[https://doc.qt.io/qt-6/qmodelindex.html](https://doc.qt.io/qt-6/qmodelindex.html)```
bool MySortFilterProxyModel::filterAcceptsRow(int sourceRow,
                                              const QModelIndex &sourceParent) const
{
    QModelIndex index0 = sourceModel()->index(sourceRow, 0, sourceParent);
    QModelIndex index1 = sourceModel()->index(sourceRow, 1, sourceParent);
    QModelIndex index2 = sourceModel()->index(sourceRow, 2, sourceParent);

    return (sourceModel()->data(index0).toString().contains(filterRegularExpression())
            || sourceModel()->data(index1).toString().contains(filterRegularExpression()))
            && dateInRange(sourceModel()->data(index2).toDate());
}
```

(This code snippet comes from the [Custom Sort/Filter Model](https://doc.qt.io/qt-6/qtwidgets-itemviews-customsortfiltermodel-example.html)  example.)

If you are working with large amounts of filtering and have to invoke [beginFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#beginFilterChange) () / [endFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#endFilterChange) () repeatedly, using [beginResetModel](https://doc.qt.io/qt-6/qabstractitemmodel.html#beginResetModel) () / [endResetModel](https://doc.qt.io/qt-6/qabstractitemmodel.html#endResetModel) () may be more efficient, depending on the implementation of your model. However, [beginResetModel](https://doc.qt.io/qt-6/qabstractitemmodel.html#beginResetModel) () / [endResetModel](https://doc.qt.io/qt-6/qabstractitemmodel.html#endResetModel) () returns the proxy model to its original state, losing selection information, and will cause the proxy model to be repopulated.

### Subclassing[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#subclassing](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#subclassing)

Since [QAbstractProxyModel](https://doc.qt.io/qt-6/qabstractproxymodel.html)  and its subclasses are derived from [QAbstractItemModel](https://doc.qt.io/qt-6/qabstractitemmodel.html) , much of the same advice about subclassing normal models also applies to proxy models. In addition, it is worth noting that many of the default implementations of functions in this class are written so that they call the equivalent functions in the relevant source model. This simple proxying mechanism may need to be overridden for source models with more complex behavior; for example, if the source model provides a custom [hasChildren](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#hasChildren) () implementation, you should also provide one in the proxy model.

Note: Some general guidelines for subclassing models are available in the [Model Subclassing Reference](https://doc.qt.io/qt-6/model-view-programming.html#model-subclassing-reference) .

See also [QAbstractProxyModel](https://doc.qt.io/qt-6/qabstractproxymodel.html) , [QAbstractItemModel](https://doc.qt.io/qt-6/qabstractitemmodel.html) , [Model/View Programming](https://doc.qt.io/qt-6/model-view-programming.html) , [Basic Sort/Filter Model Example](https://doc.qt.io/qt-6/qtwidgets-itemviews-basicsortfiltermodel-example.html) , [Custom Sort/Filter Model Example](https://doc.qt.io/qt-6/qtwidgets-itemviews-customsortfiltermodel-example.html) , and [QIdentityProxyModel](https://doc.qt.io/qt-6/qidentityproxymodel.html) .

## Member Type Documentation

### `[since 6.12]` enum class QSortFilterProxyModel:: DataChangeRelevanceFlag
flags QSortFilterProxyModel:: DataChangeRelevanceFlags[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n112](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n112)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#DataChangeRelevanceFlag-enum](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#DataChangeRelevanceFlag-enum)

This enum is used to specify the operation for which a source change is relevant.

Constant Value Description`QSortFilterProxyModel::DataChangeRelevanceFlag::NotRelevant``0x00`The change is irrelevant for both filtering and sorting`QSortFilterProxyModel::DataChangeRelevanceFlag::RelevantForFiltering``0x01`The change is relevant for filtering`QSortFilterProxyModel::DataChangeRelevanceFlag::RelevantForSorting``0x02`The change is relevant for sorting`QSortFilterProxyModel::DataChangeRelevanceFlag::RelevantForFilteringAndSorting``RelevantForFiltering | RelevantForSorting`The change is relevant for both filtering and sorting

This enum was introduced in Qt 6.12.

The DataChangeRelevanceFlags type is a typedef for [QFlags](https://doc.qt.io/qt-6/qflags.html) <DataChangeRelevanceFlag>. It stores an OR combination of DataChangeRelevanceFlag values.

See also [dataChangeRelevanceFlags](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#dataChangeRelevanceFlags) ().

### `[since 6.10]` enum class QSortFilterProxyModel:: Direction
flags QSortFilterProxyModel:: Directions[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n105](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n105)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#Direction-enum](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#Direction-enum)

This enum is used to specify the direction to which a custom filter applies when the filter parameters are changed.

Constant Value Description`QSortFilterProxyModel::Direction::Rows``0x01`The filter applies to [rows](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsRow)`QSortFilterProxyModel::Direction::Columns``0x02`The filter applies to [columns](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsColumn)`QSortFilterProxyModel::Direction::Both``Rows | Columns`The filter applies to both rows and columns

This enum was introduced in Qt 6.10.

The Directions type is a typedef for [QFlags](https://doc.qt.io/qt-6/qflags.html) <Direction>. It stores an OR combination of Direction values.

See also [beginFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#beginFilterChange) () and [endFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#endFilterChange) ().

## Property Documentation

### `[bindable, since 6.0]`autoAcceptChildRows  : bool[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n48](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n48)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#autoAcceptChildRows-prop](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#autoAcceptChildRows-prop)

Note: This property supports [QProperty](https://doc.qt.io/qt-6/qproperty.html)  bindings.

if true the proxy model will not filter out children of accepted rows, even if they themselves would be filtered out otherwise.

The default value is false.

This enumeration was introduced in Qt 6.0.

Access functions:

 bool autoAcceptChildRows () const  void setAutoAcceptChildRows (bool accept )

Notifier signal:

 void [autoAcceptChildRowsChanged](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#autoAcceptChildRowsChanged) (bool autoAcceptChildRows )

See also [recursiveFilteringEnabled](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#recursiveFilteringEnabled-prop)  and [filterAcceptsRow](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsRow) ().

### `[bindable]`dynamicSortFilter  : bool[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n31](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n31)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#dynamicSortFilter-prop](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#dynamicSortFilter-prop)

Note: This property supports [QProperty](https://doc.qt.io/qt-6/qproperty.html)  bindings.

This property holds whether the proxy model is dynamically sorted and filtered whenever the contents of the source model change

Note that you should not update the source model through the proxy model when dynamicSortFilter is true. For instance, if you set the proxy model on a [QComboBox](https://doc.qt.io/qt-6/qcombobox.html) , then using functions that update the model, e.g., [addItem](https://doc.qt.io/qt-6/qcombobox.html#addItem) (), will not work as expected. An alternative is to set dynamicSortFilter to false and call [sort](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sort) () after adding items to the [QComboBox](https://doc.qt.io/qt-6/qcombobox.html) .

The default value is true.

Access functions:

 bool dynamicSortFilter () const  void setDynamicSortFilter (bool enable )

See also [sortColumn](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortColumn) ().

### `[bindable]`filterCaseSensitivity  : [Qt::CaseSensitivity](https://doc.qt.io/qt-6/qt.html#CaseSensitivity-enum)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n33](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n33)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivity-prop](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivity-prop)

Note: This property supports [QProperty](https://doc.qt.io/qt-6/qproperty.html)  bindings.

This property holds the case sensitivity of the [QRegularExpression](https://doc.qt.io/qt-6/qregularexpression.html)  pattern used to filter the contents of the source model.

By default, the filter is case sensitive.

Note: Setting this property propagates the new case sensitivity to the [filterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRegularExpression-prop)  property, and so breaks its binding. Likewise explicitly setting [filterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRegularExpression-prop)  changes the current case sensitivity, thereby breaking its binding.

Access functions:

 Qt::CaseSensitivity filterCaseSensitivity () const  void setFilterCaseSensitivity (Qt::CaseSensitivity cs )

Notifier signal:

 void [filterCaseSensitivityChanged](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivityChanged) (Qt::CaseSensitivity filterCaseSensitivity )

See also [filterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRegularExpression-prop)  and [sortCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortCaseSensitivity-prop) .

### `[bindable]`filterKeyColumn  : int[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n29](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n29)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterKeyColumn-prop](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterKeyColumn-prop)

Note: This property supports [QProperty](https://doc.qt.io/qt-6/qproperty.html)  bindings.

This property holds the column where the key used to filter the contents of the source model is read from.

The default value is 0. If the value is -1, the keys will be read from all columns.

Access functions:

 int filterKeyColumn () const  void setFilterKeyColumn (int column )

### `[bindable]`filterRegularExpression  : [QRegularExpression](https://doc.qt.io/qt-6/qregularexpression.html)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n27](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n27)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRegularExpression-prop](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRegularExpression-prop)

Note: This property supports [QProperty](https://doc.qt.io/qt-6/qproperty.html)  bindings.

This property holds the [QRegularExpression](https://doc.qt.io/qt-6/qregularexpression.html)  used to filter the contents of the source model

Setting this property through the [QRegularExpression](https://doc.qt.io/qt-6/qregularexpression.html)  overload overwrites the current [filterCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivity-prop) . By default, the [QRegularExpression](https://doc.qt.io/qt-6/qregularexpression.html)  is an empty string matching all contents.

If no [QRegularExpression](https://doc.qt.io/qt-6/qregularexpression.html)  or an empty string is set, everything in the source model will be accepted.

The regular expression is matched against every row in the source model, so a complex or malformed pattern can slow down or freeze the entire application, especially when used with large models. Application developers are advised to measure the performance and scalability of the regular expression before using it. If the regular expression comes from a potentially untrusted input, consider sanitizing it before passing to this method or using [setFilterFixedString](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterFixedString) () instead.

Note: Setting this property propagates the case sensitivity of the new regular expression to the [filterCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivity-prop)  property, and so breaks its binding. Likewise explicitly setting [filterCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivity-prop)  changes the case sensitivity of the current regular expression, thereby breaking its binding.

Access functions:

 QRegularExpression filterRegularExpression () const  void [setFilterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterRegularExpression) (const QString & pattern )  void setFilterRegularExpression (const QRegularExpression & regularExpression )

See also [filterCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivity-prop) , [setFilterWildcard](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterWildcard) (), and [setFilterFixedString](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterFixedString) ().

### `[bindable]`filterRole  : int[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n43](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n43)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRole-prop](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRole-prop)

Note: This property supports [QProperty](https://doc.qt.io/qt-6/qproperty.html)  bindings.

This property holds the item role that is used to query the source model's data when filtering items.

The default value is [Qt::DisplayRole](https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum) .

Access functions:

 int filterRole () const  void setFilterRole (int role )

Notifier signal:

 void [filterRoleChanged](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRoleChanged) (int filterRole )

See also [filterAcceptsRow](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsRow) ().

### `[bindable]`isSortLocaleAware  : bool[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n39](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n39)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#isSortLocaleAware-prop](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#isSortLocaleAware-prop)

Note: This property supports [QProperty](https://doc.qt.io/qt-6/qproperty.html)  bindings.

This property holds the local aware setting used for comparing strings when sorting

By default, sorting is not local aware.

Access functions:

 bool isSortLocaleAware () const  void setSortLocaleAware (bool on )

Notifier signal:

 void [sortLocaleAwareChanged](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortLocaleAwareChanged) (bool sortLocaleAware )

See also [sortCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortCaseSensitivity-prop)  and [lessThan](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#lessThan) ().

### `[bindable]`recursiveFilteringEnabled  : bool[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n45](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n45)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#recursiveFilteringEnabled-prop](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#recursiveFilteringEnabled-prop)

Note: This property supports [QProperty](https://doc.qt.io/qt-6/qproperty.html)  bindings.

This property holds whether the filter to be applied recursively on children, and for any matching child, its parents will be visible as well.

The default value is false.

Access functions:

 bool isRecursiveFilteringEnabled () const  void setRecursiveFilteringEnabled (bool recursive )

Notifier signal:

 void [recursiveFilteringEnabledChanged](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#recursiveFilteringEnabledChanged) (bool recursiveFilteringEnabled )

See also [autoAcceptChildRows](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#autoAcceptChildRows-prop)  and [filterAcceptsRow](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsRow) ().

### `[bindable]`sortCaseSensitivity  : [Qt::CaseSensitivity](https://doc.qt.io/qt-6/qt.html#CaseSensitivity-enum)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n36](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n36)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortCaseSensitivity-prop](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortCaseSensitivity-prop)

Note: This property supports [QProperty](https://doc.qt.io/qt-6/qproperty.html)  bindings.

This property holds the case sensitivity setting used for comparing strings when sorting

By default, sorting is case sensitive.

Access functions:

 Qt::CaseSensitivity sortCaseSensitivity () const  void setSortCaseSensitivity (Qt::CaseSensitivity cs )

Notifier signal:

 void [sortCaseSensitivityChanged](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortCaseSensitivityChanged) (Qt::CaseSensitivity sortCaseSensitivity )

See also [filterCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivity-prop)  and [lessThan](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#lessThan) ().

### `[bindable]`sortRole  : int[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n41](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n41)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortRole-prop](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortRole-prop)

Note: This property supports [QProperty](https://doc.qt.io/qt-6/qproperty.html)  bindings.

This property holds the item role that is used to query the source model's data when sorting items.

The default value is [Qt::DisplayRole](https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum) .

Access functions:

 int sortRole () const  void setSortRole (int role )

Notifier signal:

 void [sortRoleChanged](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortRoleChanged) (int sortRole )

See also [lessThan](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#lessThan) ().

## Member Function Documentation

### `[explicit]` QSortFilterProxyModel:: QSortFilterProxyModel ([QObject](https://doc.qt.io/qt-6/qobject.html)  * parent  = nullptr)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n52](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n52)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#QSortFilterProxyModel](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#QSortFilterProxyModel)

Constructs a sorting filter model with the given parent .

### `[virtual noexcept]` QSortFilterProxyModel:: ~QSortFilterProxyModel ()[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n53](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n53)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#dtor.QSortFilterProxyModel](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#dtor.QSortFilterProxyModel)

Destroys this sorting filter model.

### `[signal, since 6.0]`void  QSortFilterProxyModel:: autoAcceptChildRowsChanged (bool autoAcceptChildRows )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n203](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n203)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#autoAcceptChildRowsChanged](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#autoAcceptChildRowsChanged)

This signals is emitted when the value of the autoAcceptChildRows  property is changed.

Note: Notifier signal for property [autoAcceptChildRows](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#autoAcceptChildRows-prop) . 

This function was introduced in Qt 6.0.

See also [autoAcceptChildRows](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#autoAcceptChildRows-prop) .

### `[protected, since 6.9]`void  QSortFilterProxyModel:: beginFilterChange ()[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n142](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n142)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#beginFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#beginFilterChange)

Prepares a change of the filter.

This function should be called if you are implementing custom filtering (e.g. [filterAcceptsRow](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsRow) ()), and your filter parameter is about to be changed.

[https://doc.qt.io/qt-6/qdate.html](https://doc.qt.io/qt-6/qdate.html)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html](https://doc.qt.io/qt-6/qsortfilterproxymodel.html)```
void MySortFilterProxyModel::setFilterMaximumDate(QDate date)
{
    beginFilterChange();
    maxDate = date;
    endFilterChange(QSortFilterProxyModel::Direction::Rows);
}
```

Once the filter has been changed, call [endFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#endFilterChange) () with [Direction::Rows](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#Direction-enum)  for row-filters, [Direction::Columns](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#Direction-enum)  for column-filters, or [Direction::Columns](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#Direction-enum) |[Direction::Rows](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#Direction-enum)  if both rows and columns are filtered.

This function was introduced in Qt 6.9.

See also [endFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#endFilterChange) ().

### `[override virtual]`[QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  QSortFilterProxyModel:: buddy (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n184](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n184)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#buddy](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#buddy)

Reimplements: [QAbstractProxyModel::buddy](https://doc.qt.io/qt-6/qabstractproxymodel.html#buddy) (const QModelIndex &index) const.

### `[override virtual]`bool  QSortFilterProxyModel:: canFetchMore (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n181](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n181)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#canFetchMore](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#canFetchMore)

Reimplements: [QAbstractProxyModel::canFetchMore](https://doc.qt.io/qt-6/qabstractproxymodel.html#canFetchMore) (const QModelIndex &parent) const.

### `[override virtual]`int  QSortFilterProxyModel:: columnCount (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent  = QModelIndex()) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n161](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n161)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#columnCount](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#columnCount)

Reimplements: [QAbstractItemModel::columnCount](https://doc.qt.io/qt-6/qabstractitemmodel.html#columnCount) (const QModelIndex &parent) const.

### `[override virtual]`[QVariant](https://doc.qt.io/qt-6/qvariant.html)  QSortFilterProxyModel:: data (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index , int role  = Qt::DisplayRole) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n164](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n164)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#data](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#data)

Reimplements: [QAbstractProxyModel::data](https://doc.qt.io/qt-6/qabstractproxymodel.html#data) (const QModelIndex &proxyIndex, int role) const.

See also [setData](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setData) ().

### `[protected invokable, since 6.12]`[QSortFilterProxyModel::DataChangeRelevanceFlags](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#DataChangeRelevanceFlag-enum)  QSortFilterProxyModel:: dataChangeRelevanceFlags (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & sourceTopLeft , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & sourceBottomRight , const [QList](https://doc.qt.io/qt-6/qlist.html) < int > & roles ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n133](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n133)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#dataChangeRelevanceFlags](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#dataChangeRelevanceFlags)

Reimplement this slot in a subclass to indicate when a source model change is relevant for filtering or sorting. It is used as a performance optimization to avoid unnecessary [filterAcceptsRow](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsRow) () and [lessThan](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#lessThan) () calls upon source model changes that do not affect the sorting and filtering results. The sourceTopLeft , sourceBottomRight  and roles  parameters are those emitted by the source model's [dataChanged](https://doc.qt.io/qt-6/qabstractitemmodel.html#dataChanged) () signal corresponding to the change being evaluated for relevance.

Note: Because of binary compatibility constraints, this method can't be virtual until Qt 7. Meanwhile, redeclare it in a subclass as a slot or [Q_INVOKABLE](https://doc.qt.io/qt-6/qobject.html#Q_INVOKABLE)  method and [QSortFilterProxyModel](https://doc.qt.io/qt-6/qsortfilterproxymodel.html)  will dynamically detect and invoke it.

Note: The default implementation assumes that any change is relevant for filtering, and only changes in the source sort column are relevant for sorting.

Note: This function can be invoked via the meta-object system and from QML. See [Q_INVOKABLE](https://doc.qt.io/qt-6/qobject.html#Q_INVOKABLE) .

This function was introduced in Qt 6.12.

See also [DataChangeRelevanceFlags](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#DataChangeRelevanceFlag-enum) , [filterAcceptsRow](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsRow) (), and [lessThan](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#lessThan) ().

### `[override virtual]`bool  QSortFilterProxyModel:: dropMimeData (const [QMimeData](https://doc.qt.io/qt-6/qmimedata.html)  * data , [Qt::DropAction](https://doc.qt.io/qt-6/qt.html#DropAction-enum) action , int row , int column , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n172](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n172)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#dropMimeData](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#dropMimeData)

Reimplements: [QAbstractProxyModel::dropMimeData](https://doc.qt.io/qt-6/qabstractproxymodel.html#dropMimeData) (const QMimeData *data, Qt::DropAction action, int row, int column, const QModelIndex &parent).

### `[protected, since 6.10]`void  QSortFilterProxyModel:: endFilterChange ([QSortFilterProxyModel::Directions](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#Direction-enum) directions  = Direction::Both)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n143](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n143)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#endFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#endFilterChange)

Invalidates the current filtering after the filter parameter has changed.

This function should be called if you implement custom filtering (e.g. [filterAcceptsRow](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsRow) ()), and your filter parameters have changed. The directions  parameter specifies whether the custom filter impacts rows, columns, or both.

Call [beginFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#beginFilterChange) () when the filter parameter is about to change, and follow with a call to this function once the filter parameters have been changed. Call with directions  set to [Direction::Rows](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#Direction-enum)  for row-filters (i.e. [filterAcceptsRow](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsRow) () is implemented), [Direction::Columns](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#Direction-enum)  for column-filters (i.e. [filterAcceptsColumn](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsColumn) () is implemented), or `Direction::Both` if both filter functions are implemented.

This function was introduced in Qt 6.10.

### `[override virtual]`void  QSortFilterProxyModel:: fetchMore (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n180](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n180)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#fetchMore](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#fetchMore)

Reimplements: [QAbstractProxyModel::fetchMore](https://doc.qt.io/qt-6/qabstractproxymodel.html#fetchMore) (const QModelIndex &parent).

### `[virtual protected]`bool  QSortFilterProxyModel:: filterAcceptsColumn (int source_column , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & source_parent ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n129](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n129)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsColumn](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsColumn)

Returns `true` if the item in the column indicated by the given source_column  and source_parent  should be included in the model; otherwise returns `false`.

Note: The default implementation always returns `true`. You must reimplement this method to get the described behavior.

See also [filterAcceptsRow](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsRow) (), [setFilterFixedString](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterFixedString) (), [setFilterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterRegularExpression) (), and [setFilterWildcard](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterWildcard) ().

### `[virtual protected]`bool  QSortFilterProxyModel:: filterAcceptsRow (int source_row , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & source_parent ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n128](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n128)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsRow](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsRow)

Returns `true` if the item in the row indicated by the given source_row  and source_parent  should be included in the model; otherwise returns false.

The default implementation returns `true` if the value held by the relevant item matches the filter string, wildcard string or regular expression.

Note: By default, the [Qt::DisplayRole](https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum)  is used to determine if the row should be accepted or not. This can be changed by setting the [filterRole](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRole-prop)  property.

See also [filterAcceptsColumn](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsColumn) (), [setFilterFixedString](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterFixedString) (), [setFilterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterRegularExpression) (), and [setFilterWildcard](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterWildcard) ().

### `[signal]`void  QSortFilterProxyModel:: filterCaseSensitivityChanged ([Qt::CaseSensitivity](https://doc.qt.io/qt-6/qt.html#CaseSensitivity-enum) filterCaseSensitivity )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n197](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n197)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivityChanged](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivityChanged)

This signal is emitted when the case sensitivity of the filter changes to filterCaseSensitivity .

Note: Notifier signal for property [filterCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivity-prop) . 

### `[signal]`void  QSortFilterProxyModel:: filterRoleChanged (int filterRole )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n201](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n201)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRoleChanged](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRoleChanged)

This signal is emitted when the filter role changes to filterRole .

Note: Notifier signal for property [filterRole](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRole-prop) . 

### `[override virtual]`[Qt::ItemFlags](https://doc.qt.io/qt-6/qt.html#ItemFlag-enum)  QSortFilterProxyModel:: flags (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n182](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n182)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#flags](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#flags)

Reimplements: [QAbstractProxyModel::flags](https://doc.qt.io/qt-6/qabstractproxymodel.html#flags) (const QModelIndex &index) const.

### `[override virtual]`bool  QSortFilterProxyModel:: hasChildren (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent  = QModelIndex()) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n162](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n162)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#hasChildren](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#hasChildren)

Reimplements: [QAbstractProxyModel::hasChildren](https://doc.qt.io/qt-6/qabstractproxymodel.html#hasChildren) (const QModelIndex &parent) const.

### `[override virtual]`[QVariant](https://doc.qt.io/qt-6/qvariant.html)  QSortFilterProxyModel:: headerData (int section , [Qt::Orientation](https://doc.qt.io/qt-6/qt.html#Orientation-enum) orientation , int role  = Qt::DisplayRole) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n167](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n167)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#headerData](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#headerData)

Reimplements: [QAbstractProxyModel::headerData](https://doc.qt.io/qt-6/qabstractproxymodel.html#headerData) (int section, Qt::Orientation orientation, int role) const.

See also [setHeaderData](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setHeaderData) ().

### `[override virtual]`[QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  QSortFilterProxyModel:: index (int row , int column , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent  = QModelIndex()) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n156](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n156)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#index](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#index)

Reimplements: [QAbstractItemModel::index](https://doc.qt.io/qt-6/qabstractitemmodel.html#index) (int row, int column, const QModelIndex &parent) const.

### `[override virtual]`bool  QSortFilterProxyModel:: insertColumns (int column , int count , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent  = QModelIndex())[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n176](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n176)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#insertColumns](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#insertColumns)

Reimplements: [QAbstractItemModel::insertColumns](https://doc.qt.io/qt-6/qabstractitemmodel.html#insertColumns) (int column, int count, const QModelIndex &parent).

### `[override virtual]`bool  QSortFilterProxyModel:: insertRows (int row , int count , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent  = QModelIndex())[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n175](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n175)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#insertRows](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#insertRows)

Reimplements: [QAbstractItemModel::insertRows](https://doc.qt.io/qt-6/qabstractitemmodel.html#insertRows) (int row, int count, const QModelIndex &parent).

### `[slot]`void  QSortFilterProxyModel:: invalidate ()[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n125](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n125)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidate](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidate)

Invalidates the current sorting and filtering.

See also [beginFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#beginFilterChange) () and [endFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#endFilterChange) ().

### `[protected, since 6.0, until 6.13]`void  QSortFilterProxyModel:: invalidateColumnsFilter ()[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n150](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n150)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidateColumnsFilter](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidateColumnsFilter)

This function is scheduled for deprecation in version 6.13.

use [beginFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#beginFilterChange) () and [endFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#endFilterChange) ([Direction::Rows](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#Direction-enum) ) instead.

Invalidates the current filtering for the columns.

This function should be called if you are implementing custom filtering (by [filterAcceptsColumn](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsColumn) ()), and your filter parameters have changed. This differs from [invalidateFilter](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidateFilter) () in that it will not invoke [filterAcceptsRow](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsRow) (), but only [filterAcceptsColumn](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsColumn) (). You can use this instead of [invalidateFilter](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidateFilter) () if you want to hide or show a column where the rows don't change.

Before your filter parameters change, call [beginFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#beginFilterChange) ().

This function was introduced in Qt 6.0.

See also [invalidate](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidate) (), [invalidateRowsFilter](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidateRowsFilter) (), and [beginFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#beginFilterChange) ().

### `[protected, until 6.13]`void  QSortFilterProxyModel:: invalidateFilter ()[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n146](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n146)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidateFilter](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidateFilter)

This function is scheduled for deprecation in version 6.13.

use [beginFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#beginFilterChange) () and [endFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#endFilterChange) () instead.

Invalidates the current filtering.

This function should be called if you are implementing custom filtering (e.g. [filterAcceptsRow](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsRow) ()), and your filter parameters have changed.

Before your filter parameters change, call [beginFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#beginFilterChange) ().

[https://doc.qt.io/qt-6/qdate.html](https://doc.qt.io/qt-6/qdate.html)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html](https://doc.qt.io/qt-6/qsortfilterproxymodel.html)```
void MySortFilterProxyModel::setFilterMaximumDate(QDate date)
{
    beginFilterChange();
    maxDate = date;
    endFilterChange(QSortFilterProxyModel::Direction::Rows);
}
```

See also [invalidate](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidate) (), [invalidateColumnsFilter](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidateColumnsFilter) (), [invalidateRowsFilter](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidateRowsFilter) (), and [beginFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#beginFilterChange) ().

### `[protected, since 6.0, until 6.13]`void  QSortFilterProxyModel:: invalidateRowsFilter ()[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n148](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n148)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidateRowsFilter](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidateRowsFilter)

This function is scheduled for deprecation in version 6.13.

use [beginFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#beginFilterChange) () and [endFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#endFilterChange) ([Direction::Columns](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#Direction-enum) ) instead.

Invalidates the current filtering for the rows.

This function should be called if you are implementing custom filtering (by [filterAcceptsRow](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsRow) ()), and your filter parameters have changed. This differs from [invalidateFilter](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidateFilter) () in that it will not invoke [filterAcceptsColumn](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsColumn) (), but only [filterAcceptsRow](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterAcceptsRow) (). You can use this instead of [invalidateFilter](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidateFilter) () if you want to hide or show a row where the columns don't change.

Before your filter parameters change, call [beginFilterChange](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#beginFilterChange) ().

This function was introduced in Qt 6.0.

See also [invalidate](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidate) (), [invalidateFilter](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidateFilter) (), and [invalidateColumnsFilter](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#invalidateColumnsFilter) ().

### `[virtual protected]`bool  QSortFilterProxyModel:: lessThan (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & source_left , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & source_right ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n130](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n130)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#lessThan](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#lessThan)

Returns `true` if the value of the item referred to by the given index source_left  is less than the value of the item referred to by the given index source_right , otherwise returns `false`.

This function is used as the `operator<` when sorting, and uses [QAbstractItemModel::compareData](https://doc.qt.io/qt-6/qabstractitemmodel.html#compareData) ().

Comparison of [QString](https://doc.qt.io/qt-6/qstring.html) s is case sensitive by default; this can be changed using the [sortCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortCaseSensitivity-prop)  property.

By default, the [Qt::DisplayRole](https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum)  associated with the [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html) es is used for comparisons. This can be changed by setting the [sortRole](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortRole-prop)  property.

Note: The indices passed in correspond to the source model.

See also [sortRole](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortRole-prop) , [sortCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortCaseSensitivity-prop) , and [dynamicSortFilter](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#dynamicSortFilter-prop) .

### `[override virtual]`[QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  QSortFilterProxyModel:: mapFromSource (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & sourceIndex ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n58](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n58)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapFromSource](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapFromSource)

Reimplements: [QAbstractProxyModel::mapFromSource](https://doc.qt.io/qt-6/qabstractproxymodel.html#mapFromSource) (const QModelIndex &sourceIndex) const.

Returns the model index in the [QSortFilterProxyModel](https://doc.qt.io/qt-6/qsortfilterproxymodel.html)  given the sourceIndex  from the source model.

See also [mapToSource](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapToSource) ().

### `[override virtual]`[QItemSelection](https://doc.qt.io/qt-6/qitemselection.html)  QSortFilterProxyModel:: mapSelectionFromSource (const [QItemSelection](https://doc.qt.io/qt-6/qitemselection.html)  & sourceSelection ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n61](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n61)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapSelectionFromSource](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapSelectionFromSource)

Reimplements: [QAbstractProxyModel::mapSelectionFromSource](https://doc.qt.io/qt-6/qabstractproxymodel.html#mapSelectionFromSource) (const QItemSelection &sourceSelection) const.

### `[override virtual]`[QItemSelection](https://doc.qt.io/qt-6/qitemselection.html)  QSortFilterProxyModel:: mapSelectionToSource (const [QItemSelection](https://doc.qt.io/qt-6/qitemselection.html)  & proxySelection ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n60](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n60)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapSelectionToSource](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapSelectionToSource)

Reimplements: [QAbstractProxyModel::mapSelectionToSource](https://doc.qt.io/qt-6/qabstractproxymodel.html#mapSelectionToSource) (const QItemSelection &proxySelection) const.

### `[override virtual]`[QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  QSortFilterProxyModel:: mapToSource (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & proxyIndex ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n57](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n57)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapToSource](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapToSource)

Reimplements: [QAbstractProxyModel::mapToSource](https://doc.qt.io/qt-6/qabstractproxymodel.html#mapToSource) (const QModelIndex &proxyIndex) const.

Returns the source model index corresponding to the given proxyIndex  from the sorting filter model.

See also [mapFromSource](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mapFromSource) ().

### `[override virtual]`[QModelIndexList](https://doc.qt.io/qt-6/qmodelindex.html#QModelIndexList-typedef)  QSortFilterProxyModel:: match (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & start , int role , const [QVariant](https://doc.qt.io/qt-6/qvariant.html)  & value , int hits  = 1, [Qt::MatchFlags](https://doc.qt.io/qt-6/qt.html#MatchFlag-enum) flags  = Qt::MatchFlags(Qt::MatchStartsWith|Qt::MatchWrap)) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n185](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n185)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#match](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#match)

Reimplements: [QAbstractItemModel::match](https://doc.qt.io/qt-6/qabstractitemmodel.html#match) (const QModelIndex &start, int role, const QVariant &value, int hits, Qt::MatchFlags flags) const.

### `[override virtual]`[QMimeData](https://doc.qt.io/qt-6/qmimedata.html)  *QSortFilterProxyModel:: mimeData (const [QModelIndexList](https://doc.qt.io/qt-6/qmodelindex.html#QModelIndexList-typedef)  & indexes ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n171](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n171)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mimeData](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mimeData)

Reimplements: [QAbstractProxyModel::mimeData](https://doc.qt.io/qt-6/qabstractproxymodel.html#mimeData) (const QModelIndexList &indexes) const.

### `[override virtual]`[QStringList](https://doc.qt.io/qt-6/qstringlist.html)  QSortFilterProxyModel:: mimeTypes () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n192](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n192)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mimeTypes](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#mimeTypes)

Reimplements: [QAbstractProxyModel::mimeTypes](https://doc.qt.io/qt-6/qabstractproxymodel.html#mimeTypes) () const.

### `[override virtual]`[QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  QSortFilterProxyModel:: parent (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & child ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n157](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n157)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#parent](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#parent)

Reimplements: [QAbstractItemModel::parent](https://doc.qt.io/qt-6/qabstractitemmodel.html#parent) (const QModelIndex &index) const.

### `[signal]`void  QSortFilterProxyModel:: recursiveFilteringEnabledChanged (bool recursiveFilteringEnabled )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n202](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n202)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#recursiveFilteringEnabledChanged](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#recursiveFilteringEnabledChanged)

This signal is emitted when the recursive filter setting is changed to recursiveFilteringEnabled .

Note: Notifier signal for property [recursiveFilteringEnabled](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#recursiveFilteringEnabled-prop) . 

### `[override virtual]`bool  QSortFilterProxyModel:: removeColumns (int column , int count , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent  = QModelIndex())[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n178](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n178)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#removeColumns](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#removeColumns)

Reimplements: [QAbstractItemModel::removeColumns](https://doc.qt.io/qt-6/qabstractitemmodel.html#removeColumns) (int column, int count, const QModelIndex &parent).

### `[override virtual]`bool  QSortFilterProxyModel:: removeRows (int row , int count , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent  = QModelIndex())[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n177](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n177)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#removeRows](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#removeRows)

Reimplements: [QAbstractItemModel::removeRows](https://doc.qt.io/qt-6/qabstractitemmodel.html#removeRows) (int row, int count, const QModelIndex &parent).

### `[override virtual]`int  QSortFilterProxyModel:: rowCount (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent  = QModelIndex()) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n160](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n160)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#rowCount](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#rowCount)

Reimplements: [QAbstractItemModel::rowCount](https://doc.qt.io/qt-6/qabstractitemmodel.html#rowCount) (const QModelIndex &parent) const.

### `[override virtual]`bool  QSortFilterProxyModel:: setData (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index , const [QVariant](https://doc.qt.io/qt-6/qvariant.html)  & value , int role  = Qt::EditRole)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n165](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n165)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setData](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setData)

Reimplements: [QAbstractProxyModel::setData](https://doc.qt.io/qt-6/qabstractproxymodel.html#setData) (const QModelIndex &index, const QVariant &value, int role).

See also [data](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#data) ().

### `[slot]`void  QSortFilterProxyModel:: setFilterFixedString (const [QString](https://doc.qt.io/qt-6/qstring.html)  & pattern )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n124](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n124)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterFixedString](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterFixedString)

Sets the fixed string used to filter the contents of the source model to the given pattern .

This method will reset the regular expression options but respect case sensitivity.

Note: Calling this method updates the regular expression, thereby breaking the binding for [filterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRegularExpression-prop) . However it has no effect on the [filterCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivity-prop)  bindings.

See also [setFilterCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivity-prop) (), [setFilterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterRegularExpression) (), [setFilterWildcard](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterWildcard) (), and [filterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRegularExpression-prop) ().

### `[slot]`void  QSortFilterProxyModel:: setFilterRegularExpression (const [QString](https://doc.qt.io/qt-6/qstring.html)  & pattern )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n121](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n121)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterRegularExpression)

Sets the regular expression used to filter the contents of the source model to pattern .

This method should be preferred for new code as it will use [QRegularExpression](https://doc.qt.io/qt-6/qregularexpression.html)  internally.

This method will reset the regular expression options but respect case sensitivity.

Note: Calling this method updates the regular expression, thereby breaking the binding for [filterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRegularExpression-prop) . However it has no effect on the [filterCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivity-prop)  bindings.

Note: Setter function for property [filterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRegularExpression-prop) . 

Note: This slot is overloaded. To connect to this slot: 

```
// Connect using qOverload:
connect(sender, &SenderClass::signal,
        sortFilterProxyModel, qOverload(&QSortFilterProxyModel::setFilterRegularExpression));

// Or using a lambda as wrapper:
connect(sender, &SenderClass::signal,
        sortFilterProxyModel, [receiver = sortFilterProxyModel](const QString &pattern) { receiver->setFilterRegularExpression(pattern); });
```

 For more examples and approaches, see [connecting to overloaded slots](https://doc.qt.io/qt-6/signalsandslots.html#connecting-to-overloaded-signals-and-slots) . 

See also [setFilterCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivity-prop) (), [setFilterWildcard](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterWildcard) (), [setFilterFixedString](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterFixedString) (), and [filterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRegularExpression-prop) ().

### `[slot]`void  QSortFilterProxyModel:: setFilterWildcard (const [QString](https://doc.qt.io/qt-6/qstring.html)  & pattern )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n123](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n123)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterWildcard](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterWildcard)

Sets the wildcard expression used to filter the contents of the source model to the given pattern .

This method will reset the regular expression options but respect case sensitivity.

Note: Calling this method updates the regular expression, thereby breaking the binding for [filterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRegularExpression-prop) . However it has no effect on the [filterCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivity-prop)  bindings.

See also [setFilterCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterCaseSensitivity-prop) (), [setFilterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterRegularExpression) (), [setFilterFixedString](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setFilterFixedString) (), and [filterRegularExpression](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#filterRegularExpression-prop) ().

### `[override virtual]`bool  QSortFilterProxyModel:: setHeaderData (int section , [Qt::Orientation](https://doc.qt.io/qt-6/qt.html#Orientation-enum) orientation , const [QVariant](https://doc.qt.io/qt-6/qvariant.html)  & value , int role  = Qt::EditRole)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n168](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n168)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setHeaderData](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setHeaderData)

Reimplements: [QAbstractProxyModel::setHeaderData](https://doc.qt.io/qt-6/qabstractproxymodel.html#setHeaderData) (int section, Qt::Orientation orientation, const QVariant &value, int role).

See also [headerData](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#headerData) ().

### `[override virtual]`void  QSortFilterProxyModel:: setSourceModel ([QAbstractItemModel](https://doc.qt.io/qt-6/qabstractitemmodel.html)  * sourceModel )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n55](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n55)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setSourceModel](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#setSourceModel)

Reimplements: [QAbstractProxyModel::setSourceModel](https://doc.qt.io/qt-6/qabstractproxymodel.html#setSourceModel) (QAbstractItemModel *sourceModel).

### `[override virtual]`[QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  QSortFilterProxyModel:: sibling (int row , int column , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & idx ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n158](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n158)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sibling](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sibling)

Reimplements: [QAbstractProxyModel::sibling](https://doc.qt.io/qt-6/qabstractproxymodel.html#sibling) (int row, int column, const QModelIndex &idx) const.

### `[override virtual]`void  QSortFilterProxyModel:: sort (int column , [Qt::SortOrder](https://doc.qt.io/qt-6/qt.html#SortOrder-enum) order  = Qt::AscendingOrder)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n190](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n190)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sort](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sort)

Reimplements: [QAbstractProxyModel::sort](https://doc.qt.io/qt-6/qabstractproxymodel.html#sort) (int column, Qt::SortOrder order).

Sorts the model by column  in the given order . If the sort column  is less than zero, the model will be sorted by source model row in the given order .

See also [sortColumn](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortColumn) ().

### `[signal]`void  QSortFilterProxyModel:: sortCaseSensitivityChanged ([Qt::CaseSensitivity](https://doc.qt.io/qt-6/qt.html#CaseSensitivity-enum) sortCaseSensitivity )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n198](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n198)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortCaseSensitivityChanged](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortCaseSensitivityChanged)

This signal is emitted when the case sensitivity for sorting changes to sortCaseSensitivity .

Note: Notifier signal for property [sortCaseSensitivity](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortCaseSensitivity-prop) . 

### int  QSortFilterProxyModel:: sortColumn () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n82](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n82)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortColumn](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortColumn)

Returns the column currently used for sorting

This returns the most recently used sort column. The default value is -1, which means that this proxy model does not sort.

See also [sort](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sort) ().

### `[signal]`void  QSortFilterProxyModel:: sortLocaleAwareChanged (bool sortLocaleAware )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n199](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n199)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortLocaleAwareChanged](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortLocaleAwareChanged)

This signal is emitted when the locale aware setting changes to sortLocaleAware .

Note: Notifier signal for property [isSortLocaleAware](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#isSortLocaleAware-prop) . 

### [Qt::SortOrder](https://doc.qt.io/qt-6/qt.html#SortOrder-enum)  QSortFilterProxyModel:: sortOrder () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n83](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n83)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortOrder](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortOrder)

Returns the order currently used for sorting

This returns the most recently used sort order. The default value is [Qt::AscendingOrder](https://doc.qt.io/qt-6/qt.html#SortOrder-enum) .

See also [sort](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sort) ().

### `[signal]`void  QSortFilterProxyModel:: sortRoleChanged (int sortRole )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n200](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n200)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortRoleChanged](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortRoleChanged)

This signal is emitted when the sort role changes to sortRole .

Note: Notifier signal for property [sortRole](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#sortRole-prop) . 

### `[override virtual]`[QSize](https://doc.qt.io/qt-6/qsize.html)  QSortFilterProxyModel:: span (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n189](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n189)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#span](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#span)

Reimplements: [QAbstractProxyModel::span](https://doc.qt.io/qt-6/qabstractproxymodel.html#span) (const QModelIndex &index) const.

### `[override virtual]`[Qt::DropActions](https://doc.qt.io/qt-6/qt.html#DropAction-enum)  QSortFilterProxyModel:: supportedDropActions () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n193](https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/itemmodels/qsortfilterproxymodel.h?h=6.12#n193)[https://doc.qt.io/qt-6/qsortfilterproxymodel.html#supportedDropActions](https://doc.qt.io/qt-6/qsortfilterproxymodel.html#supportedDropActions)

Reimplements: [QAbstractProxyModel::supportedDropActions](https://doc.qt.io/qt-6/qabstractproxymodel.html#supportedDropActions) () const.

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
