# This Python file uses the following encoding: utf-8
import sys
import logging

# Setup logging level and format.
logging.basicConfig(
    level   = logging.DEBUG,
    format  = "%(asctime)s - [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

try:
    from PySide6.QtWidgets import QApplication
except ModuleNotFoundError:
    # The user does not have PySide6 installed; let them know that they need to install it.
    sys.stderr.write(
        "\n".join(
            [
                "PySide6 has not been installed; this application cannot run!",
                "",
                "foo"
            ]
        ) + "\n"
    )
    sys.exit(1)

from src.utils.Database import GameDB
from src.MainMenu import MainMenu

# Import resources such as images and audio.
import rc_resources

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
