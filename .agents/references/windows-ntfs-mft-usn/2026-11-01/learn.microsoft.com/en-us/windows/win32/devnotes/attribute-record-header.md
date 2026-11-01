<!--
source: https://learn.microsoft.com/en-us/windows/win32/devnotes/attribute-record-header
retrieved: 2026-11-01T19:21:17.713991+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/devnotes/attribute-record-header
content_type: text/markdown
-->

---
layout: Conceptual
title: ATTRIBUTE_RECORD_HEADER structure - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/devnotes/attribute-record-header
breadcrumb_path: /windows/desktop/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-WinDevCenter
recommendations: true
adobe-target: true
ms.service: windows-api-desktop-tech
ms.subservice: system-services
ms.author: jken
author: GrantMeStrength
feedback_system: Standard
feedback_product_url: https://www.microsoft.com/en-us/windowsinsider/feedbackhub/fb
feedback_help_link_url: https://learn.microsoft.com/answers/tags/224/windows-api-win32/
feedback_help_link_type: get-help-at-qna
description: Represents an attribute record.
ms.assetid: f9d9458c-b179-441c-9f62-ff0ac2f75329
ms.topic: reference
ms.date: 2018-05-31T00:00:00.0000000Z
topic_type:
- APIRef
- kbSyntax
api_name:
- ATTRIBUTE_RECORD_HEADER
api_type:
- NA
api_location: 
locale: en-us
document_id: affc43a3-3207-0b64-fbec-ae2614c5dd70
document_version_independent_id: a56ec9af-2f6e-02a1-37c0-c9a8e46002ef
updated_at: 2025-07-12T05:08:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/win32-pr/blob/live/desktop-src/DevNotes/attribute-record-header.md
gitcommit: https://github.com/MicrosoftDocs/win32-pr/blob/93c9fd36f77c3865a0d9cbd03e53a1cc5bb7385b/desktop-src/DevNotes/attribute-record-header.md
git_commit_id: 93c9fd36f77c3865a0d9cbd03e53a1cc5bb7385b
site_name: Docs
depot_name: MSDN.win32
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.win32/{branchName}{pdfName}
word_count: 934
asset_id: devnotes/attribute-record-header
moniker_range_name: 
monikers: []
item_type: Content
source_path: desktop-src/DevNotes/attribute-record-header.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/97159432-14a9-4307-a469-d2f2c75f0e33
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/50565c62-5f6b-4687-be38-323113c72c2e
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: baea2581-8df5-a647-4682-6e305a214a96
---

# ATTRIBUTE_RECORD_HEADER structure - Win32 apps | Microsoft Learn

[This structure is valid only for version 3 of NTFS volumes; it may be altered in future versions.]

Represents an attribute record.

## Syntax

```C
typedef struct _ATTRIBUTE_RECORD_HEADER {
  ATTRIBUTE_TYPE_CODE TypeCode;
  ULONG               RecordLength;
  UCHAR               FormCode;
  UCHAR               NameLength;
  USHORT              NameOffset;
  USHORT              Flags;
  USHORT              Instance;
  union {
    struct {
      ULONG  ValueLength;
      USHORT ValueOffset;
      UCHAR  Reserved[2];
    } Resident;
    struct {
      VCN      LowestVcn;
      VCN      HighestVcn;
      USHORT   MappingPairsOffset;
      UCHAR    Reserved[6];
      LONGLONG AllocatedLength;
      LONGLONG FileSize;
      LONGLONG ValidDataLength;
      LONGLONG TotalAllocated;
    } Nonresident;
  } Form;
} ATTRIBUTE_RECORD_HEADER, *PATTRIBUTE_RECORD_HEADER;
```

## Members

- **TypeCode**
    - The attribute type code.

| Value | Meaning |
| --- | --- |
| - **$STANDARD\_INFORMATION**<br>- 0x10 | File attributes (such as read-only and archive), time stamps (such as file creation and last modified), and the hard link count. |
| - **$ATTRIBUTE\_LIST**<br>- 0x20 | A list of attributes that make up the file and the file reference of the MFT file record in which each attribute is located. |
| - **$FILE\_NAME**<br>- 0x30 | The name of the file, in Unicode characters. |
| - **$OBJECT\_ID**<br>- 0x40 | A 64-byte object identifier assigned by the link-tracking service. |
| - **$VOLUME\_NAME**<br>- 0x60 | The volume label. Present in the $Volume file. |
| - **$VOLUME\_INFORMATION**<br>- 0x70 | The volume information. Present in the $Volume file. |
| - **$DATA**<br>- 0x80 | The contents of the file. |
| - **$INDEX\_ROOT**<br>- 0x90 | Used to implement filename allocation for large directories. |
| - **$INDEX\_ALLOCATION**<br>- 0xA0 | Used to implement filename allocation for large directories. |
| - **$BITMAP**<br>- 0xB0 | A bitmap index for a large directory. |
| - **$REPARSE\_POINT**<br>- 0xC0 | The reparse point data. |
- **RecordLength**
    - The size of the attribute record, in bytes. This value reflects the required size for the record variant and is always rounded to the nearest quadword boundary.
