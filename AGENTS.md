# FileVoyager project instructions

## Performance is a primary requirement

- Build a responsive file explorer. Familiar Windows File Explorer behavior is the baseline, but rendering performance takes priority over exact visual fidelity, decorative effects, animations, and expensive presentation details.
- Prioritize fast folder navigation, smooth scrolling, responsive selection, and bounded memory use, especially for large image directories and thumbnail grids.
- Use model/view rendering and lightweight delegates. Avoid creating a widget for every file or thumbnail. Prefer predictable, uniform grid geometry over expensive per-item layout.
- Keep filesystem access, thumbnail acquisition, image decoding, and resizing out of paint callbacks and synchronous model data access. Schedule expensive work outside the UI thread; apply model and UI updates on their owning thread.
- Prioritize thumbnails for visible items, with a small bounded prefetch region. Bound queued work, worker concurrency, and image cache memory. Cancel obsolete work where supported and discard stale results after navigation or changes in requested thumbnail size.
- Load and retain images at sizes appropriate to their displayed thumbnails. Avoid retaining full-resolution originals for grid rendering or repeatedly decoding and scaling images during scrolling.
- Update only affected items and roles. Batch completed thumbnail updates when useful; avoid whole-view resets and repeated relayouts for individual image arrivals.
- Treat progressive thumbnail arrival as normal asynchronous loading, not a reason to block navigation or scrolling. Do not hide actual failures with fallback providers or silent substitutions.
- Choose rendering techniques using measurements on representative large folders: navigation latency, scrolling/frame time, UI responsiveness, thumbnail throughput, and peak memory. Cover cold and warm caches and rapid navigation. Do not claim performance based only on a small demo.
- Prefer the simplest implementation that meets measured performance needs. Add visual complexity only when its cost is justified and does not compromise core interactions.

## Fail-fast implementation policy

- Implement only the explicitly requested primary execution path.
- Never add error handling, `try`/`except`, recovery logic, fallback values, fallback providers, compatibility shims, silent substitution, or degraded modes.
- Never catch, suppress, translate, wrap, retry, or replace failures.
- Never add validation branches whose purpose is to produce a custom error path.
- Let missing files, invalid inputs, unavailable dependencies, unsupported environments, and runtime failures surface naturally from the operation that fails.
- If the primary path cannot be implemented as specified, stop and report the blocker instead of implementing an alternative path.
