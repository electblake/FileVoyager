<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-usn_record_v2
retrieved: 2026-11-01T19:21:28.692079+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-usn_record_v2
content_type: text/markdown
-->

---
layout: Conceptual
title: USN_RECORD_V2 - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-usn_record_v2
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
UID: NS:winioctl.USN_RECORD_V2
description: Contains the information for an update sequence number (USN) change journal version 2.0 record.
old-location: fs\usn_record_str.htm
tech.root: fs
ms.assetid: 1747453d-fd18-4853-a953-47131f3067ae
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: '*PUSN_RECORD, *PUSN_RECORD_V2, PUSN_RECORD, PUSN_RECORD structure pointer [Files], PUSN_RECORD_V2, PUSN_RECORD_V2 structure pointer [Files], USN_REASON_BASIC_INFO_CHANGE, USN_REASON_CLOSE, USN_REASON_COMPRESSION_CHANGE, USN_REASON_DATA_EXTEND, USN_REASON_DATA_OVERWRITE, USN_REASON_DATA_TRUNCATION, USN_REASON_EA_CHANGE, USN_REASON_ENCRYPTION_CHANGE, USN_REASON_FILE_CREATE, USN_REASON_FILE_DELETE, USN_REASON_HARD_LINK_CHANGE, USN_REASON_INDEXABLE_CHANGE, USN_REASON_INTEGRITY_CHANGE, USN_REASON_NAMED_DATA_EXTEND, USN_REASON_NAMED_DATA_OVERWRITE, USN_REASON_NAMED_DATA_TRUNCATION, USN_REASON_OBJECT_ID_CHANGE, USN_REASON_RENAME_NEW_NAME, USN_REASON_RENAME_OLD_NAME, USN_REASON_REPARSE_POINT_CHANGE, USN_REASON_SECURITY_CHANGE, USN_REASON_STREAM_CHANGE, USN_REASON_TRANSACTED_CHANGE, USN_RECORD, USN_RECORD structure [Files], USN_RECORD_V2, USN_RECORD_V2 structure [Files], USN_SOURCE_AUXILIARY_DATA, USN_SOURCE_CLIENT_REPLICATION_MANAGEMENT, USN_SOURCE_DATA_MANAGEMENT, USN_SOURCE_REPLICATION_MANAGEMENT, _win32_usn_record_str, base.usn_record_str, fs.usn_record_str, winioctl/PUSN_RECORD, winioctl/PUSN_RECORD_V2, winioctl/USN_RECORD'
req.header: winioctl.h
req.include-header: Windows.h
req.target-type: Windows
req.target-min-winverclnt: Windows XP [desktop apps only]
req.target-min-winversvr: Windows Server 2003 [desktop apps only]
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
req.typenames: USN_RECORD_V2, *PUSN_RECORD_V2
req.redist: 
topic_type:
- APIRef
- kbSyntax
api_type:
- HeaderDef
api_location:
- WinIoCtl.h
api_name:
- USN_RECORD_V2
locale: en-us
document_id: e4334110-aa72-0d19-0ed1-327888e33af1
document_version_independent_id: edb63d7e-0f4c-bd6a-17df-78432ef52b48
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/winioctl/ns-winioctl-usn_record_v2.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/winioctl/ns-winioctl-usn_record_v2.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_fs/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 1716
asset_id: winioctl/ns-winioctl-usn_record_v2
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/winioctl/ns-winioctl-usn_record_v2.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d774b87-7dcb-40bf-a0b9-5a7a9efff0d1
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/89dc5f37-0e4e-4b05-ad87-5fcd2b941a8a
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
platformId: 5d31753b-6ae3-cc59-e825-1bb33d84b238
---

# USN_RECORD_V2 - Win32 apps | Microsoft Learn

Contains the information for an update sequence number (USN) change journal version 2.0 record. Applications should not attempt to work with change journal versions earlier than 2.0. Prior to Windows 8 and Windows Server 2012 this structure was named **USN\_RECORD**. Use that name to compile with older SDKs and compilers.

## Syntax

