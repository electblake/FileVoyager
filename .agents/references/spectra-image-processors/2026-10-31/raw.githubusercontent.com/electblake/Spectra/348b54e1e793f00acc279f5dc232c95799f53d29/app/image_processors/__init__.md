<!--
source: https://raw.githubusercontent.com/electblake/Spectra/348b54e1e793f00acc279f5dc232c95799f53d29/app/image_processors/__init__.py
retrieved: 2026-10-31T23:02:13.458895+00:00
final_url: https://raw.githubusercontent.com/electblake/Spectra/348b54e1e793f00acc279f5dc232c95799f53d29/app/image_processors/__init__.py
content_type: text/plain
-->

```python
"""Image feature extractors accepting Pillow images and returning NumPy vectors."""

from .features.brightness_contrast import extract_brightness_contrast_features
from .features.geometry import extract_geometry_aspect_ratio_features
from .features.histograms import extract_histogram_features
from .features.spatial_color import extract_spatial_color_features
from .features.texture import extract_texture_features
from .features_extraction import extract_visual_features

__all__ = [
    "extract_brightness_contrast_features",
    "extract_geometry_aspect_ratio_features",
    "extract_histogram_features",
    "extract_spatial_color_features",
    "extract_texture_features",
    "extract_visual_features",
]
```
