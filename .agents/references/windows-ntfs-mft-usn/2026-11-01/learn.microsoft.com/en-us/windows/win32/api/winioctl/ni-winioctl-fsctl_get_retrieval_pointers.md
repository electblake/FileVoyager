<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_get_retrieval_pointers
retrieved: 2026-11-01T19:21:26.024499+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_get_retrieval_pointers
content_type: text/markdown
-->

---
layout: Conceptual
title: FSCTL_GET_RETRIEVAL_POINTERS - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_get_retrieval_pointers
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
UID: NI:winioctl.FSCTL_GET_RETRIEVAL_POINTERS
description: Given a file handle, retrieves a data structure that describes the allocation and location on disk of a specific file, or, given a volume handle, the locations of bad clusters on a volume.
old-location: fs\fsctl_get_retrieval_pointers.htm
tech.root: fs
ms.assetid: 002f6703-8db3-4034-a79f-3fa9c4159115
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: FSCTL_GET_RETRIEVAL_POINTERS, FSCTL_GET_RETRIEVAL_POINTERS control, FSCTL_GET_RETRIEVAL_POINTERS control code [Files], _win32_fsctl_get_retrieval_pointers, base.fsctl_get_retrieval_pointers, fs.fsctl_get_retrieval_pointers, winioctl/FSCTL_GET_RETRIEVAL_POINTERS
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
req.typenames: 
req.redist: 
topic_type:
- APIRef
- kbSyntax
api_type:
- HeaderDef
api_location:
- WinIoCtl.h
api_name:
- FSCTL_GET_RETRIEVAL_POINTERS
locale: en-us
document_id: bcdb162e-c29f-10ed-768b-a4df13cf450c
document_version_independent_id: e61b3ba8-0c5a-d8a2-9f59-049ac1681515
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/winioctl/ni-winioctl-fsctl_get_retrieval_pointers.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/winioctl/ni-winioctl-fsctl_get_retrieval_pointers.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_fs/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 339
asset_id: winioctl/ni-winioctl-fsctl_get_retrieval_pointers
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/winioctl/ni-winioctl-fsctl_get_retrieval_pointers.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: e3d0ba82-7fdb-42d6-7ee0-30ba7a441dd9
---

# FSCTL_GET_RETRIEVAL_POINTERS - Win32 apps | Microsoft Learn

Given a file handle, retrieves a data structure that describes the allocation and location on disk of a specific file, or, given a volume handle, the locations of bad clusters on a volume.

To perform this operation, call the [**DeviceIoControl**](../ioapiset/nf-ioapiset-deviceiocontrol) function with the following parameters.

```cpp
DeviceIoControl(
  (HANDLE) hDevice,                 // handle to file, directory, or volume
  FSCTL_GET_RETRIEVAL_POINTERS,     // dwIoControlCode
  (LPVOID) lpInBuffer,              // input buffer
  (DWORD) nInBufferSize,            // size of input buffer
  (LPVOID) lpOutBuffer,             // output buffer
  (DWORD) nOutBufferSize,           // size of output buffer
  (LPDWORD) lpBytesReturned,        // number of bytes returned
  (LPOVERLAPPED) lpOverlapped       // OVERLAPPED structure
);
```

## Remarks

The **FSCTL\_GET\_RETRIEVAL\_POINTERS** operation retrieves a variably sized data structure that describes the allocation and location on disk of a specific file. The structure describes the mapping between virtual cluster numbers (VCN offsets within the file or stream space) and logical cluster numbers (LCN offsets within the volume space).

The **FSCTL\_GET\_RETRIEVAL\_POINTERS** control code is supported for file or directory operations on NTFS, FAT, exFAT, UDF, and ReFS file systems.

On supported file systems, the **FSCTL\_GET\_RETRIEVAL\_POINTERS** operation returns the extent locations of nonresident data. Resident data never has extent locations.

The **FSCTL\_GET\_RETRIEVAL\_POINTERS** control code also supports the alternate functionality of locating bad clusters. To query for the locations of bad clusters on a volume formatted with NTFS, FAT, or exFAT, use a volume handle as the *hDevice* parameter. This functionality is supported only on NTFS, FAT, and exFAT, and the caller must have **MANAGE\_VOLUME\_ACCESS** permission to the volume.

For the implications of overlapped I/O on this operation, see the Remarks section of the [DeviceIoControl](../ioapiset/nf-ioapiset-deviceiocontrol) topic.

In Windows 8 and Windows Server 2012, this code is supported by the following technologies.

| Technology | Supported |
| --- | --- |
| Server Message Block (SMB) 3.0 protocol | No |
| SMB 3.0 Transparent Failover (TFO) | No |
| SMB 3.0 with Scale-out File Shares (SO) | No |
| Cluster Shared Volume File System (CsvFS) | Yes |

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows XP [desktop apps only] |
| **Minimum supported server** | Windows Server 2003 [desktop apps only] |
| **Header** | winioctl.h (include Windows.h) |
