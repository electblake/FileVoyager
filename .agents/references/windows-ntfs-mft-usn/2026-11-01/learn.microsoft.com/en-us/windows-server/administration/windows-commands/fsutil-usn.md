<!--
source: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/fsutil-usn
retrieved: 2026-11-01T19:21:31.445585+00:00
final_url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/fsutil-usn
content_type: text/markdown
-->

---
layout: Conceptual
title: fsutil usn | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/fsutil-usn
breadcrumb_path: /windows-server/breadcrumbs/toc.json
uhfHeaderId: MSDocsHeader-WindowsServer
feedback_system: Standard
recommendations: true
ms.service: windows-server
ms.subservice: windows-commands
ms.update-cycle: 1095-days
description: Reference article for the fsutil usn command, which manages the update sequence number (USN) change journal.
ms.author: roharwoo
author: robinharwood
ms.topic: reference
ms.date: 2017-10-16T00:00:00.0000000Z
locale: en-us
document_id: edfe0cbb-054c-fb3b-e3c7-b6b7bce4394d
document_version_independent_id: dc579949-a79a-ef26-9fe6-f87d551988e0
updated_at: 2026-02-16T18:34:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/windowsserverdocs-pr/blob/live/WindowsServerDocs/administration/windows-commands/fsutil-usn.md
gitcommit: https://github.com/MicrosoftDocs/windowsserverdocs-pr/blob/1dde3f071fa8b65476a0f278d15ed67c19b07896/WindowsServerDocs/administration/windows-commands/fsutil-usn.md
git_commit_id: 1dde3f071fa8b65476a0f278d15ed67c19b07896
site_name: Docs
depot_name: MSDN.WindowsServerDocs-pr
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.WindowsServerDocs-pr/{branchName}{pdfName}
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
word_count: 903
asset_id: administration/windows-commands/fsutil-usn
moniker_range_name: 
monikers: []
item_type: Content
source_path: WindowsServerDocs/administration/windows-commands/fsutil-usn.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/fc3f72c2-fb6f-4cea-95ee-b444e52254ee
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d774b87-7dcb-40bf-a0b9-5a7a9efff0d1
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/f12cf087-582d-48ac-a085-0c19adf1e391
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/89dc5f37-0e4e-4b05-ad87-5fcd2b941a8a
platformId: cb4a89e5-ea61-b3f1-73ce-56620622051e
---

# fsutil usn | Microsoft Learn

Manages the update sequence number (USN) change journal. The USN change journal provides a persistent log of all changes made to files on the volume. As files, directories, and other NTFS objects are added, deleted, and modified, NTFS enters records into the USN change journal, one for each volume on the computer. Each record indicates the type of change and the object changed. New records are appended to the end of the stream.

## Syntax

```
fsutil usn [createjournal] m=<maxsize> a=<allocationdelta> <volumepath>
fsutil usn [deletejournal] {/d | /n} <volumepath>
fsutil usn [enablerangetracking] <volumepath> [options]
fsutil usn [enumdata] <fileref> <lowUSN> <highUSN> <volumepath>
fsutil usn [queryjournal] <volumepath>
fsutil usn [readdata] <filename>
fsutil usn [readjournal] [c= <chunk-size> s=<file-size-threshold>] <volumepath>
```

### Parameters

