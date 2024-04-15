# This Python file uses the following encoding: utf-8
import sys
import logging

# Setup logging level and format.
logging.basicConfig(
    level   = logging.DEBUG,
    format  = "%(asctime)s - [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from PySide6.QtWidgets import QApplication
from src.MainMenu import MainMenu

# Import resources such as images and audio.
import rc_resources

if __name__ == "__main__":
    logger.debug("Starting app...")

    app = QApplication(sys.argv)
    widget = MainMenu()
    widget.show()
    ret = app.exec()

    logger.debug("Exiting app...")
    sys.exit(ret)
