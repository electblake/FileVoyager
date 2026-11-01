<!--
source: https://learn.microsoft.com/en-us/windows/win32/devnotes/attribute-list-entry
retrieved: 2026-11-01T19:21:18.184003+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/devnotes/attribute-list-entry
content_type: text/markdown
-->

---
layout: Conceptual
title: ATTRIBUTE_LIST_ENTRY structure - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/devnotes/attribute-list-entry
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
description: Represents an entry in the attribute list.
ms.assetid: daa0c97d-2ebe-4e14-b1f8-e4be3075b13e
ms.topic: reference
ms.date: 2018-05-31T00:00:00.0000000Z
topic_type:
- APIRef
- kbSyntax
api_name:
- ATTRIBUTE_LIST_ENTRY
api_type:
- NA
api_location: 
locale: en-us
document_id: cd7befc8-2492-c937-a12d-f93585348ff0
document_version_independent_id: 87da1c81-8ec0-ecad-f624-37b1e8361885
updated_at: 2021-01-06T23:44:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/win32-pr/blob/live/desktop-src/DevNotes/attribute-list-entry.md
gitcommit: https://github.com/MicrosoftDocs/win32-pr/blob/cc85842421beddb5e4f212dbe1f1da0f2837516e/desktop-src/DevNotes/attribute-list-entry.md
git_commit_id: cc85842421beddb5e4f212dbe1f1da0f2837516e
site_name: Docs
depot_name: MSDN.win32
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.win32/{branchName}{pdfName}
word_count: 412
asset_id: devnotes/attribute-list-entry
moniker_range_name: 
monikers: []
item_type: Content
source_path: desktop-src/DevNotes/attribute-list-entry.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 8aef9412-83e3-509b-9069-9285e87bd3ce
---

# ATTRIBUTE_LIST_ENTRY structure - Win32 apps | Microsoft Learn

[This structure is valid only for version 3 of NTFS volumes; it may be altered in future versions.]

Represents an entry in the attribute list.

## Syntax

```C
typedef struct _ATTRIBUTE_LIST_ENTRY {
  ATTRIBUTE_TYPE_CODE   AttributeTypeCode;
  USHORT                RecordLength;
  UCHAR                 AttributeNameLength;
  UCHAR                 AttributeNameOffset;
  VCN                   LowestVcn;
  MFT_SEGMENT_REFERENCE SegmentReference;
  USHORT                Reserved;
  WCHAR                 AttributeName[1];
} ATTRIBUTE_LIST_ENTRY, *PATTRIBUTE_LIST_ENTRY;
```

## Members

- **AttributeTypeCode**
    - The attribute type code.

| Value | Meaning |
| --- | --- |
| - **$STANDARD\_INFORMATION**<br>- 0x10 | File attributes (such as read-only and archive), time stamps (such as file creation and last modified), and the hard link count. |
| - **$ATTRIBUTE\_LIST**<br>- 0x20 | A list of attributes that make up the file and the file reference of the MFT file record in which each attribute is located. |
| - **$FILE\_NAME**<br>- 0x30 | The name of the file, in Unicode characters. |
| - **$OBJECT\_ID**<br>- 0x40 | An 16-byte object identifier assigned by the link-tracking service. |
| - **$VOLUME\_NAME**<br>- 0x60 | The volume label. Present in the $Volume file. |
| - **$VOLUME\_INFORMATION**<br>- 0x70 | The volume information. Present in the $Volume file. |
| - **$DATA**<br>- 0x80 | The contents of the file. |
| - **$INDEX\_ROOT**<br>- 0x90 | Used to implement filename allocation for large directories. |
| - **$INDEX\_ALLOCATION**<br>- 0xA0 | Used to implement filename allocation for large directories. |
| - **$BITMAP**<br>- 0xB0 | A bitmap index for a large directory. |
| - **$REPARSE\_POINT**<br>- 0xC0 | The reparse point data. |
- **RecordLength**
    - The size of this structure, plus the optional name buffer, in bytes.
- **AttributeNameLength**
    - The size of the optional attribute name, in characters. If a name exists, this value is nonzero and the structure is followed immediately by a Unicode string of the specified number of characters.
- **AttributeNameOffset**
    - Reserved.
- **LowestVcn**
    - The lowest virtual cluster number (VCN) for this attribute. This member is zero unless the attribute requires multiple file record segments and unless this entry is a reference to a segment other than the first one. In this case, this value is the lowest VCN that is described by the referenced segment.
- **SegmentReference**
    - The master file table (MFT) segment in which the attribute resides. See [**MFT\_SEGMENT\_REFERENCE**](mft-segment-reference).
- **Reserved**
    - Reserved.
- **AttributeName**
    - The start of the optional attribute name.

## Remarks

The attributes list is an ordered list of quadword-aligned **ATTRIBUTE\_LIST\_ENTRY** structures. This list is ordered first by the attribute type code and then by the attribute name (if present). No two attributes can have the same type code, name, and lowest VCN. Therefore, there can be at most one attribute for each type code without a name.

This structure definition is valid only for major version 3 and minor version 0 or 1, as reported by [**FSCTL\_GET\_NTFS\_VOLUME\_DATA**](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_get_ntfs_volume_data).

Note that there is no associated header file for this structure.
