<!--
source: https://learn.microsoft.com/en-us/windows/win32/fileio/change-journal-operations
retrieved: 2026-11-01T19:21:21.836217+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/fileio/change-journal-operations
content_type: text/markdown
-->

---
layout: Conceptual
title: Change journal operations - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/fileio/change-journal-operations
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
description: Control codes and structures to use with the NTFS file system update sequence number (USN) change journal.
ms.assetid: 2215f0d4-6ac8-42a5-87a5-9c76d1fae3ed
ms.topic: reference
ms.date: 2023-02-09T00:00:00.0000000Z
locale: en-us
document_id: 3dcb2ae6-bd4c-ed26-5d8d-00c75efa05b3
document_version_independent_id: 6067d3ab-4677-c469-ea50-64fb64175a1b
updated_at: 2025-03-12T15:47:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/win32-pr/blob/live/desktop-src/FileIO/change-journal-operations.md
gitcommit: https://github.com/MicrosoftDocs/win32-pr/blob/54868c37c24e1972da732005cb28c10a1bbd87ca/desktop-src/FileIO/change-journal-operations.md
git_commit_id: 54868c37c24e1972da732005cb28c10a1bbd87ca
site_name: Docs
depot_name: MSDN.win32
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.win32/{branchName}{pdfName}
word_count: 50
asset_id: fileio/change-journal-operations
moniker_range_name: 
monikers: []
item_type: Content
source_path: desktop-src/FileIO/change-journal-operations.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 6b393102-a755-0948-130f-4ac7526b7930
---

# Change journal operations - Win32 apps | Microsoft Learn

The following list identifies the control codes that work with the NTFS file system update sequence number (USN) change journal.

- [**FSCTL\_CREATE\_USN\_JOURNAL**](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_create_usn_journal)
- [**FSCTL\_DELETE\_USN\_JOURNAL**](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_delete_usn_journal)
- [**FSCTL\_ENUM\_USN\_DATA**](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_enum_usn_data)
- [**FSCTL\_MARK\_HANDLE**](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_mark_handle)
- [**FSCTL\_QUERY\_USN\_JOURNAL**](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_query_usn_journal)
- [**FSCTL\_READ\_USN\_JOURNAL**](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_read_usn_journal)

The following list identifies the structures information that relates to the NTFS file system USN change journal.

- [**CREATE\_USN\_JOURNAL\_DATA**](/en-us/windows/win32/api/WinIoCtl/ns-winioctl-create_usn_journal_data)
- [**DELETE\_USN\_JOURNAL\_DATA**](/en-us/windows/win32/api/WinIoCtl/ns-winioctl-delete_usn_journal_data)
- [**MARK\_HANDLE\_INFO**](/en-us/windows-hardware/drivers/ddi/ntifs/ns-ntifs-mark_handle_info)
- [**MFT\_ENUM\_DATA**](/en-us/windows/win32/api/WinIoCtl/ns-winioctl-mft_enum_data_v0)
- [**READ\_USN\_JOURNAL\_DATA**](/en-us/windows/win32/api/WinIoCtl/ns-winioctl-read_usn_journal_data_v0)
- [**USN\_JOURNAL\_DATA**](/en-us/windows/win32/api/WinIoCtl/ns-winioctl-usn_journal_data_v0)
- [**USN\_RECORD**](/en-us/windows/win32/api/WinIoCtl/ns-winioctl-usn_record_v2)
