# Reference summary

Reference date: **2026-11-01**. Platform: Microsoft Windows, NTFS, Win32 filesystem APIs, and Windows Search. This is a capture of the published pages on that date, not a Windows build or SDK release snapshot. No local volume format version was measured.

## Distinguish the three kinds of index

1. **NTFS metadata and directory indexes.** The MFT stores file records and attributes. NTFS directory streams use index-related attributes; `$INDEX_ROOT` and `$INDEX_ALLOCATION` are filesystem structures, not a Windows Search database. See [MFT overview](learn.microsoft.com/en-us/windows/win32/devnotes/master-file-table.md), [file streams](learn.microsoft.com/en-us/windows/win32/fileio/file-streams.md), and [MS-FSCC NTFS attribute types](learn.microsoft.com/en-us/openspecs/windows_protocols/ms-fscc/a82e9105-2405-4e37-b2c3-28c773902d85.md).
2. **An application's MFT/USN catalog.** The captured APIs support enumerating file records and consuming subsequent journal changes. An application's catalog, parent relationships, queries, and synchronization are separate application responsibilities. `FSCTL_ENUM_USN_DATA` and `FSCTL_READ_USN_JOURNAL` are distinct operations; neither is itself a persistent application search database. See [enumeration](learn.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_enum_usn_data.md) and [journal reading](learn.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_read_usn_journal.md).
3. **Windows Search.** A separate service crawls configured scope, extracts properties/content, and maintains a search catalog. Its NTFS change notifications use the USN journal. See [Windows Search indexing process](learn.microsoft.com/en-us/windows/win32/search/search-indexing-process-overview.md). This is contextual documentation, not a proposal to replace FileVoyager's backend with Windows Search.

## MFT structures and raw access

The [MFT Developer Notes](learn.microsoft.com/en-us/windows/win32/devnotes/master-file-table.md) cover file-record segments, attributes, and extension records. The bundle includes FILE_RECORD_SEGMENT_HEADER, ATTRIBUTE_RECORD_HEADER, ATTRIBUTE_LIST_ENTRY, FILE_NAME, MFT_SEGMENT_REFERENCE, MULTI_SECTOR_HEADER, and STANDARD_INFORMATION.

The [file-record header](learn.microsoft.com/en-us/windows/win32/devnotes/file-record-segment-header.md) documentation explicitly limits that structure to **NTFS major version 3, minor version 0 or 1**. It describes sequence numbers used to identify obsolete file references and the update sequence array used for multisector protection. Do not confuse the on-disk update sequence array with the USN change journal.

For platform access, read [CreateFileW](learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew.md), [FSCTL_GET_NTFS_VOLUME_DATA](learn.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_get_ntfs_volume_data.md), and [FSCTL_GET_RETRIEVAL_POINTERS](learn.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_get_retrieval_pointers.md). These document volume handles, geometry, and extent mappings; they do not supply a complete raw MFT scanner.

[FSCTL_GET_NTFS_FILE_RECORD](learn.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_get_ntfs_file_record.md) returns an in-use record at or below the requested reference number. The returned identity is therefore not necessarily the requested identity. Multiple records belonging to a file must be retrieved individually. The page explicitly lists SMB 3.0 and ReFS as unsupported for this operation.

## USN enumeration and change tracking

Start with [change journals](learn.microsoft.com/en-us/windows/win32/fileio/change-journals.md), [operations](learn.microsoft.com/en-us/windows/win32/fileio/change-journal-operations.md), and [journal identifiers](learn.microsoft.com/en-us/windows/win32/fileio/using-the-change-journal-identifier.md). Journal identity and position are distinct; journal replacement can invalidate prior state. Microsoft's identifier page documents administrator privileges for these journal operations.

The bundle includes NTFS-oriented **MFT_ENUM_DATA_V0**, **READ_USN_JOURNAL_DATA_V0**, and **USN_JOURNAL_DATA_V0**, as well as newer V1/V2 structures for understanding version boundaries. **MFT_ENUM_DATA_V1** is documented for ReFS; a higher structure suffix is not automatically the correct NTFS choice.

Record formats **USN_RECORD_V2**, **V3**, and **V4** are preserved separately. V4 documents range tracking and lists **Windows 8.1 / Windows Server 2012 R2** as minimum supported platforms. Do not treat the versions as interchangeable layouts. Use the [buffer-walking reference](learn.microsoft.com/en-us/windows/win32/fileio/walking-a-buffer-of-change-journal-records.md) alongside the record definitions. [MS-FSCC USN_RECORD_V2](learn.microsoft.com/en-us/openspecs/windows_protocols/ms-fscc/d2a2b53e-bf78-4ef3-90c7-21b918fab304.md) provides an Open Specifications representation.

The [fsutil usn reference](learn.microsoft.com/en-us/windows-server/administration/windows-commands/fsutil-usn.md) documents administrative inspection and modification commands. None were run for this capture.

## Scope and compatibility limits

- These are selected official specifications and API contracts, not a complete independently sufficient specification of every NTFS on-disk structure. Directory B-tree layout and all mapping-pair/fixup edge cases are not claimed to be fully covered.
- API pages preserve per-function OS minimums and filesystem support tables. Their differing requirements must not be generalized into one universal minimum Windows version.
- Capture metadata includes retrieval timestamps; source frontmatter retains publication/update dates where supplied. Retrieval date does not imply a recent technical revision.
- No performance benchmark, raw-volume access test, or local journal inspection was performed. Any FileVoyager performance expectation remains separate from these official source facts.

## User-provided context

The [adapter specification fixture](fixtures/user-drop-001-ntfs-adapter-spec.md) proposes buffered raw MFT scanning followed by USN reconciliation, with explicit raw-access prerequisites and no substituted enumeration path. It is preserved exactly as user context. Microsoft documentation about Windows Search recovery behavior does not override that specification or the project's fail-fast policy.

