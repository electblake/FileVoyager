# Standalone image processors

Spectra-derived Pillow image-to-NumPy-vector functions and uniform vector comparison/clustering interfaces. The numerical package remains independent of Qt; the application consumes it through a background analysis job. Importing this package does not import Qt, read settings, open files, or start workers. NumPy and Pillow are installed through the project's `uv sync --locked` environment. Feature extraction needs NumPy and Pillow. DBSCAN uses scikit-learn nearest-neighbor queries, imported only when clustering is called.

## Use the default composite

```python
from PIL import Image
from filevoyager.image_processors import SPECTRA_VISUAL_EXTRACTOR

with Image.open("picture.jpg") as image:
    vector = SPECTRA_VISUAL_EXTRACTOR(image)

print(SPECTRA_VISUAL_EXTRACTOR.name)        # spectra.visual
print(SPECTRA_VISUAL_EXTRACTOR.dimensions)  # 219
print(vector.shape)                        # (219,)
```

The caller opens and closes the image. Extraction is synchronous, leaves input pixels/mode/dimensions unchanged, and returns a new one-dimensional NumPy array. Exceptions propagate directly. No validation, retry, fallback provider, or replacement vector is supplied.

## Uniform interface

`ImageFeatureExtractor(name, dimensions, extract)` is a frozen descriptor wrapping a callable with the signature `extract(image: PIL.Image.Image) -> numpy.ndarray`. Calling the descriptor invokes that function. `dimensions` declares its output length; it does not validate it. Use stable names and correctly declared dimensions for new implementations.

`SPECTRA_EXTRACTORS` is an ordered tuple of the six individual families. `SPECTRA_VISUAL_EXTRACTOR` is the separate weighted composite. Future extraction implementations can use the same descriptor without changing the existing extractors or adding a plugin framework.

```python
from functools import partial
from filevoyager.image_processors import (
    ImageFeatureExtractor,
    SPECTRA_EXTRACTORS,
    extract_spatial_color_features,
)

spatial_2x2 = ImageFeatureExtractor(
    "custom.spatial_2x2",
    12,
    partial(extract_spatial_color_features, grid_size=2, reducing_gap=2.0),
)

# Supply an already-open image owned by the caller.
def extract_selected(image):
    return {extractor.name: extractor(image)
            for extractor in (*SPECTRA_EXTRACTORS, spatial_2x2)}
```

## Public functions and defaults

| Function | Default output | Technique |
| --- | ---: | --- |
| `extract_histogram_features(image, *, color_space, bins_per_channel, reducing_gap=None)` | 3 times bin count | RGB or Pillow HSV channel histograms, normalized together by total count plus 1e-10 |
| `extract_spatial_color_features(image, *, grid_size=4, reducing_gap=None)` | 48 | Row-major grid RGB means / 255 |
| `extract_texture_features(image, *, reducing_gap=None)` | 21 | Grayscale standard deviation, absolute x/y difference means and standard deviations, then 16 regional standard deviations; all / 255 |
| `extract_brightness_contrast_features(image, *, reducing_gap=None)` | 5 | Grayscale mean, standard deviation, median, 25th and 75th percentiles / 255 |
| `extract_geometry_aspect_ratio_features(image)` | 1 | tanh(log(width / height)) |
| `extract_visual_features(image, *, feature_weights=DEFAULT_FEATURE_WEIGHTS, reducing_gap=None)` | 219 | Weighted concatenation followed by L2 normalization |

The composite order is RGB (32 bins/channel, 96 values), HSV (16 bins/channel, 48 values), spatial (48), texture (21), brightness/contrast (5), aspect ratio (1). Default weights are `(2.0, 1.5, 1.0, 0.5, 0.8, 0.25)`. A zero weight omits that family, changing the dimension. When wrapping a configured composite, declare the sum of the enabled family dimensions. Use matching weights, preprocessing settings, and implementation revisions when comparing or persisting vectors.

At least one family must be enabled, and its combined weighted vector must have a nonzero norm. All-disabled input fails at NumPy concatenation. Zero-norm vectors are passed directly through NumPy division, with NumPy's native numerical behavior; no substitute vector is returned.

Pixel-based families independently convert the image and resize to 100 x 100 with LANCZOS, passing `reducing_gap` to Pillow. Geometry uses the original size. Conversion precedes resizing and can allocate a full-size intermediate. No EXIF orientation correction or explicit alpha compositing is added. The default 4 x 4 spatial grid divides 100 evenly; other grid sizes use integer cell dimensions.

The extraction functions are synchronous and provide no scheduling or image cache. The Image similarity dock schedules extraction and clustering on its analysis worker, outside painting and synchronous model access. See the project documentation in docs/image-similarity.md for UI behavior and performance validation.

## Provenance

Adapted from [Spectra 2.9.0, revision 348b54e1e793f00acc279f5dc232c95799f53d29](https://github.com/electblake/Spectra/tree/348b54e1e793f00acc279f5dc232c95799f53d29/app/image_processors). The [MIT license](LICENSE) and original copyright notice are included.

Changes from the captured source: default weights are local instead of imported from Spectra application settings; a named callable interface and public exports are added; the composite performs direct L2 division without the upstream zero-norm substitution behavior, following this project's fail-fast policy. Individual feature formulas are preserved.

The dated source bundle and technique summary live in `.agents/references/spectra-image-processors/2026-10-31/` at the project root. Numerical, input-preservation, extension-interface, and import-isolation checks run with:

```powershell
uv run --locked python -m unittest discover -s tests -p test_image_processors.py -v
```

## Vector comparison and clustering

```python
from functools import partial
from filevoyager.image_processors import (
    EUCLIDEAN_COMPARISON, SIMILARITY_COMPARISON, VectorClusterer, dbscan_labels,
)

# vectors: a 2D NumPy array, one consistently configured descriptor per row.
def compare_and_cluster(vectors):
    distances = EUCLIDEAN_COMPARISON(vectors[0], vectors)
    similarities = SIMILARITY_COMPARISON(vectors[0], vectors)
    clusterer = VectorClusterer(
        "dbscan.euclidean", partial(dbscan_labels, eps=0.25, min_samples=3),
    )
    labels = clusterer(vectors)
    return distances, similarities, labels
```

`VectorComparison(name, compare)` wraps `(reference, vectors) -> values`. Euclidean distances increase with difference; inverse-Euclidean similarity is `1 / (1 + distance)` and is 1 for identical vectors. It is a numerical score, not a probability. Neither function allocates an all-pairs distance matrix.

`VectorClusterer(name, cluster)` wraps `(vectors, *, cancel=None, progress=None) -> labels`. Labels are integer cluster IDs in input discovery order; -1 denotes noise. Future implementations can supply this callable contract. `cancel` is a threading.Event; cancellation returns None. `progress(completed, total)` runs on the calling thread. Exceptions propagate unchanged.

`dbscan_labels` implements DBSCAN expansion using scikit-learn BallTree radius queries. It queries one neighborhood at a time instead of using sklearn.cluster.DBSCAN's bulk neighborhood storage. `min_samples` includes the point itself. Time can still be quadratic for dense neighborhoods or high-dimensional vectors. Storage scales with the feature matrix/index plus one neighborhood, visited/queued flags, labels, and a deduplicated queue.

Supply a nonempty matrix of finite, consistent vectors, positive eps, and an integer min_samples >= 1. The dock constrains its controls; the numerical API adds no custom validation or replacement values. Border-point assignment can depend on input order, as in DBSCAN generally.
