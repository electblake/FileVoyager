<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_query_usn_journal
retrieved: 2026-11-01T19:21:23.833216+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_query_usn_journal
content_type: text/markdown
-->

---
layout: Conceptual
title: FSCTL_QUERY_USN_JOURNAL - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_query_usn_journal
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
UID: NI:winioctl.FSCTL_QUERY_USN_JOURNAL
description: Queries for information on the current update sequence number (USN) change journal, its records, and its capacity.
old-location: fs\fsctl_query_usn_journal.htm
tech.root: FileIO
ms.assetid: 9491b054-934a-4b76-bf77-f397b6386f82
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: FSCTL_QUERY_USN_JOURNAL, FSCTL_QUERY_USN_JOURNAL control, FSCTL_QUERY_USN_JOURNAL control code [Files], _win32_fsctl_query_usn_journal, base.fsctl_query_usn_journal, fs.fsctl_query_usn_journal, winioctl/FSCTL_QUERY_USN_JOURNAL
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
- FSCTL_QUERY_USN_JOURNAL
locale: en-us
document_id: 5069a441-9dca-9000-e1c4-ce470e4e56d7
document_version_independent_id: 8cbb165c-1b98-eaa6-1f10-432e7f513d68
updated_at: 2024-06-26T23:46:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/winioctl/ni-winioctl-fsctl_query_usn_journal.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/3eb4092fd59c374abb5128a98cb600f9e9c85e6c?path=/sdk-api-src/content/winioctl/ni-winioctl-fsctl_query_usn_journal.md&_a=contents
git_commit_id: 3eb4092fd59c374abb5128a98cb600f9e9c85e6c
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
word_count: 242
asset_id: winioctl/ni-winioctl-fsctl_query_usn_journal
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/winioctl/ni-winioctl-fsctl_query_usn_journal.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 8737608a-513a-baea-efd8-8571afb4273c
---

# FSCTL_QUERY_USN_JOURNAL - Win32 apps | Microsoft Learn

Queries for information on the current update sequence number (USN) change journal, its records, and its capacity.

| C++ |
| --- |
| ```<br>BOOL <br>WINAPI <br>DeviceIoControl( (HANDLE)       Device,          // handle to volume<br>                 (DWORD) FSCTL_QUERY_USN_JOURNAL,// dwIoControlCode<br>                 (LPVOID)       NULL,            // lpInBuffer<br>                 (DWORD)        0,               // nInBufferSize<br>                 (LPVOID)       lpOutBuffer,     // output buffer<br>                 (DWORD)        nOutBufferSize,  // size of output buffer<br>                 (LPDWORD)      lpBytesReturned, // number of bytes returned<br>                 (LPOVERLAPPED) lpOverlapped );  // OVERLAPPED structure<br>``` |

To perform this operation, call the [DeviceIoControl](/en-us/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) function using the following parameters. 
## Remarks

For the implications of overlapped I/O on this operation, see the Remarks section of the [DeviceIoControl](/en-us/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) topic.

For more information, see [Creating, Modifying, and Deleting a Change Journal](/en-us/windows/desktop/FileIO/creating-modifying-and-deleting-a-change-journal).

To retrieve a handle to a volume, call [CreateFile](/en-us/windows/desktop/api/fileapi/nf-fileapi-createfilea) with the *lpFileName* parameter set to a string in the following form:

\\.\*X*:

In the preceding string, *X* is the letter identifying the drive on which the volume appears. The volume must be formatted with the NTFS filesystem.

In Windows 8 and Windows Server 2012, this code is supported by the following technologies.

| Technology | Supported |
| --- | --- |
| Server Message Block (SMB) 3.0 protocol | No |
| SMB 3.0 Transparent Failover (TFO) | No |
| SMB 3.0 with Scale-out File Shares (SO) | No |
| Cluster Shared Volume File System (CsvFS) | Yes |

An application may experience false positives on CsvFs pause/resume.

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows XP [desktop apps only] |
| **Minimum supported server** | Windows Server 2003 [desktop apps only] |
| **Header** | winioctl.h (include Windows.h) |
