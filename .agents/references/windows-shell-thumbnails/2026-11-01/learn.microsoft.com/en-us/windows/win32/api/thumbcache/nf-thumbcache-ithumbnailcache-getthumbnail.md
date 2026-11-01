<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnail
retrieved: 2026-11-01T19:27:36.607253+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnail
content_type: text/markdown
-->

---
layout: Conceptual
title: IThumbnailCache::GetThumbnail (thumbcache.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnail
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
UID: NF:thumbcache.IThumbnailCache.GetThumbnail
description: Gets a cached thumbnail for a given Shell item.
old-location: shell\IThumbnailCache_GetThumbnail.htm
tech.root: shell
ms.assetid: 0fcfe68b-5d36-4be1-a468-b5c2d7af0651
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: GetThumbnail, GetThumbnail method [Windows Shell], GetThumbnail method [Windows Shell],IThumbnailCache interface, IThumbnailCache interface [Windows Shell],GetThumbnail method, IThumbnailCache.GetThumbnail, IThumbnailCache::GetThumbnail, WTS_CACHED, WTS_DEFAULT, WTS_LOWQUALITY, _shell__GetThumbnail, shell.IThumbnailCache_GetThumbnail, thumbcache/IThumbnailCache::GetThumbnail
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
- IThumbnailCache.GetThumbnail
locale: en-us
document_id: 2af043ce-6f12-575c-dfc2-694564c697f6
document_version_independent_id: cc64dfe1-e1e3-3b86-4808-e5529982321c
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnail.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnail.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_shell/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 386
asset_id: thumbcache/nf-thumbcache-ithumbnailcache-getthumbnail
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnail.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 600fb42f-bdb4-653d-9182-f93f6e247608
---

# IThumbnailCache::GetThumbnail (thumbcache.h) - Win32 apps | Microsoft Learn

Gets a cached thumbnail for a given Shell item.

## Syntax

```cpp
HRESULT GetThumbnail(
  [in]            IShellItem      *pShellItem,
  [in]            UINT            cxyRequestedThumbSize,
  [in]            WTS_FLAGS       flags,
  [out, optional] ISharedBitmap   **ppvThumb,
  [out, optional] WTS_CACHEFLAGS  *pOutFlags,
  [out, optional] WTS_THUMBNAILID *pThumbnailID
);
```

## Parameters

`[in] pShellItem`

Type: **[IShellItem](/en-us/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem)\***

A pointer to the Shell item for which to retrieve a thumbnail.

`[in] cxyRequestedThumbSize`

Type: **UINT**

The requested thumbnail size in pixels. The maximum value is 1024.

`[in] flags`

Type: **[WTS_FLAGS](/en-us/windows/desktop/api/thumbcache/ne-thumbcache-wts_flags)**

A combination of values from the [WTS_FLAGS](/en-us/windows/desktop/api/thumbcache/ne-thumbcache-wts_flags) enumeration. See the Remarks section for rules and a list of possible combinations.

`[out, optional] ppvThumb`

Type: **[ISharedBitmap](/en-us/windows/desktop/api/thumbcache/nn-thumbcache-isharedbitmap)\*\***

The address of an [ISharedBitmap](/en-us/windows/desktop/api/thumbcache/nn-thumbcache-isharedbitmap) pointer that, when this method returns successfully, receives the object used to access the thumbnail. This parameter may be **NULL**.

`[out, optional] pOutFlags`

Type: **WTS\_CACHEFLAGS\***

A pointer to a value that, when this method returns successfully, receives a combination of the following flags from the WTS\_CACHEFLAGS enumeration.

#### WTS\_DEFAULT (0x00000000)

0x00000000.

#### WTS\_LOWQUALITY (0x00000001)

0x00000001. Set when the returned bitmap dimensions are less than *cxyRequestedThumbSize*.

#### WTS\_CACHED (0x00000002)

0x00000002. Set when the returned image is in the cache.

`[out, optional] pThumbnailID`

Type: **[WTS_THUMBNAILID](/en-us/windows/desktop/api/thumbcache/ns-thumbcache-wts_thumbnailid)\***

A pointer to a value that, when this method returns successfully, receives a unique ID for the returned thumbnail. This parameter may be **NULL**, in which case the thumbnail ID is discarded.

## Return value

Type: **HRESULT**

Returns S\_OK if successful or a standard COM error value otherwise, including the following:

| Return code | Description |
| --- | --- |
| - **E\_INVALIDARG** | A parameter is invalid. |
| - **WTS\_E\_FAILEDEXTRACTION** | The Shell item does not support thumbnail extraction. For example, .exe or .lnk items. |
| - **WTS\_E\_EXTRACTIONTIMEDOUT** | The extraction took longer than the maximum allowable time. The extraction was not completed. |
| - **WTS\_E\_SURROGATEUNAVAILABLE** | A surrogate process was not available to be used for the extraction process. |
| - **WTS\_E\_FASTEXTRACTIONNOTSUPPORTED** | The WTS\_FASTEXTRACT flag was set, but fast extraction is not available. |

## Remarks

If a thumbnail is extracted, it will be cached unless WTS\_EXTRACTDONOTCACHE is specified.

The following combinations are valid for the flags parameter.

| WTS\_INCACHEONLY |
| --- |
| WTS\_FASTEXTRACT |
| WTS\_EXTRACT |
| WTS\_EXTRACT | WTS\_SLOWRECLAIM |
| WTS\_FORCEEXTRACTION |
| WTS\_FORCEEXTRACTION | WTS\_SLOWRECLAIM |
| WTS\_EXTRACTDONOTCACHE |

[GetImage](/en-us/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellitemimagefactory-getimage) also uses this cache and can provide an easier way to retrieve the thumbnail. However, **GetImage** is more general and will retrieve an icon as a fallback.

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows Vista [desktop apps only] |
| **Minimum supported server** | Windows Server 2008 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | thumbcache.h |
