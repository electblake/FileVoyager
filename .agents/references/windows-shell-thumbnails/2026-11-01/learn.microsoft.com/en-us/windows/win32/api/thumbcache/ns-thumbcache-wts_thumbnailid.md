<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/ns-thumbcache-wts_thumbnailid
retrieved: 2026-11-01T19:27:38.014811+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/ns-thumbcache-wts_thumbnailid
content_type: text/markdown
-->

---
layout: Conceptual
title: WTS_THUMBNAILID (thumbcache.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/ns-thumbcache-wts_thumbnailid
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
UID: NS:thumbcache.WTS_THUMBNAILID
description: Contains a unique identifier for a thumbnail in the system thumbnail cache.
old-location: shell\WTS_THUMBNAILID.htm
tech.root: shell
ms.assetid: 3006d1a8-c9cf-4528-9aea-8ad5d97ddff0
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: WTS_THUMBNAILID, WTS_THUMBNAILID structure [Windows Shell], _shell_WTS_THUMBNAILID, shell.WTS_THUMBNAILID, thumbcache/WTS_THUMBNAILID
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
req.typenames: WTS_THUMBNAILID
req.redist: 
ms.custom: 19H1
topic_type:
- APIRef
- kbSyntax
api_type:
- HeaderDef
api_location:
- Thumbcache.h
api_name:
- WTS_THUMBNAILID
locale: en-us
document_id: adefce9e-1402-93f5-0c87-812cd0cc2b64
document_version_independent_id: f7818161-c1e0-32f9-fccb-50ccb32d07ad
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/thumbcache/ns-thumbcache-wts_thumbnailid.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/thumbcache/ns-thumbcache-wts_thumbnailid.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_shell/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 98
asset_id: thumbcache/ns-thumbcache-wts_thumbnailid
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/thumbcache/ns-thumbcache-wts_thumbnailid.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 02a24726-f926-f983-d7f1-583612a82645
---

# WTS_THUMBNAILID (thumbcache.h) - Win32 apps | Microsoft Learn

Contains a unique identifier for a thumbnail in the system thumbnail cache.

## Syntax

```cpp
typedef struct WTS_THUMBNAILID {
  BYTE rgbKey[16];
} WTS_THUMBNAILID;
```

## Members

`rgbKey[16]`

Type: **BYTE[16]**

An array of 16 bytes that make up a unique identifier for a thumbnail in the system thumbnail cache.

## Remarks

A **WTS\_THUMBNAILID** may be retrieved from [IThumbnailCache::GetThumbnail](/en-us/windows/desktop/api/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnail) when a new thumbnail is cached. To access the cached thumbnail by its ID, the **WTS\_THUMBNAILID** may then be passed to [IThumbnailCache::GetThumbnailByID](/en-us/windows/desktop/api/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnailbyid).

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows Vista [desktop apps only] |
| **Minimum supported server** | Windows Server 2008 [desktop apps only] |
| **Header** | thumbcache.h |
