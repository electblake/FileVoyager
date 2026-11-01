"""Measure worker scans of 1,000 real Windows shortcuts, first and repeat visits."""

from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import shutil
from tempfile import TemporaryDirectory
from time import perf_counter

from PySide6.QtWidgets import QApplication

from filevoyager.directory_tree import scan_directories
from filevoyager.file_model import directory_snapshot
from filevoyager.link_drag import create_shortcuts


app = QApplication([])
with TemporaryDirectory(prefix="filevoyager-shortcut-bench-") as scratch:
    root = Path(scratch)
    target = root / "target"
    target.mkdir()
    links = root / "links"
    links.mkdir()
    with ThreadPoolExecutor(max_workers=1) as worker:
        worker.submit(create_shortcuts, (target,), links).result()
        source = links / "target - Shortcut.lnk"
        for number in range(999):
            shutil.copyfile(source, links / f"link-{number:04}.lnk")
        results = {"scope": "1,000 native .lnk files; first and repeat scans, OS cache not flushed"}
        for name, operation, args in (
                ("list_ms", directory_snapshot, (str(links), (), 0, False, True)),
                ("tree_ms", scan_directories, (str(links),))):
            elapsed = []
            for _ in range(3):
                started = perf_counter()
                worker.submit(operation, *args).result()
                elapsed.append(round((perf_counter() - started) * 1000, 2))
            results[name] = elapsed
        output = Path(".benchmarks")
        output.mkdir(exist_ok=True)
        (output / "release-040-shortcuts.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
        print(json.dumps(results, indent=2))
