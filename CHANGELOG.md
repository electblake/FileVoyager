# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1] - 2026-10-31

### Added

- Added a locked PyInstaller build, dependency notices, and a per-user Windows x64 Inno Setup installer.
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

- Normalized Qt file paths before Windows Shell thumbnail requests.
- Prevented automatic retries of failed thumbnail requests within the same navigation/view generation.
- Removed the measured 10,000-item scrolling stall caused by ancestor-folder enumeration on the UI thread.
- Restored saved grid scroll positions only after the destination folder's batched layout completed.
