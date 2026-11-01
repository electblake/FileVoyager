<!--
source: https://learn.microsoft.com/en-us/windows/win32/devnotes/master-file-table
retrieved: 2026-11-01T19:21:16.692294+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/devnotes/master-file-table
content_type: text/markdown
-->

---
layout: Conceptual
title: Master File Table (Developer Notes) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/devnotes/master-file-table
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
description: The master file table (MFT) stores the information required to retrieve files from an NTFS partition.
ms.assetid: 673fb4d0-7b6f-44fe-bfd6-1962e14ccdf5
ms.topic: concept-article
ms.date: 2018-05-31T00:00:00.0000000Z
locale: en-us
document_id: 0f28fb30-2d01-310c-8304-302696f32224
document_version_independent_id: d708c894-2349-e310-ac9d-9bf2b10b47d7
updated_at: 2025-04-15T10:05:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/win32-pr/blob/live/desktop-src/DevNotes/master-file-table.md
gitcommit: https://github.com/MicrosoftDocs/win32-pr/blob/0524d4c1b780ee35b710e7e8090dc07fcc4a0bda/desktop-src/DevNotes/master-file-table.md
git_commit_id: 0524d4c1b780ee35b710e7e8090dc07fcc4a0bda
site_name: Docs
depot_name: MSDN.win32
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.win32/{branchName}{pdfName}
word_count: 344
asset_id: devnotes/master-file-table
moniker_range_name: 
monikers: []
item_type: Content
source_path: desktop-src/DevNotes/master-file-table.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d774b87-7dcb-40bf-a0b9-5a7a9efff0d1
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/89dc5f37-0e4e-4b05-ad87-5fcd2b941a8a
platformId: cedc6a53-06e8-77c8-fe36-efd342fc0350
---

# Master File Table (Developer Notes) - Win32 apps | Microsoft Learn

[This document applies only to version 3 of NTFS volumes.]

The master file table (MFT) stores the information required to retrieve files from an NTFS partition.

A file may have one or more MFT records, and can contain one or more attributes. In NTFS, a file reference is the MFT segment reference of the base file record. For more information, see [**MFT\_SEGMENT\_REFERENCE**](mft-segment-reference).

The MFT contains file record segments; the first 16 of these are reserved for special files, such as the following:

- 0: MFT ($Mft)
- 5: root directory (\)
- 6: volume cluster allocation file ($Bitmap)
- 8: bad-cluster file ($BadClus)

Each file record segment starts with a file record segment header. For more information, see [**FILE\_RECORD\_SEGMENT\_HEADER**](file-record-segment-header). Each file record segment is followed by one or more attributes. Each attribute starts with an attribute record header. For more information, see [**ATTRIBUTE\_RECORD\_HEADER**](attribute-record-header). The attribute record includes the attribute type (such as $DATA or $BITMAP), an optional name, and the attribute value. The user data stream is an attribute, as are all streams. The attribute list is terminated with 0xFFFFFFFF ($END).

The following are some example attributes.

- The $Mft file contains an unnamed $DATA attribute that is the sequence of MFT record segments, in order.
- The $Mft file contains an unnamed $BITMAP attribute that indicates which MFT records are in use.
- The $Bitmap file contains an unnamed $DATA attribute that indicates which clusters are in use.
- The $BadClus file contains a $DATA attribute named $BAD that contains an entry that corresponds to each bad cluster.

When there is no more space for storing attributes in the file record segment, additional file record segments are allocated and inserted in the first (or base) file record segment in an attribute called the attribute list. The attribute list indicates where each attribute associated with the file can be found. This includes all attributes in the base file record, except for the attribute list itself. For more information, see [**ATTRIBUTE\_LIST\_ENTRY**](attribute-list-entry).

Structures related to the MFT include the following:

- [**ATTRIBUTE\_LIST\_ENTRY**](attribute-list-entry)
- [**ATTRIBUTE\_RECORD\_HEADER**](attribute-record-header)
- [**FILE\_NAME**](file-name)
- [**FILE\_RECORD\_SEGMENT\_HEADER**](file-record-segment-header)
- [**MFT\_SEGMENT\_REFERENCE**](mft-segment-reference)
- [**MULTI\_SECTOR\_HEADER**](multi-sector-header)
- [**STANDARD\_INFORMATION**](standard-information)
