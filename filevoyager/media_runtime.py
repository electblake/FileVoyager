"""Load the installer-owned FFmpeg libraries before Qt creates a media backend."""

from ctypes import WinDLL
import os

from platformdirs import user_data_path


FFMPEG_BIN = (user_data_path("FileVoyager", appauthor=False)
              / "tools/ffmpeg/ffmpeg-9.0.2-full_build-shared/bin")
os.environ["QT_MEDIA_BACKEND"] = "ffmpeg"
# Absolute loads pin the DLLs used by Qt, independently of PATH and PySide6's copies.
# Keep both the search-directory cookie and libraries alive for the process lifetime.
DLL_DIRECTORY = os.add_dll_directory(str(FFMPEG_BIN))
FFMPEG_LIBRARIES = tuple(WinDLL(str(FFMPEG_BIN / name)) for name in (
    "avutil-61.dll", "swresample-7.dll", "avcodec-63.dll",
    "avformat-63.dll", "swscale-10.dll",
))
