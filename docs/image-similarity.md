# Image similarity and DBSCAN sorting

The **Image similarity** dock starts in the right dock area. Drag its title to move or float it. Its title-bar close button hides it; use **Ctrl+Shift+S** or the main window's toolbar/dock context menu to show it again. Controls follow the existing Qt palette and fonts, and the dock scrolls when its contents do not fit.

## Workflow

1. Open a folder and set the six feature weights. Zero disables a family; at least one must remain enabled.
2. Set **Distance threshold (eps)** and **Minimum neighbors**, then choose **Cluster and sort**.
3. Alternatively, select one image and choose **Sort by selected image** to order images by increasing Euclidean distance to its descriptor. This uses the same feature weights; DBSCAN controls do not affect reference-image comparison.
4. Use **Cancel analysis** to stop, or **Restore name order** to return to normal ascending name sorting. Clicking a Details column also returns to normal filesystem sorting.

Analysis reads image originals in the current folder, nonrecursively. It does not rename, move, or modify files. Animated/multipage images use the first frame. Videos and other non-image files are not analyzed. Supported candidate suffixes are jpg, jpeg, png, webp, bmp, tif, tiff, gif, avif, heic, heif, and jxl; decoding still requires the installed Pillow build to support the file's codec. Missing files, unsupported codecs, invalid images, and numerical failures propagate unchanged through the worker future to the Qt callback. There are no substituted descriptors or automatic retries.

Folders remain first, followed by analyzed images, then other files. Cluster sorting uses cluster discovery order and alphabetical order within each cluster; noise follows the clusters. Reference sorting uses ascending distance with alphabetical ties. Both Grid and Details share the same proxy and selection. Status reports image, cluster, and noise counts. These settings and results apply to this session; navigating clears the custom order and cancels the previous analysis. A result is a snapshot of the folder at analysis time; rerun after external file changes.

## Parameter meaning

The six defaults are RGB 2.0, HSV 1.5, spatial color 1.0, texture 0.5, brightness/contrast 0.8, and aspect ratio 0.25. Each enabled family is multiplied by its weight, concatenated, and the composite is L2 normalized. Default length is 219. Weights are relative contributions, not six independent distance cutoffs. All enabled families must yield a finite, nonzero combined descriptor.

DBSCAN's eps is one Euclidean radius in that normalized vector space. The initial value is 0.25; smaller values require closer neighbors. The UI range is 0.0001–2.0, covering the distance range between unit vectors. **Minimum neighbors** defaults to 3 and includes the image itself; it determines whether a point is dense enough to expand a cluster. Images not reachable from a core point are noise. These defaults are starting settings, not calibrated quality guarantees.

DBSCAN can chain neighboring images into a cluster: eps is not a maximum distance between every pair of members. Border assignments can depend on input order. The worker sorts paths before clustering to make unchanged input/settings repeatable.

## Interfaces and execution

The public numerical API is documented in [the image processor package](../filevoyager/image_processors/README.md). `VectorComparison` wraps a named reference-to-matrix comparison; `VectorClusterer` wraps a named configured clustering callable. Euclidean distances, inverse-Euclidean similarity scores, and configurable DBSCAN labels are exported from `filevoyager.image_processors`.

The UI uses one analysis worker and permits only one outstanding job, with no pending analysis queue. Image loading/decoding, extraction, neighbor queries, and ordering happen there. Images close after extraction; the worker retains descriptors rather than full-resolution decoded images. Progress is polled every 50 ms. Cancellation is checked between images and neighborhood queries; it does not interrupt an image decode or neighbor query already underway. Qt models are updated only on the UI thread, once on completion.

The implementation performs DBSCAN expansion with scikit-learn `NearestNeighbors` using a Euclidean BallTree. It retains only one radius neighborhood at a time and a deduplicated queue, avoiding bulk storage of every neighborhood. Memory scales with the n-by-d descriptor/index storage plus O(n) labels, flags, neighborhood, queue, and ordering data; dense inputs can still require quadratic time. The extraction code converts before resizing and may allocate full-size intermediates for the current image. The Windows thumbnail pipeline is unchanged.

Upstream algorithm references: [DBSCAN API and memory notes](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html) and [NearestNeighbors](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html). Tests compare the implementation's labels with scikit-learn DBSCAN on duplicates, dense samples, noise, and border cases.

## Validation on 2026-10-31

With the existing 500-image Screenshots folder (about 156 MiB of source files), default parameters produced 19 clusters and 177 noise images on both passes. The benchmark used Details view, so it isolates analysis from Shell thumbnail retrieval.

| Measurement | First pass | Second pass |
| --- | ---: | ---: |
| Extraction, clustering, and sorting | 44.86 s | 42.77 s |
| 10 ms event-loop heartbeat gap, p95 | 10.92 ms | 10.91 ms |
| Maximum heartbeat gap | 52.33 ms | 63.94 ms |
| Applying 500-image order on UI thread | 25.93 ms | 50.90 ms |

Initial navigation was 1,076.91 ms; eight rapidly requested navigations plus analysis cancellation settled in 133.34 ms. Peak working set was 310.95 MiB. No persistent feature cache is implemented, so the second pass re-extracts every image. This is a first/warm application pass, not a flushed OS cold-cache experiment. The first pass overlapped the synthetic UI benchmark, so the numbers are observations rather than isolated throughput limits.

The 10,000-item UI regression used synthetic thumbnail results and no extraction: initial navigation 3,633.88 ms, warm navigation 44.34 ms, maximum scrolling heartbeat gap 44.24 ms, maximum scrollbar command 0.19 ms, peak working set 170.84 MiB. At most two thumbnail reads and 28 queued requests were observed. A heartbeat measures event-loop availability, not rendered frame time. These results do not establish extraction performance on 10,000 real originals or network directories.

Raw metrics and the dock screenshot are local ignored artifacts under `.benchmarks/similarity-*`; synthetic grid screenshots contain generated colors only. Automated checks cover API outputs, scikit-learn parity, input-weight effects, worker failure propagation, right-dock placement, undocking/reopening, shared selection/order, disabled all-zero controls, and stale-job cancellation.

A separate 10,000-item custom-order test measured a 709.60 ms UI-thread sort before metadata-key caching and 266.28 ms afterward. This is still a noticeable one-time completion pause at that scale; extraction and clustering remain on the worker. Keys are discarded on metadata changes, removals, resets, and new orders. The 500-image table above predates this optimization. The browser regression suite also exposed a batched grid scrollbar extent lag with the sorting proxy; restoration now waits for the last item and scrollbar extent to agree.
