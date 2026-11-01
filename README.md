# FileVoyager

A Windows file browser built with PySide6 6.12.0. Performance takes priority over exact Explorer styling.

## Run

For the Windows Setup executable and reproducible build instructions, see [installer packaging](packaging/README.md).

From this project directory, with Python 3.12 and uv:

```powershell
uv sync --locked
uv run filevoyager
uv run filevoyager 'C:\Users\shoji\Pictures\Screenshots'
```

The app opens the supplied folder or the last visited folder; the first launch opens your home directory. Unvisited folders containing a supported image or video file default to **Grid**; other folders default to **Details**. A saved folder preference takes precedence. Choose Small, Medium, or Large thumbnails. Click the folder tree or activate a directory in either content view to navigate. Back/Forward/Up use Alt+Left, Alt+Right, and Alt+Up. Ctrl+L focuses the editable address field. Details headers control sorting in both content views; selection survives view switches.

Each folder remembers its view, thumbnail size, and separate Details/Grid scroll positions. State is saved when leaving a folder or closing the window, including across application launches. Restoration waits for asynchronous loading/layout, and Qt clamps the saved position if the folder has become smaller. Media detection runs on the navigation worker; it does not decode files.

Window position, size, maximized state, dock/toolbar layout and visibility, pane sizes, details columns and sort order, similarity controls, and Back/Forward history are saved on close and restored on launch through QSettings. Explicit launch paths start a new navigation history. Active analysis and video playback remain session-only.

The [Preview Detail dock](docs/preview-detail.md) shows a thumbnail and Windows file/media properties for the selected item. Video previews include Play/Pause and a seek slider. Ctrl+Shift+P toggles the dock.

`platformdirs` supplies the user configuration location, which is registered as QSettings' user-scope INI default. On Windows the settings file is `%LOCALAPPDATA%\FileVoyager\FileVoyager.ini`. Folder paths are normalized and hashed as keys. Tests and benchmarks use isolated INI files rather than modifying these preferences.

This initial application browses folders. File opening, copy/move/delete, native context menus, and recursive search are not implemented.

## Thumbnail contract

The production image/video grid uses only the [Windows thumbnail service](docs/thumbnail-service.md), owned by the thumbnail-service workstream. It reads existing Shell thumbnails using flags `0x18`. It does not decode originals, generate thumbnails, warm the Windows cache, or substitute file icons for missing media thumbnails. Normal folder and non-media file icons remain available.

Uncached images produce the original native exception. PySide6 prints exceptions raised in Qt callbacks to the launching console; its event loop continues. Those cells remain undecorated. There is no custom error dialog or recovery provider. Automatic viewport refresh does not retry a failed request within that navigation/view generation. Native cache availability is required for populated image cells.

The adapter normalizes Qt's forward-slash paths to Windows native paths and converts owned BGR24 pixels into detached RGB32 QImages on workers. QPixmap/QIcon creation and painting remain on the UI thread.

## Performance design

- Asynchronous QFileSystemModel enumeration for content, shared Details/grid model and selection.
- A lazy folder tree scans/sorts directories on its own worker and inserts lightweight QStandardItemModel rows in batches of 128. Ancestor folders do not load file metadata into the UI just to reveal the current path. Directory watching keeps expanded branches current.
- Uniform grid geometry, batched layout (256 rows), lightweight delegate; no per-file widgets.
- Viewport-first requests plus one neighboring grid row, capped at 128 candidates.
- At most two native reads in flight; no executor backlog. Navigation and size changes discard stale results.
- A 64 MiB LRU budget for retained 32-bit thumbnail pixel payload. Qt objects, display resources, filesystem metadata, and in-flight images are additional memory.
- Thumbnail arrivals repaint affected grid cells without resetting or relaying out the model.
- Filesystem path resolution occurs on a separate navigation worker; rapid navigation keeps only the newest pending destination.

The shared filesystem source sorts both content views. This version uses Qt's file sorting, not a custom implementation of every Explorer sort convention. Supported image/video extensions are listed in `filevoyager/models.py`. Videos display their existing static Shell thumbnail in the grid and support playback in the Preview Detail dock. Arbitrary Shell thumbnail types are outside this initial scope.

## Standalone image processors

[Image processors](filevoyager/image_processors/README.md) expose Spectra-derived image feature functions and a uniform callable interface for future extractors. They use NumPy and Pillow. The [Media similarity dock](docs/image-similarity.md) analyzes existing image and video thumbnails for background comparison and DBSCAN sorting; thumbnail rendering continues to use the Windows Shell service.

## Verification

```powershell
uv run python -m unittest discover -s tests -v
uv run python tools/benchmark_ui.py --items 10000
uv run python tools/benchmark_ui.py --items 10000 --prefix my-profile --profile-callbacks
uv run python tools/benchmark_native_ui.py 'C:\Users\shoji\Pictures\Screenshots'
```

The first benchmark uses synthetic images solely to isolate the Qt pipeline. The native benchmark uses the production service and records real failures; it exits nonzero when any completed request failed. Both save measurements under ignored `.benchmarks/`. The native screenshot may contain personal content and is kept local.

See [measured results and limitations](docs/ui-performance.md), the [scrolling profile and fix](docs/scrolling-performance-validation.md), the [native service validation](docs/thumbnail-cache-validation.md), and the [saved Qt widget guide](.agents/references/pyside6-file-explorer/2026-10-31/WIDGET_GUIDE.md).
