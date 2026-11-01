<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/wingdi/ns-wingdi-bitmapinfo
retrieved: 2026-11-01T19:27:48.930526+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/wingdi/ns-wingdi-bitmapinfo
content_type: text/markdown
-->

---
layout: Conceptual
title: BITMAPINFO (wingdi.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/wingdi/ns-wingdi-bitmapinfo
adobe-target: true
breadcrumb_path: /windows/desktop/api/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-WinDevCenter
ms.service: windows-api-desktop-tech
ms.subservice: sdk-api-reference
ms.topic: reference
ms.author: stwhi
author: stevewhims
feedback_system: Standard
feedback_product_url: https://www.microsoft.com/en-us/windowsinsider/feedbackhub/fb
feedback_help_link_url: https://learn.microsoft.com/answers/tags/224/windows-api-win32/
feedback_help_link_type: get-help-at-qna
UID: NS:wingdi.tagBITMAPINFO
description: The BITMAPINFO structure defines the dimensions and color information for a DIB.
old-location: gdi\bitmapinfo.htm
tech.root: gdi
ms.assetid: 84cc51e8-78f3-4ee6-bc08-94feff89afb0
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: '*LPBITMAPINFO, *PBITMAPINFO, BITMAPINFO, BITMAPINFO structure [Windows GDI], PBITMAPINFO, PBITMAPINFO structure pointer [Windows GDI], _win32_BITMAPINFO_str, gdi.bitmapinfo, tagBITMAPINFO, wingdi/BITMAPINFO, wingdi/PBITMAPINFO'
req.header: wingdi.h
req.include-header: Windows.h
req.target-type: Windows
req.target-min-winverclnt: Windows 2000 Professional [desktop apps only]
req.target-min-winversvr: Windows 2000 Server [desktop apps only]
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
req.typenames: BITMAPINFO, *LPBITMAPINFO, *PBITMAPINFO
req.redist: 
ms.custom: 19H1
topic_type:
- APIRef
- kbSyntax
api_type:
- HeaderDef
api_location:
- Wingdi.h
api_name:
- BITMAPINFO
locale: en-us
document_id: 0b52052e-879a-dad8-0fd6-16c1e2faec93
document_version_independent_id: 092e1956-6f78-0d44-7d30-4edc5caf2f69
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/wingdi/ns-wingdi-bitmapinfo.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/wingdi/ns-wingdi-bitmapinfo.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_gdi/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 383
asset_id: wingdi/ns-wingdi-bitmapinfo
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/wingdi/ns-wingdi-bitmapinfo.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 29173892-2917-e8d1-1927-ebea1dba3cf0
---

# BITMAPINFO (wingdi.h) - Win32 apps | Microsoft Learn

The **BITMAPINFO** structure defines the dimensions and color information for a DIB.

## Syntax

```cpp
typedef struct tagBITMAPINFO {
  BITMAPINFOHEADER bmiHeader;
  RGBQUAD          bmiColors[1];
} BITMAPINFO, *LPBITMAPINFO, *PBITMAPINFO;
```

## Members

`bmiHeader`

A [BITMAPINFOHEADER](/en-us/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure that contains information about the dimensions of color format.

.

`bmiColors[1]`

The **bmiColors** member contains one of the following:

- An array of [RGBQUAD](/en-us/windows/desktop/api/wingdi/ns-wingdi-rgbquad). The elements of the array that make up the color table.
- An array of 16-bit unsigned integers that specifies indexes into the currently realized logical palette. This use of **bmiColors** is allowed for functions that use DIBs. When **bmiColors** elements contain indexes to a realized logical palette, they must also call the following bitmap functions: 
    [CreateDIBitmap](/en-us/windows/desktop/api/wingdi/nf-wingdi-createdibitmap)

    [CreateDIBPatternBrush](/en-us/windows/desktop/api/wingdi/nf-wingdi-createdibpatternbrush)

    [CreateDIBSection](/en-us/windows/desktop/api/wingdi/nf-wingdi-createdibsection)

    The *iUsage* parameter of [CreateDIBSection](/en-us/windows/desktop/api/wingdi/nf-wingdi-createdibsection) must be set to DIB\_PAL\_COLORS.

 The number of entries in the array depends on the values of the **biBitCount** and **biClrUsed** members of the [BITMAPINFOHEADER](/en-us/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure. 
The colors in the **bmiColors** table appear in order of importance. For more information, see the Remarks section.

## Remarks

A DIB consists of two distinct parts: a **BITMAPINFO** structure describing the dimensions and colors of the bitmap, and an array of bytes defining the pixels of the bitmap. The bits in the array are packed together, but each scan line must be padded with zeros to end on a **LONG** data-type boundary. If the height of the bitmap is positive, the bitmap is a bottom-up DIB and its origin is the lower-left corner. If the height is negative, the bitmap is a top-down DIB and its origin is the upper left corner.

A bitmap is packed when the bitmap array immediately follows the **BITMAPINFO** header. Packed bitmaps are referenced by a single pointer. For packed bitmaps, the **biClrUsed** member must be set to an even number when using the DIB\_PAL\_COLORS mode so that the DIB bitmap array starts on a **DWORD** boundary.
**Note**
The **bmiColors** member should not contain palette indexes if the bitmap is to be stored in a file or transferred to another application. 

Unless the application has exclusive use and control of the bitmap, the bitmap color table should contain explicit RGB values. 

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows 2000 Professional [desktop apps only] |
| **Minimum supported server** | Windows 2000 Server [desktop apps only] |
| **Header** | wingdi.h (include Windows.h) |
