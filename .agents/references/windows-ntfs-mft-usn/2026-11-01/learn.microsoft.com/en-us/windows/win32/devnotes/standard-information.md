<!--
source: https://learn.microsoft.com/en-us/windows/win32/devnotes/standard-information
retrieved: 2026-11-01T19:21:20.625490+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/devnotes/standard-information
content_type: text/markdown
-->

---
layout: Conceptual
title: STANDARD_INFORMATION structure - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/devnotes/standard-information
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
description: Contains the standard information attribute. This attribute is present in every base file record and must be resident.
ms.assetid: 8e668309-2722-4115-923d-bf0aa78d24f1
ms.topic: reference
ms.date: 2018-05-31T00:00:00.0000000Z
topic_type:
- APIRef
- kbSyntax
api_name:
- STANDARD_INFORMATION
api_type:
- NA
api_location: 
locale: en-us
document_id: 059a4ccc-bc08-24f7-3363-4995c907d1ab
document_version_independent_id: 08443686-a170-df5a-b660-efe4337fafce
updated_at: 2021-01-06T19:21:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/win32-pr/blob/live/desktop-src/DevNotes/standard-information.md
gitcommit: https://github.com/MicrosoftDocs/win32-pr/blob/7ddbb1ba6777e796309f6c81cca43cdae3e9228c/desktop-src/DevNotes/standard-information.md
git_commit_id: 7ddbb1ba6777e796309f6c81cca43cdae3e9228c
site_name: Docs
depot_name: MSDN.win32
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.win32/{branchName}{pdfName}
word_count: 110
asset_id: devnotes/standard-information
moniker_range_name: 
monikers: []
item_type: Content
source_path: desktop-src/DevNotes/standard-information.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 9bb66ba5-a0ad-b26d-067c-19aa3f060d82
---

# STANDARD_INFORMATION structure - Win32 apps | Microsoft Learn

[This structure is valid only for version 3 of NTFS volumes; it may be altered in future versions.]

Contains the standard information attribute. This attribute is present in every base file record and must be resident.

## Syntax

```C
typedef struct _STANDARD_INFORMATION {
  UCHAR Reserved[0x30];
  ULONG OwnerId;
  ULONG SecurityId;
} STANDARD_INFORMATION, *PSTANDARD_INFORMATION;
```

## Members

- **Reserved**
    - Reserved.
- **OwnerId**
    - The identifier of the file owner, from the security index.
- **SecurityId**
    - The security identifier for the file.

## Remarks

Note that there is no associated header file for this structure.

This structure definition is valid only for major version 3 and minor version 0 or 1, as reported by [**FSCTL\_GET\_NTFS\_VOLUME\_DATA**](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_get_ntfs_volume_data).
