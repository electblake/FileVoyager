<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-isharedbitmap-getformat
retrieved: 2026-11-01T19:27:40.017597+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-isharedbitmap-getformat
content_type: text/markdown
-->

---
layout: Conceptual
title: ISharedBitmap::GetFormat (thumbcache.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-isharedbitmap-getformat
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
UID: NF:thumbcache.ISharedBitmap.GetFormat
description: Retrieves the alpha type of the bitmap image.
old-location: shell\ISharedBitmap_GetFormat.htm
tech.root: shell
ms.assetid: 403b8b19-c96f-4205-999f-103025d2b923
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: GetFormat, GetFormat method [Windows Shell], GetFormat method [Windows Shell],ISharedBitmap interface, ISharedBitmap interface [Windows Shell],GetFormat method, ISharedBitmap.GetFormat, ISharedBitmap::GetFormat, WTSAT_ARGB, WTSAT_RGB, _shell_ISharedBitmap_GetFormat, shell.ISharedBitmap_GetFormat, thumbcache/ISharedBitmap::GetFormat
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
- ISharedBitmap.GetFormat
locale: en-us
document_id: dd8e67d1-9fc8-f5ab-0ff9-f27f733a63f4
document_version_independent_id: d12de8be-c067-db1a-d69e-95e436b31165
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/thumbcache/nf-thumbcache-isharedbitmap-getformat.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/thumbcache/nf-thumbcache-isharedbitmap-getformat.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_shell/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 100
asset_id: thumbcache/nf-thumbcache-isharedbitmap-getformat
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/thumbcache/nf-thumbcache-isharedbitmap-getformat.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 02ff93f3-a4c1-5400-2ccb-5ed2277b75fb
---

# ISharedBitmap::GetFormat (thumbcache.h) - Win32 apps | Microsoft Learn

Retrieves the alpha type of the bitmap image.

## Syntax

```cpp
HRESULT GetFormat(
  [out] WTS_ALPHATYPE *pat
);
```

## Parameters

`[out] pat`

Type: **WTS\_ALPHATYPE\***

When this method returns, contains a pointer to the alpha type of the bitmap image. One of the following values.

#### WTSAT\_RGB

The bitmap does not contain an alpha channel for transparency.

#### WTSAT\_ARGB

The bitmap contains an alpha channel for transparency.

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
