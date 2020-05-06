import unittest
from backend.tile.AuxFunctions import attach_left_right, attach_up_down

from backend.tile.Tile8MeadowCastle import Tile8
from backend.tile.Tile9MeadowCastleShield import Tile9
from backend.tile.Tile10MeadowRoadCastle import Tile10


class TestMeadow(unittest.TestCase):

    def test_meadow(self):  # test capabilities of check_for_points_after_move
        # t3 t2
        # t4 t1

        t1 = Tile8()
        t2 = Tile9()
        t3 = Tile10()
        t4 = Tile8()
        t2.turn_counterclockwise()
        t3.turn_clockwise()
        t3.turn_clockwise()
        t4.turn_clockwise()

        attach_up_down(t2, t1)
        attach_left_right(t3, t2)

        t1.sides[1][3] = 1  # a pawn is placed (player 1)
        t4.sides[1][3] = 2  # a pawn is placed (player 1)

        # castle is unfinished, but player 1 has a pawn here
        self.assertEqual(t1.check_for_points_after_game_meadow(), {})

        attach_left_right(t4, t1)
        attach_up_down(t3, t4)

        t1.sides[1][3] = 1  # a pawn is placed (player 1)

        self.assertEqual(t1.check_for_points_after_game_meadow(), {1: 3})  # castle completed, and pawn added anew
        self.assertEqual(t4.check_for_points_after_game_meadow(), {2: 3})  # another meadow, same castle, other player


if __name__ == '__main__':
    unittest.main()
