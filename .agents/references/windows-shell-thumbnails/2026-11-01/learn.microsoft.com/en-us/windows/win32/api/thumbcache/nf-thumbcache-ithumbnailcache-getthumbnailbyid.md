<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnailbyid
retrieved: 2026-11-01T19:27:37.171388+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnailbyid
content_type: text/markdown
-->

---
layout: Conceptual
title: IThumbnailCache::GetThumbnailByID (thumbcache.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnailbyid
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
UID: NF:thumbcache.IThumbnailCache.GetThumbnailByID
description: Gets a thumbnail from the thumbnail cache, given its ID.
old-location: shell\IThumbnailCache_GetThumbnailByID.htm
tech.root: shell
ms.assetid: 3b5069e2-f20b-4c43-a9e7-334366980f5c
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: GetThumbnailByID, GetThumbnailByID method [Windows Shell], GetThumbnailByID method [Windows Shell],IThumbnailCache interface, IThumbnailCache interface [Windows Shell],GetThumbnailByID method, IThumbnailCache.GetThumbnailByID, IThumbnailCache::GetThumbnailByID, WTS_CACHED, WTS_DEFAULT, WTS_LOWQUALITY, _shell__GetThumbnailByID, shell.IThumbnailCache_GetThumbnailByID, thumbcache/IThumbnailCache::GetThumbnailByID
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
- IThumbnailCache.GetThumbnailByID
locale: en-us
document_id: c6119e63-5c72-40ae-06d3-b73aff7c4b46
document_version_independent_id: afe27b5c-b0dc-b54a-bf97-1f2924e156d1
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnailbyid.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnailbyid.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_shell/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 279
asset_id: thumbcache/nf-thumbcache-ithumbnailcache-getthumbnailbyid
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnailbyid.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 3ff7a398-e3a7-429f-f519-c840be7f25e9
---

# IThumbnailCache::GetThumbnailByID (thumbcache.h) - Win32 apps | Microsoft Learn

Gets a thumbnail from the thumbnail cache, given its ID.

## Syntax

```cpp
HRESULT GetThumbnailByID(
  [in]            WTS_THUMBNAILID thumbnailID,
  [in]            UINT            cxyRequestedThumbSize,
  [out, optional] ISharedBitmap   **ppvThumb,
  [out, optional] WTS_CACHEFLAGS  *pOutFlags
);
```

## Parameters

`[in] thumbnailID`

Type: **[WTS_THUMBNAILID](/en-us/windows/desktop/api/thumbcache/ns-thumbcache-wts_thumbnailid)**

The ID of the thumbnail to retrieve. The ID is obtained by calling [GetThumbnail](/en-us/windows/desktop/api/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnail).

`[in] cxyRequestedThumbSize`

Type: **UINT**

The requested thumbnail size in pixels. This value cannot be larger than 1024.

`[out, optional] ppvThumb`

Type: **[ISharedBitmap](/en-us/windows/desktop/api/thumbcache/nn-thumbcache-isharedbitmap)\*\***

The address of a [ISharedBitmap](/en-us/windows/desktop/api/thumbcache/nn-thumbcache-isharedbitmap) interface pointer that, when this method returns successfully, receives the object for accessing the requested thumbnail. This parameter can be **NULL**.

`[out, optional] pOutFlags`

Type: **WTS\_CACHEFLAGS\***

A pointer to a value that, when this method returns successfully, receives a combination of the following flags. This value can be set to **NULL** if this information is not needed.

#### WTS\_DEFAULT (0x00000000)

0x00000000.

#### WTS\_LOWQUALITY (0x00000001)

0x00000001. Set when the returned bitmap dimensions are less than *cxyRequestedThumbSize*.

#### WTS\_CACHED (0x00000002)

0x00000002. Set when the returned image is in the cache.

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or an error value otherwise, including the following:

| Return code | Description |
| --- | --- |
| - **E\_INVALIDARG** | A parameter is invalid. |
| - **WTS\_E\_FAILEDEXTRACTION** | The Shell item does not support thumbnail extraction. For example, .exe or .lnk items. |
| - **WTS\_E\_EXTRACTIONTIMEDOUT** | The extraction took longer than the maximum allowable time. The extraction was not completed. |
| - **WTS\_E\_SURROGATEUNAVAILABLE** | A surrogate process was not available to be used for the extraction process. |
| - **WTS\_E\_FASTEXTRACTIONNOTSUPPORTED** | The WTS\_FASTEXTRACT flag was set, but fast extraction is not available. |

## Remarks

This method is typically called after [GetThumbnail](/en-us/windows/desktop/api/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnail) has already been called to retrieve the thumbnail ID.

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows Vista [desktop apps only] |
| **Minimum supported server** | Windows Server 2008 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | thumbcache.h |
