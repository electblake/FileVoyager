<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nn-thumbcache-isharedbitmap
retrieved: 2026-11-01T19:27:38.449244+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nn-thumbcache-isharedbitmap
content_type: text/markdown
-->

---
layout: Conceptual
title: ISharedBitmap (thumbcache.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nn-thumbcache-isharedbitmap
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
UID: NN:thumbcache.ISharedBitmap
description: Exposes memory-efficient methods for accessing bitmaps. This interface is used as a thin wrapper around HBITMAP objects, allowing those objects to be reference counted and protected from having their underlying data changed.
old-location: shell\ISharedBitmap.htm
tech.root: shell
ms.assetid: 72be7757-f969-4f4f-ada1-71789b8d1de0
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: ISharedBitmap, ISharedBitmap interface [Windows Shell], ISharedBitmap interface [Windows Shell],described, _shell_ISharedBitmap, shell.ISharedBitmap, thumbcache/ISharedBitmap
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
- ISharedBitmap
locale: en-us
document_id: 4b9ec4c1-eb07-8c5d-3207-61550b92dc15
document_version_independent_id: 2bf21c5b-fc5e-4db2-c1c4-22d0ef5e8e6f
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/thumbcache/nn-thumbcache-isharedbitmap.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/thumbcache/nn-thumbcache-isharedbitmap.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_shell/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 199
asset_id: thumbcache/nn-thumbcache-isharedbitmap
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/thumbcache/nn-thumbcache-isharedbitmap.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: c4c8b10f-57cd-755d-328f-1104287064d1
---

# ISharedBitmap (thumbcache.h) - Win32 apps | Microsoft Learn

Exposes memory-efficient methods for accessing bitmaps. This interface is used as a thin wrapper around HBITMAP objects, allowing those objects to be reference counted and protected from having their underlying data changed.

## Inheritance

The **ISharedBitmap** interface inherits from the [IUnknown](/en-us/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ISharedBitmap** also has these types of members:

## Methods

The **ISharedBitmap** interface has these methods.

| - |
| --- |
| [ISharedBitmap::Detach](nf-thumbcache-isharedbitmap-detach)Retrieves the bitmap contained in an ISharedBitmap object, and returns a copy if the contained bitmap resides in shared memory. |
| [ISharedBitmap::GetFormat](nf-thumbcache-isharedbitmap-getformat)Retrieves the alpha type of the bitmap image. |
| [ISharedBitmap::GetSharedBitmap](nf-thumbcache-isharedbitmap-getsharedbitmap)Retrieves the bitmap contained in an ISharedBitmap object. |
| [ISharedBitmap::GetSize](nf-thumbcache-isharedbitmap-getsize)Retrieves the size of the bitmap contained in an ISharedBitmap object. |
| [ISharedBitmap::InitializeBitmap](nf-thumbcache-isharedbitmap-initializebitmap)Initializes a new ISharedBitmap object with a given bitmap. |

## Remarks

This interface is used in conjunction with the methods of [IThumbnailCache](/en-us/windows/desktop/api/thumbcache/nn-thumbcache-ithumbnailcache). Bitmaps returned by [IThumbnailCache::GetThumbnail](/en-us/windows/desktop/api/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnail) and [IThumbnailCache::GetThumbnailByID](/en-us/windows/desktop/api/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnailbyid) are of type **ISharedBitmap**.

When an **ISharedBitmap** object is retrieved from the thumbnail cache, the underlying bitmap may reside in shared memory to provide improved performance.

The underlying data of the memory-mapped bitmap is protected while the client is accessing it.

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows Vista [desktop apps only] |
| **Minimum supported server** | Windows Server 2008 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | thumbcache.h |
