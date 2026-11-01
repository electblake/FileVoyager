<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-read_usn_journal_data_v1
retrieved: 2026-11-01T19:21:27.213785+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-read_usn_journal_data_v1
content_type: text/markdown
-->

---
layout: Conceptual
title: READ_USN_JOURNAL_DATA_V1 - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-read_usn_journal_data_v1
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
UID: NS:winioctl.READ_USN_JOURNAL_DATA_V1
description: Contains information defining a set of update sequence number (USN) change journal records to return to the calling process.R
old-location: fs\read_usn_journal_data_str.htm
tech.root: fs
ms.assetid: f88e71ba-6099-4928-9d71-732a4ca809bc
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: '*PREAD_USN_JOURNAL_DATA, *PREAD_USN_JOURNAL_DATA_V1, PREAD_USN_JOURNAL_DATA, PREAD_USN_JOURNAL_DATA structure pointer [Files], PREAD_USN_JOURNAL_DATA_V0, PREAD_USN_JOURNAL_DATA_V0 structure pointer [Files], READ_USN_JOURNAL_DATA, READ_USN_JOURNAL_DATA structure [Files], READ_USN_JOURNAL_DATA_V0, READ_USN_JOURNAL_DATA_V0 structure [Files], READ_USN_JOURNAL_DATA_V1, USN_REASON_BASIC_INFO_CHANGE, USN_REASON_CLOSE, USN_REASON_COMPRESSION_CHANGE, USN_REASON_DATA_EXTEND, USN_REASON_DATA_OVERWRITE, USN_REASON_DATA_TRUNCATION, USN_REASON_EA_CHANGE, USN_REASON_ENCRYPTION_CHANGE, USN_REASON_FILE_CREATE, USN_REASON_FILE_DELETE, USN_REASON_HARD_LINK_CHANGE, USN_REASON_INDEXABLE_CHANGE, USN_REASON_NAMED_DATA_EXTEND, USN_REASON_NAMED_DATA_OVERWRITE, USN_REASON_NAMED_DATA_TRUNCATION, USN_REASON_OBJECT_ID_CHANGE, USN_REASON_RENAME_NEW_NAME, USN_REASON_RENAME_OLD_NAME, USN_REASON_REPARSE_POINT_CHANGE, USN_REASON_SECURITY_CHANGE, USN_REASON_STREAM_CHANGE, _win32_read_usn_journal_data_str, base.read_usn_journal_data_str, fs.read_usn_journal_data_str, winioctl/PREAD_USN_JOURNAL_DATA, winioctl/PREAD_USN_JOURNAL_DATA_V0, winioctl/READ_USN_JOURNAL_DATA, winioctl/READ_USN_JOURNAL_DATA_v0'
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
req.typenames: READ_USN_JOURNAL_DATA_V1, *PREAD_USN_JOURNAL_DATA_V1
req.redist: 
topic_type:
- APIRef
- kbSyntax
api_type:
- HeaderDef
api_location:
- WinIoCtl.h
api_name:
- READ_USN_JOURNAL_DATA_V1
locale: en-us
document_id: e9f38781-6162-f134-e891-a2494e9a960d
document_version_independent_id: c7897e69-61c7-c56c-925f-a156474c142e
updated_at: 2025-11-25T23:04:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/winioctl/ns-winioctl-read_usn_journal_data_v1.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/c2c2af312729d44b4c368831a1052a5e9e3a7a9f?path=/sdk-api-src/content/winioctl/ns-winioctl-read_usn_journal_data_v1.md&_a=contents
git_commit_id: c2c2af312729d44b4c368831a1052a5e9e3a7a9f
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_fs/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 1426
asset_id: winioctl/ns-winioctl-read_usn_journal_data_v1
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/winioctl/ns-winioctl-read_usn_journal_data_v1.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d774b87-7dcb-40bf-a0b9-5a7a9efff0d1
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/89dc5f37-0e4e-4b05-ad87-5fcd2b941a8a
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 1c79ff3b-15f5-8666-cf11-8445384a5178
---

# READ_USN_JOURNAL_DATA_V1 - Win32 apps | Microsoft Learn

Contains information defining a set of update sequence number (USN) change journal records to return to the calling process. It is used by the [FSCTL_QUERY_USN_JOURNAL](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_query_usn_journal) and [FSCTL_READ_USN_JOURNAL](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_read_usn_journal) control codes. Prior to Windows 8 and Windows Server 2012 this structure was named **READ\_USN\_JOURNAL\_DATA**. Use that name to compile with older SDKs and compilers. Windows Server 2012 introduced [READ_USN_JOURNAL_DATA_V1](/en-us/previous-versions/windows/desktop/legacy/hh802706%28v=vs.85%29) to support 128-bit file identifiers used by ReFS.

## Syntax

```cpp
typedef struct {
  USN       StartUsn;
  DWORD     ReasonMask;
  DWORD     ReturnOnlyOnClose;
  DWORDLONG Timeout;
  DWORDLONG BytesToWaitFor;
  DWORDLONG UsnJournalID;
  WORD      MinMajorVersion;
  WORD      MaxMajorVersion;
} READ_USN_JOURNAL_DATA_V1, *PREAD_USN_JOURNAL_DATA_V1;
```