```cpp
typedef struct {
  DWORD         RecordLength;
  WORD          MajorVersion;
  WORD          MinorVersion;
  DWORDLONG     FileReferenceNumber;
  DWORDLONG     ParentFileReferenceNumber;
  USN           Usn;
  LARGE_INTEGER TimeStamp;
  DWORD         Reason;
  DWORD         SourceInfo;
  DWORD         SecurityId;
  DWORD         FileAttributes;
  WORD          FileNameLength;
  WORD          FileNameOffset;
  WCHAR         FileName[1];
} USN_RECORD_V2, *PUSN_RECORD_V2;
```

## Members

`RecordLength`

The total length of a record, in bytes.

Because **USN\_RECORD\_V2** is a variable size, the **RecordLength** member should be used when calculating the address of the next record in an output buffer, for example, a buffer that is returned from operations for the [DeviceIoControl](/en-us/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) function that work with **USN\_RECORD\_V2**.

The size in bytes of any change journal record is at most the size of the **USN\_RECORD\_V2** structure, plus *MaximumComponentLength* characters minus 1 (for the character declared in the structure) times the size of a wide character. The value of *MaximumComponentLength* may be determined by calling the[GetVolumeInformation](/en-us/windows/desktop/api/fileapi/nf-fileapi-getvolumeinformationa) function. In C, you can determine a record size by using the following code example.

| C++ |
| --- |
| ```<br>  MaximumChangeJournalRecordSize = <br>      ( MaximumComponentLength * sizeof(WCHAR) <br>        + sizeof(USN_RECORD)   + sizeof(WCHAR) );<br>``` |

 To maintain compatibility across version changes of the change journal software, use a run-time calculation to determine the size of the **USN\_RECORD\_V2** structure. For more information about compatibility across version changes, see the Remarks section in this topic. 
`MajorVersion`

The major version number of the change journal software for this record.

For example, if the change journal software is version 2.0, the major version number is 2.

| Value | Meaning |
| --- | --- |
| - 2 | The structure is a **USN\_RECORD\_V2** structure and the remainder of the structure should be parsed using that layout. |
| - 3 | The structure is a [USN_RECORD_V3](/en-us/windows/desktop/api/winioctl/ns-winioctl-usn_record_v3) structure and the remainder of the structure should be parsed using that layout. |
| - 4 | The structure is a [USN\_RECORD\_V4 structure](ns-winioctl-usn\_record\_v4.md) and the remainder of the structure should be parsed using that layout. |

`MinorVersion`

The minor version number of the change journal software for this record. For example, if the change journal software is version 2.0, the minor version number is zero.

`FileReferenceNumber`

The ordinal number of the file or directory for which this record notes changes.

This is an arbitrarily assigned value that associates a journal record with a file.

`ParentFileReferenceNumber`

The ordinal number of the directory where the file or directory that is associated with this record is located.

This is an arbitrarily assigned value that associates a journal record with a parent directory.

`Usn`

The USN of this record.

`TimeStamp`

The standard UTC time stamp ([FILETIME](/en-us/windows/desktop/api/minwinbase/ns-minwinbase-filetime)) of this record, in 64-bit format.

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
| - **USN\_REASON\_RENAME\_NEW\_NAME**<br>- 0x00002000 | A file or directory is renamed, and the file name in the **USN\_RECORD\_V2** structure is the new name. |
| - **USN\_REASON\_RENAME\_OLD\_NAME**<br>- 0x00001000 | The file or directory is renamed, and the file name in the **USN\_RECORD\_V2** structure is the previous name. |
| - **USN\_REASON\_REPARSE\_POINT\_CHANGE**<br>- 0x00100000 | The reparse point that is contained in a file or directory is changed, or a reparse point is added to or deleted from a file or directory. |
| - **USN\_REASON\_SECURITY\_CHANGE**<br>- 0x00000800 | A change is made in the access rights to a file or directory. |
| - **USN\_REASON\_STREAM\_CHANGE**<br>- 0x00200000 | A named stream is added to or removed from a file, or a named stream is renamed. |
| - **USN\_REASON\_TRANSACTED\_CHANGE**<br>- 0x00400000 | The given stream is modified through a TxF transaction. |

`SourceInfo`

Additional information about the source of the change, set by the [FSCTL_MARK_HANDLE](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_mark_handle) of the [DeviceIoControl](/en-us/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) operation.

