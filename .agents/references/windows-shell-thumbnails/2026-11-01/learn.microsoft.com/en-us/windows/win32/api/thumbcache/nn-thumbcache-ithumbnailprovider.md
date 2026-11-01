<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nn-thumbcache-ithumbnailprovider
retrieved: 2026-11-01T19:27:40.538193+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nn-thumbcache-ithumbnailprovider
content_type: text/markdown
-->

---
layout: Conceptual
title: IThumbnailProvider (thumbcache.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nn-thumbcache-ithumbnailprovider
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
UID: NN:thumbcache.IThumbnailProvider
description: Exposes a method for getting a thumbnail image and is intended to be implemented for thumbnail handlers. The object that implements this interface must also implement IInitializeWithStream.
old-location: shell\IThumbnailProvider.htm
tech.root: shell
ms.assetid: 55c4739a-4835-4f53-a435-804ddf06ffcf
ms.date: 2025-01-22T00:00:00.0000000Z
ms.keywords: IThumbnailProvider, IThumbnailProvider interface [Windows Shell], IThumbnailProvider interface [Windows Shell],described, _shell_IThumbnailProvider, shell.IThumbnailProvider, thumbcache/IThumbnailProvider
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
- IThumbnailProvider
locale: en-us
document_id: 090c44dd-f991-cec2-45d2-76d27b9d8243
document_version_independent_id: ee2dbd01-e939-3b9a-0d8a-300626a27f0a
updated_at: 2025-02-05T19:45:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/thumbcache/nn-thumbcache-ithumbnailprovider.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/a4102fdc373eb926216ccefa4ebcb31f7aaf1a82?path=/sdk-api-src/content/thumbcache/nn-thumbcache-ithumbnailprovider.md&_a=contents
git_commit_id: a4102fdc373eb926216ccefa4ebcb31f7aaf1a82
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_shell/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 309
asset_id: thumbcache/nn-thumbcache-ithumbnailprovider
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/thumbcache/nn-thumbcache-ithumbnailprovider.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: f34a197c-11f6-c584-8689-e8f4632be2a6
---

# IThumbnailProvider (thumbcache.h) - Win32 apps | Microsoft Learn

Exposes a method for getting a thumbnail image and is intended to be implemented for thumbnail handlers. The object that implements this interface must also implement [IInitializeWithStream](/en-us/windows/desktop/api/propsys/nn-propsys-iinitializewithstream).

## Inheritance

The **IThumbnailProvider** interface inherits from the [IUnknown](/en-us/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IThumbnailProvider** also has these types of members:

## Methods

The **IThumbnailProvider** interface has these methods.

| - |
| --- |
| [IThumbnailProvider::GetThumbnail](nf-thumbcache-ithumbnailprovider-getthumbnail)Gets a thumbnail image and alpha type. |

## Remarks

The Shell calls [IThumbnailProvider::GetThumbnail](/en-us/windows/desktop/api/thumbcache/nf-thumbcache-ithumbnailprovider-getthumbnail) to obtain an image to use as a representation of the item.

An implementation of this interface for photo thumbnails is supplied in Microsoft Windows as CLSID\_PhotoThumbnailProvider. Applications that use the supplied implementation must define a constant CLSID identifier using the GUID {C7657C4A-9F68-40fa-A4DF-96BC08EB3551}.

```
// {C7657C4A-9F68-40fa-A4DF-96BC08EB3551}
const CLSID CLSID_PhotoThumbnailProvider = {0xC7657C4A, 0x9F68, 0x40fa, {0xA4, 0xDF, 0x96, 0xBC, 0x08, 0xEB, 0x35, 0x51}} ;
```

**Initializing** The object that implements this interface must also implement [IInitializeWithStream](/en-us/windows/desktop/api/propsys/nn-propsys-iinitializewithstream). The Shell calls [IInitializeWithStream::Initialize](/en-us/windows/desktop/api/propsys/nf-propsys-iinitializewithstream-initialize) with the stream of the item, and **IInitializeWithStream** is the only initialization interface used when IThumbnailProvider instances are loaded out-of-proc (for isolation purposes). This is the primary code path for Windows for all IThumbnailCache code paths.

It is possible for a thumbnail implementation to be initialized with [IInitializeWithItem](/en-us/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iinitializewithitem) or [IInitializeWithFile](/en-us/windows/desktop/api/propsys/nn-propsys-iinitializewithfile) when the handler is request by a 3rd party without using the IThumbnailCache API, but this is uncommon. If you implement **IInitializeWithItem**, the Shell calls [IInitializeWithItem::Initialize](/en-us/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iinitializewithitem-initialize) with the [IShellItem](/en-us/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem) representation of the item. If you implement **IInitializeWithFile**, the Shell calls [IInitializeWithFile::Initialize](/en-us/windows/desktop/api/propsys/nf-propsys-iinitializewithfile-initialize) with the path of the file.

If none of these interfaces is present, **IThumbnailProvider** is not called.

**Client apps** If you're developing a client app, you should use [IShellItemImageFactory](/en-us/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitemimagefactory) instead.

**Windows Vista** IThumbnailProvider is new for Vista and replaces [IExtractImage](/en-us/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iextractimage). Vista still supports IExtractImage but lacks the ability to return the image type (alpha or not).

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows Vista [desktop apps only] |
| **Minimum supported server** | Windows Server 2008 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | thumbcache.h |
