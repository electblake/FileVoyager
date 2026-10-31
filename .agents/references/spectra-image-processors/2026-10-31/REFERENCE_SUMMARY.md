# Spectra image feature extractors

## Snapshot and sources

- Reference date: 2026-10-31.
- Spectra version: **2.9.0**, declared in [pyproject.toml](raw.githubusercontent.com/electblake/Spectra/348b54e1e793f00acc279f5dc232c95799f53d29/pyproject.md).
- Resolved main revision: `348b54e1e793f00acc279f5dc232c95799f53d29`; commit timestamp: 2026-10-26T17:44:39Z.
- Seed: https://github.com/electblake/Spectra/tree/main/app/image_processors.
- All eight files under app/image_processors are mirrored at the immutable revision, together with configuration, project metadata, requirements, README, MIT license, and upstream feature tests.
- Source observations below come from repository code. Upstream tests were inspected, not executed. No FileVoyager runtime behavior or performance was measured.

## Feature families

All pixel-based families convert the input to their target color mode, then resize independently to **100 x 100** using Pillow LANCZOS and the supplied reducing_gap. This forces square dimensions; the original shape is represented separately. Inputs are Pillow images; outputs are NumPy arrays. The caller owns the image lifetime and extractors leave the input unchanged.

| Family | Values | Default weight | Technique and output order |
| --- | ---: | ---: | --- |
| RGB histogram | 96 | 2.0 | 32 bins each for R, G, B; concatenate channels. |
| HSV histogram | 48 | 1.5 | 16 bins each for Pillow H, S, V; concatenate channels. |
| Spatial color | 48 | 1.0 | 4 x 4 cells, row-major traversal, RGB mean per cell divided by 255. |
| Texture | 21 | 0.5 | Grayscale intensity standard deviation; absolute x/y difference means; x/y difference standard deviations; 16 row-major regional intensity standard deviations; divide by 255. |
| Brightness/contrast | 5 | 0.8 | Grayscale mean, standard deviation, median, 25th percentile, 75th percentile; divide by 255. |
| Aspect ratio | 1 | 0.25 | tanh(log(width / height)) from original dimensions. |

Histogram bins use range (0, 256) for every channel, including Pillow HSV. The whole concatenated histogram is divided by its total count plus 1e-10; it is not normalized separately per channel. A constant image therefore places approximately 1/3 in each of three occupied bins.

Sources: [histograms](raw.githubusercontent.com/electblake/Spectra/348b54e1e793f00acc279f5dc232c95799f53d29/app/image_processors/features/histograms.md), [spatial color](raw.githubusercontent.com/electblake/Spectra/348b54e1e793f00acc279f5dc232c95799f53d29/app/image_processors/features/spatial_color.md), [texture](raw.githubusercontent.com/electblake/Spectra/348b54e1e793f00acc279f5dc232c95799f53d29/app/image_processors/features/texture.md), [brightness/contrast](raw.githubusercontent.com/electblake/Spectra/348b54e1e793f00acc279f5dc232c95799f53d29/app/image_processors/features/brightness_contrast.md), [geometry](raw.githubusercontent.com/electblake/Spectra/348b54e1e793f00acc279f5dc232c95799f53d29/app/image_processors/features/geometry.md).

## Composite descriptor

[extract_visual_features](raw.githubusercontent.com/electblake/Spectra/348b54e1e793f00acc279f5dc232c95799f53d29/app/image_processors/features_extraction.md) multiplies each enabled family by its weight, concatenates in the table order, and divides by the overall L2 norm when positive. Default length is 96 + 48 + 48 + 21 + 5 + 1 = **219**. A zero weight omits the family entirely, changing the vector length. All-zero weights reach NumPy concatenate with an empty list and fail naturally. No per-family L2 normalization is performed.

Default vector slices are RGB [0:96], HSV [96:144], spatial [144:192], texture [192:213], brightness [213:218], aspect [218:219]. These boundaries are derived from the source lengths and order.

[Configuration](raw.githubusercontent.com/electblake/Spectra/348b54e1e793f00acc279f5dc232c95799f53d29/app/config.md) maps resize optimization Default to None, Low to 3.0, Medium to 2.0, and High to 1.0 for reducing_gap. These values are passed to Pillow resize. The extractors themselves are synchronous and do not provide work scheduling or caching.

## Compatibility and reuse observations

- Project metadata requires Python >=3.12.10, NumPy >=1.24.0, Pillow >=10.0.0, PySide6 >=6.8,<7, platformdirs >=4.11.0, OpenCV >=5.0.0.93, PyYAML >=6.0.3, scikit-learn >=1.3.0, and SciPy >=1.10.0. These are upstream declarations, not locally verified installed versions.
- Individual numerical extractors use NumPy and Pillow. Importing the public package also imports the composite extractor and app.config, which imports Qt/platformdirs and reads the repository pyproject.toml for its version. It is therefore not an independently packaged NumPy/Pillow-only API.
- requirements.txt omits OpenCV and PyYAML present in pyproject.toml and carries an older Chromaflow comment; preserve both manifests rather than assuming they are equivalent.
- Changing enabled families changes dimensionality; changing weights or preprocessing changes descriptor meaning. Reusable stored vectors need a matching extraction configuration and revision. This is a compatibility inference from the implementation.
- Custom spatial grid sizes use integer division of 100; sizes that do not divide 100 leave border pixels outside the cells. The default grid size 4 divides evenly.
- The inspected functions contain no explicit EXIF orientation correction or alpha compositing policy. Conversions are delegated to Pillow.
- No historical comparison was performed, so this bundle does not establish breaking changes across releases.
- [MIT license](raw.githubusercontent.com/electblake/Spectra/348b54e1e793f00acc279f5dc232c95799f53d29/LICENSE.md) is included with its copyright and permission text.

## Tests and FileVoyager implications

[Upstream tests](raw.githubusercontent.com/electblake/Spectra/348b54e1e793f00acc279f5dc232c95799f53d29/tests/test_image_features.md) cover channel ordering, histogram normalization, uniform-image descriptors, row-major spatial order, input preservation for RGB/RGBA/L/P, reducing_gap None/1/2/3, vector lengths, and omitted-family weight behavior. They were captured, not run.

For FileVoyager, these are low-level color, tone, texture, and shape descriptors, not learned semantic embeddings. Pixel arrays are reduced before statistics, but each enabled pixel family independently converts and resizes the input. Conversion happens before resizing and may allocate full-size intermediate images. Small descriptor size alone does not establish bounded peak image memory or responsive UI behavior. Any future integration should keep extraction outside paint/model-data callbacks and measure throughput, memory, navigation, and scrolling on representative folders under the project instructions. No implementation is included in this reference task.

## Capture notes

All 15 requested sources were captured. GitHub /llms.txt was saved with its linked GitHub MCP repository page; that page is discovery metadata, not evidence about image features. raw.githubusercontent.com/llms.txt returned HTTP 404, recorded in MIRROR_MANIFEST.json. No requested processor source failed. Markdown source mirrors include provenance metadata and code fences; they are reference documents, not executable modules.