## Members

`StartUsn`

The USN at which to begin reading the change journal.

To start the read operation at the first record in the journal, set the **StartUsn** member to zero. Because a USN is contained in every journal record, the output buffer tells at which record the read operation actually started.

To start the read operation at a specific record, set **StartUsn** to that record USN.

If a nonzero USN is specified that is less than the first USN in the change journal, then an error occurs and the **ERROR\_JOURNAL\_ENTRY\_DELETED** error code is returned. This code may indicate a case in which the specified USN is valid at one time but has since been deleted.

For more information on navigating the change journal buffer returned in **READ\_USN\_JOURNAL\_DATA\_V0**, see [Walking a Buffer of Change Journal Records](/en-us/windows/desktop/FileIO/walking-a-buffer-of-change-journal-records).

`ReasonMask`

A mask of flags, each flag noting a change for which the file or directory has a record in the change journal. To be returned in a [FSCTL_READ_USN_JOURNAL](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_read_usn_journal) operation, a change journal record must have at least one of these flags set.

The list of valid flags is as follows. Unused bits are reserved.

| Value | Meaning |
| --- | --- |
| - **USN\_REASON\_BASIC\_INFO\_CHANGE**<br>- 0x00008000 | A user has either changed one or more file or directory attributes (such as the read-only, hidden, system, archive, or sparse attribute), or one or more time stamps. |
| - **USN\_REASON\_CLOSE**<br>- 0x80000000 | The file or directory is closed. |
| - **USN\_REASON\_COMPRESSION\_CHANGE**<br>- 0x00020000 | The compression state of the file or directory is changed from or to compressed. |
| - **USN\_REASON\_DATA\_EXTEND**<br>- 0x00000002 | The file or directory is added to. |
| - **USN\_REASON\_DATA\_OVERWRITE**<br>- 0x00000001 | Data in the file or directory is overwritten. |
| - **USN\_REASON\_DATA\_TRUNCATION**<br>- 0x00000004 | The file or directory is truncated. |
| - **USN\_REASON\_EA\_CHANGE**<br>- 0x00000400 | The user makes a change to the file or directory extended attributes. These NTFS file system attributes are not accessible to Windows-based applications. |
| - **USN\_REASON\_ENCRYPTION\_CHANGE**<br>- 0x00040000 | The file or directory is encrypted or decrypted. |
| - **USN\_REASON\_FILE\_CREATE**<br>- 0x00000100 | The file or directory is created for the first time. |
| - **USN\_REASON\_FILE\_DELETE**<br>- 0x00000200 | The file or directory is deleted. |
| - **USN\_REASON\_HARD\_LINK\_CHANGE**<br>- 0x00010000 | An NTFS file system hard link is added to or removed from the file or directory. An NTFS file system hard link, similar to a POSIX hard link, is one of several directory entries that see the same file or directory. |
| - **USN\_REASON\_INDEXABLE\_CHANGE**<br>- 0x00004000 | A user changed the **FILE\_ATTRIBUTE\_NOT\_CONTENT\_INDEXED** attribute. That is, the user changed the file or directory from one that can be content indexed to one that cannot, or vice versa. (Content indexing permits rapid searching of data by building a database of selected content.) |
| - **USN\_REASON\_NAMED\_DATA\_EXTEND**<br>- 0x00000020 | One or more named data streams for the file were added to. |
| - **USN\_REASON\_NAMED\_DATA\_OVERWRITE**<br>- 0x00000010 | Data in one or more named data streams for the file is overwritten. |
| - **USN\_REASON\_NAMED\_DATA\_TRUNCATION**<br>- 0x00000040 | One or more named data streams for the file is truncated. |
| - **USN\_REASON\_OBJECT\_ID\_CHANGE**<br>- 0x00080000 | The object identifier of the file or directory is changed. |
| - **USN\_REASON\_RENAME\_NEW\_NAME**<br>- 0x00002000 | The file or directory is renamed, and the file name in the [USN_RECORD_V2](/en-us/windows/desktop/api/winioctl/ns-winioctl-usn_record_v2) or [USN_RECORD_V3](/en-us/windows/desktop/api/winioctl/ns-winioctl-usn_record_v3) structure holding this journal record is the new name. |
| - **USN\_REASON\_RENAME\_OLD\_NAME**<br>- 0x00001000 | The file or directory is renamed, and the file name in the [USN_RECORD_V2](/en-us/windows/desktop/api/winioctl/ns-winioctl-usn_record_v2) or [USN_RECORD_V3](/en-us/windows/desktop/api/winioctl/ns-winioctl-usn_record_v3) structure holding this journal record is the previous name. |
| - **USN\_REASON\_REPARSE\_POINT\_CHANGE**<br>- 0x00100000 | The reparse point contained in the file or directory is changed, or a reparse point is added to or deleted from the file or directory. |
| - **USN\_REASON\_SECURITY\_CHANGE**<br>- 0x00000800 | A change is made in the access permissions to the file or directory. |
| - **USN\_REASON\_STREAM\_CHANGE**<br>- 0x00200000 | A named stream is added to or removed from the file or directory, or a named stream is renamed. |

