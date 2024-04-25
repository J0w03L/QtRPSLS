# This Python file uses the following encoding: utf-8
import sys
import logging

# Setup logging level and format.
logging.basicConfig(
    level   = logging.DEBUG,
    format  = "%(asctime)s - [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

from PySide6.QtWidgets import QApplication

from src.utils.database import GameDB
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
