import _winapi
import base64
from concurrent.futures import ThreadPoolExecutor
from importlib.metadata import version
import json
import os
from pathlib import Path
import subprocess
import tempfile
from urllib.request import Request, urlopen

from platformdirs import user_cache_path
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QDialog, QHBoxLayout, QLabel, QProgressBar, QPushButton, QVBoxLayout


RELEASE_URL = "https://api.github.com/repos/electblake/FileVoyager/releases/latest"


def latest_release():
    request = Request(RELEASE_URL, headers={
        "Accept": "application/vnd.github+json", "User-Agent": "FileVoyager",
    })
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def download_release(asset, progress):
    cache = user_cache_path("FileVoyager", appauthor=False, ensure_exists=True)
    directory = Path(tempfile.mkdtemp(prefix="update-", dir=cache))
    target = directory / asset["name"]
    partial = target.with_suffix(".part")
    request = Request(asset["browser_download_url"], headers={"User-Agent": "FileVoyager"})
    with urlopen(request, timeout=30) as response, partial.open("wb") as output:
        while chunk := response.read(1024 * 1024):
            output.write(chunk)
            progress[0] += len(chunk)
    partial.rename(target)
    return target


def install_after_exit(installer):
    # Inherit actual process handles: PID polling and fixed delays can race exit.
    pids = [os.getpid()]
    if "FILEVOYAGER_LAUNCHER_PID" in os.environ:
        pids.append(int(os.environ["FILEVOYAGER_LAUNCHER_PID"]))
    handles = [_winapi.OpenProcess(_winapi.SYNCHRONIZE, True, pid) for pid in pids]
    script = """$ErrorActionPreference = 'Stop'
foreach ($handle in @(%s)) {
    $wait = [System.Threading.EventWaitHandle]::new($false, [System.Threading.EventResetMode]::AutoReset)
    $wait.SafeWaitHandle = [Microsoft.Win32.SafeHandles.SafeWaitHandle]::new([IntPtr]$handle, $true)
    $wait.WaitOne() | Out-Null
    $wait.Dispose()
}
Start-Process -FilePath '%s'
""" % (", ".join(map(str, handles)), str(installer).replace("'", "''"))
    startup = subprocess.STARTUPINFO()
    startup.lpAttributeList = {"handle_list": handles}
    powershell = Path(os.environ["SystemRoot"]) / "System32/WindowsPowerShell/v1.0/powershell.exe"
    process = subprocess.Popen(
        [str(powershell), "-NoProfile", "-NonInteractive", "-EncodedCommand",
         base64.b64encode(script.encode("utf-16le")).decode("ascii")],
        startupinfo=startup, close_fds=True, creationflags=subprocess.CREATE_NO_WINDOW,
        cwd=installer.parent,
    )
    for handle in handles:
        _winapi.CloseHandle(handle)
    return process


class UpdateDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Check for updates")
        self.setMinimumWidth(480)
        self.current_version = version("filevoyager")
        self.executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="updates")
        self.future = None
        self.operation = None
        self.transferred = [0]
        self.timer = QTimer(self)
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.poll)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(f"FileVoyager\nVersion {self.current_version}"))
        self.status = QLabel("Check GitHub for the latest release.")
        layout.addWidget(self.status)
        self.progress = QProgressBar()
        self.progress.setRange(0, 1000)
        self.progress.setValue(0)
        layout.addWidget(self.progress)
        buttons = QHBoxLayout()
        layout.addLayout(buttons)
        self.check_button = QPushButton("Check for new releases")
        self.download_button = QPushButton("Download update")
        self.install_button = QPushButton("Quit and install")
        self.download_button.setEnabled(False)
        self.install_button.setEnabled(False)
        for button in (self.check_button, self.download_button, self.install_button):
            buttons.addWidget(button)
        self.check_button.clicked.connect(self.check)
        self.download_button.clicked.connect(self.download)
        self.install_button.clicked.connect(self.install)

    def check(self):
        self.check_button.setEnabled(False)
        self.download_button.setEnabled(False)
        self.install_button.setEnabled(False)
        self.status.setText("Checking GitHub releases…")
        self.progress.setRange(0, 0)
        self.operation = "check"
        self.future = self.executor.submit(latest_release)
        self.timer.start()

    def download(self):
        self.check_button.setEnabled(False)
        self.download_button.setEnabled(False)
        self.status.setText(f"Downloading FileVoyager {self.release_version}…")
        self.progress.setRange(0, 1000)
        self.progress.setValue(0)
        self.transferred[0] = 0
        self.operation = "download"
        self.future = self.executor.submit(download_release, self.asset, self.transferred)
        self.timer.start()

    def poll(self):
        if self.operation == "download":
            self.progress.setValue(self.transferred[0] * 1000 // self.asset["size"])
        if not self.future.done():
            return
        self.timer.stop()
        future = self.future
        self.future = None
        result = future.result()
        self.progress.setRange(0, 1000)
        self.progress.setValue(1000)
        self.check_button.setEnabled(True)
        if self.operation == "check":
            self.release_version = result["tag_name"].removeprefix("v")
            if tuple(map(int, self.release_version.split("."))) > tuple(map(int, self.current_version.split("."))):
                self.asset = next(asset for asset in result["assets"]
                                  if asset["name"] == f"FileVoyager-Windows-x64-Setup-{self.release_version}.exe")
                self.status.setText(f"FileVoyager {self.release_version} is available.")
                self.download_button.setEnabled(True)
            else:
                self.status.setText("FileVoyager is up to date.")
        else:
            self.installer = result
            self.status.setText("Download complete. Quit and install to update FileVoyager.")
            self.install_button.setEnabled(True)

    def install(self):
        self.install_button.setEnabled(False)
        self.progress.setRange(0, 0)
        self.status.setText("Saving settings and closing. Setup will start after FileVoyager exits.")
        install_after_exit(self.installer)
        self.accept()
        self.parentWidget().close()

    def done(self, result):
        if self.future is not None:
            return
        self.executor.shutdown(wait=True)
        super().done(result)
