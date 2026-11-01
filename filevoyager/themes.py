import qt_themes
from PySide6.QtWidgets import QComboBox, QDialog, QDialogButtonBox, QFormLayout


class ThemeDialog(QDialog):
    def __init__(self, themes, settings, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Theme")
        self.themes = themes
        self.settings = settings
        layout = QFormLayout(self)
        self.theme = QComboBox()
        self.theme.addItems(sorted(themes))
        self.theme.setCurrentText(settings.value("appearance/theme", "github_light", type=str))
        layout.addRow("&Theme:", self.theme)
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Apply | QDialogButtonBox.StandardButton.Close)
        self.buttons.button(QDialogButtonBox.StandardButton.Apply).clicked.connect(self.apply_theme)
        self.buttons.rejected.connect(self.reject)
        layout.addRow(self.buttons)

    def apply_theme(self):
        name = self.theme.currentText()
        qt_themes.set_theme(self.themes[name], style=None)
        self.settings.setValue("appearance/theme", name)
        self.settings.sync()
