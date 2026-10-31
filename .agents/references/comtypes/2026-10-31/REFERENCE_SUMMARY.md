# Reference Summary

Reference date: 2026-10-31.

## Package suitability

`comtypes` supplies Python bindings for custom Windows COM interfaces using ctypes. It is suitable for declaring and calling `IShellItemImageFactory` in the project's proposed thumbnail wrapper. It does not itself supply the complete Shell thumbnail-loading and bitmap-copying workflow; that remains project code built on Windows APIs.

The official repository describes a pure-Python package requiring Windows and Python 3.9 or later, with no additional mandatory dependencies. The project's previously reviewed Python 3.12 configuration meets that stated Python requirement. This is documentation compatibility, not a tested installation.

Source: [official repository](https://github.com/enthought/comtypes), [package metadata](https://github.com/enthought/comtypes/blob/main/pyproject.toml).

## Relevant binding behavior

- Declare the custom interface as an `IUnknown` subclass with `_iid_` and `_methods_`; describe `GetImage` using `COMMETHOD` and native ctypes argument types.
- Methods with out parameters return those values to Python rather than returning the success HRESULT. Failed HRESULT calls raise `COMError`; allow that failure to propagate under the project's fail-fast policy.
- comtypes manages interface reference counts. Avoid adding an extra manual `Release` that can cause double release.
- Generated type-library modules are a separate comtypes feature; their cache is not the Windows thumbnail cache.

Sources: [interface definitions](https://comtypes.readthedocs.io/en/stable/com_interfaces.html), [client behavior](https://comtypes.readthedocs.io/en/stable/client.html).

## FileVoyager integration decision

Use comtypes as the COM binding dependency, alongside standard-library ctypes for native Shell/GDI calls. Retain the existing reviewed path: create the Shell item, request `GetImage` with `SIIGBF_INCACHEONLY | SIIGBF_THUMBNAILONLY` (`0x18`), copy bitmap pixels into owned storage, then release the native bitmap. Do not add another thumbnail provider, generation step, retry, or icon substitution.

The cache flags and bitmap ownership requirements are grounded in the separate [Windows Shell reference bundle](../../windows-shell-thumbnails/2026-10-31/REFERENCE_SUMMARY.md). Choosing comtypes does not change those requirements or eliminate the need for per-thread COM initialization.

## Version and capture limits

The captured repository uses the moving `main` branch; the documentation uses `/stable/`. The captured pyproject declares its version dynamically from `comtypes.__version__`, rather than specifying a literal release number. These captures do not establish an exact release version. The earlier research's `1.4.17` label remains unverified; no dependency pin or claim of the latest release is made here.

The repository documents that 1.4.12 was the last release supporting Python 3.8 and that Python 3.13 requires comtypes 1.4.8 or later. These historical constraints do not block the project's Python 3.12 target.

The mirror checked both source domains for `/llms.txt`. GitHub's file was captured along with its linked GitHub MCP server page, as required by the mirror workflow; those discovery artifacts are unrelated to thumbnail integration. The comtypes documentation domain returned HTTP 404 for `/llms.txt`; both requested documentation pages were captured successfully.

No installation, import, cache hit/miss, pixel-copy, or resource-lifetime test was performed. User input is preserved separately as a fixture and is not runtime evidence.
