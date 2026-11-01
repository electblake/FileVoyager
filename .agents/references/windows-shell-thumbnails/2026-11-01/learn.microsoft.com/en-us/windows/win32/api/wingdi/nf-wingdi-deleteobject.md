<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-deleteobject
retrieved: 2026-11-01T19:27:47.689745+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-deleteobject
content_type: text/markdown
-->

---
layout: Conceptual
title: DeleteObject function (wingdi.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/wingdi/nf-wingdi-deleteobject
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
UID: NF:wingdi.DeleteObject
description: The DeleteObject function deletes a logical pen, brush, font, bitmap, region, or palette, freeing all system resources associated with the object. After the object is deleted, the specified handle is no longer valid.
old-location: gdi\deleteobject.htm
tech.root: gdi
ms.assetid: cc679af0-6839-4c83-9c42-39d7ededda40
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: DeleteObject, DeleteObject function [Windows GDI], DeleteObjectW, _win32_DeleteObject, gdi.deleteobject, wingdi/DeleteObject, wingdi/DeleteObjectW
req.header: wingdi.h
req.include-header: Windows.h
req.target-type: Windows
req.target-min-winverclnt: Windows 2000 Professional [desktop apps only]
req.target-min-winversvr: Windows 2000 Server [desktop apps only]
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: DeleteObjectW (Unicode)
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
- Ext-MS-Win-RTCore-GDI-object-l1-1-0.dll
- api-ms-win-gdi-ie-rgn-l1-1-0.dll
- ie_shims.dll
- ext-ms-win-gdi-dc-l1-1-0.dll
api_name:
- DeleteObject
- DeleteObjectW
locale: en-us
document_id: 908df0bc-2095-df34-3c80-89b12c94f7c0
document_version_independent_id: 54f31889-713f-581a-eeb1-f70834dd8fc5
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/wingdi/nf-wingdi-deleteobject.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/wingdi/nf-wingdi-deleteobject.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_gdi/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 172
asset_id: wingdi/nf-wingdi-deleteobject
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/wingdi/nf-wingdi-deleteobject.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 18085c5a-5f3a-24b8-7844-b259e7eb4cb9
---

# DeleteObject function (wingdi.h) - Win32 apps | Microsoft Learn

The **DeleteObject** function deletes a logical pen, brush, font, bitmap, region, or palette, freeing all system resources associated with the object. After the object is deleted, the specified handle is no longer valid.

## Syntax

```cpp
BOOL DeleteObject(
  [in] HGDIOBJ ho
);
```

## Parameters

`[in] ho`

A handle to a logical pen, brush, font, bitmap, region, or palette.

## Return value

If the function succeeds, the return value is nonzero.

If the specified handle is not valid or is currently selected into a DC, the return value is zero.

## Remarks

Do not delete a drawing object (pen or brush) while it is still selected into a DC.

When a pattern brush is deleted, the bitmap associated with the brush is not deleted. The bitmap must be deleted independently.

#### Examples

For an example, see [Creating Colored Pens and Brushes](/en-us/windows/desktop/gdi/creating-colored-pens-and-brushes).

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows 2000 Professional [desktop apps only] |
| **Minimum supported server** | Windows 2000 Server [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | wingdi.h (include Windows.h) |
| **Library** | Gdi32.lib |
| **DLL** | Gdi32.dll |
