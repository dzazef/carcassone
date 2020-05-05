import unittest
from backend.tile.AuxFunctions import attach_left_right, attach_up_down

from backend.tile.Tile21MeadowRoad import Tile21
from backend.tile.Tile17MeadowRoadCastle import Tile17
from backend.tile.Tile18MeadowRoadCastle import Tile18
from backend.tile.Tile20MeadowRoadCastle import Tile20
from backend.tile.Tile22MeadowRoad import Tile22


class TestRoads(unittest.TestCase):

    def test_road(self):

        # t3 t2
        # t4 t1
        # t5 t6

        t1 = Tile21()
        t2 = Tile17()
        t3 = Tile18()
        t4 = Tile20()
        t5 = Tile22()
        t6 = Tile22()

        t4.turn_counterclockwise()
        t5.turn_clockwise()
        t5.turn_clockwise()
        t6.turn_clockwise()

        attach_up_down(t2, t1)
        attach_left_right(t3, t2)
        attach_up_down(t3, t4)
        attach_left_right(t4, t1)
        attach_up_down(t4, t5)
        attach_left_right(t5, t6)
        attach_up_down(t1, t6)

        t1.sides[0][3] = 1

        self.assertEqual(t1.check_for_points_after_game_road(), {1: 6})  # after this pawns reset

        t4.sides[0][3] = 2
        t3.sides[0][3] = 1

        self.assertEqual(t3.check_for_points_after_game_road(), {1: 6, 2: 6})


if __name__ == '__main__':
    unittest.main()
