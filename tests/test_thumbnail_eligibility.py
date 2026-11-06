from collections import deque
from concurrent.futures import Future, ThreadPoolExecutor
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import unittest
from unittest.mock import Mock

from filevoyager.thumbnails import ThumbnailController, ThumbnailKey, load_existing_thumbnail


class ThumbnailEligibilityTests(unittest.TestCase):
    def test_deleted_file_and_directory_never_reach_extractor(self):
        with TemporaryDirectory() as directory, ThreadPoolExecutor(max_workers=1) as worker:
            path = Path(directory) / "deleted.jpg"
            path.write_bytes(b"image")
            path.unlink()
            loader = Mock()
            self.assertIsNone(worker.submit(load_existing_thumbnail, loader, str(path), 128).result())
            self.assertIsNone(worker.submit(load_existing_thumbnail, loader, directory, 128).result())
            loader.assert_not_called()
            path.write_bytes(b"image")
            self.assertIs(worker.submit(load_existing_thumbnail, loader, str(path), 128).result(),
                          loader.return_value)
            loader.assert_called_once_with(str(path), 128, 128)

    def test_removed_and_changed_model_entries_are_not_dispatched(self):
        source = Mock()
        removed, changed = Mock(), Mock()
        removed.isValid.return_value = False
        changed.isValid.return_value = True
        source.index.side_effect = [removed, changed]
        source.isDir.return_value = False
        source.file_metadata.return_value = (2, 20)
        controller = SimpleNamespace(
            model=Mock(), pending=deque([ThumbnailKey("deleted.jpg", 1, 10, 128, 1),
                                         ThumbnailKey("changed.jpg", 1, 10, 128, 1)]),
            active={}, requested=set(), executor=Mock(), peak_active=0, poll_timer=Mock())
        controller.model.sourceModel.return_value = source
        ThumbnailController.dispatch(controller)
        controller.executor.submit.assert_not_called()
        self.assertFalse(controller.pending)

    def test_missing_worker_result_is_not_cached_or_requeued(self):
        key = ThumbnailKey("deleted.jpg", 1, 10, 128, 1)
        future = Future()
        future.set_result(None)
        controller = SimpleNamespace(model=Mock(), active={future: (0, key)},
                                     requestFinished=Mock(), generation=0, requested={key},
                                     enabled=True, dispatch=Mock(), poll_timer=Mock())
        ThumbnailController.poll(controller)
        controller.model.cache.put.assert_not_called()
        controller.dispatch.assert_called_once_with()
        controller.poll_timer.stop.assert_called_once_with()
        self.assertIn(key, controller.requested)
