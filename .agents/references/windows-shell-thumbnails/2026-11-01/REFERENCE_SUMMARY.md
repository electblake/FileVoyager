# Reference Summary

- Reference Date: `2026-11-01`
- Platform: Windows desktop Shell/COM and GDI, OS components rather than a separately versioned package. No installed Windows build or SDK version was measured during capture. Each mirrored page retains its own update/revision metadata.

## Current FileVoyager path

SHCreateItemFromParsingName obtains IShellItemImageFactory. GetImage with SIIGBF_THUMBNAILONLY (0x08) retrieves or extracts a thumbnail, excludes icons, and returns a caller-owned HBITMAP. Adding INCACHEONLY (0x10) would prohibit generation. Unsupported items and extraction failures still fail. Default sizing preserves aspect ratio. DeleteObject releases the returned bitmap. Disk access and extraction belong on workers; the GetImage page has differing UI-thread wording in its flags and remarks, so keep both cached retrieval and extraction off the GUI thread.

Sources: [GetImage](learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellitemimagefactory-getimage.md), [Shell item creation](learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nf-shobjidl_core-shcreateitemfromparsingname.md).

## Direct cache API

IThumbnailCache exposes GetThumbnail and GetThumbnailByID for a shared system cache. GetThumbnail takes IShellItem and requested size (maximum 1024), returning ISharedBitmap, optional cache flags and an optional thumbnail ID. GetThumbnailByID uses a previously obtained ID. There is no SetThumbnail method on this interface. Direct database writing is not part of this API contract.

Extraction uses registered Windows handlers. Extracted thumbnails are cached unless EXTRACTDONOTCACHE is set. GetImage uses this same cache; the direct cache interface is related documentation, not a second FileVoyager provider. WTS_CACHED (2) reports cached status and WTS_LOWQUALITY (1) reports dimensions below the requested size. Failures include extraction failure, timeout, unavailable surrogate and unsupported fast extraction.

Sources: [IThumbnailCache](learn.microsoft.com/en-us/windows/win32/api/thumbcache/nn-thumbcache-ithumbnailcache.md), [GetThumbnail](learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnail.md), [GetThumbnailByID](learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnailbyid.md).

## Flags and compatibility

| WTS flag | Value | Meaning |
| --- | --- | --- |
| EXTRACT | 0 | Extract if missing; not a nonzero bit to add to cache-only flags |
| INCACHEONLY | 1 | Cached only |
| FASTEXTRACT | 2 | Restrict uncached extraction to embedded EXIF thumbnail |
| FORCEEXTRACTION | 4 | Ignore cache and extract anew |
| EXTRACTDONOTCACHE | 0x20 | Extract without caching |
| EXTRACTINPROC | 0x100 | Load handler in caller; documented for debugging |

Default extraction uses surrogate isolation. Microsoft describes high-priority cache lookup followed by lower-priority extraction as an option, not a requirement to replace the existing GetImage path. Core thumbnail interfaces require Windows Vista / Server 2008 desktop applications. Individual flags add Windows 7 or Windows 8 requirements; consult their entries. No breaking-change claim is made from this snapshot.

Source: [WTS_FLAGS](learn.microsoft.com/en-us/windows/win32/api/thumbcache/ne-thumbcache-wts_flags.md).

## Bitmap ownership and provider boundary

GetSharedBitmap can expose shared memory; do not apply GetImage's caller-owned lifetime assumptions to that handle. ISharedBitmap::Detach transfers a bitmap, copying shared storage when needed, and requires the caller to delete it. GetSize and GetFormat report dimensions and alpha type. IThumbnailProvider is the handler interface, not a requirement for ordinary consumers to implement a custom decoder. Provider output is a 32-bit DIB with explicit unknown, RGB or ARGB alpha classification.

Sources: [ISharedBitmap](learn.microsoft.com/en-us/windows/win32/api/thumbcache/nn-thumbcache-isharedbitmap.md), [Detach](learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-isharedbitmap-detach.md), [provider contract](learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-ithumbnailprovider-getthumbnail.md), [handler overview](learn.microsoft.com/en-us/windows/win32/shell/thumbnail-providers.md).

## COM and GDI calls

Initialize COM on each calling thread. Balance every successful CoInitializeEx, including S_FALSE, with CoUninitialize; incompatible apartments produce RPC_E_CHANGED_MODE. Keep native interfaces on the worker and release before uninitialization. CoCreateInstance is captured for direct-cache activation context, not as a call used by the current loader.

GetObjectW reads bitmap metadata. GetDIBits copies pixels into owned storage; the bitmap must not be selected into a DC. Negative uncompressed DIB height indicates top-down rows; scan lines require DWORD alignment. Inspect actual copied scan-line counts and use the specified pixel format. CreateCompatibleDC/DeleteDC and DeleteObject have distinct cleanup responsibilities. A 32-bit buffer alone does not establish valid alpha.

Sources: [CoInitializeEx](learn.microsoft.com/en-us/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex.md), [GetDIBits](learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-getdibits.md), [BITMAPINFOHEADER](learn.microsoft.com/en-us/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader.md). Other signatures and cleanup contracts are indexed individually.

## Local runtime evidence (not vendor guarantees)

Fixtures preserve the service document and benchmark JSON: 75 tests passed; a fresh 500-BMP folder had 500 verified initial cache misses; 125 grid-requested thumbnails generated successfully and all 125 subsequently passed cache-only probes. These synthetic offscreen measurements do not establish universal format support, durable cache retention or mixed-format performance. The existing function name load_cached_thumbnail now includes generation. Worker scheduling remains unchanged and native failures propagate.

The 2026-10-31 bundle's cache-only recommendation is historical and must not reverse the authorized generation change. Python binding and Qt references remain in the sibling comtypes and pyside6-file-explorer topic bundles dated 2026-10-31.

## Capture gaps

Thirty official pages were captured. https://learn.microsoft.com/llms.txt returned HTTP 404. Attempted standalone URLs https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/ne-thumbcache-wts_cacheflags and https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/ne-thumbcache-wts_alphatype also returned 404. Their values are documented in the captured GetThumbnail/GetThumbnailByID and GetFormat/IThumbnailProvider::GetThumbnail pages. No missing page is represented as a successful mirror. SOURCE_URLS lists captured sources; these failed discovery URLs are recorded here explicitly.
