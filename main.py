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

    widget = MainMenu(db)
    widget.show()
    ret = app.exec()

    logger.debug("Exiting app...")
    sys.exit(ret)