`ReturnOnlyOnClose`

A value that specifies when to return change journal records.

To receive notification when the final handle for the changed file or directory is closed, rather than at the time a change occurs, set **ReturnOnlyOnClose** to any nonzero value and specify the **USN\_REASON\_CLOSE** flag in the **ReasonMask** member.

All changes indicated by **ReasonMask** flags eventually generate a call to the change journal software when the file is closed. If your [DeviceIoControl](/en-us/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) call is waiting for the file to be closed, that call in turn will allow your **DeviceIoControl** call to return. In the event that a file or directory is not closed prior to a volume failure, operating system failure, or shutdown, a cleanup call to the change journal software occurs the next time the volume is mounted. The call occurs even if there is an intervening system restart.

To receive notification the first time each change is logged, as well as at cleanup, set **ReturnOnlyOnClose** to zero.

Whether **ReturnOnlyOnClose** is zero or nonzero, the records generated at cleanup log within the change journal all reasons for USN changes that occurred to the file or directory. Each time a final close operation occurs for an item, a USN close record is written to the change journal, and the **ReasonMask** flags for the item are all reset.

For a file or directory for which no user data exists (for example, a mounted folder), the final close operation occurs when the [CloseHandle](/en-us/windows/desktop/api/handleapi/nf-handleapi-closehandle) function is called on the last user handle to the item.

`Timeout`

The time-out value, in seconds, used with the **BytesToWaitFor** member to tell the operating system what to do if the [FSCTL_READ_USN_JOURNAL](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_read_usn_journal) operation requests more data than exists in the change journal.

If **Timeout** is zero and **BytesToWaitFor** is nonzero, and the [FSCTL_READ_USN_JOURNAL](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_read_usn_journal) operation call reaches the end of the change journal without finding data to return, **FSCTL\_READ\_USN\_JOURNAL** waits until **BytesToWaitFor** bytes of unfiltered data have been added to the change journal and then retrieves the specified records.

If **Timeout** is nonzero and **BytesToWaitFor** is nonzero, and the [FSCTL_READ_USN_JOURNAL](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_read_usn_journal) operation call reaches the end of the change journal without finding data to return, **FSCTL\_READ\_USN\_JOURNAL** waits **Timeout** seconds and then attempts to return the specified records. After **Timeout** seconds, **FSCTL\_READ\_USN\_JOURNAL** retrieves any records available within the specified range.

In either case, after the time-out period any new data appended to the change journal is processed. If there are still no records to return from the specified set, the time-out period is repeated. In this mode, [FSCTL_READ_USN_JOURNAL](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_read_usn_journal) remains outstanding until at least one record is returned or I/O is canceled.

If **BytesToWaitFor** is zero, then **Timeout** is ignored. **Timeout** is also ignored for asynchronously opened handles.

`BytesToWaitFor`

The number of bytes of unfiltered data added to the change journal. Use this value with **Timeout** to tell the operating system what to do if the [FSCTL_READ_USN_JOURNAL](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_read_usn_journal) operation requests more data than exists in the change journal.

If **BytesToWaitFor** is zero, then **Timeout** is ignored. In this case, the [FSCTL_READ_USN_JOURNAL](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_read_usn_journal) operation always returns successfully when the end of the change journal file is encountered. It also retrieves the USN that should be used for the next **FSCTL\_READ\_USN\_JOURNAL** operation. When the returned next USN is the same as the **StartUsn** supplied, there are no records available. The calling process should not use **FSCTL\_READ\_USN\_JOURNAL** again immediately.

Because the amount of data returned cannot be predicted when **BytesToWaitFor** is zero, you run a risk of overflowing the output buffer. To reduce this risk, specify a nonzero **BytesToWaitFor** value in repeated [FSCTL_READ_USN_JOURNAL](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_read_usn_journal) operations until all records in the change journal are exhausted. Then specify zero to await new records.

Alternatively, use the *lpBytesReturned* parameter of [DeviceIoControl](/en-us/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) in the [FSCTL_READ_USN_JOURNAL](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_read_usn_journal) operation call to determine the amount of data available, reallocate the output buffer (with room to spare for new records), and call **DeviceIoControl** again.

`UsnJournalID`

The identifier for the instance of the journal that is current for the volume.

The NTFS file system can miss putting events in the change journal if the change journal is stopped and restarted or deleted and re-created. If either of these events occurs, the NTFS file system gives the journal a new identifier. If the journal identifier does not agree with the current journal identifier, the call to [DeviceIoControl](/en-us/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) fails and returns an appropriate error code. To retrieve the new journal identifier, call **DeviceIoControl** with the [FSCTL_QUERY_USN_JOURNAL](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_query_usn_journal) operation.

`MinMajorVersion`

`MaxMajorVersion`

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows XP [desktop apps only] |
| **Minimum supported server** | Windows Server 2003 [desktop apps only] |
| **Header** | winioctl.h (include Windows.h) |