| Parameter | Description |
| --- | --- |
| createjournal | Creates a USN change journal. |
| m=`<maxsize>` | Specifies the maximum size, in bytes, that NTFS allocates for the change journal. |
| a=`<allocationdelta>` | Specifies the size, in bytes, of memory allocation that is added to the end and removed from the beginning of the change journal. |
| `<volumepath>` | Specifies the drive letter (followed by a colon). |
| deletejournal | Deletes or disables an active USN change journal.<br>**CAUTION:** Deleting the change journal impacts the File Replication Service (FRS) and the Indexing Service, because it requires these services to perform a complete (and time-consuming) scan of the volume. This in turn negatively impacts FRS SYSVOL replication and replication between DFS link alternates while the volume is being rescanned. |
| /d | Disables an active USN change journal, and returns input/output (I/O) control while the change journal is being disabled. |
| /n | Disables an active USN change journal and returns I/O control only after the change journal is disabled. |
| enablerangetracking | Enables USN write range tracking for a volume. |
| c=`<chunk-size>` | Specifies the chunk size to track on a volume. |
| s=`<file-size-threshold>` | Specifies the file size threshold for range tracking. |
| enumdata | Enumerates and lists the change journal entries between two specified boundaries. |
| `<fileref>` | Specifies the ordinal position within the files on the volume at which the enumeration is to begin. |
| `<lowUSN>` | Specifies the lower boundary of the range of USN values used to filter the records that are returned. Only records whose last change journal USN is between or equal to the *lowUSN* and *highUSN* member values are returned. |
| `<highUSN>` | Specifies the upper boundary of the range of USN values used to filter the files that are returned. |
| queryjournal | Queries a volume's USN data to gather information about the current change journal, its records, and its capacity. |
| readdata | Reads the USN data for a file. |
| `<filename>` | Specifies the full path to the file, including the file name and extension For example: *C:\documents\filename.txt*. |
| readjournal | Reads the USN records in the USN journal. |
| minver=`<number>` | Minimum Major Version of USN\_RECORD to return. Default = 2. |
| maxver=`<number>` | Maximum Major Version of USN\_RECORD to return. Default = 4. |
| startusn=`<USN number>` | USN to start reading the USN journal from. Default = 0. |

#### Remarks

- Programs can consult the USN change journal to determine all the modifications made to a set of files. The USN change journal is much more efficient than checking time stamps or registering for file notifications. The USN change journal is enabled and used by the Indexing Service, File Replication Service (FRS), Remote Installation Services (RIS), and Remote Storage.
- If a change journal already exists on a volume, the **createjournal** parameter updates the change journal's **maxsize** and **allocationdelta** parameters. This enables you to expand the number of records that an active journal maintains without having to disable it.
- The change journal can grow larger than this target value, but the change journal is truncated at the next NTFS checkpoint to less than this value. NTFS examines the change journal and trims it when its size exceeds the value of **maxsize** plus the value of **allocationdelta**. At NTFS checkpoints, the operating system writes records to the NTFS log file that enable NTFS to determine what processing is required to recover from a failure.
- The change journal can grow to more than the sum of the values of **maxsize** and **allocationdelta** before being trimmed.
- Deleting or disabling an active change journal is very time consuming, because the system must access all the records in the master file table (MFT) and set the last USN attribute to 0 (zero). This process can take several minutes, and it can continue after the system restarts, if a restart is necessary. During this process, the change journal is not considered active, nor is it disabled. While the system is disabling the journal, it cannot be accessed, and all journal operations return errors. You should use extreme care when disabling an active journal, because it adversely affects other applications that are using the journal.

### Examples

To create a USN change journal on drive C, type:

```
fsutil usn createjournal m=1000 a=100 c:
```

To delete an active USN change journal on drive C, type:

```
fsutil usn deletejournal /d c:
```

To enable range tracking with a specified chunk-size and file-size-threshold, type:

```
fsutil usn enablerangetracking c=16384 s=67108864 C:
```

To enumerate and list the change journal entries between two specified boundaries on drive C, type:

```
fsutil usn enumdata 1 0 1 c:
```

To query USN data for a volume on drive C, type:

```
fsutil usn queryjournal c:
```

To read the USN data for a file in the \Temp folder on drive C, type:

```
fsutil usn readdata c:\temp\sample.txt
```

To read the USN journal with a specific start USN, type:

```
fsutil usn readjournal startusn=0xF00
```

## Related links

- [Command-Line Syntax Key](command-line-syntax-key)
- [fsutil](fsutil)
