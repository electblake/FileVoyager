<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-mft_enum_data_v0
retrieved: 2026-11-01T19:21:55.135324+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-mft_enum_data_v0
content_type: text/markdown
-->

---
layout: Conceptual
title: MFT_ENUM_DATA_V0 - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-mft_enum_data_v0
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
UID: NS:winioctl.MFT_ENUM_DATA_V0
description: Contains information defining the boundaries for and starting place of an enumeration of update sequence number (USN) change journal records.
old-location: fs\mft_enum_data_str.htm
tech.root: fs
ms.assetid: bd098d10-b30f-44b0-a379-2d57e33fe1c9
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: '*PMFT_ENUM_DATA, *PMFT_ENUM_DATA_V0, MFT_ENUM_DATA, MFT_ENUM_DATA_V0, MFT_ENUM_DATA_V0 structure [Files], PMFT_ENUM_DATA_V0, PMFT_ENUM_DATA_V0 structure pointer [Files], _win32_mft_enum_data_str, base.mft_enum_data_str, fs.mft_enum_data_str, winioctl/MFT_ENUM_DATA_V0, winioctl/PMFT_ENUM_DATA_V0'
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
req.typenames: MFT_ENUM_DATA_V0, *PMFT_ENUM_DATA_V0
req.redist: 
topic_type:
- APIRef
- kbSyntax
api_type:
- HeaderDef
api_location:
- WinIoCtl.h
api_name:
- MFT_ENUM_DATA_V0
locale: en-us
document_id: 5a0ee0ff-1806-8003-e65f-e39f9de73320
document_version_independent_id: d606f78a-6962-c284-5547-7f503076123a
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/winioctl/ns-winioctl-mft_enum_data_v0.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/winioctl/ns-winioctl-mft_enum_data_v0.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_fs/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 217
asset_id: winioctl/ns-winioctl-mft_enum_data_v0
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/winioctl/ns-winioctl-mft_enum_data_v0.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/fc3f72c2-fb6f-4cea-95ee-b444e52254ee
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/f12cf087-582d-48ac-a085-0c19adf1e391
platformId: e9d2e986-0487-a9fc-6810-94e01f85f071
---

# MFT_ENUM_DATA_V0 - Win32 apps | Microsoft Learn

Contains information defining the boundaries for and starting place of an enumeration of update sequence number (USN) change journal records. It is used as the input buffer for the [FSCTL_ENUM_USN_DATA](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_enum_usn_data) control code. Prior to Windows Server 2012 this structure was named **MFT\_ENUM\_DATA**. Use that name to compile with older SDKs and compilers.

## Syntax

```cpp
typedef struct {
  DWORDLONG StartFileReferenceNumber;
  USN       LowUsn;
  USN       HighUsn;
} MFT_ENUM_DATA_V0, *PMFT_ENUM_DATA_V0;
```

## Members

`StartFileReferenceNumber`

The ordinal position within the files on the current volume at which the enumeration is to begin.

The first call to [FSCTL_ENUM_USN_DATA](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_enum_usn_data) during an enumeration must have the **StartFileReferenceNumber** member set to `(DWORDLONG)0`. Each call to **FSCTL\_ENUM\_USN\_DATA** retrieves the starting point for the subsequent call as the first entry in the output buffer. Subsequent calls must be made with **StartFileReferenceNumber** set to this value. For more information, see **FSCTL\_ENUM\_USN\_DATA**.

`LowUsn`

The lower boundary of the range of USN values used to filter which records are returned. Only records whose last change journal USN is between or equal to the **LowUsn** and **HighUsn** member values are returned.

`HighUsn`

The upper boundary of the range of USN values used to filter which files are returned.

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows XP [desktop apps only] |
| **Minimum supported server** | Windows Server 2003 [desktop apps only] |
| **Header** | winioctl.h (include Windows.h) |
