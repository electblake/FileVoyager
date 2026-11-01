import os
import shutil
import subprocess
import sys
import venv
import zipfile
from pathlib import Path

from platformdirs import user_data_path


install_dir = Path(sys.argv[0]).resolve().parent
environment = user_data_path("FileVoyager", appauthor=False) / "venv"
ffmpeg = user_data_path("FileVoyager", appauthor=False) / "tools/ffmpeg"
python = environment / "Scripts/python.exe"


def install():
    with zipfile.ZipFile(install_dir / "ffmpeg.zip") as archive:
        archive.extractall(ffmpeg)
    venv.EnvBuilder(with_pip=True).create(environment)
    subprocess.run(
        [str(python), "-I", "-m", "pip", "--isolated", "--disable-pip-version-check",
         "--retries", "0", "install", "--index-url", "https://pypi.org/simple",
         "--only-binary=:all:", "--require-hashes", "-r", str(install_dir / "requirements.txt")],
        check=True,
    )
    wheel = install_dir / (install_dir / "app-wheel.txt").read_text(encoding="utf-8")
    subprocess.run(
        [str(python), "-I", "-m", "pip", "--isolated", "--disable-pip-version-check",
         "--retries", "0", "install", "--no-index", "--no-deps", "--force-reinstall", str(wheel)],
        check=True,
    )


def run():
    subprocess.run(
        [str(python), "-I", "-m", "filevoyager", *sys.argv[2:]], check=True,
        env={**os.environ, "FILEVOYAGER_LAUNCHER_PID": str(os.getpid())},
    )


def uninstall():
    shutil.rmtree(environment)
    shutil.rmtree(ffmpeg)


if __name__ == "__main__":
    {"install": install, "run": run, "uninstall": uninstall}[sys.argv[1]]()
