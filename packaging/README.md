# Windows installer

Build on Windows x64 with Python 3.12, uv, and Inno Setup 6.7.3. From the repository root, create a fresh build environment and supply the actual installed compiler path:

```powershell
$env:UV_PROJECT_ENVIRONMENT = '.venv-build'
$env:PYTHONPATH = ''
uv sync --locked --group build --no-editable --python 3.12
.venv-build\Scripts\python -m unittest discover -s tests -v
.venv-build\Scripts\python packaging\build.py 'C:\Users\shoji\AppData\Local\Programs\Inno Setup 6\ISCC.exe'
```

`pyproject.toml` supplies the executable and installer version. `uv.lock` pins runtime and build packages. PyInstaller 6.20.0 and hooks 2026.4 produce `dist/FileVoyager`; Inno Setup produces `dist/installer/FileVoyager-Windows-x64-Setup-0.1.1.exe`. Build products are ignored by Git. Native build failures stop the Python build script. The freezer runs with isolated Python imports and only Windows system directories on PATH so unrelated developer tools cannot supply DLLs.

The installer uses a stable `FileVoyager.Desktop` AppId, installs below `%LOCALAPPDATA%\Programs\FileVoyager`, creates a Start menu shortcut and an optional desktop shortcut, and requires no elevation. It does not change PATH, download dependencies, register file associations, or install shared prerequisites. Settings remain in `%LOCALAPPDATA%\FileVoyager\FileVoyager.ini` through upgrades and uninstall. Silent installation uses `/VERYSILENT /SUPPRESSMSGBOXES /NORESTART`; post-install launch is skipped in silent mode.

The console executable preserves the application's native exception output. No application runtime code is changed for packaging.

## Dependency inventory

| Payload | Version | Scope and packaging |
| --- | --- | --- |
| CPython | 3.12.10 in the verified build | Private interpreter DLL, standard library and extension modules collected by PyInstaller; PSF license included |
| PySide6 / Essentials / Addons / shiboken6 | 6.12.0 | Private Qt DLLs, bindings, platform and image plugins selected by PyInstaller's Qt hooks |
| comtypes | 1.4.17 | Private Python COM bindings; MIT notice included |
| NumPy | 2.5.4 | Private extension modules and native numerical libraries selected by its hook; upstream notices included |
| Pillow | 13.0.0 | Private image codecs and modules selected by its hook; upstream license included |
| platformdirs | 4.14.2 | Private Python module; MIT notice included |
| Spectra-derived processors | Repository revision | Explicit hidden import because the browser does not import this standalone API; LICENSE and README included |
| Windows Shell / COM / GDI | Operating system | System-owned APIs; no DLLs copied into Windows directories |
| Windows ICU | Operating system | Uses the Windows ICU API required by Qt; no developer-tool ICU DLL is bundled |
| Microsoft C/C++ runtime | Versions supplied with Python and Qt wheels | Private DLLs collected by dependency analysis; no system-wide runtime installation |

Qt PDF and WebEngine wheels are transitive locked dependencies. The Qt image-plugin hook includes Qt PDF and supporting Qt DLLs; WebEngine is not collected. There are no helper executables or installer-time downloads. Private runtime updates ship with a new FileVoyager installer; Windows owns system API updates. Native payloads are x64. Third-party notices ship in `_internal/licenses` and the image-processor package.

The installed Qt wheels provide `LicenseRef-Qt-Commercial.txt`; those exact notices are retained. Confirm the applicable Qt commercial distribution rights before publishing this artifact. The local build is unsigned; no signing identity was provided.

## Release verification

Run the relocated bundle with only Windows system directories on PATH and without PYTHONPATH or the source tree as its working directory. Check navigation, sorting, view changes, saved preferences, and existing Shell thumbnails. Check optional processor imports and codecs separately when releasing changes to them.

In a disposable Windows x64 machine, test interactive clean installation, launch, same-AppId upgrade, silent installation and uninstallation. Verify shortcuts, preserved settings, and removal of private dependencies. This first installer has no prior production installer for a previous-release upgrade test.

On 2026-10-31 the host's VirtualBox inventory contained no registered machines, so disposable-machine lifecycle verification was blocked. Host smoke testing does not establish clean-machine compatibility. No VM or host installer lifecycle test is claimed.

The initial relocated smoke test caught an incompatible ICU DLL collected from a developer tool on PATH. The build script now restricts the freezer's PATH to Windows system directories.

Final host checks passed: 29 unit/integration tests, Inno compilation, and relocated executable startup, folder navigation, Back navigation, and Grid switching with Windows-only PATH and empty PYTHONPATH/PYTHONHOME. The smoke test produced no stderr output. Frozen media-thumbnail and optional processor/codec coverage, settings persistence across installation, and installer lifecycle checks remain unverified.

The unsigned 0.1.1 installer is 44,620,237 bytes. SHA-256: `d5c9ad2903013b53d724048a725538299e7d811ac0c80172cab851c36f19c9a7`.
