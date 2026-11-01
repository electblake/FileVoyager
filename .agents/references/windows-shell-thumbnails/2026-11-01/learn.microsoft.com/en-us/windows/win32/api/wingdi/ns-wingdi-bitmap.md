<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/wingdi/ns-wingdi-bitmap
retrieved: 2026-11-01T19:27:48.550279+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/wingdi/ns-wingdi-bitmap
content_type: text/markdown
-->

---
layout: Conceptual
title: BITMAP (wingdi.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/wingdi/ns-wingdi-bitmap
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
UID: NS:wingdi.tagBITMAP
description: The BITMAP structure defines the type, width, height, color format, and bit values of a bitmap.
old-location: gdi\bitmap.htm
tech.root: gdi
ms.assetid: 6ee382da-dd63-442b-80c3-59472defb41f
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: '*LPBITMAP, *NPBITMAP, *PBITMAP, BITMAP, BITMAP structure [Windows GDI], PBITMAP, PBITMAP structure pointer [Windows GDI], _win32_BITMAP_str, gdi.bitmap, wingdi/BITMAP, wingdi/PBITMAP'
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
req.typenames: BITMAP, *PBITMAP, *NPBITMAP, *LPBITMAP
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
- BITMAP
locale: en-us
document_id: 1022493d-a4bb-d806-59a7-792a30cbe206
document_version_independent_id: f705b477-aab6-a547-daaf-2125384b6014
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/wingdi/ns-wingdi-bitmap.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/wingdi/ns-wingdi-bitmap.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_gdi/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 322
asset_id: wingdi/ns-wingdi-bitmap
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/wingdi/ns-wingdi-bitmap.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 298fecc4-b7fb-5e5a-e255-38198deea143
---

# BITMAP (wingdi.h) - Win32 apps | Microsoft Learn

The **BITMAP** structure defines the type, width, height, color format, and bit values of a bitmap.

## Syntax

```cpp
typedef struct tagBITMAP {
  LONG   bmType;
  LONG   bmWidth;
  LONG   bmHeight;
  LONG   bmWidthBytes;
  WORD   bmPlanes;
  WORD   bmBitsPixel;
  LPVOID bmBits;
} BITMAP, *PBITMAP, *NPBITMAP, *LPBITMAP;
```

## Members

`bmType`

The bitmap type. This member must be zero.

`bmWidth`

The width, in pixels, of the bitmap. The width must be greater than zero.

`bmHeight`

The height, in pixels, of the bitmap. The height must be greater than zero.

`bmWidthBytes`

The number of bytes in each scan line. This value must be divisible by 2, because the system assumes that the bit values of a bitmap form an array that is word aligned.

`bmPlanes`

The count of color planes.

`bmBitsPixel`

The number of bits required to indicate the color of a pixel.

`bmBits`

A pointer to the location of the bit values for the bitmap. The **bmBits** member must be a pointer to an array of character (1-byte) values.

## Remarks

The bitmap formats currently used are monochrome and color. The monochrome bitmap uses a one-bit, one-plane format. Each scan is a multiple of 16 bits.

Scans are organized as follows for a monochrome bitmap of height *n*:

```syntax

    Scan 0 
    Scan 1 
    . 
    . 
    . 
    Scan n-2 
    Scan n-1 

```

The pixels on a monochrome device are either black or white. If the corresponding bit in the bitmap is 1, the pixel is set to the foreground color; if the corresponding bit in the bitmap is zero, the pixel is set to the background color.

All devices that have the RC\_BITBLT device capability support bitmaps. For more information, see [GetDeviceCaps](/en-us/windows/desktop/api/wingdi/nf-wingdi-getdevicecaps).

Each device has a unique color format. To transfer a bitmap from one device to another, use the [GetDIBits](/en-us/windows/desktop/api/wingdi/nf-wingdi-getdibits) and [SetDIBits](/en-us/windows/desktop/api/wingdi/nf-wingdi-setdibits) functions.

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows 2000 Professional [desktop apps only] |
| **Minimum supported server** | Windows 2000 Server [desktop apps only] |
| **Header** | wingdi.h (include Windows.h) |
