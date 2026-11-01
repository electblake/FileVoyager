<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/ne-thumbcache-wts_flags
retrieved: 2026-11-01T19:27:37.486665+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/ne-thumbcache-wts_flags
content_type: text/markdown
-->

---
layout: Conceptual
title: WTS_FLAGS (thumbcache.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/ne-thumbcache-wts_flags
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
UID: NE:thumbcache.WTS_FLAGS
description: Values used by IThumbnailCache::GetThumbnail to specify options for the extraction and display of the thumbnail image.
old-location: shell\WTS_FLAGS.htm
tech.root: shell
ms.assetid: D9C84E86-35AF-437f-966E-BABD02B824C0
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: WTS_APPSTYLE, WTS_CROPTOSQUARE, WTS_EXTRACT, WTS_EXTRACTDONOTCACHE, WTS_EXTRACTINPROC, WTS_FASTEXTRACT, WTS_FLAGS, WTS_FLAGS enumeration [Windows Shell], WTS_FORCEEXTRACTION, WTS_IDEALCACHESIZEONLY, WTS_INCACHEONLY, WTS_INSTANCESURROGATE, WTS_NONE, WTS_REQUIRESURROGATE, WTS_SCALETOREQUESTEDSIZE, WTS_SCALEUP, WTS_SKIPFASTEXTRACT, WTS_SLOWRECLAIM, WTS_WIDETHUMBNAILS, shell.WTS_FLAGS, thumbcache/WTS_APPSTYLE, thumbcache/WTS_CROPTOSQUARE, thumbcache/WTS_EXTRACT, thumbcache/WTS_EXTRACTDONOTCACHE, thumbcache/WTS_EXTRACTINPROC, thumbcache/WTS_FASTEXTRACT, thumbcache/WTS_FLAGS, thumbcache/WTS_FORCEEXTRACTION, thumbcache/WTS_IDEALCACHESIZEONLY, thumbcache/WTS_INCACHEONLY, thumbcache/WTS_INSTANCESURROGATE, thumbcache/WTS_NONE, thumbcache/WTS_REQUIRESURROGATE, thumbcache/WTS_SCALETOREQUESTEDSIZE, thumbcache/WTS_SCALEUP, thumbcache/WTS_SKIPFASTEXTRACT, thumbcache/WTS_SLOWRECLAIM, thumbcache/WTS_WIDETHUMBNAILS
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
req.typenames: WTS_FLAGS
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
- WTS_FLAGS
locale: en-us
document_id: 7301eb62-3f6a-82ad-8fa8-164786aa7da5
document_version_independent_id: 2e617980-7d7d-554c-2ba3-640e40723e46
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/thumbcache/ne-thumbcache-wts_flags.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/thumbcache/ne-thumbcache-wts_flags.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_shell/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 524
asset_id: thumbcache/ne-thumbcache-wts_flags
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/thumbcache/ne-thumbcache-wts_flags.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
platformId: 6a1e11bf-bdff-a9f9-b515-ed9e21fd2a04
---

# WTS_FLAGS (thumbcache.h) - Win32 apps | Microsoft Learn

Values used by [IThumbnailCache::GetThumbnail](/en-us/windows/desktop/api/thumbcache/nf-thumbcache-ithumbnailcache-getthumbnail) to specify options for the extraction and display of the thumbnail image.

## Syntax

```cpp
typedef enum WTS_FLAGS {
  WTS_NONE = 0,
  WTS_EXTRACT = 0,
  WTS_INCACHEONLY = 0x1,
  WTS_FASTEXTRACT = 0x2,
  WTS_FORCEEXTRACTION = 0x4,
  WTS_SLOWRECLAIM = 0x8,
  WTS_EXTRACTDONOTCACHE = 0x20,
  WTS_SCALETOREQUESTEDSIZE = 0x40,
  WTS_SKIPFASTEXTRACT = 0x80,
  WTS_EXTRACTINPROC = 0x100,
  WTS_CROPTOSQUARE = 0x200,
  WTS_INSTANCESURROGATE = 0x400,
  WTS_REQUIRESURROGATE = 0x800,
  WTS_APPSTYLE = 0x2000,
  WTS_WIDETHUMBNAILS = 0x4000,
  WTS_IDEALCACHESIZEONLY = 0x8000,
  WTS_SCALEUP = 0x10000
} ;
```

## Constants

| - |
| --- |
| `WTS_NONE`Value: *0*0x00000000. **Introduced in Windows 8**. None of the following options are set. |
| `WTS_EXTRACT`Value: *0*Default. 0x00000000. Extract the thumbnail if it is not cached. |
| `WTS_INCACHEONLY`Value: *0x1*0x00000001. Only return the thumbnail if it is cached. |
| `WTS_FASTEXTRACT`Value: *0x2*0x00000002. If not cached, only extract the thumbnail if it is embedded in EXIF format, typically 96x96. |
| `WTS_FORCEEXTRACTION`Value: *0x4*0x00000004. Ignore cache and extract thumbnail from source file. |
| `WTS_SLOWRECLAIM`Value: *0x8*0x00000008. The thumbnail has an extended lifetime. Use for volumes that might go offline, like non-fixed disks. |
| `WTS_EXTRACTDONOTCACHE`Value: *0x20*0x00000020. Extract but do not add the thumbnail to the cache. |
| `WTS_SCALETOREQUESTEDSIZE`Value: *0x40*0x00000040. **Introduced in Windows 7**. If the specific thumbnail size requested in the *cxyRequestedThumbSize* parameter is not available, resize the thumbnail to the requested size. If possible, a larger bitmap is reduced in scale, preserving its aspect ratio, to the width and height required. If the only available cached thumbnail is smaller than the requested size, then it is scaled up using the nearest-neighbor algorithm. |
| `WTS_SKIPFASTEXTRACT`Value: *0x80*0x00000080. **Introduced in Windows 7**. Do not extract a thumbnail embedded in the metadata of an EXIF image. |
| `WTS_EXTRACTINPROC`Value: *0x100*0x00000100. **Introduced in Windows 7**. Ensures that the thumbnail handler is loaded in the same process as the caller. When this flag is not specified, the handler is loaded into a surrogate process to protect the caller from unexpected crashes caused by the processing of the target file. Use this value when debugging thumbnail extractors. |
| `WTS_CROPTOSQUARE`Value: *0x200*0x00000200. **Introduced in Windows 8**. If necessary, crop the bitmap's dimensions so that is square. The length of the shortest side becomes the length of all sides. |
| `WTS_INSTANCESURROGATE`Value: *0x400*0x00000400. **Introduced in Windows 8**. Create a surrogate for this instance of the cache rather than using the shared DLLHost surrogate. |
| `WTS_REQUIRESURROGATE`Value: *0x800*0x00000800. **Introduced in Windows 8**. Require extractions to take place in the surrogate. |
| `WTS_APPSTYLE`Value: *0x2000*0x00002000. **Windows 8 and later**. Pass the [WTSCF_APPSTYLE](/en-us/windows/desktop/api/thumbcache/ne-thumbcache-wts_contextflags) flag to [IThumbnailSettings::SetContext](/en-us/windows/desktop/api/thumbcache/nf-thumbcache-ithumbnailsettings-setcontext), if the provider supports it. |
| `WTS_WIDETHUMBNAILS`Value: *0x4000*0x00004000. **Windows 8 and later**. Stretch and crop the bitmap so that its height is 0.7 times its width. |
| `WTS_IDEALCACHESIZEONLY`Value: *0x8000*0x00008000. **Windows 8 and later**. Return from the ideal cache snap size only. The returned image might be larger, but it will be pulled from the correct cache entry. |
| `WTS_SCALEUP`Value: *0x10000*0x00010000. **Windows 8 and later**. If necessary, stretch the image so that the height and width fit the given size. |

## Remarks

The following combinations are valid.

| WTS\_INCACHEONLY |
| --- |
| WTS\_FASTEXTRACT |
| WTS\_EXTRACT |
| WTS\_EXTRACT | WTS\_SLOWRECLAIM |
| WTS\_FORCEEXTRACTION |
| WTS\_FORCEEXTRACTION | WTS\_SLOWRECLAIM |
| WTS\_EXTRACTDONOTCACHE |

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows Vista [desktop apps only] |
| **Minimum supported server** | Windows Server 2008 [desktop apps only] |
| **Header** | thumbcache.h |
