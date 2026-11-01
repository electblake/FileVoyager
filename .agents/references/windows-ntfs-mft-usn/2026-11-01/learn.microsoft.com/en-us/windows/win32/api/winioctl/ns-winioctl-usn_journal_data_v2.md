<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-usn_journal_data_v2
retrieved: 2026-11-01T19:21:27.638766+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-usn_journal_data_v2
content_type: text/markdown
-->

---
layout: Conceptual
title: USN_JOURNAL_DATA_V2 - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-usn_journal_data_v2
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
UID: NS:winioctl.USN_JOURNAL_DATA_V2
description: Represents an update sequence number (USN) change journal, its records, and its capacity. This structure is the output buffer for the FSCTL_QUERY_USN_JOURNAL control code.
old-location: fs\usn_journal_data_v2.htm
tech.root: fs
ms.assetid: BBFA6D14-1423-45B0-83A0-62019D08507F
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: '*PUSN_JOURNAL_DATA_V2, FLAG_USN_TRACK_MODIFIED_RANGES_ENABLE, PUSN_JOURNAL_DATA_V2, PUSN_JOURNAL_DATA_V2 structure pointer [Files], USN_JOURNAL_DATA_V2, USN_JOURNAL_DATA_V2 structure [Files], fs.usn_journal_data_v2, winioctl/PUSN_JOURNAL_DATA_V2, winioctl/USN_JOURNAL_DATA_V2'
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
req.typenames: USN_JOURNAL_DATA_V2, *PUSN_JOURNAL_DATA_V2
req.redist: 
topic_type:
- APIRef
- kbSyntax
api_type:
- HeaderDef
api_location:
- WinIoCtl.h
api_name:
- USN_JOURNAL_DATA_V2
locale: en-us
document_id: ca17bbc7-3ece-23e8-c8b6-5286f303271c
document_version_independent_id: cc9a0321-b741-2040-91ba-d42181d29fa3
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/winioctl/ns-winioctl-usn_journal_data_v2.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/winioctl/ns-winioctl-usn_journal_data_v2.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_fs/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 474
asset_id: winioctl/ns-winioctl-usn_journal_data_v2
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/winioctl/ns-winioctl-usn_journal_data_v2.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: b1250bc7-ffaa-8db0-aa04-9ddb06d596f9
---

# USN_JOURNAL_DATA_V2 - Win32 apps | Microsoft Learn

Represents an update sequence number (USN) change journal, its records, and its capacity. This structure is the output buffer for the [FSCTL_QUERY_USN_JOURNAL](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_query_usn_journal) control code.

## Syntax

```cpp
typedef struct {
  DWORDLONG UsnJournalID;
  USN       FirstUsn;
  USN       NextUsn;
  USN       LowestValidUsn;
  USN       MaxUsn;
  DWORDLONG MaximumSize;
  DWORDLONG AllocationDelta;
  WORD      MinSupportedMajorVersion;
  WORD      MaxSupportedMajorVersion;
  DWORD     Flags;
  DWORDLONG RangeTrackChunkSize;
  LONGLONG  RangeTrackFileSizeThreshold;
} USN_JOURNAL_DATA_V2, *PUSN_JOURNAL_DATA_V2;
```

## Members

`UsnJournalID`

The current journal identifier. A journal is assigned a new identifier on creation and can be stamped with a new identifier in the course of its existence. The NTFS file system uses this identifier for an integrity check.

`FirstUsn`

The number of first record that can be read from the journal.

`NextUsn`

The number of next record to be written to the journal.

`LowestValidUsn`

The first record that was written into the journal for this journal instance. Enumerating the files or directories on a volume can return a USN lower than this value (in other words, a **FirstUsn** member value less than the **LowestValidUsn** member value). If it does, the journal has been stamped with a new identifier since the last USN was written. In this case, **LowestValidUsn** may indicate a discontinuity in the journal, in which changes to some or all files or directories on the volume may have occurred that are not recorded in the change journal.

`MaxUsn`

The largest USN that the change journal supports. An administrator must delete the change journal as the value of **NextUsn** approaches this value.

`MaximumSize`

The target maximum size for the change journal, in bytes. The change journal can grow larger than this value, but it is then truncated at the next NTFS file system checkpoint to less than this value.

`AllocationDelta`

The number of bytes of disk memory added to the end and removed from the beginning of the change journal each time memory is allocated or deallocated. In other words, allocation and deallocation take place in units of this size. An integer multiple of a cluster size is a reasonable value for this member.

`MinSupportedMajorVersion`

The minimum version of the USN change journal that the file system supports.

`MaxSupportedMajorVersion`

The maximum version of the USN change journal that the file system supports.

`Flags`

Whether or not range tracking is turned on. The following are the possible values for the **Flags** member.

| Value | Meaning |
| --- | --- |
| - 0x00000000 | Range tracking is not turned on for the volume. |
| - **FLAG\_USN\_TRACK\_MODIFIED\_RANGES\_ENABLE**<br>- 0x00000001 | Range tracking is turned on for the volume. |

`RangeTrackChunkSize`

The granularity of tracked ranges. Valid only when you also set the **Flags** member to **FLAG\_USN\_TRACK\_MODIFIED\_RANGES\_ENABLE**.

`RangeTrackFileSizeThreshold`

File size threshold to start tracking range for files with equal or larger size. Valid only when you also set the **Flags** member to **FLAG\_USN\_TRACK\_MODIFIED\_RANGES\_ENABLE**.

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows 8.1 [desktop apps only] |
| **Minimum supported server** | Windows Server 2012 R2 [desktop apps only] |
| **Header** | winioctl.h (include Windows.h) |
