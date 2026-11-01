<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-ntfs_volume_data_buffer
retrieved: 2026-11-01T19:21:26.449059+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-ntfs_volume_data_buffer
content_type: text/markdown
-->

---
layout: Conceptual
title: NTFS_VOLUME_DATA_BUFFER - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-ntfs_volume_data_buffer
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
UID: NS:winioctl.NTFS_VOLUME_DATA_BUFFER
description: Represents volume data. (NTFS_VOLUME_DATA_BUFFER)
old-location: fs\ntfs_volume_data_buffer_str.htm
tech.root: fs
ms.assetid: 9ca0fe72-162c-4d75-a2f3-e1c7c0b0152a
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: '*PNTFS_VOLUME_DATA_BUFFER, NTFS_EXTENDED_VOLUME_DATA, NTFS_VOLUME_DATA_BUFFER, NTFS_VOLUME_DATA_BUFFER structure [Files], PNTFS_VOLUME_DATA_BUFFER, PNTFS_VOLUME_DATA_BUFFER structure pointer [Files], _win32_ntfs_volume_data_buffer_str, base.ntfs_volume_data_buffer_str, fs.ntfs_volume_data_buffer_str, winioctl/NTFS_VOLUME_DATA_BUFFER, winioctl/PNTFS_VOLUME_DATA_BUFFER'
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
req.typenames: NTFS_VOLUME_DATA_BUFFER, *PNTFS_VOLUME_DATA_BUFFER
req.redist: 
topic_type:
- APIRef
- kbSyntax
api_type:
- HeaderDef
api_location:
- WinIoCtl.h
api_name:
- NTFS_VOLUME_DATA_BUFFER
locale: en-us
document_id: b332004b-5911-2cd9-1f07-051f7c459393
document_version_independent_id: 8eff898f-da40-7130-089f-94190a3f2bf1
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/winioctl/ns-winioctl-ntfs_volume_data_buffer.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/winioctl/ns-winioctl-ntfs_volume_data_buffer.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_fs/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 398
asset_id: winioctl/ns-winioctl-ntfs_volume_data_buffer
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/winioctl/ns-winioctl-ntfs_volume_data_buffer.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 1fdcd249-1899-ac69-a715-18a684a914d3
---

# NTFS_VOLUME_DATA_BUFFER - Win32 apps | Microsoft Learn

Represents volume data. This structure is passed to the [FSCTL_GET_NTFS_VOLUME_DATA](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_get_ntfs_volume_data) control code.

## Syntax

```cpp
typedef struct {
  LARGE_INTEGER VolumeSerialNumber;
  LARGE_INTEGER NumberSectors;
  LARGE_INTEGER TotalClusters;
  LARGE_INTEGER FreeClusters;
  LARGE_INTEGER TotalReserved;
  DWORD         BytesPerSector;
  DWORD         BytesPerCluster;
  DWORD         BytesPerFileRecordSegment;
  DWORD         ClustersPerFileRecordSegment;
  LARGE_INTEGER MftValidDataLength;
  LARGE_INTEGER MftStartLcn;
  LARGE_INTEGER Mft2StartLcn;
  LARGE_INTEGER MftZoneStart;
  LARGE_INTEGER MftZoneEnd;
} NTFS_VOLUME_DATA_BUFFER, *PNTFS_VOLUME_DATA_BUFFER;
```

## Members

`VolumeSerialNumber`

The serial number of the volume. This is a unique number assigned to the volume media by the operating system.

`NumberSectors`

The number of sectors in the specified volume.

`TotalClusters`

The number of used and free clusters in the specified volume.

`FreeClusters`

The number of free clusters in the specified volume.

`TotalReserved`

The number of reserved clusters in the specified volume.

`BytesPerSector`

The number of bytes in a sector on the specified volume.

`BytesPerCluster`

The number of bytes in a cluster on the specified volume. This value is also known as the cluster factor.

`BytesPerFileRecordSegment`

The number of bytes in a file record segment.

`ClustersPerFileRecordSegment`

The number of clusters in a file record segment.

`MftValidDataLength`

The length of the master file table, in bytes.

`MftStartLcn`

The starting logical cluster number of the master file table.

`Mft2StartLcn`

The starting logical cluster number of the master file table mirror.

`MftZoneStart`

The starting logical cluster number of the master file table zone.

`MftZoneEnd`

The ending logical cluster number of the master file table zone.

## Remarks

Reserved clusters are the free clusters reserved for later use by Windows.

The **NTFS\_VOLUME\_DATA\_BUFFER** structure represents the basic information returned by [FSCTL_GET_NTFS_VOLUME_DATA](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_get_ntfs_volume_data). For extended volume information, pass a buffer that is the combined size of the **NTFS\_VOLUME\_DATA\_BUFFER** and **NTFS\_EXTENDED\_VOLUME\_DATA** structures. Upon success, the buffer returned by **FSCTL\_GET\_NTFS\_VOLUME\_DATA** will contain the information associated with both structures. The **NTFS\_VOLUME\_DATA\_BUFFER** structure will always be filled starting at the beginning of the buffer, with the **NTFS\_EXTENDED\_VOLUME\_DATA** structure immediately following. The **NTFS\_EXTENDED\_VOLUME\_DATA** structure is defined as follows:

| C++ |
| --- |
| ```<br>typedef struct {<br>    ULONG ByteCount;<br>    USHORT MajorVersion;<br>    USHORT MinorVersion;<br>} NTFS_EXTENDED_VOLUME_DATA, *PNTFS_EXTENDED_VOLUME_DATA;<br>``` |

 This structure contains the major and minor version information for an NTFS volume. The **ByteCount** member will return the total bytes of the output buffer used for this structure by the call to [FSCTL_GET_NTFS_VOLUME_DATA](/en-us/windows/desktop/api/winioctl/ni-winioctl-fsctl_get_ntfs_volume_data). This value should be `sizeof(NTFS_EXTENDED_VOLUME_DATA)` if the buffer passed was large enough to hold it, otherwise the value will be less than `sizeof(NTFS_EXTENDED_VOLUME_DATA)`. 
## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows XP [desktop apps only] |
| **Minimum supported server** | Windows Server 2003 [desktop apps only] |
| **Header** | winioctl.h (include Windows.h) |
