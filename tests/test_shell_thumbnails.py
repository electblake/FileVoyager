"""Windows native tests; no thumbnail extraction or source decoder is used."""

from concurrent.futures import ThreadPoolExecutor
from ctypes import POINTER, WinDLL, byref, c_void_p, memmove, sizeof
from ctypes.wintypes import DWORD, HANDLE, HBITMAP, HDC, UINT
from pathlib import Path
import struct
import tempfile
import unittest
from unittest.mock import patch

from comtypes import COMError

from filevoyager import shell_thumbnails as shell


_create_dib = shell._gdi32.CreateDIBSection
_create_dib.argtypes = [HDC, POINTER(shell._BITMAPINFO), UINT, POINTER(c_void_p), HANDLE, DWORD]
_create_dib.restype = HBITMAP
_create_dib.errcheck = shell._require_nonzero
_user32 = WinDLL("user32", use_last_error=True)
_resources = _user32.GetGuiResources
_resources.argtypes = [HANDLE, DWORD]
_resources.restype = DWORD
_kernel32 = WinDLL("kernel32")
_process = _kernel32.GetCurrentProcess
_process.argtypes = []
_process.restype = HANDLE

# BGR rows: red/green on top, blue/white below; two padding bytes per row.
_PIXELS = b"\x00\x00\xff\x00\xff\x00\x00\x00\xff\x00\x00\xff\xff\xff\x00\x00"


def bitmap():
    info = shell._BITMAPINFO()
    info.bmiHeader = shell._BITMAPINFOHEADER(
        biSize=sizeof(shell._BITMAPINFOHEADER), biWidth=2, biHeight=-2,
        biPlanes=1, biBitCount=24, biSizeImage=len(_PIXELS),
    )
    address = c_void_p()
    handle = _create_dib(None, byref(info), 0, byref(address), None, 0)
    memmove(address, _PIXELS, len(_PIXELS))
    return handle


class ShellThumbnailTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="filevoyager-native-")
        cls.addClassCleanup(cls.temp.cleanup)
        cls.path = Path(cls.temp.name) / "uncached.bmp"
        # Valid, unique source file used only as a Shell item. Never request extraction.
        header = struct.pack("<2sIHHI", b"BM", 54 + len(_PIXELS), 0, 0, 54)
        dib = struct.pack("<IiiHHIIiiII", 40, 2, -2, 1, 24, 0, len(_PIXELS), 0, 0, 0, 0)
        cls.path.write_bytes(header + dib + _PIXELS)
        cls.executor = ThreadPoolExecutor(max_workers=1)
        cls.addClassCleanup(cls.executor.shutdown)

    def load(self):
        return self.executor.submit(shell.load_cached_thumbnail, str(self.path), 96, 64).result()

    def test_native_pixel_copy_orientation_channels_stride_and_ownership(self):
        handle = bitmap()
        try:
            result = shell._copy_bitmap(handle)
        finally:
            shell._delete_object(handle)
        self.assertEqual((result.width, result.height, result.stride), (2, 2, 8))
        self.assertIsInstance(result.pixels, bytes)
        self.assertEqual(len(result.pixels), 16)
        self.assertEqual(result.pixels[:6], _PIXELS[:6])
        self.assertEqual(result.pixels[8:14], _PIXELS[8:14])

    def test_cache_miss_propagates_and_does_not_populate_cache(self):
        before = self.path.read_bytes()
        for _ in range(2):
            with self.assertRaises(COMError):
                self.load()
        self.assertEqual(self.path.read_bytes(), before)

    def test_missing_path_propagates_native_failure(self):
        with self.assertRaises(OSError):
            self.executor.submit(shell.load_cached_thumbnail, str(self.path.with_name("missing.bmp")), 96, 64).result()

    def test_exact_cache_flags_and_bitmap_cleanup(self):
        handles = []
        requests = []

        def get_image(factory, size, flags):
            requests.append((size.cx, size.cy, flags))
            handles.append(bitmap())
            return handles[-1]

        with patch.object(POINTER(shell._IShellItemImageFactory), "GetImage", get_image):
            result = self.load()
        self.assertEqual(requests, [(96, 64, 0x18)])
        self.assertEqual(result.pixels[:6], _PIXELS[:6])
        with self.assertRaises(OSError):
            shell._copy_bitmap(handles[0])

    def test_copy_failure_propagates_and_releases_bitmap(self):
        handle = bitmap()
        failure = OSError("injected native copy failure")
        with patch.object(POINTER(shell._IShellItemImageFactory), "GetImage", return_value=handle):
            with patch.object(shell, "_copy_bitmap", side_effect=failure):
                with self.assertRaises(OSError) as raised:
                    self.load()
        self.assertIs(raised.exception, failure)
        with self.assertRaises(OSError):
            shell._copy_bitmap(handle)

    def test_short_native_copy_fails(self):
        handle = bitmap()
        try:
            with patch.object(shell, "_get_dibits", return_value=1):
                with self.assertRaisesRegex(OSError, "1 of 2"):
                    shell._copy_bitmap(handle)
        finally:
            shell._delete_object(handle)

    def test_repeated_calls_do_not_accumulate_gdi_handles(self):
        with patch.object(POINTER(shell._IShellItemImageFactory), "GetImage", side_effect=lambda *args: bitmap()):
            self.load()
            baseline = _resources(_process(), 0)
            for _ in range(40):
                self.load()
            self.assertEqual(_resources(_process(), 0), baseline)


if __name__ == "__main__":
    unittest.main()
