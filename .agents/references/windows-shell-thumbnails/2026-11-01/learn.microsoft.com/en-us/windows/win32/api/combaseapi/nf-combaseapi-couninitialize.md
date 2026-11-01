<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/combaseapi/nf-combaseapi-couninitialize
retrieved: 2026-11-01T19:27:44.240089+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/combaseapi/nf-combaseapi-couninitialize
content_type: text/markdown
-->

---
layout: Conceptual
title: CoUninitialize function (combaseapi.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/combaseapi/nf-combaseapi-couninitialize
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
UID: NF:combaseapi.CoUninitialize
description: Closes the COM library on the current thread, unloads all DLLs loaded by the thread, frees any other resources that the thread maintains, and forces all RPC connections on the thread to close.
old-location: com\couninitialize.htm
tech.root: com
ms.assetid: 9411cbed-fa3b-46f7-b677-6ada53324edc
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: CoUninitialize, CoUninitialize function [COM], _com_CoUninitialize, com.couninitialize, combaseapi/CoUninitialize
req.header: combaseapi.h
req.include-header: Objbase.h
req.target-type: Windows
req.target-min-winverclnt: Windows 2000 Professional [desktop apps \| UWP apps]
req.target-min-winversvr: Windows 2000 Server [desktop apps \| UWP apps]
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ole32.lib
req.dll: Ole32.dll
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
- api-ms-win-core-com-l1-1-3.dll
- api-ms-win-core-com-l1-1-2.dll
- Ole32.dll
- API-MS-Win-Core-Com-l1-1-0.dll
- ComBase.dll
- API-MS-Win-Core-Com-l1-1-1.dll
- API-MS-Win-DownLevel-Ole32-l1-1-0.dll
- API-MS-Win-DownLevel-Ole32-l1-1-1.dll
api_name:
- CoUninitialize
locale: en-us
document_id: 3e2103c3-bbbc-d0bb-1a8a-4c8e00158497
document_version_independent_id: 49fb441d-a22a-6976-3e4e-3066006deb4a
updated_at: 2025-07-01T18:41:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/combaseapi/nf-combaseapi-couninitialize.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/fa53641576e3603fa7b66d3a4ad969d3ce49d6f3?path=/sdk-api-src/content/combaseapi/nf-combaseapi-couninitialize.md&_a=contents
git_commit_id: fa53641576e3603fa7b66d3a4ad969d3ce49d6f3
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_com/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 257
asset_id: combaseapi/nf-combaseapi-couninitialize
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/combaseapi/nf-combaseapi-couninitialize.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 1ff2407b-b7cd-8c73-fd32-15e87200516b
---

# CoUninitialize function (combaseapi.h) - Win32 apps | Microsoft Learn

Closes the COM library on the current thread, unloads all DLLs loaded by the thread, frees any other resources that the thread maintains, and forces all RPC connections on the thread to close.

## Syntax

```cpp
void CoUninitialize();
```

## Return value

None

## Remarks

A thread must call **CoUninitialize** once for each successful call it has made to the [CoInitialize](/en-us/windows/desktop/api/objbase/nf-objbase-coinitialize) or [CoInitializeEx](/en-us/windows/desktop/api/combaseapi/nf-combaseapi-coinitializeex) function, including any call that returns S\_FALSE. Only the **CoUninitialize** call corresponding to the **CoInitialize** or **CoInitializeEx** call that initialized the library can close it.

Calls to [OleInitialize](/en-us/windows/desktop/api/ole2/nf-ole2-oleinitialize) must be balanced by calls to [OleUninitialize](/en-us/windows/desktop/api/ole2/nf-ole2-oleuninitialize). The **OleUninitialize** function calls **CoUninitialize** internally, so applications that call **OleUninitialize** do not also need to call **CoUninitialize**.

**CoUninitialize** should be called on application shutdown, as the last call made to the COM library after the application hides its main windows and falls through its main message loop. If there are open conversations remaining, **CoUninitialize** starts a modal message loop and dispatches any pending messages from the containers or server for this COM application. By dispatching the messages, **CoUninitialize** ensures that the application does not quit before receiving all of its pending messages. Non-COM messages are discarded.

Because there is no way to control the order in which in-process servers are loaded or unloaded, do not call [CoInitialize](/en-us/windows/desktop/api/objbase/nf-objbase-coinitialize), [CoInitializeEx](/en-us/windows/desktop/api/combaseapi/nf-combaseapi-coinitializeex), or **CoUninitialize** from the [DllMain](/en-us/windows/desktop/Dlls/dllmain) function.

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows 2000 Professional [desktop apps | UWP apps] |
| **Minimum supported server** | Windows 2000 Server [desktop apps | UWP apps] |
| **Target Platform** | Windows |
| **Header** | combaseapi.h (include Objbase.h) |
| **Library** | Ole32.lib |
| **DLL** | Ole32.dll |
