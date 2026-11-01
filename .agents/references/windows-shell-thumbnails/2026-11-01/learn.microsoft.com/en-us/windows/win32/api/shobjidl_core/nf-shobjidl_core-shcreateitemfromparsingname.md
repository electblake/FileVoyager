<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nf-shobjidl_core-shcreateitemfromparsingname
retrieved: 2026-11-01T19:27:43.429216+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nf-shobjidl_core-shcreateitemfromparsingname
content_type: text/markdown
-->

---
layout: Conceptual
title: SHCreateItemFromParsingName function (shobjidl_core.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nf-shobjidl_core-shcreateitemfromparsingname
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
UID: NF:shobjidl_core.SHCreateItemFromParsingName
description: Creates and initializes a Shell item object from a parsing name.
old-location: shell\SHCreateItemFromParsingName.htm
tech.root: shell
ms.assetid: 81e48318-b6a4-4b1a-8b78-21c00b9dc485
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: SHCreateItemFromParsingName, SHCreateItemFromParsingName function [Windows Shell], _shell_SHCreateItemFromParsingName, shell.SHCreateItemFromParsingName, shobjidl_core/SHCreateItemFromParsingName
req.header: shobjidl_core.h
req.include-header: Shobjidl.h
req.target-type: Windows
req.target-min-winverclnt: Windows Vista [desktop apps only]
req.target-min-winversvr: Windows Server 2008 [desktop apps only]
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: OneCore.Lib
req.dll: Shell32.dll
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
- ext-ms-win-shell-shell32-l1-2-3.dll
- api-ms-win-shell-namespace-l1-1-1.dll
- Shell32.dll
- API-MS-Win-Shell-Namespace-L1-1-0.dll
- Ext-MS-Win-shell-shell32-L1-2-0.dll
- Ext-MS-Win-Shell-Shell32-L1-2-1.dll
- Ext-MS-Win-Shell-Shell32-L1-2-2.dll
- Windows.Storage.Dll
api_name:
- SHCreateItemFromParsingName
locale: en-us
document_id: b45c9058-6c1c-834a-45c1-2e62e3e7b9fd
document_version_independent_id: 7cb97b2a-26af-6ce1-8a50-ed72f9515c20
updated_at: 2025-10-31T21:10:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/shobjidl_core/nf-shobjidl_core-shcreateitemfromparsingname.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/540c1f2da94f9934d5d7e4321d4270e02fe917ec?path=/sdk-api-src/content/shobjidl_core/nf-shobjidl_core-shcreateitemfromparsingname.md&_a=contents
git_commit_id: 540c1f2da94f9934d5d7e4321d4270e02fe917ec
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_shell/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 319
asset_id: shobjidl_core/nf-shobjidl_core-shcreateitemfromparsingname
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/shobjidl_core/nf-shobjidl_core-shcreateitemfromparsingname.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: db95d179-b86e-f37a-7060-b8a5a5bfb8d6
---

# SHCreateItemFromParsingName function (shobjidl_core.h) - Win32 apps | Microsoft Learn

Creates and initializes a Shell item object from a parsing name.

## Syntax

```cpp
SHSTDAPI SHCreateItemFromParsingName(
  [in]           PCWSTR   pszPath,
  [in, optional] IBindCtx *pbc,
  [in]           REFIID   riid,
  [out]          void     **ppv
);
```

## Parameters

`[in] pszPath`

Type: **PCWSTR**

A pointer to a display name.

`[in, optional] pbc`

Type: **[IBindCtx](/en-us/windows/desktop/api/objidl/nn-objidl-ibindctx)\***

Optional. A pointer to a bind context used to pass parameters as inputs and outputs to the parsing function. These passed parameters are often specific to the data source and are documented by the data source owners. For example, the file system data source accepts the name being parsed (as a [WIN32_FIND_DATA](/en-us/windows/desktop/api/minwinbase/ns-minwinbase-win32_find_dataa) structure), using the [STR_FILE_SYS_BIND_DATA](/en-us/windows/desktop/shell/str-constants) bind context parameter.

[STR_PARSE_PREFER_FOLDER_BROWSING](/en-us/windows/desktop/shell/str-constants) can be passed to indicate that URLs are parsed using the file system data source when possible. Construct a bind context object using [CreateBindCtx](/en-us/windows/desktop/api/objbase/nf-objbase-createbindctx) and populate the values using [IBindCtx::RegisterObjectParam](/en-us/windows/desktop/api/objidl/nf-objidl-ibindctx-registerobjectparam). See **Bind Context String Keys** for a complete list of these. See the [Parsing With Parameters Sample](/en-us/previous-versions/windows/desktop/legacy/dd940368%28v=vs.85%29) for an example of the use of this parameter.

If no data is being passed to or received from the parsing function, this value can be **NULL**.

`[in] riid`

Type: **REFIID**

A reference to the IID of the interface to retrieve through *ppv*, typically **IID\_IShellItem** or **IID\_IShellItem2**.

`[out] ppv`

Type: **void\*\***

When this method returns successfully, contains the interface pointer requested in *riid*. This is typically [IShellItem](/en-us/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem) or [IShellItem2](/en-us/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem2).

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

We recommend that you use the **IID\_PPV\_ARGS** macro, defined in Objbase.h, to package the *riid* and *ppv* parameters. This macro provides the correct **IID** based on the interface pointed to by the value in *ppv*, which eliminates the possibility of a coding error in *riid* that could lead to unexpected results.

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows Vista [desktop apps only] |
| **Minimum supported server** | Windows Server 2008 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | shobjidl\_core.h (include Shobjidl.h) |
| **Library** | OneCore.Lib |
| **DLL** | Shell32.dll |
