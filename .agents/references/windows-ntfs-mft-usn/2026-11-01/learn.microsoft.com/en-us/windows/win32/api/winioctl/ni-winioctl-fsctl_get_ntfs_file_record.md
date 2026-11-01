<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_get_ntfs_file_record
retrieved: 2026-11-01T19:21:25.742773+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_get_ntfs_file_record
content_type: text/markdown
-->

---
layout: Conceptual
title: FSCTL_GET_NTFS_FILE_RECORD - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_get_ntfs_file_record
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
UID: NI:winioctl.FSCTL_GET_NTFS_FILE_RECORD
description: Retrieves the first file record that is in use and is of a lesser than or equal ordinal value to the requested file reference number.
old-location: fs\fsctl_get_ntfs_file_record.htm
tech.root: fs
ms.assetid: a7308fa4-0f69-4b69-bb89-5d645e2a9f6e
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: FSCTL_GET_NTFS_FILE_RECORD, FSCTL_GET_NTFS_FILE_RECORD control, FSCTL_GET_NTFS_FILE_RECORD control code [Files], _win32_fsctl_get_ntfs_file_record, base.fsctl_get_ntfs_file_record, fs.fsctl_get_ntfs_file_record, winioctl/FSCTL_GET_NTFS_FILE_RECORD
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
- FSCTL_GET_NTFS_FILE_RECORD
locale: en-us
document_id: 27a2ac00-788d-469e-9119-5c7bfde6c1e0
document_version_independent_id: 3d487b85-f2f2-a715-22a0-b4a4b14a3dd5
updated_at: 2025-11-25T23:04:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/winioctl/ni-winioctl-fsctl_get_ntfs_file_record.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/c2c2af312729d44b4c368831a1052a5e9e3a7a9f?path=/sdk-api-src/content/winioctl/ni-winioctl-fsctl_get_ntfs_file_record.md&_a=contents
git_commit_id: c2c2af312729d44b4c368831a1052a5e9e3a7a9f
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_fs/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 366
asset_id: winioctl/ni-winioctl-fsctl_get_ntfs_file_record
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/winioctl/ni-winioctl-fsctl_get_ntfs_file_record.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: b603a1c3-47b5-718a-8a18-d49e3b580678
---

# FSCTL_GET_NTFS_FILE_RECORD - Win32 apps | Microsoft Learn

Retrieves the first file record that is in use and is of a lesser than or equal ordinal value to the requested file reference number.

To perform this operation, call the [**DeviceIoControl**](../ioapiset/nf-ioapiset-deviceiocontrol) function with the following parameters.

```cpp
BOOL DeviceIoControl(
  (HANDLE) hDevice,                 // handle to device
  FSCTL_GET_NTFS_FILE_RECORD,       // dwIoControlCode
  (LPVOID) lpInBuffer,              // input buffer
  (DWORD) nInBufferSize,            // size of input buffer
  (LPVOID) lpOutBuffer,             // output buffer
  (DWORD) nOutBufferSize,           // size of output buffer
  (LPDWORD) lpBytesReturned,        // number of bytes returned
  (LPOVERLAPPED) lpOverlapped       // OVERLAPPED structure
);
```

## Remarks

This control code enumerates file identifiers in a downward fashion, and always returns a file record that is in use. This means that the file identifier returned by this control code may not be the same as the file identifier specified in the input buffer. For example, if file identifiers 1 through 9 and 15 are in use, file identifiers 10 through 14 are not in use, and the file record corresponding to file identifier 15 is requested, that file record is returned.

If the file records that correspond to file identifiers 10 through 14 are requested, then the file record corresponding to file identifier 9 is returned. If any of the file records corresponding to file identifiers 1 through 9 are requested, those file records is returned.

To determine the correct size of the output buffer pointed to by *lpOutBuffer*, first call the [FSCTL_GET_NTFS_VOLUME_DATA](ni-winioctl-fsctl_get_ntfs_volume_data) control code to get the size of one file record. This is the value of the **BytesPerFileRecordSegment** member of the returned [NTFS_VOLUME_DATA_BUFFER](ns-winioctl-ntfs_volume_data_buffer) structure. Then set the size of the output buffer to the following expression:

`sizeof (NTFS_FILE_RECORD_OUTPUT_BUFFER) + sizeof (one file record) - 1`

If a file consists of multiple file records, they must be retrieved individually.

In Windows 8 and Windows Server 2012, this code is supported by the following technologies.

| Technology | Supported |
| --- | --- |
| Server Message Block (SMB) 3.0 protocol | No |
| SMB 3.0 Transparent Failover (TFO) | No |
| SMB 3.0 with Scale-out File Shares (SO) | No |
| Cluster Shared Volume File System (CsvFS) | Yes |
| Resilient File System (ReFS) | No |

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows XP [desktop apps only] |
| **Minimum supported server** | Windows Server 2003 [desktop apps only] |
| **Header** | winioctl.h (include Windows.h) |
