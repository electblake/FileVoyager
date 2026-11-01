<!--
source: https://learn.microsoft.com/en-us/windows/win32/devnotes/file-name
retrieved: 2026-11-01T19:21:18.739547+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/devnotes/file-name
content_type: text/markdown
-->

---
layout: Conceptual
title: FILE_NAME structure - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/devnotes/file-name
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
description: Represents a file name attribute. A file has one file name attribute for every directory it is entered into.
ms.assetid: 54458eee-b786-446c-80bd-213c13bdeb4a
ms.topic: reference
ms.date: 2018-05-31T00:00:00.0000000Z
topic_type:
- APIRef
- kbSyntax
api_name:
- FILE_NAME
api_type:
- NA
api_location: 
locale: en-us
document_id: 3a6a4b2e-9846-e348-0ddc-93b2ff223779
document_version_independent_id: 4a6da196-1137-0b6f-df31-138851681e87
updated_at: 2021-01-06T23:44:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/win32-pr/blob/live/desktop-src/DevNotes/file-name.md
gitcommit: https://github.com/MicrosoftDocs/win32-pr/blob/cc85842421beddb5e4f212dbe1f1da0f2837516e/desktop-src/DevNotes/file-name.md
git_commit_id: cc85842421beddb5e4f212dbe1f1da0f2837516e
site_name: Docs
depot_name: MSDN.win32
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.win32/{branchName}{pdfName}
word_count: 138
asset_id: devnotes/file-name
moniker_range_name: 
monikers: []
item_type: Content
source_path: desktop-src/DevNotes/file-name.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 87883316-0204-91dd-b4ad-404a5a40a777
---

# FILE_NAME structure - Win32 apps | Microsoft Learn

[This structure is valid only for version 3 of NTFS volumes; it may be altered in future versions.]

Represents a file name attribute. A file has one file name attribute for every directory it is entered into.

## Syntax

```C
typedef struct _FILE_NAME {
  FILE_REFERENCE ParentDirectory;
  UCHAR          Reserved[0x38];
  UCHAR          FileNameLength;
  UCHAR          Flags;
  WCHAR          FileName[1];
} FILE_NAME, *PFILE_NAME;
```

## Members

- **ParentDirectory**
    - A file reference to the directory that indexes to this name. See [**MFT\_SEGMENT\_REFERENCE**](mft-segment-reference).
- **Reserved**
    - Reserved.
- **FileNameLength**
    - The length of the file name, in Unicode characters.
- **Flags**
    - The file name flags.

- **FILE\_NAME\_NTFS** (0x01)
- **FILE\_NAME\_DOS** (0x02)
- **FileName**
    - The first character of the file name.

## Remarks

Note that there is no associated header file for this structure.

This structure definition is valid only for major version 3 and minor version 0 or 1, as reported by [**FSCTL\_GET\_NTFS\_VOLUME\_DATA**](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_get_ntfs_volume_data).
