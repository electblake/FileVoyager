<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-isharedbitmap-detach
retrieved: 2026-11-01T19:27:39.265444+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-isharedbitmap-detach
content_type: text/markdown
-->

---
layout: Conceptual
title: ISharedBitmap::Detach (thumbcache.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-isharedbitmap-detach
adobe-target: true
breadcrumb_path: /windows/desktop/api/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-WinDevCenter
ms.service: windows-api-desktop-tech
ms.subservice: sdk-api-reference
ms.topic: reference
ms.author: jimwalk
author: jwmsft
feedback_system: Standard
feedback_product_url: https://www.microsoft.com/en-us/windowsinsider/feedbackhub/fb
feedback_help_link_url: https://learn.microsoft.com/answers/tags/224/windows-api-win32/
feedback_help_link_type: get-help-at-qna
UID: NF:thumbcache.ISharedBitmap.Detach
description: Retrieves the bitmap contained in an ISharedBitmap object, and returns a copy if the contained bitmap resides in shared memory.
old-location: shell\ISharedBitmap_Detach.htm
tech.root: shell
ms.assetid: 1d68beca-c254-435e-a1cd-04e7aa462c84
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: Detach, Detach method [Windows Shell], Detach method [Windows Shell],ISharedBitmap interface, ISharedBitmap interface [Windows Shell],Detach method, ISharedBitmap.Detach, ISharedBitmap::Detach, _shell__Detach, shell.ISharedBitmap_Detach, thumbcache/ISharedBitmap::Detach
req.header: thumbcache.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows Vista [desktop apps only]
req.target-min-winversvr: Windows Server 2008 [desktop apps only]
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: Thumbcache.idl
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
targetos: Windows
req.typenames: 
req.redist: 
ms.custom: 19H1
topic_type:
- APIRef
- kbSyntax
api_type:
- COM
api_location:
- Thumbcache.h
api_name:
- ISharedBitmap.Detach
locale: en-us
document_id: ffdac1d0-91fd-5f3e-6cb0-16a5e5bc2aeb
document_version_independent_id: 64f72843-59ad-0219-ee32-2bc5ccfd00b2
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/thumbcache/nf-thumbcache-isharedbitmap-detach.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/thumbcache/nf-thumbcache-isharedbitmap-detach.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_shell/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 161
asset_id: thumbcache/nf-thumbcache-isharedbitmap-detach
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/thumbcache/nf-thumbcache-isharedbitmap-detach.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: a1546530-003b-f063-8721-f3c920ff3019
---

# ISharedBitmap::Detach (thumbcache.h) - Win32 apps | Microsoft Learn

Retrieves the bitmap contained in an [ISharedBitmap](/en-us/windows/desktop/api/thumbcache/nn-thumbcache-isharedbitmap) object, and returns a copy if the contained bitmap resides in shared memory. After calling this method the bitmap is no longer associated with this **ISharedBitmap** and you cannot call [ISharedBitmap::GetSharedBitmap](/en-us/windows/desktop/api/thumbcache/nf-thumbcache-isharedbitmap-getsharedbitmap) or **ISharedBitmap::Detach** on it again.

## Syntax

```cpp
HRESULT Detach(
  [out] HBITMAP *phbm
);
```

## Parameters

`[out] phbm`

Type: **HBITMAP\***

When this method returns, contains a pointer to a handle to the bitmap to retrieve.

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If the bitmap being retrieved resides in shared memory, a copy of the bitmap is returned. The **Detach** method does not release any references to the underlying shared memory.

If the bitmap being retrieved does not reside in shared memory, the bitmap itself is returned and no copy is made.

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows Vista [desktop apps only] |
| **Minimum supported server** | Windows Server 2008 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | thumbcache.h |
