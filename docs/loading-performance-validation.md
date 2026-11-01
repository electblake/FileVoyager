# 50,000-item loading and scrolling validation

Measured on Windows, Python 3.12 / PySide6 6.12, on 2026-11-01.

## Causes and changes

The native `QFileSystemModel` delivered several GUI-thread callbacks lasting
439–497 ms during initial loading. Their profiles contained almost no Python
work. Inspection of Qt's filesystem model implementation confirmed that its
collated directory sorting runs in the model thread. There is no public batch-size
control for that sort.

The file listing now uses `QAbstractItemModel` with a single scan/sort worker.
The worker reads cached `os.scandir` metadata, uses `QCollator` for natural name
sorting, formats dates, and computes changes. The GUI publishes at most 512 rows
per timer turn through Qt's insert/remove/data-change notifications. Persistent
indexes survive sorting; four recent directory snapshots are retained. Watcher
updates, renaming during publication, and cache eviction are covered by tests.
Filesystem reads and sorting do not occur in `data()` or painting.

Details now uses a fixed-row-height `QTableView`. The previous tree view repeatedly
laid out a flat listing during incremental insertion. The thumbnail grid retains
Qt's batched layout, uniform geometry, and lightweight delegate.

The scrolling trace also isolated a folder-tree timer callback comparing roughly
13,000 sibling directories, including 26,340 path normalizations, on the GUI
thread. That comparison now runs in the existing folder scan worker. GUI work is
limited to applying the resulting incremental row changes.

This follows Qt's [model thread ownership rules](https://doc.qt.io/qt-6/qabstractitemmodel.html#thread-safety):
workers prepare ordinary data; model APIs and notifications remain on the GUI
thread. Details uses the standard [Qt table view](https://doc.qt.io/qt-6/qtableview.html).
There are no per-file widgets, additional thumbnail providers, or error recovery paths.

## Repeat measurements

These are uninstrumented, offscreen runs with 50,000 actual directory entries and
synthetic thumbnail images. Before values are the two runs recorded in
`action-performance-validation.md`; after values are `loading-after-1` and
`loading-after-2`. They use the same benchmark stages. Timing varies with system
load and ancestor-folder enumeration; these ranges are observations, not statistical
confidence intervals.

| Measurement | Before, two runs | After, two runs |
| --- | ---: | ---: |
| Initial listing | 6.86–8.25 s | 5.09–5.36 s |
| Maximum event-loop gap | 517–697 ms | 50–53 ms |
| Maximum scrolling gap | 26–48 ms | 15–18 ms |
| Warm return navigation | 31–36 ms | 21–25 ms |
| 20 rapid navigation requests, final layout settled | 219–250 ms | 427–480 ms |
| Peak working set | 277 MiB | 237–244 MiB |
| Active / queued thumbnail requests | 2 / 35 | 2 / 35 |

The first twelve synthetic thumbnails arrived in 516–521 ms after switching to
the grid. Scrolling setters took at most 0.20 ms. Rapid-navigation completion
regressed in these initial runs, despite improved maximum event-loop gaps. The
pre-commit follow-up below addresses that regression.

## Real Windows thumbnail service

`loading-native-50k` used 50,000 generated, valid 256×192 PNG files and the production
Windows Shell thumbnail service. It measured:

- Initial listing: 6.57 s; first twelve thumbnails after grid switch: 696 ms.
- Maximum scrolling event-loop gap: 15.91 ms; overall maximum: 101.81 ms.
- Warm navigation: 30.22 ms; 20 rapid requests: 428.93 ms.
- Peak working set: 254.40 MiB; retained thumbnail pixels: 3.84 MiB.
- 82 completed thumbnail requests; maximum two active and 35 queued.

This validates the production thumbnail path at 50,000 entries, but the generated
small PNGs do not represent decoding costs for large photographs, mixed codecs,
network shares, or damaged files. Cold means a first model visit and empty application
thumbnail cache, not a flushed Windows filesystem/Shell cache. Event-loop gaps are
a responsiveness proxy, not compositor frame times. The measured pauses are reduced,
not eliminated.

## Reproduction

From the repository root:

```powershell
$env:QT_QPA_PLATFORM='offscreen'
uv run python tools/benchmark_ui.py --items 50000 --prefix loading-after
uv run python tools/benchmark_ui.py --items 50000 --native-thumbnails --prefix loading-native
uv run python tools/benchmark_ui.py --items 50000 --profile-events --prefix loading-diagnostic
uv run python tools/benchmark_interactions.py --items 50000 --prefix loading-actions
uv run python -m unittest discover -s tests -v
```

The benchmark creates and removes its own temporary fixtures and writes metrics,
screenshots, and optional callback profiles under `.benchmarks`. Instrumented runs
are diagnostic only: profiling changes scheduling and significantly increases
callback timings. `QAbstractItemModelTester` checks the new model's index and
notification contracts during regression tests.

At the initial checkpoint, all 82 tests passed in 15.178 seconds. Coverage includes watcher metadata changes,
natural sorting with persistent selection, cache eviction (including empty folders),
rename during row publication, worker-thread tree comparisons, and a drive reveal
racing its initial scan, alongside the existing application tests.

The 50,000-item action check measured profiled selection at 0.67–1.10 ms and drag
movement at 0.0124 ms median / 0.0154 ms p95 / 0.0958 ms maximum. Selection is slower
than the previous native-model measurement, but remains around one millisecond in
this contiguous-selection scenario.

## Pre-commit navigation follow-up

The new Python model rebuilt identical Qt flag combinations for every item during
grid layout. It now retains those immutable flag values and checks index bounds
without repeated C++/Python `hasIndex` virtual calls. The grid also preserves its
layout when its root and thumbnail size are unchanged, and uses Qt's batched
layout with 512 items per turn. A regression test verifies that reopening the
current grid preserves its scroll position without invoking another item layout.

The final synthetic run (`loading-final-batch512`, 50,000 items) measured:

| Measurement | Final |
| --- | ---: |
| Initial listing | 5.67 s |
| First twelve thumbnails | 425 ms |
| Maximum event-loop gap | 48.34 ms |
| Maximum scrolling gap | 14.02 ms |
| Warm navigation | 28.98 ms |
| Twenty rapid requests, final layout settled | 217.02 ms |
| Peak working set | 237.03 MiB |

Rapid navigation returned to the original 219–250 ms baseline, while retaining
the reduced loading and scrolling pauses. Intermediate runs with cached flags but
the smaller layout batch ranged from 202–285 ms, so individual timings should not
be treated as guarantees. Total initial listing time also varied with system load
(5.19–7.16 s in those intermediate runs); improved responsiveness is the more
consistent outcome.

The final real-Shell run (`loading-commit-native`) measured 6.18 s initial loading,
637 ms to twelve thumbnails, 28.91 ms warm navigation, and 290.25 ms for rapid
requests (previous native run: 428.93 ms). Its maximum overall gap was 97.59 ms,
with a 38.41 ms scrolling outlier and 261.82 MiB peak working set. Native scrolling
therefore varied between runs; the earlier 15.91 ms result is not a guaranteed
upper bound. This work removes the identified synchronous sort/comparison costs,
but does not establish consistently frame-perfect native-thumbnail scrolling.

Final validation: all 83 tests passed in 14.601 seconds, including the new
unchanged-grid navigation regression. Changelog headings, categories, dates, and
version ordering were validated, and `git diff --check` passed.
