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

        self.db = db

        self.ui = Ui_GameWidget()
        self.ui.setupUi(self)

        # Ensure a fixed size window.
        self.setFixedSize(600, 600)

        # Disable play buttons before connecting any events.
        self.set_play_buttons_enabled(False)

        # Hook game's play buttons.
        self.ui.rockButton.clicked.connect(lambda _: self.play_move(1))
        self.ui.paperButton.clicked.connect(lambda _: self.play_move(2))
        self.ui.scissorsButton.clicked.connect(lambda _: self.play_move(3))
        self.ui.lizardButton.clicked.connect(lambda _: self.play_move(4))
        self.ui.spockButton.clicked.connect(lambda _: self.play_move(5))

        # Hook user selection menu objects.
        self.ui.userList.currentRowChanged.connect(self.select_user)
        self.ui.userPlayButton.clicked.connect(self.start_game)

        # Hook replay menu buttons.
        self.ui.playAgainYesButton.clicked.connect(self.start_game)
        self.ui.playAgainNoButton.clicked.connect(self.close)

        # Show the user selection menu.
        self.show_user_select()

    def setup_round(self):
        # Reset round variables.
        self.currentRound = 0
        self.maxRounds = 3
        self.wonRounds = [None, None, None]

        # Reset score label text and color.
        self.ui.scoreLabel.setText("You are tied with 0 to 0.")
        self.ui.scoreLabel.setStyleSheet("color:#000;")

        # Reset outcome label pixmap.
        self.ui.sceneActionLabel.clear()

    def show_replay_menu(self):
        # Disable game's play buttons.
        self.set_play_buttons_enabled(False)

        self.ui.sceneWidgets.setCurrentIndex(2)

    def show_user_select(self):
        # Disable game's play buttons.
        self.set_play_buttons_enabled(False)

        # Refresh the user list.
        self.refresh_user_list()

        # Switch to the user page.
        self.ui.sceneWidgets.setCurrentIndex(0)

    def refresh_user_list(self):
        logger.debug("Refreshing user list.")

        # Disable new user name field and play button.
        self.ui.newUserNameField.setEnabled(False)
        self.ui.userPlayButton.setEnabled(False)

        # Clear any existing users from the user list.
        self.ui.userList.clear()
        self.selectedUser = None

        # Find existing users from the database.
        self.users = self.db.get_users()

        # Add them all to the userList.
        for userID, userName in self.users:
            self.ui.userList.addItem(userName)

        # Add an additional item for creating a new user.
        self.ui.userList.addItem("Add a new user")

    def select_user(self, new: int):
        # If new is -1, selection was cleared.
        if new == -1:
            logger.debug("User selection was cleared.")

            self.selectedUser = None
            self.ui.newUserNameField.setEnabled(False)
            self.ui.userPlayButton.setEnabled(False)
            return

        # If the last item was selected, it must be the "Create new user" item.
        if new == self.ui.userList.count() - 1 and self.ui.userList.count() != 0:
            logger.debug("\"Create new user\" item was selected.")

            self.selectedUser = -1
            self.ui.newUserNameField.setEnabled(True)
            self.ui.userPlayButton.setEnabled(True)
            return

        logger.debug(f"Selected user {new} (id: {self.users[new][0]}; name: \"{self.users[new][1]}\")")

        self.selectedUser = self.users[new]
        self.ui.newUserNameField.setEnabled(False)
        self.ui.userPlayButton.setEnabled(True)
        return

    def start_game(self):
        # Check if we need to create a new user.
        if self.selectedUser == -1:
            # Make sure the user actually entered a name. If they didn't, don't let them continue.
            if self.ui.newUserNameField.text().strip() == "":
                logger.debug("TODO: show error message; no new user name was given.")
                return

            self.selectedUser = self.db.create_user(self.ui.newUserNameField.text().strip())

        # Create new game session in database.
        self.session = self.db.create_game(self.selectedUser[0])

        # Reset round variables.
        self.setup_round()

        # Re-enable play buttons.
        self.set_play_buttons_enabled(True)

        # Switch to the main page.
        self.ui.sceneWidgets.setCurrentIndex(1)

    def play_sound(self, path: str, vol: float = 1.0):
        self.sound = QtMultimedia.QSoundEffect()
        self.sound.setSource(QtCore.QUrl.fromLocalFile(path))
        self.sound.setVolume(vol)
        self.sound.play()

    def play_move(self, moveType: int):
        # Disable move buttons temporarily.
        self.set_play_buttons_enabled(False)

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

        # Get win/loss count so far.
        wins    = self.wonRounds.count(True)
        losses  = self.wonRounds.count(False)


        # Update score label text.
        self.ui.scoreLabel.setText(
            f"You are tied with {wins} to {losses}." if wins == losses else
            f"You are winning with {wins} to {losses}." if wins > losses else
            f"You are losing with {losses} to {wins}."
        )

        # Update score label color.
        self.ui.scoreLabel.setStyleSheet(
            "color:#000;" if wins == losses else
            "color:#0f0;" if wins > losses else
            "color:#f00;"
        )

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

    def set_play_buttons_enabled(self, val: bool):
        self.ui.rockButton.setEnabled(val)
        self.ui.paperButton.setEnabled(val)
        self.ui.scissorsButton.setEnabled(val)
        self.ui.lizardButton.setEnabled(val)
        self.ui.spockButton.setEnabled(val)

    def on_sceneActionLabel_rotation_changed(self, val):
        trans = QtGui.QTransform()
        trans.rotate(val)
        self.ui.sceneActionLabel.setPixmap(self.ui.sceneActionLabel._pixmap.transformed(trans))

        if self.ui.sceneActionLabel._animation.endValue() == val:
            # Animation finished; re-enable buttons.
            logger.debug("anim finished")
            self.set_play_buttons_enabled(True)

            # Play a comic sound effect for dramatic tension!
            self.play_sound(f":/assets/Game/snd/comic{1 if self.currentRound % 2 else 2}.wav")

            # Check if the game is over.
            if self.currentRound == 3:
                won = self.wonRounds.count(True) > self.wonRounds.count(False)

                # Save the outcome of this game to the database.
                logger.debug(f"Game is over; saving game (won = {won}).")
                self.db.finish_game(self.session, won)

                # Switch to replay widget.
                self.show_replay_menu()
