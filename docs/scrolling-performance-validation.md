# Scrolling performance investigation

Date: 2026-10-31. Windows, Python 3.12, PySide6/Qt 6.12.0, comtypes 1.4.17.

## Reproduced problem and profile evidence

The historical 10,000-item synthetic benchmark reported a 260.08 ms maximum scrolling heartbeat gap. Two fresh uninstrumented baseline runs reproduced the issue at **304.69 ms** and **275.14 ms**. The same benchmark directory and scroll sequence were retained throughout; the fixture was not relocated to avoid the slow path.

The detailed callback profiler changed timing enough to mask the stall (20.69 ms maximum), so that run was used only to inspect costs, not as evidence of improvement. A narrower event profile caught `DirectoryModel.event.MetaCall` at approximately 265 ms wall time and 265.625 ms CPU during scrolling. Thumbnail polling and painting were much smaller contributors.

An initial shared-filesystem-model change reduced duplication but did not solve the problem: uninstrumented runs still reached 128.35 and 127.49 ms. Follow-up traces identified current-folder reveal in the navigation tree enumerating the ancestor Temp directory: approximately 12,165 unrelated entries, delivered in large model batches (6,906 and 5,159 rows), plus 29,591 directory-filter calls. These ancestor updates and tree layout ran on the GUI thread during the scrolling interval. The problem was not thumbnail decoding, and disabling cache-only retrieval would not address it.

Baseline artifacts are preserved under `.benchmarks/scroll-before-*`. Intermediate shared-model measurements remain under `.benchmarks/scroll-after-*`; they must not be confused with the final optimized measurements.

## Implemented tree path and remeasurement

The final approach replaces the filesystem-model-backed navigation tree with `DirectoryTreeModel`: one worker scans and sorts directory records, and the GUI inserts/removes at most 128 rows per batch. The tree is lazy, retains drive/current-path navigation, and watches loaded directories for changes. Filesystem enumeration is not performed from paint/model-data callbacks. Thumbnail generation policy, provider, concurrency, and cache budget are unchanged.

Three uninstrumented 10,000-item runs with the original fixture location and scroll sequence measured:

| Measurement | Run 1 | Run 2 | Run 3 |
| --- | ---: | ---: | ---: |
| Maximum scrolling heartbeat gap | 13.07 ms | 13.92 ms | 16.33 ms |
| Initial navigation/window load | 3,290.93 ms | 3,287.55 ms | 3,153.28 ms |
| Warm navigation | 30.98 ms | 33.37 ms | 31.06 ms |
| Peak process working set | 162.35 MiB | 162.89 MiB | 166.89 MiB |

All three used at most two active and 35 pending thumbnail requests. Artifacts: `.benchmarks/scroll-tree-after-{1,2,3}-metrics.json` and matching logs. Startup in these preliminary repetitions was approximately 3.2 seconds versus 2.3–2.5 seconds in the two fresh baselines. The final-code run below was faster, but startup varies and remains a separate optimization opportunity. Overall event-loop delays outside the scrolling interval also remain larger than the scrolling figures.

The final exact-code uninstrumented run (`scroll-tree-final-metrics.json`) measured **14.87 ms maximum scrolling gap**, **43.32 ms warm navigation**, **2,168.71 ms initial navigation**, and **167.21 MiB peak working set**. The maximum overall heartbeat gap was 97.40 ms. Compared with the original 260.08 ms scrolling result, the measured scrolling gap fell by about **94%**. This is evidence for the tested workload, not a universal latency guarantee.

A final clean diagnostic run measured 15.31 ms maximum scrolling gap, with no ancestor filesystem-model updates during scrolling; the largest scrolling callback was an 8.56 ms window update. Earlier diagnostic logs had a profiler-only bug reading a Qt receiver's name after DeferredDelete. That diagnostic was corrected to capture the name before event delivery. Uninstrumented before/after measurements were unaffected; only the final clean profile is used to confirm the absence of the long callbacks.

## Independent real-video regression

After the Qt chat finished all tests and synthetic benchmarks, this chat ran:

```powershell
.venv\Scripts\python.exe tools/benchmark_native_ui.py 'M:\X3\Catalog\Inspired\Jecay-Fansites\Francia_James.Francety.Brunette\video' --prefix video-scroll-fix --no-screenshot
```

The run exited **0**. It used the production cache-only adapter, recorded 21 non-null cached icons, and rendered the viewport in memory without saving or displaying a media screenshot.

| Measurement | Result |
| --- | ---: |
| Native video requests / successes / failures | 191 / 191 / 0 |
| First viewport thumbnail completion | 251.34 ms |
| Warm folder return | 39.40 ms |
| Eight rapid navigation requests | 83.97 ms |
| Initial navigation/window creation | 1,922.98 ms |
| Scrolling heartbeat p95 / maximum | 11.29 / 17.11 ms |
| Overall heartbeat maximum | 29.63 ms |
| Peak process working set | 138.19 MiB |
| Retained thumbnail pixels | 14.95 MiB |
| Peak active / pending thumbnail requests | 2 / 35 |

The live folder continued changing between historical tests. During this run, **512 files plus four folders** were present. Filename snapshots at 2026-10-31 18:00:54–18:00:58 America/Toronto (22:00:54–22:00:58 UTC) had identical file sets: zero additions/removals during the measurement. Do not compare its file count directly with the historical 547-file native sweep or 522-file grid run as if they were identical corpora. Raw results: `.benchmarks/video-scroll-fix-ui-metrics.json` and `.benchmarks/video-scroll-fix-run.log`.

## Correctness and unchanged native behavior

The final suite passed **19 tests in 5.267 seconds**. New coverage includes directory-only tree rows, incremental addition/removal, current-path reveal and newest-target handling, and cancellation of queued scans for deleted descendants. A deleted-directory watcher event refreshes a surviving watched ancestor; it does not catch or retry a failed scan. Actual scan and thumbnail failures still propagate.

The native loader's SHA-256 was checked again after the video run and matches the pre-change value below. No generation flags, source decoders, icon fallbacks, or native thumbnail changes were introduced.

## Thumbnail contract

The Windows loader must remain unchanged: `IShellItemImageFactory::GetImage` with `SIIGBF_INCACHEONLY | SIIGBF_THUMBNAILONLY` (`0x18`), no extraction, no source decoding, no icon fallback, and native failures surfaced. The loader's pre-change SHA-256 is `46D9B13A00BBB3FC4188F151FA3B02FF792721C48CE760FD12BC06D22B307DF7`.

## Measurement interpretation

The synthetic 10,000-item test isolates UI/model behavior with a test-only image callable; it does not validate Windows thumbnail throughput. The separate real video-folder run uses only the production Shell adapter. Timed workloads are run separately from each other and the automated test suite. Heartbeat gaps measure event-loop availability, not individual paint time or FPS. No OS cache flush is performed, so first-process/first-navigation timings are not OS-cold-cache claims.
