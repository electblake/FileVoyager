<!--
source: https://learn.microsoft.com/en-us/windows/win32/fileio/file-streams
retrieved: 2026-11-01T19:21:21.081125+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/fileio/file-streams
content_type: text/markdown
-->

---
layout: Conceptual
title: File Streams (Local File Systems) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/fileio/file-streams
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
description: In the NTFS file system, streams contain the data that is written to a file, and that gives more information about a file than attributes and properties.
ms.assetid: 41dda6f1-a6d1-4e76-94f3-a72f9e491bee
ms.topic: concept-article
ms.date: 2025-07-08T00:00:00.0000000Z
locale: en-us
document_id: 69c60ed9-80c9-84ca-0fb4-731ebcaf4a37
document_version_independent_id: 0b3a2930-094b-6372-469d-59952e91d37c
updated_at: 2025-07-10T05:08:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/win32-pr/blob/live/desktop-src/FileIO/file-streams.md
gitcommit: https://github.com/MicrosoftDocs/win32-pr/blob/804c358a9c4bce679f7de9c1ef714669cb168959/desktop-src/FileIO/file-streams.md
git_commit_id: 804c358a9c4bce679f7de9c1ef714669cb168959
site_name: Docs
depot_name: MSDN.win32
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.win32/{branchName}{pdfName}
word_count: 916
asset_id: fileio/file-streams
moniker_range_name: 
monikers: []
item_type: Content
source_path: desktop-src/FileIO/file-streams.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d774b87-7dcb-40bf-a0b9-5a7a9efff0d1
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/89dc5f37-0e4e-4b05-ad87-5fcd2b941a8a
platformId: 7dc131ad-f282-e214-fb73-5e22fde9b92f
---

# File Streams (Local File Systems) - Win32 apps | Microsoft Learn

A stream is a sequence of bytes. In the NTFS file system, streams contain the data that is written to a file, and that gives more information about a file than attributes and properties. For example, you can create a stream that contains search keywords, or the identity of the user account that creates a file.

Each stream that is associated with a file has its own allocation size, actual size, and valid data length:

- The allocation size is the amount of disk space that is reserved for a stream.
- The actual size is the number of bytes that are being used by a caller.
- The valid data length (VDL) is the number of bytes that are initialized from the allocation size for the stream.

Each stream also maintains its own state for compression, encryption, and sparseness. The **FILE\_ATTRIBUTE\_SPARSE\_FILE** attribute on the file is set in the **dwFileAttributes** member of the [WIN32_FIND_DATA](/en-us/windows/win32/api/MinWinBase/ns-minwinbase-win32_find_dataa) structure returned from the [FindFirstFile](/en-us/windows/win32/api/FileAPI/nf-fileapi-findfirstfilea), [FindFirstFileEx](/en-us/windows/win32/api/FileAPI/nf-fileapi-findfirstfileexa), and [FindNextFile](/en-us/windows/win32/api/FileAPI/nf-fileapi-findnextfilea) functions if any of the streams have ever been sparse. [GetFileAttributes](/en-us/windows/win32/api/FileAPI/nf-fileapi-getfileattributesa), [GetFileAttributesEx](/en-us/windows/win32/api/FileAPI/nf-fileapi-getfileattributesexa), [GetFileAttributesTransacted](/en-us/windows/win32/api/WinBase/nf-winbase-getfileattributestransacteda), [GetFileInformationByHandle](/en-us/windows/win32/api/FileAPI/nf-fileapi-getfileinformationbyhandle), and [GetFileInformationByHandleEx](/en-us/windows/win32/api/WinBase/nf-winbase-getfileinformationbyhandleex) return the sparse state of the default data stream if no stream is specified.

There are no file times associated with a stream. The file times for a file are updated when any stream in a file is updated.

Opportunistic locks are maintained per stream. Sharing modes are also maintained per stream. When delete access is requested on a file, the operating system checks for delete access on all open streams in a file. If another process has opened a stream without the **FILE\_SHARE\_DELETE** permission, you cannot open the file for delete access.

