<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/unknwn/nf-unknwn-iunknown-release
retrieved: 2026-11-01T19:27:45.096766+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/unknwn/nf-unknwn-iunknown-release
content_type: text/markdown
-->

---
layout: Conceptual
title: IUnknown::Release - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/unknwn/nf-unknwn-iunknown-release
adobe-target: true
breadcrumb_path: /windows/desktop/api/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-WinDevCenter
ms.service: windows-api-desktop-tech
ms.subservice: sdk-api-reference
ms.topic: reference
ms.author: stwhi
author: stevewhims
feedback_system: Standard
feedback_product_url: https://www.microsoft.com/en-us/windowsinsider/feedbackhub/fb
feedback_help_link_url: https://learn.microsoft.com/answers/tags/224/windows-api-win32/
feedback_help_link_type: get-help-at-qna
UID: NF:unknwn.IUnknown.Release
description: Decrements the reference count for an interface on a COM object.
old-location: com\iunknown_release.htm
tech.root: com
ms.assetid: 4b494c6f-f0ee-4c35-ae45-ed956f40dc7a
ms.date: 2019-05-31T00:00:00.0000000Z
ms.keywords: IUnknown interface [COM],Release method, IUnknown.Release, IUnknown::Release, Release, Release method [COM], Release method [COM],IUnknown interface, _com_iunknown_release, com.iunknown_release, unknwn/IUnknown::Release
req.header: unknwn.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 2000 Professional [desktop apps only]
req.target-min-winversvr: Windows 2000 Server [desktop apps only]
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: Unknwn.idl
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
- DllExport
api_location:
- Unknwn.h
api_name:
- IUnknown.Release
locale: en-us
document_id: 3bf28226-050b-1bca-3311-66fa20af2647
document_version_independent_id: bb611fce-e4b7-2ebb-ac78-d3921654baa6
updated_at: 2024-02-22T19:54:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/unknwn/nf-unknwn-iunknown-release.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/9267262487657894a8af112d7165006fed5035a7?path=/sdk-api-src/content/unknwn/nf-unknwn-iunknown-release.md&_a=contents
git_commit_id: 9267262487657894a8af112d7165006fed5035a7
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_com/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 164
asset_id: unknwn/nf-unknwn-iunknown-release
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/unknwn/nf-unknwn-iunknown-release.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: b72ab186-8bc0-d8e9-b019-203f8fb24802
---

# IUnknown::Release - Win32 apps | Microsoft Learn

Decrements the reference count for an interface on a COM object.

## Syntax

```cpp
ULONG Release();
```

## Return value

The method returns the new reference count. This value is intended to be used only for test purposes.

## Remarks

When the reference count on an object reaches zero, **Release** must cause the interface pointer to free itself. When the released pointer is the only (formerly) outstanding reference to an object (whether the object supports single or multiple interfaces), the implementation must free the object.

Note that aggregation of objects restricts the ability to recover interface pointers.

### Notes to callers

Call this method when you no longer need to use an interface pointer. If you are writing a method that takes an in-out parameter, call **Release** on the pointer you are passing in before copying the out-value on top of it.

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows 2000 Professional [desktop apps only] |
| **Minimum supported server** | Windows 2000 Server [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | unknwn.h |
