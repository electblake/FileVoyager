<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellitemimagefactory
retrieved: 2026-11-01T19:27:41.888268+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellitemimagefactory
content_type: text/markdown
-->

---
layout: Conceptual
title: IShellItemImageFactory (shobjidl_core.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellitemimagefactory
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
UID: NN:shobjidl_core.IShellItemImageFactory
description: Exposes a method to return either icons or thumbnails for Shell items. If no thumbnail or icon is available for the requested item, a per-class icon may be provided from the Shell.
old-location: shell\IShellItemImageFactory.htm
tech.root: shell
ms.assetid: a6eea412-553a-4bdd-afc2-cc002c4500a4
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: IShellItemImageFactory, IShellItemImageFactory interface [Windows Shell], IShellItemImageFactory interface [Windows Shell],described, _shell_IShellItemImageFactory, shell.IShellItemImageFactory, shobjidl_core/IShellItemImageFactory
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
- IShellItemImageFactory
locale: en-us
document_id: 1ba52c7f-41b9-0e71-d1f6-14c276fb225e
document_version_independent_id: 775912c7-2eb3-0cec-9949-c1a4df8eec8c
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/shobjidl_core/nn-shobjidl_core-ishellitemimagefactory.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/shobjidl_core/nn-shobjidl_core-ishellitemimagefactory.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_shell/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 125
asset_id: shobjidl_core/nn-shobjidl_core-ishellitemimagefactory
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/shobjidl_core/nn-shobjidl_core-ishellitemimagefactory.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 584edda3-6d9b-8469-279e-09829235b7c8
---

# IShellItemImageFactory (shobjidl_core.h) - Win32 apps | Microsoft Learn

Exposes a method to return either icons or thumbnails for Shell items. If no thumbnail or icon is available for the requested item, a per-class icon may be provided from the Shell.

## Inheritance

The **IShellItemImageFactory** interface inherits from the [IUnknown](/en-us/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IShellItemImageFactory** also has these types of members:

## Methods

The **IShellItemImageFactory** interface has these methods.

| - |
| --- |
| [IShellItemImageFactory::GetImage](nf-shobjidl_core-ishellitemimagefactory-getimage)Gets an HBITMAP that represents an IShellItem. |

## Remarks

A pointer to this interface is commonly obtained through one of the following functions:

- [SHCreateItemFromIDList](/en-us/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateitemfromidlist)
- [SHCreateItemFromParsingName](/en-us/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateitemfromparsingname)
- [SHCreateItemFromRelativeName](/en-us/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateitemfromrelativename)
- [SHCreateItemInKnownFolder](/en-us/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateiteminknownfolder)
- [SHCreateItemWithParent](/en-us/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateitemwithparent)

 See the [Using Image Factory](/en-us/previous-versions/windows/desktop/legacy/dd940383%28v=vs.85%29) sample for a full example of how to use this interface. 
## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows Vista [desktop apps only] |
| **Minimum supported server** | Windows Server 2008 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | shobjidl\_core.h (include Shobjidl.h) |
