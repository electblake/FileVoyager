import os
import subprocess
import sys
import tomllib
from pathlib import Path


root = Path(__file__).resolve().parents[1]
version = tomllib.loads((root / "pyproject.toml").read_text())["project"]["version"]
build_env = dict(os.environ)
build_env["PATH"] = os.pathsep.join((str(Path(os.environ["SystemRoot"]) / "System32"), os.environ["SystemRoot"]))
subprocess.run(
    [sys.executable, "-I", "-m", "PyInstaller", "packaging/FileVoyager.spec", "--clean", "--noconfirm"],
    cwd=root, env=build_env, check=True,
)
subprocess.run(
    [sys.argv[1], f"/DMyAppVersion={version}", "packaging/installer.iss"],
    cwd=root, check=True,
)
