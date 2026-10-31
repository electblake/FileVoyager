import importlib.metadata
import sys
import tomllib
from pathlib import Path

from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.win32.versioninfo import (
    FixedFileInfo, StringFileInfo, StringStruct, StringTable,
    VarFileInfo, VarStruct, VSVersionInfo,
)

root = Path(SPECPATH).parent
version = tomllib.loads((root / "pyproject.toml").read_text())["project"]["version"]
version_tuple = tuple(map(int, version.split("."))) + (0,)
datas = collect_data_files("filevoyager.image_processors", includes=["LICENSE", "README.md"])
datas.append((str(Path(sys.base_prefix) / "LICENSE.txt"), "licenses/Python"))
for name in ("PySide6", "PySide6_Essentials", "PySide6_Addons", "PySide6_Pdf", "shiboken6", "comtypes", "numpy", "pillow", "platformdirs"):
    distribution = importlib.metadata.distribution(name)
    for file in distribution.files:
        if ".dist-info/licenses/" in str(file):
            relative = str(file).split(".dist-info/licenses/", 1)[1]
            datas.append((str(distribution.locate_file(file)), str(Path("licenses") / name / Path(relative).parent)))

metadata = VSVersionInfo(
    ffi=FixedFileInfo(filevers=version_tuple, prodvers=version_tuple, mask=0x3f,
                      flags=0, OS=0x40004, fileType=1, subtype=0, date=(0, 0)),
    kids=[StringFileInfo([StringTable("040904B0", [
        StringStruct("FileDescription", "FileVoyager"),
        StringStruct("FileVersion", version),
        StringStruct("InternalName", "FileVoyager"),
        StringStruct("OriginalFilename", "FileVoyager.exe"),
        StringStruct("ProductName", "FileVoyager"),
        StringStruct("ProductVersion", version),
    ])]), VarFileInfo([VarStruct("Translation", [1033, 1200])])],
)
a = Analysis(
    [str(root / "filevoyager/__main__.py")], pathex=[str(root)],
    binaries=[], datas=datas, hiddenimports=["filevoyager.image_processors"],
    hookspath=[], hooksconfig={}, runtime_hooks=[], excludes=[], noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, [], exclude_binaries=True, name="FileVoyager",
          debug=False, strip=False, upx=False, console=True, version=metadata)
coll = COLLECT(exe, a.binaries, a.datas, strip=False, upx=False, name="FileVoyager")
