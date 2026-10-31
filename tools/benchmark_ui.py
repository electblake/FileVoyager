"""Synthetic UI benchmark. Does not exercise or replace Windows thumbnail retrieval.

Run: uv run python tools/benchmark_ui.py --items 10000
"""

import argparse
import ctypes
from ctypes import wintypes
import json
from pathlib import Path
import tempfile
import time
from collections import defaultdict

from PySide6.QtCore import QEventLoop, QSettings, QTimer
from PySide6.QtGui import QColor, QImage
from PySide6.QtWidgets import QApplication

from filevoyager.window import ExplorerWindow
from filevoyager.grid import GridDelegate, ThumbnailGrid
from filevoyager.models import FileModel
from filevoyager.directory_tree import DirectoryTreeModel
from filevoyager.thumbnails import ThumbnailController
from filevoyager.preferences import FolderPreferences


class CallbackProfile:
    def __init__(self):
        self.phase = "startup"
        self.started = time.perf_counter()
        self.totals = defaultdict(lambda: {"calls": 0, "total_ms": 0.0, "max_ms": 0.0})
        self.slow = []
        self.model_events = []

    def record(self, name, started, cpu_started):
        duration = (time.perf_counter() - started) * 1000
        cpu = (time.process_time() - cpu_started) * 1000
        key = self.phase + ":" + name
        total = self.totals[key]
        total["calls"] += 1
        total["total_ms"] += duration
        total["max_ms"] = max(total["max_ms"], duration)
        if duration >= 5:
            self.slow.append({"phase": self.phase, "callback": name,
                              "at_ms": (started - self.started) * 1000,
                              "duration_ms": duration, "process_cpu_ms": cpu})

    def instrument(self, cls, name):
        original = getattr(cls, name)

        def measured(instance, *args, **kwargs):
            started, cpu_started = time.perf_counter(), time.process_time()
            result = original(instance, *args, **kwargs)
            self.record(cls.__name__ + "." + name, started, cpu_started)
            return result

        setattr(cls, name, measured)


class ProfileApplication(QApplication):
    def __init__(self, profile):
        self.profile = profile
        super().__init__([])

    def notify(self, receiver, event):
        started, cpu_started = time.perf_counter(), time.process_time()
        name = type(receiver).__name__ + ":" + receiver.objectName() + ".event." + event.type().name
        result = super().notify(receiver, event)
        self.profile.record(name, started, cpu_started)
        return result


class MemoryCounters(ctypes.Structure):
    _fields_ = [("cb", wintypes.DWORD), ("PageFaultCount", wintypes.DWORD)] + [
        (name, ctypes.c_size_t) for name in (
            "PeakWorkingSetSize", "WorkingSetSize", "QuotaPeakPagedPoolUsage",
            "QuotaPagedPoolUsage", "QuotaPeakNonPagedPoolUsage", "QuotaNonPagedPoolUsage",
            "PagefileUsage", "PeakPagefileUsage")]


def synthetic_image(path, width, height):
    number = int(Path(path).stem.split("-")[-1])
    image = QImage(width, height, QImage.Format.Format_ARGB32_Premultiplied)
    image.fill(QColor.fromHsv(number * 37 % 360, 100, 155))
    return image


