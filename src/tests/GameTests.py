# This Python file uses the following encoding: utf-8
import unittest
from ..Game import GameMove, determine_outcome

# GameMove class tests
class TestGameMoveInit(unittest.TestCase):
    def setUp(self):
        self.rock     = GameMove.ROCK
        self.paper    = GameMove.PAPER
        self.scissors = GameMove.SCISSORS
        self.lizard   = GameMove.LIZARD
        self.spock    = GameMove.SPOCK

        self.expectedMoves      = [self.rock, self.paper, self.scissors, self.lizard, self.spock]
        self.expectedMoveNames  = ["rock", "paper", "scissors", "lizard", "spock"]
        self.expectedMoveVals   = [1, 2, 3, 4, 5]
        self.expectedMoveWins   = [[3, 4], [1, 5], [2, 4], [2, 5], [1, 3]]

        self.expectedMoveInfoStructure    = {
                                                "name": str,
                                                "wins": dict
                                            }
        self.expectedMoveInfoWinStructure = (int, str) # {1: "a", 2: "b", 3: "c"}

    def test_create_valid_game_moves(self):
        i = 1
        while i <= 5:
            try:                    _ = GameMove(i)
            except Exception as e:  self.fail(f"Couldn't create valid GameMove of type \"{i}\"; raised {type(e).__name__}!")
            i += 1

    def test_create_invalid_game_moves(self):
        for i in [0, -1, 6, 10, 100, 0.9]:
            self.assertRaises(ValueError, GameMove, 0)

    def test_validate_game_move_enum_values(self):
        i = 0
        while i < 5:
            self.assertEqual(
                self.expectedMoves[i].value,
                self.expectedMoveVals[i],
                msg = f"GameMove.{self.expectedMoveNames[i].upper()} enum value is \"{self.expectedMoves[i].value}\"; it should be \"{self.expectedMoveVals[i]}\"!"
            )
            i += 1

    def test_get_game_move_infos(self):
        i = 0
        while i < 5:
            try:                    _ = self.expectedMoves[i].info()
            except Exception as e:  self.fail(f"Couldn't get info for GameMove.{self.expectedMoveNames[i].upper()}; raised {type(e).__name__}!")
            i += 1

    def test_validate_game_move_info_structure(self):
        i = 0
        while i < 5:
            info = self.expectedMoves[i].info()

            # Ensure expected keys exist
            for k in self.expectedMoveInfoStructure.keys():
                self.assertIn(k, info.keys(), msg = f"Couldn't find key \"{k}\" in GameMove.{self.expectedMoveNames[i].upper()} info!")

            # Ensure expected keyvalues have expected types
            for k in self.expectedMoveInfoStructure:
                self.assertEqual(
                    self.expectedMoveInfoStructure[k],
                    type(info[k]),
                    msg = f"Key \"{k}\" of GameMove.{self.expectedMoveNames[i].upper()} info had type of \"{type(info[k]).__name__}\"; should be \"{self.expectedMoveInfoStructure[k].__name__}\"!"
                )

            # Ensure that all items in wins have the correct type pairs.
            for key, value in info["wins"].items():
                # Check the type of key
                self.assertEqual(
                    type(key),
                    self.expectedMoveInfoWinStructure[0],
                    msg = f"Key \"{key}\" in GameMove.{self.expectedMoveNames[i].upper()} info.wins had type of \"{type(key)}\"; should be \"{self.expectedMoveInfoWinStructure[0].__name__}\"!"
                )
                # Check the type of value
                self.assertEqual(
                    type(value),
                    self.expectedMoveInfoWinStructure[1],
                    msg = f"Value of key \"{key}\" in GameMove.{self.expectedMoveNames[i].upper()} info.wins had type of \"{type(value)}\"; should be \"{self.expectedMoveInfoWinStructure[1].__name__}\"!"
                )

            i += 1

    def test_validate_game_move_info_names(self):
        i = 0
        while i < 5:
            self.assertEqual(
                self.expectedMoves[i].info()["name"].lower(),
                self.expectedMoveNames[i].lower(),
                msg = f"GameType.{self.expectedMoveNames[i].upper()} had info name of \"{self.expectedMoves[i].info()['name'].lower()}\"; should be \"{self.expectedMoveNames[i].lower()}\"!"
            )
            i += 1

# Define test suites.
TestsGameMove = unittest.TestSuite([TestGameMoveInit()])
