<!--
source: https://learn.microsoft.com/en-us/windows/win32/fileio/change-journals
retrieved: 2026-11-01T19:21:21.468567+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/fileio/change-journals
content_type: text/markdown
-->

---
layout: Conceptual
title: Change Journals - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/fileio/change-journals
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
description: When any change is made to a file or directory in a volume, the USN change journal for that volume is updated with a description of the change and the name of the file or directory.
ms.assetid: 9a158c2b-da8e-4ca9-b3c1-2185cf41eb7d
ms.topic: reference
ms.date: 2018-05-31T00:00:00.0000000Z
locale: en-us
document_id: f703906e-14e9-4419-076a-df9fc0e477cb
document_version_independent_id: 5740e534-aa38-c731-5743-b9e6fe9924f6
updated_at: 2025-03-12T15:47:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/win32-pr/blob/live/desktop-src/FileIO/change-journals.md
gitcommit: https://github.com/MicrosoftDocs/win32-pr/blob/54868c37c24e1972da732005cb28c10a1bbd87ca/desktop-src/FileIO/change-journals.md
git_commit_id: 54868c37c24e1972da732005cb28c10a1bbd87ca
site_name: Docs
depot_name: MSDN.win32
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.win32/{branchName}{pdfName}
word_count: 371
asset_id: fileio/change-journals
moniker_range_name: 
monikers: []
item_type: Content
source_path: desktop-src/FileIO/change-journals.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/aebdc4a3-c54b-4eea-94e3-663d5e166f57
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/1baec8e6-ab38-4b56-bb59-f6282d94f311
platformId: 1d0c9d54-d061-807d-4fb4-d756c065c786
---

# Change Journals - Win32 apps | Microsoft Learn

An automatic backup application is one example of a program that must check for changes to the state of a volume to perform its task. The brute force method of checking for changes in directories or files is to scan the entire volume. However, this is often not an acceptable approach because of the decrease in system performance it would cause. Another method is for the application to register a directory notification (by calling the [**FindFirstChangeNotification**](/en-us/windows/desktop/api/FileAPI/nf-fileapi-findfirstchangenotificationa) or [**ReadDirectoryChangesW**](/en-us/windows/desktop/api/WinBase/nf-winbase-readdirectorychangesw) functions) for the directories to be backed up. This is more efficient than the first method, however, it requires that an application be running at all times. Also, if a large number of directories and files must be backed up, the amount of processing and memory overhead for such an application might also cause the operating system's performance to decrease.

To avoid these disadvantages, the NTFS file system maintains an update sequence number (USN) change journal. When any change is made to a file or directory in a volume, the USN change journal for that volume is updated with a description of the change and the name of the file or directory.

Change journals are also needed to recover file system indexing for example after a computer or volume failure. The ability to recover indexing means the file system can avoid the time-consuming process of reindexing the entire volume in such cases.

The following topics discuss change journals.
