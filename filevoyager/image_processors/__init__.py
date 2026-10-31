"""Standalone image descriptors; importing FileVoyager does not load this package."""

from .features.brightness_contrast import extract_brightness_contrast_features
from .features.geometry import extract_geometry_aspect_ratio_features
from .features.histograms import extract_histogram_features
from .features.spatial_color import extract_spatial_color_features
from .features.texture import extract_texture_features
from .features_extraction import DEFAULT_FEATURE_WEIGHTS, extract_visual_features
from .interface import ImageFeatureExtractor, SPECTRA_EXTRACTORS, SPECTRA_VISUAL_EXTRACTOR

__all__ = [
    "DEFAULT_FEATURE_WEIGHTS",
    "ImageFeatureExtractor",
    "SPECTRA_EXTRACTORS",
    "SPECTRA_VISUAL_EXTRACTOR",
    "extract_brightness_contrast_features",
    "extract_geometry_aspect_ratio_features",
    "extract_histogram_features",
    "extract_spatial_color_features",
    "extract_texture_features",
    "extract_visual_features",
]
