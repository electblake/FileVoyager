<!--
source: https://raw.githubusercontent.com/electblake/Spectra/348b54e1e793f00acc279f5dc232c95799f53d29/app/image_processors/features/brightness_contrast.py
retrieved: 2026-10-31T23:02:13.751947+00:00
final_url: https://raw.githubusercontent.com/electblake/Spectra/348b54e1e793f00acc279f5dc232c95799f53d29/app/image_processors/features/brightness_contrast.py
content_type: text/plain
-->

```python
import numpy as np
from PIL import Image as PIL_Image


def extract_brightness_contrast_features(image: PIL_Image.Image, *, reducing_gap: float | None = None) -> np.ndarray:
    """Return grayscale mean, std, median, 25th and 75th percentiles / 255.

    Leaves the input image unchanged.
    """
    gray = image.convert('L')
    gray = gray.resize((100, 100), PIL_Image.Resampling.LANCZOS, reducing_gap=reducing_gap)
    gray_array = np.array(gray, dtype=np.float32)

    features = [
        gray_array.mean() / 255.0,
        gray_array.std() / 255.0,
        np.median(gray_array) / 255.0,
        np.percentile(gray_array, 25) / 255.0,
        np.percentile(gray_array, 75) / 255.0,
    ]

    return np.array(features)
```
