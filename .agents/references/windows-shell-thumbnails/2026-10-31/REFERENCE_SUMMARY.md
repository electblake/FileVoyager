# Reference Summary

Reference date: 2026-10-31. Platform: Windows desktop Shell/COM and GDI.

## Review conclusion

The proposed mechanism fits the requested cache-only behavior. Use one primary provider: `IShellItemImageFactory::GetImage`.

```python
SIIGBF_THUMBNAILONLY = 0x00000008
SIIGBF_INCACHEONLY = 0x00000010
FLAGS = SIIGBF_INCACHEONLY | SIIGBF_THUMBNAILONLY  # 0x18
```

## Official documentation findings

### Shell image retrieval

`INCACHEONLY` prevents extraction but alone permits a cached per-instance icon. Adding `THUMBNAILONLY` excludes icons. An unavailable thumbnail produces a failing HRESULT. `MEMORYONLY` is unsuitable for thumbnails because thumbnail retrieval accesses disk. The default size behavior preserves aspect ratio; requested dimensions are not a promise of an exact square. The caller owns the returned HBITMAP and must delete it. These flags and API support Windows Vista desktop clients and later.

Source: [GetImage](https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellitemimagefactory-getimage).

### Shared cache

Windows exposes a global thumbnail cache shared across applications. This supports reuse of Shell thumbnails associated with Explorer; the cache is not a FileVoyager-owned store. The direct `IThumbnailCache` API is background context, not a second provider for this project.

Source: [IThumbnailCache](https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nn-thumbcache-ithumbnailcache).

### Shell item creation and COM ownership

`SHCreateItemFromParsingName` takes a Unicode parsing name and the requested interface IID, returning an interface pointer. Declare the native types and calling convention explicitly. Each thread using COM needs initialization and matching uninitialization. Do not transfer raw apartment-bound pointers between threads. `comtypes` supports manually declared `IUnknown` interfaces using `_iid_`, `_methods_`, and `COMMETHOD`; out parameters become Python return values. It manages COM reference counts, so an additional manual `Release` risks double release.

Sources: [Shell item creation](https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nf-shobjidl_core-shcreateitemfromparsingname), [COM initialization](https://learn.microsoft.com/en-us/windows/win32/learnwin32/initializing-the-com-library), [comtypes interfaces](https://comtypes.readthedocs.io/en/stable/com_interfaces.html).

### Pixel transfer and native lifetime

`GetObjectW` supplies bitmap metadata. `GetDIBits` copies bitmap pixels into caller storage; configure the output layout explicitly, including row alignment and orientation. A negative DIB height requests top-down rows. The bitmap must not be selected into a device context during this operation. Its return value reports copied scan lines, with zero indicating failure. GDI calls do not all raise Python exceptions automatically. `DeleteObject` releases the bitmap after its data has been copied; deleting a selected bitmap fails.

Sources: [GetObjectW](https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-getobjectw), [GetDIBits](https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-getdibits), [DeleteObject](https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-deleteobject), [ctypes](https://docs.python.org/3.12/library/ctypes.html).

## Proposed project contract (engineering recommendations)

1. Accept a file path and requested pixel bounds.
2. Perform retrieval on a COM-initialized worker to keep disk access off the UI thread. Create, use, and release the Shell interface on that worker.
3. Request the image with exactly `0x18`.
4. Read actual bitmap dimensions and copy pixels into Python-owned storage. Define the buffer's channel order, stride, orientation, and alpha treatment before implementation; do not assume an HBITMAP is an encoded PNG or an RGBA array.
5. Release the HBITMAP and other acquired native resources. Return owned pixel data and actual dimensions, not a live native handle.

Respect the project's fail-fast policy: no extraction retry, custom exception wrapping, icon substitution, alternate provider, or default image. An absent cached thumbnail remains a failure. Do not silently treat a failed native pixel-copy status as successful image data. Native status-returning APIs require an explicit design decision at implementation time under the prohibition on adding error-handling branches; this review does not introduce a status-to-exception adapter.

The cache-only requirement prevents source-thumbnail generation, not all work: lookup, disk reads, pixel copying, and possible resizing still occur. Cache availability must be established by the request itself; prior Explorer use is not an application guarantee of a usable thumbnail at every requested size. No project-owned persistent thumbnail cache is proposed.

## Versions, scope, and evidence limits

- The repository's `mise.toml` requests Python `3.12`; the matching ctypes documentation is captured. This is configuration evidence, not a runtime-version measurement.
- The supplied research labels comtypes as `1.4.17`, but its URL uses the moving `/stable/` alias. The captured interface page does not establish that version; no dependency version is pinned by this review.
- `ctypes` is standard-library Python; `comtypes` is a third-party binding dependency. Thumbnail retrieval itself uses Windows built-ins.
- No Windows build, SDK version, installed comtypes version, or runtime thumbnail behavior was measured. No loader or application was implemented in this reference-only step.
- Before implementation is accepted, verify a known cached file, an uncached file, a file without a thumbnail, actual image dimensions and pixel orientation, and native handle lifetime. These are future checks, not completed tests.
- The mirror checked `/llms.txt` on learn.microsoft.com, comtypes.readthedocs.io, and docs.python.org; all returned HTTP 404. The requested documentation pages were captured successfully.

See [SOURCE_URLS.md](SOURCE_URLS.md) for the complete official-source inventory. User-supplied statements are preserved independently in [the research fixture](fixtures/user-drop-001-user-thumbnail-research.md); they are not runtime observations.
