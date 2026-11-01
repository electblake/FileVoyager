<!--
source: https://learn.microsoft.com/en-us/windows/win32/fileio/walking-a-buffer-of-change-journal-records
retrieved: 2026-11-01T19:21:22.861068+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/fileio/walking-a-buffer-of-change-journal-records
content_type: text/markdown
-->

---
layout: Conceptual
title: Walking a Buffer of Change Journal Records - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/fileio/walking-a-buffer-of-change-journal-records
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
description: How to return change journal records that meet specified criteria.
ms.assetid: 8946adb5-da47-4711-8800-86f323081c4c
ms.topic: concept-article
ms.date: 2018-05-31T00:00:00.0000000Z
locale: en-us
document_id: 6654d037-7d6f-d0cf-631e-176421de73ef
document_version_independent_id: c9aa6fb4-69ad-b089-79a7-bb6d0f2a01ff
updated_at: 2025-03-12T15:38:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/win32-pr/blob/live/desktop-src/FileIO/walking-a-buffer-of-change-journal-records.md
gitcommit: https://github.com/MicrosoftDocs/win32-pr/blob/a955097414323a1a2517253d5454cccb022eaa6f/desktop-src/FileIO/walking-a-buffer-of-change-journal-records.md
git_commit_id: a955097414323a1a2517253d5454cccb022eaa6f
site_name: Docs
depot_name: MSDN.win32
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.win32/{branchName}{pdfName}
word_count: 607
asset_id: fileio/walking-a-buffer-of-change-journal-records
moniker_range_name: 
monikers: []
item_type: Content
source_path: desktop-src/FileIO/walking-a-buffer-of-change-journal-records.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 49236818-7759-5f0c-95b0-d5e2338ddeab
---

# Walking a Buffer of Change Journal Records - Win32 apps | Microsoft Learn

The control codes that return update sequence number (USN) change journal records, [**FSCTL\_READ\_USN\_JOURNAL**](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_read_usn_journal) and [**FSCTL\_ENUM\_USN\_DATA**](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_enum_usn_data), return similar data in the output buffer. Both return a USN followed by zero or more change journal records, each in a [**USN\_RECORD\_V2**](/en-us/windows/desktop/api/WinIoCtl/ns-winioctl-usn_record_v2) or [**USN\_RECORD\_V3**](/en-us/windows/desktop/api/WinIoCtl/ns-winioctl-usn_record_v3) structure.

The target volume for USN operations must be ReFS or NTFS 3.0 or later. To obtain the NTFS version of a volume, open a command prompt with Administrator access rights and execute the following command:

**FSUtil.exe FSInfo NTFSInfo***X*\*\*:\*\*

where *X* is the drive letter of the volume.

The following list identifies ways to get change journal records:

- Use [**FSCTL\_ENUM\_USN\_DATA**](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_enum_usn_data) to get a listing (enumeration) of all change journal records between two USNs.
- Use [**FSCTL\_READ\_USN\_JOURNAL**](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_read_usn_journal) to be more selective, such as selecting specific reasons for changes or returning when a file is closed.

Note

Both of these operations return only the subset of change journal records that meet the specified criteria.

The USN returned as the first item in the output buffer is the USN of the next record number to be retrieved. Use this value to continue reading records from the end boundary forward.

The **FileName** member of [**USN\_RECORD\_V2**](/en-us/windows/desktop/api/WinIoCtl/ns-winioctl-usn_record_v2) or [**USN\_RECORD\_V3**](/en-us/windows/desktop/api/WinIoCtl/ns-winioctl-usn_record_v3) contains the name of the file to which the record in question applies. The file name varies in length, so **USN\_RECORD\_V2** and **USN\_RECORD\_V3** are variable length structures. Their first member, **RecordLength**, is the length of the structure (including the file name), in bytes.

When you work with the **FileName** member of [**USN\_RECORD\_V2**](/en-us/windows/desktop/api/WinIoCtl/ns-winioctl-usn_record_v2) and [**USN\_RECORD\_V3**](/en-us/windows/desktop/api/WinIoCtl/ns-winioctl-usn_record_v3) structures, do not assume that the file name contains a trailing '\0' delimiter. To determine the length of the file name, use the **FileNameLength** member.

