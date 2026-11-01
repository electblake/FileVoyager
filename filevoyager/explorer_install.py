from concurrent.futures import ThreadPoolExecutor

from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QDialog, QGroupBox, QLabel, QPushButton, QVBoxLayout

from filevoyager import integrations


class ExplorerInstallDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Install in File Explorer")
        self.setMinimumWidth(480)
        self.executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="explorer-install")
        self.future = None
        self.timer = QTimer(self)
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.poll)
        layout = QVBoxLayout(self)
        explorer = QGroupBox("File Explorer")
        layout.addWidget(explorer)
        form = QVBoxLayout(explorer)
        hint = QLabel(
            f"Add Open in {integrations.APP_NAME} to right-click menus "
            "for folders, folder backgrounds, and drives."
        )
        hint.setWordWrap(True)
        form.addWidget(hint)
        self.install_button = QPushButton("Install in File Explorer")
        self.install_button.clicked.connect(self.install)
        form.addWidget(self.install_button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.status = QLabel()
        layout.addWidget(self.status)

    def install(self):
        self.install_button.setEnabled(False)
        self.status.setText("Installing in File Explorer…")
        self.future = self.executor.submit(integrations.install)
        self.timer.start()

    def poll(self):
        if not self.future.done():
            return
        self.timer.stop()
        future = self.future
        self.future = None
        future.result()
        self.status.setText("Installed in File Explorer")
        self.install_button.setEnabled(True)

    def done(self, result):
        if self.future is not None:
            return
        self.executor.shutdown(wait=True)
        super().done(result)
