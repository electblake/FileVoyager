<!--
source: https://learn.microsoft.com/en-us/windows/win32/devnotes/multi-sector-header
retrieved: 2026-11-01T19:21:20.027225+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/devnotes/multi-sector-header
content_type: text/markdown
-->

---
layout: Conceptual
title: MULTI_SECTOR_HEADER structure - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/devnotes/multi-sector-header
breadcrumb_path: /windows/desktop/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-WinDevCenter
recommendations: true
adobe-target: true
ms.service: windows-api-desktop-tech
ms.subservice: system-services
ms.author: jken
author: GrantMeStrength
feedback_system: Standard
feedback_product_url: https://www.microsoft.com/en-us/windowsinsider/feedbackhub/fb
feedback_help_link_url: https://learn.microsoft.com/answers/tags/224/windows-api-win32/
feedback_help_link_type: get-help-at-qna
description: Represents the multisector header.
ms.assetid: 0fad0e93-b940-4b52-be16-c5f177884dfb
ms.topic: reference
ms.date: 2018-05-31T00:00:00.0000000Z
topic_type:
- APIRef
- kbSyntax
api_name:
- MULTI_SECTOR_HEADER
api_type:
- NA
api_location: 
locale: en-us
document_id: eb645689-6480-63c6-1d9f-6d43ebaeb64e
document_version_independent_id: c8ea6804-3c46-548a-dba6-b36f30d7ee63
updated_at: 2021-01-06T19:21:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/win32-pr/blob/live/desktop-src/DevNotes/multi-sector-header.md
gitcommit: https://github.com/MicrosoftDocs/win32-pr/blob/7ddbb1ba6777e796309f6c81cca43cdae3e9228c/desktop-src/DevNotes/multi-sector-header.md
git_commit_id: 7ddbb1ba6777e796309f6c81cca43cdae3e9228c
site_name: Docs
depot_name: MSDN.win32
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.win32/{branchName}{pdfName}
word_count: 492
asset_id: devnotes/multi-sector-header
moniker_range_name: 
monikers: []
item_type: Content
source_path: desktop-src/DevNotes/multi-sector-header.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: a17e2bc9-4fde-8ecd-6346-8844a075a43b
---

# MULTI_SECTOR_HEADER structure - Win32 apps | Microsoft Learn

[This structure is valid only for version 3 of NTFS volumes; it may be altered in future versions.]

Represents the multisector header.

## Syntax

```C
typedef struct _MULTI_SECTOR_HEADER {
  UCHAR  Signature[4];
  USHORT UpdateSequenceArrayOffset;
  USHORT UpdateSequenceArraySize;
} MULTI_SECTOR_HEADER, *PMULTI_SECTOR_HEADER;
```

## Members

- **Signature**
    - The signature. This value is a convenience to the user.
- **UpdateSequenceArrayOffset**
    - The offset to the update sequence array, from the start of this structure. The update sequence array must end before the last USHORT value in the first sector.
- **UpdateSequenceArraySize**
    - The size of the update sequence array, in bytes.

## Remarks

Note that there is no associated header file for this structure.

This structure definition is valid only for major version 3 and minor version 0 or 1, as reported by [**FSCTL\_GET\_NTFS\_VOLUME\_DATA**](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_get_ntfs_volume_data).

The multisector header and update sequence array provide detection of incomplete multisector transfers for devices that either have a physical sector size greater than or equal to the sequence number stride (512) or that do not transfer sectors out of order. If a device exists that has a sector size smaller than the sequence number stride and it sometimes transfers sectors out of order, then the update sequence array will not provide absolute detection of incomplete transfers. The sequence number stride is set to a small enough number to provide absolute protection for all known hard disks. It is not set any smaller or there might be excessive run time or space overhead.

The update sequence array consists of an array of *n***USHORT** values, where *n* is the size of the structure being protected divided by the sequence number stride. The first word contains the update sequence number, which is a cyclical counter of the number of times the containing structure has been written to disk. Next are the *n* saved **USHORT** values that were overwritten by the update sequence number the last time the containing structure was written to disk.

Each time the protected structure is about to be written to disk, the last word in each sequence number stride is saved to its respective position in the sequence number array, then it is overwritten with the next update sequence number. After the write, or whenever the structure is read, the saved word from the sequence number array is restored to its actual position in the structure. Before restoring the saved words on reads, all the sequence numbers at the end of each stride are compared with the actual sequence number at the start of the array. If any of these comparisons are not equal, then a failed multisector transfer has been detected.

The size of the array is determined by the size of the containing structure. The update sequence array should be included at the end of the header of the structure it is protecting because of its variable size. The user must ensure that the correct space is reserved for the containing structure: (size of structure / 512 + 1) \* sizeof(USHORT).
