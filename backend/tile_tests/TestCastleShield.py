import unittest
from backend.tile.AuxFunctions import attach_left_right, attach_up_down

from backend.tile.Tile8MeadowCastle import Tile8
from backend.tile.Tile9MeadowCastleShield import Tile9
from backend.tile.Tile10MeadowRoadCastle import Tile10
from backend.tile.Tile21MeadowRoad import Tile21
from backend.tile.AuxFunctions import attach_left_right, attach_up_down


class TestCastleShield(unittest.TestCase):

    def test_castle_shield(self):  # tests workings of a dfs algorithm in a configuration of 4 connected tiles

        # t3 t2 t6
        # t4 t1 t5

        t1 = Tile8()
        t2 = Tile9()
        t3 = Tile10()
        t4 = Tile8()
        t5 = Tile21()
        t6 = Tile21()

        t2.turn_counterclockwise()
        t3.turn_clockwise()
        t3.turn_clockwise()
        t4.turn_clockwise()

        attach_up_down(t2, t1)
        attach_left_right(t3, t2)
        attach_left_right(t4, t1)
        attach_up_down(t3, t4)
        attach_left_right(t1, t5)
        attach_left_right(t2, t6)
        attach_up_down(t6, t5)

        t2.sides[0][3] = 1
        t1.sides[1][3] = 2
        t2.sides[1][3] = 1

        print(t1.after_move())  # returns {1: [10, 1]} because it completed a castle
        print(t1.after_game())  # returns {1: 3, 2: 3} because meadow is connected and both players have each one pawn


if __name__ == '__main__':
    unittest.main()
