import importlib.metadata
import subprocess
import sys
import tomllib
import zipfile
from pathlib import Path


root = Path(__file__).resolve().parents[1]
version = tomllib.loads((root / "pyproject.toml").read_text())["project"]["version"]
stage = root / "build/installer"
stage.mkdir(parents=True, exist_ok=True)
subprocess.run(["uv", "build", "--wheel", "--out-dir", str(stage)], cwd=root, check=True)
subprocess.run(
    ["uv", "export", "--locked", "--no-dev", "--no-emit-project", "--no-header",
     "--format", "requirements-txt", "--output-file", str(stage / "requirements.txt")],
    cwd=root, check=True,
)
(stage / "app-wheel.txt").write_text(f"filevoyager-{version}-py3-none-any.whl", encoding="utf-8")
with zipfile.ZipFile(stage / "bootstrap.pyz", "w", zipfile.ZIP_DEFLATED) as archive:
    archive.write(root / "packaging/bootstrap.py", "__main__.py")
    distribution = importlib.metadata.distribution("platformdirs")
    for file in distribution.files:
        if str(file).startswith("platformdirs/") and file.suffix == ".py":
            archive.write(distribution.locate_file(file), str(file))
        if ".dist-info/licenses/" in str(file):
            archive.write(distribution.locate_file(file), str(file))
subprocess.run(
    [sys.argv[1], f"/DMyAppVersion={version}", "packaging/installer.iss"],
    cwd=root, check=True,
)
