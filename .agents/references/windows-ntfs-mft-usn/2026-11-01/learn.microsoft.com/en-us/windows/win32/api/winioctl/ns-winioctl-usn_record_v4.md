<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-usn_record_v4
retrieved: 2026-11-01T19:21:29.545678+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-usn_record_v4
content_type: text/markdown
-->

---
layout: Conceptual
title: USN_RECORD_V4 - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-usn_record_v4
adobe-target: true
breadcrumb_path: /windows/desktop/api/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-WinDevCenter
ms.service: windows-api-desktop-tech
ms.subservice: sdk-api-reference
ms.topic: reference
ms.author: kbridge
author: karl-bridge-microsoft
feedback_system: Standard
feedback_product_url: https://www.microsoft.com/en-us/windowsinsider/feedbackhub/fb
feedback_help_link_url: https://learn.microsoft.com/answers/tags/224/windows-api-win32/
feedback_help_link_type: get-help-at-qna
UID: NS:winioctl.USN_RECORD_V4
description: Contains the information for an update sequence number (USN) change journal version 4.0 record. The version 2.0 and 3.0 records are defined by the USN_RECORD_V2 (also called USN_RECORD) and USN_RECORD_V3 structures respectively.
old-location: fs\usn_record_v4.htm
tech.root: fs
ms.assetid: 2636D1A1-6FD1-4F84-954C-499DCCE6E390
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: '*PUSN_RECORD_V4, PUSN_RECORD_V4, PUSN_RECORD_V4 structure pointer [Files], USN_REASON_BASIC_INFO_CHANGE, USN_REASON_CLOSE, USN_REASON_COMPRESSION_CHANGE, USN_REASON_DATA_EXTEND, USN_REASON_DATA_OVERWRITE, USN_REASON_DATA_TRUNCATION, USN_REASON_EA_CHANGE, USN_REASON_ENCRYPTION_CHANGE, USN_REASON_FILE_CREATE, USN_REASON_FILE_DELETE, USN_REASON_HARD_LINK_CHANGE, USN_REASON_INDEXABLE_CHANGE, USN_REASON_INTEGRITY_CHANGE, USN_REASON_NAMED_DATA_EXTEND, USN_REASON_NAMED_DATA_OVERWRITE, USN_REASON_NAMED_DATA_TRUNCATION, USN_REASON_OBJECT_ID_CHANGE, USN_REASON_RENAME_NEW_NAME, USN_REASON_RENAME_OLD_NAME, USN_REASON_REPARSE_POINT_CHANGE, USN_REASON_SECURITY_CHANGE, USN_REASON_STREAM_CHANGE, USN_REASON_TRANSACTED_CHANGE, USN_RECORD_V4, USN_RECORD_V4 structure [Files], USN_SOURCE_AUXILIARY_DATA, USN_SOURCE_CLIENT_REPLICATION_MANAGEMENT, USN_SOURCE_DATA_MANAGEMENT, USN_SOURCE_REPLICATION_MANAGEMENT, fs.usn_record_v4, winioctl/PUSN_RECORD_V4, winioctl/USN_RECORD_V4'
req.header: winioctl.h
req.include-header: Windows.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1 [desktop apps only]
req.target-min-winversvr: Windows Server 2012 R2 [desktop apps only]
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
targetos: Windows
req.typenames: USN_RECORD_V4, *PUSN_RECORD_V4
req.redist: 
topic_type:
- APIRef
- kbSyntax
api_type:
- HeaderDef
api_location:
- WinIoCtl.h
api_name:
- USN_RECORD_V4
locale: en-us
document_id: 52bff10e-3159-395a-6f95-81ccb4168291
document_version_independent_id: 17978d0a-7102-a648-c51a-11b575cc146a
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/winioctl/ns-winioctl-usn_record_v4.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/winioctl/ns-winioctl-usn_record_v4.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_fs/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 1362
asset_id: winioctl/ns-winioctl-usn_record_v4
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/winioctl/ns-winioctl-usn_record_v4.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d774b87-7dcb-40bf-a0b9-5a7a9efff0d1
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/89dc5f37-0e4e-4b05-ad87-5fcd2b941a8a
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
platformId: a6adee46-c78d-e8ba-5cf0-db5914f0552a
---

# USN_RECORD_V4 - Win32 apps | Microsoft Learn

Contains the information for an update sequence number (USN) change journal version 4.0 record. The version 2.0 and 3.0 records are defined by the [USN_RECORD_V2](/en-us/windows/desktop/api/winioctl/ns-winioctl-usn_record_v2) (also called **USN\_RECORD**) and [USN_RECORD_V3](/en-us/windows/desktop/api/winioctl/ns-winioctl-usn_record_v3) structures respectively.

## Syntax

