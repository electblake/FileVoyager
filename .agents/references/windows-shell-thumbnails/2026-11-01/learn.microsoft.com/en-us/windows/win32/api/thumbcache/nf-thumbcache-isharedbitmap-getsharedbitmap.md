<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-isharedbitmap-getsharedbitmap
retrieved: 2026-11-01T19:27:38.850029+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-isharedbitmap-getsharedbitmap
content_type: text/markdown
-->

---
layout: Conceptual
title: ISharedBitmap::GetSharedBitmap (thumbcache.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-isharedbitmap-getsharedbitmap
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
UID: NF:thumbcache.ISharedBitmap.GetSharedBitmap
description: Retrieves the bitmap contained in an ISharedBitmap object.
old-location: shell\ISharedBitmap_GetSharedBitmap.htm
tech.root: shell
ms.assetid: 0d2cfdba-b51f-4035-b0b2-e48933505c73
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: GetSharedBitmap, GetSharedBitmap method [Windows Shell], GetSharedBitmap method [Windows Shell],ISharedBitmap interface, ISharedBitmap interface [Windows Shell],GetSharedBitmap method, ISharedBitmap.GetSharedBitmap, ISharedBitmap::GetSharedBitmap, _shell__GetSharedBitmap, shell.ISharedBitmap_GetSharedBitmap, thumbcache/ISharedBitmap::GetSharedBitmap
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
- ISharedBitmap.GetSharedBitmap
locale: en-us
document_id: dd9284e0-25b8-6018-16eb-58fb19c55dac
document_version_independent_id: 3680f03e-e983-f844-5960-5d0d33462e70
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/thumbcache/nf-thumbcache-isharedbitmap-getsharedbitmap.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/thumbcache/nf-thumbcache-isharedbitmap-getsharedbitmap.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_shell/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 77
asset_id: thumbcache/nf-thumbcache-isharedbitmap-getsharedbitmap
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/thumbcache/nf-thumbcache-isharedbitmap-getsharedbitmap.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 8b28bb1f-ea37-dfbe-782e-2e7553fe3785
---

# ISharedBitmap::GetSharedBitmap (thumbcache.h) - Win32 apps | Microsoft Learn

Retrieves the bitmap contained in an [ISharedBitmap](/en-us/windows/desktop/api/thumbcache/nn-thumbcache-isharedbitmap) object.

## Syntax

```cpp
HRESULT GetSharedBitmap(
  [out] HBITMAP *phbm
);
```

## Parameters

`[out] phbm`

Type: **HBITMAP\***

A pointer to a handle to the bitmap.

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The bitmap retrieved might reside in shared memory.

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows Vista [desktop apps only] |
| **Minimum supported server** | Windows Server 2008 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | thumbcache.h |
