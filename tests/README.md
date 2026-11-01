# Tests

Run from the repository root on Windows after installing the shared FFmpeg dependency with Setup:

```powershell
uv run python -m unittest discover -s tests --durations 10
```

The app and tests load the same FFmpeg DLLs from the platformdirs app-data directory. Missing DLLs fail naturally; there is no alternate media provider. Qt runs offscreen, so the suite does not take over the desktop.

The suite shares one QApplication and a Qt event-loop wait. Browser, similarity and Shell tests reuse class-scoped fixtures; only mutable settings and destructive installer lifecycle checks need separate scratch state. The event-loop wait lets worker threads progress instead of repeatedly calling `QTest.qWait`. Menu checks share a window lifecycle. Persistence checks read the actual INI file without launching another interpreter. The native installer-handoff test signals entry into each process-handle wait rather than spending two seconds in fixed timeouts.

Coverage includes:

- Navigation, folder watching, history, sorting, shared selection, window and folder persistence.
- Thumbnail scheduling bounds, stale results, failures, cache eviction, native bitmap ownership and GDI handle counts.
- Image feature contracts, DBSCAN comparison against scikit-learn, cancellation and media similarity UI.
- Real video decoding, paused seeking, play/pause, source release, and actual Windows DLL paths after decoding.
- Update HTTP streaming and the real Windows process-handle handoff, without executing Setup.
- Installer payload/runtime agreement, extraction, reinstall, launcher arguments, uninstall and preservation of preferences. Venv creation and pip alone are mocked in this filesystem lifecycle test.

On 2026-11-01, the original 54 tests took 34.289 seconds and 29.726 seconds on this machine. The revised 54 tests passed in 11.835 seconds; a final run concurrent with installer compilation passed in 15.655 seconds. This is approximately 47-60% faster than the faster baseline. These are unittest execution times, excluding interpreter startup/imports; they are not application performance benchmarks. Test cases were consolidated and installer/DLL checks added, so the equal counts do not mean identical cases. Full Setup execution was not performed.
