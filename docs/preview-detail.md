# Preview Detail

The movable, floatable Preview Detail dock opens above Media similarity in the
right dock area. Ctrl+Shift+P toggles it. It follows the current selected item in
both Details and Grid views; when the current item is not selected, it uses the
first selected row. Clearing selection or navigating clears the preview.

The thumbnail appears above a scrollable QFormLayout with selectable property
values. File properties include name, location, type, size, and timestamps.
Windows media properties include image dimensions and bit depth, video dimensions,
duration, frame rate, bitrates, date taken, camera details, title, and rating when
present. Non-media selections show file properties without a media thumbnail.

Video selections also show a small Play/Pause button and a seek slider below the
preview. Play or seek replaces the poster with inline video in the same area.
Seeking while paused displays the chosen frame without starting playback.
Dragging commits a seek on release; arrow keys seek by one second and page keys
by five seconds. The slider follows playback except while being dragged.
Hiding the dock pauses playback. Changing selection, clearing it, navigating,
or closing the window stops playback and releases the media source.

Thumbnail acquisition, scaling, filesystem reads, and Shell property access run
on one worker. Selection changes are debounced for 60 ms. There is at most one
active request and one pending selection; newer selections replace pending work.
Completed obsolete requests are discarded. Only the current preview pixmap is
retained, bounded to 192 logical pixels per side at the display's device ratio.
There is no full-resolution still-image decode or image cache in the dock. Native
thumbnail and metadata failures propagate unchanged.

One Qt QMediaPlayer and QVideoWidget handle video decoding and rendering without
Python per-frame image copies. Source loading uses the same 60 ms selection
debounce and never autoplays. Video decoding uses Qt's FFmpeg backend, with the installer's shared libraries
loaded from `platformdirs.user_data_path('FileVoyager', appauthor=False)` under
`tools/ffmpeg/ffmpeg-9.0.2-full_build-shared/bin`. It never searches PATH for an
FFmpeg executable. The shared-library ABI matches Qt 6.12. Decoding
can consume source-resolution frame buffers; the 192-pixel bound applies to
poster thumbnails, not the backend's video buffers.

Metadata uses the Windows
[ShellFolderItem.ExtendedProperty API](https://learn.microsoft.com/en-us/windows/win32/shell/shellfolderitem-extendedproperty).
An absent optional property is omitted from the form.

## Validation — 2026-11-01

- Native PNG properties: 640 × 480 dimensions and 24-bit depth verified.
- Integration tests cover right/top placement, selection, view switching,
  floating, reopening, clearing, failure propagation, and stale-result rejection.
- A burst of 1,000 selection changes while a request is active acquires only the
  first and final thumbnails; thumbnail work runs off the GUI thread.
- Native video tests use the three-second MPEG-4 fixture in
  `tests/fixtures/preview-video.mp4`. They verify decoded frames after paused
  seeking, play/pause, slider synchronization, drag-release seeking, pausing on
  hide, debounced video selection, and source release on selection/shutdown.
  The fixture was generated with FFmpeg's `testsrc2=size=96x64:rate=10`,
  `-t 3 -c:v mpeg4 -q:v 5`; the tests require the same installed FFmpeg libraries as the app.
- The existing 10,000-item synthetic UI benchmark with the new dock measured
  1,680.51 ms first navigation, 44.94 ms warm navigation, 28.17 ms p95 event-loop
  gap, 51.79 ms maximum scrolling event-loop gap, and 186.23 MiB peak working set.
  Outputs are in `.benchmarks/preview-detail-metrics.json` and related images.
  This benchmark uses synthetic thumbnails and no selected preview. It measures
  the surrounding browser, not native preview throughput or cold Shell-cache
  performance; first navigation does not mean a flushed OS cache.
