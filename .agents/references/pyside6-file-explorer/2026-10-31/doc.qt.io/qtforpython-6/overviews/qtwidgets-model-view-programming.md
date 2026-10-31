<!--
source: https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html
retrieved: 2026-10-31T21:18:43.609105+00:00
final_url: https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html
content_type: text/html
-->

# Model/View Programming - Qt for Python

[Skip to content](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#furo-main-content)

[Qt for Python](https://doc.qt.io/qtforpython-6/index.html)

[Back to top](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html)

Warning

This section contains snippets that were automatically translated from C++ to Python and may contain errors.

# Model/View Programming[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)

A guide to Qt’s extensible model/view architecture.

> 

## Introduction to Model/View Programming[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#introduction-to-model-view-programming)

Qt contains a set of item view classes that use a model/view architecture to manage the relationship between data and the way it is presented to the user. The separation of functionality introduced by this architecture gives developers greater flexibility to customize the presentation of items, and provides a standard model interface to allow a wide range of data sources to be used with existing item views. In this document, we give a brief introduction to the model/view paradigm, outline the concepts involved, and describe the architecture of the item view system. Each of the components in the architecture is explained, and examples are given that show how to use the classes provided.

> 

### The model/view architecture[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#the-model-view-architecture)

Model-View-Controller (MVC) is a design pattern originating from Smalltalk that is often used when building user interfaces. In [Design Patterns](https://www.pearson.com/us/higher-education/program/Gamma-Design-Patterns-Elements-of-Reusable-Object-Oriented-Software/PGM14333.html)  , Gamma et al. write:

MVC consists of three kinds of objects. The Model is the application object, the View is its screen presentation, and the Controller defines the way the user interface reacts to user input. Before MVC, user interface designs tended to lump these objects together. MVC decouples them to increase flexibility and reuse.

If the view and the controller objects are combined, the result is the model/view architecture. This still separates the way that data is stored from the way that it is presented to the user, but provides a simpler framework based on the same principles. This separation makes it possible to display the same data in several different views, and to implement new types of views, without changing the underlying data structures. To allow flexible handling of user input, we introduce the concept of the delegate . The advantage of having a delegate in this framework is that it allows the way items of data are rendered and edited to be customized.

> 

The model/view architecture

The model communicates with a source of data, providing an interface  for the other components in the architecture. The nature of the communication depends on the type of data source, and the way the model is implemented.

The view obtains model indexes  from the model; these are references to items of data. By supplying model indexes to the model, the view can retrieve items of data from the data source.

In standard views, a delegate  renders the items of data. When an item is edited, the delegate communicates with the model directly using model indexes.

Generally, the model/view classes can be separated into the three groups described above: models, views, and delegates. Each of these components is defined by abstract  classes that provide common interfaces and, in some cases, default implementations of features. Abstract classes are meant to be subclassed in order to provide the full set of functionality expected by other components; this also allows specialized components to be written.

Models, views, and delegates communicate with each other using signals and slots :

> 

- 

Signals from the model inform the view about changes to the data held by the data source.

- 

Signals from the view provide information about the user’s interaction with the items being displayed.

- 

Signals from the delegate are used during editing to tell the model and view about the state of the editor.

#### Models[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#models)

All item models are based on the QAbstractItemModel class. This class defines an interface that is used by views and delegates to access data. The data itself does not have to be stored in the model; it can be held in a data structure or repository provided by a separate class, a file, a database, or some other application component.

The basic concepts surrounding models are presented in the section on [Model Classes](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  .

QAbstractItemModel provides an interface to data that is flexible enough to handle views that represent data in the form of tables, lists, and trees. However, when implementing new models for list and table-like data structures, the QAbstractListModel and QAbstractTableModel classes are better starting points because they provide appropriate default implementations of common functions. Each of these classes can be subclassed to provide models that support specialized kinds of lists and tables.

The process of subclassing models is discussed in the section on [Creating New Models](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  .

Qt provides some ready-made models that can be used to handle items of data:

> 

- 

QRangeModel adapts an existing C++ container or any iterable C++ range, to the model/view framework without subclassing.

- 

QStringListModel is used to store a simple list of QString items.

- 

QStandardItemModel manages more complex tree structures of items, each of which can contain arbitrary data.

- 

QFileSystemModel provides information about files and directories in the local filing system.

- 

QSqlQueryModel, QSqlTableModel, and QSqlRelationalTableModel are used to access databases using model/view conventions.

If these standard models do not meet your requirements, you can subclass QAbstractItemModel, QAbstractListModel, or QAbstractTableModel to create your own custom models. Alternatively, if your data already lives in a C++ container or range, QRangeModel can often adapt it without subclassing.

> 

#### Views[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#views)

Complete implementations are provided for different kinds of views: ``[QListView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListView.html#PySide6.QtWidgets.QListView)  displays a list of items, ``[QTableView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableView.html#PySide6.QtWidgets.QTableView)  displays data from a model in a table, and ``[QTreeView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeView.html#PySide6.QtWidgets.QTreeView)  shows model items of data in a hierarchical list. Each of these classes is based on the ``[QAbstractItemView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView)  abstract base class. Although these classes are ready-to-use implementations, they can also be subclassed to provide customized views.

The available views are examined in the section on [View Classes](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  .

> 

#### Delegates[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#delegates)

``[QAbstractItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate)  is the abstract base class for delegates in the model/view framework. The default delegate implementation is provided by ``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)  , and this is used as the default delegate by Qt’s standard views. However, ``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)  and ``[QItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QItemDelegate.html#PySide6.QtWidgets.QItemDelegate)  are independent alternatives to painting and providing editors for items in views. The difference between them is that ``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)  uses the current style to paint its items. We therefore recommend using ``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)  as the base class when implementing custom delegates or when working with Qt style sheets.

Delegates are described in the section on [Delegate Classes](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  .

> 

#### Sorting[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#sorting)

There are two ways of approaching sorting in the model/view architecture; which approach to choose depends on your underlying model.

If your model is sortable, i.e, if it reimplements the QAbstractItemModel::sort() function, both ``[QTableView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableView.html#PySide6.QtWidgets.QTableView)  and ``[QTreeView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeView.html#PySide6.QtWidgets.QTreeView)  provide an API that allows you to sort your model data programmatically. In addition, you can enable interactive sorting (i.e. allowing the users to sort the data by clicking the view’s headers), by connecting the ``[sortIndicatorChanged()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QHeaderView.html#PySide6.QtWidgets.QHeaderView.sortIndicatorChanged)  signal to the ``[sortByColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableView.html#PySide6.QtWidgets.QTableView.sortByColumn)  slot or the ``[sortByColumn()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeView.html#PySide6.QtWidgets.QTreeView.sortByColumn)  slot, respectively.

The alternative approach, if your model does not have the required interface or if you want to use a list view to present your data, is to use a proxy model to transform the structure of your model before presenting the data in the view. This is covered in detail in the section on [Proxy Models](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  .

> 

#### Convenience classes[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#convenience-classes)

A number of convenience  classes are derived from the standard view classes for the benefit of applications that rely on Qt’s item-based item view and table classes. They are not intended to be subclassed.

Examples of such classes include ``[QListWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListWidget.html#PySide6.QtWidgets.QListWidget)  , ``[QTreeWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeWidget.html#PySide6.QtWidgets.QTreeWidget)  , and ``[QTableWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableWidget.html#PySide6.QtWidgets.QTableWidget)  .

These classes are less flexible than the view classes, and cannot be used with arbitrary models. We recommend that you use a model/view approach to handling data in item views unless you strongly need an item-based set of classes.

If you wish to take advantage of the features provided by the model/view approach while still using an item-based interface, consider using view classes, such as ``[QListView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListView.html#PySide6.QtWidgets.QListView)  , ``[QTableView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableView.html#PySide6.QtWidgets.QTableView)  , and ``[QTreeView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeView.html#PySide6.QtWidgets.QTreeView)  with QStandardItemModel.

> 

## Using Models and Views[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#using-models-and-views)

The following sections explain how to use the model/view pattern in Qt. Each section includes an example and is followed by a section showing how to create new components.

> 

### Two models included in Qt[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#two-models-included-in-qt)

Two of the standard models provided by Qt are QStandardItemModel and QFileSystemModel. QStandardItemModel is a multi-purpose model that can be used to represent various different data structures needed by list, table, and tree views. This model also holds the items of data. QFileSystemModel is a model that maintains information about the contents of a directory. As a result, it does not hold any items of data itself, but simply represents files and directories on the local filing system.

QFileSystemModel provides a ready-to-use model to experiment with, and can be easily configured to use existing data. Using this model, we can show how to set up a model for use with ready-made views, and explore how to manipulate data using model indexes.

> 

### Using views with an existing model[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#using-views-with-an-existing-model)

The ``[QListView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListView.html#PySide6.QtWidgets.QListView)  and ``[QTreeView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeView.html#PySide6.QtWidgets.QTreeView)  classes are the most suitable views to use with QFileSystemModel. The example presented below displays the contents of a directory in a tree view next to the same information in a list view. The views share the user’s selection so that the selected items are highlighted in both views.

> 

We set up a QFileSystemModel so that it is ready for use, and create some views to display the contents of a directory. This shows the simplest way to use a model. The construction and use of the model is performed from within a single `main()` function:

> 

```
if __name__ == "__main__":

    app = QApplication([])
    splitter = QSplitter()
    //! [2] //! [3]
    model = QFileSystemModel()
    model.setRootPath(QDir.currentPath())
```

The model is set up to use data from a certain file system. The call to setRootPath() tells the model which drive on the file system to expose to the views.

We create two views so that we can examine the items held in the model in two different ways:

> 

```
tree = QTreeView(splitter)
//! [3] //! [6]
tree.setModel(model)
//! [4] //! [6] //! [7]
tree.setRootIndex(model.index(QDir.currentPath()))
//! [7]
list = QListView(splitter)
list.setModel(model)
list.setRootIndex(model.index(QDir.currentPath()))
```

The views are constructed in the same way as other widgets. Setting up a view to display the items in the model is simply a matter of calling its ``[setModel()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setModel)  function with the directory model as the argument. We filter the data supplied by the model by calling the ``[setRootIndex()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setRootIndex)  function on each view, passing a suitable model index  from the file system model for the current directory.

The `index()` function used in this case is unique to QFileSystemModel; we supply it with a directory and it returns a model index. Model indexes are discussed in [Model Classes](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  .

The rest of the function just displays the views within a splitter widget, and runs the application’s event loop:

> 

```
    splitter.setWindowTitle("Two views onto the same file system model")
    splitter.show()
    sys.exit(app.exec())

//! [1]
//! [2]
    model = QFileSystemModel()
    model.setRootPath(QDir.currentPath())
//! [2]
//! [3]
    model = QFileSystemModel()
    model.setRootPath(QDir.currentPath())
    //! [0] //! [2] //! [4] //! [5]
    tree = QTreeView(splitter)
//! [3]
//! [4]
    tree = QTreeView(splitter)
    //! [3] //! [6]
    tree.setModel(model)
//! [4]
//! [5]
    tree = QTreeView(splitter)
    //! [3] //! [6]
    tree.setModel(model)
    //! [4] //! [6] //! [7]
    tree.setRootIndex(model.index(QDir.currentPath()))
    //! [7]
    list = QListView(splitter)
    list.setModel(model)
    list.setRootIndex(model.index(QDir.currentPath()))
//! [5]
//! [6]
    tree.setModel(model)
//! [6]
//! [7]
    tree.setRootIndex(model.index(QDir.currentPath()))
//! [7]
```

In the above example, we neglected to mention how to handle selections of items. This subject is covered in more detail in the section about [Handling Selections in Item Views](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  .

> 

## Model Classes[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-classes)

Before examining how selections are handled, you may find it useful to examine the concepts used in the model/view framework.

> 

### Basic concepts[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#basic-concepts)

In the model/view architecture, the model provides a standard interface that views and delegates use to access data. In Qt, the standard interface is defined by the QAbstractItemModel class. No matter how the items of data are stored in any underlying data structure, all subclasses of QAbstractItemModel represent the data as a hierarchical structure containing tables of items. Views use this convention  to access items of data in the model, but they are not restricted in the way that they present this information to the user.

> 

Models also notify any attached views about changes to data through the signals and slots mechanism.

This section describes some basic concepts that are central to the way items of data are accessed by other components via a model class. More advanced concepts are discussed in later sections.

> 

#### Model indexes[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-indexes)

To ensure that the representation of the data is kept separate from the way it is accessed, the concept of a model index  is introduced. Each piece of information that can be obtained via a model is represented by a model index. Views and delegates use these indexes to request items of data to display.

As a result, only the model needs to know how to obtain data, and the type of data managed by the model can be defined fairly generally. Model indexes contain a pointer to the model that created them, and this prevents confusion when working with more than one model.

> 

```
model = index.model()
```

Model indexes provide temporary  references to pieces of information, and can be used to retrieve or modify data via the model. Since models may reorganize their internal structures from time to time, model indexes may become invalid, and should not be stored . If a long-term reference to a piece of information is required, a persistent model index  must be created. This provides a reference to the information that the model keeps up-to-date. Temporary model indexes are provided by the QModelIndex class, and persistent model indexes are provided by the QPersistentModelIndex class.

To obtain a model index that corresponds to an item of data, three properties must be specified to the model: a row number, a column number, and the model index of a parent item. The following sections describe and explain these properties in detail.

> 

#### Rows and columns[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#rows-and-columns)

In its most basic form, a model can be accessed as a simple table in which items are located by their row and column numbers. This does not mean that the underlying pieces of data are stored in an array structure ; the use of row and column numbers is only a convention to allow components to communicate with each other. We can retrieve information about any given item by specifying its row and column numbers to the model, and we receive an index that represents the item:

> 

```
index = model.index(row, column /*...*/)
```

Models that provide interfaces to simple, single level data structures like lists and tables do not need any other information to be provided but, as the above code indicates, we need to supply more information when obtaining a model index.

> 

Rows and columns

The diagram shows a representation of a basic table model in which each item is located by a pair of row and column numbers. We obtain a model index that refers to an item of data by passing the relevant row and column numbers to the model.

> 

```
indexA = model.index(0, 0, QModelIndex())
indexB = model.index(1, 1, QModelIndex())
indexC = model.index(2, 1, QModelIndex())
```

Top level items in a model are always referenced by specifying `QModelIndex()` as their parent item. This is discussed in the next section.

#### Parents of items[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#parents-of-items)

The table-like interface to item data provided by models is ideal when using data in a table or list view; the row and column number system maps exactly to the way the views display items. However, structures such as tree views require the model to expose a more flexible interface to the items within. As a result, each item can also be the parent of another table of items, in much the same way that a top-level item in a tree view can contain another list of items.

When requesting an index for a model item, we must provide some information about the item’s parent. Outside the model, the only way to refer to an item is through a model index, so a parent model index must also be given:

> 

```
index = model.index(row, column, parent)
```

Parents, rows, and columns

The diagram shows a representation of a tree model in which each item is referred to by a parent, a row number, and a column number.

Items “A” and “C” are represented as top-level siblings in the model:

> 

```
indexA = model.index(0, 0, QModelIndex())
indexC = model.index(2, 1, QModelIndex())
```

Item “A” has a number of children. A model index for item “B” is obtained with the following code:

> 

```
indexB = model.index(1, 0, indexA)
```

#### Item roles[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#item-roles)

Items in a model can perform various roles  for other components, allowing different kinds of data to be supplied for different situations. For example, Qt::DisplayRole is used to access a string that can be displayed as text in a view. Typically, items contain data for a number of different roles, and the standard roles are defined by Qt::ItemDataRole.

We can ask the model for the item’s data by passing it the model index corresponding to the item, and by specifying a role to obtain the type of data we want:

> 

```
value = model.data(index, role)
```

Item roles

The role indicates to the model which type of data is being referred to. Views can display the roles in different ways, so it is important to supply appropriate information for each role.

The [Creating New Models](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  section covers some specific uses of roles in more detail.

Most common uses for item data are covered by the standard roles defined in Qt::ItemDataRole. By supplying appropriate item data for each role, models can provide hints to views and delegates about how items should be presented to the user. Different kinds of views have the freedom to interpret or ignore this information as required. It is also possible to define additional roles for application-specific purposes.

> 

#### Summary[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#summary)

> 

- 

Model indexes give views and delegates information about the location of items provided by models in a way that is independent of any underlying data structures.

- 

Items are referred to by their row and column numbers, and by the model index of their parent items.

- 

Model indexes are constructed by models at the request of other components, such as views and delegates.

- 

If a valid model index is specified for the parent item when an index is requested using index(), the index returned refers to an item beneath that parent item in the model. The index obtained refers to a child of that item.

- 

If an invalid model index is specified for the parent item when an index is requested using index(), the index returned refers to a top-level item in the model.

- 

The role distinguishes between the different kinds of data associated with an item.

### Using model indexes[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#using-model-indexes)

To demonstrate how data can be retrieved from a model, using model indexes, we set up a QFileSystemModel without a view and display the names of files and directories in a widget. Although this does not show a normal way of using a model, it demonstrates the conventions used by models when dealing with model indexes.

QFileSystemModel loading is asynchronous to minimize system resource use. We have to take that into account when dealing with this model.

We construct a file system model in the following way:

> 

```
    model = QFileSystemModel()
    model.setRootPath(QDir.currentPath())

    def on_directory_loaded(directory):
        parent_index = model.index(directory)
        num_rows = model.rowCount(parent_index)
#! [1]
        for row in range(num_rows):
            index = model.index(row, 0, parent_index)
#! [1]
#! [2]
            text = model.data(index, Qt.DisplayRole)
#! [2]
            label = QLabel(text, window)
            layout.addWidget(label)

    model.directoryLoaded.connect(on_directory_loaded)
```

In this case, we start by setting up a default QFileSystemModel. We connect its signal `directoryLoaded(QString)` to a lambda, in which we will obtain a parent index for the directory using a specific implementation of index() provided by that model.

In the lambda, we determine the number of rows in the model using the rowCount() function.

For simplicity, we are only interested in the items in the first column of the model. We examine each row in turn, obtaining a model index for the first item in each row, and read the data stored for that item in the model.

> 

```
for row in range(num_rows):
    index = model.index(row, 0, parent_index)
```

To obtain a model index, we specify the row number, column number (zero for the first column), and the appropriate model index for the parent of all the items that we want. The text stored in each item is retrieved using the model’s data() function. We specify the model index and the DisplayRole to obtain data for the item in the form of a string.

> 

```
text = model.data(index, Qt.DisplayRole)
```

Finally, we set the root path of the QFileSystemModel so it starts loading data and triggers the lambda.

The above example demonstrates the basic principles used to retrieve data from a model:

> 

- 

The dimensions of a model can be found using rowCount() and columnCount(). These functions generally require a parent model index to be specified.

- 

Model indexes are used to access items in the model. The row, column, and parent model index are needed to specify the item.

- 

To access top-level items in a model, specify a null model index as the parent index with `QModelIndex()`.

- 

Items contain data for different roles. To obtain the data for a particular role, both the model index and the role must be supplied to the model.

### Further reading[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#further-reading)

New models can be created by implementing the standard interface provided by QAbstractItemModel. In the [Creating New Models](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  section, we demonstrate this by creating a convenient ready-to-use model for holding lists of strings.

> 

## View Classes[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#view-classes)

> 

### Concepts[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#concepts)

In the model/view architecture, the view obtains items of data from the model and presents them to the user. The way that the data is presented need not resemble the representation of the data provided by the model, and may be completely different  from the underlying data structure used to store items of data.

The separation of content and presentation is achieved by the use of a standard model interface provided by QAbstractItemModel, a standard view interface provided by ``[QAbstractItemView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView)  , and the use of model indexes that represent items of data in a general way. Views typically manage the overall layout of the data obtained from models. They may render individual items of data themselves, or use [delegates](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  to handle both rendering and editing features.

As well as presenting data, views handle navigation between items, and some aspects of item selection. The views also implement basic user interface features, such as context menus and drag and drop. A view can provide default editing facilities for items, or it may work with a [delegate](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  to provide a custom editor.

A view can be constructed without a model, but a model must be provided before it can display useful information. Views keep track of the items that the user has selected through the use of [selections](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  which can be maintained separately for each view, or shared between multiple views.

Some views, such as ``[QTableView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableView.html#PySide6.QtWidgets.QTableView)  and ``[QTreeView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeView.html#PySide6.QtWidgets.QTreeView)  , display headers as well as items. These are also implemented by a view class, ``[QHeaderView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QHeaderView.html#PySide6.QtWidgets.QHeaderView)  . Headers usually access the same model as the view that contains them. They retrieve data from the model using the QAbstractItemModel::headerData() function, and usually display header information in the form of a label. New headers can be subclassed from the ``[QHeaderView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QHeaderView.html#PySide6.QtWidgets.QHeaderView)  class to provide more specialized labels for views.

> 

### Using an existing view[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#using-an-existing-view)

Qt provides three ready-to-use view classes that present data from models in ways that are familiar to most users. ``[QListView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListView.html#PySide6.QtWidgets.QListView)  can display items from a model as a simple list, or in the form of a classic icon view. ``[QTreeView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeView.html#PySide6.QtWidgets.QTreeView)  displays items from a model as a hierarchy of lists, allowing deeply nested structures to be represented in a compact way. ``[QTableView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableView.html#PySide6.QtWidgets.QTableView)  presents items from a model in the form of a table, much like the layout of a spreadsheet application.

> 

The default behavior of the standard views shown above should be sufficient for most applications. They provide basic editing facilities, and can be customized to suit the needs of more specialized user interfaces.

> 

#### Using a model[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#using-a-model)

We take the string list model that [we created as an example model](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  , set it up with some data, and construct a view to display the contents of the model. This can all be performed within a single function:

> 

```
if __name__ == '__main__':
    app = QApplication(sys.argv)

#! [main1]
    numbers = ["One", "Two", "Three", "Four", "Five"]
    model = StringListModel(numbers)
```

Note that the `StringListModel` is declared as a QAbstractItemModel. This allows us to use the abstract interface to the model, and ensures that the code still works, even if we replace the string list model with a different model.

The list view provided by ``[QListView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListView.html#PySide6.QtWidgets.QListView)  is sufficient for presenting the items in the string list model. We construct the view, and set up the model using the following lines of code:

> 

```
view = QListView()
view.setModel(model)
```

The view is shown in the normal way:

> 

```
view.show()
sys.exit(app.exec())
```

The view renders the contents of a model, accessing data via the model’s interface. When the user tries to edit an item, the view uses a default delegate to provide an editor widget.

> 

The above image shows how a ``[QListView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListView.html#PySide6.QtWidgets.QListView)  represents the data in the string list model. Since the model is editable, the view automatically allows each item in the list to be edited using the default delegate.

> 

#### Using multiple views of a model[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#using-multiple-views-of-a-model)

Providing multiple views onto the same model is simply a matter of setting the same model for each view. In the following code we create two table views, each using the same simple table model which we have created for this example:

> 

```
firstTableView = QTableView()
secondTableView = QTableView()

firstTableView.setModel(model)
secondTableView.setModel(model)
```

The use of signals and slots in the model/view architecture means that changes to the model can be propagated to all the attached views, ensuring that we can always access the same data regardless of the view being used.

> 

The above image shows two different views onto the same model, each containing a number of selected items. Although the data from the model is shown consistently across view, each view maintains its own internal selection model. This can be useful in certain situations but, for many applications, a shared selection model is desirable.

> 

### Handling selections of items[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#handling-selections-of-items)

The mechanism for handling selections of items within views is provided by the QItemSelectionModel class. All of the standard views construct their own selection models by default, and interact with them in the normal way. The selection model being used by a view can be obtained through the ``[selectionModel()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionModel)  function, and a replacement selection model can be specified with ``[setSelectionModel()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelectionModel)  . The ability to control the selection model used by a view is useful when we want to provide multiple consistent views onto the same model data.

Generally, unless you are subclassing a model or view, you don’t need to manipulate the contents of selections directly. However, the interface to the selection model can be accessed, if required, and this is explored in [Handling Selections in Item Views](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  .

> 

#### Sharing selections among views[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#sharing-selections-among-views)

Although it is convenient that the view classes provide their own selection models by default, when we use more than one view onto the same model it is often desirable that both the model’s data and the user’s selection are shown consistently in all views. Since the view classes allow their internal selection models to be replaced, we can achieve a unified selection between views with the following line:

> 

```
secondTableView.setSelectionModel(firstTableView.selectionModel())
```

The second view is given the selection model for the first view. Both views now operate on the same selection model, keeping both the data and the selected items synchronized.

> 

In the example shown above, two views of the same type were used to display the same model’s data. However, if two different types of view were used, the selected items may be represented very differently in each view; for example, a contiguous selection in a table view can be represented as a fragmented set of highlighted items in a tree view.

> 

## Delegate Classes[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#delegate-classes)

> 

### Concepts[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#id2)

Unlike the Model-View-Controller pattern, the model/view design does not include a completely separate component for managing interaction with the user. Generally, the view is responsible for the presentation of model data to the user, and for processing user input. To allow some flexibility in the way this input is obtained, the interaction is performed by delegates. These components provide input capabilities and are also responsible for rendering individual items in some views. The standard interface for controlling delegates is defined in the ``[QAbstractItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate)  class.

Delegates are expected to be able to render their contents themselves by implementing the `paint()` and `sizeHint()` functions. However, simple widget-based delegates can subclass ``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)  instead of ``[QAbstractItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate)  , and take advantage of the default implementations of these functions.

Editors for delegates can be implemented either by using widgets to manage the editing process or by handling events directly. The first approach is covered later in this section.

> 

### Using an existing delegate[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#using-an-existing-delegate)

The standard views provided with Qt use instances of ``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)  to provide editing facilities. This default implementation of the delegate interface renders items in the usual style for each of the standard views: ``[QListView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListView.html#PySide6.QtWidgets.QListView)  , ``[QTableView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableView.html#PySide6.QtWidgets.QTableView)  , and ``[QTreeView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeView.html#PySide6.QtWidgets.QTreeView)  .

All the standard roles are handled by the default delegate used by the standard views. The way these are interpreted is described in the ``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)  documentation.

The delegate used by a view is returned by the ``[itemDelegate()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.itemDelegate)  function. The ``[setItemDelegate()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setItemDelegate)  function allows you to install a custom delegate for a standard view, and it is necessary to use this function when setting the delegate for a custom view.

> 

### A simple delegate[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#a-simple-delegate)

The delegate implemented here uses a ``[QSpinBox](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QSpinBox.html#PySide6.QtWidgets.QSpinBox)  to provide editing facilities, and is mainly intended for use with models that display integers. Although we set up a custom integer-based table model for this purpose, we could easily have used QStandardItemModel instead, since the custom delegate controls data entry. We construct a table view to display the contents of the model, and this will use the custom delegate for editing.

> 

We subclass the delegate from ``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)  because we do not want to write custom display functions. However, we must still provide functions to manage the editor widget:

> 

```
class SpinBoxDelegate(QStyledItemDelegate):

    Q_OBJECT
# public
    SpinBoxDelegate(QObject parent = None)
    QWidget createEditor(QWidget parent, QStyleOptionViewItem option,
                          QModelIndex index) override
    def setEditorData(editor, index):
    def setModelData(editor, model,):
                      QModelIndex index) override
    def updateEditorGeometry(editor, option,):
                              QModelIndex index) override

def __init__(self, parent):
    super().__init__(parent)
```

Note that no editor widgets are set up when the delegate is constructed. We only construct an editor widget when it is needed.

> 

#### Providing an editor[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#providing-an-editor)

In this example, when the table view needs to provide an editor, it asks the delegate to provide an editor widget that is appropriate for the item being modified. The ``[createEditor()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate.createEditor)  function is supplied with everything that the delegate needs to be able to set up a suitable widget:

> 

```
QWidget SpinBoxDelegate.createEditor(QWidget parent,
                                       QStyleOptionViewItem /* option */,
                                       QModelIndex /* index */)

    editor = QSpinBox(parent)
    editor.setFrame(False)
    editor.setMinimum(0)
    editor.setMaximum(100)
    return editor
```

Note that we do not need to keep a pointer to the editor widget because the view takes responsibility for destroying it when it is no longer needed.

We install the delegate’s default event filter on the editor to ensure that it provides the standard editing shortcuts that users expect. Additional shortcuts can be added to the editor to allow more sophisticated behavior; these are discussed in the section on [Editing Hints](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  .

The view ensures that the editor’s data and geometry are set correctly by calling functions that we define later for these purposes. We can create different editors depending on the model index supplied by the view. For example, if we have a column of integers and a column of strings we could return either a `QSpinBox` or a `QLineEdit`, depending on which column is being edited.

The delegate must provide a function to copy model data into the editor. In this example, we read the data stored in the display role, and set the value in the spin box accordingly.

> 

```
def setEditorData(self, editor,):
                                    QModelIndex index)

    value = index.data(Qt.ItemDataRole.EditRole).toInt()
    spinBox = QSpinBox(editor)
    spinBox.setValue(value)
```

In this example, we know that the editor widget is a spin box, but we could have provided different editors for different types of data in the model, in which case we would need to cast the widget to the appropriate type before accessing its member functions.

> 

#### Submitting data to the model[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#submitting-data-to-the-model)

When the user has finished editing the value in the spin box, the view asks the delegate to store the edited value in the model by calling the ``[setModelData()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate.setModelData)  function.

> 

```
def setModelData(self, editor, model,):
                                   QModelIndex index)

    spinBox = QSpinBox(editor)
    spinBox.interpretText()
    value = spinBox.value()
    model.setData(index, value, Qt.ItemDataRole.EditRole)
```

Since the view manages the editor widgets for the delegate, we only need to update the model with the contents of the editor supplied. In this case, we ensure that the spin box is up-to-date, and update the model with the value it contains using the index specified.

The standard ``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)  class informs the view when it has finished editing by emitting the ``[closeEditor()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate.closeEditor)  signal. The view ensures that the editor widget is closed and destroyed. In this example, we only provide simple editing facilities, so we never need to emit this signal.

All the operations on data are performed through the interface provided by QAbstractItemModel. This makes the delegate mostly independent from the type of data it manipulates, but some assumptions must be made in order to use certain types of editor widgets. In this example, we have assumed that the model always contains integer values, but we can still use this delegate with different kinds of models because QVariant provides sensible default values for unexpected data.

> 

#### Updating the editor’s geometry[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#updating-the-editor-s-geometry)

It is the responsibility of the delegate to manage the editor’s geometry. The geometry must be set when the editor is created, and when the item’s size or position in the view is changed. Fortunately, the view provides all the necessary geometry information inside a ``[view option](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyleOptionViewItem.html#PySide6.QtWidgets.QStyleOptionViewItem)  object.

> 

```
def updateEditorGeometry(self, editor,):
                                           QStyleOptionViewItem option,
                                           QModelIndex /* index */)

    editor.setGeometry(option.rect)
```

In this case, we just use the geometry information provided by the view option in the item rectangle. A delegate that renders items with several elements would not use the item rectangle directly. It would position the editor in relation to the other elements in the item.

> 

#### Editing hints[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#editing-hints)

After editing, delegates should provide hints to the other components about the result of the editing process, and provide hints that will assist any subsequent editing operations. This is achieved by emitting the ``[closeEditor()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate.closeEditor)  signal with a suitable hint. This is taken care of by the default ``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)  event filter which we installed on the spin box when it was constructed.

The behavior of the spin box could be adjusted to make it more user friendly. In the default event filter supplied by ``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)  , if the user hits Return to confirm their choice in the spin box, the delegate commits the value to the model and closes the spin box. We can change this behavior by installing our own event filter on the spin box, and provide editing hints that suit our needs; for example, we might emit ``[closeEditor()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate.closeEditor)  with the `EditNextItem` hint to automatically start editing the next item in the view.

Another approach that does not require the use of an event filter is to provide our own editor widget, perhaps subclassing ``[QSpinBox](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QSpinBox.html#PySide6.QtWidgets.QSpinBox)  for convenience. This alternative approach would give us more control over how the editor widget behaves at the cost of writing additional code. It is usually easier to install an event filter in the delegate if you need to customize the behavior of a standard Qt editor widget.

Delegates do not have to emit these hints, but those that do not will be less integrated into applications, and will be less usable than those that emit hints to support common editing actions.

> 

## Handling Selections in Item Views[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#handling-selections-in-item-views)

> 

### Concepts[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#id5)

The selection model used in the item view classes provides a general description of selections based on the facilities of the model/view architecture. Although the standard classes for manipulating selections are sufficient for the item views provided, the selection model allows you to create specialized selection models to suit the requirements for your own item models and views.

Information about the items selected in a view is stored in an instance of the QItemSelectionModel class. This maintains model indexes for items in a single model, and is independent of any views. Since there can be many views onto a model, it is possible to share selections between views, allowing applications to show multiple views in a consistent way.

Selections are made up of selection ranges . These efficiently maintain information about large selections of items by recording only the starting and ending model indexes for each range of selected items. Non-contiguous selections of items are constructed by using more than one selection range to describe the selection.

Selections are applied to a collection of model indexes held by a selection model. The most recent selection of items applied is known as the current selection . The effects of this selection can be modified even after its application through the use of certain types of selection commands. These are discussed later in this section.

> 

#### Current item and selected items[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#current-item-and-selected-items)

In a view, there is always a current item and a selected item - two independent states. An item can be the current item and selected at the same time. The view is responsible for ensuring that there is always a current item as keyboard navigation, for example, requires a current item.

The table below highlights the differences between current item and selected items.

> 

Current Item

Selected Items

There can only be one current item.

There can be multiple selected items.

The current item will be changed with key navigation or mouse button clicks.

The selected state of items is set or unset, depending on several pre-defined modes - e.g., single selection, multiple selection, etc. - when the user interacts with the items.

The current item will be edited if the edit key, F2, is pressed or the item is double-clicked (provided that editing is enabled).

The current item can be used together with an anchor to specify a range that should be selected or deselected (or a combination of the two).

The current item is indicated by the focus rectangle.

The selected items are indicated with the selection rectangle.

When manipulating selections, it is often helpful to think of QItemSelectionModel as a record of the selection state of all the items in an item model. Once a selection model is set up, collections of items can be selected, deselected, or their selection states can be toggled without the need to know which items are already selected. The indexes of all selected items can be retrieved at any time, and other components can be informed of changes to the selection model via the signals and slots mechanism.

> 

### Using a selection model[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#using-a-selection-model)

The standard view classes provide default selection models that can be used in most applications. A selection model belonging to one view can be obtained using the view’s ``[selectionModel()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.selectionModel)  function, and shared between many views with ``[setSelectionModel()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView.setSelectionModel)  , so the construction of new selection models is generally not required.

A selection is created by specifying a model, and a pair of model indexes to a QItemSelection. This uses the indexes to refer to items in the given model, and interprets them as the top-left and bottom-right items in a block of selected items. To apply the selection to items in a model requires the selection to be submitted to a selection model; this can be achieved in a number of ways, each having a different effect on the selections already present in the selection model.

> 

#### Selecting items[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#selecting-items)

To demonstrate some of the principal features of selections, we construct an instance of a custom table model with 32 items in total, and open a table view onto its data:

> 

```
model = TableModel(8, 4, app)
table = QTableView(0)
table.setModel(model)
selectionModel = table.selectionModel()
```

The table view’s default selection model is retrieved for later use. We do not modify any items in the model, but instead select a few items that the view will display at the top-left of the table. To do this, we need to retrieve the model indexes corresponding to the top-left and bottom-right items in the region to be selected:

> 

```
topLeft = QModelIndex()
bottomRight = QModelIndex()
topLeft = model.index(0, 0, QModelIndex())
bottomRight = model.index(5, 2, QModelIndex())
```

To select these items in the model, and see the corresponding change in the table view, we need to construct a selection object then apply it to the selection model:

> 

```
selection = QItemSelection(topLeft, bottomRight)
selectionModel.select(selection, QItemSelectionModel.Select)
```

The selection is applied to the selection model using a command defined by a combination of selection flags. In this case, the flags used cause the items recorded in the selection object to be included in the selection model, regardless of their previous state. The resulting selection is shown by the view.

> 

The selection of items can be modified using various operations that are defined by the selection flags. The selection that results from these operations may have a complex structure, but it is represented efficiently by the selection model. The use of different selection flags to manipulate the selected items is described when we examine how to update a selection.

> 

#### Reading the selection state[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#reading-the-selection-state)

The model indexes stored in the selection model can be read using the selectedIndexes() function. This returns an unsorted list of model indexes that we can iterate over as long as we know which model they are for:

> 

```
indexes = selectionModel.selectedIndexes()
for index in indexes:
    text = QString("(%1,%2)").arg(index.row()).arg(index.column())
    model.setData(index, text)
```

The above code uses a range-based for-loop to iterate over, and modify, the items corresponding to the indexes returned by the selection model.

The selection model emits signals to indicate changes in the selection. These notify other components about changes to both the selection as a whole and the currently focused item in the item model. We can connect the selectionChanged() signal to a slot, and examine the items in the model that are selected or deselected when the selection changes. The slot is called with two QItemSelection objects: one contains a list of indexes that correspond to newly selected items; the other contains indexes that correspond to newly deselected items.

In the following code, we provide a slot that receives the selectionChanged() signal, fills in the selected items with a string, and clears the contents of the deselected items.

> 

```
def updateSelection(self, selected,):
    QItemSelection deselected)

    items = selected.indexes()
    for index in items:
        text = QString("(%1,%2)").arg(index.row()).arg(index.column())
        model.setData(index, text)

items = deselected.indexes()
for index in items:
    model.setData(index, QString())
```

We can keep track of the currently focused item by connecting the currentChanged() signal to a slot that is called with two model indexes. These correspond to the previously focused item, and the currently focused item.

In the following code, we provide a slot that receives the currentChanged() signal, and uses the information provided to update the status bar of a ``[QMainWindow](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMainWindow.html#PySide6.QtWidgets.QMainWindow)  :

> 

```
def changeCurrent(self, current,):
    QModelIndex previous)

    statusBar().showMessage(
        tr("Moved from (%1,%2) to (%3,%4)")
            .arg(previous.row()).arg(previous.column())
            .arg(current.row()).arg(current.column()))
```

Monitoring selections made by the user is straightforward with these signals, but we can also update the selection model directly.

> 

#### Updating a selection[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#updating-a-selection)

Selection commands are provided by a combination of selection flags, defined by QItemSelectionModel::SelectionFlag. Each selection flag tells the selection model how to update its internal record of selected items when either of the select() functions are called. The most commonly used flag is the Select flag which instructs the selection model to record the specified items as being selected. The Toggle flag causes the selection model to invert the state of the specified items, selecting any deselected items given, and deselecting any currently selected items. The Deselect flag deselects all the specified items.

Individual items in the selection model are updated by creating a selection of items, and applying them to the selection model. In the following code, we apply a second selection of items to the table model shown above, using the Toggle command to invert the selection state of the items given.

> 

```
toggleSelection = QItemSelection()
topLeft = model.index(2, 1, QModelIndex())
bottomRight = model.index(7, 3, QModelIndex())
toggleSelection.select(topLeft, bottomRight)
selectionModel.select(toggleSelection, QItemSelectionModel.Toggle)
```

The results of this operation are displayed in the table view, providing a convenient way of visualizing what we have achieved:

> 

By default, the selection commands only operate on the individual items specified by the model indexes. However, the flag used to describe the selection command can be combined with additional flags to change entire rows and columns. For example if you call select() with only one index, but with a command that is a combination of Select and Rows, the entire row containing the item referred to is selected. The following code demonstrates the use of the Rows and Columns flags:

> 

```
columnSelection = QItemSelection()
topLeft = model.index(0, 1, QModelIndex())
bottomRight = model.index(0, 2, QModelIndex())
columnSelection.select(topLeft, bottomRight)
selectionModel.select(columnSelection,
    QItemSelectionModel.Select | QItemSelectionModel.Columns)
rowSelection = QItemSelection()
topLeft = model.index(0, 0, QModelIndex())
bottomRight = model.index(1, 0, QModelIndex())
rowSelection.select(topLeft, bottomRight)
selectionModel.select(rowSelection,
    QItemSelectionModel.Select | QItemSelectionModel.Rows)
```

Although only four indexes are supplied to the selection model, the use of the Columns and Rows selection flags means that two columns and two rows are selected. The following image shows the result of these two selections:

> 

The commands performed on the example model have all involved accumulating a selection of items in the model. It is also possible to clear the selection, or to replace the current selection with a new one.

To replace the current selection with a new selection, combine the other selection flags with the Current flag. A command using this flag instructs the selection model to replace its current collection of model indexes with those specified in a call to select(). To clear all selections before you start adding new ones, combine the other selection flags with the Clear flag. This has the effect of resetting the selection model’s collection of model indexes.

> 

#### Selecting all items in a model[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#selecting-all-items-in-a-model)

To select all items in a model, it is necessary to create a selection for each level of the model that covers all items in that level. We do this by retrieving the indexes corresponding to the top-left and bottom-right items with a given parent index:

> 

```
topLeft = model.index(0, 0, parent)
bottomRight = model.index(model.rowCount(parent)-1,
    model.columnCount(parent)-1, parent)
```

A selection is constructed with these indexes and the model. The corresponding items are then selected in the selection model:

> 

```
selection = QItemSelection(topLeft, bottomRight)
selectionModel.select(selection, QItemSelectionModel.Select)
```

This needs to be performed for all levels in the model. For top-level items, we would define the parent index in the usual way:

> 

```
parent = QModelIndex()
```

For hierarchical models, the hasChildren() function is used to determine whether any given item is the parent of another level of items.

> 

## Creating New Models[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#creating-new-models)

The separation of functionality between the model/view components allows models to be created that can take advantage of existing views. This approach lets us present data from a variety of sources using standard graphical user interface components, such as ``[QListView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListView.html#PySide6.QtWidgets.QListView)  , ``[QTableView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableView.html#PySide6.QtWidgets.QTableView)  , and ``[QTreeView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeView.html#PySide6.QtWidgets.QTreeView)  .

The QAbstractItemModel class provides an interface that is flexible enough to support data sources that arrange information in hierarchical structures, allowing for the possibility that data will be inserted, removed, modified, or sorted in some way. It also provides support for drag and drop operations.

The QAbstractListModel and QAbstractTableModel classes provide support for interfaces to simpler non-hierarchical data structures, and are easier to use as a starting point for simple list and table models.

In this section, we create a simple read-only model to explore the basic principles of the model/view architecture. Later in this section, we adapt this simple model so that items can be modified by the user.

For an example of a more complex model, see the Simple Tree Model  example.

The requirements of QAbstractItemModel subclasses is described in more detail in the [Model Subclassing Reference](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  document.

> 

### Designing a model[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#designing-a-model)

When creating a new model for an existing data structure, it is important to consider which type of model should be used to provide an interface onto the data. If the data is already held in a C++ container or in any type that models an iterable C++ range, QRangeModel may provide a suitable model without any subclassing, provided that the input range and its element type are supported.

If a ready-made model is not applicable and the data structure can be represented as a list or table of items, you can subclass QAbstractListModel or QAbstractTableModel since these classes provide suitable default implementations for many functions.

However, if the underlying data structure can only be represented by a hierarchical tree structure, it is necessary to subclass QAbstractItemModel. This approach is taken in the Simple Tree Model  example.

In this section, we implement a simple model based on a list of strings, so the QAbstractListModel provides an ideal base class on which to build.

Whatever form the underlying data structure takes, it is usually a good idea to supplement the standard QAbstractItemModel API in specialized models with one that allows more natural access to the underlying data structure. This makes it easier to populate the model with data, yet still enables other general model/view components to interact with it using the standard API. The model described below provides a custom constructor for just this purpose.

> 

### A read-only example model[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#a-read-only-example-model)

The model implemented here is a simple, non-hierarchical, read-only data model based on the standard QStringListModel class. It has a QStringList as its internal data source, and implements only what is needed to make a functioning model. To make the implementation easier, we subclass QAbstractListModel because it defines sensible default behavior for list models, and it exposes a simpler interface than the QAbstractItemModel class.

When implementing a model it is important to remember that QAbstractItemModel does not store any data itself, it merely presents an interface that the views use to access the data. For a minimal read-only model it is only necessary to implement a few functions as there are default implementations for most of the interface. The class declaration is as follows:

> 

```
class StringListModel(QAbstractListModel):
    def __init__(self, strings, parent=None):
        ...

    def rowCount(self, parent=QModelIndex()):
        ...

    def data(self, index, role):
        ...

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        ...

    def flags(self, index):
        ...

    def setData(self, index, value, role=Qt.EditRole):
        ...

    def insertRows(self, position, rows, parent):
        ...

    def removeRows(self, position, rows, parent):
        ...
role = Qt.ItemDataRole.DisplayRole) override()

# private
    stringList = QStringList()
```

Apart from the model’s constructor, we only need to implement two functions: rowCount() returns the number of rows in the model and data() returns an item of data corresponding to a specified model index.

Well behaved models also implement headerData() to give tree and table views something to display in their headers.

Note that this is a non-hierarchical model, so we don’t have to worry about the parent-child relationships. If our model was hierarchical, we would also have to implement the index() and parent() functions.

The list of strings is stored internally in the `stringList` private member variable.

> 

#### Dimensions of the model[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#dimensions-of-the-model)

We want the number of rows in the model to be the same as the number of strings in the string list. We implement the rowCount() function with this in mind:

> 

```
class StringListModel(QAbstractListModel):
    def __init__(self, strings, parent=None):
        super().__init__(parent)
        self._strings = strings
```

Since the model is non-hierarchical, we can safely ignore the model index corresponding to the parent item. By default, models derived from QAbstractListModel only contain one column, so we do not need to reimplement the columnCount() function.

> 

#### Model headers and data[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-headers-and-data)

For items in the view, we want to return the strings in the string list. The data() function is responsible for returning the item of data that corresponds to the index argument:

> 

```
def data(self, QModelIndex index, int role):

    if not index.isValid():
        return QVariant()
    if index.row() >= stringList.size():
        return QVariant()
    if role == Qt.ItemDataRole.DisplayRole:
        return stringList.at(index.row())
else:
        return QVariant()
```

We only return a valid QVariant if the model index supplied is valid, the row number is within the range of items in the string list, and the requested role is one that we support.

Some views, such as ``[QTreeView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeView.html#PySide6.QtWidgets.QTreeView)  and ``[QTableView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableView.html#PySide6.QtWidgets.QTableView)  , are able to display headers along with the item data. If our model is displayed in a view with headers, we want the headers to show the row and column numbers. We can provide information about the headers by subclassing the headerData() function:

> 

```
def headerData(self, section, orientation, role=Qt.DisplayRole):
    """Returns the appropriate header string depending on the orientation of
       the header and the section. If anything other than the display role is
       requested, we return an invalid variant."""
    if role != Qt.DisplayRole:
        return None
    if orientation == Qt.Horizontal:
        return f"Column {section}"
    return f"Row {section}"
```

Again, we return a valid QVariant only if the role is one that we support. The orientation of the header is also taken into account when deciding the exact data to return.

Not all views display headers with the item data, and those that do may be configured to hide them. Nonetheless, it is recommended that you implement the headerData() function to provide relevant information about the data provided by the model.

An item can have several roles, giving out different data depending on the role specified. The items in our model only have one role, DisplayRole, so we return the data for items irrespective of the role specified. However, we could reuse the data we provide for the DisplayRole in other roles, such as the ToolTipRole that views can use to display information about items in a tooltip.

> 

### An editable model[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#an-editable-model)

The read-only model shows how simple choices could be presented to the user but, for many applications, an editable list model is much more useful. We can modify the read-only model to make the items editable by changing the data() function we implemented for read-only, and by implementing two extra functions: flags() and setData(). The following function declarations are added to the class definition:

> 

```
Qt.ItemFlags flags(QModelIndex index) override
bool setData(QModelIndex index, QVariant value,
role = Qt.ItemDataRole.EditRole) override()
```

#### Making the model editable[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#making-the-model-editable)

A delegate checks whether an item is editable before creating an editor. The model must let the delegate know that its items are editable. We do this by returning the correct flags for each item in the model; in this case, we enable all items and make them both selectable and editable:

> 

```
def flags(self, index):
    """Returns an appropriate value for the item's flags. Valid items are
       enabled, selectable, and editable."""

    if not index.isValid():
        return Qt.ItemIsEnabled
    return super().flags(index) | Qt.ItemIsEditable
```

Note that we do not have to know how the delegate performs the actual editing process. We only have to provide a way for the delegate to set the data in the model. This is achieved through the setData() function:

> 

```
def setData(self, index, value, role=Qt.EditRole):
    """Changes an item in the string list, but only if the following conditions
       are met:

       # The index supplied is valid.
       # The index corresponds to an item to be shown in a view.
       # The role associated with editing text is specified.

       The dataChanged() signal is emitted if the item is changed."""

    if index.isValid() and role == Qt.EditRole:
        self._strings[index.row()] = value
        self.dataChanged.emit(index, index, {role})
        return True
return False
```

In this model, the item in the string list that corresponds to the model index is replaced by the value provided. However, before we can modify the string list, we must make sure that the index is valid, the item is of the correct type, and that the role is supported. By convention, we insist that the role is the EditRole since this is the role used by the standard item delegate. For boolean values, however, you can use Qt::CheckStateRole and set the Qt::ItemIsUserCheckable flag; a checkbox is then used for editing the value. The underlying data in this model is the same for all roles, so this detail just makes it easier to integrate the model with standard components.

When the data has been set, the model must let the views know that some data has changed. This is done by emitting the dataChanged() signal. Since only one item of data has changed, the range of items specified in the signal is limited to just one model index.

Also the data() function needs to be changed to add the Qt::EditRole test:

> 

```
def data(self, index, role):
    """Returns an appropriate value for the requested data.
       If the view requests an invalid index, an invalid variant is returned.
       Any valid index that corresponds to a string in the list causes that
      string to be returned."""
    row = index.row()
    if not index.isValid() or row >= len(self._strings):
        return None
    if role != Qt.DisplayRole and role != Qt.EditRole:
        return None
    return self._strings[row]
```

#### Inserting and removing rows[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#inserting-and-removing-rows)

It is possible to change the number of rows and columns in a model. In the string list model it only makes sense to change the number of rows, so we only reimplement the functions for inserting and removing rows. These are declared in the class definition:

> 

```
bool insertRows(int position, int rows, QModelIndex index = QModelIndex()) override
bool removeRows(int position, int rows, QModelIndex index = QModelIndex()) override
```

Since rows in this model correspond to strings in a list, the `insertRows()` function inserts a number of empty strings into the string list before the specified position. The number of strings inserted is equivalent to the number of rows specified.

The parent index is normally used to determine where in the model the rows should be added. In this case, we only have a single top-level list of strings, so we just insert empty strings into that list.

> 

```
def insertRows(self, position, rows, parent):
    """Inserts a number of rows into the model at the specified position."""
    self.beginInsertRows(QModelIndex(), position, position + rows - 1)
    for row in range(rows):
        self._strings.insert(position, "")
    self.endInsertRows()
    return True
```

The model first calls the beginInsertRows() function to inform other components that the number of rows is about to change. The function specifies the row numbers of the first and last new rows to be inserted, and the model index for their parent item. After changing the string list, it calls endInsertRows() to complete the operation and inform other components that the dimensions of the model have changed, returning true to indicate success.

The function to remove rows from the model is also simple to write. The rows to be removed from the model are specified by the position and the number of rows given. We ignore the parent index to simplify our implementation, and just remove the corresponding items from the string list.

> 

```
def removeRows(self, position, rows, parent):
    """Removes a number of rows from the model at the specified position."""
    self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
    for row in range(rows):
        del self._strings[position]
    self.endRemoveRows()
    return True
```

The beginRemoveRows() function is always called before any underlying data is removed, and specifies the first and last rows to be removed. This allows other components to access the data before it becomes unavailable. After the rows have been removed, the model emits endRemoveRows() to finish the operation and let other components know that the dimensions of the model have changed.

> 

### Next steps[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#next-steps)

We can display the data provided by this model, or any other model, using the ``[QListView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListView.html#PySide6.QtWidgets.QListView)  class to present the model’s items in the form of a vertical list. For the string list model, this view also provides a default editor so that the items can be manipulated. We examine the possibilities made available by the standard view classes in [View Classes](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  .

The [Model Subclassing Reference](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  document discusses the requirements of QAbstractItemModel subclasses in more detail, and provides a guide to the virtual functions that must be implemented to enable various features in different types of models.

> 

## Item View Convenience Classes[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#item-view-convenience-classes)

The item-based widgets have names which reflect their uses: `QListWidget` provides a list of items, `QTreeWidget` displays a multi-level tree structure, and `QTableWidget` provides a table of cell items. Each class inherits the behavior of the `QAbstractItemView` class which implements common behavior for item selection and header management.

> 

### List widgets[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#list-widgets)

Single level lists of items are typically displayed using a `QListWidget` and a number of `QListWidgetItem`s. A list widget is constructed in the same way as any other widget:

> 

```
listWidget = QListWidget(self)
```

List items can be added directly to the list widget when they are constructed:

> 

```
QListWidgetItem(tr("Sycamore"), listWidget)
QListWidgetItem(tr("Chestnut"), listWidget)
QListWidgetItem(tr("Mahogany"), listWidget)
```

They can also be constructed without a parent list widget and added to a list at some later time:

> 

```
newItem = QListWidgetItem()
newItem.setText(itemText)
listWidget.insertItem(row, newItem)
```

Each item in a list can display a text label and an icon. The colors and font used to render the text can be changed to provide a customized appearance for items. Tooltips, status tips, and “What’s This?” help are all easily configured to ensure that the list is properly integrated into the application.

> 

```
newItem.setToolTip(toolTipText)
newItem.setStatusTip(toolTipText)
newItem.setWhatsThis(whatsThisText)
```

By default, items in a list are presented in the order of their creation. Lists of items can be sorted according to the criteria given in Qt::SortOrder to produce a list of items that is sorted in forward or reverse alphabetical order:

> 

```
listWidget.sortItems(Qt.AscendingOrder)
listWidget.sortItems(Qt.DescendingOrder)
```

### Tree widgets[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#tree-widgets)

Trees or hierarchical lists of items are provided by the `QTreeWidget` and `QTreeWidgetItem` classes. Each item in the tree widget can have child items of its own, and can display a number of columns of information. Tree widgets are created just like any other widget:

> 

```
treeWidget = QTreeWidget(self)
```

Before items can be added to the tree widget, the number of columns must be set. For example, we could define two columns, and create a header to provide labels at the top of each column:

> 

```
treeWidget.setColumnCount(2)
headers = QStringList()
headers << tr("Subject") << tr("Default")
treeWidget.setHeaderLabels(headers)
```

The easiest way to set up the labels for each section is to supply a string list. For more sophisticated headers, you can construct a tree item, decorate it as you wish, and use that as the tree widget’s header.

Top-level items in the tree widget are constructed with the tree widget as their parent widget. They can be inserted in an arbitrary order, or you can ensure that they are listed in a particular order by specifying the previous item when constructing each item:

> 

```
cities = QTreeWidgetItem(treeWidget)
cities.setText(0, tr("Cities"))
osloItem = QTreeWidgetItem(cities)
osloItem.setText(0, tr("Oslo"))
osloItem.setText(1, tr("Yes"))

planets = QTreeWidgetItem(treeWidget, cities)
```

Tree widgets deal with top-level items slightly differently to other items from deeper within the tree. Items can be removed from the top level of the tree by calling the tree widget’s ``[takeTopLevelItem()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeWidget.html#PySide6.QtWidgets.QTreeWidget.takeTopLevelItem)  function, but items from lower levels are removed by calling their parent item’s ``[takeChild()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeWidgetItem.html#PySide6.QtWidgets.QTreeWidgetItem.takeChild)  function. Items are inserted in the top level of the tree with the ``[insertTopLevelItem()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeWidget.html#PySide6.QtWidgets.QTreeWidget.insertTopLevelItem)  function. At lower levels in the tree, the parent item’s ``[insertChild()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeWidgetItem.html#PySide6.QtWidgets.QTreeWidgetItem.insertChild)  function is used.

It is easy to move items around between the top level and lower levels in the tree. We just need to check whether the items are top-level items or not, and this information is supplied by each item’s `parent()` function. For example, we can remove the current item in the tree widget regardless of its location:

> 

```
parent = currentItem.parent()
index = int()
if parent:
    index = parent.indexOfChild(treeWidget.currentItem())
    del parent.takeChild(index)
else:
    index = treeWidget.indexOfTopLevelItem(treeWidget.currentItem())
    del treeWidget.takeTopLevelItem(index)
```

Inserting the item somewhere else in the tree widget follows the same pattern:

> 

```
    parent = currentItem.parent()
    newItem = QTreeWidgetItem()
    if parent:
        newItem = QTreeWidgetItem(parent, treeWidget.currentItem())
else:
newItem = QTreeWidgetItem(treeWidget, treeWidget.currentItem())
```

### Table widgets[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#table-widgets)

Tables of items similar to those found in spreadsheet applications are constructed with the `QTableWidget` and `QTableWidgetItem`. These provide a scrolling table widget with headers and items to use within it.

Tables can be created with a set number of rows and columns, or these can be added to an unsized table as they are needed.

> 

```
tableWidget = QTableWidget()
tableWidget = QTableWidget(12, 3, self)
```

Items are constructed outside the table before being added to the table at the required location:

> 

```
newItem = QTableWidgetItem(tr("%1").arg(()
    pow(row, column+1)))
tableWidget.setItem(row, column, newItem)
```

Horizontal and vertical headers can be added to the table by constructing items outside the table and using them as headers:

> 

```
valuesHeaderItem = QTableWidgetItem(tr("Values"))
tableWidget.setHorizontalHeaderItem(0, valuesHeaderItem)
```

Note that the rows and columns in the table begin at zero.

> 

### Common features[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#common-features)

There are a number of item-based features common to each of the convenience classes that are available through the same interfaces in each class. We present these in the following sections with some examples for different widgets. Look at the list of [Model/View Classes](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  for each of the widgets for more details about the use of each function used.

> 

#### Hidden items[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#hidden-items)

It is sometimes useful to be able to hide items in an item view widget rather than remove them. Items for all of the above widgets can be hidden and later shown again. You can determine whether an item is hidden by calling the isItemHidden() function, and items can be hidden with `setItemHidden()`.

Since this operation is item-based, the same function is available for all three convenience classes.

> 

#### Selections[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#selections)

The way items are selected is controlled by the widget’s selection mode ( `SelectionMode` ). This property controls whether the user can select one or many items and, in many-item selections, whether the selection must be a continuous range of items. The selection mode works in the same way for all of the above widgets.

> 

Single item selections:  Where the user needs to choose a single item from a widget, the default `SingleSelection` mode is most suitable. In this mode, the current item and the selected item are the same.

Multi-item selections:  In this mode, the user can toggle the selection state of any item in the widget without changing the existing selection, much like the way non-exclusive checkboxes can be toggled independently.

Extended selections:  Widgets that often require many adjacent items to be selected, such as those found in spreadsheets, require the `ExtendedSelection` mode. In this mode, continuous ranges of items in the widget can be selected with both the mouse and the keyboard. Complex selections, involving many items that are not adjacent to other selected items in the widget, can also be created if modifier keys are used.

If the user selects an item without using a modifier key, the existing selection is cleared.

The selected items in a widget are read using the `selectedItems()` function, providing a list of relevant items that can be iterated over. For example, we can find the sum of all the numeric values within a list of selected items with the following code:

> 

```
> selected = tableWidget.selectedItems()
number = 0
total = 0
for item in selected:
    ok = bool()
    value = item.text().toDouble(ok)
    if ok and not item.text().isEmpty():
        total += value
        number += 1
```

Note that for the single selection mode, the current item will be in the selection. In the multi-selection and extended selection modes, the current item may not lie within the selection, depending on the way the user formed the selection.

> 

#### Searching[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#searching)

It is often useful to be able to find items within an item view widget, either as a developer or as a service to present to users. All three item view convenience classes provide a common `findItems()` function to make this as consistent and simple as possible.

Items are searched for by the text that they contain according to criteria specified by a selection of values from Qt::MatchFlags. We can obtain a list of matching items with the `findItems()` function:

> 

```
> found = treeWidget.findItems(
    itemText, Qt.MatchWildcard)
for item in found:
    item.setSelected(True)
    # Show the item->text(0) for each item.
```

The above code causes items in a tree widget to be selected if they contain the text given in the search string. This pattern can also be used in the list and table widgets.

> 

## Using Drag and Drop with Item Views[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#using-drag-and-drop-with-item-views)

Qt’s drag and drop infrastructure is fully supported by the model/view framework. Items in lists, tables, and trees can be dragged within the views, and data can be imported and exported as MIME-encoded data.

The standard views automatically support internal drag and drop, where items are moved around to change the order in which they are displayed. By default, drag and drop is not enabled for these views because they are configured for the simplest, most common uses. To allow items to be dragged around, certain properties of the view need to be enabled, and the items themselves must also allow dragging to occur.

The requirements for a model that only allows items to be exported from a view, and which does not allow data to be dropped into it, are fewer than those for a fully-enabled drag and drop model.

See also the [Model Subclassing Reference](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  for more information about enabling drag and drop support in new models.

> 

### Using convenience views[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#using-convenience-views)

Each of the types of item used with ``[QListWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListWidget.html#PySide6.QtWidgets.QListWidget)  , ``[QTableWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableWidget.html#PySide6.QtWidgets.QTableWidget)  , and ``[QTreeWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeWidget.html#PySide6.QtWidgets.QTreeWidget)  is configured to use a different set of flags by default. For example, each ``[QListWidgetItem](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListWidgetItem.html#PySide6.QtWidgets.QListWidgetItem)  or ``[QTreeWidgetItem](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeWidgetItem.html#PySide6.QtWidgets.QTreeWidgetItem)  is initially enabled, checkable, selectable, and can be used as the source of a drag and drop operation; each ``[QTableWidgetItem](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableWidgetItem.html#PySide6.QtWidgets.QTableWidgetItem)  can also be edited and used as the target of a drag and drop operation.

Although all of the standard items have one or both flags set for drag and drop, you generally need to set various properties in the view itself to take advantage of the built-in support for drag and drop:

> 

- 

To enable item dragging, set the view’s ``[dragEnabled()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id5)  property to `true`.

- 

To allow the user to drop either internal or external items within the view, set the view’s ``[viewport()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractScrollArea.html#PySide6.QtWidgets.QAbstractScrollArea.viewport)  ‘s ``[acceptDrops()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#id0)  property to `true`.

- 

To show the user where the item currently being dragged will be placed if dropped, set the view’s ``[showDropIndicator()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id12)  property. This provides the user with continuously updating information about item placement within the view.

For example, we can enable drag and drop in a list widget with the following lines of code:

> 

```
listWidget = QListWidget(self)
listWidget.setSelectionMode(QAbstractItemView.SingleSelection)
listWidget.setDragEnabled(True)
listWidget.viewport().setAcceptDrops(True)
listWidget.setDropIndicatorShown(True)
```

The result is a list widget which allows the items to be copied around within the view, and even lets the user drag items between views containing the same type of data. In both situations, the items are copied rather than moved.

To enable the user to move the items around within the view, we must set the list widget’s ``[dragDropMode()](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#id3)  :

> 

```
listWidget.setDragDropMode(QAbstractItemView.InternalMove)
```

### Using model/view classes[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#using-model-view-classes)

Setting up a view for drag and drop follows the same pattern used with the convenience views. For example, a ``[QListView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListView.html#PySide6.QtWidgets.QListView)  can be set up in the same way as a ``[QListWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListWidget.html#PySide6.QtWidgets.QListWidget)  :

> 

```
listView = QListView(self)
listView.setSelectionMode(QAbstractItemView.ExtendedSelection)
listView.setDragEnabled(True)
listView.setAcceptDrops(True)
listView.setDropIndicatorShown(True)
```

Since access to the data displayed by the view is controlled by a model, the model used also has to provide support for drag and drop operations. The actions supported by a model can be specified by reimplementing the QAbstractItemModel::supportedDropActions() function. For example, copy and move operations are enabled with the following code:

> 

```
def supportedDropActions(self):
    return Qt.CopyAction | Qt.MoveAction
```

Although any combination of values from Qt::DropActions can be given, the model needs to be written to support them. For example, to allow Qt::MoveAction to be used properly with a list model, the model must provide an implementation of QAbstractItemModel::removeRows(), either directly or by inheriting the implementation from its base class.

> 

#### Enabling drag and drop for items[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#enabling-drag-and-drop-for-items)

Models indicate to views which items can be dragged, and which will accept drops, by reimplementing the QAbstractItemModel::flags() function to provide suitable flags.

For example, a model which provides a simple list based on QAbstractListModel can enable drag and drop for each of the items by ensuring that the flags returned contain the Qt::ItemIsDragEnabled and Qt::ItemIsDropEnabled values:

> 

```
def flags(self, index):
    default_flags = super().flags(index)
    if index.isValid():
        return Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | default_flags
    return Qt.ItemIsDropEnabled | default_flags
```

Note that items can be dropped into the top level of the model, but dragging is only enabled for valid items.

In the above code, since the model is derived from QStringListModel, we obtain a default set of flags by calling its implementation of the flags() function.

> 

#### Encoding exported data[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#encoding-exported-data)

When items of data are exported from a model in a drag and drop operation, they are encoded into an appropriate format corresponding to one or more MIME types. Models declare the MIME types that they can use to supply items by reimplementing the QAbstractItemModel::mimeTypes() function, returning a list of standard MIME types.

For example, a model that only provides plain text would provide the following implementation:

> 

```
def mimeTypes(self):
    return ["application/vnd.text.list"]
```

The model must also provide code to encode data in the advertised format. This is achieved by reimplementing the QAbstractItemModel::mimeData() function to provide a QMimeData object, just as in any other drag and drop operation.

The following code shows how each item of data, corresponding to a given list of indexes, is encoded as plain text and stored in a QMimeData object.

> 

```
def mimeData(self, indexes):
    mime_data = QMimeData()
    encoded_data = QByteArray()
    stream = QDataStream(encoded_data, QIODevice.WriteOnly)
    for index in indexes:
        if index.isValid():
            text = self.data(index, Qt.DisplayRole)
            stream.writeQString(text)

    mime_data.setData("application/vnd.text.list", encoded_data)
    return mime_data
```

Since a list of model indexes is supplied to the function, this approach is general enough to be used in both hierarchical and non-heirarchical models.

Note that custom datatypes must be declared as meta objects and that stream operators must be implemented for them. See the QMetaObject class description for details.

> 

#### Inserting dropped data into a model[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#inserting-dropped-data-into-a-model)

The way that any given model handles dropped data depends on both its type (list, table, or tree) and the way its contents is likely to be presented to the user. Generally, the approach taken to accommodate dropped data should be the one that most suits the model’s underlying data store.

Different types of model tend to handle dropped data in different ways. List and table models only provide a flat structure in which items of data are stored. As a result, they may insert new rows (and columns) when data is dropped on an existing item in a view, or they may overwrite the item’s contents in the model using some of the data supplied. Tree models are often able to add child items containing new data to their underlying data stores, and will therefore behave more predictably as far as the user is concerned.

Dropped data is handled by a model’s reimplementation of QAbstractItemModel::dropMimeData(). For example, a model that handles a simple list of strings can provide an implementation that handles data dropped onto existing items separately to data dropped into the top level of the model (i.e., onto an invalid item).

Models can forbid dropping on certain items, or depending on the dropped data, by reimplementing QAbstractItemModel::canDropMimeData().

The model first has to make sure that the operation should be acted on, the data supplied is in a format that can be used, and that its destination within the model is valid:

> 

```
def canDropMimeData(self, data, action, row, column, parent):
    if not data.hasFormat("application/vnd.text.list"):
        return False

    if column > 0:
        return False

    return True
def dropMimeData(self, data, action, row, column, parent):
    if not self.canDropMimeData(data, action, row, column, parent):
        return False

    if action == Qt.IgnoreAction:
        return True
```

A simple one column string list model can indicate failure if the data supplied is not plain text, or if the column number given for the drop is invalid.

The data to be inserted into the model is treated differently depending on whether it is dropped onto an existing item or not. In this simple example, we want to allow drops between existing items, before the first item in the list, and after the last item.

When a drop occurs, the model index corresponding to the parent item will either be valid, indicating that the drop occurred on an item, or it will be invalid, indicating that the drop occurred somewhere in the view that corresponds to top level of the model.

> 

```
begin_row = 0

if row != -1:
    begin_row = row
```

We initially examine the row number supplied to see if we can use it to insert items into the model, regardless of whether the parent index is valid or not.

> 

```
elif parent.isValid():
    begin_row = parent.row()
```

If the parent model index is valid, the drop occurred on an item. In this simple list model, we find out the row number of the item and use that value to insert dropped items into the top level of the model.

> 

```
else:
    begin_row = self.rowCount(QModelIndex())
```

When a drop occurs elsewhere in the view, and the row number is unusable, we append items to the top level of the model.

In hierarchical models, when a drop occurs on an item, it would be better to insert new items into the model as children of that item. In the simple example shown here, the model only has one level, so this approach is not appropriate.

> 

#### Decoding imported data[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#decoding-imported-data)

Each implementation of dropMimeData() must also decode the data and insert it into the model’s underlying data structure.

For a simple string list model, the encoded items can be decoded and streamed into a QStringList:

> 

```
encoded_data = data.data("application/vnd.text.list")
stream = QDataStream(encoded_data, QIODevice.ReadOnly)
new_items = []
while not stream.atEnd():
    new_items.append(stream.readQString())
```

The strings can then be inserted into the underlying data store. For consistency, this can be done through the model’s own interface:

> 

```
self.insertRows(begin_row, len(new_items), QModelIndex())
for text in new_items:
    idx = self.index(begin_row, 0, QModelIndex())
    self.setData(idx, text)
    begin_row += 1

return True
```

Note that the model will typically need to provide implementations of the QAbstractItemModel::insertRows() and QAbstractItemModel::setData() functions.

> 

## Proxy Models[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#proxy-models)

In the model/view framework, items of data supplied by a single model can be shared by any number of views, and each of these can possibly represent the same information in completely different ways. Custom views and delegates are effective ways to provide radically different representations of the same data. However, applications often need to provide conventional views onto processed versions of the same data, such as differently-sorted views onto a list of items.

Although it seems appropriate to perform sorting and filtering operations as internal functions of views, this approach does not allow multiple views to share the results of such potentially costly operations. The alternative approach, involving sorting within the model itself, leads to the similar problem where each view has to display items of data that are organized according to the most recent processing operation.

To solve this problem, the model/view framework uses proxy models to manage the information supplied between individual models and views. Proxy models are components that behave like ordinary models from the perspective of a view, and access data from source models on behalf of that view. The signals and slots used by the model/view framework ensure that each view is updated appropriately no matter how many proxy models are placed between itself and the source model.

> 

### Using proxy models[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#using-proxy-models)

Proxy models can be inserted between an existing model and any number of views. Qt is supplied with a standard proxy model, QSortFilterProxyModel, that is usually instantiated and used directly, but can also be subclassed to provide custom filtering and sorting behavior. The QSortFilterProxyModel class can be used in the following way:

> 

```
filterModel = QSortFilterProxyModel(parent)
filterModel.setSourceModel(stringListModel)

filteredView = QListView()
filteredView.setModel(filterModel)
```

Since proxy models inherit from QAbstractItemModel, they can be connected to any kind of view, and can be shared between views. They can also be used to process the information obtained from other proxy models in a pipeline arrangement.

The QSortFilterProxyModel class is designed to be instantiated and used directly in applications. More specialized proxy models can be created by subclassing this classes and implementing the required comparison operations.

> 

### Customizing proxy models[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#customizing-proxy-models)

Generally, the type of processing used in a proxy model involves mapping each item of data from its original location in the source model to either a different location in the proxy model. In some models, some items may have no corresponding location in the proxy model; these models are filtering  proxy models. Views access items using model indexes provided by the proxy model, and these contain no information about the source model or the locations of the original items in that model.

QSortFilterProxyModel enables data from a source model to be filtered before being supplied to views, and also allows the contents of a source model to be supplied to views as pre-sorted data.

> 

#### Custom filtering models[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#custom-filtering-models)

The QSortFilterProxyModel class provides a filtering model that is fairly versatile, and which can be used in a variety of common situations. For advanced users, QSortFilterProxyModel can be subclassed, providing a mechanism that enables custom filters to be implemented.

Subclasses of QSortFilterProxyModel can reimplement two virtual functions that are called whenever a model index from the proxy model is requested or used:

> 

- 

filterAcceptsColumn() is used to filter specific columns from part of the source model.

- 

filterAcceptsRow() is used to filter specific rows from part of the source model.

The default implementations of the above functions in QSortFilterProxyModel return true to ensure that all items are passed through to views; reimplementations of these functions should return false to filter out individual rows and columns.

> 

#### Custom sorting models[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#custom-sorting-models)

QSortFilterProxyModel instances use std::stable_sort() function to set up mappings between items in the source model and those in the proxy model, allowing a sorted hierarchy of items to be exposed to views without modifying the structure of the source model. To provide custom sorting behavior, reimplement the lessThan() function to perform custom comparisons.

> 

## Model Subclassing Reference[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-subclassing-reference)

Model subclasses need to provide implementations of many of the virtual functions defined in the QAbstractItemModel base class. The number of these functions that need to be implemented depends on the type of model - whether it supplies views with a simple list, a table, or a complex hierarchy of items. Models that inherit from QAbstractListModel and QAbstractTableModel can take advantage of the default implementations of functions provided by those classes. Models that expose items of data in tree-like structures must provide implementations for many of the virtual functions in QAbstractItemModel.

The functions that need to be implemented in a model subclass can be divided into three groups:

> 

- 

Item data handling:  All models need to implement functions to enable views and delegates to query the dimensions of the model, examine items, and retrieve data.

- 

Navigation and index creation:  Hierarchical models need to provide functions that views can call to navigate the tree-like structures they expose, and obtain model indexes for items.

- 

Drag and drop support and MIME type handling:  Models inherit functions that control the way that internal and external drag and drop operations are performed. These functions allow items of data to be described in terms of MIME types that other components and applications can understand.

### Item data handling[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#item-data-handling)

Models can provide varying levels of access to the data they provide: They can be simple read-only components, some models may support resizing operations, and others may allow items to be edited.

> 

### Read-Only access[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#read-only-access)

To provide read-only access to data provided by a model, the following functions must  be implemented in the model’s subclass:

> 

flags()

Used by other components to obtain information about each item provided by the model. In many models, the combination of flags should include Qt::ItemIsEnabled and Qt::ItemIsSelectable.

data()

Used to supply item data to views and delegates. Generally, models only need to supply data for Qt::DisplayRole and any application-specific user roles, but it is also good practice to provide data for Qt::ToolTipRole, Qt::AccessibleTextRole, and Qt::AccessibleDescriptionRole. See the Qt::ItemDataRole enum documentation for information about the types associated with each role.

headerData()

Provides views with information to show in their headers. The information is only retrieved by views that can display header information.

rowCount()

Provides the number of rows of data exposed by the model.

These four functions must be implemented in all types of model, including list models (QAbstractListModel subclasses) and table models (QAbstractTableModel subclasses).

Additionally, the following functions must  be implemented in direct subclasses of QAbstractTableModel and QAbstractItemModel:

> 

columnCount()

Provides the number of columns of data exposed by the model. List models do not provide this function because it is already implemented in QAbstractListModel.

#### Editable items[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#editable-items)

Editable models allow items of data to be modified, and may also provide functions to allow rows and columns to be inserted and removed. To enable editing, the following functions must be implemented correctly:

> 

flags()

Must return an appropriate combination of flags for each item. In particular, the value returned by this function must include Qt::ItemIsEditable in addition to the values applied to items in a read-only model.

setData()

Used to modify the item of data associated with a specified model index. To be able to accept user input, provided by user interface elements, this function must handle data associated with Qt::EditRole. The implementation may also accept data associated with many different kinds of roles specified by Qt::ItemDataRole. After changing the item of data, models must emit the dataChanged() signal to inform other components of the change.

setHeaderData()

Used to modify horizontal and vertical header information. After changing the item of data, models must emit the headerDataChanged() signal to inform other components of the change.

#### Resizable models[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#resizable-models)

All types of model can support the insertion and removal of rows. Table models and hierarchical models can also support the insertion and removal of columns. It is important to notify other components about changes to the model’s dimensions both before  and after  they occur. As a result, the following functions can be implemented to allow the model to be resized, but implementations must ensure that the appropriate functions are called to notify attached views and delegates:

> 

insertRows()

Used to add new rows and items of data to all types of model. Implementations must call beginInsertRows() before  inserting new rows into any underlying data structures, and call endInsertRows() immediately afterwards .

removeRows()

Used to remove rows and the items of data they contain from all types of model. Implementations must call beginRemoveRows() before  rows are removed from any underlying data structures, and call endRemoveRows() immediately afterwards .

insertColumns()

Used to add new columns and items of data to table models and hierarchical models. Implementations must call beginInsertColumns() before  inserting new columns into any underlying data structures, and call endInsertColumns() immediately afterwards .

removeColumns()

Used to remove columns and the items of data they contain from table models and hierarchical models. Implementations must call beginRemoveColumns() before  columns are removed from any underlying data structures, and call endRemoveColumns() immediately afterwards .

Generally, these functions should return true if the operation was successful. However, there may be cases where the operation only partly succeeded; for example, if less than the specified number of rows could be inserted. In such cases, the model should return false to indicate failure to enable any attached components to handle the situation.

The signals emitted by the functions called in implementations of the resizing API give attached components the chance to take action before any data becomes unavailable. The encapsulation of insert and remove operations with begin and end functions also enable the model to manage persistent model indexes correctly.

Normally, the begin and end functions are capable of informing other components about changes to the model’s underlying structure. For more complex changes to the model’s structure, perhaps involving internal reorganization, sorting of data or any other structural change, it is necessary to perform the following sequence:

> 

- 

Emit the layoutAboutToBeChanged() signal

- 

Update internal data which represents the structure of the model.

- 

Update persistent indexes using changePersistentIndexList()

- 

Emit the layoutChanged() signal.

This sequence can be used for any structural update in lieu of the more high-level and convenient protected methods. For example, if a model of two million rows needs to have all odd numbered rows removed, that is 1 million discountiguous ranges of 1 element each. It would be possible to use beginRemoveRows and endRemoveRows 1 million times, but that would obviously be inefficient. Instead, this can be signalled as a single layout change which updates all necessary persistent indexes at once.

> 

#### Lazy population of model data[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#lazy-population-of-model-data)

Lazy population of model data effectively allows requests for information about the model to be deferred until it is actually needed by views.

Some models need to obtain data from remote sources, or must perform time-consuming operations to obtain information about the way the data is organized. Since views generally request as much information as possible in order to accurately display model data, it can be useful to restrict the amount of information returned to them to reduce unnecessary follow-up requests for data.

In hierarchical models where finding the number of children of a given item is an expensive operation, it is useful to ensure that the model’s rowCount() implementation is only called when necessary. In such cases, the hasChildren() function can be reimplemented to provide an inexpensive way for views to check for the presence of children and, in the case of ``[QTreeView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeView.html#PySide6.QtWidgets.QTreeView)  , draw the appropriate decoration for their parent item.

Whether the reimplementation of hasChildren() returns `true` or `false`, it may not be necessary for the view to call rowCount() to find out how many children are present. For example, ``[QTreeView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeView.html#PySide6.QtWidgets.QTreeView)  does not need to know how many children there are if the parent item has not been expanded to show them.

If it is known that many items will have children, reimplementing hasChildren() to unconditionally return `true` is sometimes a useful approach to take. This ensures that each item can be later examined for children while making initial population of model data as fast as possible. The only disadvantage is that items without children may be displayed incorrectly in some views until the user attempts to view the non-existent child items.

> 

### Navigation and model index creation[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#navigation-and-model-index-creation)

Hierarchical models need to provide functions that views can call to navigate the tree-like structures they expose, and obtain model indexes for items.

> 

#### Parents and children[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#parents-and-children)

Since the structure exposed to views is determined by the underlying data structure, it is up to each model subclass to create its own model indexes by providing implementations of the following functions:

> 

index()

Given a model index for a parent item, this function allows views and delegates to access children of that item. If no valid child item - corresponding to the specified row, column, and parent model index, can be found, the function must return QModelIndex(), which is an invalid model index.

parent()

Provides a model index corresponding to the parent of any given child item. If the model index specified corresponds to a top-level item in the model, or if there is no valid parent item in the model, the function must return an invalid model index, created with the empty QModelIndex() constructor.

Both functions above use the createIndex() factory function to generate indexes for other components to use. It is normal for models to supply some unique identifier to this function to ensure that the model index can be re-associated with its corresponding item later on.

> 

### Drag and drop support and MIME type handling[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#drag-and-drop-support-and-mime-type-handling)

The model/view classes support drag and drop operations, providing default behavior that is sufficient for many applications. However, it is also possible to customize the way items are encoded during drag and drop operations, whether they are copied or moved by default, and how they are inserted into existing models.

Additionally, the convenience view classes implement specialized behavior that should closely follow that expected by existing developers. The [Convenience Views](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  section provides an overview of this behavior.

> 

#### MIME data[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#mime-data)

By default, the built-in models and views use an internal MIME type (`application/x-qabstractitemmodeldatalist`) to pass around information about model indexes. This specifies data for a list of items, containing the row and column numbers of each item, and information about the roles that each item supports.

Data encoded using this MIME type can be obtained by calling QAbstractItemModel::mimeData() with a QModelIndexList containing the items to be serialized.

When implementing drag and drop support in a custom model, it is possible to export items of data in specialized formats by reimplementing the following function:

> 

mimeData()

This function can be reimplemented to return data in formats other than the default `application/x-qabstractitemmodeldatalist` internal MIME type.

Subclasses can obtain the default QMimeData object from the base class and add data to it in additional formats.

For many models, it is useful to provide the contents of items in common format represented by MIME types such as `text/plain` and `image/png`. Note that images, colors and HTML documents can easily be added to a QMimeData object with the QMimeData::setImageData(), QMimeData::setColorData(), and QMimeData::setHtml() functions.

> 

#### Accepting dropped data[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#accepting-dropped-data)

When a drag and drop operation is performed over a view, the underlying model is queried to determine which types of operation it supports and the MIME types it can accept. This information is provided by the QAbstractItemModel::supportedDropActions() and QAbstractItemModel::mimeTypes() functions. Models that do not override the implementations provided by QAbstractItemModel support copy operations and the default internal MIME type for items.

When serialized item data is dropped onto a view, the data is inserted into the current model using its implementation of QAbstractItemModel::dropMimeData(). The default implementation of this function will never overwrite any data in the model; instead, it tries to insert the items of data either as siblings of an item, or as children of that item.

To take advantage of QAbstractItemModel’s default implementation for the built-in MIME type, new models must provide reimplementations of the following functions:

> 

insertRows()

These functions enable the model to automatically insert new data using the existing implementation provided by QAbstractItemModel::dropMimeData().

insertColumns()

setData()

Allows the new rows and columns to be populated with items.

setItemData()

This function provides more efficient support for populating new items.

To accept other forms of data, these functions must be reimplemented:

> 

supportedDropActions()

Used to return a combination of drop actions, indicating the types of drag and drop operations that the model accepts.

mimeTypes()

Used to return a list of MIME types that can be decoded and handled by the model. Generally, the MIME types that are supported for input into the model are the same as those that it can use when encoding data for use by external components.

dropMimeData()

Performs the actual decoding of the data transferred by drag and drop operations, determines where in the model it will be set, and inserts new rows and columns where necessary. How this function is implemented in subclasses depends on the requirements of the data exposed by each model.

If the implementation of the dropMimeData() function changes the dimensions of a model by inserting or removing rows or columns, or if items of data are modified, care must be taken to ensure that all relevant signals are emitted. It can be useful to simply call reimplementations of other functions in the subclass, such as setData(), insertRows(), and insertColumns(), to ensure that the model behaves consistently.

In order to ensure drag operations work properly, it is important to reimplement the following functions that remove data from the model:

> 

- 

removeRows()

- 

removeRow()

- 

removeColumns()

- 

removeColumn()

For more information about drag and drop with item views, refer to [Using drag and drop with item views](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  .

> 

#### Convenience views[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#convenience-views)

The convenience views ( ``[QListWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListWidget.html#PySide6.QtWidgets.QListWidget)  , ``[QTableWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableWidget.html#PySide6.QtWidgets.QTableWidget)  , and ``[QTreeWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeWidget.html#PySide6.QtWidgets.QTreeWidget)  ) override the default drag and drop functionality to provide less flexible, but more natural behavior that is appropriate for many applications. For example, since it is more common to drop data into cells in a ``[QTableWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableWidget.html#PySide6.QtWidgets.QTableWidget)  , replacing the existing contents with the data being transferred, the underlying model will set the data of the target items rather than insert new rows and columns into the model. For more information on drag and drop in convenience views, you can see [Using drag and drop with item views](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#model-view-programming)  .

> 

### Performance optimization for large amounts of data[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#performance-optimization-for-large-amounts-of-data)

The canFetchMore() function checks if the parent has more data available and returns `true` or false accordingly. The fetchMore() function fetches data based on the parent specified. Both these functions can be combined, for example, in a database query involving incremental data to populate a QAbstractItemModel. We reimplement canFetchMore() to indicate if there is more data to be fetched and fetchMore() to populate the model as required.

Another example would be dynamically populated tree models, where we reimplement fetchMore() when a branch in the tree model is expanded.

If your reimplementation of fetchMore() adds rows to the model, you need to call beginInsertRows() and endInsertRows(). Also, both canFetchMore() and fetchMore() must be reimplemented as their default implementation returns false and does nothing.

> 

## The Model/View Classes[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#the-model-view-classes)

These classes use the model/view design pattern in which the underlying data (in the model) is kept separate from the way the data is presented and manipulated by the user (in the view).

> 

``[QAbstractItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate)

The QAbstractItemDelegate class is used to display and edit data items from a model.

``[QAbstractItemView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView)

The QAbstractItemView class provides the basic functionality for item view classes.

``[QColumnView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QColumnView.html#PySide6.QtWidgets.QColumnView)

The QColumnView class provides a model/view implementation of a column view.

``[QDataWidgetMapper](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDataWidgetMapper.html#PySide6.QtWidgets.QDataWidgetMapper)

The QDataWidgetMapper class provides mapping between a section of a data model to widgets.

``[QHeaderView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QHeaderView.html#PySide6.QtWidgets.QHeaderView)

The QHeaderView class provides a header row or header column for item views.

``[QItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QItemDelegate.html#PySide6.QtWidgets.QItemDelegate)

The QItemDelegate class provides display and editing facilities for data items from a model.

``[QItemEditorFactory](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QItemEditorFactory.html#PySide6.QtWidgets.QItemEditorFactory)

The QItemEditorFactory class provides widgets for editing item data in views and delegates.

``[QItemEditorCreatorBase](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QItemEditorCreatorBase.html#PySide6.QtWidgets.QItemEditorCreatorBase)

The QItemEditorCreatorBase class provides an abstract base class that must be subclassed when implementing new item editor creators.

`QItemEditorCreator`

The QItemEditorCreator class makes it possible to create item editor creator bases without subclassing QItemEditorCreatorBase.

`QStandardItemEditorCreator`

The QStandardItemEditorCreator class provides the possibility to register widgets without having to subclass QItemEditorCreatorBase.

``[QListView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListView.html#PySide6.QtWidgets.QListView)

The QListView class provides a list or icon view onto a model.

``[QListWidgetItem](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListWidgetItem.html#PySide6.QtWidgets.QListWidgetItem)

The QListWidgetItem class provides an item for use with the QListWidget item view class.

``[QListWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListWidget.html#PySide6.QtWidgets.QListWidget)

The QListWidget class provides an item-based list widget.

``[QStyledItemDelegate](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate)

The QStyledItemDelegate class provides display and editing facilities for data items from a model.

``[QTableView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableView.html#PySide6.QtWidgets.QTableView)

The QTableView class provides a default model/view implementation of a table view.

``[QTableWidgetSelectionRange](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableWidgetSelectionRange.html#PySide6.QtWidgets.QTableWidgetSelectionRange)

The QTableWidgetSelectionRange class provides a way to interact with selection in a model without using model indexes and a selection model.

``[QTableWidgetItem](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableWidgetItem.html#PySide6.QtWidgets.QTableWidgetItem)

The QTableWidgetItem class provides an item for use with the QTableWidget class.

``[QTableWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableWidget.html#PySide6.QtWidgets.QTableWidget)

The QTableWidget class provides an item-based table view with a default model.

``[QTreeView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeView.html#PySide6.QtWidgets.QTreeView)

The QTreeView class provides a default model/view implementation of a tree view.

``[QTreeWidgetItem](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeWidgetItem.html#PySide6.QtWidgets.QTreeWidgetItem)

The QTreeWidgetItem class provides an item for use with the QTreeWidget convenience class.

``[QTreeWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeWidget.html#PySide6.QtWidgets.QTreeWidget)

The QTreeWidget class provides a tree view that uses a predefined tree model.

``[QTreeWidgetItemIterator](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeWidgetItemIterator.html#PySide6.QtWidgets.QTreeWidgetItemIterator)

The QTreeWidgetItemIterator class provides a way to iterate over the items in a QTreeWidget instance.

## Related Examples[¶](https://doc.qt.io/qtforpython-6/overviews/qtwidgets-model-view-programming.html#related-examples)

> 

- 

Simple Tree Model
