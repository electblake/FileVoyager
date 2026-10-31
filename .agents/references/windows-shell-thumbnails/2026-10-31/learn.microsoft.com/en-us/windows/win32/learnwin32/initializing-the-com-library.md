<!--
source: https://learn.microsoft.com/en-us/windows/win32/learnwin32/initializing-the-com-library
retrieved: 2026-10-31T21:17:04.958236+00:00
final_url: https://learn.microsoft.com/en-us/windows/win32/learnwin32/initializing-the-com-library
content_type: text/markdown
-->

---
layout: Conceptual
title: Initializing the COM Library - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/learnwin32/initializing-the-com-library
breadcrumb_path: /windows/desktop/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-WinDevCenter
recommendations: true
adobe-target: true
ms.service: windows-api-desktop-tech
ms.subservice: get-started
ms.author: jken
author: GrantMeStrength
feedback_system: Standard
feedback_product_url: https://www.microsoft.com/en-us/windowsinsider/feedbackhub/fb
feedback_help_link_url: https://learn.microsoft.com/answers/tags/224/windows-api-win32/
feedback_help_link_type: get-help-at-qna
description: Initializing the COM Library
ms.assetid: b044e146-8409-4f8d-87d3-52f21ebc2255
ms.topic: concept-article
ms.date: 2018-05-31T00:00:00.0000000Z
locale: en-us
document_id: 2c97623b-d9b6-3efe-10a8-86747e2d1173
document_version_independent_id: 562e0a46-f37b-ad84-16b9-541e24671b04
updated_at: 2025-03-13T17:42:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/win32-pr/blob/live/desktop-src/LearnWin32/initializing-the-com-library.md
gitcommit: https://github.com/MicrosoftDocs/win32-pr/blob/641bad19094f7ca28b1ddcc95c05d2f9e5f169f1/desktop-src/LearnWin32/initializing-the-com-library.md
git_commit_id: 641bad19094f7ca28b1ddcc95c05d2f9e5f169f1
site_name: Docs
depot_name: MSDN.win32
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.win32/{branchName}{pdfName}
word_count: 361
asset_id: learnwin32/initializing-the-com-library
moniker_range_name: 
monikers: []
item_type: Content
source_path: desktop-src/LearnWin32/initializing-the-com-library.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/caec7b7f-4941-4578-b79f-c63b1c1f5af4
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/754dea88-f800-4835-b6b5-280cb5d81e88
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: b7d4ccd9-cfd5-e044-542f-13a9c8cc2162
---

# Initializing the COM Library - Win32 apps | Microsoft Learn

Any Windows program that uses COM must initialize the COM library by calling the [**CoInitializeEx**](/en-us/windows/desktop/api/combaseapi/nf-combaseapi-coinitializeex) function. Each thread that uses a COM interface must make a separate call to this function. **CoInitializeEx** has the following signature:

```C
HRESULT CoInitializeEx(LPVOID pvReserved, DWORD dwCoInit);
```

The first parameter is reserved and must be **NULL**. The second parameter specifies the threading model that your program will use. COM supports two different threading models, *apartment threaded* and *multithreaded*. If you specify apartment threading, you are making the following guarantees:

- You will access each COM object from a single thread; you will not share COM interface pointers between multiple threads.
- The thread will have a message loop. (See [Window Messages](window-messages) in Module 1.)

If either of these constraints is not true, use the multithreaded model. To specify the threading model, set one of the following flags in the *dwCoInit* parameter.

| Flag | Description |
| --- | --- |
| **COINIT\_APARTMENTTHREADED** | Apartment threaded. |
| **COINIT\_MULTITHREADED** | Multithreaded. |

You must set exactly one of these flags. Generally, a thread that creates a window should use the **COINIT\_APARTMENTTHREADED** flag, and other threads should use **COINIT\_MULTITHREADED**. However, some COM components require a particular threading model.

Note

Actually, even if you specify apartment threading, it is still possible to share interfaces between threads, by using a technique called *marshaling*. Marshaling is beyond the scope of this module. The important point is that with apartment threading, you must never simply copy an interface pointer to another thread. For more information about the COM threading models, see [Processes, Threads, and Apartments](/en-us/windows/desktop/com/processes--threads--and-apartments).

In addition to the flags already mentioned, it is a good idea to set the **COINIT\_DISABLE\_OLE1DDE** flag in the *dwCoInit* parameter. Setting this flag avoids some overhead associated with Object Linking and Embedding (OLE) 1.0, an obsolete technology.

Here is how you would initialize COM for apartment threading:

```C
HRESULT hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED | COINIT_DISABLE_OLE1DDE);
```

The **HRESULT** return type contains an error or success code. We'll look at COM error handling in the next section.

## Uninitializing the COM Library

For every successful call to [**CoInitializeEx**](/en-us/windows/desktop/api/combaseapi/nf-combaseapi-coinitializeex), you must call [**CoUninitialize**](/en-us/windows/desktop/api/combaseapi/nf-combaseapi-couninitialize) before the thread exits. This function takes no parameters and has no return value.

```C
CoUninitialize();
```

## Next

[Error Codes in COM](error-codes-in-com)
