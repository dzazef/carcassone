import unittest

from backend.tile.AuxFunctions import attach_left_right, attach_up_down
from backend.tile.Tile1MonasteryMeadow import Tile1
from backend.tile.Tile21MeadowRoad import Tile21
from backend.tile.Tile22MeadowRoad import Tile22


class TestMonastery(unittest.TestCase):

    def test_monastery(self):  # test capabilities of check_for_points_after_move_monastery

        #      t4 t3
        # (t5) t1 t2

        t1 = Tile1()  # monastery here
        t2 = Tile21()
        t3 = Tile22()
        t4 = Tile21()
        t5 = Tile21()

        t4.turn_clockwise()

        attach_left_right(t1, t2)
        attach_up_down(t3, t2)
        attach_left_right(t4, t3)
        attach_up_down(t4, t1)

        t1.center[3] = 1  # player 1

        print(t1.check_for_points_after_game_monastery())  # 3 Tiles around

        attach_left_right(t5, t1)
        t1.center[3] = 1  # same pawn as above

        print(t1.check_for_points_after_game_monastery())  # 4 Tiles around


if __name__ == '__main__':
    unittest.main()
