# Live Windows thumbnail-cache validation

Date: 2026-10-31. Windows host, Python 3.12, comtypes 1.4.17, PySide6 6.12.0.

## Native loader: real 500-image directory

Command:

```powershell
.venv\Scripts\python.exe tools/benchmark_shell_cache.py 'C:\Users\shoji\Pictures\Screenshots'
```

This enumerates the actual folder without opening or decoding image contents. Two worker threads request 192×192 bounds using only `IShellItemImageFactory::GetImage` flags `0x18`. Results are copied into owned pixels and immediately released after scalar measurements are recorded. The benchmark retains no thumbnail cache.

| Measurement | First pass | Repeat pass |
| --- | ---: | ---: |
| Images attempted | 500 | 500 |
| Cached thumbnails returned | 489 | 489 |
| Native cache failures | 11 | 11 |
| Total elapsed | 1.478 s | 1.421 s |
| Successful reads per second | 330.95 | 344.16 |
| Successful-call median | 4.99 ms | 4.85 ms |
| Successful-call p95 | 6.88 ms | 6.76 ms |
| Successful-call maximum | 61.35 ms | 11.72 ms |
| Pixel payload copied | 30,652,136 bytes | 30,652,136 bytes |

Peak native-benchmark process working set: **41.11 MiB**. This includes interpreter/bindings and is not the Qt application's memory use. Per-call latency excludes executor wait; throughput includes failed attempts and batch scheduling. First pass means fresh benchmark process, not flushed OS disk/cache state. One file had also been probed before this measurement. No cache eviction was performed.

A separate real first-file probe returned a 182×192 bitmap, 548-byte stride, and 105,216 owned bytes. The actual native hit path is therefore exercised, beyond the earlier injected-HBITMAP tests.

The same 11 recent files failed on both passes with HRESULT `0x80030002` (`-2147287038`). They exist in the enumerated folder but have no usable thumbnail returned by this cache-only request. No miss was turned into an icon or generated thumbnail. Raw paths and errors are preserved in `.benchmarks/shell-cache.json`. The benchmark saves its measurement report, then propagates a failed future unchanged and exits nonzero; these results are **not** an all-files-success claim.

## Scope and reproduction

`tools/benchmark_shell_cache.py` is a diagnostic measurement harness, not an application provider. It records failed futures explicitly for the report and then surfaces the failure. The full second pass measures repeat access; it does not retry misses with extraction flags or an alternative provider.

The production loader was not modified during this measurement. No Explorer window was opened to populate its cache, and no thumbnail-generation API was called. The existing 489-hit/11-failure distribution remained unchanged across both passes. Windows and unrelated applications may independently maintain their cache; the claim is limited to this test's calls.

These results cover a real 500-image folder, not a 10,000-image or larger real directory. Native service timings alone do not establish UI performance; the integrated results follow.

## Integrated Qt grid verification

The coordinated UI chat ran `tools/benchmark_native_ui.py` on the same 500-image folder using the production `shell_bridge` adapter. A first run failed all native requests because QFileSystemModel supplies forward-slash paths. The adapter now normalizes paths with `os.path.normpath` before the Shell call. The initial blank-grid run is not success evidence.

After correction, `.benchmarks/native-grid.png` was visually inspected: the viewport contains distinct image thumbnails with varied aspect ratios, in the expected file grid. These are actual cache-derived images, not synthetic colors or file-type icons. The screenshot remains local.

| Corrected Qt measurement | Result |
| --- | ---: |
| Initial navigation | 1,996.40 ms |
| First viewport thumbnail completion | 299.05 ms |
| Warm folder return | 32.42 ms |
| Eight rapid navigation requests | 80.45 ms |
| Native reads attempted / successful / failed | 184 / 180 / 4 |
| Scrolling event-loop gap p95 / maximum | 11.69 / 17.84 ms |
| Overall event-loop gap p95 / maximum | 13.91 / 103.21 ms |
| Maximum scrollbar setValue duration | 1.78 ms |
| Peak process working set | 155.47 MiB |
| Retained thumbnail pixel cache | 20.07 MiB |
| Peak active / pending thumbnail requests | 2 / 35 |

The grid requests only visible/prefetched images, so its four observed misses are a subset of the full-folder native sweep's 11. Native failures surfaced and the corrected benchmark exited nonzero; it is a working cached-hit rendering test with explicit cache misses, not an all-success run. Raw metrics and tracebacks are in `.benchmarks/native-ui-metrics.json` and `.benchmarks/native-ui-run.log`.

The scrolling metric measures Qt timer/event-loop responsiveness, **not frame rendering time or FPS**. Warm navigation benefits from application/model caches. No OS cold-cache flush was performed. Initial navigation around two seconds remains a performance concern; the repeat navigation and scrolling measurements do not erase that startup cost. No claim is made for folders larger than the tested 500 actual images.
