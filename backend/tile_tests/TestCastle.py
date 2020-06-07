import unittest

from backend.tile.AuxFunctions import attach_left_right, attach_up_down
from backend.tile.Tile10MeadowRoadCastle import Tile10
from backend.tile.Tile8MeadowCastle import Tile8
from backend.tile.Tile9MeadowCastleShield import Tile9


class TestCastle(unittest.TestCase):

    def test_Castle(self):  # test capabilities of check_for_points_after_move

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

        t2.sides[0][3] = 1  # a pawn is placed (player 1)
        self.assertEqual(t1.check_for_points_after_move_castle(), {})  # castle is not completed

        attach_left_right(t4, t1)
        attach_up_down(t3, t4)

        t2.sides[0][3] = 1  # a pawn is placed (player 1)
        t4.sides[0][3] = 2  # (player 2)
        t3.sides[0][3] = 2  # (player 2), now player 2 has more pawns in this structure

        self.assertEqual(t1.check_for_points_after_move_castle(), {2: [10, 2], 1: [0, 1]})  # player 2 has more pawns

        t2.sides[0][3] = 1  # a pawn is placed (player 1)
        t3.sides[0][3] = 2  # (player 2)

        # player 2 and 1 have equal numbers of pawns
        self.assertEqual(t1.check_for_points_after_move_castle(), {1: [10, 1], 2: [10, 1]})

        self.assertEqual(t1.check_for_points_after_move_castle(), {})  # there are no pawns upon completion {}

    def test_Castle_after_game(self):  # test capabilities of check_for_points_after_game

        # t3 t2
        #    t1

        t1 = Tile8()
        t2 = Tile9()
        t3 = Tile10()
        t2.turn_counterclockwise()
        t3.turn_clockwise()
        t3.turn_clockwise()

        attach_up_down(t2, t1)
        attach_left_right(t3, t2)

        t2.sides[0][3] = 1  # a pawn is placed (player 1)
        self.assertEqual(t1.check_for_points_after_move_castle(), {})  # castle not completed
        self.assertEqual(t1.check_for_points_after_game_castle(), {})  # no pawn in the unfinished castle
        # grants 3 points for castle tiles and 1 for shield
        self.assertEqual(t2.check_for_points_after_game_castle(), {1: 4})


if __name__ == '__main__':
    unittest.main()
