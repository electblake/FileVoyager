<!--
source: https://learn.microsoft.com/en-us/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance
retrieved: 2026-11-01T19:27:44.604752+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance
content_type: text/markdown
-->

---
layout: Conceptual
title: CoCreateInstance function (combaseapi.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance
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
UID: NF:combaseapi.CoCreateInstance
description: Creates a single uninitialized object of the class associated with a specified CLSID.
old-location: com\cocreateinstance.htm
tech.root: com
ms.assetid: 7295a55b-12c7-4ed0-a7a4-9ecee16afdec
ms.date: 2018-12-05T00:00:00.0000000Z
ms.keywords: CoCreateInstance, CoCreateInstance function [COM], _com_CoCreateInstance, com.cocreateinstance, combaseapi/CoCreateInstance
req.header: combaseapi.h
req.include-header: Objbase.h
req.target-type: Windows
req.target-min-winverclnt: Windows 2000 Professional [desktop apps only]
req.target-min-winversvr: Windows 2000 Server [desktop apps only]
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
ms.custom: snippet-project
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
- CoCreateInstance
locale: en-us
document_id: 32ef5183-c262-8bfe-f152-b645b97019c8
document_version_independent_id: d549c31a-e7d7-6e0a-65b2-51aef38a7cda
updated_at: 2025-07-01T18:41:00.0000000Z
original_content_git_url: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build?path=/sdk-api-src/content/combaseapi/nf-combaseapi-cocreateinstance.md&version=GBlive&_a=contents
gitcommit: https://cpubwin.visualstudio.com/DefaultCollection/win32/_git/sdk-api-build/commit/fa53641576e3603fa7b66d3a4ad969d3ce49d6f3?path=/sdk-api-src/content/combaseapi/nf-combaseapi-cocreateinstance.md&_a=contents
git_commit_id: fa53641576e3603fa7b66d3a4ad969d3ce49d6f3
site_name: Docs
depot_name: MSDN.sdk-api-build
page_type: conceptual
toc_rel: ../_com/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.sdk-api-build/{branchName}{pdfName}
search.mshattr.devlang: c++
word_count: 593
asset_id: combaseapi/nf-combaseapi-cocreateinstance
moniker_range_name: 
monikers: []
item_type: Content
source_path: sdk-api-src/content/combaseapi/nf-combaseapi-cocreateinstance.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 76e68c09-34a7-89be-2674-824f0e012b59
---

# CoCreateInstance function (combaseapi.h) - Win32 apps | Microsoft Learn

Creates and default-initializes a single object of the class associated with a specified CLSID.

Call **CoCreateInstance** when you want to create only one object on the local system. To create a single object on a remote system, call the [CoCreateInstanceEx](/en-us/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstanceex) function. To create multiple objects based on a single CLSID, call the [CoGetClassObject](/en-us/windows/desktop/api/combaseapi/nf-combaseapi-cogetclassobject) function.

## Syntax

```cpp
HRESULT CoCreateInstance(
  [in]  REFCLSID  rclsid,
  [in]  LPUNKNOWN pUnkOuter,
  [in]  DWORD     dwClsContext,
  [in]  REFIID    riid,
  [out] LPVOID    *ppv
);
```

## Parameters

`[in] rclsid`

The CLSID associated with the data and code that will be used to create the object.

`[in] pUnkOuter`

If **NULL**, indicates that the object is not being created as part of an aggregate. If non-**NULL**, pointer to the aggregate object's [IUnknown](/en-us/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface (the controlling **IUnknown**).

`[in] dwClsContext`

Context in which the code that manages the newly created object will run. The values are taken from the enumeration [CLSCTX](/en-us/windows/desktop/api/wtypesbase/ne-wtypesbase-clsctx).

`[in] riid`

A reference to the identifier of the interface to be used to communicate with the object.

`[out] ppv`

Address of pointer variable that receives the interface pointer requested in *riid*. Upon successful return, \**ppv* contains the requested interface pointer. Upon failure, \**ppv* contains **NULL**.

## Return value

This function can return the following values.

| Return code | Description |
| --- | --- |
| - **S\_OK** | An instance of the specified object class was successfully created. |
| - **REGDB\_E\_CLASSNOTREG** | A specified class is not registered in the registration database. Also can indicate that the type of server you requested in the [CLSCTX](/en-us/windows/desktop/api/wtypesbase/ne-wtypesbase-clsctx) enumeration is not registered or the values for the server types in the registry are corrupt. |
| - **CLASS\_E\_NOAGGREGATION** | This class cannot be created as part of an aggregate. |
| - **E\_NOINTERFACE** | The specified class does not implement the requested interface, or the controlling [IUnknown](/en-us/windows/desktop/api/unknwn/nn-unknwn-iunknown) does not expose the requested interface. |
| - **E\_POINTER** | The *ppv* parameter is **NULL**. |

## Remarks

The **CoCreateInstance** function provides a convenient shortcut by connecting to the class object associated with the specified CLSID, creating a default-initialized instance, and releasing the class object. As such, it encapsulates the following functionality:

```syntax
CoGetClassObject(rclsid, dwClsContext, NULL, IID_IClassFactory, &pCF); 
hresult = pCF->CreateInstance(pUnkOuter, riid, ppvObj);
pCF->Release(); 

```

It is convenient to use **CoCreateInstance** when you need to create only a single instance of an object on the local machine. If you are creating an instance on remote computer, call [CoCreateInstanceEx](/en-us/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstanceex). When you are creating multiple instances, it is more efficient to obtain a pointer to the class object's [IClassFactory](/en-us/windows/desktop/api/unknwnbase/nn-unknwnbase-iclassfactory) interface and use its methods as needed. In the latter case, you should use the [CoGetClassObject](/en-us/windows/desktop/api/combaseapi/nf-combaseapi-cogetclassobject) function.

In the [CLSCTX](/en-us/windows/desktop/api/wtypesbase/ne-wtypesbase-clsctx) enumeration, you can specify the type of server used to manage the object. The constants can be CLSCTX\_INPROC\_SERVER, CLSCTX\_INPROC\_HANDLER, CLSCTX\_LOCAL\_SERVER, CLSCTX\_REMOTE\_SERVER or any combination of these values. The constant CLSCTX\_ALL is defined as the combination of all four. For more information about the use of one or a combination of these constants, see [CLSCTX](/en-us/windows/desktop/api/wtypesbase/ne-wtypesbase-clsctx).

### UWP applications

Although there are no restrictions on which CLSIDs a UWP application can pass to **CoCreateInstance**, many objects will fail with **E\_ACCESSDENIED** for security reasons, especially if they do not run in-process. Additionally, even if you can successfully create an object, it might fail at a later time due to UWP security constraints, app-model differences, etc. In particular, background tasks should limit the objects they communicate with to avoid hangs or other complications due to connected stand-by.

## Examples

```cpp
// Create WIC factory
hr = CoCreateInstance(
    CLSID_WICImagingFactory,
    NULL,
    CLSCTX_INPROC_SERVER,
    IID_PPV_ARGS(&m_pIWICFactory)
    );
```

## Requirements

| Requirement | Value |
| --- | --- |
| **Minimum supported client** | Windows 2000 Professional [desktop apps only] |
| **Minimum supported server** | Windows 2000 Server [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | combaseapi.h (include Objbase.h) |
| **Library** | Ole32.lib |
| **DLL** | Ole32.dll |
