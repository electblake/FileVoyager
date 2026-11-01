"""Installer lifecycle uses a small local ZIP; media tests use the installed DLLs."""

import os
from pathlib import Path
import runpy
import tempfile
import unittest
from unittest.mock import patch
import zipfile

from filevoyager.media_runtime import FFMPEG_BIN


class PackagingTests(unittest.TestCase):
    def test_install_reinstall_launch_and_uninstall_preserve_preferences(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            data = root / "data"
            data.mkdir()
            preferences = data / "FileVoyager.ini"
            preferences.write_text("keep preferences", encoding="utf-8")
            with patch("platformdirs.user_data_path", return_value=data):
                bootstrap = runpy.run_path(str(Path(__file__).resolve().parents[1] / "packaging/bootstrap.py"))
            state = bootstrap["install"].__globals__
            state["install_dir"] = root
            (root / "app-wheel.txt").write_text("filevoyager-test.whl", encoding="utf-8")
            archive_root = FFMPEG_BIN.parent.name
            with zipfile.ZipFile(root / "ffmpeg.zip", "w") as archive:
                archive.writestr(archive_root + "/bin/ffmpeg.exe", b"test payload")
                archive.writestr(archive_root + "/LICENSE", "license")
            # Exercise the real filesystem lifecycle without installing Python packages.
            with patch("venv.EnvBuilder") as builder, patch("subprocess.run") as run:
                state["environment"].mkdir()
                for _ in range(2):
                    bootstrap["install"]()
                self.assertEqual(builder.return_value.create.call_count, 2)
                self.assertEqual(run.call_count, 4)
                self.assertTrue(all(call.kwargs["check"] for call in run.call_args_list))
                self.assertIn("--require-hashes", run.call_args_list[0].args[0])
                self.assertIn("--no-deps", run.call_args_list[1].args[0])
                with patch("sys.argv", ["bootstrap.pyz", "run", "C:/Pictures"]):
                    bootstrap["run"]()
                self.assertEqual(run.call_args.args[0], [str(state["python"]), "-I", "-m", "filevoyager", "C:/Pictures"])
                self.assertEqual(run.call_args.kwargs["env"]["FILEVOYAGER_LAUNCHER_PID"], str(os.getpid()))
            payload = state["ffmpeg"] / archive_root
            self.assertEqual((payload / "bin/ffmpeg.exe").read_bytes(), b"test payload")
            self.assertEqual((payload / "LICENSE").read_text(), "license")
            self.assertEqual(state["environment"].parent, state["ffmpeg"].parent.parent)
            bootstrap["uninstall"]()
            self.assertFalse(state["environment"].exists())
            self.assertFalse(state["ffmpeg"].exists())
            self.assertEqual(preferences.read_text(), "keep preferences")

    def test_installer_payload_matches_runtime_and_verifies_download(self):
        script = (Path(__file__).resolve().parents[1] / "packaging/installer.iss").read_text()
        entry = next(line for line in script.splitlines() if 'DestName: "ffmpeg.zip"' in line)
        self.assertIn(FFMPEG_BIN.parent.name + ".zip", entry)
        self.assertIn('Hash: "8d31e162f1616e37aab3fa2db991b97e1b8dbeb1c8465fd81a81be16ff91b328"', entry)
        self.assertIn("external download ignoreversion deleteafterinstall", entry)
