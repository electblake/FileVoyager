<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-isharedbitmap-getsize
retrieved: 2026-11-01T19:27:39.589686+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-isharedbitmap-getsize
content_type: text/markdown
-->

---
layout: Conceptual
title: ISharedBitmap::GetSize (thumbcache.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-isharedbitmap-getsize
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
UID: NF:thumbcache.ISharedBitmap.GetSize
description: Retrieves the size of the bitmap contained in an ISharedBitmap object.
old-location: shell\ISharedBitmap_GetSize.htm
tech.root: shell
ms.assetid: 612fbb6d-2539-4055-9037-7e64ddced4e9
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: GetSize, GetSize method [Windows Shell], GetSize method [Windows Shell],ISharedBitmap interface, ISharedBitmap interface [Windows Shell],GetSize method, ISharedBitmap.GetSize, ISharedBitmap::GetSize, _shell__GetSize, shell.ISharedBitmap_GetSize, thumbcache/ISharedBitmap::GetSize
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
- ISharedBitmap.GetSize
locale: en-us
document_id: ae0b8a84-3b63-091a-9628-c50867b21680
document_version_independent_id: 85da9936-1b23-e0fb-4170-965c4ccb77d2
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/thumbcache/nf-thumbcache-isharedbitmap-getsize.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/thumbcache/nf-thumbcache-isharedbitmap-getsize.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_shell/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 84
asset_id: thumbcache/nf-thumbcache-isharedbitmap-getsize
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/thumbcache/nf-thumbcache-isharedbitmap-getsize.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 4a7e013b-9843-458e-f35f-e5a79459a50e
---

# ISharedBitmap::GetSize (thumbcache.h) - Win32 apps | Microsoft Learn

Retrieves the size of the bitmap contained in an [ISharedBitmap](/en-us/windows/desktop/api/thumbcache/nn-thumbcache-isharedbitmap) object.

## Syntax

```cpp
HRESULT GetSize(
  [out] SIZE *pSize
);
```

## Parameters

`[out] pSize`

Type: **[SIZE](/en-us/windows/win32/api/windef/ns-windef-size)\***

When this method returns, contains a pointer to a value that specifies the size, in pixels, of the contained bitmap.

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows Vista [desktop apps only] |
| **Minimum supported server** | Windows Server 2008 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | thumbcache.h |
