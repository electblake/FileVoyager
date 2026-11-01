# Folder shortcut regression validation

Validated on Windows on 2026-11-01 for FileVoyager 0.4.0.

## Behavior reviewed and corrected

- Folder shortcuts open from Details and Grid and expand lazily in the tree.
  Tree branch identity is separate from the real filesystem path, so two links
  to one target can expand independently. A link back to an ancestor is not
  recursively enumerated until the user expands each level.
- Opening a child from the content view, Back/Forward, and Up preserve the
  selected shortcut branch. Completed tree reveals no longer reselect an old row
  when an unrelated scan finishes.
- Retargeting a shortcut replaces its old subtree, releases its old watch, and
  updates the content view. F5 refreshes the current listing and watched tree
  branches. Removing one alias leaves other aliases' watches active.
- Paste and drop destinations use the target folder. Rename, cut, copy, drag
  sources, and packing use the shortcut file. Tree Flatten and Join actions are
  disabled on shortcut files, matching the content views.
- Shortcut targets are cached as strings with a 4,096-entry LRU bound. Keys
  include the absolute shortcut path, nanosecond modification time, and size.
  Each scan still stats the shortcut and its target. COM objects are created and
  released on scan workers, never stored in the cache or accessed during paint.
  Native failures remain visible; no recovery provider or missing-target
  substitution was added.

The existing suite initially passed 118 tests despite the gaps above. All 121
tests in the final suite passed in 29.2 seconds. The expanded suite covers retargeting, actual paste operations, drop destination and
source identity, rename identity, worker/cache behavior, duplicate and cyclic
branches, watcher updates, Details/Grid double-clicks, and branch-preserving
navigation. Broader coverage includes file operations, clipboard/drag behavior,
themes, selection, sorting, preview/video, similarity, native thumbnails,
installer bootstrap lifecycle, and update handoff.

## Shortcut scans

`tools/benchmark_shortcuts.py` creates 1,000 real `.lnk` files and scans them on a
single worker. Before measurements used the original uncached implementation
from this change; after measurements use the final bounded cache. The tree scan
runs after the file scan and therefore shares its cached target strings.

| Scan | Before | After |
| --- | ---: | ---: |
| First file-list scan | 4,916 ms | 5,052 ms |
| Repeat file-list scans | 5,912â€“6,609 ms | 40â€“42 ms |
| Tree scans after file-list scans | 5,220â€“6,430 ms | 29â€“36 ms |

The first visit still pays Windows shortcut-loading cost; these results do not
claim improved first-scan latency. Repeat scans no longer reload every unchanged
shortcut. The cache is shared by the tree and listing workers.

## Large-folder and native thumbnail measurements

`tools/benchmark_ui.py --items 50000` uses 50,000 actual filesystem entries with
synthetic images to isolate model/view work. The table compares consecutive
unprofiled runs of release 0.3.0 and the final implementation. Earlier overlapping
runs were excluded from this comparison. OS disk caches were not flushed.

| Metric | 0.3.0 | 0.4.0 |
| --- | ---: | ---: |
| Initial listing | 3,443 ms | 3,649 ms |
| First 12 thumbnails | 295 ms | 311 ms |
| Warm navigation | 26 ms | 31 ms |
| 20 rapid navigation requests | 176 ms | 456 ms |
| Maximum scrolling heartbeat gap | 12.83 ms | 10.91 ms |
| Peak working set | 238.97 MiB | 258.13 MiB |
| Active / queued thumbnail peaks | 2 / 35 | 2 / 35 |

Navigation timing and process working set varied between runs. Investigation of
the slower rapid-navigation result with event profiling measured 236 ms for that
phase; its only callback exceeding 5 ms was a 6.28 ms grid timer. No new long
tree/model callback was found in that phase. These workload samples establish
bounded queues and responsive scrolling, not statistically proven latency or
memory equivalence. The new shortcut/tree metadata has a memory cost.

`--items 1000 --native-thumbnails` additionally exercised real Shell generation
from generated PNG files: 105 thumbnails completed, 12.36 ms maximum scrolling
heartbeat gap, 24.54 ms warm navigation, 40.26 ms for 20 rapid requests, and
213.68 MiB peak working set. Active/queued work remained at 2/35. This does not
measure every installed Shell extension or network destination.

Detailed JSON, logs, screenshots, and the profiled callbacks are stored locally
under `.benchmarks/release-040-*`. The release remains unsigned. Full Setup
execution and upgrade/uninstall testing of the user's active installation were
not performed; packaging verification uses build/content checks and the isolated
bootstrap tests.
