<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellitemimagefactory-getimage
retrieved: 2026-10-31T21:17:03.013095+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellitemimagefactory-getimage
content_type: text/markdown
-->

---
layout: Conceptual
title: IShellItemImageFactory::GetImage (shobjidl_core.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellitemimagefactory-getimage
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
UID: NF:shobjidl_core.IShellItemImageFactory.GetImage
description: Gets an HBITMAP that represents an IShellItem.
old-location: shell\IShellItemImageFactory_GetImage.htm
tech.root: shell
ms.assetid: b31a5eb7-f12f-41e0-9047-450240371424
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: GetImage, GetImage method [Windows Shell], GetImage method [Windows Shell],IShellItemImageFactory interface, IShellItemImageFactory interface [Windows Shell],GetImage method, IShellItemImageFactory.GetImage, IShellItemImageFactory::GetImage, SIIGBF_BIGGERSIZEOK, SIIGBF_CROPTOSQUARE, SIIGBF_ICONBACKGROUND, SIIGBF_ICONONLY, SIIGBF_INCACHEONLY, SIIGBF_MEMORYONLY, SIIGBF_RESIZETOFIT, SIIGBF_SCALEUP, SIIGBF_THUMBNAILONLY, SIIGBF_WIDETHUMBNAILS, _shell_IShellItemImageFactory_GetImage, shell.IShellItemImageFactory_GetImage, shobjidl_core/IShellItemImageFactory::GetImage
req.header: shobjidl_core.h
req.include-header: Shobjidl.h
req.target-type: Windows
req.target-min-winverclnt: Windows Vista [desktop apps only]
req.target-min-winversvr: Windows Server 2008 [desktop apps only]
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: Shobjidl.idl
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
- shobjidl_core.h
api_name:
- IShellItemImageFactory.GetImage
locale: en-us
document_id: 90f4e7d8-f8cf-cad4-9bcb-fc20e92c9c88
document_version_independent_id: 112ab3a4-ea8e-e5fa-ec5a-814fbb52ac58
updated_at: 2024-11-20T01:20:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/shobjidl_core/nf-shobjidl_core-ishellitemimagefactory-getimage.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/adea022c86382b9cef5d28bccca8b9b719e57d6b?path=/sdk-api-src/content/shobjidl_core/nf-shobjidl_core-ishellitemimagefactory-getimage.md&_a=contents
git_commit_id: adea022c86382b9cef5d28bccca8b9b719e57d6b
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_shell/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 586
asset_id: shobjidl_core/nf-shobjidl_core-ishellitemimagefactory-getimage
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/shobjidl_core/nf-shobjidl_core-ishellitemimagefactory-getimage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
platformId: 048eb0fb-3b50-6589-b6e8-fafde258380d
---

# IShellItemImageFactory::GetImage (shobjidl_core.h) - Win32 apps | Microsoft Learn

Gets an **HBITMAP** that represents an [IShellItem](/en-us/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem). The default behavior is to load a thumbnail. If there is no thumbnail for the current **IShellItem**, it retrieves an **HBITMAP** for the icon of the item. The thumbnail or icon is extracted if it is not currently cached.

## Syntax

```cpp
HRESULT GetImage(
  [in]  SIZE    size,
  [in]  SIIGBF  flags,
  [out] HBITMAP *phbm
);
```

## Parameters

`[in] size`

Type: **[SIZE](/en-us/windows/win32/api/windef/ns-windef-size)**

A structure that specifies the size of the image to be received.

`[in] flags`

Type: **SIIGBF**

One or more of the following:

#### SIIGBF\_RESIZETOFIT (0x00000000)

Shrink the bitmap as necessary to fit, preserving its aspect ratio.

#### SIIGBF\_BIGGERSIZEOK (0x00000001)

Passed by callers if they want to stretch the returned image themselves. For example, if the caller passes an icon size of 80x80, a 96x96 thumbnail could be returned. This action can be used as a performance optimization if the caller expects that they will need to stretch the image. Note that the Shell implementation of [IShellItemImageFactory](/en-us/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitemimagefactory) performs a GDI stretch blit. If the caller wants a higher quality image stretch than provided through that mechanism, they should pass this flag and perform the stretch themselves.

#### SIIGBF\_MEMORYONLY (0x00000002)

Return the item only if it is already in memory. Do not access the disk even if the item is cached. Note that this only returns an already-cached icon and can fall back to a per-class icon if an item has a per-instance icon that has not been cached. Retrieving a thumbnail, even if it is cached, always requires the disk to be accessed, so **GetImage** should not be called from the UI thread without passing **SIIGBF\_MEMORYONLY**.

#### SIIGBF\_ICONONLY (0x00000004)

Return only the icon, never the thumbnail.

#### SIIGBF\_THUMBNAILONLY (0x00000008)

Return only the thumbnail, never the icon. Note that not all items have thumbnails, so **SIIGBF\_THUMBNAILONLY** will cause the method to fail in these cases.

#### SIIGBF\_INCACHEONLY (0x00000010)

Allows access to the disk, but only to retrieve a cached item. This returns a cached thumbnail if it is available. If no cached thumbnail is available, it returns a cached per-instance icon but does not extract a thumbnail or icon.

#### SIIGBF\_CROPTOSQUARE (0x00000020)

**Introduced in Windows 8**. If necessary, crop the bitmap to a square.

#### SIIGBF\_WIDETHUMBNAILS (0x00000040)

**Introduced in Windows 8**. Stretch and crop the bitmap to a 0.7 aspect ratio.

#### SIIGBF\_ICONBACKGROUND (0x00000080)

**Introduced in Windows 8**. If returning an icon, paint a background using the associated app's registered background color.

#### SIIGBF\_SCALEUP (0x00000100)

**Introduced in Windows 8**. If necessary, stretch the bitmap so that the height and width fit the given size.

`[out] phbm`

Type: **HBITMAP\***

Pointer to a value that, when this method returns successfully, receives the handle of the retrieved bitmap. It is the responsibility of the caller to free this retrieved resource through [DeleteObject](/en-us/windows/desktop/api/wingdi/nf-wingdi-deleteobject) when it is no longer needed.

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Icon extraction can be time consuming. This method generally should not be called from a UI thread to avoid causing that thread to become unresponsive. You can call **IShellItemImageFactory::GetImage** on a UI thread if you set the **SIIGBF\_INCACHEONLY** flag. However, if the image is not found in the cache, the calling application should be prepared to launch a background thread to extract the image. An extraction should never be done on a UI thread.

See the [Using Image Factory](/en-us/windows/win32/shell/samples-usingimagefactory) sample for a full example of how to use this method.

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows Vista [desktop apps only] |
| **Minimum supported server** | Windows Server 2008 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | shobjidl\_core.h (include Shobjidl.h) |
