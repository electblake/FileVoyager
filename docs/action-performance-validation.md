# Action and drag performance validation

Measured on Windows on 2026-11-01, using the local Python 3.12 / PySide6 6.12 environment.

## Changes

- Used compact `QItemSelection` ranges for selected-row counts instead of repeatedly creating a `QModelIndex` for every selected row.
- Iterated selected rows lazily where an action needs to examine items. Flatten availability stops at the first file; similarity-reference detection stops at the second file. A folder plus one file still uses that file as the reference.
- Retrieved only the first selected row when previewing a selection whose current item is no longer selected.
- Parsed local drag URLs once on entry, retained their paths for that drag, and released them on drop or leaving the view. Mouse movement checks the destination and modifiers without rereading the payload. Alt still selects Qt's native link action; copy and move remain unavailable.
- Retained the existing worker-thread filesystem actions, model/view rendering, bounded thumbnail queue and cache, and incremental updates.

Qt documents selection ranges as a way to [save memory and avoid unnecessary work](https://doc.qt.io/qt-6/qitemselection.html). The implementation follows that representation rather than keeping a second per-item selection cache.

## Reproduction

Run from the repository root with `QT_QPA_PLATFORM=offscreen`:

```powershell
uv run python tools/benchmark_interactions.py --items 10000 --prefix actions-after
uv run python tools/benchmark_ui.py --items 10000 --prefix actions-ui-after
uv run python tools/benchmark_interactions.py --items 50000 --prefix actions-50k-after
uv run python tools/benchmark_ui.py --items 50000 --prefix actions-ui-50k-after
```

The interaction benchmark creates real files and selects a contiguous range containing one directory and all image files. It profiles three selection operations, then measures 100 drag moves with one URL per file. Selection timings include cProfile overhead on both sides of the comparison; they are not uninstrumented end-user latency estimates. Drag timings are unprofiled. Detailed profiles and JSON metrics are written to the ignored `.benchmarks` directory.

The UI benchmark measures a first visit with an empty application thumbnail cache, first thumbnails, scrolling, a return visit with a warm application cache, memory, and thumbnail queue bounds. Cold does not mean a flushed Windows disk cache. The added rapid-navigation phase issues 20 alternating navigation requests and waits for the final directory and its layout to settle.

## 10,000-item comparison

| Measurement | Before | After |
| --- | ---: | ---: |
| Profiled selection median, three samples | 131.51 ms | 0.14 ms |
| Profiled selection range | 130.64–133.65 ms | 0.13–0.41 ms |
| Drag move median | 4.42 ms | 0.010 ms |
| Drag move p95 | 5.87 ms | 0.013 ms |
| Drag move maximum | 20.43 ms | 0.067 ms |
| Initial navigation | 1,503 ms | 1,648 ms |
| First 12 synthetic thumbnails | 225 ms | 211 ms |
| Warm navigation | 25.38 ms | 23.20 ms |
| Maximum scrolling event-loop gap | 11.67 ms | 11.64 ms |
| Peak working set | 211.49 MiB | 207.84 MiB |
| Peak active / queued thumbnail requests | 2 / 35 | 2 / 35 |

The selection profile went from 150,353 function calls to 514 over the measured select/clear sequence. The baseline spent 236 ms in 27 calls to `selectedRows`; the optimized selection handlers do not call it. The changes specifically improve selection and drag-move cost. The first-visit result was slower, so these runs do not establish an improvement in startup or cold navigation.

## 50,000-item scale check

Profiled selection took 0.18–0.45 ms (median 0.21 ms). Drag moves took 0.0088 ms median, 0.0116 ms p95, and 0.0892 ms maximum.

The first uninstrumented UI run measured 6,863 ms initial navigation, 753 ms to the first 12 thumbnails, 30.80 ms warm navigation, and 250.22 ms for 20 rapid navigation requests. Peak working set was 277.18 MiB, with 5.81 MiB retained thumbnail pixels and two active / 35 pending requests. Maximum scrolling event-loop gap was 48.20 ms; the overall maximum was 516.84 ms. These pauses remain limitations of this run and are not hidden by the selection/drag improvements.

A callback-instrumented diagnostic run measured an 11.98 ms maximum scrolling gap and contained no individual scrolling callbacks over 5 ms. Instrumentation changes scheduling, so that run alone cannot establish that the larger pause was fixed.

A second uninstrumented confirmation run measured 26.31 ms maximum scrolling gap, 36.46 ms warm navigation, 219.28 ms for rapid navigation, and 277.29 MiB peak working set. Initial navigation took 8,251 ms and the overall maximum event-loop gap was 697.05 ms. No rendering or filesystem-model changes were made between these runs. Large-folder initial loading and occasional scrolling pauses remain unisolated; this work does not claim to eliminate them.

## Limits and regression coverage

These benchmarks use synthetic thumbnails and offscreen Qt. They do not measure native Shell thumbnail throughput, image decoding, visible compositor frame time, network folders, or the duration of filesystem copies/merges. Event-loop gaps are a responsiveness proxy, not frame times. Sparse selections with many ranges and selections containing only folders still require more work than the contiguous image selection measured here.

Regression tests exercise multi-selection, shortening/reversing Shift ranges, renaming, menu targets, folder merges, native `.lnk` creation, modifier/cursor-action changes, drag payload reuse, and action/reference state after selection changes. The new large-selection check rejects calls that expand all selected rows in the UI update handlers.

All 75 tests passed in 10.176 seconds after the application changes. No commit or release was created.
