# NTFS

This adapter supplies the [index contract](index.md) on Windows using the Master File Table and USN change journal. It assumes an already-authorized process with raw-volume access and a readable journal. Service deployment and elevation workflows are outside scope.

## Identity and metadata

| Core value | NTFS source |
| --- | --- |
| Source identity | Persistent volume identity; drive letter is a display root |
| Object identity | File reference including record number and sequence |
| Directory entry | Long-name link, parent reference and object reference |
| Object metadata | Standard information and unnamed data-stream logical size |
| Change position | Volume identity, journal identifier and next USN |

Keep each hardlink and exclude duplicate DOS short-name aliases. Translate native timestamps and attribute bits into catalog values. Do not follow reparse targets or index alternate streams as separate files.

## Enumeration

Discover local fixed NTFS volumes. Read volume geometry and the MFT data-run mapping, then scan in-use file records in buffered chunks. Apply record fixups and parse names, parents and required metadata. Handle fragmented extents and extension records containing required attributes.

Capture the journal position before scanning and consume subsequent changes before publishing readiness. No recursive directory walk is substituted for this path.

## Changes

Use `FSCTL_QUERY_USN_JOURNAL` to obtain journal state and `FSCTL_READ_USN_JOURNAL` to consume changes. Resolve rename pairs, deletions and hardlink changes into core update operations. Re-read affected records when journal events omit required metadata or link information.

Retain sequence identity to distinguish a reused MFT slot from its former object. Removing one hardlink must not remove its siblings. Commit the next USN with the changes it represents.

If required journal history or source access is unavailable, let the operation fail. Do not silently rescan, omit records or substitute incomplete metadata.

## Implementation references

The clone uses Rust and `windows-sys` for raw volume access: [volume reader](../src-tauri/src/infrastructure/ntfs/volume.rs), [MFT parser](../src-tauri/src/infrastructure/ntfs/mft.rs), [journal watcher](../src-tauri/src/infrastructure/ntfs/usn.rs). These implement platform concerns; the core catalog and search must not depend on their native structures.

Microsoft references: [journal operations](https://learn.microsoft.com/en-us/windows/win32/fileio/change-journal-operations) and [journal identifiers](https://learn.microsoft.com/en-us/windows/win32/fileio/using-the-change-journal-identifier).
