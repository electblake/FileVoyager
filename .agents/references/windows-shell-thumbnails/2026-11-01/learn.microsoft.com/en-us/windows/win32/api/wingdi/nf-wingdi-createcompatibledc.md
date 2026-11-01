<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-createcompatibledc
retrieved: 2026-11-01T19:27:46.755154+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-createcompatibledc
content_type: text/markdown
-->

---
layout: Conceptual
title: CreateCompatibleDC function (wingdi.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-createcompatibledc
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
UID: NF:wingdi.CreateCompatibleDC
description: The CreateCompatibleDC function creates a memory device context (DC) compatible with the specified device.
old-location: gdi\createcompatibledc.htm
tech.root: gdi
ms.assetid: 6ddc3705-2995-41af-af94-258aed597e17
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: CreateCompatibleDC, CreateCompatibleDC function [Windows GDI], _win32_CreateCompatibleDC, gdi.createcompatibledc, wingdi/CreateCompatibleDC
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
- Ext-MS-Win-GDI-DC-Create-l1-1-0.dll
- Ext-MS-Win-GDI-DC-Create-l1-1-1.dll
- ext-ms-win-gdi-dc-create-l1-1-2.dll
- GDI32Full.dll
api_name:
- CreateCompatibleDC
locale: en-us
document_id: c4ff44c0-84d4-7d82-6d10-b9dea5bf20d4
document_version_independent_id: 4189eabc-ae6c-ffd3-6dd2-bf13418de667
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/wingdi/nf-wingdi-createcompatibledc.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/wingdi/nf-wingdi-createcompatibledc.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_gdi/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 387
asset_id: wingdi/nf-wingdi-createcompatibledc
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/wingdi/nf-wingdi-createcompatibledc.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: f893ce15-dcbf-7af2-c3bc-13220544b901
---

# CreateCompatibleDC function (wingdi.h) - Win32 apps | Microsoft Learn

The **CreateCompatibleDC** function creates a memory device context (DC) compatible with the specified device.

## Syntax

```cpp
HDC CreateCompatibleDC(
  [in] HDC hdc
);
```

## Parameters

`[in] hdc`

A handle to an existing DC. If this handle is **NULL**, the function creates a memory DC compatible with the application's current screen.

## Return value

If the function succeeds, the return value is the handle to a memory DC.

If the function fails, the return value is **NULL**.

## Remarks

A memory DC exists only in memory. When the memory DC is created, its display surface is exactly one monochrome pixel wide and one monochrome pixel high. Before an application can use a memory DC for drawing operations, it must select a bitmap of the correct width and height into the DC. To select a bitmap into a DC, use the [CreateCompatibleBitmap](/en-us/windows/desktop/api/wingdi/nf-wingdi-createcompatiblebitmap) function, specifying the height, width, and color organization required.

When a memory DC is created, all attributes are set to normal default values. The memory DC can be used as a normal DC. You can set the attributes; obtain the current settings of its attributes; and select pens, brushes, and regions.

The **CreateCompatibleDC** function can only be used with devices that support raster operations. An application can determine whether a device supports these operations by calling the [GetDeviceCaps](/en-us/windows/desktop/api/wingdi/nf-wingdi-getdevicecaps) function.

When you no longer need the memory DC, call the [DeleteDC](/en-us/windows/desktop/api/wingdi/nf-wingdi-deletedc) function. We recommend that you call **DeleteDC** to delete the DC. However, you can also call [DeleteObject](/en-us/windows/desktop/api/wingdi/nf-wingdi-deleteobject) with the HDC to delete the DC.

If *hdc* is **NULL**, the thread that calls **CreateCompatibleDC** owns the HDC that is created. When this thread is destroyed, the HDC is no longer valid. Thus, if you create the HDC and pass it to another thread, then exit the first thread, the second thread will not be able to use the HDC.

**ICM:** If the DC that is passed to this function is enabled for Image Color Management (ICM), the DC created by the function is ICM-enabled. The source and destination color spaces are specified in the DC.

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
