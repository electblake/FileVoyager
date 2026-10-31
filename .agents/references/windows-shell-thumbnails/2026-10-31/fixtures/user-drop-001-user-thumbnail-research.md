Windows system context

Use [**Windows Shell’s&#x20;**](https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellitemimagefactory-getimage?utm_source=chatgpt.com)[**`IShellItemImageFactory::GetImage`**](https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellitemimagefactory-getimage?utm_source=chatgpt.com). It retrieves images through the shared Windows thumbnail cache used by File Explorer. [Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/api/thumbcache/nn-thumbcache-ithumbnailcache)

For **existing thumbnails only**, combine these flags:
```ini
SIIGBF_THUMBNAILONLY = 0x00000008SIIGBF_INCACHEONLY = 0x00000010flags = SIIGBF_INCACHEONLY | SIIGBF_THUMBNAILONLY
```

| Setting                | Effect                                                             |
| ---------------------- | ------------------------------------------------------------------ |
| `SIIGBF_INCACHEONLY`   | Retrieve a cached result without extracting a new thumbnail.       |
| `SIIGBF_THUMBNAILONLY` | Require an actual thumbnail; prevent fallback to a file-type icon. |
| Both combined          | Return an existing thumbnail, or fail if one is unavailable.       |

Cache retrieval can still involve disk access. `SIIGBF_MEMORYONLY` is unsuitable because it only returns cached icons, not thumbnails. [Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellitemimagefactory-getimage?utm_source=chatgpt.com)

## Python solution

Use [**`comtypes`**](https://comtypes.readthedocs.io/en/stable/com_interfaces.html?utm_source=chatgpt.com) together with Python’s standard-library [**`ctypes`**](https://docs.python.org/3/library/ctypes.html?utm_source=chatgpt.com):

| Component  | Responsibility                                                                           |
| ---------- | ---------------------------------------------------------------------------------------- |
| `comtypes` | Declare the `IShellItemImageFactory` COM interface and call its `GetImage` method.       |
| `ctypes`   | Call Windows DLL functions for creating the Shell item and handling the returned bitmap. |

This requires a small Python wrapper containing the COM interface declaration and native function signatures. `comtypes` provides the COM binding machinery. [comtypes 1.4.17 documentation](https://comtypes.readthedocs.io/en/stable/com_interfaces.html?utm_source=chatgpt.com)

The wrapper’s flow is:

1. Call **`SHCreateItemFromParsingName`** with the file path to obtain an **`IShellItemImageFactory`** interface. [Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nf-shobjidl_core-shcreateitemfromparsingname?utm_source=chatgpt.com)
2. Call **`GetImage`** with the requested dimensions and the flags above.
3. Copy the returned **`HBITMAP`** pixels into a Python-owned image buffer for analysis.
4. Free the native bitmap with **`DeleteObject`** after copying its pixels. [Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellitemimagefactory-getimage?utm_source=chatgpt.com)