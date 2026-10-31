import unittest
from unittest.mock import patch

from PySide6.QtGui import QImage

from filevoyager.shell_bridge import load_thumbnail_image
from filevoyager.shell_thumbnails import ThumbnailPixels


class BridgeTests(unittest.TestCase):
    def test_normalizes_qt_paths_and_detaches_bgr_pixels(self):
        pixels = ThumbnailPixels(1, 2, 4, bytes([0, 0, 255, 0, 255, 0, 0, 0]))
        with patch("filevoyager.shell_bridge.load_cached_thumbnail", return_value=pixels) as load:
            image = load_thumbnail_image("C:/Pictures/example.png", 128, 128)
        load.assert_called_once_with("C:\\Pictures\\example.png", 128, 128)
        self.assertEqual(image.format(), QImage.Format.Format_RGB32)
        self.assertEqual(image.pixelColor(0, 0).getRgb(), (255, 0, 0, 255))
        self.assertEqual(image.pixelColor(0, 1).getRgb(), (0, 0, 255, 255))
        self.assertEqual(image.sizeInBytes(), 8)

    def test_native_failure_is_not_wrapped_or_replaced(self):
        failure = OSError("native failure")
        with patch("filevoyager.shell_bridge.load_cached_thumbnail", side_effect=failure):
            with self.assertRaises(OSError) as raised:
                load_thumbnail_image("C:/Pictures/example.png", 128, 128)
        self.assertIs(raised.exception, failure)
