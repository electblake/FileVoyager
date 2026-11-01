"""Windows Shell thumbnails with system-managed generation and caching. Call from an MTA worker, never paint/data()."""

from ctypes import (
    OleDLL, WinDLL, POINTER, Structure, byref, cast, c_int, c_ubyte,
    c_void_p, get_last_error, sizeof,
)
from ctypes.wintypes import BOOL, DWORD, HANDLE, HBITMAP, HDC, LONG, LPCWSTR, UINT, WORD
from dataclasses import dataclass

from comtypes import (
    COMMETHOD, GUID, HRESULT, IUnknown, CoInitializeEx, CoUninitialize,
    COINIT_MULTITHREADED,
)


class _SIZE(Structure):
    _fields_ = [("cx", LONG), ("cy", LONG)]


class _BITMAP(Structure):
    _fields_ = [
        ("bmType", LONG), ("bmWidth", LONG), ("bmHeight", LONG),
        ("bmWidthBytes", LONG), ("bmPlanes", WORD), ("bmBitsPixel", WORD),
        ("bmBits", c_void_p),
    ]


class _BITMAPINFOHEADER(Structure):
    _fields_ = [
        ("biSize", DWORD), ("biWidth", LONG), ("biHeight", LONG),
        ("biPlanes", WORD), ("biBitCount", WORD), ("biCompression", DWORD),
        ("biSizeImage", DWORD), ("biXPelsPerMeter", LONG),
        ("biYPelsPerMeter", LONG), ("biClrUsed", DWORD), ("biClrImportant", DWORD),
    ]


class _BITMAPINFO(Structure):
    _fields_ = [("bmiHeader", _BITMAPINFOHEADER), ("bmiColors", DWORD * 1)]


class _IShellItemImageFactory(IUnknown):
    _iid_ = GUID("{BCC18B79-BA16-442F-80C4-8A59C30C463B}")
    _methods_ = [COMMETHOD(
        [], HRESULT, "GetImage",
        (["in"], _SIZE, "size"),
        (["in"], UINT, "flags"),
        (["out"], POINTER(HBITMAP), "bitmap"),
    )]


_THUMBNAIL_ONLY = 0x00000008
_shell32 = OleDLL("shell32")
_gdi32 = WinDLL("gdi32", use_last_error=True)
_create_item = _shell32.SHCreateItemFromParsingName
_create_item.argtypes = [LPCWSTR, c_void_p, POINTER(GUID), POINTER(POINTER(_IShellItemImageFactory))]
_create_item.restype = HRESULT


def _require_nonzero(result, function, arguments):
    if not result:
        raise OSError(f"{function.__name__} failed (GetLastError={get_last_error()})")
    return result


_get_object = _gdi32.GetObjectW
_get_object.argtypes = [HANDLE, c_int, POINTER(_BITMAP)]
_get_object.restype = c_int
_get_object.errcheck = _require_nonzero
_create_dc = _gdi32.CreateCompatibleDC
_create_dc.argtypes = [HDC]
_create_dc.restype = HDC
_create_dc.errcheck = _require_nonzero
_delete_dc = _gdi32.DeleteDC
_delete_dc.argtypes = [HDC]
_delete_dc.restype = BOOL
_delete_dc.errcheck = _require_nonzero
_delete_object = _gdi32.DeleteObject
_delete_object.argtypes = [HANDLE]
_delete_object.restype = BOOL
_delete_object.errcheck = _require_nonzero
_get_dibits = _gdi32.GetDIBits
_get_dibits.argtypes = [HDC, HBITMAP, UINT, UINT, c_void_p, POINTER(_BITMAPINFO), UINT]
_get_dibits.restype = c_int
_get_dibits.errcheck = _require_nonzero


@dataclass(frozen=True, slots=True)
class ThumbnailPixels:
    """Owned top-down BGR24 bytes, opaque, with DWORD-aligned scan lines."""

    width: int
    height: int
    stride: int
    pixels: bytes


def _copy_bitmap(bitmap: int) -> ThumbnailPixels:
    """Copy an existing bitmap; the caller retains ownership of the handle."""
    metadata = _BITMAP()
    _get_object(bitmap, sizeof(metadata), byref(metadata))
    width, height = metadata.bmWidth, abs(metadata.bmHeight)
    stride = (width * 3 + 3) & ~3
    info = _BITMAPINFO()
    info.bmiHeader = _BITMAPINFOHEADER(
        biSize=sizeof(_BITMAPINFOHEADER), biWidth=width, biHeight=-height,
        biPlanes=1, biBitCount=24, biCompression=0, biSizeImage=stride * height,
    )
    buffer = (c_ubyte * (stride * height))()
    dc = _create_dc(None)
    try:
        # Do not select the bitmap into the DC: GetDIBits forbids that.
        copied = _get_dibits(dc, bitmap, 0, height, buffer, byref(info), 0)
        if copied != height:
            raise OSError(f"GetDIBits copied {copied} of {height} scan lines")
        return ThumbnailPixels(width, height, stride, bytes(buffer))
    finally:
        _delete_dc(dc)


def load_cached_thumbnail(path: str, width: int, height: int) -> ThumbnailPixels:
    """Retrieve or generate a Shell thumbnail, using the Windows cache and no icons.

    The calling worker must be uninitialized for COM or already in the MTA.
    Each call balances its own initialization. Native failures propagate.
    Requested dimensions are bounds; returned dimensions describe the bitmap.
    """
    CoInitializeEx(COINIT_MULTITHREADED)
    try:
        factory = POINTER(_IShellItemImageFactory)()
        _create_item(path, None, byref(_IShellItemImageFactory._iid_), byref(factory))
        try:
            bitmap = factory.GetImage(_SIZE(width, height), _THUMBNAIL_ONLY)
        finally:
            # Release before CoUninitialize even if a traceback retains factory.
            # Null the owning comtypes pointer to prevent its destructor releasing twice.
            factory.Release()
            cast(byref(factory), POINTER(c_void_p))[0] = None
        try:
            return _copy_bitmap(bitmap)
        finally:
            _delete_object(bitmap)
    finally:
        CoUninitialize()
