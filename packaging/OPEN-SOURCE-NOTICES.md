# Open-source runtime dependencies

FileVoyager installs Qt for Python Community Edition from the public Python Package Index, using the exact versions and wheel hashes in requirements.txt. Qt is dynamically loaded from the virtual environment. The installed distribution metadata for PySide6, PySide6-Essentials, PySide6-Addons and shiboken6 6.12.0 declares `LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only`. A bundled `LicenseRef-Qt-Commercial.txt` describes the alternative commercial license; its presence does not make these PyPI distributions commercial-only.

- Community/commercial distribution documentation: https://doc.qt.io/qtforpython-6/commercial/index.html
- PySide6 Community package: https://pypi.org/project/PySide6/6.12.0/
- Qt for Python source: https://code.qt.io/cgit/pyside/pyside-setup.git/tree/?h=v6.12.0
- Qt source: https://code.qt.io/cgit/qt/qt5.git/tree/?h=v6.12.0
- Qt licensing and source downloads: https://www.qt.io/licensing/open-source-lgpl-obligations

Python 3.12.10 is installed privately from the Python Software Foundation's Windows x64 NuGet distribution. Its LICENSE.txt and bundled pip license remain in runtime/tools. Python source: https://www.python.org/downloads/release/python-31210/.

FFmpeg 9.0.2 Windows x64 shared is downloaded directly from Gyan Doshi's GitHub release at installation time. Gyan identifies this shared build as GPLv3. Its license, README, and documentation remain alongside the binaries under the platformdirs application-data directory, in tools/ffmpeg/ffmpeg-9.0.2-full_build-shared. Build information and library list: https://www.gyan.dev/ffmpeg/builds/. Binary release: https://github.com/GyanD/codexffmpeg/releases/tag/9.0.2. FFmpeg source revision linked by the distributor: https://github.com/FFmpeg/FFmpeg/commit/946fcce07b.

Dependency wheels are downloaded directly from PyPI at installation time, with their distribution metadata and notices intact. The bootstrap archive includes platformdirs and its MIT license. The FileVoyager wheel includes the Spectra-derived processors' LICENSE and README. No Qt binaries are embedded in the Setup executable.

The application adds no restriction on replacing the dynamically loaded Qt libraries or reverse engineering for debugging modifications to those libraries. The virtual environment is located using platformdirs.user_data_path('FileVoyager', appauthor=False), under its venv subdirectory.
