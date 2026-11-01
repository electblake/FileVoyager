<!--
source: https://learn.microsoft.com/en-us/windows/win32/devnotes/mft-segment-reference
retrieved: 2026-11-01T19:21:19.178869+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/devnotes/mft-segment-reference
content_type: text/markdown
-->

---
layout: Conceptual
title: MFT_SEGMENT_REFERENCE structure - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/devnotes/mft-segment-reference
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
description: Represents an address in the master file table (MFT). The address is tagged with a circularly reused sequence number that is set at the time the MFT segment reference was valid.
ms.assetid: 59d83b95-83fb-4630-8ce4-f58441c748ab
ms.topic: reference
ms.date: 2018-05-31T00:00:00.0000000Z
topic_type:
- APIRef
- kbSyntax
api_name:
- MFT_SEGMENT_REFERENCE
api_type:
- NA
api_location: 
locale: en-us
document_id: a1999d0f-bcf5-a56b-7fe2-729736afcf02
document_version_independent_id: 66582468-4d6b-a166-b9a3-33650bdb8803
updated_at: 2021-01-06T19:21:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/win32-pr/blob/live/desktop-src/DevNotes/mft-segment-reference.md
gitcommit: https://github.com/MicrosoftDocs/win32-pr/blob/7ddbb1ba6777e796309f6c81cca43cdae3e9228c/desktop-src/DevNotes/mft-segment-reference.md
git_commit_id: 7ddbb1ba6777e796309f6c81cca43cdae3e9228c
site_name: Docs
depot_name: MSDN.win32
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.win32/{branchName}{pdfName}
word_count: 141
asset_id: devnotes/mft-segment-reference
moniker_range_name: 
monikers: []
item_type: Content
source_path: desktop-src/DevNotes/mft-segment-reference.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: bf42a232-c08a-98f9-d10b-e67ff81f2e20
---

# MFT_SEGMENT_REFERENCE structure - Win32 apps | Microsoft Learn

[This structure is valid only for version 3 of NTFS volumes; it may be altered in future versions.]

Represents an address in the master file table (MFT). The address is tagged with a circularly reused sequence number that is set at the time the MFT segment reference was valid.

## Syntax

```C
typedef struct _MFT_SEGMENT_REFERENCE {
  ULONG  SegmentNumberLowPart;
  USHORT SegmentNumberHighPart;
  USHORT SequenceNumber;
} MFT_SEGMENT_REFERENCE, *PMFT_SEGMENT_REFERENCE;
```

## Members

- **SegmentNumberLowPart**
    - The low part of the segment number.
- **SegmentNumberHighPart**
    - The high part of the segment number.
- **SequenceNumber**
    - The nonzero sequence number. The value 0 is reserved.

## Remarks

Note that there is no associated header file for this structure.

This structure definition is valid only for major version 3 and minor version 0 or 1, as reported by [**FSCTL\_GET\_NTFS\_VOLUME\_DATA**](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_get_ntfs_volume_data).

The **FILE\_REFERENCE** data type is defined as follows.

```syntax
typedef MFT_SEGMENT_REFERENCE FILE_REFERENCE, *PFILE_REFERENCE;
```
