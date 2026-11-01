"""Offscreen selection/drag benchmark; real files, synthetic thumbnails."""

import argparse
import cProfile
import json
from pathlib import Path
import pstats
import tempfile
import time

from PySide6.QtCore import QItemSelection, QItemSelectionModel, QMimeData, QPointF, QSettings, QUrl, Qt
from PySide6.QtGui import QDragEnterEvent, QDragMoveEvent, QDragLeaveEvent
from PySide6.QtWidgets import QApplication

from benchmark_ui import synthetic_image, wait_for
from filevoyager.preferences import FolderPreferences
from filevoyager.window import ExplorerWindow


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--items", type=int, default=10000)
    parser.add_argument("--prefix", required=True)
    args = parser.parse_args()
    app = QApplication([])
    output = Path(".benchmarks")
    output.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="filevoyager-interactions-") as scratch:
        root = Path(scratch) / "images"
        root.mkdir()
        paths = [root / f"photo-{number:05}.png" for number in range(args.items)]
        for path in paths:
            path.touch()
        destination = root / "destination"
        destination.mkdir()
        preferences = FolderPreferences(QSettings(str(Path(scratch) / "settings.ini"), QSettings.Format.IniFormat))
        preferences.save(str(root), preferences.load(str(root), False))
        window = ExplorerWindow(str(root), synthetic_image, preferences=preferences)
        window.show()
        wait_for(lambda: window.current_path == str(root) and not window.pending_restore
                 and window.model.rowCount(window.details.rootIndex()) == args.items + 1)
        parent = window.details.rootIndex()
        first = window.model.index(0, 0, parent)
        last = window.model.index(args.items, 3, parent)
        window.selection.setCurrentIndex(first, QItemSelectionModel.SelectionFlag.NoUpdate)
        samples = []
        profile = cProfile.Profile()
        profile.enable()
        for _ in range(3):
            window.selection.clearSelection()
            start = time.perf_counter()
            window.selection.select(QItemSelection(first, last), QItemSelectionModel.SelectionFlag.Select)
            samples.append((time.perf_counter() - start) * 1000)
        profile.disable()
        with (output / f"{args.prefix}-selection-profile.txt").open("w") as stream:
            pstats.Stats(profile, stream=stream).sort_stats("cumulative").print_stats(30)
        window.selection.clearSelection()
        mime = QMimeData()
        mime.setUrls([QUrl.fromLocalFile(str(path)) for path in paths])
        point = QPointF(window.details.visualRect(first).center())
        enter = QDragEnterEvent(point, Qt.DropAction.LinkAction, mime,
                               Qt.MouseButton.LeftButton, Qt.KeyboardModifier.AltModifier)
        app.sendEvent(window.details.viewport(), enter)
        assert enter.isAccepted()
        moves = []
        for _ in range(100):
            event = QDragMoveEvent(point, Qt.DropAction.LinkAction, mime,
                                  Qt.MouseButton.LeftButton, Qt.KeyboardModifier.AltModifier)
            start = time.perf_counter()
            app.sendEvent(window.details.viewport(), event)
            moves.append((time.perf_counter() - start) * 1000)
            assert event.isAccepted()
        app.sendEvent(window.details.viewport(), QDragLeaveEvent())
        metrics = {"items": args.items, "selection_ms": samples,
                   "drag_move_p50_ms": sorted(moves)[50], "drag_move_p95_ms": sorted(moves)[95],
                   "drag_move_max_ms": max(moves), "scope": "Real files; synthetic thumbnails; offscreen Qt"}
        (output / f"{args.prefix}-interactions.json").write_text(json.dumps(metrics, indent=2))
        print(json.dumps(metrics, indent=2))
        window.close()
        app.processEvents()


if __name__ == "__main__":
    main()
