# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Added a Refresh button and F5 shortcut to rescan the current folder asynchronously.
- Added View → Theme with a qt-themes dropdown, an Apply button, and a saved application-wide theme selection.

### Changed

- Replaced Back, Forward, and Up navigation labels with Qt's built-in icons.

### Fixed

- Preserved the existing Qt Fusion style when applying themes to avoid restyling every widget; verified all 14 themes preserve browser selection, scrolling, and thumbnail generation.

## [0.1.8] - 2026-11-01

### Added

- Added Alt-drag Windows shortcut creation in Details, Grid, and the folder tree, with native link-cursor feedback.

### Changed

- Enabled thumbnail generation through Windows Shell `GetImage`, letting Windows cache missing thumbnails while preserving bounded background scheduling.
- Moved large-folder metadata loading, natural sorting, and folder-tree comparisons to background workers, with bounded Qt model updates and four cached directory listings.
- Used fixed-height table rows for Details and compact Qt selection ranges for responsive large selections and drag interactions.

### Fixed

- Reduced initial-loading pauses and scrolling gaps in 50,000-item folders while preserving selection, sorting, renaming, and live filesystem updates.
- Preserved completed grid layouts when reopening an unchanged folder at the same thumbnail size.

## [0.1.7] - 2026-11-01

### Added

- Added F2 inline renaming in Details and Grid, with Enter to save and Escape to cancel.
- Added Help → Keyboard Shortcuts with searchable, sortable action/default/custom columns and custom key combinations saved through QSettings.
- Added background Pack to Folder and Flatten operations for selected items, including an optional copy mode when packing.
- Added right-click menus for Details, Grid, and folder-tree items, reusing Flatten, Pack to Folder, and Rename operations while preserving multi-selection.

### Fixed

- Handled folder rename conflicts with a merge confirmation showing both folders and creation dates, followed by Replace, Skip, or Cancel prompts for duplicate files.
- Refreshed the preview and similarity reference after renaming an item.

## [0.1.6] - 2026-11-01

### Added

- Added a pinned, SHA-256-verified FFmpeg 9.0.2 shared-library download to Windows Setup, stored beside the venv under the platformdirs application-data directory and removed on uninstall.

### Changed

- Consolidated Qt test setup and event-loop waits, reused media and native fixtures, and removed redundant window and interpreter startups while retaining native playback, filesystem, and installer-handoff checks.

### Fixed

- Loaded the installer-managed FFmpeg DLLs by absolute path before Qt creates its media backend, replacing the unused standalone-executable payload.
- Removed a timing race in the stale-preview test and synchronized installer-handoff checks with the helper's native process waits.

## [0.1.5] - 2026-11-01

### Added

- Added a movable Preview Detail dock with background thumbnail and Windows file/media property loading.
- Added inline video playback, play/pause controls, and paused-frame seeking in the preview dock.
- Remembered the last folder across launches, with explicit launch paths taking precedence.
- Saved and restored window geometry, maximized state, dock and toolbar layout, pane sizes, details columns and sorting, similarity controls, and navigation history through QSettings.

### Fixed

- Changed similarity sorting to analyze existing Windows Shell thumbnails for all grid-supported media, including videos, instead of decoding image originals.
- Enabled videos as comparison references and renamed the dock and controls to Media similarity.

## [0.1.4] - 2026-10-31

### Added

- Added uniform vector comparison and DBSCAN clustering interfaces with one-neighborhood-at-a-time memory use.
- Added a movable Image similarity dock on the right with DBSCAN distance/minimum-neighbor settings, six feature weights, background analysis, cancellation, and shared Grid/Details sorting.

### Fixed

- Waited for the grid scrollbar extent to finish its batched layout before restoring saved positions with the sorting proxy.

## [0.1.3] - 2026-10-31

### Added

- Added File â†’ Quit, saving QSettings before shutdown, and Help â†’ Check for updates with GitHub release checks, download progress, and staged update buttons.
- Added an installer handoff that waits for both FileVoyager and its installed launcher to exit before starting Setup.

## [0.1.2] - 2026-10-31

### Changed

- Bumped the package and Windows installer to 0.1.2 without changing application behavior or runtime dependencies.

## [0.1.1] - 2026-10-31

### Added

- Added a per-user Windows x64 Inno Setup installer that installs private Python 3.12, creates a platformdirs-managed venv, and installs the application wheel and hash-locked PyPI dependencies.
- Documented Qt for Python Community Edition licensing and added installer failure exit-code checks.
- Added a revision-pinned Spectra reference bundle documenting image feature formulas, weights, dependencies, and upstream tests.
- Added standalone Spectra image feature functions, a uniform callable extractor interface, and NumPy/Pillow dependencies without application integration.
- Added the initial Windows file browser with a folder tree, sortable Details view, thumbnail grid, shared selection, and Back/Forward/Up navigation.
- Added cache-only Windows Shell thumbnails for images and videos using `comtypes` and `ctypes`, without thumbnail generation or icon substitution.
- Added bounded background thumbnail requests, viewport-first scheduling, a 64 MiB pixel cache, and stale-result rejection.
- Added asynchronous folder-tree scanning with bounded UI updates and directory-change tracking.
- Added per-folder view, thumbnail-size, and scroll-position preferences, plus automatic Grid selection for media folders.
- Added the `filevoyager` launcher, dependency lockfile, automated tests, and synthetic and real-media benchmark tools.
- Added local Qt, Windows Shell, and `comtypes` reference bundles, API documentation, and performance validation reports.

### Fixed

- Updated grid scrollbar geometry before restoring a saved position after batched layout.
- Normalized Qt file paths before Windows Shell thumbnail requests.
- Prevented automatic retries of failed thumbnail requests within the same navigation/view generation.
- Removed the measured 10,000-item scrolling stall caused by ancestor-folder enumeration on the UI thread.
- Restored saved grid scroll positions only after the destination folder's batched layout completed.
