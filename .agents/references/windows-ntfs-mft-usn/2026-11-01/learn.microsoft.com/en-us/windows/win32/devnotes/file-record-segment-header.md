<!--
source: https://learn.microsoft.com/en-us/windows/win32/devnotes/file-record-segment-header
retrieved: 2026-11-01T19:21:17.202149+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/devnotes/file-record-segment-header
content_type: text/markdown
-->

---
layout: Conceptual
title: FILE_RECORD_SEGMENT_HEADER structure - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/devnotes/file-record-segment-header
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
description: Represents the file record segment. This is the header for each file record segment in the master file table (MFT).
ms.assetid: 4548ad49-1924-4888-8966-c45f8e453c6f
ms.topic: reference
ms.date: 2018-05-31T00:00:00.0000000Z
topic_type:
- APIRef
- kbSyntax
api_name:
- FILE_RECORD_SEGMENT_HEADER
api_type:
- NA
api_location: 
locale: en-us
document_id: b7fbe807-084e-f736-198e-5a8ddcb5598f
document_version_independent_id: 27c6a262-d0f1-4687-6512-3695c0bea266
updated_at: 2021-01-06T23:44:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/win32-pr/blob/live/desktop-src/DevNotes/file-record-segment-header.md
gitcommit: https://github.com/MicrosoftDocs/win32-pr/blob/cc85842421beddb5e4f212dbe1f1da0f2837516e/desktop-src/DevNotes/file-record-segment-header.md
git_commit_id: cc85842421beddb5e4f212dbe1f1da0f2837516e
site_name: Docs
depot_name: MSDN.win32
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.win32/{branchName}{pdfName}
word_count: 255
asset_id: devnotes/file-record-segment-header
moniker_range_name: 
monikers: []
item_type: Content
source_path: desktop-src/DevNotes/file-record-segment-header.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 4700b8e2-a4d2-ef72-a8c7-5740748443b3
---

# FILE_RECORD_SEGMENT_HEADER structure - Win32 apps | Microsoft Learn

[This structure is valid only for version 3 of NTFS volumes; it may be altered in future versions.]

Represents the file record segment. This is the header for each file record segment in the master file table (MFT).

## Syntax

```C
typedef struct _FILE_RECORD_SEGMENT_HEADER {
  MULTI_SECTOR_HEADER   MultiSectorHeader;
  ULONGLONG             Reserved1;
  USHORT                SequenceNumber;
  USHORT                Reserved2;
  USHORT                FirstAttributeOffset;
  USHORT                Flags;
  ULONG                 Reserved3[2];
  FILE_REFERENCE        BaseFileRecordSegment;
  USHORT                Reserved4;
  UPDATE_SEQUENCE_ARRAY UpdateSequenceArray;
} FILE_RECORD_SEGMENT_HEADER, *PFILE_RECORD_SEGMENT_HEADER;
```

## Members

- **MultiSectorHeader**
    - The multisector header defined by the cache manager. The [**MULTI\_SECTOR\_HEADER**](multi-sector-header) structure always contains the signature "FILE" and a description of the location and size of the update sequence array.
- **Reserved1**
    - Reserved.
- **SequenceNumber**
    - The sequence number. This value is incremented each time that a file record segment is freed; it is 0 if the segment is not used. The **SequenceNumber** field of a file reference must match the contents of this field; if they do not match, the file reference is incorrect and probably obsolete.
- **Reserved2**
    - Reserved.
- **FirstAttributeOffset**
    - The offset of the first attribute record, in bytes.
- **Flags**
    - The file flags.

- **FILE\_RECORD\_SEGMENT\_IN\_USE** (0x0001)
- **FILE\_FILE\_NAME\_INDEX\_PRESENT** (0x0002)
- **Reserved3**
    - Reserved.
- **BaseFileRecordSegment**
    - A file reference to the base file record segment for this file. If this is the base file record, the value is 0. See [**MFT\_SEGMENT\_REFERENCE**](mft-segment-reference).
- **Reserved4**
    - Reserved.
- **UpdateSequenceArray**
    - The update sequence array to protect multisector transfers of the file record segment.

## Remarks

Note that there is no associated header file for this structure.

This structure definition is valid only for major version 3 and minor version 0 or 1, as reported by [**FSCTL\_GET\_NTFS\_VOLUME\_DATA**](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_get_ntfs_volume_data).
