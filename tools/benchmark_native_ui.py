"""Exercise the real Shell thumbnail service and Qt event loop against existing files.

uv run python tools/benchmark_native_ui.py "C:\\Users\\shoji\\Pictures\\Screenshots"
Windows generates missing thumbnails; no application decoder or alternate provider.
"""

import argparse
import ctypes
from ctypes import wintypes
import json
import os
from datetime import datetime, timezone
from pathlib import Path
import time

from PySide6.QtCore import QSettings, QTimer
from PySide6.QtWidgets import QApplication

from filevoyager.shell_bridge import load_thumbnail_image
from filevoyager.window import ExplorerWindow
from filevoyager.preferences import FolderPreferences


class MemoryCounters(ctypes.Structure):
    _fields_ = [("cb", wintypes.DWORD), ("PageFaultCount", wintypes.DWORD)] + [
        (name, ctypes.c_size_t) for name in (
            "PeakWorkingSetSize", "WorkingSetSize", "QuotaPeakPagedPoolUsage",
            "QuotaPagedPoolUsage", "QuotaPeakNonPagedPoolUsage", "QuotaNonPagedPoolUsage",
            "PagefileUsage", "PeakPagefileUsage")]


class NativeBenchmark:
    def __init__(self, app, path, prefix="native", capture_screenshot=True):
        self.app = app
        self.path = str(Path(path).resolve(strict=True))
        self.prefix = prefix
        self.capture_screenshot = capture_screenshot
        with os.scandir(self.path) as entries:
            self.start_names = frozenset(entry.name for entry in entries if entry.is_file())
        self.snapshot_started = datetime.now(timezone.utc).isoformat()
        self.phase = "opening"
        self.beats = []
        self.scroll_beats = []
        self.scroll_calls = []
        self.results = []
        self.started = time.perf_counter()
        self.metrics = {"scope": "Real Shell service with Windows generation; first visit is not an OS cold-cache flush",
                        "folder": self.path}
        preferences = FolderPreferences(QSettings(str(Path(".benchmarks") / f"{prefix}-settings.ini"), QSettings.Format.IniFormat))
        preferences.save(self.path, {"view": "details", "size": 128, "grid": [0, 0], "details": [0, 0]})
        self.window = ExplorerWindow(self.path, load_thumbnail_image, preferences=preferences)
        self.window.thumbnails.requestFinished.connect(self.results.append)
        self.window.files.directoryLoaded.connect(self.directory_loaded)
        self.loaded = set()
        self.window.show()
        self.heartbeat = QTimer()
        self.heartbeat.setInterval(10)
        self.heartbeat.timeout.connect(self.beat)
        self.heartbeat.start()
        self.tick_timer = QTimer()
        self.tick_timer.setInterval(20)
        self.tick_timer.timeout.connect(self.tick)
        self.tick_timer.start()

    def directory_loaded(self, path):
        self.loaded.add(str(Path(path)))

    def beat(self):
        now = time.perf_counter()
        self.beats.append(now)
        if self.phase == "scrolling":
            self.scroll_beats.append(now)

    def settled(self):
        controller = self.window.thumbnails
        return (not controller.active and not controller.pending
                and not controller.refresh_timer.isActive())

    def tick(self):
        now = time.perf_counter()
        if self.phase == "opening" and self.path in self.loaded:
            self.metrics["initial_navigation_ms"] = round((now - self.started) * 1000, 2)
            self.metrics["items"] = self.window.model.rowCount(self.window.details.rootIndex())
            self.phase = "first_grid"
            self.grid_started = now
            self.window.switch_view(self.window.grid)
        elif self.phase == "first_grid" and self.settled():
            self.metrics["first_viewport_thumbnails_ms"] = round((now - self.grid_started) * 1000, 2)
            self.metrics["first_viewport_cached_icons"] = sum(
                not icon.isNull() for icon, _ in self.window.cache.entries.values())
            rendered = self.window.grid.viewport().grab()
            self.metrics["rendered_viewport_pixels"] = rendered.width() * rendered.height()
            self.output = Path(".benchmarks")
            self.output.mkdir(exist_ok=True)
            if self.capture_screenshot:
                self.window.grab().save(str(self.output / f"{self.prefix}-grid.png"))
            self.fractions = iter([.1, .2, .4, .7, 1.0, .8, .3, 0.0])
            self.scroll_steps = 0
            self.last_scroll = now
            self.phase = "scrolling"
        elif self.phase == "scrolling" and now - self.last_scroll >= .2:
            if self.scroll_steps < 8:
                fraction = next(self.fractions)
                start = time.perf_counter()
                bar = self.window.grid.verticalScrollBar()
                bar.setValue(int(bar.maximum() * fraction))
                self.scroll_calls.append((time.perf_counter() - start) * 1000)
                self.last_scroll = now
                self.scroll_steps += 1
            elif self.settled():
                self.window.switch_view(self.window.details)
                self.window.navigate(str(Path(self.path).parent))
                self.phase = "parent"
        elif self.phase == "parent" and self.window.current_path == str(Path(self.path).parent):
            self.warm_started = now
            self.window.navigate(self.path)
            self.phase = "warm"
        elif self.phase == "warm" and self.window.current_path == self.path:
            self.metrics["warm_navigation_ms"] = round((now - self.warm_started) * 1000, 2)
            self.window.switch_view(self.window.grid)
            self.phase = "warm_grid"
        elif self.phase == "warm_grid" and self.settled():
            self.rapid_started = now
            for target in [str(Path(self.path).parent), self.path] * 4:
                self.window.navigate(target)
            self.phase = "rapid"
        elif (self.phase == "rapid" and self.window.navigation_future is None
              and self.window.navigation_pending is None and self.settled()):
            self.metrics["rapid_8_requests_ms"] = round((now - self.rapid_started) * 1000, 2)
            self.finish()

    def finish(self):
        with os.scandir(self.path) as entries:
            end_names = frozenset(entry.name for entry in entries if entry.is_file())
        snapshot_ended = datetime.now(timezone.utc).isoformat()
        counters = MemoryCounters()
        counters.cb = ctypes.sizeof(counters)
        kernel = ctypes.WinDLL("kernel32")
        kernel.GetCurrentProcess.restype = wintypes.HANDLE
        kernel.K32GetProcessMemoryInfo.argtypes = [wintypes.HANDLE, ctypes.POINTER(MemoryCounters), wintypes.DWORD]
        assert kernel.K32GetProcessMemoryInfo(kernel.GetCurrentProcess(), ctypes.byref(counters), counters.cb)
        gaps = sorted((b - a) * 1000 for a, b in zip(self.beats, self.beats[1:]))
        scroll_gaps = sorted((b - a) * 1000 for a, b in zip(self.scroll_beats, self.scroll_beats[1:]))
        self.metrics.update({
            "snapshot_start_utc": self.snapshot_started,
            "snapshot_end_utc": snapshot_ended,
            "snapshot_start_files": len(self.start_names),
            "snapshot_end_files": len(end_names),
            "files_added_during_run": len(end_names - self.start_names),
            "files_removed_during_run": len(self.start_names - end_names),
            "final_items": self.window.model.rowCount(self.window.grid.rootIndex()),
            "event_loop_gap_p95_ms": round(gaps[int(len(gaps) * .95)], 2),
            "event_loop_gap_max_ms": round(max(gaps), 2),
            "scroll_event_loop_gap_p95_ms": round(scroll_gaps[int(len(scroll_gaps) * .95)], 2),
            "scroll_event_loop_gap_max_ms": round(max(scroll_gaps), 2),
            "scroll_set_value_max_ms": round(max(self.scroll_calls), 2),
            "peak_working_set_mib": round(counters.PeakWorkingSetSize / 1048576, 2),
            "cached_pixels_mib": round(self.window.cache.bytes_used / 1048576, 2),
            "native_attempts": len(self.results),
            "native_successes": sum(future.exception() is None for future in self.results),
            "native_failures": sum(future.exception() is not None for future in self.results),
            "peak_active_requests": self.window.thumbnails.peak_active,
            "peak_pending_requests": self.window.thumbnails.peak_pending,
        })
        (self.output / f"{self.prefix}-ui-metrics.json").write_text(json.dumps(self.metrics, indent=2), encoding="utf-8")
        print(json.dumps(self.metrics, indent=2), flush=True)
        self.tick_timer.stop()
        self.heartbeat.stop()
        self.window.close()
        self.app.quit()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder")
    parser.add_argument("--prefix", default="native")
    parser.add_argument("--no-screenshot", action="store_true")
    args = parser.parse_args()
    app = QApplication([])
    benchmark = NativeBenchmark(app, args.folder, args.prefix, not args.no_screenshot)
    app.exec()
    # Qt logs slot exceptions and continues its event loop. Re-observe the exact
    # completed futures after the measurement so a failed native run exits nonzero.
    for future in benchmark.results:
        future.result()


if __name__ == "__main__":
    main()
