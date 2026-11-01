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

## System-managed generation and caching

GetImage uses `SIIGBF_THUMBNAILONLY` (`0x08`). Windows retrieves a cached thumbnail or extracts and caches one through its registered thumbnail handler. The existing `load_cached_thumbnail` entry point now permits generation. Unsupported items and extraction failures propagate; there are no retries, alternate providers, or icon substitutions. Cache retrieval and bitmap conversion still perform work and may access disk. The UI must retrieve failed futures rather than silently discarding their exceptions.

Sources: [saved Shell research](../.agents/references/windows-shell-thumbnails/2026-10-31/REFERENCE_SUMMARY.md), [comtypes reference](../.agents/references/comtypes/2026-10-31/REFERENCE_SUMMARY.md).

## Verification

Run `.venv\Scripts\python.exe -m unittest discover -s tests -p test_shell_thumbnails.py -v` on Windows. The native tests cover extraction and Windows cache reuse. Native GDI tests verify row orientation, BGR channel order, padded stride, owned data after deletion, and stable GDI handle count over 40 calls. A real Shell test verifies a cache-only miss on a unique valid BMP, generation through the production loader, and a subsequent cache-only hit without changing the source file. Missing paths still fail. An injected GetImage result verifies exact `0x08` arguments and handle cleanup on both successful copying and copy failure; short native copies also fail explicitly.

The successful retrieval test injects an HBITMAP at GetImage; it does not claim a verified live Windows-cache hit. The generation test uses the real registered Windows handler. Large-folder throughput and cold/warm-cache performance measurements belong to integrated application validation and have not been performed by this module's tests.

Subsequent live validation is documented in [thumbnail-cache-validation.md](thumbnail-cache-validation.md): the real 500-image folder produced 489 native cached-thumbnail hits per pass, plus 11 explicitly reported failures.

## Generation validation (2026-11-01)

All 75 tests passed in 12.573 seconds, including native cache-miss, generation and cache-hit verification and existing scheduler tests.

An offscreen Qt integration run used a fresh temporary folder of 500 synthetic 640x480 BMPs. Cache-only probes verified all 500 were absent before opening. The unchanged grid scheduler generated 125 thumbnails while navigating and scrolling, with zero native failures. Subsequent cache-only probes retrieved all 125 from Windows. The temporary source folder was removed after verification.

Initial navigation: 1041.93 ms; first viewport thumbnails: 380.29 ms; warm navigation: 106.96 ms; eight rapid navigation requests: 115.46 ms. Scrolling event-loop gap p95: 10.62 ms, maximum: 11.69 ms. Peak process working set: 210.36 MiB. Peak active requests: two; peak pending requests: 21. These synthetic BMP/offscreen measurements do not establish mixed-format large-folder performance or physical display frame times. The full suite ran separately from the final measurement.

The initial run generated successfully but its post-run probe used unnormalized Qt paths and failed parsing. The probe was corrected to normalize paths as the production adapter already does, and the complete test reran successfully on a new uncached folder.

Local artifacts: `.benchmarks/validate_generation.py` and `.benchmarks/cold-generation-ui-metrics.json`.