The following example calls [**FSCTL\_READ\_USN\_JOURNAL**](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_read_usn_journal) and walks the buffer of change journal records that the operation returns.

```C
#include <Windows.h>
#include <WinIoCtl.h>
#include <stdio.h>

#define BUF_LEN 4096

void main()
{
   HANDLE hVol;
   CHAR Buffer[BUF_LEN];

   USN_JOURNAL_DATA JournalData;
   READ_USN_JOURNAL_DATA ReadData = {0, 0xFFFFFFFF, FALSE, 0, 0};
   PUSN_RECORD UsnRecord;  

   DWORD dwBytes;
   DWORD dwRetBytes;
   int I;

   hVol = CreateFile( TEXT("\\\\.\\c:"), 
               GENERIC_READ | GENERIC_WRITE, 
               FILE_SHARE_READ | FILE_SHARE_WRITE,
               NULL,
               OPEN_EXISTING,
               0,
               NULL);

   if( hVol == INVALID_HANDLE_VALUE )
   {
      printf("CreateFile failed (%d)\n", GetLastError());
      return;
   }

   if( !DeviceIoControl( hVol, 
          FSCTL_QUERY_USN_JOURNAL, 
          NULL,
          0,
          &JournalData,
          sizeof(JournalData),
          &dwBytes,
          NULL) )
   {
      printf( "Query journal failed (%d)\n", GetLastError());
      return;
   }

   ReadData.UsnJournalID = JournalData.UsnJournalID;

   printf( "Journal ID: %I64x\n", JournalData.UsnJournalID );
   printf( "FirstUsn: %I64x\n\n", JournalData.FirstUsn );

   for(I=0; I<=10; I++)
   {
      memset( Buffer, 0, BUF_LEN );

      if( !DeviceIoControl( hVol, 
            FSCTL_READ_USN_JOURNAL, 
            &ReadData,
            sizeof(ReadData),
            &Buffer,
            BUF_LEN,
            &dwBytes,
            NULL) )
      {
         printf( "Read journal failed (%d)\n", GetLastError());
         return;
      }

      dwRetBytes = dwBytes - sizeof(USN);

      // Find the first record
      UsnRecord = (PUSN_RECORD)(((PUCHAR)Buffer) + sizeof(USN));  

      printf( "****************************************\n");

      // This loop could go on for a long time, given the current buffer size.
      while( dwRetBytes > 0 )
      {
         printf( "USN: %I64x\n", UsnRecord->Usn );
         printf("File name: %.*S\n", 
                  UsnRecord->FileNameLength/2, 
                  UsnRecord->FileName );
         printf( "Reason: %x\n", UsnRecord->Reason );
         printf( "\n" );

         dwRetBytes -= UsnRecord->RecordLength;

         // Find the next record
         UsnRecord = (PUSN_RECORD)(((PCHAR)UsnRecord) + 
                  UsnRecord->RecordLength); 
      }
      // Update starting USN for next call
      ReadData.StartUsn = *(USN *)&Buffer; 
   }

   CloseHandle(hVol);

}
```

The size in bytes of any record specified by a [**USN\_RECORD\_V2**](/en-us/windows/desktop/api/WinIoCtl/ns-winioctl-usn_record_v2) or [**USN\_RECORD\_V3**](/en-us/windows/desktop/api/WinIoCtl/ns-winioctl-usn_record_v3) structure is at most `((MaxComponentLength - 1) * Width) + Size` where *MaxComponentLength* is the maximum length in characters of the record file name. The width is the size of a wide character, and the *Size* is the size of the structure.

To obtain the maximum length, call the [**GetVolumeInformation**](/en-us/windows/desktop/api/FileAPI/nf-fileapi-getvolumeinformationa) function and examine the value pointed to by the *lpMaximumComponentLength* parameter. Subtract one from *MaxComponentLength* to account for the fact that the definition of [**USN\_RECORD**](/en-us/windows/desktop/api/WinIoCtl/ns-winioctl-usn_record_v2) and [**USN\_RECORD\_V3**](/en-us/windows/desktop/api/WinIoCtl/ns-winioctl-usn_record_v3) includes one character of the file name.

In the C programming language, the largest possible record size is the following:

`(MaxComponentLength - 1) * sizeof(WCHAR) + sizeof(USN_RECORD)`