If a file being copied has a data stream and the network redirector is used, the file can only be copied if the client has both the read permission and the read attributes permission.

## Naming Conventions for Streams

When specified from the Windows shell command line, the full name of a stream is "*filename*:*stream name*:*stream type*", as in the following example: "myfile.dat:stream1:$DATA".

Any characters that are legal for a file name are also legal for the stream name, including spaces. For more information, see [Naming a File](naming-a-file). The stream type (also called an attribute type code) is internal to the NTFS file system. Users therefore can't create new stream types, but they can open existing NTFS file system types. Stream type specifier values always start with the dollar sign ($) symbol. See below for a list of stream types.

By default, the default data stream is unnamed. To fully specify the default data stream, use "*filename*::$DATA", where $DATA is the stream type. This is the equivalent of "*filename*". You can create a named stream in the file using the [file naming conventions](naming-a-file). Note that "$DATA" is a legal stream name. For example, the full name of a stream named "$DATA" on a file named "*sample*" would be "*sample*:$DATA:$DATA". If you created a stream named "bar" on the same file its full name would be "*sample*:bar:$DATA".

When creating and working with files that have one-character names, prefix the file name with period followed by a backslash (.) or use a fully qualified path name. The reason to do this is that Windows treats one-character file names as drive letters. When a drive letter is specified with a relative path, a colon separates the drive letter from the path. When there is an ambiguity about whether a one-character name is a drive letter or a file name, Windows assumes it is a drive letter if the string following the colon is a valid path, even if the drive letter is invalid.

## Stream Types

Following is the list of NTFS stream types, also called attribute type codes. Some of the stream types are internal to NTFS and their format is undocumented.

| Stream Type | Description |
| --- | --- |
| ::$ATTRIBUTE\_LIST | Contains a list of all attributes that make up the file and identifies where each attribute is located. |
| ::$BITMAP | A bitmap used by indexes to manage the b-tree free space for a directory. The b-tree is managed in 4 KB chunks (regardless of cluster size) and this is used to manage the allocation of these chunks. This stream type is present on every directory. |
| ::$DATA | Data stream. The default data stream has no name. Data streams can be enumerated using the [FindFirstStreamW](/en-us/windows/win32/api/fileapi/nf-fileapi-findfirststreamw) and [FindNextStreamW](/en-us/windows/win32/api/fileapi/nf-fileapi-findnextstreamw) functions. |
| ::$EA | Contains Extended Attributes data. |
| ::$EA\_INFORMATION | Contains support information about the Extended Attributes. |
| ::$FILE\_NAME | The name of the file, in Unicode characters. This includes the short name of the file as well as any hard links. |
| ::$INDEX\_ALLOCATION | The stream type of a directory. Used to implement filename allocation for large directories. This stream represents the directory itself and contains all of the data of the directory. Changes to streams of this type are logged to the NTFS change journal. The default stream name of an $INDEX\_ALLOCATION stream type is $I30 so "*DirName*", "*DirName*::$INDEX\_ALLOCATION", and "*DirName*:$I30:$INDEX\_ALLOCATION" are all equivalent. |
| ::$INDEX\_ROOT | This stream represents root of the b-tree of an index. This stream type is present on every directory. |
| ::$LOGGED\_UTILITY\_STREAM | Similar to ::$DATA but operations are logged to the NTFS change journal. Used by EFS and [Transactional NTFS (TxF)](transactional-ntfs-portal). The ":*StreamName*:$*StreamType*" pair for EFS is ":$EFS:$LOGGED\_UTILITY\_STREAM" and for TxF is ":$TXF\_DATA:$LOGGED\_UTILITY\_STREAM". |
| ::$OBJECT\_ID | An 16-byte ID used to identify the file for the link-tracking service. |
| ::$REPARSE\_POINT | The [reparse point](reparse-points) data. |
