<!--
source: https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html
retrieved: 2026-10-31T21:19:05.776856+00:00
final_url: https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html
content_type: text/html
-->

# PySide6 - Qt for Python

[Skip to content](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#furo-main-content)

[Qt for Python](https://doc.qt.io/qtforpython-6/index.html)

[Back to top](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html)

# PySide6[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#pyside6)

## 6.12.0[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id1)

- 

[PYSIDE-3302](https://qt-project.atlassian.net/browse//PYSIDE-3302)  QtQmlFeatures, a new module providing reactive QObject properties through @auto_properties, @watch, @effect, and @computed, has been added.

- 

[PYSIDE-3294](https://qt-project.atlassian.net/browse//PYSIDE-3294)  QMetaObject::className() now returns qualified names for nested classes, separated by dots (“Outer.Inner”).

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Deployment: pyside6-deploy now supports a [tool.pyside6.deploy] section in the pyproject.toml file.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Deployment: pyside6-deploy, pyside6-android-deploy, and pyside6-project deploy now accept –no-install to skip automatic build-dependency installation.

- 

[PYSIDE-3459](https://qt-project.atlassian.net/browse//PYSIDE-3459)  Deployment: pyside6-deploy now creates standalone packages by default; use –onefile to retain the former default.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  cross_compile_android: JDK lookup and NDK quarantine on macOS have been fixed.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Android Deployment: The NDK version in the tool has been updated to r28c. The limited API wheel tag has been raised to cp310.

- 

[PYSIDE-3425](https://qt-project.atlassian.net/browse//PYSIDE-3425)  Android Deployment now supports host Python versions 3.10 through 3.14 and produces binaries compatible with Android devices using 16 KB memory pages.

- 

[PYSIDE-3425](https://qt-project.atlassian.net/browse//PYSIDE-3425)  Android Deployment now reports unmet prerequisites instead of hanging and reliably deploys applications using QtQmlFeatures.

- 

[PYSIDE-3038](https://qt-project.atlassian.net/browse//PYSIDE-3038)  Type hints: QDate and QDateTime have been fixed to accept Python datetime types.

- 

[PYSIDE-3221](https://qt-project.atlassian.net/browse//PYSIDE-3221)  Initial support for Python 3.15 has been added.

- 

[PYSIDE-3276](https://qt-project.atlassian.net/browse//PYSIDE-3276)  The stylekit examples have been updated for 6.12.

- 

[PYSIDE-3301](https://qt-project.atlassian.net/browse//PYSIDE-3301)  The colorpaletteclient example has been updated and a small server has been added.

- 

[PYSIDE-3301](https://qt-project.atlassian.net/browse//PYSIDE-3301)  Object list model example: Use @auto_properties and @watch

- 

[PYSIDE-3306](https://qt-project.atlassian.net/browse//PYSIDE-3306)  CMake build: Regressions affecting header packaging and include paths have been fixed.

- 

[PYSIDE-3314](https://qt-project.atlassian.net/browse//PYSIDE-3314)  Support for iOS has been added.

- 

[PYSIDE-3319](https://qt-project.atlassian.net/browse//PYSIDE-3319)  Security: A potential zip slip in Android deploy wheel extraction has been fixed.

- 

[PYSIDE-3319](https://qt-project.atlassian.net/browse//PYSIDE-3319)  Security: Android Deployment now verifies downloaded NDK and command-line tools before extracting them.

- 

[PYSIDE-3319](https://qt-project.atlassian.net/browse//PYSIDE-3319)  Security: pyside6-qml now warns before importing Python files adjacent to the QML source.

- 

[PYSIDE-3320](https://qt-project.atlassian.net/browse//PYSIDE-3320)  Security: A potential shell injection in pyside6-deploy on Windows has been fixed.

- 

[PYSIDE-3331](https://qt-project.atlassian.net/browse//PYSIDE-3331)  Security: Deserialization of non-trivial classes from QDataStream/QSettings is now blocked.

- 

[PYSIDE-3334](https://qt-project.atlassian.net/browse//PYSIDE-3334)  Security: Qt Widgets Designer will now request a one-time confirmation for loading Python plugins.

- 

[PYSIDE-3335](https://qt-project.atlassian.net/browse//PYSIDE-3335)  QBitArray.fromBits(PyBuffer)/QBitArray.bits() have been added.

- 

[PYSIDE-3338](https://qt-project.atlassian.net/browse//PYSIDE-3338)  Type hints: The copy  return type annotation has been fixed.

- 

[PYSIDE-3359](https://qt-project.atlassian.net/browse//PYSIDE-3359)  Security: QUiLoader::loadUiType() no longer searches the pyside6-uic binary in the path. This now requires an explicit opt-in via a keyword argument and will trigger a warning. We generally recommend moving away from the function in favor of using pyside6-uic at build time.

- 

[PYSIDE-3364](https://qt-project.atlassian.net/browse//PYSIDE-3364)  A warning when encountering an unknown signal parameter has been added.

- 

[PYSIDE-3365](https://qt-project.atlassian.net/browse//PYSIDE-3365)  QStandardItemModel: A memory leak when using clear() after populating using invisibleRootItem() has been fixed.

- 

[PYSIDE-3366](https://qt-project.atlassian.net/browse//PYSIDE-3366)  SBOM documents have been added. (todo done?)

- 

[PYSIDE-3367](https://qt-project.atlassian.net/browse//PYSIDE-3367)  The copy constructors of QTree/Table/ListWidgetItem have been removed.

- 

[PYSIDE-3374](https://qt-project.atlassian.net/browse//PYSIDE-3374)  Issues occuring when registering QML singletons after creating the QQmlEngine have been fixed.

- 

[PYSIDE-3376](https://qt-project.atlassian.net/browse//PYSIDE-3376)  A bug affecting connections to private methods (prefixed by “__”) when invoked by derived classes has been fixed.

- 

[PYSIDE-3409](https://qt-project.atlassian.net/browse//PYSIDE-3409)  A crash retrieving the wrapper for QtWebEngineCore.ResourceRequestBody has been fixed.

- 

[PYSIDE-3423](https://qt-project.atlassian.net/browse//PYSIDE-3423)  A crash returning a class implementing the sequence protocol from QAbstractItemModel.data() has been fixed.

- 

[PYSIDE-3426](https://qt-project.atlassian.net/browse//PYSIDE-3426)  Android: The prebuilt CPython is now being used, replacing manual cross-compilation.

- 

[PYSIDE-3469](https://qt-project.atlassian.net/browse//PYSIDE-3469)  A crash caused by stale pointers to QLayoutItem instances due to incorrect parenting has been fixed.

## 6.11.3[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id2)

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Deployment: An option “–no-install” to skip installing build dependencies has been added.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Deployment: The “python_path” config option has been removed.

- 

[PYSIDE-3463](https://qt-project.atlassian.net/browse//PYSIDE-3463)  A bug causing the object returned by QObject.thread() to have the wrong ownership has been fixed.

## 6.11.2[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id3)

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  pyside6-project: Options for deployment have been added.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Deployment: Nuitka has been updated to 4.1.1.

- 

[PYSIDE-2206](https://qt-project.atlassian.net/browse//PYSIDE-2206)  The buildings part of the OSM buildings demo has been added.

- 

[PYSIDE-2541](https://qt-project.atlassian.net/browse//PYSIDE-2541)  Type hints: The QML decorators type hint has been fixed.

- 

[PYSIDE-3168](https://qt-project.atlassian.net/browse//PYSIDE-3168)  Class QCanvasGradientStop has been added.

- 

[PYSIDE-3203](https://qt-project.atlassian.net/browse//PYSIDE-3203)  Type hints: QSplitter.replaceWidget() has been fixed to return optional.

- 

[PYSIDE-3301](https://qt-project.atlassian.net/browse//PYSIDE-3301)  The colorpaletteclient example has been updated and a small server has been added.

- 

[PYSIDE-3311](https://qt-project.atlassian.net/browse//PYSIDE-3311)  pyside6-project/qmltyperegistrar: Empty .qmltypes files have been fixed.

- 

[PYSIDE-3339](https://qt-project.atlassian.net/browse//PYSIDE-3339)  Type hints: The return type of QObject.parent() has been fixed.

- 

[PYSIDE-3347](https://qt-project.atlassian.net/browse//PYSIDE-3347)  Documentation: The module index pages have been updated and some security-relevant documentation has been added.

- 

[PYSIDE-3353](https://qt-project.atlassian.net/browse//PYSIDE-3353)  A crash calling a class method, such as QObject::tr() using the snake case feature has been fixed.

- 

[PYSIDE-3356](https://qt-project.atlassian.net/browse//PYSIDE-3356)  Exception handling in QCoreApplication.processEvents() has been fixed.

- 

[PYSIDE-3360](https://qt-project.atlassian.net/browse//PYSIDE-3360)  metaobjectdump: Decorated Python enum classes are now recognized.

- 

[PYSIDE-3380](https://qt-project.atlassian.net/browse//PYSIDE-3380)  A crash using QAction.menu() has been fixed.

- 

[PYSIDE-3406](https://qt-project.atlassian.net/browse//PYSIDE-3406)  Support for developer versions of libclang with non-standard values of LLVM_PACKAGE_VERSION has been improved.

- 

[PYSIDE-3417](https://qt-project.atlassian.net/browse//PYSIDE-3417)  The Qt6QuickShapesDesignHelpers library missing from the wheel has been added.

## 6.11.1[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id4)

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Nuitka dependency of pyside6-deploy is updated to 4.0.

- 

[PYSIDE-3288](https://qt-project.atlassian.net/browse//PYSIDE-3288)  It is now possible to defer deletion of QObjects in case they get garbage-collected by a thread different from their owner thread and thus ensure the correct thread affinity.

- 

[PYSIDE-3031](https://qt-project.atlassian.net/browse//PYSIDE-3031)  A memory leak in buffer protocol handling of QByteArray has been fixed (Non-Limited API only).

- 

[PYSIDE-3051](https://qt-project.atlassian.net/browse//PYSIDE-3051)  The mappings and type hints for the division operator have been fixed.

- 

[PYSIDE-3105](https://qt-project.atlassian.net/browse//PYSIDE-3105)  Cross compilation support has been improved.

- 

[PYSIDE-3243](https://qt-project.atlassian.net/browse//PYSIDE-3243)  A missing library error occurring in the PySidePlugin on Windows has been fixed (Non-Limited API only).

- 

[PYSIDE-3288](https://qt-project.atlassian.net/browse//PYSIDE-3288)  libpyside: Warning messages are now prefixed.

- 

[PYSIDE-3290](https://qt-project.atlassian.net/browse//PYSIDE-3290)  Deployment: QML files not being included in deployment have been fixed.

- 

[PYSIDE-3294](https://qt-project.atlassian.net/browse//PYSIDE-3294)  Qt Widgets Designer plugin: It is now possible to use inner classes as custom widgets. The interoperability between Python custom widgets and C++ custom widgets (with or without namespaces) has been improved.

- 

[PYSIDE-3295](https://qt-project.atlassian.net/browse//PYSIDE-3295)  The CMake build has been fixed.

- 

[PYSIDE-3297](https://qt-project.atlassian.net/browse//PYSIDE-3297)  Qt Labs libraries new in 6.11.have been added.

- 

[PYSIDE-3299](https://qt-project.atlassian.net/browse//PYSIDE-3299)  Deployment: Multi-line arrays in the TOML config file are now also properly parsed when using Python <3.11.

- 

[PYSIDE-3304](https://qt-project.atlassian.net/browse//PYSIDE-3304)  type hints: The type hints for QMetaObject.invokeMethod() have been fixed.

- 

[PYSIDE-3307](https://qt-project.atlassian.net/browse//PYSIDE-3307)  A crash occurring when using unittest.mock/patch on slot receivers has been fixed.

- 

[QTBUG-71856] The document viewer demo has been updated, now featuring switching UI language changes at runtime.

- 

[QTBUG-130067] An example demoing the newly added Qt Quick Controls StyleKit example has been added.

## 6.11.0[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id5)

- 

QQmlComponent: Functions create_withownership() and createWithInitialProperties_withownership() have been added to return created QML objects with Python ownership.

- 

[PYSIDE-2716](https://qt-project.atlassian.net/browse//PYSIDE-2716)  It is now possible to specify options for pyside6-uic and pyside6-rcc in a pyproject.toml file. This is useful for example to disable overly aggressive compression by pyside6-rcc which may result in files that are not usable on all platforms.

- 

[PYSIDE-2786](https://qt-project.atlassian.net/browse//PYSIDE-2786)  The minimum supported Python version has been raised to 3.10.

- 

[PYSIDE-3168](https://qt-project.atlassian.net/browse//PYSIDE-3168)  A number of examples have been updated for Qt 6.11.

- 

[PYSIDE-3168](https://qt-project.atlassian.net/browse//PYSIDE-3168)  The QtCanvasPainter module and an example have been added.

- 

[PYSIDE-3193](https://qt-project.atlassian.net/browse//PYSIDE-3193)  Type hints: The return type of QTranslator.translate() has been fixed.

- 

[PYSIDE-3257](https://qt-project.atlassian.net/browse//PYSIDE-3257)  pyside6-designer has been fixed to display Python help.

- 

[PYSIDE-3273](https://qt-project.atlassian.net/browse//PYSIDE-3273)  A warning displayed when calling sys.exit() in a overridden function has been suppressed.

- 

[PYSIDE-3279](https://qt-project.atlassian.net/browse//PYSIDE-3279)  Signal emission has been sped up by code optimizations.

- 

[QTBUG-131837] The QWebView class of QtWebView and an example demoing it have been added.

- 

[QTBUG-143503] It is now possible to populate QML views with JSON data as shown in the updated colorpaletteclient example.

## 6.10.3[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id6)

- 

[PYSIDE-2862](https://qt-project.atlassian.net/browse//PYSIDE-2862)  QHttpServerConfiguration has been added.

- 

[PYSIDE-3079](https://qt-project.atlassian.net/browse//PYSIDE-3079)  type hints: The type hints of the Slot decorator have been fixed.

- 

[PYSIDE-3263](https://qt-project.atlassian.net/browse//PYSIDE-3263)  Documentation on how to use image resources in ui files has been improved.

- 

[PYSIDE-3265](https://qt-project.atlassian.net/browse//PYSIDE-3265)  pyside6-project: Additional command line arguments to “run” are now suported.

- 

[PYSIDE-3266](https://qt-project.atlassian.net/browse//PYSIDE-3266)  A crash when connecting a slot with result to a signal has been fixed.

- 

[PYSIDE-3267](https://qt-project.atlassian.net/browse//PYSIDE-3267)  Missing libraries and plugins required for pyside6-svgtoqml have been added.

- 

[PYSIDE-3280](https://qt-project.atlassian.net/browse//PYSIDE-3280)  A bug related to QWebEngineExtensionManager.extensions() has been fixed.

## 6.10.2[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id7)

- 

[PYSIDE-2206](https://qt-project.atlassian.net/browse//PYSIDE-2206)  The multimedia player example has been updated.

- 

[PYSIDE-3189](https://qt-project.atlassian.net/browse//PYSIDE-3189)  Type hints: Some missing optional return types have been added.

- 

[PYSIDE-3231](https://qt-project.atlassian.net/browse//PYSIDE-3231)  Type hints: Element access for all QMatrix types has been fixed to consistently provide a call operator (operator()) as well as mgetitem (operator[][]).

- 

[PYSIDE-3233](https://qt-project.atlassian.net/browse//PYSIDE-3233)  The Shiboken6Tools CMake module has been fixed to find Python on manylinux_2_34.

- 

[PYSIDE-3241](https://qt-project.atlassian.net/browse//PYSIDE-3241)  The metatype JSON files that had been missing from the wheels have been added.

- 

[PYSIDE-3248](https://qt-project.atlassian.net/browse//PYSIDE-3248)  QtWebView has been added to the Android wheels.

- 

[PYSIDE-3034](https://qt-project.atlassian.net/browse//PYSIDE-3034)  Type hints: Public variables have been added.

- 

[PYSIDE-3250](https://qt-project.atlassian.net/browse//PYSIDE-3250)  The snake_case feature has been fixed to also work for imported modules.

- 

[PYSIDE-3254](https://qt-project.atlassian.net/browse//PYSIDE-3254)  The include-dir specification in the pkgconfig file of libpyside has been fixed.

- 

[PYSIDE-3244](https://qt-project.atlassian.net/browse//PYSIDE-3244)  A regression causing tuples to be converted to

- 

[PYSIDE-3256](https://qt-project.atlassian.net/browse//PYSIDE-3256)  QVariantList when passed in a QVariant has been fixed.

## 6.10.1[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id8)

- 

[PYSIDE-2206](https://qt-project.atlassian.net/browse//PYSIDE-2206)  Many examples and tutorials have been updated.

- 

[PYSIDE-3147](https://qt-project.atlassian.net/browse//PYSIDE-3147)  Python 3.14 is now supported.

- 

[PYSIDE-3174](https://qt-project.atlassian.net/browse//PYSIDE-3174)  type hints: The type annotations of QtCore.Slot have been fixed.

- 

[PYSIDE-3179](https://qt-project.atlassian.net/browse//PYSIDE-3179)  A regression breaking QtRemoteObjects has been fixed.

- 

[PYSIDE-3190](https://qt-project.atlassian.net/browse//PYSIDE-3190)  Disconnecting multiple index-based connections has been fixed.

- 

[PYSIDE-3201](https://qt-project.atlassian.net/browse//PYSIDE-3201)  An issue handling types with equal names in signal/slot connections has been fixed.

- 

[PYSIDE-3206](https://qt-project.atlassian.net/browse//PYSIDE-3206)  A conversion from tuple to QVariantList has been added.

- 

[PYSIDE-3213](https://qt-project.atlassian.net/browse//PYSIDE-3213)  QQuickTextDocument can now be used as a property in QML.

- 

[PYSIDE-3217](https://qt-project.atlassian.net/browse//PYSIDE-3217)  A regression breaking enumeration properties in Qt Widgets Designer has been fixed.

- 

[PYSIDE-3227](https://qt-project.atlassian.net/browse//PYSIDE-3227)  A bug affecting QMetaProperty attributes when using @Property has been fixed.

## 6.10.0[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id9)

PySide now uses multi-phase Python extension module initialization for the non-deployed case. For scripting appplications, this implies that it is no longer sufficient to call the Init() function of a module to load the module in order to be able to access its type structs for binding variables. Instead, PyImport_ImportModule() must be used (see scriptable application example).

- 

[PYSIDE-1735](https://qt-project.atlassian.net/browse//PYSIDE-1735)  @QEnum, @QFlag and QMetaEnum now support unsigned 64 bit values for QML usage (with the exception of Qt Widgets Designer), following the support added to Qt.

- 

[PYSIDE-2840](https://qt-project.atlassian.net/browse//PYSIDE-2840)  It is now possible to use @QEnum/@QFlag-decorated enumerations as properties of custom widgets in Qt Widgets Designer.

- 

[PYSIDE-2916](https://qt-project.atlassian.net/browse//PYSIDE-2916)  The invocation of functions overridden in Python has been optimized for speed.

- 

[PYSIDE-3012](https://qt-project.atlassian.net/browse//PYSIDE-3012)  type hints: The annotations of QPropertyAnimation have been fixed.

- 

[PYSIDE-3084](https://qt-project.atlassian.net/browse//PYSIDE-3084)  Enumerations are now stored as such instead of an opaque PyObjectWrapper in functions returning QVariant.

- 

[PYSIDE-3137](https://qt-project.atlassian.net/browse//PYSIDE-3137)  A warning occurring when doing the first signal connection from a thread has been fixed.

- 

[PYSIDE-3143](https://qt-project.atlassian.net/browse//PYSIDE-3143)  A bug causing events to be wrongly converted to QStandardItem has been fixed. Also, a leak of QStandardItem instances returned from QStandardItemModel functions has been fixed.

- 

[PYSIDE-3146](https://qt-project.atlassian.net/browse//PYSIDE-3146)  Deployment: Values generated into pysidedeploy.spec are now sorted.

- 

[PYSIDE-3147](https://qt-project.atlassian.net/browse//PYSIDE-3147)  Initial adaptations for the upcoming Python version 3.14 have been done.

- 

[PYSIDE-3164](https://qt-project.atlassian.net/browse//PYSIDE-3164)  type hints: Enum values have been added to the stubs for improved type checking.

- 

[PYSIDE-3178](https://qt-project.atlassian.net/browse//PYSIDE-3178)  type hints: The return types of QPoint(F)/QSize(F).toTuple have been fixed.

- 

[QTBUG-110428] The QtExampleIcons module has been removed due to the removal of the underlying library in Qt.

## 6.9.3[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id10)

- 

[PYSIDE-2308](https://qt-project.atlassian.net/browse//PYSIDE-2308)  type hints: The type annotation of the notify parameter of QtCore.Property has been corrected.

- 

[PYSIDE-3047](https://qt-project.atlassian.net/browse//PYSIDE-3047)  type hints: The type annotations of QPolygon(F)’s operator<< have been corrected.

- 

[PYSIDE-3048](https://qt-project.atlassian.net/browse//PYSIDE-3048)  type hints: The type annotations now contain enum values.

- 

[PYSIDE-3162](https://qt-project.atlassian.net/browse//PYSIDE-3162)  type hints: The ‘from future  import annotations’ have been removed from the stub files.

- 

[PYSIDE-3163](https://qt-project.atlassian.net/browse//PYSIDE-3163)  type hints: The mypy comment has been removed from the docstring.

- 

[PYSIDE-2206](https://qt-project.atlassian.net/browse//PYSIDE-2206)  Tye QtBluetooth/heartrate_game example has been updated.

## 6.9.2[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id11)

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Android Deployment: Installing packages is no longer forced.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Desktop Deployment: A warning for Qt resource files has been fixed.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Desktop Deployment: Nuitka has been upgraded to 2.7.11.

- 

[PYSIDE-2846](https://qt-project.atlassian.net/browse//PYSIDE-2846)  type hints: The mypy version has been increased.

- 

[PYSIDE-2846](https://qt-project.atlassian.net/browse//PYSIDE-2846)  type hints: Signature warnings about QObject properties of unknown type passed to the constructor have been fixed.

- 

[PYSIDE-2938](https://qt-project.atlassian.net/browse//PYSIDE-2938)  The MSVC runtime libraries bundled in Windows wheels have been updated.

- 

[PYSIDE-3095](https://qt-project.atlassian.net/browse//PYSIDE-3095)  pyside6-project lupdate now supports specifying subdirectories in .ts file names.

- 

[PYSIDE-3115](https://qt-project.atlassian.net/browse//PYSIDE-3115)  A bug affecting QVariant conversion of Python classes inheriting QGraphicsProxyObject has been fixed.

- 

[PYSIDE-3119](https://qt-project.atlassian.net/browse//PYSIDE-3119)  A SECURITY.md document required for Github has been added.

- 

[PYSIDE-3124](https://qt-project.atlassian.net/browse//PYSIDE-3124)  Documentation about thread affinity has been added to the Signals and Slot tutorial.

- 

[PYSIDE-3127](https://qt-project.atlassian.net/browse//PYSIDE-3127)  A bug occurring when choosing a camera in the camera example has been fixed.

- 

[PYSIDE-3132](https://qt-project.atlassian.net/browse//PYSIDE-3132)  A crash calling setItemDelegateForColumn/Row() repeatedly has been fixed.

- 

[PYSIDE-3133](https://qt-project.atlassian.net/browse//PYSIDE-3133)  A crash on conversion errors when parsing keyword arguments has been fixed.

- 

[PYSIDE-3135](https://qt-project.atlassian.net/browse//PYSIDE-3135)  type hints: typing.Self is no longer modified in versions < 3.11.

- 

[PYSIDE-3139](https://qt-project.atlassian.net/browse//PYSIDE-3139)  type hints: The return types of QGuiApplication.screenAt() and QGuiApplication.modalWindow() have been fixed.

- 

[PYSIDE-3146](https://qt-project.atlassian.net/browse//PYSIDE-3146)  Deployment: Values generated into pysidedeploy.spec are now sorted.

- 

[PYSIDE-3147](https://qt-project.atlassian.net/browse//PYSIDE-3147)  Initial adaptations for the upcoming Python version 3.14 have been done.

- 

[PYSIDE-3148](https://qt-project.atlassian.net/browse//PYSIDE-3148)  A memory corruption occurring when connecting several signals to one non-QObject receiver has been fixed.

## 6.9.1[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id12)

- 

[PYSIDE-841](https://qt-project.atlassian.net/browse//PYSIDE-841)  An example showing an audio graph using Qt Graphs has been added.

- 

[PYSIDE-2193](https://qt-project.atlassian.net/browse//PYSIDE-2193)  A crash retrieving a Python type QObject property (encapsulated in a QVariant) been fixed.

- 

[PYSIDE-3052](https://qt-project.atlassian.net/browse//PYSIDE-3052)  class QMessageLogger has been added for handling debug, info, warning, critical, and fatal messages, including support for QLoggingCategory.

- 

[PYSIDE-3012](https://qt-project.atlassian.net/browse//PYSIDE-3012)  type hints: The type signature for the Property class has been fixed.

- 

[PYSIDE-3021](https://qt-project.atlassian.net/browse//PYSIDE-3021)  type-hints: The QMessagebox annotations has been fixed.

- 

[PYSIDE-3029](https://qt-project.atlassian.net/browse//PYSIDE-3029)  type-hints: The hints for properties on init  functions has been fixed.

- 

[PYSIDE-3041](https://qt-project.atlassian.net/browse//PYSIDE-3041)  type hints: The str parameter of QLineEdit.setText() has been made optional.

- 

[PYSIDE-3050](https://qt-project.atlassian.net/browse//PYSIDE-3050)  type hints: Type signature for QProgressDialog.setCancelButton has been fixed.

- 

[PYSIDE-3055](https://qt-project.atlassian.net/browse//PYSIDE-3055)  type hints: Type signature for QTabBar.setTabButton has been fixed.

- 

[PYSIDE-3056](https://qt-project.atlassian.net/browse//PYSIDE-3056)  type hints: Type signature for qtTrId has been fixed.

- 

[PYSIDE-3057](https://qt-project.atlassian.net/browse//PYSIDE-3057)  type hints: Type signature for QTreeWidget.setItemWidget has been fixed.

- 

[PYSIDE-3058](https://qt-project.atlassian.net/browse//PYSIDE-3058)  type hints: Return value for QTreeWidget.topLevelItem and QTreeWidget.takeTopLevelItem has been fixed.

- 

[PYSIDE-3059](https://qt-project.atlassian.net/browse//PYSIDE-3059)  type hints: The type signature for QObject class has been fixed.

- 

[PYSIDE-3061](https://qt-project.atlassian.net/browse//PYSIDE-3061)  The building of .pyi files in debug mode on Windows has been fixed.

- 

[PYSIDE-3067](https://qt-project.atlassian.net/browse//PYSIDE-3067)  A crash when entering a Qt message handler with a Python error set has been fixed.

- 

[PYSIDE-3069](https://qt-project.atlassian.net/browse//PYSIDE-3069)  A crash retrieving a QGraphicsProxyObject from a QVariant has been fixed.

- 

[PYSIDE-3078](https://qt-project.atlassian.net/browse//PYSIDE-3078)  type hints: The parent widget parameter of the QInputDialog get() methods has been made optional.

- 

[PYSIDE-3087](https://qt-project.atlassian.net/browse//PYSIDE-3087)  The dependency of pyside6-project on tomlkit has been removed.

- 

[PYSIDE-3089](https://qt-project.atlassian.net/browse//PYSIDE-3089)  An error in pyside6-metaobjectdump when encountering @Slot(result=None) has been fixed.

## 6.9.0[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id13)

- 

The usage of macros from CPython (limited API) has been reduced in favor of calling functions directly.

- 

Support for std::chrono::milliseconds has been added.

- 

Windows ARM64 was added as a new supported platform (technical preview)

- 

[PYSIDE-862](https://qt-project.atlassian.net/browse//PYSIDE-862)  Support for QtRemoteObjects has been extended.

- 

[PYSIDE-1057](https://qt-project.atlassian.net/browse//PYSIDE-1057)  A memory leak connecting to signals has been fixed.

- 

[PYSIDE-1277](https://qt-project.atlassian.net/browse//PYSIDE-1277)  A bug connecting signals by QMetaMethod has been fixed.

- 

[PYSIDE-1735](https://qt-project.atlassian.net/browse//PYSIDE-1735)  Most enumerations are now fully qualified in documentation and translated code snippets. Enum values automatically converted to “None_” are also correctly documented.

- 

[PYSIDE-2714](https://qt-project.atlassian.net/browse//PYSIDE-2714)  Qt Creator 17.x+ and PySide tools now support projects that have a pyproject.toml instead of a *.pyproject

- 

[PYSIDE-2846](https://qt-project.atlassian.net/browse//PYSIDE-2846)  The type annotation of the Slot() decorator has been fixed.

- 

[PYSIDE-2966](https://qt-project.atlassian.net/browse//PYSIDE-2966)  A bug making it possible to instantiate non-constructible classes and namespaces has been fixed.

- 

[PYSIDE-2891](https://qt-project.atlassian.net/browse//PYSIDE-2891)  A bug in signature handling affecting 32bit builds has been fixed.

- 

[PYSIDE-2958](https://qt-project.atlassian.net/browse//PYSIDE-2958)  Building against unsupported python versions has been enabled.

- 

[PYSIDE-2997](https://qt-project.atlassian.net/browse//PYSIDE-2997)  Type hints: The signature of QMessageBox.information() has been fixed.

- 

[PYSIDE-3001](https://qt-project.atlassian.net/browse//PYSIDE-3001)  QtAsyncio: The error messages printed on an exceptions in tasks have been improved.

- 

[PYSIDE-3002](https://qt-project.atlassian.net/browse//PYSIDE-3002)  QPaintEngine’s virtual functions taking a C-style array of geometry primitives have been fixed.

- 

[PYSIDE-3003](https://qt-project.atlassian.net/browse//PYSIDE-3003)  Type hints: A bug causing overloads to be omitted has been fixed.

- 

[PYSIDE-3004](https://qt-project.atlassian.net/browse//PYSIDE-3004)  A crash in slots when receiving an object-type parameter passed by const-ref has been fixed.

- 

[PYSIDE-3005](https://qt-project.atlassian.net/browse//PYSIDE-3005)  A bug affecting QOpenGLShaderProgram.setUniformValueArray(int,float*,int,int) has been fixed.

- 

[PYSIDE-3012](https://qt-project.atlassian.net/browse//PYSIDE-3012)  Type hints: Since using Callable, Iterable and Sequence from typing is deprecated, they are imported from collections.abc.

- 

[PYSIDE-3012](https://qt-project.atlassian.net/browse//PYSIDE-3012)  Type hints: Object inheritance has been removed from classes.

- 

[PYSIDE-3013](https://qt-project.atlassian.net/browse//PYSIDE-3013)  QFont.Tag(str), QFont.Tag.fromString(), QFont.Tag.fromValue() have been added.

- 

[PYSIDE-3014](https://qt-project.atlassian.net/browse//PYSIDE-3014)  QAbstractSpinBox.fixup() has been fixed.

- 

[PYSIDE-3017](https://qt-project.atlassian.net/browse//PYSIDE-3017)  The overloads of QCanDbcFileParser.parse() have been fixed.

- 

[PYSIDE-3020](https://qt-project.atlassian.net/browse//PYSIDE-3020)  A bug disconnecting a string-based connection by passing a callable has been fixed.

- 

[QTBUG-72968] The type of the “result” parameter of the native event filters has been changed to “qintptr” for Qt 6.

- 

[QTBUG-108199] PySide has been adapted to the deprecation of Qt::TimeSpec in Qt.

## 6.8.3[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id14)

- 

[PYSIDE-1735](https://qt-project.atlassian.net/browse//PYSIDE-1735)  Most enumerations are now fully qualified in documentation and translated code snippets. Enum values automatically converted to “None_” are also correctly documented.

- 

[PYSIDE-2846](https://qt-project.atlassian.net/browse//PYSIDE-2846)  The type annotation of the Slot() decorator has been fixed.

- 

[PYSIDE-2997](https://qt-project.atlassian.net/browse//PYSIDE-2997)  Type hints: The signature of QMessageBox.information() has been fixed.

- 

[PYSIDE-3001](https://qt-project.atlassian.net/browse//PYSIDE-3001)  QtAsyncio: The error messages printed on an exceptions in tasks have been improved.

- 

[PYSIDE-3002](https://qt-project.atlassian.net/browse//PYSIDE-3002)  QPaintEngine’s virtual functions taking a C-style array of geometry primitives have been fixed.

- 

[PYSIDE-3003](https://qt-project.atlassian.net/browse//PYSIDE-3003)  Type hints: A bug causing overloads to be omitted has been fixed.

- 

[PYSIDE-3012](https://qt-project.atlassian.net/browse//PYSIDE-3012)  Type hints: Since using Callable, Iterable and Sequence from typing is deprecated, they are imported from collections.abc.

- 

[PYSIDE-3012](https://qt-project.atlassian.net/browse//PYSIDE-3012)  Type hints: Object inheritance has been removed from classes.

- 

[PYSIDE-3013](https://qt-project.atlassian.net/browse//PYSIDE-3013)  QFont.Tag(str), QFont.Tag.fromString(), QFont.Tag.fromValue() have been added.

- 

[PYSIDE-3014](https://qt-project.atlassian.net/browse//PYSIDE-3014)  QAbstractSpinBox.fixup() has been fixed.

- 

[PYSIDE-3017](https://qt-project.atlassian.net/browse//PYSIDE-3017)  The overloads of QCanDbcFileParser.parse() have been fixed.

- 

[PYSIDE-3020](https://qt-project.atlassian.net/browse//PYSIDE-3020)  A bug disconnecting a string-based connection by passing a callable has been fixed.

- 

[QTBUG-72968] The type of the “result” parameter of the native event filters has been changed to “qintptr” for Qt 6.

## 6.8.2[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id15)

- 

[PYSIDE-487](https://qt-project.atlassian.net/browse//PYSIDE-487)  Some missing bindings were added.

- 

[PYSIDE-841](https://qt-project.atlassian.net/browse//PYSIDE-841)  The simple bar graph (QtGraphs) and zoomlinechart (QtCharts) examples have been added.

- 

[PYSIDE-1106](https://qt-project.atlassian.net/browse//PYSIDE-1106)  Documentation: A number of missing documentation pages has been added. The module pages were updated and improved, now showing the QML types more prominently. Parameter names and documentation of global and/or added functions have been added.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Deployment: Development folders are no longer included in the deployed executable. A bug parsing “from . import x” has been fixed. .webp files are now supported. Nuitka has been upgraded to 2.5.1. Non-existent plugins are now disregarded.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Android Deployment: The Android NDK is now automatically downloaded.

- 

[PYSIDE-1735](https://qt-project.atlassian.net/browse//PYSIDE-1735)  Examples and tests have been changed to use fully qualified enumerations.

- 

[PYSIDE-2624](https://qt-project.atlassian.net/browse//PYSIDE-2624)  Type hints: Positional parameters are now used according to PEP 570.

- 

[PYSIDE-2846](https://qt-project.atlassian.net/browse//PYSIDE-2846)  Type hints: Properties in constructors are now supported (including snake_case). Empty enums have been fixed for mypy 1.14.

- 

[PYSIDE-2846](https://qt-project.atlassian.net/browse//PYSIDE-2846)  A crash related to inner classes in Qt3DRender has been fixed.

- 

[PYSIDE-2936](https://qt-project.atlassian.net/browse//PYSIDE-2936)  A crash using QDBusUnixFileDescriptor in QDBusAbstractInterface::call() has been fixed.

- 

[PYSIDE-2939](https://qt-project.atlassian.net/browse//PYSIDE-2939)  Type hints: The heuristic for ambiguous signature removal has been fixed.

- 

[PYSIDE-2941](https://qt-project.atlassian.net/browse//PYSIDE-2941)  Type hints: Some optional return annotations have been fixed.

- 

[PYSIDE-2946](https://qt-project.atlassian.net/browse//PYSIDE-2946)  A crash registering smart pointer types conversions of class hierarchies has been fixed.

## 6.8.2[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id16)

- 

[PYSIDE-3000](https://qt-project.atlassian.net/browse//PYSIDE-3000)  A bug in 6.8.2 causing the MSVC runtime libraries no longer being shipped has been fixed.

## 6.8.1[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id17)

- 

[PYSIDE-1106](https://qt-project.atlassian.net/browse//PYSIDE-1106)  Documentation: Inner classes are now shown nested into their outer classes for referencing to work correctly.

- 

[PYSIDE-2689](https://qt-project.atlassian.net/browse//PYSIDE-2689)  Documentation: A workaround has been made to fix the search context of class pages.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Deployment: The bundling of QML files has been improved by using nuitka’s ‘include-data-dir’ command line option.

- 

[PYSIDE-2206](https://qt-project.atlassian.net/browse//PYSIDE-2206)  The OSM-buildings demo (maps part) and the zoomlinechart example have been added.

- 

[PYSIDE-2211](https://qt-project.atlassian.net/browse//PYSIDE-2211)  Type hints: Errors resulting from inconsistencies between binary operators and their corresponding in-place operators have been fixed.

- 

[PYSIDE-2751](https://qt-project.atlassian.net/browse//PYSIDE-2751)  Support for Python 3.13 has been added.

- 

[PYSIDE-2825](https://qt-project.atlassian.net/browse//PYSIDE-2825)  Missing libraries required for QtWebView have been added.

- 

[PYSIDE-2846](https://qt-project.atlassian.net/browse//PYSIDE-2846)  Type hints: mypy support has been greatly improved and the .pyi files are now tested.

- 

[PYSIDE-2884](https://qt-project.atlassian.net/browse//PYSIDE-2884)  Type hints: typing.Callable has been fixed to include the parameters.

- 

[PYSIDE-2886](https://qt-project.atlassian.net/browse//PYSIDE-2886)  Type hints: Multiple signatures and Union expressions have been fixed.

- 

[PYSIDE-2891](https://qt-project.atlassian.net/browse//PYSIDE-2891)  An issue affecting 32bit builds has been fixed.

- 

[PYSIDE-2893](https://qt-project.atlassian.net/browse//PYSIDE-2893)  The installation of the module doc snippet files has been fixed.

- 

[PYSIDE-2895](https://qt-project.atlassian.net/browse//PYSIDE-2895)  PySide’s init .py no longer contains build-directory-dependent code and PySide6. all  has been fixed to again work.

- 

[PYSIDE-2901](https://qt-project.atlassian.net/browse//PYSIDE-2901)  Documentation: Tutorials and reference pages related to Signal and Slots have been improved.

- 

[PYSIDE-2903](https://qt-project.atlassian.net/browse//PYSIDE-2903)  Type hints: Duplicated occurrences of ‘#’ in the pyi type specifications causing errors have been fixed.

- 

[PYSIDE-2910](https://qt-project.atlassian.net/browse//PYSIDE-2910)  Deployment: Bundling of the FluentWinUI3 style for Qt Quick Controls has been fixed.

- 

[PYSIDE-2913](https://qt-project.atlassian.net/browse//PYSIDE-2913)  QWebEngineDesktopMediaRequest has been added.

- 

[PYSIDE-2915](https://qt-project.atlassian.net/browse//PYSIDE-2915)  Type hints: Rich compare functions are now supported.

- 

[PYSIDE-2917](https://qt-project.atlassian.net/browse//PYSIDE-2917)  numpy version 2 is now used Python 3.10+.

## 6.8.1[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id18)

- 

[PYSIDE-2964](https://qt-project.atlassian.net/browse//PYSIDE-2964)  Added WebView to macOS wheels.

## 6.8.0[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id19)

- 

[PYSIDE-769](https://qt-project.atlassian.net/browse//PYSIDE-769)  QtAsyncio: The application argument has been removed from the loop policy.

- 

[PYSIDE-2221](https://qt-project.atlassian.net/browse//PYSIDE-2221)  The code for signal connections for Python callables not targeting a QMetaMethod has be reimplemented to simplify code and prepare for removal of the GIL.

- 

[PYSIDE-2404](https://qt-project.atlassian.net/browse//PYSIDE-2404)  Lazy loading has been extended to smart pointers and nested types.

- 

[PYSIDE-2620](https://qt-project.atlassian.net/browse//PYSIDE-2620)  pyside6-svgtoqml has been added.

- 

[PYSIDE-2701](https://qt-project.atlassian.net/browse//PYSIDE-2701)  The size of the generated code has been reduced.

- 

[PYSIDE-2701](https://qt-project.atlassian.net/browse//PYSIDE-2701)  Python formats with “#” in it are now supported.

- 

[PYSIDE-2711](https://qt-project.atlassian.net/browse//PYSIDE-2711)  An undesired invalidation of QObjects/QWidgets after calling parent(Widget)() has been fixed.

- 

[PYSIDE-2766](https://qt-project.atlassian.net/browse//PYSIDE-2766)  Android wheels are now provided.

- 

[PYSIDE-2786](https://qt-project.atlassian.net/browse//PYSIDE-2786)  Modern typing syntax is now used in examples and QtAsyncio code, enabled by a future import for Python 3.9, too.

- 

[PYSIDE-2805](https://qt-project.atlassian.net/browse//PYSIDE-2805)  An overload taking a slot connected to QMessageBox.accepted has been added to QMessageBox.open().

- 

[PYSIDE-2810](https://qt-project.atlassian.net/browse//PYSIDE-2810)  The number of QByteArray conversions in libpyside’s signal handling has been reduced.

- 

[PYSIDE-2820](https://qt-project.atlassian.net/browse//PYSIDE-2820)  Opaque containers of type QList can now be used for initial properties in QML.

- 

[PYSIDE-2803](https://qt-project.atlassian.net/browse//PYSIDE-2803)  Deployment: An issue in QML import scanning causing overly long command lines has been fixed.

- 

[PYSIDE-2837](https://qt-project.atlassian.net/browse//PYSIDE-2837)  The documentation has been restructured and updated.

- 

[PYSIDE-2859](https://qt-project.atlassian.net/browse//PYSIDE-2859)  QModelRoleDataSpan for implementing QAbstractItemModel.multiData() has been added.

- 

[PYSIDE-2840](https://qt-project.atlassian.net/browse//PYSIDE-2840)  Enumeration properties for Qt Designer custom widgets have been fixed.

- 

[PYSIDE-2845](https://qt-project.atlassian.net/browse//PYSIDE-2845)  QSemaphore.tryAcquire() has been fixed to work with the snake case feature. The existing C++ function try_acquire() has been removed.

- 

[PYSIDE-2846](https://qt-project.atlassian.net/browse//PYSIDE-2846)  Type hints: Many issues in the generated stub files have been fixed to enable checking with mypy.

## 6.7.3[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id20)

- 

A –flatpak option has been added to setup.py, enabling a flatpak build of Qt for Python.

- 

[PYSIDE-769](https://qt-project.atlassian.net/browse//PYSIDE-769)  QtAsyncio: The application argument has been removed from the loop policy.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Deployment: Nuitka has been updated to 2.3.7. Scanning for QML dependencies has been fixed to skip some directories.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Android Cross Compilation: INSTSONAME has been added.

- 

[PYSIDE-1877](https://qt-project.atlassian.net/browse//PYSIDE-1877)  Properties of type QAbstractItemModel can now be used in QML.

- 

[PYSIDE-2192](https://qt-project.atlassian.net/browse//PYSIDE-2192)  PySide Qt Gui applications can now be used in interactive mode, for example notebooks.

- 

[PYSIDE-2517](https://qt-project.atlassian.net/browse//PYSIDE-2517)  Type hints: The signatures of QObject.findChild()/ findChildren() have been improved to reflect the type passed in.

- 

[PYSIDE-2622](https://qt-project.atlassian.net/browse//PYSIDE-2622)  Deployment: Nuitka –standalone mode is now supported.

- 

[PYSIDE-2656](https://qt-project.atlassian.net/browse//PYSIDE-2656)  QtMultimedia on macOS has been fixed.

- 

[PYSIDE-2702](https://qt-project.atlassian.net/browse//PYSIDE-2702)  An option to force processing system headers has been added for cases where Qt is installed into the system.

- 

[PYSIDE-2752](https://qt-project.atlassian.net/browse//PYSIDE-2752)  Type hints: A syntax error caused by empty Enums has been fixed.

- 

[PYSIDE-2766](https://qt-project.atlassian.net/browse//PYSIDE-2766)  Android Deployment: pyside6-android-deploy now works macOS, too.

- 

[PYSIDE-2785](https://qt-project.atlassian.net/browse//PYSIDE-2785)  Deployment: ‘dist-packages’ is now skipped similar to ‘site-packages’ when scanning for QML dependencies.

- 

[PYSIDE-2788](https://qt-project.atlassian.net/browse//PYSIDE-2788)  Type hints: The signature of QFormLayout.getLayoutPosition() has been fixed.

- 

[PYSIDE-2789](https://qt-project.atlassian.net/browse//PYSIDE-2789)  numpy 2.0 is now supported.

- 

[PYSIDE-2790](https://qt-project.atlassian.net/browse//PYSIDE-2790)  QtAsyncio: cancel count and uncancel() have been added.

- 

[PYSIDE-2796](https://qt-project.atlassian.net/browse//PYSIDE-2796)  A potential crash in currentOpcode_Is_CallMethNoArgs() has been fixed.

- 

[PYSIDE-2799](https://qt-project.atlassian.net/browse//PYSIDE-2799)  QtAsyncio: A hang when an exception occurs inside a TaskGroup body has been fixed.

- 

[PYSIDE-2803](https://qt-project.atlassian.net/browse//PYSIDE-2803)  Desktop Deployment: Overflows of command lines on Windows have been fixed.

- 

[PYSIDE-2806](https://qt-project.atlassian.net/browse//PYSIDE-2806)  Desktop Deployment: The application name has been fixed.

- 

[PYSIDE-2814](https://qt-project.atlassian.net/browse//PYSIDE-2814)  Deployment: Arguments with spaces can now be used for “extra_args” due to using shlex for splitting the command line arguments.

- 

[PYSIDE-2819](https://qt-project.atlassian.net/browse//PYSIDE-2819)  The correct libclang is now used for arm64.

- 

[PYSIDE-2825](https://qt-project.atlassian.net/browse//PYSIDE-2825)  QtWebView has been added.

- 

[PYSIDE-2828](https://qt-project.atlassian.net/browse//PYSIDE-2828)  Documentation: The .qrc tutorial has been updated.

- 

[PYSIDE-2833](https://qt-project.atlassian.net/browse//PYSIDE-2833)  The QML tutorials have been updated.

- 

[PYSIDE-2834](https://qt-project.atlassian.net/browse//PYSIDE-2834)  QDir.entry(Info)List(QDir.Filter, QDir.SortFlags) has been fixed to work with Python 3.11 and later.

- 

[PYSIDE-2836](https://qt-project.atlassian.net/browse//PYSIDE-2836)  PySide6/ init .py now has a static list of modules, enabling code checkers to work.

- 

[PYSIDE-2870](https://qt-project.atlassian.net/browse//PYSIDE-2870)  A crash when using QStateMachine.postEvent() has been fixed.

## 6.7.2[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id21)

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Android Deployment now used the development branch of p4a.

- 

[PYSIDE-2712](https://qt-project.atlassian.net/browse//PYSIDE-2712)  Type hints: Modified types are no longer considered as eligible implicit conversions.

- 

[PYSIDE-2745](https://qt-project.atlassian.net/browse//PYSIDE-2745)  Exceptions occurring in a slot connected to a 0-delay singleShot timer signal are no longer suppressed.

- 

[PYSIDE-2747](https://qt-project.atlassian.net/browse//PYSIDE-2747)  Running on Fedora 40 with Python 3.12.3-2 has been fixed.

- 

[PYSIDE-2748](https://qt-project.atlassian.net/browse//PYSIDE-2748)  Type hints: QTranslator.translate() has been fixed.

- 

[PYSIDE-2749](https://qt-project.atlassian.net/browse//PYSIDE-2749)  Lazy Load: A performance regression showing in Qt event filters has been fixed.

- 

[PYSIDE-2750](https://qt-project.atlassian.net/browse//PYSIDE-2750)  Qt6VirtualKeyboardSettings have been added to the wheel.

- 

[PYSIDE-2756](https://qt-project.atlassian.net/browse//PYSIDE-2756)  Type hints: The return type of QItemSelection. init () has been fixed.

- 

[PYSIDE-2758](https://qt-project.atlassian.net/browse//PYSIDE-2758)  QQuickWebEngineProfile.setUrlRequestInterceptor() has been added.

- 

[PYSIDE-2759](https://qt-project.atlassian.net/browse//PYSIDE-2759)  The ownership of cache object passed to QNetworkAccessManager.setCache() has been fixed.

- 

[PYSIDE-2762](https://qt-project.atlassian.net/browse//PYSIDE-2762)  Type hints: The return type of QModelIndex.internalPointer() has been fixed.

- 

[PYSIDE-2767](https://qt-project.atlassian.net/browse//PYSIDE-2767)  Type hints: An error checking the property decorator has been fixed.

- 

[PYSIDE-2768](https://qt-project.atlassian.net/browse//PYSIDE-2768)  Type hints: smart pointer signatures have been fixed.

## 6.7.1[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id22)

- 

[PYSIDE-487](https://qt-project.atlassian.net/browse//PYSIDE-487)  A number of missing classes have been added.

- 

[PYSIDE-2629](https://qt-project.atlassian.net/browse//PYSIDE-2629)  Tooling: pyside6-qsb, pyside6-balsam and pyside6-balsamui have been added.

- 

[PYSIDE-2644](https://qt-project.atlassian.net/browse//PYSIDE-2644)  QtAsyncio: An issue with tasks with loop not cancelling has been fixed.

- 

[PYSIDE-2663](https://qt-project.atlassian.net/browse//PYSIDE-2663)  A crash when browsing https://outlook.com has been fixed.

- 

[PYSIDE-2665](https://qt-project.atlassian.net/browse//PYSIDE-2665)  A syntax error in the pyi-files has been fixed.

- 

[PYSIDE-2668](https://qt-project.atlassian.net/browse//PYSIDE-2668)  The comparison of QOperatingSystemVersion.OSType has been fixed.

- 

[PYSIDE-2675](https://qt-project.atlassian.net/browse//PYSIDE-2675)  Lazy Load: An issue with polymorphic classes has been fixed.

- 

[PYSIDE-2676](https://qt-project.atlassian.net/browse//PYSIDE-2676)  A crash with Python 3.12 when creating classes from meta classes has been fixed.

- 

[PYSIDE-2685](https://qt-project.atlassian.net/browse//PYSIDE-2685)  An error in the pyi-files related to the import of NoneType has been fixed.

- 

[PYSIDE-2686](https://qt-project.atlassian.net/browse//PYSIDE-2686)  Missing imports for types of return values have been added to the pyi-files.

- 

[PYSIDE-2698](https://qt-project.atlassian.net/browse//PYSIDE-2698)  A crash when querying the size of QtQml.ListProperty has been fixed and documentation for QtQml.ListProperty has been added.

- 

[PYSIDE-2705](https://qt-project.atlassian.net/browse//PYSIDE-2705)  Warnings about failures of QObject.disconnect() can now be suppressed.

- 

[PYSIDE-2709](https://qt-project.atlassian.net/browse//PYSIDE-2709)  A bug using legacy qmlRegisterType() for class hierarchies has been fixed.

- 

[QTBUG-123997] Multimedia: The renaming of the namespace QAudio to QtAudio has been undone following a revert in Qt.

## 6.7.0[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id23)

- 

setup.py now uses CMake Unity Build Mode by default.

- 

The namespace QAudio has been renamed to QtAudio in Qt 6.7. An alias has been created, but it may not work in all cases.

- 

pyside6-project now has an lupdate mode updating translation files (.ts) from the sources.

- 

Python code has been updated to be free of flake8 warnings using a custom configuration.

- 

For deployment, the supported version of Nuitka has been raised to 2.1.0.

- 

singleShot timers with a timeout of 0 now call the C++ function (which directly calls QMetaObject::invokeMethod) instead of manually creating and starting a timer object, slightly improving performance.

- 

[PYSIDE-769](https://qt-project.atlassian.net/browse//PYSIDE-769)  QtAsyncio: Fix a missing attribute error on Windows. Fix

- 

[PYSIDE-2641](https://qt-project.atlassian.net/browse//PYSIDE-2641)  QtAsyncio.run() not returning the result of a coroutine. It is now possible to disable the signal handler for SIGINT by passing a parameter to run(). The loop policy is reset after run() finishes.

- 

[PYSIDE-838](https://qt-project.atlassian.net/browse//PYSIDE-838)  Functions qCompress/qUncompress() taking a PyBuffer/len arguments have been fixed.

- 

[PYSIDE-1106](https://qt-project.atlassian.net/browse//PYSIDE-1106)  Documentation: Decorators, global functions and enumerations are now documented add indexed from the module page. The class documentation now uses more sphinx domain directives. Pages for all tools have been added. The order of the examples list has been changed to show relevant examples first.

- 

[PYSIDE-1275](https://qt-project.atlassian.net/browse//PYSIDE-1275)  QObject.disconnect() now returns False with a warning instead of raising an exception for non-fatal cases.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Deployment: Issues when using pyenv have been fixed. The finding of dependent modules has been improved. On Windows, this now requires the dumpbin tool, which is added to the path by calling the vcvarsall.bat script of Microsoft Visual Studio.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Android Deployment: The NDK version in the tool has been updated. Python has been updated to 3.11. CMake version 3.23 is now required. The wheels are no longer built with –limited-api. The generated pysidedeploy.spec has an explicit group called `android` which stores the wheels and plugins.

- 

[PYSIDE-1906](https://qt-project.atlassian.net/browse//PYSIDE-1906)  Hash value calculation has been optimized.

- 

[PYSIDE-2206](https://qt-project.atlassian.net/browse//PYSIDE-2206)  The colorpaletteclient demo as well as the hellographs and simplerhiwidget examples have been added.

- 

[PYSIDE-2215](https://qt-project.atlassian.net/browse//PYSIDE-2215)  Intersphinx support has been improved.

- 

[PYSIDE-2280](https://qt-project.atlassian.net/browse//PYSIDE-2280)  A type for os.PathLike type hints has been added.

- 

[PYSIDE-2404](https://qt-project.atlassian.net/browse//PYSIDE-2404)  Application startup time has been significantly decreased by creating the types on demand. The importing of numpy has also been deferred since it caused quite some delay.

- 

[PYSIDE-2432](https://qt-project.atlassian.net/browse//PYSIDE-2432)  A static create() function for decorated QML singletons has been added.

- 

[PYSIDE-2484](https://qt-project.atlassian.net/browse//PYSIDE-2484)  The QML type registration code has been ported to use RegisterTypeAndRevisions.

- 

[PYSIDE-2535](https://qt-project.atlassian.net/browse//PYSIDE-2535)  Obtaining DBUS properties from QDBusInterface has been fixed. As a consequence though, it is no longer possible to derive a Python class with signals/slots from QDBusInterface.

- 

[PYSIDE-2504](https://qt-project.atlassian.net/browse//PYSIDE-2504)  Documentation: Option ‘build_rst_docs’ has been deprecated in favor of ‘build_base_docs’.

- 

[PYSIDE-2524](https://qt-project.atlassian.net/browse//PYSIDE-2524)  It is now possible to connect signals to slots/lambdas with more arguments provided they have default parameters.

- 

[PYSIDE-2524](https://qt-project.atlassian.net/browse//PYSIDE-2524)  The signal connection code has been optimized.

- 

[PYSIDE-2543](https://qt-project.atlassian.net/browse//PYSIDE-2543)  QtQuickTest has been added.

- 

[PYSIDE-2576](https://qt-project.atlassian.net/browse//PYSIDE-2576)  Documentation: The extendedexplorer tutorial has been improved.

- 

[PYSIDE-2590](https://qt-project.atlassian.net/browse//PYSIDE-2590)  Some fixes have been made be able to cope with namespaced Qt builds.

- 

[PYSIDE-2610](https://qt-project.atlassian.net/browse//PYSIDE-2610)  The QTextureImageData methods returning an enumeration of QOpenGLTexture have been added.

- 

[PYSIDE-2605](https://qt-project.atlassian.net/browse//PYSIDE-2605)  An error about the C++ object being deleted when calling QWidget.style() in an embedded application has been fixed.

- 

[PYSIDE-2468](https://qt-project.atlassian.net/browse//PYSIDE-2468)  Deployment: Support for the Qt permission API has been added. macOS bundle applications are now created.

- 

[PYSIDE-2597](https://qt-project.atlassian.net/browse//PYSIDE-2597)  Desktop Deployment: The the plugins included have been optimized.

- 

[PYSIDE-2633](https://qt-project.atlassian.net/browse//PYSIDE-2633)  C++ typedefs of container instantiations are now registered in Python under their name, making possible to decorate slots with those names (for example, “QRemoteObjectSourceLocation”).

- 

[PYSIDE-2639](https://qt-project.atlassian.net/browse//PYSIDE-2639)  Segmentation fault with QLocale.system() has been fixed.

- 

[PYSIDE-2652](https://qt-project.atlassian.net/browse//PYSIDE-2652)  A bug when passing values of unsigned long long type exceeding the long long maximum value to float parameters has been fixed.

- 

[PYSIDE-2663](https://qt-project.atlassian.net/browse//PYSIDE-2663)  A crash in QtWebEngine browsing https://outlook.com has been fixed.

- 

[PYSIDE-2668](https://qt-project.atlassian.net/browse//PYSIDE-2668)  A bug when comparing QOperatingSystemVersion::OSType has been fixed.

- 

[QTBUG-119785] The Filesystemexplorer-example has been updated.

## 6.6.3[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id24)

- 

pyside6-project now also builds translation (.qm) files.

- 

[PYSIDE-769](https://qt-project.atlassian.net/browse//PYSIDE-769)  QtAsyncio: Fix a missing attribute error on Windows. Fix

- 

[PYSIDE-2641](https://qt-project.atlassian.net/browse//PYSIDE-2641)  QtAsyncio.run() not returning the result of a coroutine. It is now possible to disable the signal handler for SIGINT by passing a parameter to run(). The loop policy is reset after run() finishes.

- 

[PYSIDE-1112](https://qt-project.atlassian.net/browse//PYSIDE-1112)  Documentation: The list of tools has been updated.

- 

[PYSIDE-1112](https://qt-project.atlassian.net/browse//PYSIDE-1112)  Documentation: A page on the pyside6-project tool has been added.

- 

[PYSIDE-1955](https://qt-project.atlassian.net/browse//PYSIDE-1955)  Type hints: Add support for classmethods

- 

[PYSIDE-2206](https://qt-project.atlassian.net/browse//PYSIDE-2206)  An exit crash of the audiooutput example has been fixed.

- 

[PYSIDE-2263](https://qt-project.atlassian.net/browse//PYSIDE-2263)  Type hints: Support for class attributes has been added.

- 

[PYSIDE-2468](https://qt-project.atlassian.net/browse//PYSIDE-2468)  Documentation on the PySide6 Permission API has been added.

- 

[PYSIDE-2590](https://qt-project.atlassian.net/browse//PYSIDE-2590)  Some fixes have been made be able to cope with namespaced Qt builds.

- 

[PYSIDE-2599](https://qt-project.atlassian.net/browse//PYSIDE-2599)  The conversion of QVariant<->QMatrix x  has been fixed.

- 

[PYSIDE-2603](https://qt-project.atlassian.net/browse//PYSIDE-2603)  Documentation: A broken link to the widget styling tutorial has been fixed.

- 

[PYSIDE-2610](https://qt-project.atlassian.net/browse//PYSIDE-2610)  Inheritance from QAbstractTextureImage/ QTextureImageDataGenerator has been fixed.

- 

[PYSIDE-2612](https://qt-project.atlassian.net/browse//PYSIDE-2612)  Plain CMake builds with Limited API on Windows have been fixed.

- 

[PYSIDE-2613](https://qt-project.atlassian.net/browse//PYSIDE-2613)  Connecting to signals with QFlags<> arguments has been fixed.

- 

[PYSIDE-2627](https://qt-project.atlassian.net/browse//PYSIDE-2627)  A regression breaking calling Signal.connect() with QObject-derived callables has been fixed.

- 

[PYSIDE-2628](https://qt-project.atlassian.net/browse//PYSIDE-2628)  A crash using struct.unpack() on a QByteArray with Limited API has been fixed.

- 

[PYSIDE-2638](https://qt-project.atlassian.net/browse//PYSIDE-2638)  A crash when adding None to a QLayout has been fixed.

- 

[PYSIDE-2639](https://qt-project.atlassian.net/browse//PYSIDE-2639)  macOS: A segmentation fault in QLocale.system() has been fixed.

- 

[PYSIDE-2640](https://qt-project.atlassian.net/browse//PYSIDE-2640)  pyside6-qml now uses a QQuickView when the rootobject is a QQuickItem.

## 6.6.2[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id25)

- 

[PYSIDE-535](https://qt-project.atlassian.net/browse//PYSIDE-535)  PyPySide has been updated to Python 3.10

- 

[PYSIDE-769](https://qt-project.atlassian.net/browse//PYSIDE-769)  QtAsyncio: call_soon_threadsafe() and QtAsyncio.run() (with [PYSIDE-1112](https://qt-project.atlassian.net/browse//PYSIDE-1112)  keep_running and quit_qapp arguments) have been implemented. [PYSIDE-2561](https://qt-project.atlassian.net/browse//PYSIDE-2561)  A bug with Python 3.12 has been fixed. Documentation has [PYSIDE-2575](https://qt-project.atlassian.net/browse//PYSIDE-2575)  been added. Keyboard interrupts are now caught. Cancelling waiting tasks has been fixed. Tasks are now awaitable.

- 

[PYSIDE-1106](https://qt-project.atlassian.net/browse//PYSIDE-1106)  Documentation: The generation process has been optimized and warnings have been reduced.

- 

[PYSIDE-1586](https://qt-project.atlassian.net/browse//PYSIDE-1586)  Qt Charts: class QColorAxis has been added.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Android Deployment: The QtQuick dependency is now added when present.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Deployment problems when using pyenv have been fixed.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Nuitka has been upgraded to 1.8.0

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Deployment: An icon for the application has been added.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  A separate requirements.txt for Android deployment has been added.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Android Deployment: `buildozer` is now installed with the –init cli argument

- 

[PYSIDE-1931](https://qt-project.atlassian.net/browse//PYSIDE-1931)  Further hangs in QSql(Relational)TableModel.select() (PostGres with SSH tunnel) have been fixed.

- 

[PYSIDE-2206](https://qt-project.atlassian.net/browse//PYSIDE-2206)  Examples quick3d/proceduraltexture, sql/books have been updated. The contactslist has been added. Examples supported on Android are tagged as `Android`.

- 

[PYSIDE-2439](https://qt-project.atlassian.net/browse//PYSIDE-2439)  FindPython is now used instead of the deprecated FindPythonInterp and FindPythonLibs CMake modules.

- 

[PYSIDE-2539](https://qt-project.atlassian.net/browse//PYSIDE-2539)  Documentation: The enum name is now generated for flags.

- 

[PYSIDE-2544](https://qt-project.atlassian.net/browse//PYSIDE-2544)  A crash accessing QDBusVariant.variant() has been fixed.

- 

[PYSIDE-2547](https://qt-project.atlassian.net/browse//PYSIDE-2547)  A hang in QDBusConnection.connect() has been fixed.

- 

[PYSIDE-2558](https://qt-project.atlassian.net/browse//PYSIDE-2558)  Documentation: the differences between commercial and lts releases have been clarified.

- 

[PYSIDE-2568](https://qt-project.atlassian.net/browse//PYSIDE-2568)  A crash of pyside6-designer with pyenv on Unix has been fixed.

- 

[PYSIDE-2574](https://qt-project.atlassian.net/browse//PYSIDE-2574)  Documentation: A favicon for browser tabs has been added.

## 6.6.1[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id26)

- 

PySide6 examples are now also available as a separate wheel (PySide6_Examples).

- 

[PYSIDE-748](https://qt-project.atlassian.net/browse//PYSIDE-748)  An optional parameter “tag” has been added to @Slot, allowing to set QMetaMethod.tag().

- 

[PYSIDE-769](https://qt-project.atlassian.net/browse//PYSIDE-769)  QtAsyncio: Support for ThreadPoolExecutor has been added.

- 

[PYSIDE-841](https://qt-project.atlassian.net/browse//PYSIDE-841)  QtQuick3D procedural texture and QRhi window examples have been added.

- 

[PYSIDE-2230](https://qt-project.atlassian.net/browse//PYSIDE-2230)  Support for Python 3.12 has been added.

- 

[PYSIDE-2367](https://qt-project.atlassian.net/browse//PYSIDE-2367)  Threading deadlocks of QObject::(dis)connect() with (dis)connectNotify() have been fixed.

- 

[PYSIDE-2485](https://qt-project.atlassian.net/browse//PYSIDE-2485)  A QLocale-related crash on macOS has been fixed.

- 

[PYSIDE-2487](https://qt-project.atlassian.net/browse//PYSIDE-2487)  Error messages around signal/slot connections have been improved.

- 

[PYSIDE-2494](https://qt-project.atlassian.net/browse//PYSIDE-2494)  The install location of QtAsyncio for CMake builds has been fixed.

- 

[PYSIDE-2500](https://qt-project.atlassian.net/browse//PYSIDE-2500)  QMetaMethod.invoke() has been added. The invocation functions of QMetaObject now accept up to 10 arguments.

- 

[PYSIDE-2509](https://qt-project.atlassian.net/browse//PYSIDE-2509)  The signature of SignalInstance.connect() has been fixed.

- 

[PYSIDE-2510](https://qt-project.atlassian.net/browse//PYSIDE-2510)  An error is now set when instantiating a Signal on a non-QObject.

- 

[PYSIDE-2514](https://qt-project.atlassian.net/browse//PYSIDE-2514)  The type hints of QAbstractItemView.setModel()/QGraphicsView.setScene() now accept None.

- 

[QTBUG-113331] QRhi and related classes have been added.

## 6.6.0[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id27)

- 

The module QtGraphs has been added.

- 

[PYSIDE-769](https://qt-project.atlassian.net/browse//PYSIDE-769)  A custom asyncio event loop based on Qt has been implemented.

- 

[PYSIDE-1106](https://qt-project.atlassian.net/browse//PYSIDE-1106)  Documentation: The translation of code snippets from C++ to Python has been improved.

- 

[PYSIDE-1106](https://qt-project.atlassian.net/browse//PYSIDE-1106)  Documentation: The example gallery has been improved.

- 

[PYSIDE-1106](https://qt-project.atlassian.net/browse//PYSIDE-1106)  Documentation: Markdown is now also supported for example documentation.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Android: Unity build is now enabled by default. Qt Permissions API has been added for Android. Auto download of Android NDK and SDK now possible with Android wheel cross-compilation tool. Full support for Qt modules now available on Android. .js files are now supported when QML/Quick application deployed to Android.

- 

[PYSIDE-1735](https://qt-project.atlassian.net/browse//PYSIDE-1735)  The old enumerations have been removed.

- 

[PYSIDE-1884](https://qt-project.atlassian.net/browse//PYSIDE-1884)  The doc  attribute is now used for signatures when provided.

- 

[PYSIDE-2206](https://qt-project.atlassian.net/browse//PYSIDE-2206)  Example improvements: removed macpasteboardmime, tabbed browser and old statemachine examples; updated camera, chart theme, DOM bookmarks, Bluetooth heartrate game, Bluetooth lowenergyscanner, markdowneditor, mapviewer, mdi, QML reference examples, quicknanobrowser and scriptableapplication; added document viewer, filesystemexplorer, simplebrowser, statemachine moveblocks, screencapture, Qt Graphs widgetgallery and widgetsnanobrowser.

- 

[PYSIDE-2226](https://qt-project.atlassian.net/browse//PYSIDE-2226)  QLocale.toLong() has been fixed to properly return a tuple (int, bool) rather than only int.

- 

[PYSIDE-2235](https://qt-project.atlassian.net/browse//PYSIDE-2235)  Type hints: QObject.setParent() now accepts an Optional object.

- 

[PYSIDE-2272](https://qt-project.atlassian.net/browse//PYSIDE-2272)  Type hints: The signatures of the qmlRegister() functions have been fixed.

- 

[PYSIDE-2384](https://qt-project.atlassian.net/browse//PYSIDE-2384)  QWizardPage::registerField() taking a Signal instance has been added.

- 

[PYSIDE-2394](https://qt-project.atlassian.net/browse//PYSIDE-2394)  A deprecation warning about QSqlQueryModel::setQuery(const QSqlQuery &) originating from Qt / C++ has been removed.

- 

[PYSIDE-2395](https://qt-project.atlassian.net/browse//PYSIDE-2395)  The signatures of QClipboard.setPixmap() and setImage() have been fixed.

- 

[PYSIDE-2402](https://qt-project.atlassian.net/browse//PYSIDE-2402)  Modules QtDBus and QtHttpServer have been enabled on Windows.

- 

[PYSIDE-2415](https://qt-project.atlassian.net/browse//PYSIDE-2415)  QQmlComponent is now supported as a Property.

- 

[PYSIDE-2417](https://qt-project.atlassian.net/browse//PYSIDE-2417)  Overflows when passing int to functions taking floats have been fixed.

- 

[PYSIDE-2442](https://qt-project.atlassian.net/browse//PYSIDE-2442)  QDataStream.writeRawData() now also takes bytes.

- 

[PYSIDE-2471](https://qt-project.atlassian.net/browse//PYSIDE-2471)  The pyside6-project now also recognizes .pyw files as Python files on Windows.

- 

[PYSIDE-2473](https://qt-project.atlassian.net/browse//PYSIDE-2473)  Feature switching has been fixed to work with unittest.mock.patch.dict.

## 6.5.3[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id28)

- 

[PYSIDE-1884](https://qt-project.atlassian.net/browse//PYSIDE-1884)  The doc  attribute is now used for signatures when provided.

- 

[PYSIDE-2235](https://qt-project.atlassian.net/browse//PYSIDE-2235)  Type hints: setParent() now accepts an Optional object.

- 

[PYSIDE-2272](https://qt-project.atlassian.net/browse//PYSIDE-2272)  The signatures of the qmlRegister() functions have been fixed.

- 

[PYSIDE-2387](https://qt-project.atlassian.net/browse//PYSIDE-2387)  The signature of qVersion() has been fixed.

- 

[PYSIDE-2394](https://qt-project.atlassian.net/browse//PYSIDE-2394)  A deprecation warning for QSqlQueryModel.setQuery(QSqlQuery) has been removed.

- 

[PYSIDE-2395](https://qt-project.atlassian.net/browse//PYSIDE-2395)  The signatures for QClipboard.setPixmap() and QClipboard.setImage() have been fixed.

- 

[PYSIDE-2402](https://qt-project.atlassian.net/browse//PYSIDE-2402)  The modules QtDBus and QtHttpServer have been enabled on Windows.

- 

[PYSIDE-2411](https://qt-project.atlassian.net/browse//PYSIDE-2411)  The documentation for QPainter.drawText() has been fixed.

- 

[PYSIDE-2412](https://qt-project.atlassian.net/browse//PYSIDE-2412)  A bug removing rows in the Tetrix example has been fixed.

- 

[PYSIDE-2415](https://qt-project.atlassian.net/browse//PYSIDE-2415)  Support for QQmlComponent in Property has been added.

- 

[PYSIDE-2417](https://qt-project.atlassian.net/browse//PYSIDE-2417)  Overflows when passing int to functions taking floats have been fixed.

- 

[PYSIDE-2418](https://qt-project.atlassian.net/browse//PYSIDE-2418)  Connections to base class slots incorrectly falling back to the global receiver have been fixed.

- 

[PYSIDE-2425](https://qt-project.atlassian.net/browse//PYSIDE-2425)  Theme switching of the chart theme example has been fixed.

- 

[PYSIDE-2368](https://qt-project.atlassian.net/browse//PYSIDE-2368)  The signature of PySide6.QtCore.Signal has been fixed.

- 

[PYSIDE-2393](https://qt-project.atlassian.net/browse//PYSIDE-2393)  A recursion occurring with pytest-forked has been fixed.

- 

[PYSIDE-2419](https://qt-project.atlassian.net/browse//PYSIDE-2419)  QLocale::system() on macOS has been fixed.

- 

[PYSIDE-2422](https://qt-project.atlassian.net/browse//PYSIDE-2422)  A crash occurring when passing None to QGridLayout.removeItem() has been turned into a warning.

- 

[PYSIDE-2433](https://qt-project.atlassian.net/browse//PYSIDE-2433)  Crashes related to enums in QML singletons have been fixed.

- 

[PYSIDE-2444](https://qt-project.atlassian.net/browse//PYSIDE-2444)  Incorrect signatures in class QState have been fixed.

- 

[PYSIDE-2454](https://qt-project.atlassian.net/browse//PYSIDE-2454)  Default parameters for containers without indirections have been fixed.

- 

[PYSIDE-2461](https://qt-project.atlassian.net/browse//PYSIDE-2461)  Build system: The “modules” is now correctly resolved relative to archdata.

## 6.5.2[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id29)

- 

[PYSIDE-2184](https://qt-project.atlassian.net/browse//PYSIDE-2184)  .pyi files are now installed by CMake.

- 

[PYSIDE-2206](https://qt-project.atlassian.net/browse//PYSIDE-2206)  The QtStateMachine moveblocks example has been added.

- 

[PYSIDE-2206](https://qt-project.atlassian.net/browse//PYSIDE-2206)  The QtLocation mapviewer example has been revamped.

- 

[PYSIDE-2331](https://qt-project.atlassian.net/browse//PYSIDE-2331)  Type hints of several functions taking a str have been fixed.

- 

[PYSIDE-2339](https://qt-project.atlassian.net/browse//PYSIDE-2339)  Enumeration types are now kept when passed through the QVariant APIs of QAbstractItemModel, and a conversion to int takes place when required (Qt.CheckState and similar).

- 

[PYSIDE-2340](https://qt-project.atlassian.net/browse//PYSIDE-2340)  A crash when using QScxmlStateMachine::connectToEvent() has been fixed.

- 

[PYSIDE-2347](https://qt-project.atlassian.net/browse//PYSIDE-2347)  Output of QObject slots has been added to the metaobjectdump.py tool as an input of qmllint.

- 

[PYSIDE-2364](https://qt-project.atlassian.net/browse//PYSIDE-2364)  The type hint for QQmlExpression.evaluate() has been fixed.

- 

[PYSIDE-2299](https://qt-project.atlassian.net/browse//PYSIDE-2299)  A memory leak connecting free methods/lambdas has been

- 

[PYSIDE-2371](https://qt-project.atlassian.net/browse//PYSIDE-2371)  Fixed regression related to memory leak when connecting signal to local function.

- 

[PYSIDE-2381](https://qt-project.atlassian.net/browse//PYSIDE-2381)  Fixed issue qith QSetting list of strings and value()

- 

[PYSIDE-2384](https://qt-project.atlassian.net/browse//PYSIDE-2384)  Fixed QWizardPage.registerField signature

## 6.5.1[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id30)

- 

pyside6-qmlcachegen has been added.

- 

The qmllint target of pyside6-project has been fixed to work on Windows.

- 

[PYSIDE-1106](https://qt-project.atlassian.net/browse//PYSIDE-1106)  The example documentation has been improved.

- 

[PYSIDE-2206](https://qt-project.atlassian.net/browse//PYSIDE-2206)  Many examples and tutorials have been revamped.

- 

[PYSIDE-2278](https://qt-project.atlassian.net/browse//PYSIDE-2278)  Type hints: Checks for None with pyright have been fixed.

- 

[PYSIDE-2283](https://qt-project.atlassian.net/browse//PYSIDE-2283)  Qt platform dependencies have been linked to the documentation.

- 

[PYSIDE-2284](https://qt-project.atlassian.net/browse//PYSIDE-2284)  Type hints: The missing NoneType import has been added.

- 

[PYSIDE-2285](https://qt-project.atlassian.net/browse//PYSIDE-2285)  Type hints for return values modified to Tuple[] have been added.

- 

[PYSIDE-2289](https://qt-project.atlassian.net/browse//PYSIDE-2289)  opengl32sw.dll is now again shipped.

- 

[PYSIDE-2293](https://qt-project.atlassian.net/browse//PYSIDE-2293)  The deployment tool has been fixed to keep structure of QML files.

- 

[PYSIDE-2294](https://qt-project.atlassian.net/browse//PYSIDE-2294)  A regression bug in handling multiple inheritance has been fixed.

- 

[PYSIDE-2298](https://qt-project.atlassian.net/browse//PYSIDE-2298)  QTimeZone::Initialization has been added.

- 

[PYSIDE-2299](https://qt-project.atlassian.net/browse//PYSIDE-2299)  A leak connecting signals to anonymous functions has been fixed.

- 

[PYSIDE-2300](https://qt-project.atlassian.net/browse//PYSIDE-2300)  QSqlQueryModel::query() has been re-added.

- 

[PYSIDE-2302](https://qt-project.atlassian.net/browse//PYSIDE-2302)  A bug blocking the UI when loading images from a thread has been fixed.

- 

[PYSIDE-2310](https://qt-project.atlassian.net/browse//PYSIDE-2310)  The delayed reporting of exceptions in reimplemented

- 

[PYSIDE-2321](https://qt-project.atlassian.net/browse//PYSIDE-2321)  virtual functions introduced in 6.4.3 has been reverted to the original state.

- 

[PYSIDE-2318](https://qt-project.atlassian.net/browse//PYSIDE-2318)  Type hints: Signatures for QDBusAbstractInterfaceBase functions have been fixed.

- 

[PYSIDE-2325](https://qt-project.atlassian.net/browse//PYSIDE-2325)  Missing OpenGL type system files have been added.

- 

[PYSIDE-2328](https://qt-project.atlassian.net/browse//PYSIDE-2328)  A crash when connecting to temporary signal sources has been fixed.

- 

[PYSIDE-2329](https://qt-project.atlassian.net/browse//PYSIDE-2329)  Signals with parameters can now be connected by passing keyword arguments to constructor.

- 

[PYSIDE-2334](https://qt-project.atlassian.net/browse//PYSIDE-2334)  Some missing libraries (QtPdfQuick/QtQuickEffects) have been added.

- 

[QTBUG-112708] Building with QT_FEATURE_opengles2 has been fixed.

## 6.5.0[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id31)

- 

pyside6-project can now generate simple project templates.

- 

QtSerialBus has been added.

- 

Class QHashSeed has been added.

- 

[PYSIDE-510](https://qt-project.atlassian.net/browse//PYSIDE-510)  The non-standard signature  attribute of functions and classes has been removed in favor of get_signature().

- 

[PYSIDE-1019](https://qt-project.atlassian.net/browse//PYSIDE-1019)  A callback error when using true_property has been fixed.

- 

[PYSIDE-1713](https://qt-project.atlassian.net/browse//PYSIDE-1713)  A `signatures` attribute has been added to the Signal type in order to increase compatibility with other implementations.

- 

[PYSIDE-2029](https://qt-project.atlassian.net/browse//PYSIDE-2029) feature  switching now works even with recursive imports like in the qasync module. In addition, a new efficient optimization has been implemented for feature  switching. Initial work towards PyPy support for feature  switching has been done.

- 

[PYSIDE-2101](https://qt-project.atlassian.net/browse//PYSIDE-2101)  Python 3.10 and up have an incompatibility to the signature  attribute. This is fixed by a temporary patch until the final removal of that attribute.

- 

[PYSIDE-753](https://qt-project.atlassian.net/browse//PYSIDE-753)  The shared pointer types of Qt 3D have been added.

- 

[PYSIDE-769](https://qt-project.atlassian.net/browse//PYSIDE-769)  asyncio versions of the async examples have been added.

- 

[PYSIDE-841](https://qt-project.atlassian.net/browse//PYSIDE-841)  Examples networkx graph viewer, can bus, modbus client, charts lightMarker and selection, charts selected point configuration, graphgallery, qmlsurfacegallery, map view (QtLocation) and and Qt Quick custom geometry have been added.

- 

[PYSIDE-971](https://qt-project.atlassian.net/browse//PYSIDE-971)  QOpenGLContext.getProcAddress() has been added.

- 

[PYSIDE-1019](https://qt-project.atlassian.net/browse//PYSIDE-1019)  libpyside: The function `getMetaDataFromQObject` has been removed.

- 

[PYSIDE-1106](https://qt-project.atlassian.net/browse//PYSIDE-1106)  The documentation code snippet conversion has been improved.

- 

[PYSIDE-1295](https://qt-project.atlassian.net/browse//PYSIDE-1295)  QObject::sender() has been implemented for non-C++ slots.

- 

[PYSIDE-1345](https://qt-project.atlassian.net/browse//PYSIDE-1345)  QSGGeometry.vertexDataAsPoint2D()/setVertexDataAsPoint2D() has been added.

- 

[PYSIDE-1564](https://qt-project.atlassian.net/browse//PYSIDE-1564)  Cooperative multiple inheritance is now implemented for all init  methods.

- 

[PYSIDE-1603](https://qt-project.atlassian.net/browse//PYSIDE-1603)  Signals are now listed in the typing hints.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  Initial support for Android Deployment has been added.

- 

[PYSIDE-1713](https://qt-project.atlassian.net/browse//PYSIDE-1713)  Compatibility of Qt signals has been improved by providing a signatures attribute.

- 

[PYSIDE-1735](https://qt-project.atlassian.net/browse//PYSIDE-1735)  Documentation: enum types are now indicated.

- 

[PYSIDE-2079](https://qt-project.atlassian.net/browse//PYSIDE-2079)  setuptools are now used instead of distutils.

- 

[PYSIDE-2098](https://qt-project.atlassian.net/browse//PYSIDE-2098)  dicts can now be passed as QVariantMap to QML.

- 

[PYSIDE-2136](https://qt-project.atlassian.net/browse//PYSIDE-2136)  An error calling deprecated functions with warning-as-error set has been fixed.

- 

[PYSIDE-2141](https://qt-project.atlassian.net/browse//PYSIDE-2141)  A crash when deleting QObject instances with connections in threads has been fixed.

- 

[PYSIDE-2155](https://qt-project.atlassian.net/browse//PYSIDE-2155)  CMake UNITY_BUILD (jumbo) builds are now supported, speeding up building. Pass –unity to setup.py.

- 

[PYSIDE-2160](https://qt-project.atlassian.net/browse//PYSIDE-2160)  The formatting of delayed errors in Python 3.11 has been improved.

- 

[PYSIDE-2221](https://qt-project.atlassian.net/browse//PYSIDE-2221)  First changes for NoGIL support have been added.

- 

[PYSIDE-2206](https://qt-project.atlassian.net/browse//PYSIDE-2206)  Some examples have been updated.

- 

[PYSIDE-2230](https://qt-project.atlassian.net/browse//PYSIDE-2230)  First changes for Python 3.12 have been added.

- 

[PYSIDE-2234](https://qt-project.atlassian.net/browse//PYSIDE-2234)  QRunnable.create() has been added.

- 

[PYSIDE-2236](https://qt-project.atlassian.net/browse//PYSIDE-2236)  QMetaMethod.fromSignal() has been added.

- 

[PYSIDE-2247](https://qt-project.atlassian.net/browse//PYSIDE-2247)  Examples are not included in the wheels any more and the setup.py option –no-example was removed. Examples can now be downloaded as .zip files from the documentation.

- 

[PYSIDE-2251](https://qt-project.atlassian.net/browse//PYSIDE-2251)  Qt Designer Python plugins now work with non- activated virtual environments.

- 

[PYSIDE-2259](https://qt-project.atlassian.net/browse//PYSIDE-2259)  QtTextToSpeech has been added.

- 

[PYSIDE-2252](https://qt-project.atlassian.net/browse//PYSIDE-2252)  QAbstractTextDocumentLayout::PaintContext has been added.

- 

[PYSIDE-2169](https://qt-project.atlassian.net/browse//PYSIDE-2169)  A leak in Enum forgiveness mode has been fixed.

- 

[PYSIDE-2260](https://qt-project.atlassian.net/browse//PYSIDE-2260)  A QML deployment issue with Nuitka has been fixed.

## 6.4.3[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id32)

- 

A requirements file for documentation builds (requirements-doc.txt) has been added.

- 

A workaround has been implemented for Qt version conflicts when installing PySide6 in an Anaconda environment.

- 

[PYSIDE-0079](https://qt-project.atlassian.net/browse//PYSIDE-0079)  signals: An old refcounting error has been fixed which was introduced by the PYSIDE-68 fix.

- 

[PYSIDE-1014](https://qt-project.atlassian.net/browse//PYSIDE-1014)  Sorting overriding QStandardItem::operator<() has been enabled.

- 

[PYSIDE-1402](https://qt-project.atlassian.net/browse//PYSIDE-1402)  QtCore.Property: An old refcounting error has been fixed.

- 

[PYSIDE-1931](https://qt-project.atlassian.net/browse//PYSIDE-1931)  A hang in QSqlQueryModel.setQuery() (PostGres with SSH tunnel) has been fixed.

- 

[PYSIDE-2168](https://qt-project.atlassian.net/browse//PYSIDE-2168)  QLocale.toString() has been fixed to handle negative values correctly.

- 

[PYSIDE-2169](https://qt-project.atlassian.net/browse//PYSIDE-2169)  Fixed a leak in the Python enum “forgiveness mode”.

- 

[PYSIDE-2189](https://qt-project.atlassian.net/browse//PYSIDE-2189)  feature switching: _mod_uses_pyside has been made safe against binary modules.

- 

[PYSIDE-2197](https://qt-project.atlassian.net/browse//PYSIDE-2197)  Signals are now generated into pyi files as attributes.

- 

[PYSIDE-2199](https://qt-project.atlassian.net/browse//PYSIDE-2199)  The –binary option of pyside6-rcc has been fixed.

- 

[PYSIDE-2201](https://qt-project.atlassian.net/browse//PYSIDE-2201)  Crashes caused by temporary instances of signals have been fixed by introducing a weak reference.

- 

[PYSIDE-2202](https://qt-project.atlassian.net/browse//PYSIDE-2202)  pyside6-metaobjectdump: Parse failures caused by call operators in base class specifications have been fixed.

- 

[PYSIDE-2203](https://qt-project.atlassian.net/browse//PYSIDE-2203)  pyside6-metaobjectdump: Parse failures caused by complex function decorators have been fixed.

- 

[PYSIDE-2204](https://qt-project.atlassian.net/browse//PYSIDE-2204)  The encoding of hte prefix path in the embedded :/qt/etc/qt.conf resource has been fixed to be UTF-8.

- 

[PYSIDE-2222](https://qt-project.atlassian.net/browse//PYSIDE-2222)  An exit crash when loading Python custom widget plugins by QUiLoader has been fixed.

- 

[PYSIDE-2229](https://qt-project.atlassian.net/browse//PYSIDE-2229)  Fixed an error when building commercial wheels from source.

- 

[PYSIDE-2237](https://qt-project.atlassian.net/browse//PYSIDE-2237)  Fields named “from” are now exposed as “from_” to avoid using the reserved word (occurs in “QtGui.QPageRanges.Range.from”).

- 

[PYSIDE-2239](https://qt-project.atlassian.net/browse//PYSIDE-2239)  Opaque containers now have correct module  names.

## 6.4.2[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id33)

- 

[PYSIDE-769](https://qt-project.atlassian.net/browse//PYSIDE-769)  asyncio versions of the async examples have been added.

- 

[PYSIDE-1019](https://qt-project.atlassian.net/browse//PYSIDE-1019)  A callback error when using true_property has been fixed.

- 

[PYSIDE-1106](https://qt-project.atlassian.net/browse//PYSIDE-1106)  Documentation: The automatic code snippet conversion has been improved.

- 

[PYSIDE-1889](https://qt-project.atlassian.net/browse//PYSIDE-1889) feature : A weird case of false metafunction lookup has been fixed.

- 

[PYSIDE-2029](https://qt-project.atlassian.net/browse//PYSIDE-2029) feature  switching now works even with recursive imports like in the qasync module. It also has been optimized and simplified in preparation for eventual PyPy support.

- 

[PYSIDE-2042](https://qt-project.atlassian.net/browse//PYSIDE-2042)  true_property was fixed to work with inherited properties as well.

- 

[PYSIDE-2128](https://qt-project.atlassian.net/browse//PYSIDE-2128)  An issue affecting CMake-only builds has been fixed.

- 

[PYSIDE-2133](https://qt-project.atlassian.net/browse//PYSIDE-2133)  The float type overload of QLocale.toCurrencyString() has been fixed.

- 

[PYSIDE-2136](https://qt-project.atlassian.net/browse//PYSIDE-2136)  Errors when calling deprecated functions with warning-as-error set have been fixed.

## 6.4.1[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id34)

- 

A context manager for QOpenGLVertexArrayObject.Binder has been added.

- 

[PYSIDE-1970](https://qt-project.atlassian.net/browse//PYSIDE-1970)  The long missing support for slots  was finally added.

- 

[PYSIDE-841](https://qt-project.atlassian.net/browse//PYSIDE-841)  networkx graph viewer, charts lightMarker and selection examples have been added.

- 

[PYSIDE-1106](https://qt-project.atlassian.net/browse//PYSIDE-1106)  Documentation builds have been fixed to work with system-installed versions of Qt 6.

- 

[PYSIDE-1603](https://qt-project.atlassian.net/browse//PYSIDE-1603)  A bug when passing wrong keyword args to signals has been fixed.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  The missing entry point for pyside6-qtpy2cpp has been added.

- 

[PYSIDE-1713](https://qt-project.atlassian.net/browse//PYSIDE-1713)  A `signatures` attribute has been added to the Signal type in order to increase compatibility with other implementations.

- 

[PYSIDE-1735](https://qt-project.atlassian.net/browse//PYSIDE-1735)  Developer documentation about enum features has been added.

- 

[PYSIDE-1735](https://qt-project.atlassian.net/browse//PYSIDE-1735)  Some enums have been changed to be IntEnum-based.

- 

[PYSIDE-1844](https://qt-project.atlassian.net/browse//PYSIDE-1844)  Build system: It is no longer required to have Qt in PATH (tough recommended).

- 

[PYSIDE-1957](https://qt-project.atlassian.net/browse//PYSIDE-1957)  The missing Qt5Compat.GraphicalEffects has been added to the wheel.

- 

[PYSIDE-2074](https://qt-project.atlassian.net/browse//PYSIDE-2074)  Build system: Overriding of PYTHON_SITE_PACKAGES has been enabled.

- 

[PYSIDE-2081](https://qt-project.atlassian.net/browse//PYSIDE-2081)  Type annotations for the static functions of QInputDialog have been fixed.

- 

[PYSIDE-2084](https://qt-project.atlassian.net/browse//PYSIDE-2084)  The build with OpenGLES has been fixed.

- 

[PYSIDE-2087](https://qt-project.atlassian.net/browse//PYSIDE-2087)  It is now possible to build QtUiTools without Qt Designer.

- 

[PYSIDE-2089](https://qt-project.atlassian.net/browse//PYSIDE-2089)  Crashes when not implementing abstract methods have been fixed.

- 

[PYSIDE-2091](https://qt-project.atlassian.net/browse//PYSIDE-2091)  Build system: The check for FORCE_LIMITED_API has been fixed.

- 

[PYSIDE-2091](https://qt-project.atlassian.net/browse//PYSIDE-2091)  Build system: The minimum required CMake version has been bumped to CMake 3.18+ (matching Qt).

- 

[PYSIDE-2095](https://qt-project.atlassian.net/browse//PYSIDE-2095)  A bug when using signals with new enums on Python 3.11 has been fixed.

- 

[PYSIDE-2101](https://qt-project.atlassian.net/browse//PYSIDE-2101)  Python 3.10 and higher are not compatible to the signature  attribute. This has been fixed by a temporary patch until the final removal of that attribute.

- 

[PYSIDE-2106](https://qt-project.atlassian.net/browse//PYSIDE-2106)  A bug resulting in duplication of values in QML properties of type QVariantList has been fixed.

- 

[PYSIDE-2121](https://qt-project.atlassian.net/browse//PYSIDE-2121)  A deadlock when using QMetaObject.invokeMethod(BlockingQueuedConnection) has been fixed.

## 6.4.0[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id35)

- 

Modules QtPdf, QtPdfWidgets and QtSpatialAudio have been added.

- 

[PYSIDE-353](https://qt-project.atlassian.net/browse//PYSIDE-353)  PySide builds with PyPy 3.9.

- 

[PYSIDE-769](https://qt-project.atlassian.net/browse//PYSIDE-769)  Examples that demonstrate usage of Trio async package with Qt have been added.

- 

[PYSIDE-841](https://qt-project.atlassian.net/browse//PYSIDE-841)  Examples surface_numpy, minimal surface (QtDataVisualization), dropsite, dirview, Google suggest license wizard, QtBluetooth heart rate server and client, QML window, QML Plugins, analog clock (QtGui), digital clock (QtWidgets), spreadsheet, terminal (QtSerialPort) and character map, have been added.

- 

[PYSIDE-962](https://qt-project.atlassian.net/browse//PYSIDE-962)  Errors message about test-configuring projects with cmake have been improved.

- 

[PYSIDE-1019](https://qt-project.atlassian.net/browse//PYSIDE-1019)  The feature module has been improved by a reset function.

- 

[PYSIDE-1106](https://qt-project.atlassian.net/browse//PYSIDE-1106)  The documentation build process has been improved; it no longer requires a complete PySide6 build.

- 

[PYSIDE-1312](https://qt-project.atlassian.net/browse//PYSIDE-1312)  Support for QFormLayout::TakeRowResult has been added.

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  A tool for deployment, pyside6-deploy, has been added.

- 

[PYSIDE-1721](https://qt-project.atlassian.net/browse//PYSIDE-1721)  The C++ to Python code snippet translation has been much improved.

- 

[PYSIDE-1731](https://qt-project.atlassian.net/browse//PYSIDE-1731)  PyEnum: Fix the old Enums to produce correct .pyi files, again.

- 

[PYSIDE-1735](https://qt-project.atlassian.net/browse//PYSIDE-1735)  The new forgiveness mode of Python enums allows to use old enum code, most of the time.

- 

[PYSIDE-1735](https://qt-project.atlassian.net/browse//PYSIDE-1735)  PyEnum: Most IntEnum/IntFlag classes were modified to Enum/Flag

- 

[PYSIDE-1735](https://qt-project.atlassian.net/browse//PYSIDE-1735)  PyEnum: QKeyCombination was improved to also work after the change from IntEnum to Enum.

- 

[PYSIDE-1735](https://qt-project.atlassian.net/browse//PYSIDE-1735)  PyEnum can now be fully configured by flags at startup for internal use. The default is unchanged and enables everything as before.

- 

[PYSIDE-1797](https://qt-project.atlassian.net/browse//PYSIDE-1797)  Link errors about PyIndex_Check() when using Limited_API have been fixed.

- 

[PYSIDE-1860](https://qt-project.atlassian.net/browse//PYSIDE-1860)  Modules are now optimized for size.

- 

[PYSIDE-1878](https://qt-project.atlassian.net/browse//PYSIDE-1878)  The tool pyside6-qml has been added.

- 

[PYSIDE-1880](https://qt-project.atlassian.net/browse//PYSIDE-1880)  A numpy overload for QSurfaceDataProxy.resetArray() has been added.

- 

[PYSIDE-1883](https://qt-project.atlassian.net/browse//PYSIDE-1883)  Test::qWait()/qSleep() have been added.

- 

[PYSIDE-1887](https://qt-project.atlassian.net/browse//PYSIDE-1887)  Overriding QGraphicsItem::itemChange() has been fixed.

- 

[PYSIDE-1887](https://qt-project.atlassian.net/browse//PYSIDE-1887)  Specify meta type registration for some class hierarchies

- 

[PYSIDE-1893](https://qt-project.atlassian.net/browse//PYSIDE-1893)  Error “Internal C++ object already deleted.” when using QWidget.nativeParentWidget() has been fixed.

- 

[PYSIDE-1895](https://qt-project.atlassian.net/browse//PYSIDE-1895)  ‘\0’ can now be embedded in 1 byte strings.

- 

[PYSIDE-1898](https://qt-project.atlassian.net/browse//PYSIDE-1898)  Q_ARG/Q_RETURN_ARG have been implemented for QMetaObject.invokeMethod() with arguments.

- 

[PYSIDE-1898](https://qt-project.atlassian.net/browse//PYSIDE-1898)  qMetaTypeFromPyType() has been fixed for for wrapped types.

- 

[PYSIDE-1898](https://qt-project.atlassian.net/browse//PYSIDE-1898)  QMetaType: a constructor taking a PyTypeObject has been added.

- 

[PYSIDE-1899](https://qt-project.atlassian.net/browse//PYSIDE-1899)  Class QLoggingCategory and functions qCDebug(), qCInfo(), qCWarning() and qCCritical() has been added.

- 

[PYSIDE-1859](https://qt-project.atlassian.net/browse//PYSIDE-1859)  The Microsoft Windows handle types HBITMAP, HICON and HRGN have been added.

- 

[PYSIDE-1906](https://qt-project.atlassian.net/browse//PYSIDE-1906)  All qHash() functions are now exposed to Python.

- 

[PYSIDE-1913](https://qt-project.atlassian.net/browse//PYSIDE-1913)  The bool cast for QByteArray has been changed to return False for empty byte arrays to match the expected behavior.

- 

[PYSIDE-1924](https://qt-project.atlassian.net/browse//PYSIDE-1924)  Numpy support is now enabled by default.

- 

[PYSIDE-1945](https://qt-project.atlassian.net/browse//PYSIDE-1945)  pyside6-qtpy2cpp.py, a Qt-specific, simple tool for converting Python code to C++ has been added.

- 

[PYSIDE-1957](https://qt-project.atlassian.net/browse//PYSIDE-1957)  The Qt5Compat QML imports have been added (QtGraphicalEffects).

- 

[PYSIDE-1901](https://qt-project.atlassian.net/browse//PYSIDE-1901)  The broken string conversion for non-compact strings when using Limited API has been fixed.

- 

[PYSIDE-1905](https://qt-project.atlassian.net/browse//PYSIDE-1905)  Overloads with more parameters have been added to QDBusAbstractInterface::call().

- 

[PYSIDE-1906](https://qt-project.atlassian.net/browse//PYSIDE-1906)  qHash() functions are now automatically exposed as tp_hash.

- 

[PYSIDE-1909](https://qt-project.atlassian.net/browse//PYSIDE-1909)  Type discovery for QStyleOption-derived classes has been fixed.

- 

[PYSIDE-1911](https://qt-project.atlassian.net/browse//PYSIDE-1911)  A repr  function for PySideSignalInstance has been added.

- 

[PYSIDE-1912](https://qt-project.atlassian.net/browse//PYSIDE-1912)  QWebEngineCookieStore.setCookieFilter() and QtWebEngineProfile.setNotificationPresenter() have been added.

- 

[PYSIDE-1919](https://qt-project.atlassian.net/browse//PYSIDE-1919)  A GIL state crash when collecting QObjects with signals occurring in Python 3.10 has been fixed.

- 

[PYSIDE-1921](https://qt-project.atlassian.net/browse//PYSIDE-1921)  QQmlContext.setContextProperties() has been added.

- 

[PYSIDE-1930](https://qt-project.atlassian.net/browse//PYSIDE-1930)  Returning enums from QAbstractListModel.data() has been fixed.

- 

[PYSIDE-1934](https://qt-project.atlassian.net/browse//PYSIDE-1934)  Type hinting for QListWidget.selected_indexes() has been fixed.

- 

[PYSIDE-1939](https://qt-project.atlassian.net/browse//PYSIDE-1939)  A crash in QTextBlock.layout() has been fixed.

- 

[PYSIDE-1947](https://qt-project.atlassian.net/browse//PYSIDE-1947)  QAudioBuffer.data()/constData() has been added.

- 

[PYSIDE-1957](https://qt-project.atlassian.net/browse//PYSIDE-1957)  Add Qt5Compat.GraphicalEffects

- 

[PYSIDE-1960](https://qt-project.atlassian.net/browse//PYSIDE-1960)  Support for Python 3.11 has been added.

- 

[PYSIDE-1968](https://qt-project.atlassian.net/browse//PYSIDE-1968)  Type hinting for QPixmap.save() has been fixed.

- 

[PYSIDE-1974](https://qt-project.atlassian.net/browse//PYSIDE-1974)  Returning flags from QAbstractTableModel and other models has been fixed.

- 

[PYSIDE-1978](https://qt-project.atlassian.net/browse//PYSIDE-1978)  Signal QAbstractItemModel::layoutAboutToBeChanged(QList ) has been fixed.

- 

[PYSIDE-1984](https://qt-project.atlassian.net/browse//PYSIDE-1984)  The snippets of the model view tutorials have been fixed.

- 

[PYSIDE-1986](https://qt-project.atlassian.net/browse//PYSIDE-1986)  Setting properties by named arguments for Q[VH]BoxLayout has been fixed.

- 

[PYSIDE-2000](https://qt-project.atlassian.net/browse//PYSIDE-2000)  The VS Code debugging tutorial for Windows has been updated.

- 

[PYSIDE-2004](https://qt-project.atlassian.net/browse//PYSIDE-2004)  The tools qmlformat and qmlls have been added.

- 

[PYSIDE-2005](https://qt-project.atlassian.net/browse//PYSIDE-2005)  A documentation section for cmake-only build has been added.

- 

[PYSIDE-2017](https://qt-project.atlassian.net/browse//PYSIDE-2017)  The functions glGet(Boolean|Double|Float|Integer)v() and glGet(Boolean|Double|Float|Integer)i_v() have been added.

- 

[PYSIDE-2019](https://qt-project.atlassian.net/browse//PYSIDE-2019)  Issues with QtDataVisualization’s QValue3DAxisFormatter have been fixed.

- 

[PYSIDE-2021](https://qt-project.atlassian.net/browse//PYSIDE-2021)  The index operator of QKeySequence now returns QKeyCombination when the new PyEnums are used.

- 

[PYSIDE-2025](https://qt-project.atlassian.net/browse//PYSIDE-2025)  Setters for the the lists in QtDataVisualization’s QValue3DAxisFormatter have been fixed added.

- 

[PYSIDE-2033](https://qt-project.atlassian.net/browse//PYSIDE-2033)  A logging category “qt.pyside.libpyside” with useful warnings has been added to libpyside.

- 

[PYSIDE-2034](https://qt-project.atlassian.net/browse//PYSIDE-2034)  Blocking threads in static functions of QMessageBox have been fixed.

- 

[PYSIDE-2038](https://qt-project.atlassian.net/browse//PYSIDE-2038)  Documentation: Improve module pages title

- 

[PYSIDE-2039](https://qt-project.atlassian.net/browse//PYSIDE-2039)  A regression bug when setting override cursors without context manager has been fixed.

- 

[PYSIDE-2048](https://qt-project.atlassian.net/browse//PYSIDE-2048)  A TypeError when comparing Qt.Flags and objects has been fixed.

- 

[PYSIDE-2059](https://qt-project.atlassian.net/browse//PYSIDE-2059)  Function qt_set_sequence_auto_mnemonic() has been added to QtGui.

- 

[PYSIDE-2060](https://qt-project.atlassian.net/browse//PYSIDE-2060)  Cross-compilation to Raspberry Pi 4 has been fixed.

## 6.4.0[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id36)

- 

[PYSIDE-1106](https://qt-project.atlassian.net/browse//PYSIDE-1106)  Fix modules being omitted from the documentation

- 

[PYSIDE-1612](https://qt-project.atlassian.net/browse//PYSIDE-1612)  wheels: Add pyside6-qtpy2cpp entry point

- 

[PYSIDE-1912](https://qt-project.atlassian.net/browse//PYSIDE-1912)  Deploy Tool : refactoring

- 

[PYSIDE-1957](https://qt-project.atlassian.net/browse//PYSIDE-1957)  Include Qt5Compat.GraphicalEffects QML files

- 

[PYSIDE-2063](https://qt-project.atlassian.net/browse//PYSIDE-2063)  PyEnum: Drop the Embedding of the Enum Module

- 

[PYSIDE-2081](https://qt-project.atlassian.net/browse//PYSIDE-2081)  Fix type annotations for static functions of QInputDialog

- 

[PYSIDE-2084](https://qt-project.atlassian.net/browse//PYSIDE-2084)  Fix build with OpenGLES

- 

[PYSIDE-2085](https://qt-project.atlassian.net/browse//PYSIDE-2085)  Remove mentions to Python 3.6

- 

[PYSIDE-2086](https://qt-project.atlassian.net/browse//PYSIDE-2086)  Make wheels compatible with Python 3.11

## 6.3.2[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id37)

- 

[PYSIDE-841](https://qt-project.atlassian.net/browse//PYSIDE-841)  New examples have been added (SpinBoxDelegate, Bluetooth heart rate).

- 

[PYSIDE-1312](https://qt-project.atlassian.net/browse//PYSIDE-1312)  QFormLayout::takeRow() has been added.

- 

[PYSIDE-1735](https://qt-project.atlassian.net/browse//PYSIDE-1735)  The duplication of enum values into the enclosing scope, allowing to write Qt.AlignLeft instead of Qt.Alignment.AlignLeft, is now implemented differently and no longer advertized in PYI files or line completion.

- 

[PYSIDE-1735](https://qt-project.atlassian.net/browse//PYSIDE-1735)  The new Python enums are made as compatible to the old ones as possible. It is again allowed to use Qt.Alignment() instead of Qt.AlignmentFlag(0), and a default of 0 is always allowed but also not advertized. Qt.Modifiers/Qt.KeyboardModifierflags can also still be used interchangeably.

- 

[PYSIDE-1735](https://qt-project.atlassian.net/browse//PYSIDE-1735)  Most former IntEnum/IntFlag are replaced by pure Enum/Flag classes in a generally compatible way to other implementations.

- 

[PYSIDE-1735](https://qt-project.atlassian.net/browse//PYSIDE-1735)  PyEnum handles QKeyCombination correctly with “|” or (deprecated) “+” operators, without falling back to using IntEnum.

- 

[PYSIDE-1735](https://qt-project.atlassian.net/browse//PYSIDE-1735)  Python Enums use the newest implementation for Python (3.10) for compatibility and speed.

- 

[PYSIDE-1735](https://qt-project.atlassian.net/browse//PYSIDE-1735)  A weird build problem on macOS and other platforms was fixed.

- 

[PYSide-1735] The cleanup calls by were sped up by using PyName for staticMetaObject.

- 

[PYSIDE-1984](https://qt-project.atlassian.net/browse//PYSIDE-1984)  The code snippets in the modelview tutorial have been improved.

- 

[PYSIDE-1930](https://qt-project.atlassian.net/browse//PYSIDE-1930)  Returning enums from QAbstractItemModel.flags() and QAbstractItemModel.data() has been fixed.

- 

[PYSIDE-1934](https://qt-project.atlassian.net/browse//PYSIDE-1934)  The type hinting for the return value of QListWidget.selected_indexes() has been fixed.

- 

[PYSIDE-1960](https://qt-project.atlassian.net/browse//PYSIDE-1960)  Initial support for Python 3.11 has been added.

- 

[PYSIDE-1968](https://qt-project.atlassian.net/browse//PYSIDE-1968)  The signature of QPixmap.save() has been fixed.

- 

[PYSIDE-1978](https://qt-project.atlassian.net/browse//PYSIDE-1978)  The signal QAbstractItemModel.layoutAboutToBeChanged(QList ) has been fixed. Also, the error message about using the wrong signal overload has been improved.

- 

[PYSIDE-2030](https://qt-project.atlassian.net/browse//PYSIDE-2030)  The converter tools for Python code snippets for the documentation has been improved.

- 

[PYSIDE-2019](https://qt-project.atlassian.net/browse//PYSIDE-2019)  Crashes related to QtDataVisualization’QValue3DAxisFormatter have been fixed.

- 

[PYSIDE-2034](https://qt-project.atlassian.net/browse//PYSIDE-2034)  The static functions of QMessageBox have been fixed to not block threads.

- 

[PYSIDE-2039](https://qt-project.atlassian.net/browse//PYSIDE-2039)  A regression affecting setting override cursors without context manager has been fixed.

## 6.3.1[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id38)

- 

[PYSIDE-1019](https://qt-project.atlassian.net/browse//PYSIDE-1019)  Feature switching was improved by avoiding cross-talk to enable for example tests using PyTest.

- 

[PYSIDE-353](https://qt-project.atlassian.net/browse//PYSIDE-353)  PySide now builds with PyPy 3.9.

- 

[PYSIDE-1735](https://qt-project.atlassian.net/browse//PYSIDE-1735)  New Pythons Enums were added as an optional feature, which can be activated bv setting the environment variable PYSIDE63_OPTION_PYTHON_ENUM.

- 

[PYSIDE-1797](https://qt-project.atlassian.net/browse//PYSIDE-1797)  An issue preventing using PySide with Python 3.6 or 3.7 related to symbol PyIndex_Check was fixed.

- 

[PYSIDE-1859](https://qt-project.atlassian.net/browse//PYSIDE-1859)  Windows handle types HBITMAP, HICON, HRGN are now supported (as int types).

- 

[PYSIDE-1880](https://qt-project.atlassian.net/browse//PYSIDE-1880)  The QtDataVisualization surface examples have been extended and improved.

- 

[PYSIDE-1883](https://qt-project.atlassian.net/browse//PYSIDE-1883)  QTest.qWait() and QTest.qSleep() have been added.

- 

[PYSIDE-1887](https://qt-project.atlassian.net/browse//PYSIDE-1887)  Overriding QGraphicsItem::itemChange() has been fixed.

- 

[PYSIDE-1893](https://qt-project.atlassian.net/browse//PYSIDE-1893)  A crash with error “Internal C++ object already deleted.” when using QWidget.nativeParentWidget() has been fixed.

- 

[PYSIDE-1895](https://qt-project.atlassian.net/browse//PYSIDE-1895)  Embedded 0 characters in UNICODE strings are now handled correctly.

- 

[PYSIDE-1899](https://qt-project.atlassian.net/browse//PYSIDE-1899)  QLoggingCategory, qCDebug, qCInfo, qCWarning and qCCritical have been added.

- 

[PYSIDE-1901](https://qt-project.atlassian.net/browse//PYSIDE-1901)  String conversion for non-compact strings when using Limited API has been fixed.

- 

[PYSIDE-1905](https://qt-project.atlassian.net/browse//PYSIDE-1905)  Overloads with more parameters have been added to QDBusAbstractInterface.call()

- 

[PYSIDE-1909](https://qt-project.atlassian.net/browse//PYSIDE-1909)  qstyleoption_cast<> has been implemented in order to be able to handle QStyleOption-derived classes.

- 

[PYSIDE-1911](https://qt-project.atlassian.net/browse//PYSIDE-1911)  PySideSignalInstance has now a repr .

- 

[PYSIDE-1912](https://qt-project.atlassian.net/browse//PYSIDE-1912)  QWebEngineCookieStore.setCookieFilter and QtWebEngineProfile.setNotificationPresenter have been added.

- 

[PYSIDE-1919](https://qt-project.atlassian.net/browse//PYSIDE-1919)  A GIL state crash when collecting QObjects with signals in Python 3.10 has been fixed.

- 

[PYSIDE-1921](https://qt-project.atlassian.net/browse//PYSIDE-1921)  QQmlContext::setContextProperties() has been added.

- 

[PYSIDE-1939](https://qt-project.atlassian.net/browse//PYSIDE-1939)  A crash in QTextBlock.layout() has been fixed.

- 

[PYSIDE-1947](https://qt-project.atlassian.net/browse//PYSIDE-1947)  QAudioBuffer.data()/constData() have been added.

## 6.3.0[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id39)

- 

The PySide wheels have been split. There is now a PySide6-Essentials and a PySide6-Addons wheel. The PySide6 wheel has been kept as a convenience to install all modules.

- 

The QtNfc module has been added.

- 

New QML tools have been added: pyside6-metaobjectdump, pyside6-qmltyperegistrar and pyside6-qmllint.

- 

Several class decorators have been added for QML: QmlAttached, QmlExtended, QmlForeign, QmlNamedElement, QmlSingleton and QmlUncreatable.

- 

class QPyQmlPropertyValueSource for implementing QML value property sources has been added.

- 

QML code has been split out from libpyside into a new library libpysideqml. libpyside thus no longer depends on QtQml and pyside.h no longer includes QML headers. pyside.h has been split into smaller headers.

- 

The setup.py –qmake option is deprecated starting with Qt 6.3. Use the –qtpaths option instead.

- 

Build directories are now created inside the root ./build directory, rather than directly under the root of the project.

- 

A context manager for override cursors has been added. It is now possible to write code like: with QApplication.setOverrideCursor(Qt.WaitCursor):…

- 

A completely new development was done to support the fast PyPy implementation. A listing of all the necessary steps can be found in the extra documentation for PyPy with PySide in ./doc/pypyside.rst .

- 

[PYSIDE-535](https://qt-project.atlassian.net/browse//PYSIDE-535)  Support for PyPy was added. Examples were fixed and adapted to use context managers, for example for QPainter, to ensure proper deletion.

- 

[PYSIDE-535](https://qt-project.atlassian.net/browse//PYSIDE-535)  QPainter has become a context manager. Using a with statement saves the need to call painter.end() .

- 

[PYSIDE-610](https://qt-project.atlassian.net/browse//PYSIDE-610)  The SSL methods of QWebSockets were enabled.

- 

[PYSIDE-802](https://qt-project.atlassian.net/browse//PYSIDE-802)  Support for cross-building was added.

- 

[PYSIDE-841](https://qt-project.atlassian.net/browse//PYSIDE-841)  New tutorials were added: Debugging Tutorial and Signals and slots.

- 

[PYSIDE-841](https://qt-project.atlassian.net/browse//PYSIDE-841)  New examples were added: areachart, audiosource, barchart, blurpicker, borderlayout, btscanner, dragable icons, mimetypebrowser, relational table model, rendercontrol_opengl, screenshot, tab dialog and threadedqopenglwidget.

- 

[PYSIDE-841](https://qt-project.atlassian.net/browse//PYSIDE-841)  Further QML reference examples were added: binding, coercion, default, extended, grouped, methods, properties and valuesource.

- 

[PYSIDE-1318](https://qt-project.atlassian.net/browse//PYSIDE-1318)  The MyPy display of `Signal` was corrected so that the relationship of `Signal` and `SignalInstance` is reflected.

- 

[PYSIDE-1431](https://qt-project.atlassian.net/browse//PYSIDE-1431)  Signal instances allow pass-through of methods with the same name, explicitly and with multiple inheritance.

- 

[PYSIDE-1431](https://qt-project.atlassian.net/browse//PYSIDE-1431)  Signal initialization now respects the order of subclasses in the mro().

- 

[PYSIDE-1670](https://qt-project.atlassian.net/browse//PYSIDE-1670)  When a property overrides an existing function with multiple arity or parameters, an underscore is appended to the property name.

- 

[PYSIDE-1675](https://qt-project.atlassian.net/browse//PYSIDE-1675)  Error message are more correct now when indexed generic types are involved like Union, Sequence and Iterable.

- 

[PYSIDE-1675](https://qt-project.atlassian.net/browse//PYSIDE-1675)  A crash when inserting a signal into a non-QObject was fixed.

- 

[PYSIDE-1702](https://qt-project.atlassian.net/browse//PYSIDE-1702)  snake_case handling now does explicitly not touch user defined classes.

- 

[PYSIDE-1705](https://qt-project.atlassian.net/browse//PYSIDE-1705)  Properties are now usable in constructors of classes in any combination of snake_case and true_property.

- 

[PYSIDE-1746](https://qt-project.atlassian.net/browse//PYSIDE-1746)  The byte-compiling of example files is now suppressed to reduce wheel size.

- 

[PYSIDE-1758](https://qt-project.atlassian.net/browse//PYSIDE-1758)  A left-over replacement of the interactive underscore variable when QApplication is created was removed.

- 

[PYSIDE-1760](https://qt-project.atlassian.net/browse//PYSIDE-1760)  A race condition caused by the move from distutils to setuptools with certain Python builds was fixed.

- 

[PYSIDE-1765](https://qt-project.atlassian.net/browse//PYSIDE-1765)  true_property overriding was enabled.

- 

[PYSIDE-1765](https://qt-project.atlassian.net/browse//PYSIDE-1765)  The snake_case feature is now more complete since it renames hidden methods, too.

- 

[PYSIDE-1788](https://qt-project.atlassian.net/browse//PYSIDE-1788) repr  functions for some QEvent-derived classes were added.

- 

[PYSIDE-1252](https://qt-project.atlassian.net/browse//PYSIDE-1252)  Entry points for UI tools on macOS were fixed.

- 

[PYSIDE-1318](https://qt-project.atlassian.net/browse//PYSIDE-1318)  mypy-support: The handling of `Signal` was improved.

- 

[PYSIDE-1431](https://qt-project.atlassian.net/browse//PYSIDE-1431)  The equality test for inherited signals was fixed.

- 

[PYSIDE-1499](https://qt-project.atlassian.net/browse//PYSIDE-1499)  The implicit conversion of icon.addPixmap(str) was replaced by an explicit version which takes PyPathLike.

- 

[PYSIDE-1520](https://qt-project.atlassian.net/browse//PYSIDE-1520)  mypy-support: The handling of slots, enum and PathLike was improved.

- 

[PYSIDE-1547](https://qt-project.atlassian.net/browse//PYSIDE-1547)  The legacy OpenGL option is now used to build on linux, removing a dependency to vendor-specific OpenGL libraries.

- 

[PYSIDE-1605](https://qt-project.atlassian.net/browse//PYSIDE-1605)  An opaque container are now used for OpenGL in the hellogl2 example.

- 

[PYSIDE-1631](https://qt-project.atlassian.net/browse//PYSIDE-1631)  The qmlRegisterType() overload taking a library URL was added.

- 

[PYSIDE-1673](https://qt-project.atlassian.net/browse//PYSIDE-1673)  QObject.property() was fixed for QFlag types.

- 

[PYSIDE-1674](https://qt-project.atlassian.net/browse//PYSIDE-1674)  QVideoFrame::bits(int) was added.

- 

[PYSIDE-1675](https://qt-project.atlassian.net/browse//PYSIDE-1675)  MyPy support has been improved.

- 

[PYSIDE-1675](https://qt-project.atlassian.net/browse//PYSIDE-1675)  A bug in Slot. call  was fixed.

- 

[PYSIDE-1675](https://qt-project.atlassian.net/browse//PYSIDE-1675)  A segfault when signal was applied to non-QObject was fixed.

- 

[PYSIDE-1681](https://qt-project.atlassian.net/browse//PYSIDE-1681)  A hang in QQmlApplicationEngine functions with message handlers was fixed.

- 

[PYSIDE-1685](https://qt-project.atlassian.net/browse//PYSIDE-1685)  Constructing a QFont from a family string was fixed.

- 

[PYSIDE-1691](https://qt-project.atlassian.net/browse//PYSIDE-1691)  Class QCborTag was added.

- 

[PYSIDE-1696](https://qt-project.atlassian.net/browse//PYSIDE-1696)  QFlags comparison to self was fixed.

- 

[PYSIDE-1701](https://qt-project.atlassian.net/browse//PYSIDE-1701)  A bug in the TicTacToe Qt Designer taskmenu example was fixed.

- 

[PYSIDE-1702](https://qt-project.atlassian.net/browse//PYSIDE-1702) feature : snake_case handling on user defined classes was fixed.

- 

[PYSIDE-1703](https://qt-project.atlassian.net/browse//PYSIDE-1703)  The build with MSVC 19.29.30136 was fixed.

- 

[PYSIDE-1708](https://qt-project.atlassian.net/browse//PYSIDE-1708)  The QtQuick3D module was added.

- 

[PYSIDE-1709](https://qt-project.atlassian.net/browse//PYSIDE-1709)  A repr  function for QMetaObject was added.

- 

[PYSIDE-1709](https://qt-project.atlassian.net/browse//PYSIDE-1709)  The QML metatype json files of Qt are now shipped for usage by pyside6-qmllint.

- 

[PYSIDE-1714](https://qt-project.atlassian.net/browse//PYSIDE-1714)  The sequence protocol has been implemented for QRegion.

- 

[PYSIDE-1715](https://qt-project.atlassian.net/browse//PYSIDE-1715)  A crash when connecting a slot after disconnecting non- existent connection to same slot was fixed.

- 

[PYSIDE-1721](https://qt-project.atlassian.net/browse//PYSIDE-1721)  The documentation generation process has been streamlined and the snippets conversion tool has been improved.

- 

[PYSIDE-1725](https://qt-project.atlassian.net/browse//PYSIDE-1725)  URLs in class inheritance diagrams have been made clickable (within same module).

- 

[PYSIDE-1726](https://qt-project.atlassian.net/browse//PYSIDE-1726)  The build in case Vulkan is not installed was fixed.

- 

[PYSIDE-1727](https://qt-project.atlassian.net/browse//PYSIDE-1727)  Signature: The doc  attribute of classes was fixed.

- 

[PYSIDE-1730](https://qt-project.atlassian.net/browse//PYSIDE-1730)  Name clashes of signals and inherited methods were fixed.

- 

[PYSIDE-1736](https://qt-project.atlassian.net/browse//PYSIDE-1736)  QQmlApplicationEngine.load(str) was fixed.

- 

[PYSIDE-1755](https://qt-project.atlassian.net/browse//PYSIDE-1755)  Nuitka compiled methods are now safely distinguished.

- 

[PYSIDE-1757](https://qt-project.atlassian.net/browse//PYSIDE-1757) feature : A bug in true_property was fixed.

- 

[PYSIDE-1758](https://qt-project.atlassian.net/browse//PYSIDE-1758)  QApplication no longer touches the underscore variable.

- 

[PYSIDE-1769](https://qt-project.atlassian.net/browse//PYSIDE-1769)  Crashes in WebEngine signal emissions were fixed.

- 

[PYSIDE-1770](https://qt-project.atlassian.net/browse//PYSIDE-1770)  Enum QXYSeries.PointConfiguration enum was added.

- 

[PYSIDE-1798](https://qt-project.atlassian.net/browse//PYSIDE-1798)  QVariant can now be converted to enum types.

- 

[PYSIDE-1804](https://qt-project.atlassian.net/browse//PYSIDE-1804)  QByteArray:: msetitem () was fixed for big endian architectures.

- 

[PYSIDE-1815](https://qt-project.atlassian.net/browse//PYSIDE-1815)  QAbstractOAuth.setModifyParametersFunction was added.

- 

[PYSIDE-1824](https://qt-project.atlassian.net/browse//PYSIDE-1824)  QLowEnergyServiceData.characteristics() was fixed.

- 

[PYSIDE-1826](https://qt-project.atlassian.net/browse//PYSIDE-1826)  A crash when implementing QQuickAsyncImageProvider.requestImageResponse() was fixed.

- 

[PYSIDE-1827](https://qt-project.atlassian.net/browse//PYSIDE-1827)  Signals/slots with non-QObject object type parameters were fixed.

- 

[PYSIDE-1840](https://qt-project.atlassian.net/browse//PYSIDE-1840)  The qFuzzyCompare() overloads for the classes in QtGui were added.

- 

[PYSIDE-1845](https://qt-project.atlassian.net/browse//PYSIDE-1845)  Properties of type QQmlPropertyMap * were fixed.

- 

[PYSIDE-1876](https://qt-project.atlassian.net/browse//PYSIDE-1876)  Class QPyQmlParserStatus for handling QML parser status changes has been added.

- 

[QTBUG-95010] The new Multimedia-API was adopted.

## 6.2.4[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id40)

- 

[PYSIDE-1702](https://qt-project.atlassian.net/browse//PYSIDE-1702)  snake_case handling now does explicitly not touch user defined classes.

- 

[PYSIDE-1705](https://qt-project.atlassian.net/browse//PYSIDE-1705)  Properties are now usable in constructors of classes in any combination of snake_case and true_property.

- 

[PYSIDE-1765](https://qt-project.atlassian.net/browse//PYSIDE-1765)  The snake_case feature is now more complete since it renames hidden methods, too. Overriding was enabled.

- 

[PYSIDE-1252](https://qt-project.atlassian.net/browse//PYSIDE-1252)  The entry points for UI tools on macOS have been fixed.

- 

[PYSIDE-1798](https://qt-project.atlassian.net/browse//PYSIDE-1798)  QVariant can now be converted to Enum types.

- 

[PYSIDE-1804](https://qt-project.atlassian.net/browse//PYSIDE-1804)  A bug in QByteArray:: msetitem () on big endian architectures has been fixed.

- 

[PYSIDE-1815](https://qt-project.atlassian.net/browse//PYSIDE-1815)  QAbstractOAuth.setModifyParametersFunction() has been added

- 

[PYSIDE-1824](https://qt-project.atlassian.net/browse//PYSIDE-1824)  QLowEnergyServiceData.characteristics() has been fixed.

- 

[PYSIDE-1826](https://qt-project.atlassian.net/browse//PYSIDE-1826)  A life cycle issue with QQuickAsyncImageProvider.requestImageResponse() has been fixed.

- 

[PYSIDE-1827](https://qt-project.atlassian.net/browse//PYSIDE-1827)  Signals/slots with non-QObject object types have been fixed.

## 6.2.3[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id41)

- 

repr  functions for QEvent-derived classes were added.

- 

audio source, mimetype browser, borderlayout, threadedqopenglwidget and regular expression examples were added.

- 

A debugging tutorial was added.

- 

[PYSIDE-1318](https://qt-project.atlassian.net/browse//PYSIDE-1318)  The MyPy display of `Signal` was corrected so that the relationship of `Signal` and `SignalInstance` is reflected.

- 

[PYSIDE-1431](https://qt-project.atlassian.net/browse//PYSIDE-1431)  Signal instances allow pass-through of methods with the same name, explicitly and with multiple inheritance.

- 

[PYSIDE-1675](https://qt-project.atlassian.net/browse//PYSIDE-1675)  A crash when inserting a signal into a non-QObject was fixed.

- 

[PYSIDE-1675](https://qt-project.atlassian.net/browse//PYSIDE-1675)  A bug fix in Slot. call  was fixed.

- 

[PYSIDE-1675](https://qt-project.atlassian.net/browse//PYSIDE-1675)  A segfault when a signal is applied to a non-QObject was fixed.

- 

[PYSIDE-1725](https://qt-project.atlassian.net/browse//PYSIDE-1725)  Documentation: classes in inheritance diagrams are now clickable (within one module).

- 

[PYSIDE-1726](https://qt-project.atlassian.net/browse//PYSIDE-1726)  The build for the case when no Vulkan is installed was fixed.

- 

[PYSIDE-1727](https://qt-project.atlassian.net/browse//PYSIDE-1727)  The signature and doc  attribute of classes issue was fixed.

- 

[PYSIDE-1730](https://qt-project.atlassian.net/browse//PYSIDE-1730)  A pass-through for signals in case of multiple inheritance was added.

- 

[PYSIDE-1736 QQmlApplicationEngine.load(str) was fixed.

- 

[PYSIDE-1755](https://qt-project.atlassian.net/browse//PYSIDE-1755) code  inspection on slot connections was fixed.

- 

[PYSIDE-1757](https://qt-project.atlassian.net/browse//PYSIDE-1757)  The error handling of true_property was improved.

- 

[PYSIDE-1769](https://qt-project.atlassian.net/browse//PYSIDE-1769)  A crash in WebEngine signal emissions was fixed.

- 

[PYSIDE-1770](https://qt-project.atlassian.net/browse//PYSIDE-1770)  Enum QXYSeries.PointConfiguration was added.

- 

[PYSIDE-1792](https://qt-project.atlassian.net/browse//PYSIDE-1792)  allow threads was added to QFileDialog’s static functions (getSaveFileName(), etc.).

- 

[QTBUG-95010] New Multimedia functions were added

## 6.2.2[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id42)

- 

pyside.h no longer includes QML headers.

- 

[PYSIDE-1666](https://qt-project.atlassian.net/browse//PYSIDE-1666)  sets are now supported for functions taking a QSet.

- 

[PYSIDE-1670](https://qt-project.atlassian.net/browse//PYSIDE-1670)  When a property would override an existing function with multiple arity or parameters, append an underscore to the property name.

- 

[PYSIDE-1675](https://qt-project.atlassian.net/browse//PYSIDE-1675)  Error message are more correct now when indexed generic types are involved like Union, Sequence and Iterable.

- 

[PYSIDE-535](https://qt-project.atlassian.net/browse//PYSIDE-535)  PyPySide: fix tests and improvements.

- 

[PYSIDE-802](https://qt-project.atlassian.net/browse//PYSIDE-802)  coin: Don’t prepend /bin: to PATH on Linux hosts

- 

[PYSIDE-803](https://qt-project.atlassian.net/browse//PYSIDE-803)  Allow threads in QtGui.QTextDocument.print_

- 

[PYSIDE-841](https://qt-project.atlassian.net/browse//PYSIDE-841)  Add new QML examples: ‘properties’, ‘coercion’, ‘methods’, ‘default’

- 

[PYSIDE-841](https://qt-project.atlassian.net/browse//PYSIDE-841)  Add new widgets examples: ‘blurpicker’, and ‘dragable icons’

- 

[PYSIDE-1033](https://qt-project.atlassian.net/browse//PYSIDE-1033)  setup.py: Don’t add the Qt prefix dir to PATH env var before building

- 

[PYSIDE-1431](https://qt-project.atlassian.net/browse//PYSIDE-1431)  Fix equality test for inherited signals

- 

[PYSIDE-1520](https://qt-project.atlassian.net/browse//PYSIDE-1520)  mypy-support: Improve handling of slots, enum and PathLike

- 

[PYSIDE-1547](https://qt-project.atlassian.net/browse//PYSIDE-1547)  Use legacy OpenGL option to build on linux

- 

[PYSIDE-1669](https://qt-project.atlassian.net/browse//PYSIDE-1669)  Fix QIcon.addPixmap() to accept a PyPathLike argument

- 

[PYSIDE-1670](https://qt-project.atlassian.net/browse//PYSIDE-1670) feature : handle properties with function overloads

- 

[PYSIDE-1675](https://qt-project.atlassian.net/browse//PYSIDE-1675)  Signature: re-implement error messages for generic types

- 

[PYSIDE-1675](https://qt-project.atlassian.net/browse//PYSIDE-1675)  signature: avoid false positives in .pyi import

- 

[PYSIDE-1696](https://qt-project.atlassian.net/browse//PYSIDE-1696)  Fix QFlags comparison to self

- 

[PYSIDE-1701](https://qt-project.atlassian.net/browse//PYSIDE-1701)  Fix invalid drawing of horizontal lines in the Qt Designer taskmenu example

- 

[PYSIDE-1703](https://qt-project.atlassian.net/browse//PYSIDE-1703)  Fix build with MSVC 19.29.30136

- 

[PYSIDE-1708](https://qt-project.atlassian.net/browse//PYSIDE-1708)  Add QtQuick3D module

- 

[PYSIDE-1709](https://qt-project.atlassian.net/browse//PYSIDE-1709)  Add a QmlUncreatable and QmlSingleton decorators

- 

[PYSIDE-1710](https://qt-project.atlassian.net/browse//PYSIDE-1710)  signature: improve error handling for embedded applications

- 

[PYSIDE-1714](https://qt-project.atlassian.net/browse//PYSIDE-1714)  Add a sequence protocol for QRegion

- 

[PYSIDE-1715](https://qt-project.atlassian.net/browse//PYSIDE-1715)  Fix crash when connecting slot after disconnecting non- existent connection to same slot

## 6.2.1[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id43)

- 

[PYSIDE-610](https://qt-project.atlassian.net/browse//PYSIDE-610)  Enable the SSL methods of QWebSockets

- 

[PYSIDE-841](https://qt-project.atlassian.net/browse//PYSIDE-841)  Add a signals and slots tutorial

- 

[PYSIDE-841](https://qt-project.atlassian.net/browse//PYSIDE-841)  Add examples: barchart, areachart, tab dialog, screenshot relational table model, btscanner, rendercontrol_opengl, and the ‘adding’ from the QML reference.

- 

[PYSIDE-1631](https://qt-project.atlassian.net/browse//PYSIDE-1631)  Add qmlRegister functions taking a library URL

- 

[PYSIDE-1673](https://qt-project.atlassian.net/browse//PYSIDE-1673)  Fix QObject.property() for QFlag types

- 

[PYSIDE-1674](https://qt-project.atlassian.net/browse//PYSIDE-1674)  Expose QVideoFrame::bits(int)

- 

[PYSIDE-1681](https://qt-project.atlassian.net/browse//PYSIDE-1681)  Fix hang in QQmlApplicationEngine functions with message handler

- 

[PYSIDE-1685](https://qt-project.atlassian.net/browse//PYSIDE-1685)  Fix constructing a QFont from a family string

- 

[PYSIDE-1691](https://qt-project.atlassian.net/browse//PYSIDE-1691)  Add QCborTag

## 6.2.0[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id44)

- 

Crashes in QClipboard.mimeData(), QTextCursor.currentList() and QTextCursor.currentTable() have been fixed.

- 

The Python Unicode API was updated to the newest version when not in limited API mode, too.

- 

The function QUrl.fromFilePath supports now the os.PathLike structure in addition to string arguments.

- 

QMultiMap and QMultiHash are now converted to a dict of key/list of values (corresponding to defaultdict).

- 

QThreadPool().start(std::function) and tryStart(std::function) have been added.

- 

[PYSIDE-131](https://qt-project.atlassian.net/browse//PYSIDE-131)  The `tr` function now works also for PySide derived Python class instances with the right context.

- 

[PYSIDE-487](https://qt-project.atlassian.net/browse//PYSIDE-487)  Implement qmlRegisterSingletonInstance

- 

[PYSIDE-535](https://qt-project.atlassian.net/browse//PYSIDE-535)  Tests which use reference counting need to be skipped in upcoming PyPy builds.

- 

[PYSIDE-535](https://qt-project.atlassian.net/browse//PYSIDE-535)  During replacement of type extender macros by functions, a hidden enum/flags alias error was detected and fixed.

- 

[PYSIDE-1252](https://qt-project.atlassian.net/browse//PYSIDE-1252)  pyside6-lupdate and the related tools from Qt Linguist have been re-added, enabling using the Qt translation system.

- 

[PYSIDE-1252](https://qt-project.atlassian.net/browse//PYSIDE-1252)  The tr() translation method of QObject has been changed to be a class method. This makes it possible to use tr() on a class without instantiation.

- 

[PYSIDE-1334](https://qt-project.atlassian.net/browse//PYSIDE-1334)  QObject.connect() now returns an instance of QMetaObject.Connection which can be used to disconnect instead of a bool.

- 

[PYSIDE-1362](https://qt-project.atlassian.net/browse//PYSIDE-1362)  A crash in QCustom3DVolume::setTextureData() has been fixed.

- 

[PYSIDE-1378](https://qt-project.atlassian.net/browse//PYSIDE-1378)  Assistant is now shipped along with PySide.

- 

[PYSIDE-1436](https://qt-project.atlassian.net/browse//PYSIDE-1436)  Support Python 3.10

- 

[PYSIDE-1436](https://qt-project.atlassian.net/browse//PYSIDE-1436)  Feature switching needs to reset the internal type cache. This was an omittion that becomes relevant in Python 3.10 .

- 

[PYSIDE-1482](https://qt-project.atlassian.net/browse//PYSIDE-1482)  A number of missing classes from the qtbase, qt3d, qtdeclarative. repository have been added.

- 

[PYSIDE-1482](https://qt-project.atlassian.net/browse//PYSIDE-1482)  A number of free functions from QtQml have been added.

- 

[PYSIDE-1482](https://qt-project.atlassian.net/browse//PYSIDE-1482)  QSharedMemory was added.

- 

[PYSIDE-1499](https://qt-project.atlassian.net/browse//PYSIDE-1499)  pathlib.Path gets additionally accepted for all function arguments which have a std::filesystem::path type.

- 

[PYSIDE-1570](https://qt-project.atlassian.net/browse//PYSIDE-1570)  The QtDBus module has been added.

- 

[PYSIDE-1570](https://qt-project.atlassian.net/browse//PYSIDE-1570)  The QtNetworkAuth module has been added.

- 

[PYSIDE-841](https://qt-project.atlassian.net/browse//PYSIDE-841)  examples: clean and update code, add more screenshots, remove version numbers from qml imports and new examples: dynamic spline, string and object list models, markdowneditor, data surface, abstract list model qml, opengl under qml, richtext/textedit, linguist, qsharedmemory.

- 

[PYSIDE-841](https://qt-project.atlassian.net/browse//PYSIDE-841)  tutorials: update datavisualization and expenses

- 

[PYSIDE-862](https://qt-project.atlassian.net/browse//PYSIDE-862)  Allow spaces in ClassInfo keys

- 

[PYSIDE-905](https://qt-project.atlassian.net/browse//PYSIDE-905)  PySide6: Add Qt::FindChildOptions to QObject::findChild(ren)

- 

[PYSIDE-907](https://qt-project.atlassian.net/browse//PYSIDE-907)  PySide6: Add QKey support for the setShortcut method

- 

[PYSIDE-1019](https://qt-project.atlassian.net/browse//PYSIDE-1019) feature : Support generation of modified .pyi files and fix default instances.

- 

[PYSIDE-1019](https://qt-project.atlassian.net/browse//PYSIDE-1019)  pyi_generator: Optimize imports

- 

[PYSIDE-1019](https://qt-project.atlassian.net/browse//PYSIDE-1019)  feature: move getFeatureSelectId to Shiboken and refactor

- 

[PYSIDE-1019](https://qt-project.atlassian.net/browse//PYSIDE-1019)  Shiboken: Remove cheating macros

- 

[PYSIDE-1033](https://qt-project.atlassian.net/browse//PYSIDE-1033)  cmake: Fix option –sanitize-address

- 

[PYSIDE-1112](https://qt-project.atlassian.net/browse//PYSIDE-1112)  sample binding: Document how to force MSVC in case CMake detects clang

- 

[PYSIDE-1112](https://qt-project.atlassian.net/browse//PYSIDE-1112)  PySide6: Update documentation on Qt Designer and resource files

- 

[PYSIDE-1160](https://qt-project.atlassian.net/browse//PYSIDE-1160)  PySide6: Expose QHostInfo.lookupHost()

- 

[PYSIDE-1252](https://qt-project.atlassian.net/browse//PYSIDE-1252)  PySide6: Add entry points for the Qt Linguist tools

- 

[PYSIDE-1252](https://qt-project.atlassian.net/browse//PYSIDE-1252)  ApiExtractor: add classmethod attribute to add-function for tr()

- 

[PYSIDE-1252](https://qt-project.atlassian.net/browse//PYSIDE-1252)  ApiExtractor: add classmethod attribute to add-function, fix

- 

[PYSIDE-1329](https://qt-project.atlassian.net/browse//PYSIDE-1329)  PySide6: Fix signature of QObject.tr()

- 

[PYSIDE-1334](https://qt-project.atlassian.net/browse//PYSIDE-1334)  Return QMetaObject.Connection from QObject.connect()

- 

[PYSIDE-1362](https://qt-project.atlassian.net/browse//PYSIDE-1362)  Fix crash in QCustom3DVolume::setTextureData()

- 

[PYSIDE-1370](https://qt-project.atlassian.net/browse//PYSIDE-1370)  PySide6: Add QSharedMemory

- 

[PYSIDE-1378](https://qt-project.atlassian.net/browse//PYSIDE-1378)  PySide6: Add assistant executable

- 

[PYSIDE-1378](https://qt-project.atlassian.net/browse//PYSIDE-1378)  build scripts: Extract helper functions to patch executables

- 

[PYSIDE-1378](https://qt-project.atlassian.net/browse//PYSIDE-1378)  Build scripts/UNIX: Extract helper function to copy GUI executables

- 

[PYSIDE-1378](https://qt-project.atlassian.net/browse//PYSIDE-1378)  PySide6: Add some information on the tools

- 

[PYSIDE-1415](https://qt-project.atlassian.net/browse//PYSIDE-1415)  Turn generate_pyi into a general pyi_generator tool

- 

[PYSIDE-1415](https://qt-project.atlassian.net/browse//PYSIDE-1415)  Remove SimpleNamespace Python Implementation

- 

[PYSIDE-1437](https://qt-project.atlassian.net/browse//PYSIDE-1437)  Revert “Allow calling CI’s build scripts with python2”

- 

[PYSIDE-1438](https://qt-project.atlassian.net/browse//PYSIDE-1438)  Fix QSurfaceDataProxy::resetArray() crash

- 

[PYSIDE-1455](https://qt-project.atlassian.net/browse//PYSIDE-1455)  Turn off numpy support in libpyside by default

- 

[PYSIDE-1455](https://qt-project.atlassian.net/browse//PYSIDE-1455)  Fix Designer plugin to load on Linux/macOS, add hints for trouble-shooting.

- 

[PYSIDE-1467](https://qt-project.atlassian.net/browse//PYSIDE-1467)  PySide6: Fix signature of CoreApplication.instance()

- 

[PYSIDE-1482](https://qt-project.atlassian.net/browse//PYSIDE-1482)  Re-add QtMultimedia/Widgets, fix examples, and missing classes.

- 

[PYSIDE-1482](https://qt-project.atlassian.net/browse//PYSIDE-1482)  PySide6/signature: Add PySideSignalInstance

- 

[PYSIDE-1482](https://qt-project.atlassian.net/browse//PYSIDE-1482)  libpyside: Add type check for PySideSignalInstanceType

- 

[PYSIDE-1482](https://qt-project.atlassian.net/browse//PYSIDE-1482)  Add classes QChannel, QChannelComponent, QSignalSpy and more non-template QML functions

- 

[PYSIDE-1482](https://qt-project.atlassian.net/browse//PYSIDE-1482)  PySide6/QSignalSpy: Add constructor taking a signal

- 

[PYSIDE-1482](https://qt-project.atlassian.net/browse//PYSIDE-1482)  Add further global functions

- 

[PYSIDE-1482](https://qt-project.atlassian.net/browse//PYSIDE-1482)  VoidPtr: Add setters and getters for the size, and isWritable

- 

[PYSIDE-1499](https://qt-project.atlassian.net/browse//PYSIDE-1499)  cppgenerator: remove a left-over “this” to get rid of a warning

- 

[PYSIDE-1499](https://qt-project.atlassian.net/browse//PYSIDE-1499)  build support for pathlib.Path, migrating examples, and qml load functions

- 

[PYSIDE-1523](https://qt-project.atlassian.net/browse//PYSIDE-1523)  Document the usage of Nuitka

- 

[PYSIDE-1556](https://qt-project.atlassian.net/browse//PYSIDE-1556)  Fix cmake argument for standalone macOS

- 

[PYSIDE-1563](https://qt-project.atlassian.net/browse//PYSIDE-1563)  Fix crashes when using the QImage(uchar *) data constructors

- 

[PYSIDE-1563](https://qt-project.atlassian.net/browse//PYSIDE-1563)  Revert “Fix crashes when using the QImage(uchar *) data constructors”

- 

[PYSIDE-1563](https://qt-project.atlassian.net/browse//PYSIDE-1563)  Fix error about not holding the GIL when releasing QImage memory

- 

[PYSIDE-1566](https://qt-project.atlassian.net/browse//PYSIDE-1566)  Fix Designer plugin to load on macOS

- 

[PYSIDE-1568](https://qt-project.atlassian.net/browse//PYSIDE-1568)  CMake: Rename the ENABLE_ platform variables

- 

[PYSIDE-1568](https://qt-project.atlassian.net/browse//PYSIDE-1568)  Remove QtX11Extras, QtMacExtras and per-platform typesystem files

- 

[PYSIDE-1568](https://qt-project.atlassian.net/browse//PYSIDE-1568)  Introduce conditional processing instructions to typesystem XML

- 

[PYSIDE-1570](https://qt-project.atlassian.net/browse//PYSIDE-1570)  Add QtDBus module, QtNetworkAuth QtWebEngineQuick and initial Support for QtBluetooth

- 

[PYSIDE-1570](https://qt-project.atlassian.net/browse//PYSIDE-1570)  Re-add QtWebEngine

- 

[PYSIDE-1570](https://qt-project.atlassian.net/browse//PYSIDE-1570)  Fix assert when retrieving wrapper from different thread

- 

[PYSIDE-1571](https://qt-project.atlassian.net/browse//PYSIDE-1571)  PySide6: Add BluetoothServiceInfo::Alternative, Sequence

- 

[PYSIDE-1583](https://qt-project.atlassian.net/browse//PYSIDE-1583)  PySide6: Extend the porting guide

- 

[PYSIDE-1584](https://qt-project.atlassian.net/browse//PYSIDE-1584)  mdi/application examples: Fix startup without settings file

- 

[PYSIDE-1585](https://qt-project.atlassian.net/browse//PYSIDE-1585)  PySide6: Refactor qvariant conversion code

- 

[PYSIDE-1588](https://qt-project.atlassian.net/browse//PYSIDE-1588)  Use replaced types in functions signatures

- 

[PYSIDE-1589](https://qt-project.atlassian.net/browse//PYSIDE-1589)  nuitka: Fix slot access for compiled functions

- 

[PYSIDE-1593](https://qt-project.atlassian.net/browse//PYSIDE-1593)  PyClassProperty: Correct the decorator and publish the class

- 

[PYSIDE-1599](https://qt-project.atlassian.net/browse//PYSIDE-1599)  testing: enforce that .pyi files are always tested

- 

[PYSIDE-1609](https://qt-project.atlassian.net/browse//PYSIDE-1609)  PySide6: Fix crashes in QObject.findChild()

- 

[PYSIDE-1609](https://qt-project.atlassian.net/browse//PYSIDE-1609)  PySide6: Add a test for QObject.findChildren() by type

- 

[PYSIDE-1611](https://qt-project.atlassian.net/browse//PYSIDE-1611)  PySide6: Add missing API of QQuickFramebufferObject.Renderer

- 

[PYSIDE-1614](https://qt-project.atlassian.net/browse//PYSIDE-1614)  Fix logging level being set when importing PySide6

- 

[PYSIDE-1617](https://qt-project.atlassian.net/browse//PYSIDE-1617)  Fix leak in QML ListProperty type

- 

[PYSIDE-1619](https://qt-project.atlassian.net/browse//PYSIDE-1619)  Add fallback case for QSettings.value

- 

[PYSIDE-1621](https://qt-project.atlassian.net/browse//PYSIDE-1621)  signature: make zip file access totally virtual

- 

[PYSIDE-1621](https://qt-project.atlassian.net/browse//PYSIDE-1621)  signature: update and make embedding aware

- 

[PYSIDE-1621](https://qt-project.atlassian.net/browse//PYSIDE-1621)  Remove signature loader completely from physical FS

- 

[PYSIDE-1623](https://qt-project.atlassian.net/browse//PYSIDE-1623)  PySide6: Add Qt Quick Controls 2 to the documentation

- 

[PYSIDE-1625](https://qt-project.atlassian.net/browse//PYSIDE-1625)  PySide6: Fix QMenu.exec_()

- 

[PYSIDE-1626](https://qt-project.atlassian.net/browse//PYSIDE-1626)  feature: fix the UIC switching problem

- 

[PYSIDE-1626](https://qt-project.atlassian.net/browse//PYSIDE-1626)  PySide6: Work around uic feature test failure

- 

[PYSIDE-1629](https://qt-project.atlassian.net/browse//PYSIDE-1629)  PySide6: Fix crash with qmlRegisterSingletonType() when invoked from JavaScript

- 

[PYSIDE-1636](https://qt-project.atlassian.net/browse//PYSIDE-1636)  Fix GLES builds

- 

[PYSIDE-1639](https://qt-project.atlassian.net/browse//PYSIDE-1639)  Allow threads for QInputDialog templates, and QAbstractSocket methods.

- 

[PYSIDE-1646](https://qt-project.atlassian.net/browse//PYSIDE-1646)  Fix for OpenGL types on macOS

- 

[PYSIDE-1647](https://qt-project.atlassian.net/browse//PYSIDE-1647)  Fix crash when constructing a QApplication in an embedded application

- 

[PYSIDE-1650](https://qt-project.atlassian.net/browse//PYSIDE-1650)  PySide6: Add QAccessible::installFactory()

- 

[PYSIDE-1650](https://qt-project.atlassian.net/browse//PYSIDE-1650)  PySide6: Add QAccessibleActionInterface

- 

[PYSIDE-1659](https://qt-project.atlassian.net/browse//PYSIDE-1659)  PySide6: Document QUiLoader restriction wrt signal/slot connections

- 

[PYSIDE-1662](https://qt-project.atlassian.net/browse//PYSIDE-1662)  Fix Qt Quick painteditem example to work, and run from a different directory

- 

[PYSIDE-1663](https://qt-project.atlassian.net/browse//PYSIDE-1663)  Add QWebEnginePage::setWebChannel(QWebChannel*,quint32)

- 

[QTBUG-75870] qtpaths is now used to query Qt properties.

- 

[QTBUG-75870] build scripts: Remove qtchooser handling, replace qmake mkspec parsing by cmake, and introduce qtpaths as qmake replacement

- 

[QTBUG-95649] Disable gestures from QtSensors

## 6.1.3[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id45)

- 

The Python Unicode API was updated to the newest version when not in limited API mode, too.

- 

[PYSIDE-131](https://qt-project.atlassian.net/browse//PYSIDE-131)  The `tr` function now works also for PySide derived Python class instances with the right context, and fix translation for derived types.

- 

[PYSIDE-1252](https://qt-project.atlassian.net/browse//PYSIDE-1252)  The tr() translation method of QObject has been changed to be a class method. This makes it possible to use tr() on a class without instantiation.

- 

[PYSIDE-1482](https://qt-project.atlassian.net/browse//PYSIDE-1482)  Add classes QChannel, QChannelComponent, QSharedMemory.

- 

[PYSIDE-1609](https://qt-project.atlassian.net/browse//PYSIDE-1609)  PySide6: Fix crashes in QObject.findChild()

- 

[PYSIDE-1614](https://qt-project.atlassian.net/browse//PYSIDE-1614)  Fix logging level being set when importing PySide6

- 

[PYSIDE-1617](https://qt-project.atlassian.net/browse//PYSIDE-1617)  Fix leak in QML ListProperty type

- 

[PYSIDE-1621](https://qt-project.atlassian.net/browse//PYSIDE-1621)  signature: make zip file access totally virtual, and make embedding aware.

- 

[PYSIDE-1626](https://qt-project.atlassian.net/browse//PYSIDE-1626)  feature: fix the UIC switching problem

- 

[PYSIDE-1629](https://qt-project.atlassian.net/browse//PYSIDE-1629)  PySide6: Fix crash with qmlRegisterSingletonType() when invoked from JavaScript

- 

[PYSIDE-1636](https://qt-project.atlassian.net/browse//PYSIDE-1636)  Fix GLES builds

- 

[PYSIDE-1646](https://qt-project.atlassian.net/browse//PYSIDE-1646)  Fix the signature mapping after enabling macOS primitive types

- 

[PYSIDE-1647](https://qt-project.atlassian.net/browse//PYSIDE-1647)  Fix crash when constructing a QApplication in an embedded application

## 6.1.2[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id46)

- 

[PYSIDE-1482](https://qt-project.atlassian.net/browse//PYSIDE-1482)  A number of missing classes, enumerations and functions have been added.

- 

[PYSIDE-1160](https://qt-project.atlassian.net/browse//PYSIDE-1160)  QHostInfo.lookupHost() was added.

- 

[PYSIDE-1563](https://qt-project.atlassian.net/browse//PYSIDE-1563)  A previous fix the bug has been amended, fixing errors about not holding the GIL when releasing QImage memory.

- 

[PYSIDE-1589](https://qt-project.atlassian.net/browse//PYSIDE-1589)  Slot access for compiled functions for Nuitka has been fixed.

- 

[PYSIDE-1593](https://qt-project.atlassian.net/browse//PYSIDE-1593)  The decorator of PyClassProperty has been corrected and the class has been published.

## 6.1.1[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id47)

- 

A crash in QCustom3DVolume::setTextureData() has been fixed.

- 

Crashes in QClipboard.mimeData(), QTextCursor.currentList() and QTextCursor.currentTable() have been fixed.

- 

The internal mechanism to create .pyi files was generalized into a general usage tool.

- 

The Qt Designer plugin which was not working on macOS is now fixed.

- 

General improvement to examples and documentation.

- 

[PYSIDE-1019](https://qt-project.atlassian.net/browse//PYSIDE-1019) feature : Support generation of modified .pyi files and fixed other issues.

- 

[PYSIDE-1570](https://qt-project.atlassian.net/browse//PYSIDE-1570)  PySide6: Adapt QtMultimedia to current state

- 

[PYSIDE-1563](https://qt-project.atlassian.net/browse//PYSIDE-1563)  Fixed crashes when using the QImage(uchar *) data constructors

## 6.1.0[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id48)

- 

QtOpenGLFunctions have been moved into QtOpenGL. * Examples habe been improve: brush up, use snake_case, add new ones, etc

- 

[PYSIDE-535](https://qt-project.atlassian.net/browse//PYSIDE-535)  PyPy-compatibility was improved by: Avoid the builtins  quirk and import builtins, instead

- 

[PYSIDE-1019](https://qt-project.atlassian.net/browse//PYSIDE-1019)  Confusing import error messages causes by feature-import have been fixed.

- 

[PYSIDE-1425](https://qt-project.atlassian.net/browse//PYSIDE-1425)  The broken encoding of QCoreApplication.arguments() on Windows has been fixed.

- 

[PYSIDE-1455](https://qt-project.atlassian.net/browse//PYSIDE-1455)  Bindings for the Qt Designer libraries have been added

- 

[PYSIDE-1455](https://qt-project.atlassian.net/browse//PYSIDE-1455)  A Qt Designer plugin has been added, allowing for creating custom widgets in Python. (Experimental Support)

- 

[PYSIDE-1482](https://qt-project.atlassian.net/browse//PYSIDE-1482)  Active Qt, QtCharts, QtDataVisualization and QStateMachine have been re-added. The namespaces from QtCharts and QtDataVisualization have been removed.

- 

[PYSIDE-1503](https://qt-project.atlassian.net/browse//PYSIDE-1503)  Overloads using numpy-arrays of x,y data have been added to functions taking lists of QPointF. (Experimental support depending on option –pyside-numpy-support to setup.py)

- 

[PYSIDE-1520](https://qt-project.atlassian.net/browse//PYSIDE-1520)  Implicit C++ conversions generated by shiboken are now reflected as typing.Union[].

- 

[PYSIDE-1523](https://qt-project.atlassian.net/browse//PYSIDE-1523)  Nuitka: Allow for compiled functions and methods, too.

## 6.0.4[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id49)

- 

[PYSIDE-841](https://qt-project.atlassian.net/browse//PYSIDE-841)  Further examples have been added (editable Json Model, Paintbrush like example, matplotlib and downloader).

- 

[PYSIDE-1540](https://qt-project.atlassian.net/browse//PYSIDE-1540)  The performance of QPainter::drawPoints(QPolygon) has been improved.

- 

[PYSIDE-1544](https://qt-project.atlassian.net/browse//PYSIDE-1544)  std::pair has been adedd as a container.

## 6.0.3[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id50)

- 

[PYSIDE-955](https://qt-project.atlassian.net/browse//PYSIDE-955)  QOpenGLVersionFunctionsFactory has been added.

- 

[PYSIDE-1112](https://qt-project.atlassian.net/browse//PYSIDE-1112)  The documentation has been overhauled, particularly the examples, deployment and porting sections.

- 

[PYSIDE-1511](https://qt-project.atlassian.net/browse//PYSIDE-1511)  QOpenGLFunctions.glShaderSource()/glGetShaderSource() have been added.

## 6.0.2[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id51)

- 

[PYSIDE-1478](https://qt-project.atlassian.net/browse//PYSIDE-1478)  A bug related to using QQmlContext.setContextProperty() with the snake case feature has been fixed.

## 6.0.1[¶](https://doc.qt.io/qtforpython-6/release_notes/pyside6_release_notes.html#id52)

- 

[PYSIDE-454](https://qt-project.atlassian.net/browse//PYSIDE-454)  Remove rejection of namespace std in Qt bindings

- 

[PYSIDE-510](https://qt-project.atlassian.net/browse//PYSIDE-510)  signature: Fix the parser regex for Qt6

- 

[PYSIDE-841](https://qt-project.atlassian.net/browse//PYSIDE-841)  scriptable application/Unix: Remove setting of PYTHONHOME for virtualenv

- 

[PYSIDE-841](https://qt-project.atlassian.net/browse//PYSIDE-841)  scriptable application: Actually expose the generated module

- 

[PYSIDE-1019](https://qt-project.atlassian.net/browse//PYSIDE-1019)  feature: delete setter after creating property only for standard naming

- 

[PYSIDE-1019](https://qt-project.atlassian.net/browse//PYSIDE-1019)  feature: Fix a flag error when no snake_case is selected

- 

[PYSIDE-1447](https://qt-project.atlassian.net/browse//PYSIDE-1447)  qApp: fix flag handling in Python 3.8+ and a Python 3.9 issue

- 

[PYSIDE-1449](https://qt-project.atlassian.net/browse//PYSIDE-1449)  PySide6: Add QTestlib’s QAbstractItemModelTester

- 

[PYSIDE-1456](https://qt-project.atlassian.net/browse//PYSIDE-1456)  designer: add rpath for linux

- 

[PYSIDE-1460](https://qt-project.atlassian.net/browse//PYSIDE-1460)  signature: Fix infinite loop changing up directories on Windows shares

- 

[PYSIDE-1463](https://qt-project.atlassian.net/browse//PYSIDE-1463)  feature: Disable selection while creating a type

- 

[PYSIDE-1466](https://qt-project.atlassian.net/browse//PYSIDE-1466)  QSetting.value add overload documentation

- 

[PYSIDE-1469](https://qt-project.atlassian.net/browse//PYSIDE-1469)  build_scripts: fix get_config_var for Big Sur
