<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-mft_enum_data_v1
retrieved: 2026-11-01T19:21:26.817935+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-mft_enum_data_v1
content_type: text/markdown
-->

---
layout: Conceptual
title: MFT_ENUM_DATA_V1 - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-mft_enum_data_v1
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
UID: NS:winioctl.MFT_ENUM_DATA_V1
description: Contains information defining the boundaries for and starting place of an enumeration of update sequence number (USN) change journal records for ReFS volumes.
old-location: fs\mft_enum_data_v1.htm
tech.root: fs
ms.assetid: 6d7b50e3-60cf-4eaf-9d22-fbb20c7e0bba
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: '*PMFT_ENUM_DATA, *PMFT_ENUM_DATA_V1, MFT_ENUM_DATA, MFT_ENUM_DATA_V1, MFT_ENUM_DATA_V1 structure [Files], PMFT_ENUM_DATA_V1, PMFT_ENUM_DATA_V1 structure pointer [Files], fs.mft_enum_data_v1, winioctl/MFT_ENUM_DATA_V1, winioctl/PMFT_ENUM_DATA_V1'
req.header: winioctl.h
req.include-header: Windows.h
req.target-type: Windows
req.target-min-winverclnt: None supported
req.target-min-winversvr: Windows Server 2012 [desktop apps only]
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
req.typenames: MFT_ENUM_DATA_V1, *PMFT_ENUM_DATA_V1
req.redist: 
topic_type:
- APIRef
- kbSyntax
api_type:
- HeaderDef
api_location:
- WinIoCtl.h
api_name:
- MFT_ENUM_DATA_V1
locale: en-us
document_id: 163f2ed7-7cdf-43a9-1426-293bb2b8db4c
document_version_independent_id: a073ec59-8e4b-d77a-7efd-fd59c5ca5304
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/winioctl/ns-winioctl-mft_enum_data_v1.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/winioctl/ns-winioctl-mft_enum_data_v1.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_fs/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 257
asset_id: winioctl/ns-winioctl-mft_enum_data_v1
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/winioctl/ns-winioctl-mft_enum_data_v1.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: db7ac93d-6aae-74ac-c77b-dcaab3572284
---

# MFT_ENUM_DATA_V1 - Win32 apps | Microsoft Learn

Contains information defining the boundaries for and starting place of an enumeration of update sequence number (USN) change journal records for ReFS volumes. It is used as the input buffer for the [FSCTL_ENUM_USN_DATA](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_enum_usn_data) control code.

## Syntax

```cpp
typedef struct {
  DWORDLONG StartFileReferenceNumber;
  USN       LowUsn;
  USN       HighUsn;
  WORD      MinMajorVersion;
  WORD      MaxMajorVersion;
} MFT_ENUM_DATA_V1, *PMFT_ENUM_DATA_V1;
```

## Members

`StartFileReferenceNumber`

The ordinal position within the files on the current volume at which the enumeration is to begin.

The first call to [FSCTL_ENUM_USN_DATA](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_enum_usn_data) during an enumeration must have the **StartFileReferenceNumber** member set to `(DWORDLONG)0`. Each call to **FSCTL\_ENUM\_USN\_DATA** retrieves the starting point for the subsequent call as the first entry in the output buffer. Subsequent calls must be made with **StartFileReferenceNumber** set to this value. For more information, see **FSCTL\_ENUM\_USN\_DATA**.

`LowUsn`

The lower boundary of the range of USN values used to filter which records are returned. Only records whose last change journal USN is between or equal to the **LowUsn** and **HighUsn** member values are returned.

`HighUsn`

The upper boundary of the range of USN values used to filter which files are returned.

`MinMajorVersion`

Indicates the minimum supported major version for the USN change journal.

`MaxMajorVersion`

Indicates the maximum supported major version for the USN change journal.

| Value | Meaning |
| --- | --- |
| - 2 | The data returned from the [FSCTL_ENUM_USN_DATA](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_enum_usn_data) control code will contain [USN_RECORD_V2](/en-us/windows/desktop/api/winioctl/ns-winioctl-usn_record_v2) structures. |
| - 3 | The data returned from the [FSCTL_ENUM_USN_DATA](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_enum_usn_data) control code will contain [USN_RECORD_V2](/en-us/windows/desktop/api/winioctl/ns-winioctl-usn_record_v2) or [USN_RECORD_V3](/en-us/windows/desktop/api/winioctl/ns-winioctl-usn_record_v3) structures. |

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | None supported |
| **Minimum supported server** | Windows Server 2012 [desktop apps only] |
| **Header** | winioctl.h (include Windows.h) |
