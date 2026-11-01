<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-deletedc
retrieved: 2026-11-01T19:27:47.155061+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-deletedc
content_type: text/markdown
-->

---
layout: Conceptual
title: DeleteDC function (wingdi.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-deletedc
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
UID: NF:wingdi.DeleteDC
description: The DeleteDC function deletes the specified device context (DC).
old-location: gdi\deletedc.htm
tech.root: gdi
ms.assetid: 1aa549a0-c95f-4385-a30e-8906f67e39cd
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: DeleteDC, DeleteDC function [Windows GDI], _win32_DeleteDC, gdi.deletedc, wingdi/DeleteDC
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
- DeleteDC
locale: en-us
document_id: fcb0a731-61ce-5718-7da0-687497d5110d
document_version_independent_id: 472a0de5-0b8d-cbc3-073a-fc3b1d3037c5
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/wingdi/nf-wingdi-deletedc.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/wingdi/nf-wingdi-deletedc.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_gdi/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 124
asset_id: wingdi/nf-wingdi-deletedc
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/wingdi/nf-wingdi-deletedc.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: c0904482-fcda-c9e0-ece5-114356db40b6
---

# DeleteDC function (wingdi.h) - Win32 apps | Microsoft Learn

The **DeleteDC** function deletes the specified device context (DC).

## Syntax

```cpp
BOOL DeleteDC(
  [in] HDC hdc
);
```

## Parameters

`[in] hdc`

A handle to the device context.

## Return value

If the function succeeds, the return value is nonzero.

If the function fails, the return value is zero.

## Remarks

An application must not delete a DC whose handle was obtained by calling the [GetDC](/en-us/windows/desktop/api/winuser/nf-winuser-getdc) function. Instead, it must call the [ReleaseDC](/en-us/windows/desktop/api/winuser/nf-winuser-releasedc) function to free the DC.

#### Examples

For an example, see [Retrieving the Capabilities of a Printer](/en-us/windows/desktop/gdi/retrieving-the-capabilities-of-a-printer).

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows 2000 Professional [desktop apps only] |
| **Minimum supported server** | Windows 2000 Server [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | wingdi.h (include Windows.h) |
| **Library** | Gdi32.lib |
| **DLL** | Gdi32.dll |