```cpp
typedef struct {
  USN_RECORD_COMMON_HEADER Header;
  FILE_ID_128              FileReferenceNumber;
  FILE_ID_128              ParentFileReferenceNumber;
  USN                      Usn;
  DWORD                    Reason;
  DWORD                    SourceInfo;
  DWORD                    RemainingExtents;
  WORD                     NumberOfExtents;
  WORD                     ExtentSize;
  USN_RECORD_EXTENT        Extents[1];
} USN_RECORD_V4, *PUSN_RECORD_V4;
```

## Members

`Header`

A [USN_RECORD_COMMON_HEADER](/en-us/windows/desktop/api/winioctl/ns-winioctl-usn_record_common_header) structure that describes the record length, major version, and minor version for the record.

`FileReferenceNumber`

The 128-bit ordinal number of the file or directory for which this record notes changes.

This value is an arbitrarily assigned value that associates a journal record with a file.

`ParentFileReferenceNumber`

The 128-bit ordinal number of the directory where the file or directory that is associated with this record is located.

This value is an arbitrarily assigned value that associates a journal record with a parent directory.

`Usn`

The USN of this record.

`Reason`

The flags that identify reasons for changes that have accumulated in this file or directory journal record since the file or directory opened.

When a file or directory closes, then a final USN record is generated with the **USN\_REASON\_CLOSE** flag set. The next change (for example, after the next open operation or deletion) starts a new record with a new set of reason flags.

A rename or move operation generates two USN records, one that records the old parent directory for the item, and one that records a new parent.

The following table identifies the possible flags.
**Note** Unused bits are reserved.

| Value | Meaning |
| --- | --- |
| - **USN\_REASON\_BASIC\_INFO\_CHANGE**<br>- 0x00008000 | A user has either changed one or more file or directory attributes (for example, the read-only, hidden, system, archive, or sparse attribute), or one or more time stamps. |
| - **USN\_REASON\_CLOSE**<br>- 0x80000000 | The file or directory is closed. |
| - **USN\_REASON\_COMPRESSION\_CHANGE**<br>- 0x00020000 | The compression state of the file or directory is changed from or to compressed. |
| - **USN\_REASON\_DATA\_EXTEND**<br>- 0x00000002 | The file or directory is extended (added to). |
| - **USN\_REASON\_DATA\_OVERWRITE**<br>- 0x00000001 | The data in the file or directory is overwritten. |
| - **USN\_REASON\_DATA\_TRUNCATION**<br>- 0x00000004 | The file or directory is truncated. |
| - **USN\_REASON\_EA\_CHANGE**<br>- 0x00000400 | The user made a change to the extended attributes of a file or directory. <br>These NTFS file system attributes are not accessible to Windows-based applications. |
| - **USN\_REASON\_ENCRYPTION\_CHANGE**<br>- 0x00040000 | The file or directory is encrypted or decrypted. |
| - **USN\_REASON\_FILE\_CREATE**<br>- 0x00000100 | The file or directory is created for the first time. |
| - **USN\_REASON\_FILE\_DELETE**<br>- 0x00000200 | The file or directory is deleted. |
| - **USN\_REASON\_HARD\_LINK\_CHANGE**<br>- 0x00010000 | An NTFS file system hard link is added to or removed from the file or directory. <br>An NTFS file system hard link, similar to a POSIX hard link, is one of several directory entries that see the same file or directory. |
| - **USN\_REASON\_INDEXABLE\_CHANGE**<br>- 0x00004000 | A user changes the **FILE\_ATTRIBUTE\_NOT\_CONTENT\_INDEXED** attribute. <br>That is, the user changes the file or directory from one where content can be indexed to one where content cannot be indexed, or vice versa. Content indexing permits rapid searching of data by building a database of selected content. |
| - **USN\_REASON\_INTEGRITY\_CHANGE**<br>- 0x00800000 | A user changed the state of the **FILE\_ATTRIBUTE\_INTEGRITY\_STREAM** attribute for the given stream. <br>On the ReFS file system, integrity streams maintain a checksum of all data for that stream, so that the contents of the file can be validated during read or write operations. |
| - **USN\_REASON\_NAMED\_DATA\_EXTEND**<br>- 0x00000020 | The one or more named data streams for a file are extended (added to). |
| - **USN\_REASON\_NAMED\_DATA\_OVERWRITE**<br>- 0x00000010 | The data in one or more named data streams for a file is overwritten. |
| - **USN\_REASON\_NAMED\_DATA\_TRUNCATION**<br>- 0x00000040 | The one or more named data streams for a file is truncated. |
| - **USN\_REASON\_OBJECT\_ID\_CHANGE**<br>- 0x00080000 | The object identifier of a file or directory is changed. |
| - **USN\_REASON\_RENAME\_NEW\_NAME**<br>- 0x00002000 | A file or directory is renamed, and the file name in the **USN\_RECORD\_V4** structure is the new name. |
| - **USN\_REASON\_RENAME\_OLD\_NAME**<br>- 0x00001000 | The file or directory is renamed, and the file name in the **USN\_RECORD\_V4** structure is the previous name. |
| - **USN\_REASON\_REPARSE\_POINT\_CHANGE**<br>- 0x00100000 | The reparse point that is contained in a file or directory is changed, or a reparse point is added to or deleted from a file or directory. |
| - **USN\_REASON\_SECURITY\_CHANGE**<br>- 0x00000800 | A change is made in the access rights to a file or directory. |
| - **USN\_REASON\_STREAM\_CHANGE**<br>- 0x00200000 | A named stream is added to or removed from a file, or a named stream is renamed. |
| - **USN\_REASON\_TRANSACTED\_CHANGE**<br>- 0x00400000 | The given stream is modified through a committed TxF transaction. |

