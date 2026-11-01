"""Measure Windows Shell thumbnail retrieval and generation through registered handlers."""

import argparse
from concurrent.futures import ThreadPoolExecutor
import ctypes
from ctypes import wintypes
import json
from pathlib import Path
import statistics
import time

from filevoyager.shell_thumbnails import load_cached_thumbnail


class MemoryCounters(ctypes.Structure):
    _fields_ = [("cb", wintypes.DWORD), ("PageFaultCount", wintypes.DWORD)] + [
        (name, ctypes.c_size_t) for name in (
            "PeakWorkingSetSize", "WorkingSetSize", "QuotaPeakPagedPoolUsage",
            "QuotaPagedPoolUsage", "QuotaPeakNonPagedPoolUsage", "QuotaNonPagedPoolUsage",
            "PagefileUsage", "PeakPagefileUsage")]


def timed_load(path, size):
    start = time.perf_counter()
    result = load_cached_thumbnail(str(path), size, size)
    elapsed = (time.perf_counter() - start) * 1000
    return elapsed, result.width, result.height, len(result.pixels)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", type=Path)
    parser.add_argument("--size", type=int, default=192)
    parser.add_argument("--suffix", nargs="+", default=[".png", ".jpg", ".jpeg", ".webp", ".bmp"],
                        help="Media suffixes to measure, e.g. --suffix .mp4 .mkv")
    parser.add_argument("--output", type=Path, default=Path(".benchmarks/shell-cache.json"))
    args = parser.parse_args()
    start = time.perf_counter()
    suffixes = frozenset(suffix.lower() for suffix in args.suffix)
    paths = sorted(p for p in args.folder.iterdir()
                   if p.is_file() and p.suffix.lower() in suffixes)
    enumeration_ms = (time.perf_counter() - start) * 1000
    report = {
        "folder": str(args.folder), "files": len(paths), "suffixes": sorted(suffixes),
        "requested_pixels": args.size,
        "flags": "0x08", "workers": 2, "enumeration_ms": enumeration_ms,
        "scope": "Windows Shell retrieval and generation. First pass is process-cold, not necessarily OS-cache-cold; no cache eviction.",
        "passes": [],
    }
    failed_futures = []
    with ThreadPoolExecutor(max_workers=2) as executor:
        for name in ("first", "repeat"):
            start = time.perf_counter()
            results = []
            failures = []
            # At most two calls are in flight; retain only scalar measurements.
            for offset in range(0, len(paths), 2):
                batch = [(p, executor.submit(timed_load, p, args.size))
                         for p in paths[offset:offset + 2]]
                for path, future in batch:
                    error = future.exception()
                    if error is not None:
                        failures.append({"path": str(path), "error": repr(error)})
                        failed_futures.append(future)
                    else:
                        results.append(future.result())
            elapsed = time.perf_counter() - start
            timings = sorted(row[0] for row in results)
            report["passes"].append({
                "name": name, "seconds": elapsed, "hits": len(results), "failures": failures,
                "successful_reads_per_second": len(results) / elapsed,
                "latency_ms": {"median": statistics.median(timings),
                               "p95": timings[int((len(timings) - 1) * .95)], "max": max(timings)},
                "pixel_bytes_copied": sum(row[3] for row in results),
                "returned_dimension_examples": [row[1:3] for row in results[:5]],
            })
            print(json.dumps(report["passes"][-1]), flush=True)
    kernel = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel.GetCurrentProcess.restype = wintypes.HANDLE
    kernel.K32GetProcessMemoryInfo.argtypes = [wintypes.HANDLE, ctypes.POINTER(MemoryCounters), wintypes.DWORD]
    kernel.K32GetProcessMemoryInfo.restype = wintypes.BOOL
    counters = MemoryCounters(cb=ctypes.sizeof(MemoryCounters))
    if not kernel.K32GetProcessMemoryInfo(kernel.GetCurrentProcess(), ctypes.byref(counters), counters.cb):
        raise ctypes.WinError(ctypes.get_last_error())
    report["peak_working_set_mib"] = counters.PeakWorkingSetSize / 1048576
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(args.output)
    # Measurement records native failures, then re-raises through Future.result().
    # No failed image is substituted and a failed run cannot exit successfully.
    for future in failed_futures:
        future.result()


if __name__ == "__main__":
    main()
