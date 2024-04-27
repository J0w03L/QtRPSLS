# This Python file uses the following encoding: utf-8
import logging
logger = logging.getLogger(__name__)

from PySide6 import QtCore, QtGui, QtWidgets
from .ui.ui_MainMenu import Ui_MainMenu
from .Game import GameWidget
from .utils.Database import GameDB

class MainMenu(QtWidgets.QMainWindow):
    def __init__(self, db: GameDB, parent = None, width: int = 600, height: int = 600):
        super().__init__(parent)

        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)

        """
            Setup background image animation.

            The background image label will slowly spin forever.

            As a bonus -- because said label has content scaling
            enabled -- the image will also slowly zoom in and out
            as it spins.

            Unfortunately, SVG layers aren't being rendered
            properly, so a PNG is being used here instead.
        """
        self.ui.bgImg._pixmap = QtGui.QPixmap(":/assets/MainMenu/img/rpsls_diagram_transparent.png")
        self.ui.bgImg._animation = QtCore.QVariantAnimation(
            self.ui.bgImg,
            loopCount = -1,
            startValue = 0.0,
            endValue = 360.0,
            duration = 20000,
            valueChanged = self.on_rotation_changed
        )
        self.ui.bgImg._animation.start()

        # Ensure the window is fixed to 600x600.
        self.resize_menu(width, height)

        # Ensure that we always start on the initial menu page.
        self.change_menu_page(0)

        """
            Hook button events.

            Lambdas are used in cases where arguments need to be passed to a function,
            because Qt's connect function only accepts a function object for a parameter.
        """
        self.ui.mainExitButton.clicked.connect(self.close)
        self.ui.mainAboutButton.clicked.connect(lambda _: self.change_menu_page(1))
        self.ui.mainGuideButton.clicked.connect(lambda _: self.change_menu_page(2))
        self.ui.mainPlayButton.clicked.connect(lambda _: self.open_game_widget(db))
        self.ui.aboutBackButton.clicked.connect(lambda _: self.change_menu_page(0))
        self.ui.guideBackButton.clicked.connect(lambda _: self.change_menu_page(0))

    def open_game_widget(self, db: GameDB):
        logger.debug("Opening game widget.")

        # Create and show the widget.
        widget = GameWidget(db)
        widget.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        logger.debug("Showing game widget.")
        widget.show()

        # Hide the main menu widget.
        logger.debug("Hiding main menu widget.")
        self.setVisible(False)

        # Connect destroyed event so that the main menu widget re-appears when game widget is closed.
        widget.destroyed.connect(lambda _: self.setVisible(True))

        # This feels VERY hacky, but if I don't do this, the game widget never gets a chance to show up.
        QtCore.QEventLoop().exec()

    def change_menu_page(self, index: int):
        logger.debug(f"Switching to menu page {index}.")
        self.ui.widgets.setCurrentIndex(index)

    def resize_menu(self, width: int, height: int):
        logger.debug(f"Resizing menu to [{width}, {height}].")

        # Set widget size to fized value.
        self.setFixedSize(width, height)

        # Update background frame size
        self.ui.bg.resize(width, height)

        # Update content frame size
        self.ui.content.resize(width, height)

    def on_rotation_changed(self, val):
        trans = QtGui.QTransform()
        trans.rotate(val)
        self.ui.bgImg.setPixmap(self.ui.bgImg._pixmap.transformed(trans))
