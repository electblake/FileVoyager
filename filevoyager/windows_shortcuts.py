"""Resolve Windows folder shortcuts on directory scan workers."""

import os
import stat
from functools import lru_cache

from comtypes import CoInitializeEx, CoUninitialize, COINIT_MULTITHREADED
from comtypes.client import CreateObject


@lru_cache(maxsize=4096)
def shortcut_target(path, modified_ns, size):
    """Cache only target strings; never retain COM objects across worker calls."""
    CoInitializeEx(COINIT_MULTITHREADED)
    shell = CreateObject("WScript.Shell", dynamic=True)
    shortcut = shell.CreateShortcut(path)
    target = shortcut.TargetPath
    del shortcut, shell
    CoUninitialize()
    return target


def folder_shortcut_targets(paths):
    targets = {}
    for path in paths:
        metadata = os.stat(path)
        target = shortcut_target(os.path.abspath(path), metadata.st_mtime_ns, metadata.st_size)
        targets[path] = target if stat.S_ISDIR(os.stat(target).st_mode) else ""
    return targets
