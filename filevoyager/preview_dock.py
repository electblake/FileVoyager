"""Single-selection preview with bounded, latest-selection-only background work."""

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

from filevoyager import media_runtime

from comtypes import CoInitializeEx, CoUninitialize, COINIT_MULTITHREADED
from comtypes.client import CreateObject
from PySide6.QtCore import QSignalBlocker, QTimer, Qt, QUrl
from PySide6.QtGui import QPixmap
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (
    QDockWidget, QFormLayout, QHBoxLayout, QLabel, QScrollArea, QSlider,
    QStackedWidget, QStyle, QToolButton, QVBoxLayout, QWidget,
)

from filevoyager.models import MEDIA_SUFFIXES


VIDEO_SUFFIXES = frozenset({
    ".mp4", ".m4v", ".mkv", ".webm", ".mov", ".avi", ".wmv",
    ".mpg", ".mpeg", ".ts", ".mts", ".m2ts",
})


def load_properties(path):
    file = Path(path)
    info = file.stat()
    rows = [
        ("Name", file.name), ("Location", str(file.parent)),
        ("Type", "Folder" if file.is_dir() else file.suffix.upper().lstrip(".")),
        ("Size", f"{info.st_size:,} bytes"),
        ("Modified", str(datetime.fromtimestamp(info.st_mtime).replace(microsecond=0))),
        ("Created", str(datetime.fromtimestamp(info.st_birthtime).replace(microsecond=0))),
    ]
    if file.suffix.lower() in MEDIA_SUFFIXES and file.is_file():
        CoInitializeEx(COINIT_MULTITHREADED)
        shell = CreateObject("Shell.Application", dynamic=True)
        folder = shell.NameSpace(str(file.parent))
        item = folder.ParseName(file.name)
        for label, name in (
            ("Width", "System.Image.HorizontalSize"),
            ("Height", "System.Image.VerticalSize"),
            ("Bit depth", "System.Image.BitDepth"),
            ("Frame width", "System.Video.FrameWidth"),
            ("Frame height", "System.Video.FrameHeight"),
            ("Duration", "System.Media.Duration"),
            ("Frame rate", "System.Video.FrameRate"),
            ("Total bitrate", "System.Video.TotalBitrate"),
            ("Audio bitrate", "System.Audio.EncodingBitrate"),
            ("Date taken", "System.Photo.DateTaken"),
            ("Camera maker", "System.Photo.CameraManufacturer"),
            ("Camera model", "System.Photo.CameraModel"),
            ("Title", "System.Title"),
            ("Rating", "System.Rating"),
        ):
            value = item.ExtendedProperty(name)
            # Missing optional metadata is a normal property-store result.
            if value is None or value == "":
                continue
            if name == "System.Media.Duration":
                seconds = int(value) // 10_000_000
                value = f"{seconds // 3600}:{seconds // 60 % 60:02}:{seconds % 60:02}"
            elif name == "System.Video.FrameRate":
                value = f"{value / 1000:g} fps"
            elif name in ("System.Video.TotalBitrate", "System.Audio.EncodingBitrate"):
                value = f"{value / 1000:g} kbps"
            rows.append((label, str(value)))
        del item, folder, shell
        CoUninitialize()
    return rows


