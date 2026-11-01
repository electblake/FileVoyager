import argparse
import sys

from PySide6.QtWidgets import QApplication

from filevoyager.window import ExplorerWindow
from filevoyager.shell_bridge import load_thumbnail_image


def main():
    parser = argparse.ArgumentParser(description="FileVoyager")
    parser.add_argument("folder", nargs="?")
    args = parser.parse_args()
    app = QApplication(sys.argv[:1])
    app.setApplicationName("FileVoyager")
    app.setOrganizationName("FileVoyager")
    window = ExplorerWindow(args.folder, load_thumbnail_image)
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
