<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex
retrieved: 2026-11-01T19:27:43.905653+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex
content_type: text/markdown
-->

---
layout: Conceptual
title: CoInitializeEx function (combaseapi.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex
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
UID: NF:combaseapi.CoInitializeEx
description: Initializes the COM library for use by the calling thread, sets the thread's concurrency model, and creates a new apartment for the thread if one is required.
old-location: com\coinitializeex.htm
tech.root: com
ms.assetid: ffb79c0f-aeda-4ea1-aea8-afb79109837f
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: CoInitializeEx, CoInitializeEx function [COM], _com_CoInitializeEx, com.coinitializeex, combaseapi/CoInitializeEx
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
- CoInitializeEx
locale: en-us
document_id: d69df099-ae80-6995-faa9-ac70c0eed32c
document_version_independent_id: 3b512053-25cf-d838-74e6-554fa1428d11
updated_at: 2025-07-01T18:41:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/combaseapi/nf-combaseapi-coinitializeex.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/fa53641576e3603fa7b66d3a4ad969d3ce49d6f3?path=/sdk-api-src/content/combaseapi/nf-combaseapi-coinitializeex.md&_a=contents
git_commit_id: fa53641576e3603fa7b66d3a4ad969d3ce49d6f3
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_com/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 612
asset_id: combaseapi/nf-combaseapi-coinitializeex
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/combaseapi/nf-combaseapi-coinitializeex.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
platformId: 0c20924e-c2b2-8eb5-c899-edb4b8439d1c
---

# CoInitializeEx function (combaseapi.h) - Win32 apps | Microsoft Learn

Initializes the COM library for use by the calling thread, sets the thread's concurrency model, and creates a new apartment for the thread if one is required.

You should call Windows::Foundation::Initialize to initialize the thread instead of **CoInitializeEx** if you want to use the Windows Runtime APIs or if you want to use both COM and Windows Runtime components. Windows::Foundation::Initialize is sufficient to use for COM components.

## Syntax

```cpp
HRESULT CoInitializeEx(
  [in, optional] LPVOID pvReserved,
  [in]           DWORD  dwCoInit
);
```

## Parameters

`[in, optional] pvReserved`

This parameter is reserved and must be **NULL**.

`[in] dwCoInit`

The concurrency model and initialization options for the thread. Values for this parameter are taken from the [COINIT](/en-us/windows/desktop/api/objbase/ne-objbase-coinit) enumeration. Any combination of values from **COINIT** can be used, except that the COINIT\_APARTMENTTHREADED and COINIT\_MULTITHREADED flags cannot both be set. The default is COINIT\_MULTITHREADED.

## Return value

This function can return the standard return values E\_INVALIDARG, E\_OUTOFMEMORY, and E\_UNEXPECTED, as well as the following values.

| Return code | Description |
| --- | --- |
| - **S\_OK** | The COM library was initialized successfully on this thread. |
| - **S\_FALSE** | The COM library is already initialized on this thread. |
| - **RPC\_E\_CHANGED\_MODE** | A previous call to [CoInitializeEx](/en-us/windows/desktop/api/combaseapi/nf-combaseapi-coinitializeex) specified an incompatible concurrency model for this thread. This could also indicate that a change from neutral-threaded apartment to single-threaded apartment has occurred. |

## Remarks

**CoInitializeEx** must be called at least once, and is usually called only once, for each thread that uses the COM library. Multiple calls to **CoInitializeEx** by the same thread are allowed as long as they pass the same concurrency flag, but subsequent valid calls return S\_FALSE. If the concurrency flag does not match, then the call fails and returns RPC\_E\_CHANGED\_MODE. (For the purpose of this rule, a call to [CoInitialize](/en-us/windows/desktop/api/objbase/nf-objbase-coinitialize) is equivalent to calling **CoInitializeEx** with the COINIT\_APARTMENTTHREADED flag.) To uninitialize the COM library gracefully on a thread, each successful call to [CoInitialize](/en-us/windows/desktop/api/objbase/nf-objbase-coinitialize) or **CoInitializeEx**, including any call that returns S\_FALSE, must be balanced by a corresponding call to [CoUninitialize](/en-us/windows/desktop/api/combaseapi/nf-combaseapi-couninitialize). Once COM has been uninitialized on a thread, you can reinitialize it in any mode, subject to the constraints above.

You need to initialize the COM library on a thread before you call any of the library functions except [CoGetMalloc](/en-us/windows/desktop/api/combaseapi/nf-combaseapi-cogetmalloc), to get a pointer to the standard allocator, and the memory allocation functions. Otherwise, the COM function will return CO\_E\_NOTINITIALIZED.

Objects created in a single-threaded apartment (STA) receive method calls only from their apartment's thread, so calls are serialized and arrive only at message-queue boundaries (when the [PeekMessage](/en-us/windows/desktop/api/winuser/nf-winuser-peekmessagea) or [SendMessage](/en-us/previous-versions/windows/desktop/oe/oe-ihttpmailtransport-sendmessage) function is called).

Objects created on a COM thread in a multithread apartment (MTA) must be able to receive method calls from other threads at any time. You would typically implement some form of concurrency control in a multithreaded object's code using synchronization primitives such as critical sections, semaphores, or mutexes to help protect the object's data.

When an object that is configured to run in the neutral threaded apartment (NTA) is called by a thread that is in either an STA or the MTA, that thread transfers to the NTA. If this thread subsequently calls **CoInitializeEx**, the call fails and returns RPC\_E\_CHANGED\_MODE.

Because OLE technologies are not thread-safe, the [OleInitialize](/en-us/windows/desktop/api/ole2/nf-ole2-oleinitialize) function calls **CoInitializeEx** with the COINIT\_APARTMENTTHREADED flag. As a result, an apartment that is initialized for multithreaded object concurrency cannot use the features enabled by **OleInitialize**.

Because there is no way to control the order in which in-process servers are loaded or unloaded, do not call [CoInitialize](/en-us/windows/desktop/api/objbase/nf-objbase-coinitialize), **CoInitializeEx**, or [CoUninitialize](/en-us/windows/desktop/api/combaseapi/nf-combaseapi-couninitialize) from the [DllMain](/en-us/windows/desktop/Dlls/dllmain) function.

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows 2000 Professional [desktop apps | UWP apps] |
| **Minimum supported server** | Windows 2000 Server [desktop apps | UWP apps] |
| **Target Platform** | Windows |
| **Header** | combaseapi.h (include Objbase.h) |
| **Library** | Ole32.lib |
| **DLL** | Ole32.dll |
