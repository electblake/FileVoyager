<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_read_file_usn_data
retrieved: 2026-11-01T19:21:24.741067+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_read_file_usn_data
content_type: text/markdown
-->

---
layout: Conceptual
title: FSCTL_READ_FILE_USN_DATA - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_read_file_usn_data
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
UID: NI:winioctl.FSCTL_READ_FILE_USN_DATA
description: Retrieves the update sequence number (USN) change-journal information for the specified file or directory.
old-location: fs\fsctl_read_file_usn_data.htm
tech.root: FileIO
ms.assetid: 22c797c8-87c8-4d45-b163-4573e6ed17e1
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: FSCTL_READ_FILE_USN_DATA, FSCTL_READ_FILE_USN_DATA control, FSCTL_READ_FILE_USN_DATA control code [Files], base.fsctl_read_file_usn_data, fs.fsctl_read_file_usn_data, winioctl/FSCTL_READ_FILE_USN_DATA
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
- FSCTL_READ_FILE_USN_DATA
locale: en-us
document_id: 5d3d452e-c974-bcfa-2ed7-17362aac3274
document_version_independent_id: 2ad7b1fe-249e-386c-1899-1a171894e806
updated_at: 2024-06-26T23:46:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/winioctl/ni-winioctl-fsctl_read_file_usn_data.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/3eb4092fd59c374abb5128a98cb600f9e9c85e6c?path=/sdk-api-src/content/winioctl/ni-winioctl-fsctl_read_file_usn_data.md&_a=contents
git_commit_id: 3eb4092fd59c374abb5128a98cb600f9e9c85e6c
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
word_count: 285
asset_id: winioctl/ni-winioctl-fsctl_read_file_usn_data
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/winioctl/ni-winioctl-fsctl_read_file_usn_data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: 6a7d7fa7-7e24-dbf2-1beb-7d2419454c7d
---

# FSCTL_READ_FILE_USN_DATA - Win32 apps | Microsoft Learn

Retrieves the update sequence number (USN) change-journal information for the specified file or directory.

To perform this operation, call the [DeviceIoControl](/en-us/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) function with the following parameters.

| C++ |
| --- |
| ```<br>BOOL <br>WINAPI <br>DeviceIoControl( (HANDLE)       hDevice,         // handle to device<br>                 (DWORD) FSCTL_READ_FILE_USN_DATA, // dwIoControlCode<br>                 (LPVOID)       lpInBuffer,      // input buffer<br>                 (DWORD)        nInBufferSize,   // size of input buffer<br>                 (LPVOID)       lpOutBuffer,     // output buffer<br>                 (DWORD)        nOutBufferSize,  // size of output buffer<br>                 (LPDWORD)      lpBytesReturned, // number of bytes returned<br>                 (LPOVERLAPPED) lpOverlapped );  // OVERLAPPED structure<br>``` |

## Remarks

If the call succeeds, the members of the returned [USN_RECORD_V2](/en-us/windows/desktop/api/winioctl/ns-winioctl-usn_record_v2) or [USN_RECORD_V3](/en-us/windows/desktop/api/winioctl/ns-winioctl-usn_record_v3) structure are valid except for the following members: **TimeStamp**, **Reason**, and **SourceInfo**. The **Usn** member represents the last USN written to the journal for this file or directory.

For more information, see [Creating, Modifying, and Deleting a Change Journal](/en-us/windows/desktop/FileIO/creating-modifying-and-deleting-a-change-journal).

To retrieve a handle to a volume, call [CreateFile](/en-us/windows/desktop/api/fileapi/nf-fileapi-createfilea) with the *lpFileName* parameter set to a string in the following form:

\\.\*X*:

In the preceding string, *X* is the letter identifying the drive on which the volume appears. The volume must be ReFS or NTFS 3.0 or later. To obtain the NTFS version of a volume, open a command prompt with Administrator access rights and execute the following command:

**FSUtil.exe FSInfo NTFSInfo ***X***:**

where *X* is the drive letter of the volume.

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
