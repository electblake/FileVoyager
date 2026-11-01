# Windows NTFS, MFT, and USN references

Reference date: 2026-11-01. Captured for FileVoyager using the reference-powers:reference-mirror skill.

This bundle preserves 36 official Microsoft documentation pages covering NTFS metadata indexing, MFT record structures, USN enumeration/change tracking, raw volume access, and the separate Windows Search indexing service. It is a documentation snapshot, not a claim of a complete NTFS on-disk specification or an implementation proposal.

Start with [REFERENCE_SUMMARY.md](REFERENCE_SUMMARY.md), then use [REFERENCE_INDEX.md](REFERENCE_INDEX.md) to open local mirrors. [SOURCE_URLS.md](SOURCE_URLS.md) lists captured official URLs. Markdown mirrors retain source and retrieval metadata and the Microsoft page metadata provided by the server.

## Contents

- `learn.microsoft.com/`: official source mirrors, including Win32 API reference, Developer Notes, Microsoft Open Specifications, and Windows Server command documentation.
- `fixtures/user-drop-001-ntfs-adapter-spec.md`: exact copy of the user-provided `S:/Spaces/File-Organization/AllTheThings/specs/ntfs.md`. This is project reference material, not Microsoft documentation or instructions authorizing implementation. Its original relative links are preserved and are not necessarily resolvable from the fixture directory.
- `capture-manifest.json`: initial 33-page capture and llms.txt discovery result.
- `capture-manifest-ntfs-v0.json`: three additional NTFS V0 API structure references.

All 36 selected pages were captured. The discovery request to https://learn.microsoft.com/llms.txt returned HTTP 404; no llms.txt content or discovered links were available. No alternative source was substituted.

No project code, volume contents, journal configuration, or Windows Search settings were changed. Commands appearing in mirrored documentation are reference examples and were not executed.
