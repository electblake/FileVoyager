<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_enum_usn_data
retrieved: 2026-11-01T19:21:23.435368+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_enum_usn_data
content_type: text/markdown
-->

---
layout: Conceptual
title: FSCTL_ENUM_USN_DATA - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_enum_usn_data
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
UID: NI:winioctl.FSCTL_ENUM_USN_DATA
description: Enumerates the update sequence number (USN) data between two specified boundaries to obtain master file table (MFT) records.
old-location: fs\fsctl_enum_usn_data.htm
tech.root: FileIO
ms.assetid: 44d20401-a2ed-4756-9fda-878a24eab7c3
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: FSCTL_ENUM_USN_DATA, FSCTL_ENUM_USN_DATA control, FSCTL_ENUM_USN_DATA control code [Files], _win32_fsctl_enum_usn_data, base.fsctl_enum_usn_data, fs.fsctl_enum_usn_data, winioctl/FSCTL_ENUM_USN_DATA
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
- FSCTL_ENUM_USN_DATA
locale: en-us
document_id: 671f9366-955a-7b84-41f6-2ebce2752df8
document_version_independent_id: 6d3780d9-7149-98b1-9f0f-a0a63f293f32
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/winioctl/ni-winioctl-fsctl_enum_usn_data.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/winioctl/ni-winioctl-fsctl_enum_usn_data.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
word_count: 284
asset_id: winioctl/ni-winioctl-fsctl_enum_usn_data
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/winioctl/ni-winioctl-fsctl_enum_usn_data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: 364ddbcf-738e-7982-a74b-91543350e6c9
---

# FSCTL_ENUM_USN_DATA - Win32 apps | Microsoft Learn

Enumerates the update sequence number (USN) data between two specified boundaries to obtain master file table (MFT) records.

To perform this operation, call the [DeviceIoControl](/en-us/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) function with the following parameters.

| C++ |
| --- |
| ```<br>BOOL <br>WINAPI <br>DeviceIoControl( (HANDLE) hDevice,              // handle to volume<br>                 (DWORD) FSCTL_ENUM_USN_DATA,   // dwIoControlCode(LPVOID) lpInBuffer,           // input buffer<br>                 (DWORD) nInBufferSize,         // size of input buffer<br>                 (LPVOID) lpOutBuffer,          // output buffer<br>                 (DWORD) nOutBufferSize,        // size of output buffer<br>                 (LPDWORD) lpBytesReturned,     // number of bytes returned<br>                 (LPOVERLAPPED) lpOverlapped ); // OVERLAPPED structure);<br>``` |

## Remarks

For the implications of overlapped I/O on this operation, see the Remarks section of the [DeviceIoControl](/en-us/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) topic.

To enumerate files on a volume, use the **FSCTL\_ENUM\_USN\_DATA** operation one or more times. On the first call, set the starting point, the **StartFileReferenceNumber** member of the [MFT_ENUM_DATA](/en-us/windows/desktop/api/winioctl/ns-winioctl-mft_enum_data_v0) structure, to `(DWORDLONG)0`. Each call to **FSCTL\_ENUM\_USN\_DATA** retrieves the starting point for the subsequent call as the first entry in the output buffer.

By comparing To identify recent changes to a volume, use the [FSCTL_READ_USN_JOURNAL](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_read_usn_journal) control code.

To retrieve a handle to a volume, call [CreateFile](/en-us/windows/desktop/api/fileapi/nf-fileapi-createfilea) with the *lpFileName* parameter set to a string in the following form:

\\.\*X*:

In the preceding string, *X* is the letter identifying the drive on which the volume appears. The volume must be NTFS.

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
