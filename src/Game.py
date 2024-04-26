# This Python file uses the following encoding: utf-8

import logging
logger = logging.getLogger(__name__)

from PySide6 import QtCore, QtGui, QtWidgets, QtMultimedia
from enum import Enum
from random import randint

from .ui.ui_Game import Ui_GameWidget
from .utils.Database import GameDB

class GameMove(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    LIZARD = 4
    SPOCK = 5

    def info(self) -> dict:
        if self.value not in range (1, 6): raise IndexError(f"Invalid GameMove of type \"{self.value}\"!")
        return  [
                    {
                        "name": "Rock",
                        "wins": {
                            3: "blunts",        # Rock blunts Scissors
                            4: "crushes"        # Rock crushes Lizard
                        }
                    },
                    {
                        "name": "Paper",
                        "wins": {
                            1: "covers",        # Paper covers Rock
                            5: "disproves"      # Paper disproves Spock
                        }
                    },
                    {
                        "name": "Scissors",
                        "wins": {
                            2: "cuts",          # Scissors cuts Paper
                            4: "decapitates"    # Scissors decapitates Lizard
                        }
                    },
                    {
                        "name": "Lizard",
                        "wins": {
                            2: "eats",          # Lizard eats Paper
                            5: "poisons"        # Lizard poisons Spock
                        }
                    },
                    {
                        "name": "Spock",
                        "wins": {
                            1: "vaporizes",     # Spock vaporizes Rock
                            3: "smashes"        # Spock smashes Scissors
                        }
                    }
                ][self.value - 1]

"""
    Determine the outcome of two moves.

    Returns a tuple containing:
        - a boolean indicating whether move1 won (or None if it tied)
        - action text for the game to display (eg. "Rock crushes Lizard")
"""
def determine_outcome(move1: GameMove, move2: GameMove) -> tuple:
    logger.debug(f"Determining outcome for move type {move1.value} played against {move2.value}.")

    move1Info = move1.info()
    move2Info = move2.info()

    # If the moves are the same, no need to check anything else.
    if move1.value == move2.value: return (None, f"{move1Info['name']} ties with {move2Info['name']}!")

    # Check for a winning condition.
    if move2.value in move1Info["wins"].keys(): return (True, f"{move1Info['name']} {move1Info['wins'][move2.value]} {move2Info['name']}!")

    # No winning condition was found; move 2 must have won.
    return (False, f"{move2Info['name']} {move2Info['wins'][move1.value]} {move1Info['name']}!")


class GameWidget(QtWidgets.QWidget):
    def __init__(self, db: GameDB):
        logger.debug("__init__()")

        super().__init__()

        self.ui = Ui_GameWidget()
        self.ui.setupUi(self)

        # Ensure a fixed size window.
        self.setFixedSize(600, 600)

        # Setup round stuff.
        self.currentRound = 0
        self.maxRounds = 3
        self.wonRounds = [None, None, None]

        # Hook buttons.
        self.ui.rockButton.clicked.connect(lambda _: self.play_move(1))
        self.ui.paperButton.clicked.connect(lambda _: self.play_move(2))
        self.ui.scissorsButton.clicked.connect(lambda _: self.play_move(3))
        self.ui.lizardButton.clicked.connect(lambda _: self.play_move(4))
        self.ui.spockButton.clicked.connect(lambda _: self.play_move(5))

    def play_sound(self, path: str, vol: float = 1.0):
        self.sound = QtMultimedia.QSoundEffect()
        self.sound.setSource(QtCore.QUrl.fromLocalFile(path))
        self.sound.setVolume(vol)
        self.sound.play()

    def play_move(self, moveType: int):
        # Disable move buttons temporarily.
        self.ui.rockButton.setEnabled(False)
        self.ui.paperButton.setEnabled(False)
        self.ui.scissorsButton.setEnabled(False)
        self.ui.lizardButton.setEnabled(False)
        self.ui.spockButton.setEnabled(False)

        # Create moves; 2nd one is pseudo-randomly generated.
        move1 = GameMove(moveType)
        move2 = GameMove(randint(1, 5))

        logger.debug(f"Player played {move1.info()['name']} against {move2.info()['name']}.")

        # Find out what the outcome of these moves are.
        playerWon, actionText = determine_outcome(move1, move2)

        # Record win/loss and advance round where applicable.
        match playerWon:
            case True:
                # Player won.
                logger.debug("Player won.")

                self.wonRounds[self.currentRound] = True
                self.currentRound += 1
            case False:
                # Player lost.
                logger.debug("Player lost.")

                self.wonRounds[self.currentRound] = False
                self.currentRound += 1
            case None:
                # Player tied. Don't advance the round or record a win/loss.
                logger.debug("Player tied.")

        # Create a pixmap that we can animate. We'll render the actionText to this with a QPainter.
        self.ui.sceneActionLabel._pixmap = QtGui.QPixmap(581, 411)

        actionPainter = QtGui.QPainter(self.ui.sceneActionLabel._pixmap)

        # "Clear" the background of the pixmap.
        actionPainter.fillRect(QtCore.QRect(0, 0, 581, 411), QtGui.QColor(239, 239, 239))

        # Setup text font/color and enable antialiasing.
        actionPainter.setFont(QtGui.QFont("Arial", 30))
        actionPainter.setPen(QtGui.QColor(0, 255, 0) if playerWon else QtGui.QColor(255, 0, 0))
        actionPainter.setRenderHint(QtGui.QPainter.Antialiasing)

        # Draw the text.
        actionPainter.drawText(QtCore.QRect(0, 0, 581, 411), QtCore.Qt.AlignCenter, actionText)

        # Pick a random animation direction.
        animDir = randint(1, 2)

        # Create the animation.
        self.ui.sceneActionLabel._animation = QtCore.QVariantAnimation(
            self.ui.sceneActionLabel,
            loopCount = 1,
            startValue = 270.0 if animDir == 1 else 90.0,
            endValue = 360.0 if animDir == 1 else 0.0,
            duration = 150,
            valueChanged = self.on_sceneActionLabel_rotation_changed
        )

        # Aaaand play it!
        self.ui.sceneActionLabel._animation.start()

    def on_sceneActionLabel_rotation_changed(self, val):
        trans = QtGui.QTransform()
        trans.rotate(val)
        self.ui.sceneActionLabel.setPixmap(self.ui.sceneActionLabel._pixmap.transformed(trans))

        if self.ui.sceneActionLabel._animation.endValue() == val:
            # Animation finished; re-enable buttons.
            logger.debug("anim finished")
            self.ui.rockButton.setEnabled(True)
            self.ui.paperButton.setEnabled(True)
            self.ui.scissorsButton.setEnabled(True)
            self.ui.lizardButton.setEnabled(True)
            self.ui.spockButton.setEnabled(True)

            # Play a comic sound effect for dramatic tension!
            self.play_sound(f":/assets/Game/snd/comic{1 if self.currentRound % 2 else 2}.wav")
