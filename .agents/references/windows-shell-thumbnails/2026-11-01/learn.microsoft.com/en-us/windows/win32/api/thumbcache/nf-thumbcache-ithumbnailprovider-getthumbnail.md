<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-ithumbnailprovider-getthumbnail
retrieved: 2026-11-01T19:27:41.020522+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-ithumbnailprovider-getthumbnail
content_type: text/markdown
-->

---
layout: Conceptual
title: IThumbnailProvider::GetThumbnail (thumbcache.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nf-thumbcache-ithumbnailprovider-getthumbnail
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
UID: NF:thumbcache.IThumbnailProvider.GetThumbnail
description: Gets a thumbnail image and alpha type.
old-location: shell\IThumbnailProvider_GetThumbnail.htm
tech.root: shell
ms.assetid: 5ea237fb-6b1c-4e87-a9f3-711ffa37b3dc
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: GetThumbnail, GetThumbnail method [Windows Shell], GetThumbnail method [Windows Shell],IThumbnailProvider interface, IThumbnailProvider interface [Windows Shell],GetThumbnail method, IThumbnailProvider.GetThumbnail, IThumbnailProvider::GetThumbnail, WTSAT_ARGB, WTSAT_RGB, WTSAT_UNKNOWN, _shell_IThumbnailProvider_GetThumbnail, shell.IThumbnailProvider_GetThumbnail, thumbcache/IThumbnailProvider::GetThumbnail
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
- IThumbnailProvider.GetThumbnail
locale: en-us
document_id: 20592807-5e09-f546-0888-00fffa819b02
document_version_independent_id: e630b722-0f21-b891-ebbb-fbc4d8bda22d
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/thumbcache/nf-thumbcache-ithumbnailprovider-getthumbnail.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/thumbcache/nf-thumbcache-ithumbnailprovider-getthumbnail.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_shell/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 278
asset_id: thumbcache/nf-thumbcache-ithumbnailprovider-getthumbnail
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/thumbcache/nf-thumbcache-ithumbnailprovider-getthumbnail.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 3cd73980-1be4-7789-d84a-80ffdde69f77
---

# IThumbnailProvider::GetThumbnail (thumbcache.h) - Win32 apps | Microsoft Learn

Gets a thumbnail image and alpha type.

## Syntax

```cpp
HRESULT GetThumbnail(
  [in]  UINT          cx,
  [out] HBITMAP       *phbmp,
  [out] WTS_ALPHATYPE *pdwAlpha
);
```

## Parameters

`[in] cx`

Type: **UINT**

The maximum thumbnail size, in pixels. The Shell draws the returned bitmap at this size or smaller. The returned bitmap should fit into a square of width and height *cx*, though it does not need to be a square image. The Shell scales the bitmap to render at lower sizes. For example, if the image has a 6:4 aspect ratio, then the returned bitmap should also have a 6:4 aspect ratio.

`[out] phbmp`

Type: **HBITMAP\***

When this method returns, contains a pointer to the thumbnail image handle. The image must be a DIB section and 32 bits per pixel. The Shell scales down the bitmap if its width or height is larger than the size specified by *cx*. The Shell always respects the aspect ratio and never scales a bitmap larger than its original size.

`[out] pdwAlpha`

Type: **WTS\_ALPHATYPE\***

When this method returns, contains a pointer to one of the following values from the WTS\_ALPHATYPE enumeration:

#### WTSAT\_UNKNOWN (0x0)

0x0. The bitmap is an unknown format. The Shell tries nonetheless to detect whether the image has an alpha channel.

#### WTSAT\_RGB (0x1)

0x1. The bitmap is an RGB image without alpha. The alpha channel is invalid and the Shell ignores it.

#### WTSAT\_ARGB (0x2)

0x2. The bitmap is an ARGB image with a valid alpha channel.

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