- **FormCode**
    - The attribute form code.

| Value | Meaning |
| --- | --- |
| - **RESIDENT\_FORM**<br>- 0x00 | The value is contained in the file record and immediately follows the attribute record header. |
| - **NONRESIDENT\_FORM**<br>- 0x01 | The value is contained in other sectors on the disk. |
- **NameLength**
    - The size of the optional attribute name, in characters, or 0 if there is no attribute name. The maximum attribute name length is 255 characters.
- **NameOffset**
    - The offset of the attribute name from the start of the attribute record, in bytes. If the **NameLength** member is 0, this member is undefined.
- **Flags**
    - The attribute flags.

- **ATTRIBUTE\_FLAG\_COMPRESSION\_MASK** (0x00FF)
- **ATTRIBUTE\_FLAG\_SPARSE** (0x8000)
- **ATTRIBUTE\_FLAG\_ENCRYPTED** (0x4000)
- **Instance**
    - The unique instance for this attribute in the file record.
- **Form**
    - If the **FormCode** member is RESIDENT\_FORM, the union is a **Resident** structure. If **FormCode** is NONRESIDENT\_FORM, the union is a **Nonresident** structure.

- **Resident**
    - - **ValueLength**
    - The size of the attribute value, in bytes.
- **ValueOffset**
    - The offset to the value from the start of the attribute record, in bytes.
- **Reserved**
    - Reserved.
- **Nonresident**
    - - **LowestVcn**
    - The lowest virtual cluster number (VCN) covered by this attribute record.
- **HighestVcn**
    - The highest VCN covered by this attribute record.
- **MappingPairsOffset**
    - The offset to the mapping pairs array from the start of the attribute record, in bytes. For more information, see Remarks.
- **Reserved**
    - Reserved.
- **AllocatedLength**
    - The allocated size of the file, in bytes. This value is an even multiple of the cluster size. This member is not valid if the **LowestVcn** member is nonzero.
- **FileSize**
    - The file size (highest byte that can be read plus 1), in bytes. This member is not valid if **LowestVcn** is nonzero.
- **ValidDataLength**
    - The valid data length (highest initialized byte plus 1), in bytes. This value is rounded to the nearest cluster boundary. This member is not valid if **LowestVcn** is nonzero.
- **TotalAllocated**
    - The total allocated for the file (the sum of the allocated clusters).

## Remarks

Note that there is no associated header file for this structure.

This structure definition is valid only for major version 3 and minor version 0 or 1, as reported by [**FSCTL\_GET\_NTFS\_VOLUME\_DATA**](/en-us/windows/win32/api/winioctl/ni-winioctl-fsctl_get_ntfs_volume_data).

Attribute records are always aligned on a quadword boundary.

If the attribute is nonresident, the attribute record header contains a list of retrieval information that provides a mapping between VCN and logical cluster number (LCN) for the attribute. If the retrieval information does not fit in the base file segment, it can be stored in an external file record segment by itself. If it still does not fit into one external file record segment, there is a provision in the attribute list to contain multiple entries for an attribute that requires additional retrieval information.

The mapping pairs array is stored in a compressed form and assumes that the information is decompressed and cached by the system. It consists of a series of NextVcn/CurrentLcn pairs. For example, if a file has a single run of 8 clusters starting at LCN 128 and the file starts at LowestVcn 0, then the mapping pairs array has just one entry, which is NextVcn=8 and CurrentLcn=128. The array is a byte stream that stores the changes to the working variables when processed sequentially. The byte stream is to be interpreted as a zero-terminated stream of triples, as follows:

count byte = *v* + (*l* \* 16)

where *v* is the number of changed low-order VCN bytes and *l* is the number of changed low-order LCN bytes.

The decompression algorithm is as follows:

1. Initialize NextVcn to `Attribute->LowestVcn` and CurrentLcn to 0.
2. Initialize the byte stream pointer to `(PCHAR)Attribute + Attribute->AttributeForm->Nonresident->MappingPairsOffset`.
3. Set CurrentVcn to NextVcn.
4. Read the next byte from the stream. If it is 0, then break; else extract *v* and *l* as previously described.
5. Interpret the next *v* bytes as a signed quantity, with the low-order byte first. Unpack it sign-extended into 64 bits and add it to NextVcn.
6. Interpret the next *l* bytes as a signed quantity, with the low-order byte first. Unpack it sign-extended into 64 bits and add it to CurrentLcn. If this produces a CurrentLcn of 0, then the VCNs from CurrentVcn to NextVcn–1 are unallocated.
7. Update the cached mapping information from CurrentVcn, NextVcn, and CurrentLcn.
8. Go to step 3.
