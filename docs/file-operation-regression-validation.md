# File-operation regression validation

Validated on Windows, 2026-11-01, with Python 3.12 and PySide6 6.12.

The final full suite passed all 116 tests. Changelog headings, dates, categories, version order, and `git diff --check` also passed.

## Regressions corrected

- Clipboard action updates expanded the same selection multiple times. A profiled 10,000-item selection took 1,079–1,099 ms. Action availability now uses selection presence; paths are expanded when executing commands. The same benchmark took 0.30–0.57 ms after the change.
- Move drag hover checks scanned every source on each mouse movement. Source and parent sets are built on drag entry; hover checks inspect only destination ancestors. Both sets are released on drop or drag leave.
- Suppressing a press to preserve a selected drag batch also suppressed ordinary clicks. Selected-item presses are deferred until release when no drag occurs, preserving Qt's single-click and double-click behavior.
- Post-action refresh could scan a moved-away cached directory. The action worker identifies surviving refresh directories, and the GUI invalidates removed listings. Moving the current folder navigates to its parent.
- `shutil.move` could retry a failed rename as a copy, including overwriting a newly appeared destination. Moves now use explicit same-volume rename/replace or cross-volume copy-then-remove; filesystem failures propagate.

## Measurements

Interaction benchmarks use real files, synthetic thumbnails, and offscreen Qt. Selection measurements include cProfile overhead. These are three selection samples and 100 hover events, not a latency guarantee.

| 50,000-item interaction | Measured |
| --- | ---: |
| Profiled selection range | 0.34–0.85 ms |
| Move hover median / p95 / maximum | 0.043 / 0.067 / 0.176 ms |
| Link hover median / p95 / maximum | 0.011 / 0.013 / 0.077 ms |

The separate 50,000-image UI run used real Windows Shell thumbnails from generated 256×192 PNG files, with offscreen Qt. Cold means the first model visit and empty application cache; the Windows disk and Shell caches were not flushed.

| UI measurement | Measured |
| --- | ---: |
| Initial navigation | 3,659 ms |
| First 12 thumbnails | 426 ms |
| Warm navigation | 25.2 ms |
| 20 rapid navigation requests | 205.8 ms |
| Maximum scrolling event-loop gap | 15.4 ms |
| Maximum scrollbar update | 0.38 ms |
| Peak process working set | 255.5 MiB |
| Cached thumbnail pixels | 3.61 MiB |
| Peak active / queued thumbnail requests | 2 / 35 |

These measurements establish the selection improvement and exercise navigation, scrolling, thumbnail scheduling, and memory at scale. They do not establish an improvement in native window rendering or cold OS-cache throughput.

## Reproduction

From the repository root, set `QT_QPA_PLATFORM=offscreen` and `PYTHONPATH=.`:

```powershell
.venv/Scripts/python.exe -m unittest discover -s tests
.venv/Scripts/python.exe tools/benchmark_interactions.py --items 10000 --prefix regression-after
.venv/Scripts/python.exe tools/benchmark_interactions.py --items 50000 --prefix regression-50k
.venv/Scripts/python.exe tools/benchmark_ui.py --items 50000 --prefix regression-ui-50k --native-thumbnails
```

Detailed profiles and metrics are written to the ignored `.benchmarks` directory. Tests cover shared conflict choices, copy-source preservation, cut clipboard lifetime, folder/background/tree paste, text shortcut isolation, move drops, selection mode, click activation, moved-folder refresh, rename races, and the cross-volume branch. Cross-volume tests simulate differing device IDs; the benchmark uses local storage.
