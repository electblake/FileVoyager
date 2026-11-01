"""Qt actions for file item views."""

from PySide6.QtCore import QSortFilterProxyModel, Qt
from PySide6.QtGui import QAction, QKeySequence, QStandardItem, QStandardItemModel
from PySide6.QtWidgets import (
    QDialog, QDialogButtonBox, QHeaderView, QKeySequenceEdit, QLabel, QLineEdit,
    QStyledItemDelegate, QTableView, QVBoxLayout,
)


class Shortcuts:
    def __init__(self, settings):
        self.settings = settings
        self.entries = {}

    def add(self, key, label, default, *actions):
        custom = (self.settings.value("shortcuts/" + key, type=str)
                  if self.settings.contains("shortcuts/" + key) else "")
        self.entries[key] = (label, default, actions)
        for action in actions:
            action.setShortcut(QKeySequence(custom or default, QKeySequence.SequenceFormat.PortableText))

    def set_custom(self, key, sequence):
        _, default, actions = self.entries[key]
        setting = "shortcuts/" + key
        if sequence.isEmpty():
            self.settings.remove(setting)
        else:
            self.settings.setValue(setting, sequence.toString(QKeySequence.SequenceFormat.PortableText))
        for action in actions:
            action.setShortcut(QKeySequence(default) if sequence.isEmpty() else sequence)


class ShortcutDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QKeySequenceEdit(parent)
        editor.setClearButtonEnabled(True)
        editor.editingFinished.connect(lambda: self.commitData.emit(editor))
        return editor

    def setEditorData(self, editor, index):
        editor.setKeySequence(QKeySequence(index.data(), QKeySequence.SequenceFormat.NativeText))

    def setModelData(self, editor, model, index):
        model.setData(index, editor.keySequence().toString(QKeySequence.SequenceFormat.NativeText))


class KeyboardShortcutsDialog(QDialog):
    def __init__(self, shortcuts, parent):
        super().__init__(parent)
        self.shortcuts = shortcuts
        self.setWindowTitle("Keyboard Shortcuts")
        self.resize(720, 480)
        layout = QVBoxLayout(self)
        self.search = QLineEdit()
        self.search.setPlaceholderText("Search actions or shortcuts…")
        self.search.setAccessibleName("Search keyboard shortcuts")
        self.search.setClearButtonEnabled(True)
        layout.addWidget(self.search)
        hint = QLabel("Double-click a custom shortcut and press the new keys. Clear it to use the default.")
        hint.setWordWrap(True)
        layout.addWidget(hint)
        self.model = QStandardItemModel(self)
        self.model.setHorizontalHeaderLabels(["Shortcut action", "Default", "Custom shortcut"])
        for key, (label, default, _) in shortcuts.entries.items():
            name = QStandardItem(label)
            name.setData(key, Qt.ItemDataRole.UserRole)
            name.setEditable(False)
            standard = QStandardItem(QKeySequence(default).toString(QKeySequence.SequenceFormat.NativeText))
            standard.setEditable(False)
            setting = "shortcuts/" + key
            custom = QKeySequence(shortcuts.settings.value(setting, type=str),
                                  QKeySequence.SequenceFormat.PortableText) if shortcuts.settings.contains(setting) else QKeySequence()
            self.model.appendRow([name, standard, QStandardItem(custom.toString(QKeySequence.SequenceFormat.NativeText))])
        self.proxy = QSortFilterProxyModel(self)
        self.proxy.setSourceModel(self.model)
        self.proxy.setFilterKeyColumn(-1)
        self.proxy.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.proxy.setSortCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.search.textChanged.connect(self.proxy.setFilterFixedString)
        self.table = QTableView()
        self.table.setAccessibleName("Keyboard shortcuts")
        self.table.setModel(self.proxy)
        self.table.setItemDelegateForColumn(2, ShortcutDelegate(self.table))
        self.table.setSortingEnabled(True)
        self.table.sortByColumn(0, Qt.SortOrder.AscendingOrder)
        self.table.verticalHeader().hide()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.table)
        self.buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        layout.addWidget(self.buttons)

    def accept(self):
        self.buttons.setFocus()
        for row in range(self.model.rowCount()):
            key = self.model.item(row, 0).data(Qt.ItemDataRole.UserRole)
            sequence = QKeySequence(self.model.item(row, 2).text(), QKeySequence.SequenceFormat.NativeText)
            self.shortcuts.set_custom(key, sequence)
        self.shortcuts.settings.sync()
        super().accept()


def install_item_shortcuts(view):
    rename = QAction("Rename", view)
    rename.setShortcutContext(Qt.ShortcutContext.WidgetShortcut)
    rename.setAutoRepeat(False)
    rename.triggered.connect(lambda: view.edit(view.selectionModel().selectedRows(0)[0]))
    view.addAction(rename)

    def update_rename():
        rename.setEnabled(len(view.selectionModel().selectedRows(0)) == 1)

    view.selectionModel().selectionChanged.connect(update_rename)
    update_rename()
    return rename
