# Windows installer

Setup installs a private Python 3.12.10 runtime, creates a virtual environment using platformdirs, and installs FileVoyager's wheel and locked dependencies. It does not freeze the application or include the project directory. An internet connection to NuGet and PyPI is required during installation.

## Build

On Windows x64 with Python 3.12, uv, and Inno Setup 6.7.3, run from the repository root:

```powershell
uv sync --locked
$env:QT_QPA_PLATFORM='offscreen'
uv run --locked python -m unittest discover -s tests -v
uv run python packaging\build.py 'C:\Users\shoji\AppData\Local\Programs\Inno Setup 6\ISCC.exe'
```

Supply the actual installed compiler path. `pyproject.toml` supplies the wheel and installer version. `uv.lock` supplies all runtime versions and hashes. `uv export --locked` generates the installer requirements. The bootstrap zipapp contains only the installation script, platformdirs, and its license. Build products are ignored by Git. The output is `dist/installer/FileVoyager-Windows-x64-Setup-0.1.4.exe`.

## Installation and updates

1. Inno Setup downloads the official PSF Windows x64 Python 3.12.10 NuGet archive, verifies its pinned SHA-256, and extracts it below `{app}/runtime`. Python is not registered globally and PATH is not modified.
2. The private interpreter runs `bootstrap.pyz install`. `platformdirs.user_data_path('FileVoyager', appauthor=False) / 'venv'` selects `%LOCALAPPDATA%\FileVoyager\venv` on Windows.
3. Python's `venv` module creates the environment with pip. Pip installs wheel-only dependencies directly from `https://pypi.org/simple`, with exact versions and required hashes. Pip configuration is isolated and retries are disabled. The local FileVoyager wheel is installed with dependency resolution disabled because dependencies were already installed from the lock.
4. Start menu and optional desktop shortcuts invoke the bootstrap launcher, which executes the venv's Python with `-I -m filevoyager`. The console preserves native exception output.

Installation is per-user without elevation, defaults to `%LOCALAPPDATA%\Programs\FileVoyager`, and keeps the stable `FileVoyager.Desktop` AppId. Reinstalling updates the same environment from the supplied requirements and wheel. Do not move the installed private Python directory: the venv refers to it.

The approved Inno exit-code check reports failure when environment creation or pip installation fails, returns a nonzero Setup exit code, disables post-install launch, and retains original command output in the setup log. The wizard displays installation failure; the uninstaller can remove the incomplete installation. There are no retries, alternate indexes, fallback interpreters, or custom recovery. On 2026-10-31 the user explicitly authorized this exit-code check as an exception to the project's custom-error-path restriction and requested venv installation in place of the Inno skill's default frozen-bundle workflow.

Close FileVoyager before reinstalling or uninstalling. Uninstall removes the venv and the private interpreter. Folder preferences at `%LOCALAPPDATA%\FileVoyager\FileVoyager.ini` remain. The venv is application-owned; manually installed packages inside it are also removed. No system Python installation is modified.

Silent installation: `/VERYSILENT /SUPPRESSMSGBOXES /NORESTART /LOG="install.log"`. Post-install launch is skipped in silent mode. Setup logging is enabled automatically; provide `/LOG` to choose a known path.

## Dependency sources

| Component | Source and ownership |
| --- | --- |
| Python 3.12.10 x64 | PSF NuGet `python` package, downloaded by Inno into the private application directory |
| platformdirs 4.14.2 | MIT-licensed bootstrap module; also installed in the venv from PyPI |
| Qt for Python Community 6.12.0 | Public PyPI PySide6, Essentials, Addons and shiboken6; metadata declares LGPL/GPL licensing |
| Qt PDF / WebEngine 6.12.0.140 | Transitive public PyPI dependencies installed with PySide6 |
| comtypes 1.4.17, NumPy 2.5.4, Pillow 13.0.0 | Public PyPI wheels installed with their native libraries, metadata and notices |
| FileVoyager 0.1.4 | Locally built wheel, including the Spectra-derived processors and their license |
| scikit-learn 1.9.1, SciPy 1.18.1 and their dependencies | Public PyPI wheels for vector comparisons and DBSCAN neighbor queries |
| Windows Shell / COM / GDI | Operating-system APIs; not installed by Setup |

Python URL: `https://api.nuget.org/v3-flatcontainer/python/3.12.10/python.3.12.10.nupkg`.
SHA-256: `0eb85c2dfccccf1b17352de4c397f69194035b7d37149eacc16f1147d93de3b8`.
Extracted size: 39,200,793 bytes. The archive includes Python, pip, venv and license files under `tools`.

See [open-source notices](OPEN-SOURCE-NOTICES.md). The prior commercial-only interpretation based on `LicenseRef-Qt-Commercial.txt` was incorrect: the public PyPI packages explicitly declare the open-source licensing alternatives. The installer is unsigned.

## Release verification

VM testing was explicitly waived by the user on 2026-10-31. Host installation tests do not establish compatibility with a clean Windows machine. Verify compilation, host silent installation, the installed wheel's tests, launch, same-version reinstall, uninstall, and preference preservation before publishing. This is the first published installer; a previous-release upgrade cannot yet be tested.

Verified on 2026-10-31: all 29 source tests and all 29 installed-wheel tests passed. Host silent install, same-version reinstall, final clean install and uninstall returned 0. Preferences survived uninstall byte-for-byte. A deliberate venv creation failure returned 1 and retained the original traceback. Uninstalling while the smoke-test app was still running failed on a locked DLL; after stopping the test processes, cleanup returned 0.

The installed native-thumbnail benchmark completed 193 requests with zero failures. The final 10,000-item synthetic benchmark measured 17.19 ms maximum scrolling heartbeat gap, 36.16 ms warm navigation, and 176.72 MiB peak working set; the same-session baseline was 16.21 ms, 38.68 ms, and 177.04 MiB. A preceding run was slower, so these are workload-specific observations, not latency guarantees. The scroll-restoration test exposed a stale scrollbar-range race; the grid now updates geometry before announcing layout completion.

The 0.1.1 unsigned installer is 2,632,406 bytes, SHA-256 `4da45cb18e6d01a6cf50f12674ab86ee57d47cf00c69dd456b0e4716698e104b`.

Release 0.1.2 changes version metadata only. Its wheel contents and runtime dependency lock were compared with 0.1.1, and its installer was compiled without launching the application or running installation again. Each GitHub release includes its own SHA-256 checksum asset.

Release 0.1.4 includes the similarity dock and DBSCAN sorting. All 46 tests passed with the offscreen Qt platform; the staged wheel matched project sources, all exported dependencies were pinned with hashes, and Inno Setup compilation and version checks passed. No installer execution or upgrade/uninstall lifecycle testing was performed for this release. The release includes an installer SHA-256 checksum asset.
