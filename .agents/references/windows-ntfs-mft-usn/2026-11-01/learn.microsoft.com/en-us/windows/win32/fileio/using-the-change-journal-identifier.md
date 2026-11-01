<!--
source: https://learn.microsoft.com/en-us/windows/win32/fileio/using-the-change-journal-identifier
retrieved: 2026-11-01T19:21:22.540349+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/fileio/using-the-change-journal-identifier
content_type: text/markdown
-->

---
layout: Conceptual
title: Using the Change Journal Identifier - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/fileio/using-the-change-journal-identifier
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
description: The NTFS file system associates an unsigned 64-bit identifier with each change journal.
ms.assetid: 5ae79460-b69a-4901-a417-1d5358dcba29
ms.topic: concept-article
ms.date: 2018-05-31T00:00:00.0000000Z
locale: en-us
document_id: 7465e004-4d0d-fc51-08ed-8129327329f7
document_version_independent_id: 30fa68fc-473b-a4c1-c157-2554a96ab414
updated_at: 2025-03-12T15:38:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/win32-pr/blob/live/desktop-src/FileIO/using-the-change-journal-identifier.md
gitcommit: https://github.com/MicrosoftDocs/win32-pr/blob/a955097414323a1a2517253d5454cccb022eaa6f/desktop-src/FileIO/using-the-change-journal-identifier.md
git_commit_id: a955097414323a1a2517253d5454cccb022eaa6f
site_name: Docs
depot_name: MSDN.win32
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.win32/{branchName}{pdfName}
word_count: 342
asset_id: fileio/using-the-change-journal-identifier
moniker_range_name: 
monikers: []
item_type: Content
source_path: desktop-src/FileIO/using-the-change-journal-identifier.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 0cda953d-de68-7ccf-dd23-286de959ed4b
---

# Using the Change Journal Identifier - Win32 apps | Microsoft Learn

The NTFS file system associates an unsigned 64-bit identifier with each change journal. The journal is stamped with this identifier when it is created. The file system stamps the journal with a new identifier where the existing update sequence number (USN) records either are or may be unusable.

For example, the NTFS file system restamps a change journal with a new identifier when a volume is moved from one version of NTFS to another and then back. Such a move can happen in a dual-boot environment or when working with removable media.

To obtain the identifier of the current change journal on a specified volume, use the [**FSCTL\_QUERY\_USN\_JOURNAL**](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_query_usn_journal) control code. To perform this and all other change journal operations, you must have system administrator privileges. That is, you must be a member of the Administrators group.

When an administrator deletes and re-creates the change journal, for example when the current USN value approaches the maximum possible USN value, the USN values begin again from zero. When the NTFS file system stamps a journal with a new identifier rather than re-creating the journal, it does not reset the USN to zero but continues from the current USN. In either case, all existing USNs are less than any future USNs.

When you need information on a specific set of records, use the [**FSCTL\_QUERY\_USN\_JOURNAL**](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_query_usn_journal) control code to obtain the change journal identifier. Then use the [**FSCTL\_READ\_USN\_JOURNAL**](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_read_usn_journal) control code to read the journal records of interest. The NTFS file system only returns records that are valid for the journal specified by the identifier.

Your application needs both the records' USNs and the identifier to read the journal. This requirement provides an integrity check for cases where your application should ignore the existing records in the file and where records were written in previous instances of the journal for the same volume.

To obtain the records in which you are interested, you must start at the oldest record (that is, with the lowest USN) and scan forward until you locate the first record of interest.
