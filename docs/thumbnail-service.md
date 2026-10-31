# Native thumbnail service

`filevoyager.shell_thumbnails.load_cached_thumbnail(path: str, width: int, height: int)` returns a frozen, slotted `ThumbnailPixels` with `width`, `height`, `stride`, and immutable `pixels: bytes`.

The buffer is **top-down BGR24**, opaque, with DWORD-aligned rows (`stride = (width * 3 + 3) & ~3`). Dimensions describe the actual Shell bitmap, not necessarily the requested bounds. Alpha is intentionally not part of this contract: GDI's 32-bit output must not be assumed to contain valid premultiplied alpha. There is no encoded image, source-file decoder, persistent cache, or live native handle in the result.

Qt adapter (owned by the UI implementation):

```python
result = load_cached_thumbnail(path, width, height)
image = QImage(result.pixels, result.width, result.height,
               result.stride, QImage.Format.Format_BGR888).copy()
```

The copy detaches QImage from Python buffer lifetime. Run retrieval and conversion on a worker. Create QPixmap and update models on the UI thread. The scheduler owns viewport prioritization, bounded concurrency, caching and rejection of stale results.

Supply a native Windows parsing path. Qt's QFileSystemModel supplies forward slashes; the Qt adapter normalizes these with `os.path.normpath` before calling this loader. A live grid test found that passing the slash-separated path directly to SHCreateItemFromParsingName fails with E_INVALIDARG. Path normalization belongs to the Qt boundary; the loader does not retry a failed parsing name.

## COM and native lifetime

Import this module during ordinary application startup (comtypes initializes its importing thread). Call the loader on dedicated workers that are COM-uninitialized or already MTA. It calls CoInitializeEx(MTA) and balances every successful initialization with CoUninitialize. Existing incompatible STA initialization fails naturally; there is no apartment retry. COM pointers stay on the calling thread and are released before uninitialization, including when traceback frames retain the Python pointer.

The loader deletes its HBITMAP and temporary device context in cleanup-only finally blocks. Native status checks raise OSError; Shell COM failures propagate unchanged. The user explicitly authorized these native checks and cleanup-only try/finally on 2026-10-31. There are no catches or retries.

## Cache-only behavior

The only GetImage flags are `SIIGBF_INCACHEONLY | SIIGBF_THUMBNAILONLY` (`0x18`). A cache miss or an item without a thumbnail raises. Nothing generates a thumbnail, retries with different flags, or returns an icon. Cache retrieval and bitmap conversion still perform work and may access disk. The UI must retrieve failed futures rather than silently discarding their exceptions.

Sources: [saved Shell research](../.agents/references/windows-shell-thumbnails/2026-10-31/REFERENCE_SUMMARY.md), [comtypes reference](../.agents/references/comtypes/2026-10-31/REFERENCE_SUMMARY.md).

## Verification

Run `.venv\Scripts\python.exe -m unittest discover -s tests -p test_shell_thumbnails.py -v` on Windows. Seven tests passed on 2026-10-31 with comtypes 1.4.17. Native GDI tests verify row orientation, BGR channel order, padded stride, owned data after deletion, and stable GDI handle count over 40 calls. Real Shell requests verify repeated cache misses on a unique valid BMP and failure for a missing path. An injected GetImage result verifies exact `0x18` arguments and handle cleanup on both successful copying and copy failure; short native copies also fail explicitly.

The successful retrieval test injects an HBITMAP at GetImage; it does not claim a verified live Windows-cache hit. No test requests thumbnail generation. Large-folder throughput and cold/warm-cache performance measurements belong to integrated application validation and have not been performed by this module's tests.

Subsequent live validation is documented in [thumbnail-cache-validation.md](thumbnail-cache-validation.md): the real 500-image folder produced 489 native cached-thumbnail hits per pass, plus 11 explicitly reported failures.
