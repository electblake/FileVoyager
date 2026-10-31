import subprocess
import sys
import unittest
from functools import partial

import numpy as np
from PIL import Image

from filevoyager.image_processors import (
    ImageFeatureExtractor,
    SPECTRA_EXTRACTORS,
    SPECTRA_VISUAL_EXTRACTOR,
    extract_histogram_features,
    extract_spatial_color_features,
    extract_visual_features,
)


class ImageProcessorTests(unittest.TestCase):
    def test_histogram_bins_and_channel_normalization(self):
        with Image.new("RGB", (100, 100), "red") as image:
            for space, bins, occupied in [("RGB", 32, [31, 32, 64]), ("HSV", 16, [0, 31, 47])]:
                with self.subTest(space=space):
                    result = extract_histogram_features(image, color_space=space, bins_per_channel=bins)
                    np.testing.assert_array_equal(np.flatnonzero(result), occupied)
                    np.testing.assert_allclose(result[occupied], 1 / 3)

    def test_uniform_image_values_through_uniform_interface(self):
        with Image.new("RGB", (200, 100), "white") as image:
            values = {extractor.name: extractor(image) for extractor in SPECTRA_EXTRACTORS}
        np.testing.assert_array_equal(values["spectra.spatial_color"], np.ones(48))
        np.testing.assert_array_equal(values["spectra.texture"], np.zeros(21))
        np.testing.assert_array_equal(values["spectra.brightness_contrast"], [1, 0, 1, 1, 1])
        np.testing.assert_allclose(values["spectra.aspect_ratio"], [0.6])

    def test_spatial_order_and_custom_extractor(self):
        extractor = ImageFeatureExtractor("custom.spatial_2x2", 12,
                                          partial(extract_spatial_color_features, grid_size=2))
        with Image.new("RGB", (100, 100)) as image:
            for box, color in [((0, 0, 50, 50), "red"), ((50, 0, 100, 50), "green"),
                               ((0, 50, 50, 100), "blue"), ((50, 50, 100, 100), "white")]:
                image.paste(color, box)
            result = extractor(image)
        self.assertEqual(result.shape, (extractor.dimensions,))
        np.testing.assert_array_equal(result, np.array([255, 0, 0, 0, 128, 0, 0, 0, 255, 255, 255, 255]) / 255)

    def test_inputs_preserved_and_declared_dimensions(self):
        pixels = np.random.default_rng(7).integers(0, 256, (120, 240, 3), dtype=np.uint8)
        with Image.fromarray(pixels) as source:
            for mode in ["RGB", "RGBA", "L", "P"]:
                with self.subTest(mode=mode), source.convert(mode) as image:
                    original = image.tobytes()
                    for extractor in (*SPECTRA_EXTRACTORS, SPECTRA_VISUAL_EXTRACTOR):
                        result = extractor(image)
                        self.assertEqual(result.shape, (extractor.dimensions,))
                        self.assertTrue(np.isfinite(result).all())
                    for gap in [None, 1.0, 2.0, 3.0]:
                        result = extract_visual_features(image, reducing_gap=gap)
                        self.assertEqual(result.shape, (219,))
                        np.testing.assert_allclose(np.linalg.norm(result), 1)
                    self.assertEqual(image.mode, mode)
                    self.assertEqual(image.size, (240, 120))
                    self.assertEqual(image.tobytes(), original)

    def test_weight_order_and_omitted_families(self):
        with Image.new("RGB", (200, 100), "white") as image:
            result = extract_visual_features(image, feature_weights=(0, 0, 0, 0, 2, 3))
        np.testing.assert_allclose(result, np.array([2, 0, 2, 2, 2, 1.8]) / np.sqrt(19.24))

    def test_imports_do_not_load_ui_or_eagerly_load_processors(self):
        subprocess.run([sys.executable, "-c", "import sys; import filevoyager; "
                        "assert 'filevoyager.image_processors' not in sys.modules; "
                        "import filevoyager.image_processors; "
                        "assert not any(name.startswith('PySide6') for name in sys.modules); "
                        "assert 'filevoyager.window' not in sys.modules"], check=True)
