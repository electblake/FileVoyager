# UI validation — 2026-10-31

Environment: Windows, Python 3.12.10, PySide6/Qt 6.12.0, comtypes 1.4.17. These are development measurements on this machine, not performance guarantees or frame-time certification.

## Real Windows thumbnail grid

The native benchmark used the existing `C:\Users\shoji\Pictures\Screenshots` directory (500 images), the real application views, `app.exec()`, and only the cache-only Shell service. No thumbnail generation or source decoding was performed. The initial populated grid was visually inspected locally; thumbnails have correct orientation, aspect ratio, and color. The screenshot remains in ignored `.benchmarks/native-grid.png` because it contains user images.

| Measurement | Result |
|---|---:|
| Initial window construction and first folder load | 1,996 ms |
| First grid viewport requests settled | 299 ms |
| Warm return to folder | 32.42 ms |
| Eight rapidly issued navigation requests, latest destination settled | 80.45 ms |
| Scrolling event-loop gap, p95 / maximum | 11.69 / 17.84 ms |
| Scroll-position command, maximum | 1.78 ms |
| Peak process working set | 155.47 MiB |
| Retained thumbnail pixels | 20.07 MiB |
| Completed native reads | 180 successes / 4 failures |
| Peak active / queued requests | 2 / 35 |

The 10 ms heartbeat measures event-loop availability, not rendered frames. The overall maximum heartbeat gap was 103.21 ms, including transitions and screenshot capture. Initial startup remains around two seconds on this machine; it is not yet an optimized launch path. These numbers precede the final folder-tree selection synchronization adjustment, which does not change the thumbnail pipeline.

The four failures were absent Shell cache entries reached during scrolling. The original COM exceptions were printed, no substitutes were displayed, and the benchmark re-observed completed futures after the event loop to exit with status 1. This is a successful rendering/integration check for cached items, not a failure-free all-images run. The service's full-folder probe independently reported 489 cached files and 11 misses; see [native validation](thumbnail-cache-validation.md).

An initial integration run failed all 147 requests because Qt supplied forward-slash paths to SHCreateItemFromParsingName. The production adapter now uses `os.path.normpath` before native calls; a regression test checks this exact boundary and BGR-to-RGB pixel conversion. A separate scheduler regression verifies failed requests are not automatically retried on refresh. Native counters in the current benchmark derive from completed futures on the UI thread, avoiding unsynchronized worker counters.

Raw results: `.benchmarks/native-ui-metrics.json` and `.benchmarks/native-ui-run.log`.

## Real video grid

The final isolated run used the user's requested video folder on M: and the same production provider. It completed with exit status 0: **187 native requests succeeded, zero failed**. The first viewport contained 21 cached non-null icons; a 2,043,090-pixel viewport was rendered in memory. No video screenshot was saved or displayed.

| Measurement | Result |
|---|---:|
| Initial navigation/window creation | 1,799.01 ms |
| First viewport requests settled | 271.72 ms |
| Warm return | 34.65 ms |
| Eight rapid navigation requests settled | 80.25 ms |
| Scrolling heartbeat p95 / maximum | 11.52 / 18.53 ms |
| Overall heartbeat maximum | 25.88 ms |
| Peak working set | 152.16 MiB |
| Retained thumbnail pixel payload | 19.92 MiB |
| Peak active / queued requests | 2 / 35 |

The directory changed externally between earlier probes (547 files) and this run. The final filename snapshots at 2026-10-31 21:40:00.516763Z and 21:40:04.667864Z both contained 522 files, with zero additions/removals during the measured interval. Qt displayed 526 entries, including folders. No source files were changed by these benchmarks. See [the combined video validation](video-thumbnail-validation.md) for the native full-folder probe and accounting. Raw final artifacts: `.benchmarks/video-native-ui-metrics.json` and `.benchmarks/video-native-ui-run.log`.

## Large-directory UI isolation

The synthetic benchmark populated 10,000 empty test filenames and returned generated QImages from a test-only callable. The production application never uses that callable. The last run measured:

- Initial enumeration/window load: 2,101.47 ms.
- First twelve synthetic thumbnails: 215.74 ms.
- Warm navigation: 141.62 ms.
- Peak working set: 154.09 MiB; cached pixel payload: 11.68 MiB.
- At most 2 active and 35 queued requests; only 61 thumbnails completed across viewport changes, rather than requesting all 10,000 files.
- Maximum scrolling heartbeat gap: 260.08 ms, although the scroll-position call itself took at most 0.47 ms.

The original QTest.qWait-based waits could starve Python workers and caused an integration-test timeout. Tests and the synthetic harness now wait through Qt event loops. At this initial implementation stage, the corrected 10,000-item run still showed long heartbeat stalls. A subsequent targeted profile identified ancestor-folder enumeration in the navigation tree; the folder tree now scans/sorts only directories on a worker and inserts lightweight rows in batches of 128. See [the subsequent profile, fix, and repeated results](scrolling-performance-validation.md), which supersedes this historical scrolling limitation. Actual larger cached-media folders, network directories, and OS-cold cache conditions still require measurement.

Profiling prompted cell-only thumbnail repainting and a one-column navigation model rather than hiding three columns. No unsupported claim of universal smoothness is made from these changes.

## Automated coverage

Integration tests cover shared selection, sorting, Back/Forward history, newest-navigation-wins behavior, viewport-bounded background work, warm display-cache reuse, stale completion rejection, byte-budgeted LRU eviction, unchanged exception propagation, and no automatic failed-request retry. Adapter tests cover Windows path normalization, BGR channels, orientation, detached 32-bit storage, and native exception identity. The service workstream supplies native COM/GDI tests.
