<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-getdibits
retrieved: 2026-10-31T21:17:04.130880+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-getdibits
content_type: text/markdown
-->

---
layout: Conceptual
title: GetDIBits function (wingdi.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-getdibits
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
UID: NF:wingdi.GetDIBits
description: The GetDIBits function retrieves the bits of the specified compatible bitmap and copies them into a buffer as a DIB using the specified format.
old-location: gdi\getdibits.htm
tech.root: gdi
ms.assetid: be3ffa3f-b343-4e38-8b1e-aeccf35d92b8
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: DIB_PAL_COLORS, DIB_RGB_COLORS, GetDIBits, GetDIBits function [Windows GDI], _win32_GetDIBits, gdi.getdibits, wingdi/GetDIBits
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
req.lib: Gdi32.lib
req.dll: Gdi32.dll
req.irql: 
targetos: Windows
req.typenames: 
req.redist: 
ms.custom: 19H1
topic_type:
- APIRef
- kbSyntax
api_type:
- DllExport
api_location:
- gdi32.dll
- Ext-MS-Win-GDI-Draw-l1-1-0.dll
- Ext-MS-Win-GDI-Draw-l1-1-1.dll
- ext-ms-win-gdi-draw-l1-1-2.dll
- Ext-MS-Win-GDI-Draw-L1-1-3.dll
- GDI32Full.dll
api_name:
- GetDIBits
locale: en-us
document_id: cb89299f-42f5-8d94-2c0c-6ed062fe841a
document_version_independent_id: 35a483cc-b089-3208-f153-b4b99b7880e0
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/wingdi/nf-wingdi-getdibits.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/wingdi/nf-wingdi-getdibits.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_gdi/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 636
asset_id: wingdi/nf-wingdi-getdibits
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/wingdi/nf-wingdi-getdibits.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
platformId: 8bcae889-975c-0b33-b1e2-bd4e14efa56c
---

# GetDIBits function (wingdi.h) - Win32 apps | Microsoft Learn

The **GetDIBits** function retrieves the bits of the specified compatible bitmap and copies them into a buffer as a DIB using the specified format.

## Syntax

```cpp
int GetDIBits(
  [in]      HDC          hdc,
  [in]      HBITMAP      hbm,
  [in]      UINT         start,
  [in]      UINT         cLines,
  [out]     LPVOID       lpvBits,
  [in, out] LPBITMAPINFO lpbmi,
  [in]      UINT         usage
);
```

## Parameters

`[in] hdc`

A handle to the device context.

`[in] hbm`

A handle to the bitmap. This must be a compatible bitmap (DDB).

`[in] start`

The first scan line to retrieve.

`[in] cLines`

The number of scan lines to retrieve.

`[out] lpvBits`

A pointer to a buffer to receive the bitmap data. If this parameter is **NULL**, the function passes the dimensions and format of the bitmap to the [BITMAPINFO](/en-us/windows/desktop/api/wingdi/ns-wingdi-bitmapinfo) structure pointed to by the *lpbmi* parameter.

`[in, out] lpbmi`

A pointer to a [BITMAPINFO](/en-us/windows/desktop/api/wingdi/ns-wingdi-bitmapinfo) structure that specifies the desired format for the DIB data.

`[in] usage`

The format of the **bmiColors** member of the [BITMAPINFO](/en-us/windows/desktop/api/wingdi/ns-wingdi-bitmapinfo) structure. It must be one of the following values.

| Value | Meaning |
| --- | --- |
| - **DIB\_PAL\_COLORS** | The color table should consist of an array of 16-bit indexes into the current logical palette. |
| - **DIB\_RGB\_COLORS** | The color table should consist of literal red, green, blue (RGB) values. |

## Return value

If the *lpvBits* parameter is non-**NULL** and the function succeeds, the return value is the number of scan lines copied from the bitmap.

If the *lpvBits* parameter is **NULL** and **GetDIBits** successfully fills the [BITMAPINFO](/en-us/windows/desktop/api/wingdi/ns-wingdi-bitmapinfo) structure, the return value is nonzero.

If the function fails, the return value is zero.

This function can return the following value.

| Return code | Description |
| --- | --- |
| - **ERROR\_INVALID\_PARAMETER** | One or more of the input parameters is invalid. |

## Remarks

If the requested format for the DIB matches its internal format, the RGB values for the bitmap are copied. If the requested format doesn't match the internal format, a color table is synthesized. The following table describes the color table synthesized for each format.

| Value | Meaning |
| --- | --- |
| 1\_BPP | The color table consists of a black and a white entry. |
| 4\_BPP | The color table consists of a mix of colors identical to the standard VGA palette. |
| 8\_BPP | The color table consists of a general mix of 256 colors defined by GDI. (Included in these 256 colors are the 20 colors found in the default logical palette.) |
| 24\_BPP | No color table is returned. |

If the *lpvBits* parameter is a valid pointer, the first six members of the [BITMAPINFOHEADER](/en-us/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure must be initialized to specify the size and format of the DIB. The scan lines must be aligned on a **DWORD** except for RLE compressed bitmaps.

A bottom-up DIB is specified by setting the height to a positive number, while a top-down DIB is specified by setting the height to a negative number. The bitmap color table will be appended to the [BITMAPINFO](/en-us/windows/desktop/api/wingdi/ns-wingdi-bitmapinfo) structure.

If *lpvBits* is **NULL**, **GetDIBits** examines the first member of the first structure pointed to by *lpbi*. This member must specify the size, in bytes, of a [BITMAPCOREHEADER](/en-us/windows/desktop/api/wingdi/ns-wingdi-bitmapcoreheader) or a [BITMAPINFOHEADER](/en-us/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure. The function uses the specified size to determine how the remaining members should be initialized.

If *lpvBits* is **NULL** and the bit count member of [BITMAPINFO](/en-us/windows/desktop/api/wingdi/ns-wingdi-bitmapinfo) is initialized to zero, **GetDIBits** fills in a [BITMAPINFOHEADER](/en-us/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure or [BITMAPCOREHEADER](/en-us/windows/desktop/api/wingdi/ns-wingdi-bitmapcoreheader) without the color table. This technique can be used to query bitmap attributes.

The bitmap identified by the *hbmp* parameter must not be selected into a device context when the application calls this function.

The origin for a bottom-up DIB is the lower-left corner of the bitmap; the origin for a top-down DIB is the upper-left corner.

#### Examples

For an example, see [Capturing an Image](/en-us/windows/desktop/gdi/capturing-an-image).

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows 2000 Professional [desktop apps only] |
| **Minimum supported server** | Windows 2000 Server [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | wingdi.h (include Windows.h) |
| **Library** | Gdi32.lib |
| **DLL** | Gdi32.dll |
