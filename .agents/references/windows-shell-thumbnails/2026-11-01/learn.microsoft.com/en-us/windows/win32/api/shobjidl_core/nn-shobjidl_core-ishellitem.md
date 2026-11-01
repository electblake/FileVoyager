<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellitem
retrieved: 2026-11-01T19:27:43.112267+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellitem
content_type: text/markdown
-->

---
layout: Conceptual
title: IShellItem (shobjidl_core.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellitem
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
UID: NN:shobjidl_core.IShellItem
description: Exposes methods that retrieve information about a Shell item. IShellItem and IShellItem2 are the preferred representations of items in any new code.
old-location: shell\IShellItem.htm
tech.root: shell
ms.assetid: 599b9c0a-df04-4dbd-a5a6-a8736eecc560
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: IShellItem, IShellItem interface [Windows Shell], IShellItem interface [Windows Shell],described, _win32_IShellItem, shell.IShellItem, shobjidl_core/IShellItem
req.header: shobjidl_core.h
req.include-header: Shobjidl.h
req.target-type: Windows
req.target-min-winverclnt: Windows XP with SP1 [desktop apps only]
req.target-min-winversvr: Windows Server 2003 [desktop apps only]
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: Shell32.dll (version 6.0 or later)
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
- Shell32.dll
api_name:
- IShellItem
locale: en-us
document_id: 827b4167-32b0-eb69-5400-ca3704f2a226
document_version_independent_id: 9262e8c6-39cf-11e0-0440-fca4fd38f69a
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/shobjidl_core/nn-shobjidl_core-ishellitem.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/shobjidl_core/nn-shobjidl_core-ishellitem.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_shell/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 145
asset_id: shobjidl_core/nn-shobjidl_core-ishellitem
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/shobjidl_core/nn-shobjidl_core-ishellitem.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 5616a771-bcf3-bb36-63e0-123685875879
---

# IShellItem (shobjidl_core.h) - Win32 apps | Microsoft Learn

Exposes methods that retrieve information about a Shell item. **IShellItem** and [IShellItem2](/en-us/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem2) are the preferred representations of items in any new code.

## Inheritance

The **IShellItem** interface inherits from the [IUnknown](/en-us/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IShellItem** also has these types of members:

- [Methods](/en-us/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellitem#methods)

## Methods

The **IShellItem** interface has these methods.

| - |
| --- |
| [IShellItem::BindToHandler](nf-shobjidl_core-ishellitem-bindtohandler)Binds to a handler for an item as specified by the handler ID value (BHID). |
| [IShellItem::Compare](nf-shobjidl_core-ishellitem-compare)Compares two IShellItem objects. |
| [IShellItem::GetAttributes](nf-shobjidl_core-ishellitem-getattributes)Gets a requested set of attributes of the IShellItem object. |
| [IShellItem::GetDisplayName](nf-shobjidl_core-ishellitem-getdisplayname)Gets the display name of the IShellItem object. |
| [IShellItem::GetParent](nf-shobjidl_core-ishellitem-getparent)Gets the parent of an IShellItem object. |

## Remarks

### When to Implement
 Third parties do not implement this interface; only use the implementation provided with the system. 
## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows XP with SP1 [desktop apps only] |
| **Minimum supported server** | Windows Server 2003 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | shobjidl\_core.h (include Shobjidl.h) |