When a thread writes a new USN record, the source information flags in the prior record continues to be present only if the thread also sets those flags. Therefore, the source information structure allows applications to filter out USN records that are set only by a known source, for example, an antivirus filter.

One of the two following values can be set.

| Value | Meaning |
| --- | --- |
| - **USN\_SOURCE\_AUXILIARY\_DATA**<br>- 0x00000002 | The operation adds a private data stream to a file or directory. <br>An example might be a virus detector adding checksum information. As the virus detector modifies the item, the system generates USN records. **USN\_SOURCE\_AUXILIARY\_DATA** indicates that the modifications did not change the application data. |
| - **USN\_SOURCE\_DATA\_MANAGEMENT**<br>- 0x00000001 | The operation provides information about a change to the file or directory made by the operating system. <br>A typical use is when the Remote Storage system moves data from external to local storage. Remote Storage is the hierarchical storage management software. Such a move usually at a minimum adds the **USN\_REASON\_DATA\_OVERWRITE** flag to a USN record. However, the data has not changed from the user's point of view. By noting **USN\_SOURCE\_DATA\_MANAGEMENT** in the **SourceInfo** member, you can determine that although a write operation is performed on the item, data has not changed. |
| - **USN\_SOURCE\_REPLICATION\_MANAGEMENT**<br>- 0x00000004 | The operation is modifying a file to match the contents of the same file which exists in another member of the replica set. |
| - **USN\_SOURCE\_CLIENT\_REPLICATION\_MANAGEMENT**<br>- 0x00000008 | The operation is modifying a file on client systems to match the contents of the same file that exists in the cloud. |

`SecurityId`

The unique security identifier assigned to the file or directory associated with this record.

`FileAttributes`

The attributes for the file or directory associated with this record, as returned by the [GetFileAttributes](/en-us/windows/desktop/api/fileapi/nf-fileapi-getfileattributesa) function. Attributes of streams associated with the file or directory are excluded.

`FileNameLength`

The length of the name of the file or directory associated with this record, in bytes. The **FileName** member contains this name. Use this member to determine file name length, rather than depending on a trailing '\0' to delimit the file name in **FileName**.

`FileNameOffset`

The offset of the **FileName** member from the beginning of the structure.

`FileName[1]`

The name of the file or directory associated with this record in Unicode format. This file or directory name is of variable length.

When working with **FileName**, do not count on the file name that contains a trailing '\0' delimiter, but instead determine the length of the file name by using **FileNameLength**.

Do not perform any compile-time pointer arithmetic using **FileName**. Instead, make necessary calculations at run time by using the value of the **FileNameOffset** member. Doing so helps make your code compatible with any future versions of **USN\_RECORD\_V2**.

## Remarks

In output buffers returned from [DeviceIoControl](/en-us/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) operations that work with **USN\_RECORD\_V2**, all records are aligned on 64-bit boundaries from the start of the buffer.

To provide a path for upward compatibility in change journal clients, Microsoft provides a major and minor version number of the change journal software in the **USN\_RECORD\_V2** structure. Your code should examine these values, detect its own compatibility with the change journal software, and if necessary gracefully handle any incompatibility.

A change in the minor version number indicates that the existing **USN\_RECORD\_V2** structure members are still valid, but that new members may have been added between the penultimate member and the last, which is a variable-length string.

To handle such a change gracefully, your code should not do any compile-time pointer arithmetic that relies on the location of the last member. For example, this makes the C code `sizeof(USN_RECORD)` unreliable. Instead, rely on run-time calculations by using the **RecordLength** member.

An increase in the major version number of the change journal software indicates that the **USN\_RECORD\_V2** structure may have undergone major changes, and that the current definition may not be reliable. If your code detects a change in the major version number of the change journal software, it should not work with the change journal.

For more information, see [Creating, Modifying, and Deleting a Change Journal](/en-us/windows/desktop/FileIO/creating-modifying-and-deleting-a-change-journal).

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows XP [desktop apps only] |
| **Minimum supported server** | Windows Server 2003 [desktop apps only] |
| **Header** | winioctl.h (include Windows.h) |
