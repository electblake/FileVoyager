"""Explicitly started, single-job media thumbnail analysis in a movable Qt dock."""

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from threading import Event

from PySide6.QtCore import QTimer, Signal
from PySide6.QtWidgets import (
    QDockWidget, QDoubleSpinBox, QFormLayout, QGroupBox, QLabel, QProgressBar,
    QPushButton, QScrollArea, QSpinBox, QVBoxLayout, QWidget,
)

from filevoyager.similarity_jobs import (
    AnalysisProgress, AnalysisSettings, analyze_folder,
)
from filevoyager.models import MEDIA_SUFFIXES


class SimilarityDock(QDockWidget):
    orderReady = Signal(object)
    clearRequested = Signal()

    def __init__(self, load_thumbnail, parent=None):
        super().__init__("Media similarity", parent)
        self.load_thumbnail = load_thumbnail
        self.setObjectName("imageSimilarityDock")
        self.folder = ""
        self.reference = None
        self.future = None
        self.cancel_event = Event()
        self.executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="similarity")
        self.progress = AnalysisProgress()
        self.timer = QTimer(self)
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.poll)
        body = QWidget()
        layout = QVBoxLayout(body)
        description = QLabel("Compare existing image and video thumbnails in this folder to sort by similarity or DBSCAN groups.")
        description.setWordWrap(True)
        layout.addWidget(description)
        self.parameters = QGroupBox("Clustering")
        form = QFormLayout(self.parameters)
        form.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapLongRows)
        self.eps = QDoubleSpinBox()
        self.eps.setDecimals(4)
        self.eps.setRange(0.0001, 2.0)
        self.eps.setSingleStep(0.05)
        self.eps.setValue(0.25)
        self.eps.setToolTip("Maximum Euclidean neighbor distance on the normalized weighted vector. Lower values form tighter groups.")
        form.addRow("Distance threshold (eps)", self.eps)
        self.min_samples = QSpinBox()
        self.min_samples.setRange(1, 1000000)
        self.min_samples.setValue(3)
        self.min_samples.setToolTip("Neighbors required for a core media item, including the item itself. Noise is sorted after clusters.")
        form.addRow("Minimum neighbors", self.min_samples)
        layout.addWidget(self.parameters)
        self.features = QGroupBox("Feature weights")
        weights_form = QFormLayout(self.features)
        self.weights = []
        for label, value in zip(("RGB color", "HSV color", "Spatial color", "Texture", "Brightness / contrast", "Aspect ratio"),
                                AnalysisSettings().weights):
            spin = QDoubleSpinBox()
            spin.setRange(0, 100)
            spin.setDecimals(2)
            spin.setSingleStep(0.1)
            spin.setValue(value)
            spin.valueChanged.connect(self.update_actions)
            weights_form.addRow(label, spin)
            self.weights.append(spin)
        layout.addWidget(self.features)
        hint = QLabel("Higher weights increase influence. Zero disables a feature. Enable at least one feature.")
        hint.setWordWrap(True)
        layout.addWidget(hint)
        self.cluster_button = QPushButton("Cluster and sort")
        self.cluster_button.clicked.connect(lambda: self.start(None))
        layout.addWidget(self.cluster_button)
        self.reference_label = QLabel("Select one media item to compare.")
        self.reference_label.setWordWrap(True)
        layout.addWidget(self.reference_label)
        self.compare_button = QPushButton("Sort by selected media")
        self.compare_button.clicked.connect(lambda: self.start(self.reference))
        layout.addWidget(self.compare_button)
        self.cancel_button = QPushButton("Cancel analysis")
        self.cancel_button.clicked.connect(self.cancel)
        layout.addWidget(self.cancel_button)
        self.clear_button = QPushButton("Restore name order")
        self.clear_button.clicked.connect(self.clearRequested)
        layout.addWidget(self.clear_button)
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 1)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)
        self.status = QLabel("Ready")
        self.status.setWordWrap(True)
        layout.addWidget(self.status)
        layout.addStretch()
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(body)
        self.setWidget(scroll)
        self.update_actions()

    def update_actions(self, *args):
        idle = self.future is None
        enabled = idle and bool(self.folder) and any(spin.value() != 0 for spin in self.weights)
        self.cluster_button.setEnabled(enabled)
        self.compare_button.setEnabled(enabled and self.reference is not None)
        self.cancel_button.setEnabled(not idle and not self.cancel_event.is_set())
        self.clear_button.setEnabled(idle)
        self.parameters.setEnabled(idle)
        self.features.setEnabled(idle)

    def set_folder(self, path):
        self.cancel()
        self.folder = path
        self.set_selection(())
        self.status.setText("Ready" if self.future is None else "Cancelling previous folder analysis…")
        self.update_actions()

    def set_selection(self, paths):
        self.reference = paths[0] if len(paths) == 1 and Path(paths[0]).suffix.lower() in MEDIA_SUFFIXES else None
        self.reference_label.setText("Reference: " + Path(self.reference).name if self.reference else "Select one media item to compare.")
        self.update_actions()

    def start(self, reference):
        self.cancel_event = Event()
        self.progress = AnalysisProgress()
        settings = AnalysisSettings(tuple(spin.value() for spin in self.weights), self.eps.value(), self.min_samples.value())
        self.future = self.executor.submit(analyze_folder, self.folder, settings, reference,
                                           self.cancel_event, self.progress, self.load_thumbnail)
        self.status.setText("Starting thumbnail analysis…")
        self.progress_bar.setRange(0, 0)
        self.update_actions()
        self.timer.start()

    def cancel(self):
        self.cancel_event.set()
        if self.future is not None:
            self.status.setText("Cancelling…")
        self.update_actions()

    def poll(self):
        stage, completed, total = self.progress.state
        self.progress_bar.setRange(0, total)
        self.progress_bar.setValue(completed)
        if not self.cancel_event.is_set():
            self.status.setText(f"{stage}: {completed:,} / {total:,}")
        if not self.future.done():
            return
        future = self.future
        self.future = None
        self.timer.stop()
        self.progress_bar.setRange(0, 1)
        self.progress_bar.setValue(1)
        self.status.setText("Analysis stopped")
        self.update_actions()
        result = future.result()
        if self.cancel_event.is_set() or result is None:
            self.status.setText("Cancelled")
            return
        self.orderReady.emit(result)
        if not result.paths:
            self.status.setText("No media items in this folder.")
        elif result.distances:
            self.status.setText(f"Sorted {len(result.paths):,} media items by distance to the selected thumbnail.")
        else:
            self.status.setText(f"{len(result.paths):,} media items · {result.clusters:,} clusters · {result.noise:,} noise items")

    def shutdown(self):
        self.cancel_event.set()
        self.timer.stop()
        self.executor.shutdown(wait=True, cancel_futures=False)
        if self.future is not None:
            self.future.result()
            self.future = None