class PreviewDock(QDockWidget):
    def __init__(self, load_thumbnail, parent=None):
        super().__init__("Preview Detail", parent)
        self.setObjectName("previewDetailDock")
        self.load_thumbnail = load_thumbnail
        self.path = ""
        self.generation = 0
        self.pending = None
        self.future = None
        self.executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="preview")
        self.timer = QTimer(self)
        self.timer.setInterval(16)
        self.timer.timeout.connect(self.poll)
        self.debounce = QTimer(self)
        self.debounce.setSingleShot(True)
        self.debounce.setInterval(60)
        self.debounce.timeout.connect(self.dispatch)
        body = QWidget()
        layout = QVBoxLayout(body)
        self.preview = QLabel("Select an item to preview.")
        self.preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.preview.setFixedHeight(192)
        self.preview.setMinimumWidth(192)
        self.video = QVideoWidget()
        self.video.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
        self.display = QStackedWidget()
        self.display.setFixedHeight(192)
        self.display.addWidget(self.preview)
        self.display.addWidget(self.video)
        layout.addWidget(self.display)
        self.player = QMediaPlayer(self)
        self.audio = QAudioOutput(self)
        self.player.setAudioOutput(self.audio)
        self.player.setVideoOutput(self.video)
        self.controls = QWidget()
        controls_layout = QHBoxLayout(self.controls)
        controls_layout.setContentsMargins(0, 0, 0, 0)
        self.play_button = QToolButton()
        self.play_button.clicked.connect(self.toggle_playback)
        controls_layout.addWidget(self.play_button)
        self.seek_slider = QSlider(Qt.Orientation.Horizontal)
        self.seek_slider.setAccessibleName("Video position")
        self.seek_slider.setToolTip("Seek video")
        self.seek_slider.setTracking(False)
        self.seek_slider.setRange(0, 0)
        self.seek_slider.setSingleStep(1000)
        self.seek_slider.setPageStep(5000)
        self.seek_slider.valueChanged.connect(self.seek)
        controls_layout.addWidget(self.seek_slider, 1)
        layout.addWidget(self.controls)
        self.controls.hide()
        self.play_button.setEnabled(False)
        self.seek_slider.setEnabled(False)
        self.player.durationChanged.connect(self.update_duration)
        self.player.positionChanged.connect(self.update_position)
        self.player.seekableChanged.connect(self.seek_slider.setEnabled)
        self.player.playbackStateChanged.connect(self.update_play_button)
        self.player.mediaStatusChanged.connect(self.update_media_status)
        self.visibilityChanged.connect(self.pause_when_hidden)
        self.update_play_button(self.player.playbackState())
        self.form = QFormLayout()
        self.form.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapLongRows)
        layout.addLayout(self.form)
        layout.addStretch()
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(body)
        self.setWidget(scroll)

    def set_item(self, path, media=False):
        if path == self.path:
            return
        self.path = path
        self.generation += 1
        self.pending = None
        self.debounce.stop()
        self.player.stop()
        self.player.setSource(QUrl())
        self.display.setCurrentWidget(self.preview)
        self.controls.setVisible(media and Path(path).suffix.lower() in VIDEO_SUFFIXES)
        self.play_button.setEnabled(False)
        self.seek_slider.setEnabled(False)
        self.update_duration(0)
        self.preview.setText("Loading…" if path else "Select an item to preview.")
        while self.form.rowCount():
            self.form.removeRow(0)
        if path:
            ratio = self.devicePixelRatioF()
            self.pending = (self.generation, path, media, ratio)
            self.debounce.start()

    def load(self, request):
        _, path, media, ratio = request
        image = None
        if media:
            pixels = round(192 * ratio)
            image = self.load_thumbnail(path, pixels, pixels)
            image = image.scaled(pixels, pixels, Qt.AspectRatioMode.KeepAspectRatio,
                                 Qt.TransformationMode.SmoothTransformation)
        return image, load_properties(path)

    def dispatch(self):
        if self.pending is not None:
            _, path, media, _ = self.pending
            if media and Path(path).suffix.lower() in VIDEO_SUFFIXES:
                source = QUrl.fromLocalFile(path)
                if self.player.source() != source:
                    self.player.setSource(source)
        if self.future is None and self.pending is not None:
            self.request = self.pending
            self.pending = None
            self.future = self.executor.submit(self.load, self.request)
            self.timer.start()

    def update_duration(self, duration):
        with QSignalBlocker(self.seek_slider):
            self.seek_slider.setRange(0, duration)

    def update_position(self, position):
        if not self.seek_slider.isSliderDown():
            with QSignalBlocker(self.seek_slider):
                self.seek_slider.setValue(position)

    def update_media_status(self, status):
        self.play_button.setEnabled(status in (
            QMediaPlayer.MediaStatus.LoadedMedia, QMediaPlayer.MediaStatus.BufferingMedia,
            QMediaPlayer.MediaStatus.BufferedMedia, QMediaPlayer.MediaStatus.EndOfMedia,
        ))

    def update_play_button(self, state):
        playing = state == QMediaPlayer.PlaybackState.PlayingState
        icon = QStyle.StandardPixmap.SP_MediaPause if playing else QStyle.StandardPixmap.SP_MediaPlay
        self.play_button.setIcon(self.style().standardIcon(icon))
        self.play_button.setToolTip("Pause" if playing else "Play")
        self.play_button.setAccessibleName("Pause video" if playing else "Play video")

    def toggle_playback(self):
        self.display.setCurrentWidget(self.video)
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    def seek(self, position):
        self.display.setCurrentWidget(self.video)
        if self.player.playbackState() == QMediaPlayer.PlaybackState.StoppedState:
            self.player.pause()
        self.player.setPosition(position)

    def pause_when_hidden(self, visible):
        if not visible and self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()

    def poll(self):
        if self.future is None or not self.future.done():
            return
        future = self.future
        self.future = None
        self.timer.stop()
        image, rows = future.result()
        generation, _, _, ratio = self.request
        if generation == self.generation:
            self.preview.setText("No media preview" if image is None else "")
            if image is not None:
                pixmap = QPixmap.fromImage(image)
                pixmap.setDevicePixelRatio(ratio)
                self.preview.setPixmap(pixmap)
            for name, value in rows:
                label = QLabel(value)
                label.setTextFormat(Qt.TextFormat.PlainText)
                label.setWordWrap(True)
                label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
                self.form.addRow(name, label)
        if not self.debounce.isActive():
            self.dispatch()

    def shutdown(self):
        self.player.stop()
        self.player.setSource(QUrl())
        self.debounce.stop()
        self.timer.stop()
        self.pending = None
        self.executor.shutdown(wait=True, cancel_futures=False)
        if self.future is not None:
            self.future.result()
            self.future = None
