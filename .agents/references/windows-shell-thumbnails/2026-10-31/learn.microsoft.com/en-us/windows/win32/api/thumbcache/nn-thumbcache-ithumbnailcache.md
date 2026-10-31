<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nn-thumbcache-ithumbnailcache
retrieved: 2026-10-31T21:17:03.348315+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nn-thumbcache-ithumbnailcache
content_type: text/markdown
-->

---
layout: Conceptual
title: IThumbnailCache (thumbcache.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nn-thumbcache-ithumbnailcache
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
UID: NN:thumbcache.IThumbnailCache
description: Exposes methods for a system thumbnail cache that is shared across applications.
old-location: shell\IThumbnailCache.htm
tech.root: shell
ms.assetid: b0ddfca0-49b8-4f53-8d22-9a561d09367a
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: IThumbnailCache, IThumbnailCache interface [Windows Shell], IThumbnailCache interface [Windows Shell],described, _shell_IThumbnailCache, shell.IThumbnailCache, thumbcache/IThumbnailCache
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
- IThumbnailCache
locale: en-us
document_id: e458fe71-5d94-54f4-b987-ccb2d855d638
document_version_independent_id: 66e3aa8a-da47-93c9-be51-00aca8a4ba47
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/thumbcache/nn-thumbcache-ithumbnailcache.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/thumbcache/nn-thumbcache-ithumbnailcache.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_shell/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 439
asset_id: thumbcache/nn-thumbcache-ithumbnailcache
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/thumbcache/nn-thumbcache-ithumbnailcache.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
platformId: 4a90d4b2-1645-8016-404b-b749c65b7d1b
---

# IThumbnailCache (thumbcache.h) - Win32 apps | Microsoft Learn

Exposes methods for a system thumbnail cache that is shared across applications.

## Inheritance

The **IThumbnailCache** interface inherits from the [IUnknown](/en-us/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IThumbnailCache** also has these types of members:

## Methods

The **IThumbnailCache** interface has these methods.

| - |
| --- |
| [IThumbnailCache::GetThumbnail](nf-thumbcache-ithumbnailcache-getthumbnail)Gets a cached thumbnail for a given Shell item. |
| [IThumbnailCache::GetThumbnailByID](nf-thumbcache-ithumbnailcache-getthumbnailbyid)Gets a thumbnail from the thumbnail cache, given its ID. |

## Remarks

The Thumbnail Cache API is designed to provide applications with a unified method to retrieve and cache thumbnails. In Windows XP, thumbnail caching is done on a per-folder basis, and the cache is maintained in a Thumbs.db file within each folder. While this approach provides spatial locality, it does not support previews and queries across folders. The thumbnail cache in Windows Vista addresses this shortcoming by providing a global cache.

To cache a thumbnail, an application must first obtain an [IShellItem](/en-us/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem) that represents the item for which a thumbnail will be obtained, and then pass the **IShellItem** to a call to [IThumbnailCache::GetThumbnail](/en-us/windows/desktop/api/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnail). If the flags parameter to **IThumbnailCache::GetThumbnail** includes the flag WTS\_EXTRACT, and the thumbnail is not already cached, a thumbnail will be extracted and placed in the cache. If the flag WTS\_FORCEEXTRACTION is set, the cache is ignored and a new thumbnail is always extracted. See the **IThumbnailCache::GetThumbnail** topic for more details on the flags passed to **IThumbnailCache::GetThumbnail**.

If a thumbnail is not already in the cache, it will be automatically extracted from the source file using the existing implementation(s) of [IExtractImage](/en-us/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iextractimage) or [IThumbnailProvider](/en-us/windows/desktop/api/thumbcache/nn-thumbcache-ithumbnailprovider) that is registered on the operating system. Your application does not have to provide an implementation of the thumbnail extractor.

When [IThumbnailCache::GetThumbnail](/en-us/windows/desktop/api/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnail) returns, its *pThumbnailID* parameter receives a WTS\_THUMBNAILID structure that contains the unique ID of the thumbnail. If this ID is saved, it can then be passed to [IThumbnailCache::GetThumbnailByID](/en-us/windows/desktop/api/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnailbyid) to retrieve the cached thumbnail. Alternatively, **IThumbnailCache::GetThumbnail** may be called with the WTS\_CACHEONLY flag set. In this case, a thumbnail will be returned only if it is already cached. The disadvantage of using **IThumbnailCache::GetThumbnail** rather than **IThumbnailCache::GetThumbnailByID**, is that an [IShellItem](/en-us/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem) must still be provided.

Multiple threads can be used to access the thumbnail cache to improve performance. [IThumbnailCache::GetThumbnail](/en-us/windows/desktop/api/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnail) may be called on a higher priority thread with either the WTS\_INCACHEONLY or the WTS\_FASTEXTRACT flag set, so that cached thumbnails are retrieved immediately. Then if the image is not in the cache, or WTS\_LOWQUALITY indicates the cached image was not of ideal quality, a lower priority thread may be used to call **IThumbnailCache::GetThumbnail** with the WTS\_EXTRACT flag set, so that a thumbnail may be extracted.

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows Vista [desktop apps only] |
| **Minimum supported server** | Windows Server 2008 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | thumbcache.h |
