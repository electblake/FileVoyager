<!--
source: https://doc.qt.io/qt-6/qfilesystemmodel.html
retrieved: 2026-10-31T21:19:02.255379+00:00
final_url: https://doc.qt.io/qt-6/qfilesystemmodel.html
content_type: text/html
-->

# QFileSystemModel Class | Qt GUI | Qt 6.12.0

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

- [Qt GUI](https://doc.qt.io/qt-6/qtgui-index.html)

- [C++ Classes](https://doc.qt.io/qt-6/qtgui-module.html)

- QFileSystemModel

On this page

# QFileSystemModel Class

The QFileSystemModel class provides a data model for the local filesystem. [More...](https://doc.qt.io/qt-6/qfilesystemmodel.html#details)

 Header:`#include <QFileSystemModel>` CMake:`find_package(Qt6 REQUIRED COMPONENTS Gui)`
`target_link_libraries(mytarget PRIVATE Qt6::Gui)` qmake:`QT += gui` Inherits:[QAbstractItemModel](https://doc.qt.io/qt-6/qabstractitemmodel.html)

- [List of all members, including inherited members](https://doc.qt.io/qt-6/qfilesystemmodel-members.html)

## Public Types[https://doc.qt.io/qt-6/qfilesystemmodel.html#public-types](https://doc.qt.io/qt-6/qfilesystemmodel.html#public-types)

 enum [Option](https://doc.qt.io/qt-6/qfilesystemmodel.html#Option-enum)  { DontWatchForChanges, DontResolveSymlinks, DontUseCustomDirectoryIcons }  flags [Options](https://doc.qt.io/qt-6/qfilesystemmodel.html#Option-enum)  enum [Roles](https://doc.qt.io/qt-6/qfilesystemmodel.html#Roles-enum)  { FileIconRole, FilePathRole, FileNameRole, FilePermissions, FileInfoRole }

## Properties[https://doc.qt.io/qt-6/qfilesystemmodel.html#properties](https://doc.qt.io/qt-6/qfilesystemmodel.html#properties)

- [nameFilterDisables](https://doc.qt.io/qt-6/qfilesystemmodel.html#nameFilterDisables-prop)  : bool

- [options](https://doc.qt.io/qt-6/qfilesystemmodel.html#options-prop)  : Options

- [readOnly](https://doc.qt.io/qt-6/qfilesystemmodel.html#readOnly-prop)  : bool

- [resolveSymlinks](https://doc.qt.io/qt-6/qfilesystemmodel.html#resolveSymlinks-prop)  : bool

## Public Functions[https://doc.qt.io/qt-6/qfilesystemmodel.html#public-functions](https://doc.qt.io/qt-6/qfilesystemmodel.html#public-functions)

[QFileSystemModel](https://doc.qt.io/qt-6/qfilesystemmodel.html#QFileSystemModel) (QObject * parent  = nullptr)  virtual [~QFileSystemModel](https://doc.qt.io/qt-6/qfilesystemmodel.html#dtor.QFileSystemModel) ()  QIcon [fileIcon](https://doc.qt.io/qt-6/qfilesystemmodel.html#fileIcon) (const QModelIndex & index ) const  QFileInfo [fileInfo](https://doc.qt.io/qt-6/qfilesystemmodel.html#fileInfo) (const QModelIndex & index ) const  QString [fileName](https://doc.qt.io/qt-6/qfilesystemmodel.html#fileName) (const QModelIndex & index ) const  QString [filePath](https://doc.qt.io/qt-6/qfilesystemmodel.html#filePath) (const QModelIndex & index ) const  QDir::Filters [filter](https://doc.qt.io/qt-6/qfilesystemmodel.html#filter) () const  QAbstractFileIconProvider *[iconProvider](https://doc.qt.io/qt-6/qfilesystemmodel.html#iconProvider) () const  QModelIndex [index](https://doc.qt.io/qt-6/qfilesystemmodel.html#index-1) (const QString & path , int column  = 0) const  bool [isDir](https://doc.qt.io/qt-6/qfilesystemmodel.html#isDir) (const QModelIndex & index ) const  bool [isReadOnly](https://doc.qt.io/qt-6/qfilesystemmodel.html#readOnly-prop) () const  QDateTime [lastModified](https://doc.qt.io/qt-6/qfilesystemmodel.html#lastModified) (const QModelIndex & index ) const`(since 6.6)` QDateTime [lastModified](https://doc.qt.io/qt-6/qfilesystemmodel.html#lastModified-1) (const QModelIndex & index , const QTimeZone & tz ) const  QModelIndex [mkdir](https://doc.qt.io/qt-6/qfilesystemmodel.html#mkdir) (const QModelIndex & parent , const QString & name )  QVariant [myComputer](https://doc.qt.io/qt-6/qfilesystemmodel.html#myComputer) (int role  = Qt::DisplayRole) const  bool [nameFilterDisables](https://doc.qt.io/qt-6/qfilesystemmodel.html#nameFilterDisables-prop) () const  QStringList [nameFilters](https://doc.qt.io/qt-6/qfilesystemmodel.html#nameFilters) () const  QFileSystemModel::Options [options](https://doc.qt.io/qt-6/qfilesystemmodel.html#options-prop) () const  QFileDevice::Permissions [permissions](https://doc.qt.io/qt-6/qfilesystemmodel.html#permissions) (const QModelIndex & index ) const  bool [remove](https://doc.qt.io/qt-6/qfilesystemmodel.html#remove) (const QModelIndex & index )  bool [resolveSymlinks](https://doc.qt.io/qt-6/qfilesystemmodel.html#resolveSymlinks-prop) () const  bool [rmdir](https://doc.qt.io/qt-6/qfilesystemmodel.html#rmdir) (const QModelIndex & index )  QDir [rootDirectory](https://doc.qt.io/qt-6/qfilesystemmodel.html#rootDirectory) () const  QString [rootPath](https://doc.qt.io/qt-6/qfilesystemmodel.html#rootPath) () const  void [setFilter](https://doc.qt.io/qt-6/qfilesystemmodel.html#setFilter) (QDir::Filters filters )  void [setIconProvider](https://doc.qt.io/qt-6/qfilesystemmodel.html#setIconProvider) (QAbstractFileIconProvider * provider )  void [setNameFilterDisables](https://doc.qt.io/qt-6/qfilesystemmodel.html#nameFilterDisables-prop) (bool enable )  void [setNameFilters](https://doc.qt.io/qt-6/qfilesystemmodel.html#setNameFilters) (const QStringList & filters )  void [setOption](https://doc.qt.io/qt-6/qfilesystemmodel.html#setOption) (QFileSystemModel::Option option , bool on  = true)  void [setOptions](https://doc.qt.io/qt-6/qfilesystemmodel.html#options-prop) (QFileSystemModel::Options options )  void [setReadOnly](https://doc.qt.io/qt-6/qfilesystemmodel.html#readOnly-prop) (bool enable )  void [setResolveSymlinks](https://doc.qt.io/qt-6/qfilesystemmodel.html#resolveSymlinks-prop) (bool enable )  QModelIndex [setRootPath](https://doc.qt.io/qt-6/qfilesystemmodel.html#setRootPath) (const QString & newPath )  qint64 [size](https://doc.qt.io/qt-6/qfilesystemmodel.html#size) (const QModelIndex & index ) const  bool [testOption](https://doc.qt.io/qt-6/qfilesystemmodel.html#testOption) (QFileSystemModel::Option option ) const  QString [type](https://doc.qt.io/qt-6/qfilesystemmodel.html#type) (const QModelIndex & index ) const

## Reimplemented Public Functions[https://doc.qt.io/qt-6/qfilesystemmodel.html#reimplemented-public-functions](https://doc.qt.io/qt-6/qfilesystemmodel.html#reimplemented-public-functions)

 virtual bool [canFetchMore](https://doc.qt.io/qt-6/qfilesystemmodel.html#canFetchMore) (const QModelIndex & parent ) const override  virtual int [columnCount](https://doc.qt.io/qt-6/qfilesystemmodel.html#columnCount) (const QModelIndex & parent  = QModelIndex()) const override  virtual QVariant [data](https://doc.qt.io/qt-6/qfilesystemmodel.html#data) (const QModelIndex & index , int role  = Qt::DisplayRole) const override  virtual bool [dropMimeData](https://doc.qt.io/qt-6/qfilesystemmodel.html#dropMimeData) (const QMimeData * data , Qt::DropAction action , int row , int column , const QModelIndex & parent ) override  virtual void [fetchMore](https://doc.qt.io/qt-6/qfilesystemmodel.html#fetchMore) (const QModelIndex & parent ) override  virtual Qt::ItemFlags [flags](https://doc.qt.io/qt-6/qfilesystemmodel.html#flags) (const QModelIndex & index ) const override  virtual bool [hasChildren](https://doc.qt.io/qt-6/qfilesystemmodel.html#hasChildren) (const QModelIndex & parent  = QModelIndex()) const override  virtual QVariant [headerData](https://doc.qt.io/qt-6/qfilesystemmodel.html#headerData) (int section , Qt::Orientation orientation , int role  = Qt::DisplayRole) const override  virtual QModelIndex [index](https://doc.qt.io/qt-6/qfilesystemmodel.html#index) (int row , int column , const QModelIndex & parent  = QModelIndex()) const override  virtual QMimeData *[mimeData](https://doc.qt.io/qt-6/qfilesystemmodel.html#mimeData) (const QModelIndexList & indexes ) const override  virtual QStringList [mimeTypes](https://doc.qt.io/qt-6/qfilesystemmodel.html#mimeTypes) () const override  virtual QModelIndex [parent](https://doc.qt.io/qt-6/qfilesystemmodel.html#parent) (const QModelIndex & index ) const override  virtual QHash<int, QByteArray> [roleNames](https://doc.qt.io/qt-6/qfilesystemmodel.html#roleNames) () const override  virtual int [rowCount](https://doc.qt.io/qt-6/qfilesystemmodel.html#rowCount) (const QModelIndex & parent  = QModelIndex()) const override  virtual bool [setData](https://doc.qt.io/qt-6/qfilesystemmodel.html#setData) (const QModelIndex & idx , const QVariant & value , int role  = Qt::EditRole) override  virtual QModelIndex [sibling](https://doc.qt.io/qt-6/qfilesystemmodel.html#sibling) (int row , int column , const QModelIndex & idx ) const override  virtual void [sort](https://doc.qt.io/qt-6/qfilesystemmodel.html#sort) (int column , Qt::SortOrder order  = Qt::AscendingOrder) override  virtual Qt::DropActions [supportedDropActions](https://doc.qt.io/qt-6/qfilesystemmodel.html#supportedDropActions) () const override

## Signals[https://doc.qt.io/qt-6/qfilesystemmodel.html#signals](https://doc.qt.io/qt-6/qfilesystemmodel.html#signals)

 void [directoryLoaded](https://doc.qt.io/qt-6/qfilesystemmodel.html#directoryLoaded) (const QString & path )  void [fileRenamed](https://doc.qt.io/qt-6/qfilesystemmodel.html#fileRenamed) (const QString & path , const QString & oldName , const QString & newName )  void [rootPathChanged](https://doc.qt.io/qt-6/qfilesystemmodel.html#rootPathChanged) (const QString & newPath )

## Reimplemented Protected Functions[https://doc.qt.io/qt-6/qfilesystemmodel.html#reimplemented-protected-functions](https://doc.qt.io/qt-6/qfilesystemmodel.html#reimplemented-protected-functions)

 virtual bool [event](https://doc.qt.io/qt-6/qfilesystemmodel.html#event) (QEvent * event ) override  virtual void [timerEvent](https://doc.qt.io/qt-6/qfilesystemmodel.html#timerEvent) (QTimerEvent * event ) override

## Detailed Description[https://doc.qt.io/qt-6/qfilesystemmodel.html#details](https://doc.qt.io/qt-6/qfilesystemmodel.html#details)

This class provides access to the local filesystem, providing functions for renaming and removing files and directories, and for creating new directories. In the simplest case, it can be used with a suitable display widget as part of a browser or filter.

QFileSystemModel can be accessed using the standard interface provided by [QAbstractItemModel](https://doc.qt.io/qt-6/qabstractitemmodel.html) , but it also provides some convenience functions that are specific to a directory model. The [fileInfo](https://doc.qt.io/qt-6/qfilesystemmodel.html#fileInfo) (), [isDir](https://doc.qt.io/qt-6/qfilesystemmodel.html#isDir) (), [fileName](https://doc.qt.io/qt-6/qfilesystemmodel.html#fileName) () and [filePath](https://doc.qt.io/qt-6/qfilesystemmodel.html#filePath) () functions provide information about the underlying files and directories related to items in the model. Directories can be created and removed using [mkdir](https://doc.qt.io/qt-6/qfilesystemmodel.html#mkdir) (), [rmdir](https://doc.qt.io/qt-6/qfilesystemmodel.html#rmdir) ().

### Example Usage[https://doc.qt.io/qt-6/qfilesystemmodel.html#example-usage](https://doc.qt.io/qt-6/qfilesystemmodel.html#example-usage)

A directory model that displays the contents of a default directory is usually constructed with a parent object:

[https://doc.qt.io/qt-6/qfilesystemmodel.html](https://doc.qt.io/qt-6/qfilesystemmodel.html)[https://doc.qt.io/qt-6/qfilesystemmodel.html](https://doc.qt.io/qt-6/qfilesystemmodel.html)[https://doc.qt.io/qt-6/qdir.html](https://doc.qt.io/qt-6/qdir.html)```
QFileSystemModel *model = new QFileSystemModel;
model->setRootPath(QDir::currentPath());
```

A tree view can be used to display the contents of the model

[https://doc.qt.io/qt-6/qtreeview.html](https://doc.qt.io/qt-6/qtreeview.html)[https://doc.qt.io/qt-6/qtreeview.html](https://doc.qt.io/qt-6/qtreeview.html)```
QTreeView *tree = new QTreeView(splitter);
tree->setModel(model);
```

and the contents of a particular directory can be displayed by setting the tree view's root index:

[https://doc.qt.io/qt-6/qdir.html](https://doc.qt.io/qt-6/qdir.html)```
tree->setRootIndex(model->index(QDir::currentPath()));
```

The view's root index can be used to control how much of a hierarchical model is displayed. QFileSystemModel provides a convenience function that returns a suitable model index for a path to a directory within the model.

### Caching and Performance[https://doc.qt.io/qt-6/qfilesystemmodel.html#caching-and-performance](https://doc.qt.io/qt-6/qfilesystemmodel.html#caching-and-performance)

QFileSystemModel uses a separate thread to populate itself, so it will not cause the main thread to hang as the file system is being queried. Calls to [rowCount](https://doc.qt.io/qt-6/qfilesystemmodel.html#rowCount) () will return `0` until the model populates a directory. The thread in which the QFileSystemModel lives needs to run an event loop to process the incoming data.

QFileSystemModel will not start populating itself until [setRootPath](https://doc.qt.io/qt-6/qfilesystemmodel.html#setRootPath) () is called. This prevents any unnecessary querying of the system's root file system, such as enumerating the drives on Windows, until that point.

QFileSystemModel keeps a cache with file information. The cache is automatically kept up to date using the [QFileSystemWatcher](https://doc.qt.io/qt-6/qfilesystemwatcher.html) .

See also [Model Classes](https://doc.qt.io/qt-6/model-view-programming.html#model-classes) .

## Member Type Documentation

### enum QFileSystemModel:: Option
flags QFileSystemModel:: Options[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n52](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n52)[https://doc.qt.io/qt-6/qfilesystemmodel.html#Option-enum](https://doc.qt.io/qt-6/qfilesystemmodel.html#Option-enum)

Constant Value Description`QFileSystemModel::DontWatchForChanges``0x00000001`Do not add file watchers to the paths. This reduces overhead when using the model for simple tasks like line edit completion.`QFileSystemModel::DontResolveSymlinks``0x00000002`Don't resolve symlinks in the file system model. By default, symlinks are resolved.`QFileSystemModel::DontUseCustomDirectoryIcons``0x00000004`Always use the default directory icon. Some platforms allow the user to set a different icon. Custom icon lookup causes a big performance impact over network or removable drives. This sets the QFileIconProvider::DontUseCustomDirectoryIcons option in the icon provider accordingly.

The Options type is a typedef for [QFlags](https://doc.qt.io/qt-6/qflags.html) <Option>. It stores an OR combination of Option values.

See also [resolveSymlinks](https://doc.qt.io/qt-6/qfilesystemmodel.html#resolveSymlinks-prop) .

### enum QFileSystemModel:: Roles[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n35](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n35)[https://doc.qt.io/qt-6/qfilesystemmodel.html#Roles-enum](https://doc.qt.io/qt-6/qfilesystemmodel.html#Roles-enum)

Constant Value Description`QFileSystemModel::FileIconRole``Qt::DecorationRole``QFileSystemModel::FilePathRole``Qt::UserRole + 1``QFileSystemModel::FileNameRole``Qt::UserRole + 2``QFileSystemModel::FilePermissions``Qt::UserRole + 3``QFileSystemModel::FileInfoRole``Qt::FileInfoRole`The [QFileInfo](https://doc.qt.io/qt-6/qfileinfo.html)  object for the index

## Property Documentation

### nameFilterDisables  : bool[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n26](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n26)[https://doc.qt.io/qt-6/qfilesystemmodel.html#nameFilterDisables-prop](https://doc.qt.io/qt-6/qfilesystemmodel.html#nameFilterDisables-prop)

This property holds whether files that don't pass the name filter are hidden or disabled

This property is `true` by default

Access functions:

 bool nameFilterDisables () const  void setNameFilterDisables (bool enable )

### options  : [Options](https://doc.qt.io/qt-6/qfilesystemmodel.html#Option-enum)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n27](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n27)[https://doc.qt.io/qt-6/qfilesystemmodel.html#options-prop](https://doc.qt.io/qt-6/qfilesystemmodel.html#options-prop)

This property holds the various options that affect the model

By default, all options are disabled.

Options should be set before changing properties.

Access functions:

 QFileSystemModel::Options options () const  void setOptions (QFileSystemModel::Options options )

See also [setOption](https://doc.qt.io/qt-6/qfilesystemmodel.html#setOption) () and [testOption](https://doc.qt.io/qt-6/qfilesystemmodel.html#testOption) ().

### readOnly  : bool[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n25](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n25)[https://doc.qt.io/qt-6/qfilesystemmodel.html#readOnly-prop](https://doc.qt.io/qt-6/qfilesystemmodel.html#readOnly-prop)

This property holds whether the directory model allows writing to the file system

If this property is set to false, the directory model will allow renaming, copying and deleting of files and directories.

This property is `true` by default

Access functions:

 bool isReadOnly () const  void setReadOnly (bool enable )

### resolveSymlinks  : bool[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n24](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n24)[https://doc.qt.io/qt-6/qfilesystemmodel.html#resolveSymlinks-prop](https://doc.qt.io/qt-6/qfilesystemmodel.html#resolveSymlinks-prop)

This property holds whether the directory model should resolve symbolic links

This is only relevant on Windows.

By default, this property is `true`.

Access functions:

 bool resolveSymlinks () const  void setResolveSymlinks (bool enable )

See also [QFileSystemModel::Options](https://doc.qt.io/qt-6/qfilesystemmodel.html#Option-enum) .

## Member Function Documentation

### `[explicit]` QFileSystemModel:: QFileSystemModel ([QObject](https://doc.qt.io/qt-6/qobject.html)  * parent  = nullptr)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n61](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n61)[https://doc.qt.io/qt-6/qfilesystemmodel.html#QFileSystemModel](https://doc.qt.io/qt-6/qfilesystemmodel.html#QFileSystemModel)

Constructs a file system model with the given parent .

### `[virtual noexcept]` QFileSystemModel:: ~QFileSystemModel ()[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n62](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n62)[https://doc.qt.io/qt-6/qfilesystemmodel.html#dtor.QFileSystemModel](https://doc.qt.io/qt-6/qfilesystemmodel.html#dtor.QFileSystemModel)

Destroys this file system model.

### `[override virtual]`bool  QFileSystemModel:: canFetchMore (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n70](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n70)[https://doc.qt.io/qt-6/qfilesystemmodel.html#canFetchMore](https://doc.qt.io/qt-6/qfilesystemmodel.html#canFetchMore)

Reimplements: [QAbstractItemModel::canFetchMore](https://doc.qt.io/qt-6/qabstractitemmodel.html#canFetchMore) (const QModelIndex &parent) const.

### `[override virtual]`int  QFileSystemModel:: columnCount (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent  = QModelIndex()) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n74](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n74)[https://doc.qt.io/qt-6/qfilesystemmodel.html#columnCount](https://doc.qt.io/qt-6/qfilesystemmodel.html#columnCount)

Reimplements: [QAbstractItemModel::columnCount](https://doc.qt.io/qt-6/qabstractitemmodel.html#columnCount) (const QModelIndex &parent) const.

### `[override virtual]`[QVariant](https://doc.qt.io/qt-6/qvariant.html)  QFileSystemModel:: data (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index , int role  = Qt::DisplayRole) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n77](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n77)[https://doc.qt.io/qt-6/qfilesystemmodel.html#data](https://doc.qt.io/qt-6/qfilesystemmodel.html#data)

Reimplements: [QAbstractItemModel::data](https://doc.qt.io/qt-6/qabstractitemmodel.html#data) (const QModelIndex &index, int role) const.

See also [setData](https://doc.qt.io/qt-6/qfilesystemmodel.html#setData) ().

### `[signal]`void  QFileSystemModel:: directoryLoaded (const [QString](https://doc.qt.io/qt-6/qstring.html)  & path )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n32](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n32)[https://doc.qt.io/qt-6/qfilesystemmodel.html#directoryLoaded](https://doc.qt.io/qt-6/qfilesystemmodel.html#directoryLoaded)

This signal is emitted when the gatherer thread has finished to load the path .

### `[override virtual]`bool  QFileSystemModel:: dropMimeData (const [QMimeData](https://doc.qt.io/qt-6/qmimedata.html)  * data , [Qt::DropAction](https://doc.qt.io/qt-6/qt.html#DropAction-enum) action , int row , int column , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n88](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n88)[https://doc.qt.io/qt-6/qfilesystemmodel.html#dropMimeData](https://doc.qt.io/qt-6/qfilesystemmodel.html#dropMimeData)

Reimplements: [QAbstractItemModel::dropMimeData](https://doc.qt.io/qt-6/qabstractitemmodel.html#dropMimeData) (const QMimeData *data, Qt::DropAction action, int row, int column, const QModelIndex &parent).

Handles the data  supplied by a drag and drop operation that ended with the given action  over the row in the model specified by the row  and column  and by the parent  index. Returns true if the operation was successful.

See also [supportedDropActions](https://doc.qt.io/qt-6/qfilesystemmodel.html#supportedDropActions) ().

### `[override virtual protected]`bool  QFileSystemModel:: event ([QEvent](https://doc.qt.io/qt-6/qevent.html)  * event )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n140](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n140)[https://doc.qt.io/qt-6/qfilesystemmodel.html#event](https://doc.qt.io/qt-6/qfilesystemmodel.html#event)

Reimplements: [QObject::event](https://doc.qt.io/qt-6/qobject.html#event) (QEvent *e).

### `[override virtual]`void  QFileSystemModel:: fetchMore (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n71](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n71)[https://doc.qt.io/qt-6/qfilesystemmodel.html#fetchMore](https://doc.qt.io/qt-6/qfilesystemmodel.html#fetchMore)

Reimplements: [QAbstractItemModel::fetchMore](https://doc.qt.io/qt-6/qabstractitemmodel.html#fetchMore) (const QModelIndex &parent).

### [QIcon](https://doc.qt.io/qt-6/qicon.html)  QFileSystemModel:: fileIcon (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n132](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n132)[https://doc.qt.io/qt-6/qfilesystemmodel.html#fileIcon](https://doc.qt.io/qt-6/qfilesystemmodel.html#fileIcon)

Returns the icon for the item stored in the model under the given index .

### [QFileInfo](https://doc.qt.io/qt-6/qfileinfo.html)  QFileSystemModel:: fileInfo (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n134](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n134)[https://doc.qt.io/qt-6/qfilesystemmodel.html#fileInfo](https://doc.qt.io/qt-6/qfilesystemmodel.html#fileInfo)

Returns the [QFileInfo](https://doc.qt.io/qt-6/qfileinfo.html)  for the item stored in the model under the given index .

### [QString](https://doc.qt.io/qt-6/qstring.html)  QFileSystemModel:: fileName (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n131](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n131)[https://doc.qt.io/qt-6/qfilesystemmodel.html#fileName](https://doc.qt.io/qt-6/qfilesystemmodel.html#fileName)

Returns the file name for the item stored in the model under the given index .

### [QString](https://doc.qt.io/qt-6/qstring.html)  QFileSystemModel:: filePath (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n121](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n121)[https://doc.qt.io/qt-6/qfilesystemmodel.html#filePath](https://doc.qt.io/qt-6/qfilesystemmodel.html#filePath)

Returns the path of the item stored in the model under the index  given.

### `[signal]`void  QFileSystemModel:: fileRenamed (const [QString](https://doc.qt.io/qt-6/qstring.html)  & path , const [QString](https://doc.qt.io/qt-6/qstring.html)  & oldName , const [QString](https://doc.qt.io/qt-6/qstring.html)  & newName )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n31](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n31)[https://doc.qt.io/qt-6/qfilesystemmodel.html#fileRenamed](https://doc.qt.io/qt-6/qfilesystemmodel.html#fileRenamed)

This signal is emitted whenever a file with the oldName  is successfully renamed to newName . The file is located in the directory path .

### [QDir::Filters](https://doc.qt.io/qt-6/qdir.html#Filter-enum)  QFileSystemModel:: filter () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n102](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n102)[https://doc.qt.io/qt-6/qfilesystemmodel.html#filter](https://doc.qt.io/qt-6/qfilesystemmodel.html#filter)

Returns the filter specified for the directory model.

If a filter has not been set, the default filter is [QDir::AllEntries](https://doc.qt.io/qt-6/qdir.html#Filter-enum)  | [QDir::NoDotAndDotDot](https://doc.qt.io/qt-6/qdir.html#Filter-enum)  | [QDir::AllDirs](https://doc.qt.io/qt-6/qdir.html#Filter-enum) .

See also [setFilter](https://doc.qt.io/qt-6/qfilesystemmodel.html#setFilter) () and [QDir::Filters](https://doc.qt.io/qt-6/qdir.html#Filter-enum) .

### `[override virtual]`[Qt::ItemFlags](https://doc.qt.io/qt-6/qt.html#ItemFlag-enum)  QFileSystemModel:: flags (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n82](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n82)[https://doc.qt.io/qt-6/qfilesystemmodel.html#flags](https://doc.qt.io/qt-6/qfilesystemmodel.html#flags)

Reimplements: [QAbstractItemModel::flags](https://doc.qt.io/qt-6/qabstractitemmodel.html#flags) (const QModelIndex &index) const.

### `[override virtual]`bool  QFileSystemModel:: hasChildren (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent  = QModelIndex()) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n69](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n69)[https://doc.qt.io/qt-6/qfilesystemmodel.html#hasChildren](https://doc.qt.io/qt-6/qfilesystemmodel.html#hasChildren)

Reimplements: [QAbstractItemModel::hasChildren](https://doc.qt.io/qt-6/qabstractitemmodel.html#hasChildren) (const QModelIndex &parent) const.

### `[override virtual]`[QVariant](https://doc.qt.io/qt-6/qvariant.html)  QFileSystemModel:: headerData (int section , [Qt::Orientation](https://doc.qt.io/qt-6/qt.html#Orientation-enum) orientation , int role  = Qt::DisplayRole) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n80](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n80)[https://doc.qt.io/qt-6/qfilesystemmodel.html#headerData](https://doc.qt.io/qt-6/qfilesystemmodel.html#headerData)

Reimplements: [QAbstractItemModel::headerData](https://doc.qt.io/qt-6/qabstractitemmodel.html#headerData) (int section, Qt::Orientation orientation, int role) const.

### [QAbstractFileIconProvider](https://doc.qt.io/qt-6/qabstractfileiconprovider.html)  *QFileSystemModel:: iconProvider () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n99](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n99)[https://doc.qt.io/qt-6/qfilesystemmodel.html#iconProvider](https://doc.qt.io/qt-6/qfilesystemmodel.html#iconProvider)

Returns the file icon provider for this directory model.

See also [setIconProvider](https://doc.qt.io/qt-6/qfilesystemmodel.html#setIconProvider) ().

### `[override virtual]`[QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  QFileSystemModel:: index (int row , int column , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent  = QModelIndex()) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n64](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n64)[https://doc.qt.io/qt-6/qfilesystemmodel.html#index](https://doc.qt.io/qt-6/qfilesystemmodel.html#index)

Reimplements: [QAbstractItemModel::index](https://doc.qt.io/qt-6/qabstractitemmodel.html#index) (int row, int column, const QModelIndex &parent) const.

### [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  QFileSystemModel:: index (const [QString](https://doc.qt.io/qt-6/qstring.html)  & path , int column  = 0) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n65](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n65)[https://doc.qt.io/qt-6/qfilesystemmodel.html#index-1](https://doc.qt.io/qt-6/qfilesystemmodel.html#index-1)

Returns the model item index for the given path  and column .

This is an overloaded function.

### bool  QFileSystemModel:: isDir (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n122](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n122)[https://doc.qt.io/qt-6/qfilesystemmodel.html#isDir](https://doc.qt.io/qt-6/qfilesystemmodel.html#isDir)

Returns `true` if the model item index  represents a directory; otherwise returns `false`.

### [QDateTime](https://doc.qt.io/qt-6/qdatetime.html)  QFileSystemModel:: lastModified (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n126](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n126)[https://doc.qt.io/qt-6/qfilesystemmodel.html#lastModified](https://doc.qt.io/qt-6/qfilesystemmodel.html#lastModified)

Returns the date and time (in local time) when index  was last modified.

This is an overloaded function, equivalent to calling:

[https://doc.qt.io/qt-6/qtimezone.html](https://doc.qt.io/qt-6/qtimezone.html)```
lastModified(index, QTimeZone::LocalTime);
```

If index  is invalid, a default constructed [QDateTime](https://doc.qt.io/qt-6/qdatetime.html)  is returned.

### `[since 6.6]`[QDateTime](https://doc.qt.io/qt-6/qdatetime.html)  QFileSystemModel:: lastModified (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index , const [QTimeZone](https://doc.qt.io/qt-6/qtimezone.html)  & tz ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n127](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n127)[https://doc.qt.io/qt-6/qfilesystemmodel.html#lastModified-1](https://doc.qt.io/qt-6/qfilesystemmodel.html#lastModified-1)

Returns the date and time, in the time zone tz , when index  was last modified.

Typical arguments for tz  are `QTimeZone::UTC` or `QTimeZone::LocalTime`. UTC does not require any conversion from the time returned by the native file system API, therefore getting the time in UTC is potentially faster. LocalTime is typically chosen if the time is shown to the user.

If index  is invalid, a default constructed [QDateTime](https://doc.qt.io/qt-6/qdatetime.html)  is returned.

This function was introduced in Qt 6.6.

### `[override virtual]`[QMimeData](https://doc.qt.io/qt-6/qmimedata.html)  *QFileSystemModel:: mimeData (const [QModelIndexList](https://doc.qt.io/qt-6/qmodelindex.html#QModelIndexList-typedef)  & indexes ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n87](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n87)[https://doc.qt.io/qt-6/qfilesystemmodel.html#mimeData](https://doc.qt.io/qt-6/qfilesystemmodel.html#mimeData)

Reimplements: [QAbstractItemModel::mimeData](https://doc.qt.io/qt-6/qabstractitemmodel.html#mimeData) (const QModelIndexList &indexes) const.

Returns an object that contains a serialized description of the specified indexes . The format used to describe the items corresponding to the indexes is obtained from the [mimeTypes](https://doc.qt.io/qt-6/qfilesystemmodel.html#mimeTypes) () function.

If the list of indexes is empty, `nullptr` is returned rather than a serialized empty list.

### `[override virtual]`[QStringList](https://doc.qt.io/qt-6/qstringlist.html)  QFileSystemModel:: mimeTypes () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n86](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n86)[https://doc.qt.io/qt-6/qfilesystemmodel.html#mimeTypes](https://doc.qt.io/qt-6/qfilesystemmodel.html#mimeTypes)

Reimplements: [QAbstractItemModel::mimeTypes](https://doc.qt.io/qt-6/qabstractitemmodel.html#mimeTypes) () const.

Returns a list of MIME types that can be used to describe a list of items in the model.

### [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  QFileSystemModel:: mkdir (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent , const [QString](https://doc.qt.io/qt-6/qstring.html)  & name )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n129](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n129)[https://doc.qt.io/qt-6/qfilesystemmodel.html#mkdir](https://doc.qt.io/qt-6/qfilesystemmodel.html#mkdir)

Create a directory with the name  in the parent  model index.

### [QVariant](https://doc.qt.io/qt-6/qvariant.html)  QFileSystemModel:: myComputer (int role  = Qt::DisplayRole) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n76](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n76)[https://doc.qt.io/qt-6/qfilesystemmodel.html#myComputer](https://doc.qt.io/qt-6/qfilesystemmodel.html#myComputer)

Returns the data stored under the given role  for the item "My Computer".

See also [Qt::ItemDataRole](https://doc.qt.io/qt-6/qt.html#ItemDataRole-enum) .

### [QStringList](https://doc.qt.io/qt-6/qstringlist.html)  QFileSystemModel:: nameFilters () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n114](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n114)[https://doc.qt.io/qt-6/qfilesystemmodel.html#nameFilters](https://doc.qt.io/qt-6/qfilesystemmodel.html#nameFilters)

Returns a list of filters applied to the names in the model.

See also [setNameFilters](https://doc.qt.io/qt-6/qfilesystemmodel.html#setNameFilters) ().

### `[override virtual]`[QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  QFileSystemModel:: parent (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n66](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n66)[https://doc.qt.io/qt-6/qfilesystemmodel.html#parent](https://doc.qt.io/qt-6/qfilesystemmodel.html#parent)

Reimplements: [QAbstractItemModel::parent](https://doc.qt.io/qt-6/qabstractitemmodel.html#parent) (const QModelIndex &index) const.

### [QFileDevice::Permissions](https://doc.qt.io/qt-6/qfiledevice.html#Permission-enum)  QFileSystemModel:: permissions (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n133](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n133)[https://doc.qt.io/qt-6/qfilesystemmodel.html#permissions](https://doc.qt.io/qt-6/qfilesystemmodel.html#permissions)

Returns the complete OR-ed together combination of QFile::Permission for the index .

### bool  QFileSystemModel:: remove (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n135](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n135)[https://doc.qt.io/qt-6/qfilesystemmodel.html#remove](https://doc.qt.io/qt-6/qfilesystemmodel.html#remove)

Removes the model item index  from the file system model and deletes the corresponding file from the file system , returning true if successful. If the item cannot be removed, false is returned.

Warning: This function deletes files from the file system; it does not  move them to a location where they can be recovered.

See also [rmdir](https://doc.qt.io/qt-6/qfilesystemmodel.html#rmdir) ().

### bool  QFileSystemModel:: rmdir (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n130](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n130)[https://doc.qt.io/qt-6/qfilesystemmodel.html#rmdir](https://doc.qt.io/qt-6/qfilesystemmodel.html#rmdir)

Removes the directory corresponding to the model item index  in the file system model and deletes the corresponding directory from the file system , returning true if successful. If the directory cannot be removed, false is returned.

Warning: This function deletes directories from the file system; it does not  move them to a location where they can be recovered.

See also [remove](https://doc.qt.io/qt-6/qfilesystemmodel.html#remove) ().

### `[override virtual]`[QHash](https://doc.qt.io/qt-6/qhash.html) < int , [QByteArray](https://doc.qt.io/qt-6/qbytearray.html) > QFileSystemModel:: roleNames () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n91](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n91)[https://doc.qt.io/qt-6/qfilesystemmodel.html#roleNames](https://doc.qt.io/qt-6/qfilesystemmodel.html#roleNames)

Reimplements: [QAbstractItemModel::roleNames](https://doc.qt.io/qt-6/qabstractitemmodel.html#roleNames) () const.

### [QDir](https://doc.qt.io/qt-6/qdir.html)  QFileSystemModel:: rootDirectory () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n96](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n96)[https://doc.qt.io/qt-6/qfilesystemmodel.html#rootDirectory](https://doc.qt.io/qt-6/qfilesystemmodel.html#rootDirectory)

The currently set directory

See also [rootPath](https://doc.qt.io/qt-6/qfilesystemmodel.html#rootPath) ().

### [QString](https://doc.qt.io/qt-6/qstring.html)  QFileSystemModel:: rootPath () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n95](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n95)[https://doc.qt.io/qt-6/qfilesystemmodel.html#rootPath](https://doc.qt.io/qt-6/qfilesystemmodel.html#rootPath)

The currently set root path

See also [setRootPath](https://doc.qt.io/qt-6/qfilesystemmodel.html#setRootPath) () and [rootDirectory](https://doc.qt.io/qt-6/qfilesystemmodel.html#rootDirectory) ().

### `[signal]`void  QFileSystemModel:: rootPathChanged (const [QString](https://doc.qt.io/qt-6/qstring.html)  & newPath )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n30](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n30)[https://doc.qt.io/qt-6/qfilesystemmodel.html#rootPathChanged](https://doc.qt.io/qt-6/qfilesystemmodel.html#rootPathChanged)

This signal is emitted whenever the root path has been changed to a newPath .

### `[override virtual]`int  QFileSystemModel:: rowCount (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & parent  = QModelIndex()) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n73](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n73)[https://doc.qt.io/qt-6/qfilesystemmodel.html#rowCount](https://doc.qt.io/qt-6/qfilesystemmodel.html#rowCount)

Reimplements: [QAbstractItemModel::rowCount](https://doc.qt.io/qt-6/qabstractitemmodel.html#rowCount) (const QModelIndex &parent) const.

### `[override virtual]`bool  QFileSystemModel:: setData (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & idx , const [QVariant](https://doc.qt.io/qt-6/qvariant.html)  & value , int role  = Qt::EditRole)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n78](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n78)[https://doc.qt.io/qt-6/qfilesystemmodel.html#setData](https://doc.qt.io/qt-6/qfilesystemmodel.html#setData)

Reimplements: [QAbstractItemModel::setData](https://doc.qt.io/qt-6/qabstractitemmodel.html#setData) (const QModelIndex &index, const QVariant &value, int role).

See also [data](https://doc.qt.io/qt-6/qfilesystemmodel.html#data) ().

### void  QFileSystemModel:: setFilter ([QDir::Filters](https://doc.qt.io/qt-6/qdir.html#Filter-enum) filters )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n101](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n101)[https://doc.qt.io/qt-6/qfilesystemmodel.html#setFilter](https://doc.qt.io/qt-6/qfilesystemmodel.html#setFilter)

Sets the directory model's filter to that specified by filters .

Note that the filter you set should always include the [QDir::AllDirs](https://doc.qt.io/qt-6/qdir.html#Filter-enum)  enum value, otherwise [QFileSystemModel](https://doc.qt.io/qt-6/qfilesystemmodel.html)  won't be able to read the directory structure.

See also [filter](https://doc.qt.io/qt-6/qfilesystemmodel.html#filter) () and [QDir::Filters](https://doc.qt.io/qt-6/qdir.html#Filter-enum) .

### void  QFileSystemModel:: setIconProvider ([QAbstractFileIconProvider](https://doc.qt.io/qt-6/qabstractfileiconprovider.html)  * provider )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n98](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n98)[https://doc.qt.io/qt-6/qfilesystemmodel.html#setIconProvider](https://doc.qt.io/qt-6/qfilesystemmodel.html#setIconProvider)

Sets the provider  of file icons for the directory model.

See also [iconProvider](https://doc.qt.io/qt-6/qfilesystemmodel.html#iconProvider) ().

### void  QFileSystemModel:: setNameFilters (const [QStringList](https://doc.qt.io/qt-6/qstringlist.html)  & filters )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n113](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n113)[https://doc.qt.io/qt-6/qfilesystemmodel.html#setNameFilters](https://doc.qt.io/qt-6/qfilesystemmodel.html#setNameFilters)

Sets the name filters  to apply against the existing files.

See also [nameFilters](https://doc.qt.io/qt-6/qfilesystemmodel.html#nameFilters) ().

### void  QFileSystemModel:: setOption ([QFileSystemModel::Option](https://doc.qt.io/qt-6/qfilesystemmodel.html#Option-enum) option , bool on  = true)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n116](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n116)[https://doc.qt.io/qt-6/qfilesystemmodel.html#setOption](https://doc.qt.io/qt-6/qfilesystemmodel.html#setOption)

Sets the given option  to be enabled if on  is true; otherwise, clears the given option .

Options should be set before changing properties.

See also [options](https://doc.qt.io/qt-6/qfilesystemmodel.html#options-prop)  and [testOption](https://doc.qt.io/qt-6/qfilesystemmodel.html#testOption) ().

### [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  QFileSystemModel:: setRootPath (const [QString](https://doc.qt.io/qt-6/qstring.html)  & newPath )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n94](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n94)[https://doc.qt.io/qt-6/qfilesystemmodel.html#setRootPath](https://doc.qt.io/qt-6/qfilesystemmodel.html#setRootPath)

Sets the directory that is being watched by the model to newPath  by installing a [file system watcher](https://doc.qt.io/qt-6/qfilesystemwatcher.html)  on it. Any changes to files and directories within this directory will be reflected in the model.

If the path is changed, the [rootPathChanged](https://doc.qt.io/qt-6/qfilesystemmodel.html#rootPathChanged) () signal will be emitted.

Note: This function does not change the structure of the model or modify the data available to views. In other words, the "root" of the model is not  changed to include only files and directories within the directory specified by newPath  in the file system.

See also [rootPath](https://doc.qt.io/qt-6/qfilesystemmodel.html#rootPath) (), [QTreeView::setRootIndex](https://doc.qt.io/qt-6/qtreeview.html#setRootIndex) (), and [TreeView::rootIndex](https://doc.qt.io/qt-6/qml-qtquick-treeview.html#rootIndex-prop) .

### `[override virtual]`[QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  QFileSystemModel:: sibling (int row , int column , const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & idx ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n68](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n68)[https://doc.qt.io/qt-6/qfilesystemmodel.html#sibling](https://doc.qt.io/qt-6/qfilesystemmodel.html#sibling)

Reimplements: [QAbstractItemModel::sibling](https://doc.qt.io/qt-6/qabstractitemmodel.html#sibling) (int row, int column, const QModelIndex &index) const.

### [qint64](https://doc.qt.io/qt-6/qttypes.html#qint64-typedef)  QFileSystemModel:: size (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n123](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n123)[https://doc.qt.io/qt-6/qfilesystemmodel.html#size](https://doc.qt.io/qt-6/qfilesystemmodel.html#size)

Returns the size in bytes of index . If the file does not exist, 0 is returned.

### `[override virtual]`void  QFileSystemModel:: sort (int column , [Qt::SortOrder](https://doc.qt.io/qt-6/qt.html#SortOrder-enum) order  = Qt::AscendingOrder)[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n84](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n84)[https://doc.qt.io/qt-6/qfilesystemmodel.html#sort](https://doc.qt.io/qt-6/qfilesystemmodel.html#sort)

Reimplements: [QAbstractItemModel::sort](https://doc.qt.io/qt-6/qabstractitemmodel.html#sort) (int column, Qt::SortOrder order).

### `[override virtual]`[Qt::DropActions](https://doc.qt.io/qt-6/qt.html#DropAction-enum)  QFileSystemModel:: supportedDropActions () const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n90](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n90)[https://doc.qt.io/qt-6/qfilesystemmodel.html#supportedDropActions](https://doc.qt.io/qt-6/qfilesystemmodel.html#supportedDropActions)

Reimplements: [QAbstractItemModel::supportedDropActions](https://doc.qt.io/qt-6/qabstractitemmodel.html#supportedDropActions) () const.

### bool  QFileSystemModel:: testOption ([QFileSystemModel::Option](https://doc.qt.io/qt-6/qfilesystemmodel.html#Option-enum) option ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n117](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n117)[https://doc.qt.io/qt-6/qfilesystemmodel.html#testOption](https://doc.qt.io/qt-6/qfilesystemmodel.html#testOption)

Returns `true` if the given option  is enabled; otherwise, returns false.

See also [options](https://doc.qt.io/qt-6/qfilesystemmodel.html#options-prop)  and [setOption](https://doc.qt.io/qt-6/qfilesystemmodel.html#setOption) ().

### `[override virtual protected]`void  QFileSystemModel:: timerEvent ([QTimerEvent](https://doc.qt.io/qt-6/qtimerevent.html)  * event )[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n139](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n139)[https://doc.qt.io/qt-6/qfilesystemmodel.html#timerEvent](https://doc.qt.io/qt-6/qfilesystemmodel.html#timerEvent)

Reimplements: [QObject::timerEvent](https://doc.qt.io/qt-6/qobject.html#timerEvent) (QTimerEvent *event).

### [QString](https://doc.qt.io/qt-6/qstring.html)  QFileSystemModel:: type (const [QModelIndex](https://doc.qt.io/qt-6/qmodelindex.html)  & index ) const[https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n124](https://code.qt.io/cgit/qt/qtbase.git/tree/src/gui/itemmodels/qfilesystemmodel.h?h=6.12#n124)[https://doc.qt.io/qt-6/qfilesystemmodel.html#type](https://doc.qt.io/qt-6/qfilesystemmodel.html#type)

Returns the type of file index  such as "Directory" or "JPEG file".

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
