# Actual video-folder cache validation

For the subsequent scrolling fix and independent video regression, see [scrolling-performance-validation.md](scrolling-performance-validation.md). The historical measurements below are preserved as their own snapshots.

Date: 2026-10-31. Windows, Python 3.12, comtypes 1.4.17, PySide6 6.12.0.

Target: `M:\X3\Catalog\Inspired\Jecay-Fansites\Francia_James.Francety.Brunette\video`.
The initial native enumeration found **547 MP4 files**. Source videos were neither decoded nor played. The directory changed externally during later testing: subsequent enumerations found 533 and then 522 files. At 2026-10-31 21:39:13 UTC, an independent enumeration found 522 files; a PowerShell check including hidden/system entries found the same count, all with Archive attributes. The count difference is not attributed to hidden-file filtering. These tests did not modify the media.

## Native Windows-cache results

```powershell
.venv\Scripts\python.exe tools/benchmark_shell_cache.py 'M:\X3\Catalog\Inspired\Jecay-Fansites\Francia_James.Francety.Brunette\video' --suffix .mp4 --output .benchmarks/video-shell-cache.json
```

The unchanged loader uses `IShellItemImageFactory::GetImage` with exactly `0x18` (`INCACHEONLY | THUMBNAILONLY`), then copies the returned bitmap. No extraction flag, source decoder, icon substitution, or cache-populating Explorer action is involved. Two workers run with at most two calls in flight.

| Measurement | First pass | Repeat pass |
| --- | ---: | ---: |
| Cached video thumbnails | 547 / 547 | 547 / 547 |
| Failures | 0 | 0 |
| Total elapsed | 1.467 s | 1.299 s |
| Successful reads per second | 372.93 | 421.23 |
| Call latency median | 4.57 ms | 4.25 ms |
| Call latency p95 | 6.08 ms | 5.38 ms |
| Call latency maximum | 63.67 ms | 9.27 ms |
| Owned pixel bytes copied | 33,785,856 | 33,785,856 |

Enumeration took 9.23 ms. Peak native-benchmark process working set was 40.66 MiB. This does not include the Qt grid process. The initial separate probe returned a 108×192 thumbnail with 324-byte stride and 62,208 owned pixel bytes.

Both sweeps completed successfully, exit code 0. Raw measurements and command output remain in `.benchmarks/video-shell-cache.json` and `.benchmarks/video-shell-cache-run.log`.

First pass means a fresh benchmark process, **not an OS-cold-cache test**. One video was probed beforehand. The existing thumbnail cache was not cleared or populated. The repeat pass measures reuse of existing cached thumbnails; it is not an extraction retry. These results cover the 547 MP4 paths captured by the initial enumeration in this specific folder, not every video format or an uncached library. The later Qt run uses a separately recorded live-folder snapshot.

## Qt integration scope

The native loader accepts Shell items independently of file extension. The Qt chat extended the model/delegate and scheduler to a shared `MEDIA_SUFFIXES`/`MEDIA_EXTENSIONS` set including MP4 and other video suffixes. Pending video thumbnails remain undecorated; native failures propagate without icon substitution. No source decoder or alternative thumbnail provider was added. The 16-test suite passed, including video scheduling coverage, before the final isolated run.

## Final isolated Qt grid run

```powershell
.venv\Scripts\python.exe tools/benchmark_native_ui.py 'M:\X3\Catalog\Inspired\Jecay-Fansites\Francia_James.Francety.Brunette\video' --prefix video-native --no-screenshot
```

Run interval: **2026-10-31 17:40:00–17:40:04 America/Toronto** (21:40:00–21:40:04 UTC). Filename snapshots recorded 522 files at both start and end, with zero added/removed filenames during this run. Four subfolders account for the grid's 526 total items. This is a later corpus than the native benchmark's initial 547 paths; the two totals must not be presented as the same snapshot.

| Measurement | Final result |
| --- | ---: |
| Native grid requests / successes / failures | 187 / 187 / 0 |
| Non-null cached thumbnail icons after initial viewport load | 21 |
| Rendered viewport pixels, in memory | 2,043,090 |
| Initial navigation | 1,799.01 ms |
| First viewport thumbnail completion | 271.72 ms |
| Warm folder return | 34.65 ms |
| Eight rapid navigation requests | 80.25 ms |
| Scrolling event-loop gap p95 / maximum | 11.52 / 18.53 ms |
| Overall event-loop gap p95 / maximum | 12.05 / 25.88 ms |
| Maximum scrollbar setValue duration | 0.48 ms |
| Peak process working set | 152.16 MiB |
| Retained thumbnail pixel cache | 19.92 MiB |
| Peak active / pending requests | 2 / 35 |

The run exited **0**. The production adapter loaded actual cached video thumbnails into QImage/QIcon storage; the grid viewport was rendered in memory. No video screenshot was saved or displayed in the chat. This is programmatic rendering verification, not a visual review of private media. Because the grid schedules only visible/prefetched items, its 187 calls are not a second full-folder sweep.

The final timing run occurred after the native sweep and test suite completed. An earlier exploratory UI run overlapped tests and is excluded from this final table. Raw final evidence: `.benchmarks/video-native-ui-metrics.json` and `.benchmarks/video-native-ui-run.log`.

Scrolling timer gaps measure event-loop responsiveness, **not FPS or individual paint time**. OS cache state was not flushed. Warm return benefits from application/model caches. Initial navigation around 1.8 seconds remains an optimization opportunity. The cache-only contract guarantees neither thumbnail availability for future additions nor support for every video format; this successful real-folder validation establishes MP4 cache reuse on this machine.
