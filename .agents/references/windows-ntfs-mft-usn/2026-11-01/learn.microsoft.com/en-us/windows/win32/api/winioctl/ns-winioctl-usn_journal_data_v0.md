<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-usn_journal_data_v0
retrieved: 2026-11-01T19:21:56.023292+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-usn_journal_data_v0
content_type: text/markdown
-->

---
layout: Conceptual
title: USN_JOURNAL_DATA_V0 - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-usn_journal_data_v0
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
UID: NS:winioctl.USN_JOURNAL_DATA_V0
description: Represents an update sequence number (USN) change journal, its records, and its capacity. (USN_JOURNAL_DATA_V0)
old-location: fs\usn_journal_data_str.htm
tech.root: fs
ms.assetid: 6b75eab2-aa10-4b48-8918-e4b03b5d8564
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: '*PUSN_JOURNAL_DATA, *PUSN_JOURNAL_DATA_V0, PUSN_JOURNAL_DATA, PUSN_JOURNAL_DATA structure pointer [Files], PUSN_JOURNAL_DATA_V0, PUSN_JOURNAL_DATA_V0 structure pointer [Files], USN_JOURNAL_DATA, USN_JOURNAL_DATA structure [Files], USN_JOURNAL_DATA_V0, USN_JOURNAL_DATA_V0 structure [Files], _win32_usn_journal_data_str, base.usn_journal_data_str, fs.usn_journal_data_str, winioctl/PUSN_JOURNAL_DATA, winioctl/PUSN_JOURNAL_DATA_V0, winioctl/USN_JOURNAL_DATA'
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
req.typenames: USN_JOURNAL_DATA_V0, *PUSN_JOURNAL_DATA_V0
req.redist: 
topic_type:
- APIRef
- kbSyntax
api_type:
- HeaderDef
api_location:
- WinIoCtl.h
api_name:
- USN_JOURNAL_DATA_V0
locale: en-us
document_id: 57851a73-3aaa-ff8a-3769-55cbba934a47
document_version_independent_id: b56cdb49-b430-e7e4-33db-797e737fe2ce
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/winioctl/ns-winioctl-usn_journal_data_v0.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/winioctl/ns-winioctl-usn_journal_data_v0.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_fs/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 371
asset_id: winioctl/ns-winioctl-usn_journal_data_v0
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/winioctl/ns-winioctl-usn_journal_data_v0.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 6117cc9c-a454-fb5a-e653-447753058cd6
---

# USN_JOURNAL_DATA_V0 - Win32 apps | Microsoft Learn

Represents an update sequence number (USN) change journal, its records, and its capacity. This structure is the output buffer for the [FSCTL_QUERY_USN_JOURNAL](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_query_usn_journal) control code. Prior to Windows 8 and Windows Server 2012 this structure was named **USN\_JOURNAL\_DATA**. Use that name to compile with older SDKs and compilers.

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
} USN_JOURNAL_DATA_V0, *PUSN_JOURNAL_DATA_V0;
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

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows XP [desktop apps only] |
| **Minimum supported server** | Windows Server 2003 [desktop apps only] |
| **Header** | winioctl.h (include Windows.h) |
