import base64
from concurrent.futures import Future
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

from PySide6.QtWidgets import QApplication, QWidget

from filevoyager import updates


class UpdateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def setUp(self):
        self.parent = QWidget()
        with patch.object(updates, "version", return_value="0.1.2"):
            self.dialog = updates.UpdateDialog(self.parent)
        self.addCleanup(self.parent.close)
        self.addCleanup(self.dialog.close)

    def release(self, version="0.1.10"):
        return {"tag_name": "v" + version, "assets": [{
            "name": f"FileVoyager-Windows-x64-Setup-{version}.exe",
            "size": 2097155, "browser_download_url": "https://example.invalid/setup.exe",
        }]}

    def finish(self, result):
        self.dialog.future = Future()
        self.dialog.future.set_result(result)
        self.dialog.poll()

    def test_staged_buttons_numeric_versions_and_shutdown_order(self):
        dialog = self.dialog
        self.assertFalse(dialog.download_button.isEnabled())
        self.assertFalse(dialog.install_button.isEnabled())
        pending = Future()
        with patch.object(dialog.executor, "submit", return_value=pending):
            dialog.check()
        self.assertFalse(dialog.check_button.isEnabled())
        self.assertEqual(dialog.progress.maximum(), 0)
        self.finish(self.release())
        self.assertTrue(dialog.download_button.isEnabled())
        self.assertFalse(dialog.install_button.isEnabled())
        with patch.object(dialog.executor, "submit", return_value=pending):
            dialog.download()
        dialog.transferred[0] = 1048576
        dialog.poll()
        self.assertEqual(dialog.progress.value(), 499)
        self.assertFalse(dialog.install_button.isEnabled())
        installer = Path(tempfile.gettempdir()) / "test-setup.exe"
        self.finish(installer)
        self.assertTrue(dialog.install_button.isEnabled())
        self.assertEqual(dialog.progress.value(), 1000)
        sequence = []
        with patch.object(updates, "install_after_exit", side_effect=lambda path: sequence.append(path)), \
                patch.object(self.parent, "close", side_effect=lambda: sequence.append("close")):
            dialog.install()
        self.assertEqual(sequence, [installer, "close"])

    def test_same_or_older_release_does_not_enable_download(self):
        for version in ("0.1.2", "0.1.1"):
            self.dialog.operation = "check"
            self.finish(self.release(version))
            self.assertFalse(self.dialog.download_button.isEnabled())
            self.assertFalse(self.dialog.install_button.isEnabled())

    def test_busy_dialog_stays_open_and_failure_surfaces_unchanged(self):
        dialog = self.dialog
        dialog.open()
        dialog.future = Future()
        dialog.reject()
        self.assertTrue(dialog.isVisible())
        failure = OSError("network failed")
        dialog.future.set_exception(failure)
        with self.assertRaises(OSError) as raised:
            dialog.poll()
        self.assertIs(raised.exception, failure)
        self.assertFalse(dialog.install_button.isEnabled())
        dialog.reject()
        self.assertFalse(dialog.isVisible())

    def test_http_check_and_streamed_download_on_worker(self):
        payload = b"x" * 2097155
        release = self.release()
        requests = []

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                requests.append((self.path, self.headers["User-Agent"]))
                body = json.dumps(release).encode() if self.path == "/latest" else payload
                self.send_response(200)
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, *args):
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        address = f"http://127.0.0.1:{server.server_port}"
        release["assets"][0]["browser_download_url"] = address + "/setup.exe"
        with tempfile.TemporaryDirectory() as temp, \
                patch.object(updates, "RELEASE_URL", address + "/latest"), \
                patch.object(updates, "user_cache_path", return_value=Path(temp)):
            self.dialog.check()
            self.assertEqual(self.dialog.future.result(timeout=10), release)
            self.dialog.poll()
            self.dialog.download()
            target = self.dialog.future.result(timeout=10)
            self.dialog.poll()
            self.assertEqual(target.read_bytes(), payload)
            self.assertEqual(self.dialog.transferred[0], len(payload))
            self.assertFalse(target.with_suffix(".part").exists())
            self.assertTrue(self.dialog.install_button.isEnabled())
        self.assertEqual(requests, [("/latest", "FileVoyager"), ("/setup.exe", "FileVoyager")])

    def test_handoff_waits_for_app_and_launcher_without_running_installer(self):
        # Use real Windows process handles and PowerShell, replacing only Setup
        # with a marker write. No application window or installer is launched.
        children = [subprocess.Popen(
            [sys.executable, "-c", "import sys; sys.stdin.buffer.read()"],
            stdin=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW,
        ) for _ in range(2)]
        for child in children:
            self.addCleanup(child.wait, timeout=10)
            self.addCleanup(child.stdin.close)
        with tempfile.TemporaryDirectory() as temp:
            marker = Path(temp) / "installer-started.txt"
            real_popen = subprocess.Popen

            def harmless_helper(args, **kwargs):
                script = base64.b64decode(args[-1]).decode("utf-16le")
                prefix, command = script.rsplit("Start-Process -FilePath ", 1)
                self.assertEqual(command.strip(), "'" + str(Path(temp) / "setup.exe") + "'")
                script = prefix + "[IO.File]::WriteAllText('" + str(marker).replace("'", "''") + "', 'started')"
                args[-1] = base64.b64encode(script.encode("utf-16le")).decode("ascii")
                return real_popen(args, **kwargs)

            with patch.object(updates.os, "getpid", return_value=children[0].pid), \
                    patch.dict(os.environ, {"FILEVOYAGER_LAUNCHER_PID": str(children[1].pid)}), \
                    patch.object(updates.subprocess, "Popen", side_effect=harmless_helper):
                helper = updates.install_after_exit(Path(temp) / "setup.exe")
            with self.assertRaises(subprocess.TimeoutExpired):
                helper.wait(timeout=1)
            self.assertFalse(marker.exists())
            children[0].stdin.close()
            children[0].wait(timeout=10)
            with self.assertRaises(subprocess.TimeoutExpired):
                helper.wait(timeout=1)
            self.assertFalse(marker.exists())
            children[1].stdin.close()
            children[1].wait(timeout=10)
            self.assertEqual(helper.wait(timeout=15), 0)
            self.assertEqual(marker.read_text(), "started")

    def test_bootstrap_supplies_launcher_pid(self):
        bootstrap = runpy.run_path(str(Path(__file__).resolve().parents[1] / "packaging/bootstrap.py"))
        with patch("subprocess.run") as run:
            bootstrap["run"]()
        self.assertEqual(run.call_args.kwargs["env"]["FILEVOYAGER_LAUNCHER_PID"], str(os.getpid()))


if __name__ == "__main__":
    unittest.main()
