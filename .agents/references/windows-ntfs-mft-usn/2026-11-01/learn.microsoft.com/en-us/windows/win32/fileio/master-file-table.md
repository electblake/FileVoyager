<!--
source: https://learn.microsoft.com/en-us/windows/win32/fileio/master-file-table
retrieved: 2026-11-01T19:21:16.252217+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/fileio/master-file-table
content_type: text/markdown
-->

---
layout: Conceptual
title: Master File Table (Local File Systems) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/fileio/master-file-table
breadcrumb_path: /windows/desktop/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-WinDevCenter
recommendations: true
adobe-target: true
ms.service: windows-api-desktop-tech
ms.subservice: data-access-storage
ms.author: jken
author: GrantMeStrength
feedback_system: Standard
feedback_product_url: https://www.microsoft.com/en-us/windowsinsider/feedbackhub/fb
feedback_help_link_url: https://learn.microsoft.com/answers/tags/224/windows-api-win32/
feedback_help_link_type: get-help-at-qna
description: All information about a file, including its size, time and date stamps, permissions, and data content, is stored either in master file table (MFT) entries, or in space outside the MFT that is described by MFT entries.
ms.assetid: e0933846-278e-4bc8-8982-c5819c252dad
ms.topic: concept-article
ms.date: 2024-09-05T00:00:00.0000000Z
locale: en-us
document_id: 36fa3374-85c6-484f-8da2-0720fdf56c7e
document_version_independent_id: 99b3630a-f502-2a2c-7910-b676f21c55fe
updated_at: 2025-04-15T10:05:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/win32-pr/blob/live/desktop-src/FileIO/master-file-table.md
gitcommit: https://github.com/MicrosoftDocs/win32-pr/blob/8318cb63ec1c9a6d504c8bf55ba4a9c091640a93/desktop-src/FileIO/master-file-table.md
git_commit_id: 8318cb63ec1c9a6d504c8bf55ba4a9c091640a93
site_name: Docs
depot_name: MSDN.win32
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.win32/{branchName}{pdfName}
word_count: 524
asset_id: fileio/master-file-table
moniker_range_name: 
monikers: []
item_type: Content
source_path: desktop-src/FileIO/master-file-table.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 0dfa4213-57ff-1c68-0f33-ed7443bb4f5b
---

# Master File Table (Local File Systems) - Win32 apps | Microsoft Learn

The NTFS file system contains a file called the *master file table*, or MFT. There is at least one entry in the MFT for every file on an NTFS file system volume, including the MFT itself. All information about a file, including its size, time and date stamps, permissions, and data content, is stored either in MFT entries, or in space outside the MFT that is described by MFT entries.

As files are added to an NTFS file system volume, more entries are added to the MFT and the MFT increases in size. When files are deleted from an NTFS file system volume, their MFT entries are marked as free and may be reused. However, disk space that has been allocated for these entries is not reallocated, and the size of the MFT does not decrease.

The NTFS file system reserves space for the MFT to keep the MFT as contiguous as possible as it grows. The space reserved by the NTFS file system for the MFT in each volume is called the MFT zone. Space for file and directories are also allocated from this space, but only after all of the volume space outside of the MFT zone has been allocated.

Depending on the average file size and other variables, either the reserved MFT zone or the unreserved space on the disk may be allocated first as the disk fills to capacity. Volumes with a small number of relatively large files will allocate the unreserved space first, while volumes with a large number of relatively small files allocate the MFT zone first. In either case, fragmentation of the MFT starts to take place when one region or the other becomes fully allocated. If the unreserved space is completely allocated, space for user files and directories will be allocated from the MFT zone. If the MFT zone is completely allocated, space for new MFT entries will be allocated from the unreserved space.

The MFT itself can be defragmented. To reduce the chance of the MFT zone becoming fully allocated before the defragmentation process is complete, leave as much space at the beginning of the MFT zone as possible before defragmenting the volume. If the MFT zone becomes fully allocated before defragmentation has completed, there must be unallocated space outside of the MFT zone.

The default MFT zone is calculated and reserved by the system when it mounts the volume, and is based on volume size. You can increase the MFT zone by means of the registry entry detailed in [How NTFS reserves space for its Master File Table (MFT)](/en-us/troubleshoot/windows-server/backup-and-storage/ntfs-reserves-space-for-mft), but you cannot make the default MFT zone smaller than what is calculated. Increasing the MFT zone does not decrease the disk space that users can use for data files.

To determine the current size of the MFT, analyze the NTFS file system drive with Disk Defragmenter, then click the **View Report** button. The drive statistics will be displayed, including the current MFT size, and number of fragments. You can also obtain the size of the MFT by using the [FSCTL_GET_NTFS_VOLUME_DATA](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_get_ntfs_volume_data) control code.
