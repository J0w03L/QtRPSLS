# This Python file uses the following encoding: utf-8
import sys
import logging

# Setup logging level and format.
logging.basicConfig(
    level   = logging.DEBUG,
    format  = "%(asctime)s - [%(levelname)s] %(name)s::%(lineno)d (%(funcName)s): %(message)s"
)
logger = logging.getLogger(__name__)

try:
    from PySide6.QtWidgets import QApplication
    from PySide6.QtGui import QPalette, QColor
except ModuleNotFoundError:
    # The user does not have PySide6 installed; let them know that they need to install it.
    # We don't use logger for this; logger is primarily for debugging purposes.
    sys.stderr.write(
        "\n".join(
            [
                "PySide6 has not been installed; this application cannot run!",
                "",
                "Please install the \"pyside6\" package with the below command:",
                "    python -m pip install pyside6"
            ]
        ) + "\n"
    )

    # Exit with a non-zero status code to indicate an error occurred.
    sys.exit(1)

# Try to import resources such as images and audio.
# We don't need to use them in here, but if they don't exist, we can catch it early here.
try:
    import rc_resources
except ModuleNotFoundError:
    sys.stderr.write(
        "\n".join(
            [
                "py-QtRPSLS could not find rc_resources.py; this application cannot run!",
                "",
                "Please re-download py-QtRPSLS or run the following command in this program's root directory:",
                "    pyside6-rcc resources.qrc -o rc_resources.py"
            ]
        ) + "\n"
    )
    sys.exit(1)

from src.utils.Database import GameDB
from src.MainMenu import MainMenu

if __name__ == "__main__":
    logger.debug("Loading database...")
    db = GameDB("rpsls.db")

    logger.debug("Starting app...")

    app = QApplication(sys.argv)

    # Explicit application styling so that colors are consistent cross-platform.
    app.setStyle("fusion")

    # Force the palette to be the same on all platforms, regardless of system theme.
    # This isn't entirely ideal, but I'm too crunched for time on this to make everything
    # look fine across different themes.
    palette = QPalette(
        windowText      = QColor(0, 0, 0, 255),
        button          = QColor(239, 239, 239, 255),
        light           = QColor(255, 255, 255, 255),
        midlight        = QColor(202, 202, 202, 255),
        dark            = QColor(159, 159, 159, 255),
        mid             = QColor(184, 184, 184, 255),
        text            = QColor(0, 0, 0, 255),
        bright_text     = QColor(255, 255, 255, 255),
        buttonText      = QColor(0, 0, 0, 255),
        base            = QColor(255, 255, 255, 255),
        window          = QColor(239, 239, 239, 255),
        shadow          = QColor(118, 118, 118, 255),
        highlight       = QColor(48, 140, 198, 255),
        highlightedText = QColor(255, 255, 255, 255),
        link            = QColor(0, 0, 255, 255),
        linkVisited     = QColor(255, 0, 255, 255),
        alternateBase   = QColor(247, 247, 247, 255),
        tooltipBase     = QColor(255, 255, 220, 255),
        tooltipText     = QColor(0, 0, 0, 255),
        placeholderText = QColor(0, 0, 0, 128),
        accent          = QColor(48, 140, 198, 255),
    )
    app.setPalette(palette)

    widget = MainMenu(db)
    widget.show()
    ret = app.exec()

    logger.debug("Exiting app...")
    sys.exit(ret)
