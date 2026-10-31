"""Named image-to-vector callables for independently configured extractors."""

from collections.abc import Callable
from dataclasses import dataclass
from functools import partial

import numpy as np
from PIL import Image

from .features.brightness_contrast import extract_brightness_contrast_features
from .features.geometry import extract_geometry_aspect_ratio_features
from .features.histograms import extract_histogram_features
from .features.spatial_color import extract_spatial_color_features
from .features.texture import extract_texture_features
from .features_extraction import extract_visual_features


@dataclass(frozen=True)
class ImageFeatureExtractor:
    """An identifier, declared vector length, and synchronous Pillow callable.

    Configure callable options before registration, for example with partial.
    The callable owns its output; the caller owns and closes the input image.
    """

    name: str
    dimensions: int
    extract: Callable[[Image.Image], np.ndarray]

    def __call__(self, image: Image.Image) -> np.ndarray:
        return self.extract(image)


SPECTRA_EXTRACTORS = (
    ImageFeatureExtractor("spectra.rgb_histogram", 96,
                          partial(extract_histogram_features, color_space="RGB", bins_per_channel=32)),
    ImageFeatureExtractor("spectra.hsv_histogram", 48,
                          partial(extract_histogram_features, color_space="HSV", bins_per_channel=16)),
    ImageFeatureExtractor("spectra.spatial_color", 48, extract_spatial_color_features),
    ImageFeatureExtractor("spectra.texture", 21, extract_texture_features),
    ImageFeatureExtractor("spectra.brightness_contrast", 5, extract_brightness_contrast_features),
    ImageFeatureExtractor("spectra.aspect_ratio", 1, extract_geometry_aspect_ratio_features),
)

SPECTRA_VISUAL_EXTRACTOR = ImageFeatureExtractor("spectra.visual", 219, extract_visual_features)