`SourceInfo`

Additional information about the source of the change, set by the [FSCTL_MARK_HANDLE](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_mark_handle) of the [DeviceIoControl](/en-us/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) operation.

When a thread writes a new USN record, the source information flags in the prior record continue to be present only if the thread also sets those flags. Therefore, the source information structure allows applications to filter out USN records that are set only by a known source, for example, an antivirus filter.

One of the following values can be set.

| Value | Meaning |
| --- | --- |
| - **USN\_SOURCE\_AUXILIARY\_DATA**<br>- 0x00000002 | The operation adds a private data stream to a file or directory. <br>One example is a virus detector adding checksum information. As the virus detector modifies the item, the system generates USN records. **USN\_SOURCE\_AUXILIARY\_DATA** indicates that the modifications did not change the application data. |
| - **USN\_SOURCE\_DATA\_MANAGEMENT**<br>- 0x00000001 | The operation provides information about a change to the file or directory made by the operating system. <br>A typical use is when the Remote Storage system moves data from external to local storage. Remote Storage is the hierarchical storage management software. Such a move usually at a minimum adds the **USN\_REASON\_DATA\_OVERWRITE** flag to a USN record. However, the data has not changed from the user's point of view. By noting **USN\_SOURCE\_DATA\_MANAGEMENT** in the **SourceInfo** member, you can determine that although a write operation is performed on the item, data has not changed. |
| - **USN\_SOURCE\_REPLICATION\_MANAGEMENT**<br>- 0x00000004 | The operation is modifying a file to match the contents of the same file which exists in another member of the replica set. |
| - **USN\_SOURCE\_CLIENT\_REPLICATION\_MANAGEMENT**<br>- 0x00000008 | The operation is modifying a file on client systems to match the contents of the same file that exists in the cloud. |

`RemainingExtents`

The number of extents that remain after the current **USN\_RECORD\_V4** record. Multiple version 4.0 records may be required to describe all of the modified extents for a given file. When the **RemainingExtents** member is 0, the current **USN\_RECORD\_V4** record is the last **USN\_RECORD\_V4** record for the file. The last **USN\_RECORD\_V4** entry for a given file is always followed by a [USN_RECORD_V3](/en-us/windows/desktop/api/winioctl/ns-winioctl-usn_record_v3) record with at least the **USN\_REASON\_CLOSE** flag set.

`NumberOfExtents`

The number of extents in current **USN\_RECORD\_V4** entry.

`ExtentSize`

The size of each [USN_RECORD_EXTENT](/en-us/windows/desktop/api/winioctl/ns-winioctl-usn_record_extent) structure in the **Extents** member, in bytes.

`Extents[1]`

An array of [USN_RECORD_EXTENT](/en-us/windows/desktop/api/winioctl/ns-winioctl-usn_record_extent) structures that represent the extents in the **USN\_RECORD\_V4** entry.

## Remarks

A **USN\_RECORD\_V4** record is only output when range tracking is turned on and the file size is equal or larger than the value of the **RangeTrackFileSizeThreshold** member. The user always receives one or more **USN\_RECORD\_V4** records followed by one [USN_RECORD_V3](/en-us/windows/desktop/api/winioctl/ns-winioctl-usn_record_v3) record.

To provide a path forward compatibility in change journal clients, Microsoft provides a major and minor version number of the change journal software in the **USN\_RECORD\_V4** structure. Your code should examine these values, examine its own compatibility with the change journal software, and gracefully handle any incompatibility if necessary.

A change in the minor version number indicates that the existing **USN\_RECORD\_V4** structure members are still valid, but that new members may have been added between the penultimate member and the last, which is a variable-length string.

To handle such a change gracefully, your code should not do any compile-time pointer arithmetic that relies on the location of the last member. For example, a change in the minor version number makes the `sizeof(USN_RECORD)` call unreliable. Instead, rely on run-time calculations that use the **RecordLength** member.

An increase in the major version number of the change journal software indicates that the **USN\_RECORD\_V4** structure may have undergone major changes, and that the current definition may not be reliable. If your code detects a change in the major version number of the change journal software, the code should not work with the change journal.

For more information, see [Creating, Modifying, and Deleting a Change Journal](/en-us/windows/desktop/FileIO/creating-modifying-and-deleting-a-change-journal).

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows 8.1 [desktop apps only] |
| **Minimum supported server** | Windows Server 2012 R2 [desktop apps only] |
| **Header** | winioctl.h (include Windows.h) |
