import unittest

from backend.tile.AuxFunctions import attach_left_right, attach_up_down
from backend.tile.Tile10MeadowRoadCastle import Tile10
from backend.tile.Tile16MeadowCastle import Tile16
from backend.tile.Tile6MeadowRoadCastle import Tile6
from backend.tile.Tile8MeadowCastle import Tile8
from backend.tile.Tile9MeadowCastleShield import Tile9


class TestDFS(unittest.TestCase):

    def test_fourconnectedtest(self):
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
        self.assertTrue(t1.fit_up(t2))
        attach_up_down(t2, t1)
        self.assertTrue(t2.fit_left(t3))
        attach_left_right(t3, t2)
        self.assertTrue(t3.fit_down(t4))
        self.assertTrue(t1.fit_left(t4))
        attach_left_right(t4, t1)
        attach_up_down(t3, t4)

        self.assertTrue((None, None) not in t1.dfs_start(t1.sides[0]))  # no instances of (None, None) means that
        # castle is completed

    def test_castlecompletion(self):
        t1 = Tile6()
        t2 = Tile16()
        t2.turn_clockwise()
        t3 = Tile16()
        t3.turn_counterclockwise()

        attach_left_right(t2, t1)
        attach_left_right(t1, t3)

        self.assertFalse((None, None) not in t1.dfs_start(t1.sides[0]))  # not completed

        t4 = Tile16()
        t4.turn_clockwise()
        t4.turn_clockwise()
        attach_up_down(t4, t1)

        self.assertTrue((None, None) not in t1.dfs_start(t1.sides[0]))  # completed


if __name__ == '__main__':
    unittest.main()
