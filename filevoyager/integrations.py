import sys
from pathlib import Path


APP_NAME = "FileVoyager"
CONTEXTS = (
    (r"Software\Classes\Directory\shell", "%1"),
    (r"Software\Classes\Directory\Background\shell", "%V"),
    (r"Software\Classes\Drive\shell", "%1"),
)


def install():
    import winreg

    # Inno Setup installs this package into a private Python environment.
    launcher = [str(Path(sys.executable).resolve()), "-I", "-m", "filevoyager"]
    icon = f'"{Path(__file__).resolve().with_name("FileVoyager.ico")}"'
    for root, target in CONTEXTS:
        menu_key = rf"{root}\{APP_NAME}"
        command = " ".join(f'"{part}"' for part in [*launcher, target])
        print(f"File Explorer command ({root}): {command}")
        with winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, menu_key, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, f"Open in {APP_NAME}")
            winreg.SetValueEx(key, "Icon", 0, winreg.REG_SZ, icon)
        with winreg.CreateKeyEx(
            winreg.HKEY_CURRENT_USER, menu_key + r"\command", 0, winreg.KEY_SET_VALUE,
        ) as key:
            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, command)
    print(f"[OK] Installed {len(CONTEXTS)} File Explorer context menu entries.")
    return 0
