<!--
source: https://doc.qt.io/qtforpython-6/gettingstarted.html
retrieved: 2026-10-31T21:18:16.696940+00:00
final_url: https://doc.qt.io/qtforpython-6/gettingstarted.html
content_type: text/html
-->

# Getting Started - Qt for Python

[Skip to content](https://doc.qt.io/qtforpython-6/gettingstarted.html#furo-main-content)

[Qt for Python](https://doc.qt.io/qtforpython-6/index.html)

[Back to top](https://doc.qt.io/qtforpython-6/gettingstarted.html)

# Getting Started[¶](https://doc.qt.io/qtforpython-6/gettingstarted.html#getting-started)

Here you can find the steps to install and create a simple application using the two technologies that Qt provides: Qt Widgets and Qt Quick.

Note

If you are new to Qt, you can check the [Frequently Asked Questions](https://doc.qt.io/qtforpython-6/gettingstarted.html#faq-section)  section at the end of this page to understand concepts, file types, compatibles IDEs, etc. In case you own a Qt License, please refer to [Commercial Use](https://doc.qt.io/qtforpython-6/commercial/index.html#commercial-page) .

## Requirements[¶](https://doc.qt.io/qtforpython-6/gettingstarted.html#requirements)

Before you can install Qt for Python, first you must install the following software:

- 

[Official](https://www.python.org/downloads/)  Python 3.10+

- 

We highly  recommend using a virtual environment, such as [venv](https://docs.python.org/3/library/venv.html)  or [virtualenv](https://virtualenv.pypa.io/en/latest)  and avoid installing PySide6 via `pip` in your system.

- 

No Qt installation is required : having Qt installed in your system will not interfere with your PySide6 installation if you do it via `pip install`, because the Python packages (wheels) already include Qt binaries. Most notably, style plugins from the system won’t have any effect on PySide applications.

## Installation[¶](https://doc.qt.io/qtforpython-6/gettingstarted.html#installation)

### 1. Creating and activating an environment[¶](https://doc.qt.io/qtforpython-6/gettingstarted.html#creating-and-activating-an-environment)

You can do this by running the following on a terminal:

- 

Create environment (Your Python executable might be called `python3`):

```
python -m venv env
```

- 

Activate the environment on Linux/macOS:

```
source env/bin/activate
```

or in Windows:

```
env\Scripts\activate.bat
```

### 2. Installing PySide6[¶](https://doc.qt.io/qtforpython-6/gettingstarted.html#installing-pyside6)

Note

For a commercial installation, refer to [Commercial Use](https://doc.qt.io/qtforpython-6/commercial/index.html#commercial-page) .

Now you are ready to install the Qt for Python packages using `pip`. From the terminal, run the following command:

- 

For the latest version:

```
pip install pyside6
```

- 

For a specific version, like 6.10.1:

```
pip install pyside6==6.10.1
```

- 

It is also possible to install a specific snapshot from our servers. To do so, you can use the following command:

```
pip install --index-url=https://download.qt.io/snapshots/ci/pyside/6.10/latest pyside6 --trusted-host download.qt.io
```

### 3. Test your installation[¶](https://doc.qt.io/qtforpython-6/gettingstarted.html#test-your-installation)

Now that you have Qt for Python installed, test your setup by running the following Python constructs to print version information:

```
import PySide6.QtCore

# Prints PySide6 version
print(PySide6.__version__)

# Prints the Qt version used to compile PySide6
print(PySide6.QtCore.__version__)
```

Note

For more information about what’s included in the `pyside6` package, check [Package Details](https://doc.qt.io/qtforpython-6/package_details.html#package-details) .

## Create your first Qt Application[¶](https://doc.qt.io/qtforpython-6/gettingstarted.html#create-your-first-qt-application)

Qt provides two technologies to build User Interfaces:

- 

Qt Widgets, an imperative programming and design approach that has been around since the beginning of Qt, making it a stable and reliable technology for UI applications.

- 

Qt Quick, a declarative programming and design approach, which enables you to create fluid UIs by describing them in terms of simple elements.

Both technologies offer you the possibility to use drag and drop  tools to create your interfaces. [pyside6-designer](https://doc.qt.io/qtforpython-6/tools/pyside-designer.html#pyside6-designer)  for Qt Widgets (included when you install pyside6), and Qt Design Studio for Qt Quick ([Get it here](https://doc.qt.io/qt-6/install-qt-design-studio.html) ).

Note

After reading this page, it is recommended that you check the [pyside6-project](https://doc.qt.io/qtforpython-6/tools/pyside-project.html#pyside6-project)  tool to learn how to create projects automatically without writing all the code by hand.

### Create your first Qt Application with Qt Widgets[¶](https://doc.qt.io/qtforpython-6/gettingstarted.html#create-your-first-qt-application-with-qt-widgets)

Your Qt for Python setup is ready. You can explore it further by developing a simple application that prints `"Hello World"` in several languages. The following instructions will guide you through the development process:

- 

Imports

Create a new file named `hello_world.py`, and add the following imports to it.:

```
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
```

The PySide6 Python module provides access to the Qt APIs as its submodule. In this case, you are importing the QtCore , QtWidgets , and QtGui  submodules.

- 

Main Class

Define a class named `MyWidget`, which extends QWidget  and includes a QPushButton  and QLabel .:

```
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))
```

The `MyWidget` class has the `magic` member function that randomly chooses an item from the `hello` list. When you click the button, the `magic` function is called.

- 

Application execution

Now, add a main function where you instantiate `MyWidget` and `show` it.:

```
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
```

Run your example by writing the following command:

```
python hello_world.py
```

Try clicking the button at the bottom to see which greeting you get.

### Create your first Qt Application with Qt Quick[¶](https://doc.qt.io/qtforpython-6/gettingstarted.html#create-your-first-qt-application-with-qt-quick)

To do the same using Qt Quick:

- 

Imports

Create a new file named `hello_world_quick.py`, and add the following imports to it.:

```
import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
```

- 

Declarative UI

The UI can be described in the QML language:

```
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 300
    height: 200
    visible: true
    title: "Hello World"

    readonly property list<string> texts: ["Hallo Welt", "Hei maailma",
                                           "Hola Mundo", "Привет мир"]

    function setText() {
        var i = Math.round(Math.random() * 3)
        text.text = texts[i]
    }

    ColumnLayout {
        anchors.fill:  parent

        Text {
            id: text
            text: "Hello World"
            Layout.alignment: Qt.AlignHCenter
        }
        Button {
            text: "Click me"
            Layout.alignment: Qt.AlignHCenter
            onClicked:  setText()
        }
    }
}
```

Put the this into a file named `Main.qml` into a directory named `Example` along with a file named `qmldir` to describe a basic QML module:

```
module Example
Main 254.0 Main.qml
```

- 

Application execution

Now, add a main function where you instantiate a QQmlApplicationEngine  and load the QML:

```
import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.addImportPath(sys.path[0])
    engine.loadFromModule("Example", "Main")
    if not engine.rootObjects():
        sys.exit(-1)
    exit_code = app.exec()
    del engine
    sys.exit(exit_code)
```

Run your example by writing the following command:

```
python main.py
```

Try clicking the button at the bottom to see which greeting you get.

## Next steps[¶](https://doc.qt.io/qtforpython-6/gettingstarted.html#next-steps)

Now that you have use both technologies, you can head to our [Examples](https://doc.qt.io/qtforpython-6/examples/index.html#pyside6-examples)  and [Tutorials](https://doc.qt.io/qtforpython-6/tutorials/index.html#pyside6-tutorials)  sections.

Tip

Visual Studio Code Users : If you use VSCode, check out the [Qt Python VSCode Extension](https://doc.qt.io/qtforpython-6/tools/vscode-ext.html#vscode-ext)  which provides project templates, debugging support, build tasks, and other productivity features for PySide6 development.

## Frequently Asked Questions[¶](https://doc.qt.io/qtforpython-6/gettingstarted.html#frequently-asked-questions)

Here you can find a couple of common questions and situations that will clarify questions before you start programming.

 What is Qt

Qt, QML, Widgets… What is the difference?

[Qt, QML, Widgets…What Is The Difference?](https://doc.qt.io/qtforpython-6/faq/whatisqt.html#whatisqt)

 Compatible IDEs

Which IDEs are compatible with PySide?

[Which IDEs Are Compatible?](https://doc.qt.io/qtforpython-6/faq/whichide.html#whichide)

 Binding Generation

What is Shiboken?

[Binding Generation: What Is Shiboken?](https://doc.qt.io/qtforpython-6/faq/whatisshiboken.html#whatisshiboken)

 File types

File Types in PySide

[File Types](https://doc.qt.io/qtforpython-6/faq/typesoffiles.html#typesoffiles)

 App distribution

Distributing your application to other systems and platforms

[Distributing Your Application to Other Systems/Platforms](https://doc.qt.io/qtforpython-6/faq/distribution.html#distribution)

 Why Qt for Python?

As a Qt/C++ developer, why should I consider Qt for Python?

[Why Qt for Python?](https://doc.qt.io/qtforpython-6/faq/whyqtforpython.html#whyqtforpython)
