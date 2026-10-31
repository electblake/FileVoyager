# FileVoyager: Windows Shell cached thumbnails

Reference date: 2026-10-31.

Review and source bundle for FileVoyager's primary thumbnail-loading path: use the Windows Shell's existing shared thumbnail cache through IShellItemImageFactory, without generating thumbnails or substituting icons.

- [Reviewed loading contract](REFERENCE_SUMMARY.md)
- [Source inventory](SOURCE_URLS.md)
- [Navigation index](REFERENCE_INDEX.md)
- [Original user research](fixtures/user-drop-001-user-thumbnail-research.md)

This is a documentation review, not an implemented or runtime-tested loader. The original research is preserved separately, including its joined flag declarations. The summary supplies readable declarations and implementation constraints.
