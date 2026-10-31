<!--
source: https://raw.githubusercontent.com/electblake/Spectra/348b54e1e793f00acc279f5dc232c95799f53d29/app/image_processors/features/geometry.py
retrieved: 2026-10-31T23:02:13.924355+00:00
final_url: https://raw.githubusercontent.com/electblake/Spectra/348b54e1e793f00acc279f5dc232c95799f53d29/app/image_processors/features/geometry.py
content_type: text/plain
-->

```python
import numpy as np
from PIL import Image


def extract_geometry_aspect_ratio_features(image: Image.Image) -> np.ndarray:
    """Return one value: tanh(log(width / height)).

    Leaves the input image unchanged.
    """
    width, height = image.size
    return np.array([np.tanh(np.log(width / height))])
```