def wait_for(condition, seconds=30):
    loop = QEventLoop()
    timer = QTimer()
    timer.setInterval(5)
    timer.timeout.connect(lambda: loop.quit() if condition() else None)
    timeout = QTimer()
    timeout.setSingleShot(True)
    timeout.timeout.connect(loop.quit)
    timer.start()
    timeout.start(round(seconds * 1000))
    loop.exec()
    timer.stop()
    timeout.stop()
    assert condition(), "Benchmark condition timed out"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--items", type=int, default=10000)
    parser.add_argument("--prefix", default="ui")
    parser.add_argument("--profile-callbacks", action="store_true")
    args = parser.parse_args()
    profile = CallbackProfile()
    if args.profile_callbacks:
        for cls, names in [(GridDelegate, ["paint", "sizeHint"]),
                           (ThumbnailGrid, ["candidate_rows", "scrollContentsBy"]),
                           (ThumbnailController, ["refresh", "poll"]),
                           (DirectoryTreeModel, ["apply_batch", "poll"]),
                           (FileModel, ["fileInfo", "filePath", "isDir"])]:
            for name in names:
                profile.instrument(cls, name)
        app = ProfileApplication(profile)
    else:
        app = QApplication([])
    output = Path(".benchmarks")
    output.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="filevoyager-bench-") as temp:
        first = Path(temp) / "Large image folder"
        second = Path(temp) / "Another folder"
        first.mkdir()
        second.mkdir()
        for number in range(args.items):
            (first / f"photo-{number:05}.png").touch()
        for number in range(100):
            (second / f"photo-{number:05}.png").touch()
        beats = []
        timer = QTimer()
        timer.setInterval(10)
        timer.timeout.connect(lambda: beats.append(time.perf_counter()))
        timer.start()
        start = time.perf_counter()
        preferences = FolderPreferences(QSettings(str(Path(temp) / "benchmark.ini"), QSettings.Format.IniFormat))
        preferences.save(str(first), preferences.load(str(first), False))
        window = ExplorerWindow(str(first), synthetic_image, preferences=preferences)
        window.tree.setObjectName("folder-tree")
        window.details.setObjectName("details")
        if args.profile_callbacks:
            def record_rows(kind, parent, first, last):
                profile.model_events.append({"event": kind, "phase": profile.phase,
                    "at_ms": (time.perf_counter() - profile.started) * 1000,
                    "path": window.files.filePath(parent), "first": first, "last": last})
            window.files.rowsAboutToBeInserted.connect(
                lambda parent, first, last: record_rows("before-insert", parent, first, last))
            window.files.rowsInserted.connect(
                lambda parent, first, last: record_rows("after-insert", parent, first, last))
            window.files.directoryLoaded.connect(lambda path: profile.model_events.append({
                "event": "loaded", "phase": profile.phase, "path": path,
                "at_ms": (time.perf_counter() - profile.started) * 1000}))
        window.show()
        wait_for(lambda: window.current_path == str(first)
                 and window.model.rowCount(window.details.rootIndex()) == args.items)
        cold_navigation_ms = (time.perf_counter() - start) * 1000
        window.grab().save(str(output / f"{args.prefix}-details.png"))
        profile.phase = "first-grid"
        start = time.perf_counter()
        window.switch_view(window.grid)
        wait_for(lambda: window.thumbnails.completed >= 12)
        first_thumbnails_ms = (time.perf_counter() - start) * 1000
        wait_for(lambda: not window.thumbnails.active and not window.thumbnails.pending)
        window.grab().save(str(output / f"{args.prefix}-grid.png"))
        profile.phase = "scroll"
        scroll_start = len(beats)
        scroll_calls = []
        for fraction in [0.1, 0.2, 0.4, 0.7, 1.0, 0.8, 0.3, 0.0]:
            start = time.perf_counter()
            window.grid.verticalScrollBar().setValue(int(window.grid.verticalScrollBar().maximum() * fraction))
            scroll_calls.append((time.perf_counter() - start) * 1000)
            scroll_loop = QEventLoop()
            QTimer.singleShot(100, scroll_loop.quit)
            scroll_loop.exec()
        scroll_beats = beats[scroll_start:]
        profile.phase = "warm-navigation"
        window.navigate(str(second))
        wait_for(lambda: window.current_path == str(second))
        start = time.perf_counter()
        window.navigate(str(first))
        wait_for(lambda: window.current_path == str(first)
                 and window.model.rowCount(window.grid.rootIndex()) == args.items)
        warm_navigation_ms = (time.perf_counter() - start) * 1000
        wait_for(lambda: not window.thumbnails.active and not window.thumbnails.pending)
        counters = MemoryCounters()
        counters.cb = ctypes.sizeof(counters)
        kernel = ctypes.WinDLL("kernel32")
        kernel.GetCurrentProcess.restype = wintypes.HANDLE
        kernel.K32GetProcessMemoryInfo.argtypes = [wintypes.HANDLE, ctypes.POINTER(MemoryCounters), wintypes.DWORD]
        assert kernel.K32GetProcessMemoryInfo(kernel.GetCurrentProcess(), ctypes.byref(counters), counters.cb)
        gaps = sorted((right - left) * 1000 for left, right in zip(beats, beats[1:]))
        scroll_gaps = [(right - left) * 1000 for left, right in zip(scroll_beats, scroll_beats[1:])]
        metrics = {
            "scope": "Synthetic QImage source; excludes native Shell retrieval and source decoding; cold means first model visit, not flushed OS disk cache",
            "items": args.items,
            "initial_navigation_ms": round(cold_navigation_ms, 2),
            "first_12_thumbnails_ms": round(first_thumbnails_ms, 2),
            "warm_navigation_ms": round(warm_navigation_ms, 2),
            "event_loop_gap_p95_ms": round(gaps[int(len(gaps) * .95)], 2),
            "event_loop_gap_max_ms": round(max(gaps), 2),
            "scroll_event_loop_gap_max_ms": round(max(scroll_gaps), 2),
            "scroll_set_value_max_ms": round(max(scroll_calls), 2),
            "peak_working_set_mib": round(counters.PeakWorkingSetSize / 1048576, 2),
            "cached_pixels_mib": round(window.cache.bytes_used / 1048576, 2),
            "thumbnails_completed": window.thumbnails.completed,
            "peak_active_requests": window.thumbnails.peak_active,
            "peak_pending_requests": window.thumbnails.peak_pending,
        }
        (output / f"{args.prefix}-metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
        if args.profile_callbacks:
            (output / f"{args.prefix}-callbacks.json").write_text(json.dumps({
                "totals": profile.totals, "slow_callbacks": profile.slow,
                "model_events": profile.model_events,
            }, indent=2), encoding="utf-8")
        print(json.dumps(metrics, indent=2))
        timer.stop()
        window.close()
        app.processEvents()


if __name__ == "__main__":
    main()
