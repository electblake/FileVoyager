"""Shared Qt event loop and class-scoped scratch space for fast integration tests."""

import os
from pathlib import Path
import tempfile
import unittest

os.environ["QT_QPA_PLATFORM"] = "offscreen"

from PySide6.QtCore import QEventLoop, QTimer
from PySide6.QtWidgets import QApplication


class QtCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])
        cls.temp = tempfile.TemporaryDirectory(prefix="filevoyager-test-")
        cls.addClassCleanup(cls.temp.cleanup)
        cls.root = Path(cls.temp.name)

    def wait_for(self, condition, seconds=5):
        if condition():
            return
        loop = QEventLoop()
        poll = QTimer()
        poll.setInterval(1)
        poll.timeout.connect(lambda: loop.quit() if condition() else None)
        timeout = QTimer()
        timeout.setSingleShot(True)
        timeout.timeout.connect(loop.quit)
        poll.start()
        timeout.start(round(seconds * 1000))
        loop.exec()
        poll.stop()
        timeout.stop()
        self.assertTrue(condition(), "Qt condition did not become true")
