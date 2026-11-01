<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-getobjectw
retrieved: 2026-11-01T19:27:46.063279+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-getobjectw
content_type: text/markdown
-->

---
layout: Conceptual
title: GetObjectW function (wingdi.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-getobjectw
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
UID: NF:wingdi.GetObjectW
description: The GetObjectW (Unicode) function (wingdi.h) retrieves information for the specified graphics object.
old-location: gdi\getobject.htm
tech.root: gdi
ms.assetid: 555ab876-d990-426d-915c-f98df82a10aa
ms.date: 2022-08-08T00:00:00.0000000Z
ms.keywords: GetObject, GetObject function [Windows GDI], GetObjectA, GetObjectW, HBITMAP, HBITMAP returned from a call to CreateDIBSection, HBRUSH, HFONT, HPALETTE, HPEN, HPEN returned from a call to ExtCreatePen, _win32_GetObject, gdi.getobject, wingdi/GetObject, wingdi/GetObjectA, wingdi/GetObjectW
req.header: wingdi.h
req.include-header: Windows.h
req.target-type: Windows
req.target-min-winverclnt: Windows 2000 Professional [desktop apps only]
req.target-min-winversvr: Windows 2000 Server [desktop apps only]
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: GetObjectW (Unicode) and GetObjectA (ANSI)
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
- Ext-MS-Win-GDI-DC-l1-2-0.dll
- ext-ms-win-gdi-dc-l1-1-0.dll
- ext-ms-win-gdi-dc-l1-2-1.dll
- GDI32Full.dll
api_name:
- GetObject
- GetObjectA
- GetObjectW
locale: en-us
document_id: 1895eb34-e4a2-6dbb-ccf0-c7e60a697b29
document_version_independent_id: a5e7a618-69aa-b6c3-8ac0-567c0bbf7a11
updated_at: 2024-11-20T00:20:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/wingdi/nf-wingdi-getobjectw.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/a9040b7bd365036907a35293e28d8cd449e31b87?path=/sdk-api-src/content/wingdi/nf-wingdi-getobjectw.md&_a=contents
git_commit_id: a9040b7bd365036907a35293e28d8cd449e31b87
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_gdi/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 463
asset_id: wingdi/nf-wingdi-getobjectw
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/wingdi/nf-wingdi-getobjectw.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: fc6669bc-b577-d0b0-7f91-3b0350bfd4dd
---

# GetObjectW function (wingdi.h) - Win32 apps | Microsoft Learn

The **GetObject** function retrieves information for the specified graphics object.

## Syntax

```cpp
int GetObjectW(
        HANDLE h,
        int    c,
        LPVOID pv
);
```

## Parameters

`h`

`c`

`pv`

## Return value

If the function succeeds, and *lpvObject* is a valid pointer, the return value is the number of bytes stored into the buffer.

If the function succeeds, and *lpvObject* is **NULL**, the return value is the number of bytes required to hold the information the function would store into the buffer.

If the function fails, the return value is zero.

## Remarks

The buffer pointed to by the *lpvObject* parameter must be sufficiently large to receive the information about the graphics object. Depending on the graphics object, the function uses a [BITMAP](/en-us/windows/desktop/api/wingdi/ns-wingdi-bitmap), [DIBSECTION](/en-us/windows/desktop/api/wingdi/ns-wingdi-dibsection), [EXTLOGPEN](/en-us/windows/desktop/api/wingdi/ns-wingdi-extlogpen), [LOGBRUSH](/en-us/windows/desktop/api/wingdi/ns-wingdi-logbrush), [LOGFONT](/en-us/windows/desktop/api/wingdi/ns-wingdi-logfonta), or [LOGPEN](/en-us/windows/desktop/api/wingdi/ns-wingdi-logpen) structure, or a count of table entries (for a logical palette).

If *hgdiobj* is a handle to a bitmap created by calling [CreateDIBSection](/en-us/windows/desktop/api/wingdi/nf-wingdi-createdibsection), and the specified buffer is large enough, the **GetObject** function returns a [DIBSECTION](/en-us/windows/desktop/api/wingdi/ns-wingdi-dibsection) structure. In addition, the **bmBits** member of the [BITMAP](/en-us/windows/desktop/api/wingdi/ns-wingdi-bitmap) structure contained within the **DIBSECTION** will contain a pointer to the bitmap's bit values.

If *hgdiobj* is a handle to a bitmap created by any other means, **GetObject** returns only the width, height, and color format information of the bitmap. You can obtain the bitmap's bit values by calling the [GetDIBits](/en-us/windows/desktop/api/wingdi/nf-wingdi-getdibits) or [GetBitmapBits](/en-us/windows/desktop/api/wingdi/nf-wingdi-getbitmapbits) function.

If *hgdiobj* is a handle to a logical palette, **GetObject** retrieves a 2-byte integer that specifies the number of entries in the palette. The function does not retrieve the [LOGPALETTE](/en-us/windows/desktop/api/wingdi/ns-wingdi-logpalette) structure defining the palette. To retrieve information about palette entries, an application can call the [GetPaletteEntries](/en-us/windows/desktop/api/wingdi/nf-wingdi-getpaletteentries) function.

If *hgdiobj* is a handle to a font, the [LOGFONT](/en-us/windows/desktop/api/wingdi/ns-wingdi-logfonta) that is returned is the **LOGFONT** used to create the font. If Windows had to make some interpolation of the font because the precise **LOGFONT** could not be represented, the interpolation will not be reflected in the **LOGFONT**. For example, if you ask for a vertical version of a font that doesn't support vertical painting, the **LOGFONT** indicates the font is vertical, but Windows will paint it horizontally.

#### Examples

For an example, see [Storing an Image](/en-us/windows/desktop/gdi/storing-an-image).

Note

The wingdi.h header defines GetObject as an alias that automatically selects the ANSI or Unicode version of this function based on the definition of the UNICODE preprocessor constant. Mixing usage of the encoding-neutral alias with code that is not encoding-neutral can lead to mismatches that result in compilation or runtime errors. For more information, see [Conventions for Function Prototypes](/en-us/windows/win32/intl/conventions-for-function-prototypes).

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows 2000 Professional [desktop apps only] |
| **Minimum supported server** | Windows 2000 Server [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | wingdi.h (include Windows.h) |
| **Library** | Gdi32.lib |
| **DLL** | Gdi32.dll |
