import unittest

from backend.tile.AuxFunctions import attach_left_right, attach_up_down
from backend.tile.Tile13MeadowCastleShield import Tile13
from backend.tile.Tile14MeadowCastle import Tile14
from backend.tile.Tile15MeadowCastle import Tile15
from backend.tile.Tile16MeadowCastle import Tile16
from backend.tile.Tile17MeadowRoadCastle import Tile17
from backend.tile.Tile18MeadowRoadCastle import Tile18
from backend.tile.Tile19MeadowRoadCastle import Tile19
from backend.tile.Tile20MeadowRoadCastle import Tile20
from backend.tile.Tile22MeadowRoad import Tile22
from backend.tile.Tile23MeadowRoad import Tile23
from backend.tile.Tile25Start import Tile25
from backend.tile.Tile2MonasteryMeadowRoad import Tile2
from backend.tile.Tile4MeadowCastle import Tile4
from backend.tile.Tile8MeadowCastle import Tile8
from backend.tile.Tile9MeadowCastleShield import Tile9


class BigTest(unittest.TestCase):

    def test_whole_board(self):
        # t1  t2  t3  t4  t5  t6
        # t7  t8  t9  t10 t11 t12
        # t13 t14 t15 t16 t17 t18
        # t19 t20 t21 t22 t23 t24

        t1 = Tile18()
        t2 = Tile8()
        t3 = Tile13()
        t4 = Tile18()
        t5 = Tile19()
        t6 = Tile14()
        t7 = Tile13()
        t8 = Tile8()
        t9 = Tile17()
        t10 = Tile20()
        t11 = Tile22()
        t12 = Tile13()
        t13 = Tile15()
        t14 = Tile2()
        t15 = Tile23()
        t16 = Tile15()
        t17 = Tile22()
        t18 = Tile25()
        t19 = Tile9()
        t20 = Tile4()
        t21 = Tile18()
        t22 = Tile25()
        t23 = Tile17()
        t24 = Tile16()

        t1.turn_clockwise()
        t1.turn_clockwise()
        t2.turn_clockwise()
        t2.turn_clockwise()
        t4.turn_counterclockwise()
        t5.turn_clockwise()
        t6.turn_counterclockwise()
        t7.turn_clockwise()
        t8.turn_clockwise()
        t9.turn_counterclockwise()
        t10.turn_clockwise()
        t10.turn_clockwise()
        t11.turn_clockwise()
        t12.turn_clockwise()
        t14.turn_counterclockwise()
        t15.turn_clockwise()
        t17.turn_counterclockwise()
        t19.turn_clockwise()
        t20.turn_clockwise()
        t20.turn_clockwise()
        t21.turn_counterclockwise()
        t23.turn_clockwise()
        t24.turn_counterclockwise()

        attach_left_right(t1, t2)
        attach_left_right(t2, t3)
        attach_left_right(t3, t4)
        attach_left_right(t4, t5)
        attach_left_right(t5, t6)
        attach_left_right(t7, t8)
        attach_left_right(t8, t9)
        attach_left_right(t9, t10)
        attach_left_right(t10, t11)

        attach_left_right(t11, t12)

        attach_left_right(t13, t14)
        attach_left_right(t14, t15)
        attach_left_right(t15, t16)
        attach_left_right(t16, t17)
        attach_left_right(t17, t18)
        attach_left_right(t19, t20)
        attach_left_right(t20, t21)
        attach_left_right(t21, t22)
        attach_left_right(t22, t23)
        attach_left_right(t23, t24)

        attach_up_down(t1, t7)
        attach_up_down(t7, t13)
        attach_up_down(t13, t19)
        attach_up_down(t2, t8)
        attach_up_down(t8, t14)
        attach_up_down(t14, t20)
        attach_up_down(t3, t9)
        attach_up_down(t9, t15)
        attach_up_down(t15, t21)
        attach_up_down(t4, t10)
        attach_up_down(t10, t16)
        attach_up_down(t16, t22)
        attach_up_down(t5, t11)
        attach_up_down(t11, t17)
        attach_up_down(t17, t23)
        attach_up_down(t6, t12)
        attach_up_down(t12, t18)
        attach_up_down(t18, t24)

        t1.sides[2][3] = 1
        t24.sides[1][3] = 1
        t8.sides[1][3] = 2
        t16.sides[2][3] = 3
        t11.sides[0][3] = 4
        t18.sides[3][3] = 4

        self.assertEqual(t2.check_for_points_after_game_castle(), {})  # no one is there

        t20.sides[0][3] = 1
        self.assertEqual(t20.check_for_points_after_game_castle(), {1: 5})  # player 1 is there

        self.assertEqual(t8.check_for_points_after_game_meadow(), {2: 9, 1: 9})
        self.assertEqual(t11.check_for_points_after_game_meadow(), {4: 12, 3: 12})
        self.assertEqual(t1.check_for_points_after_game_meadow(), {1: 6})

        t24.sides[0][3] = 1
        self.assertEqual(t24.check_for_points_after_game_castle(), {1: 2})

        t14.center[3] = 2
        self.assertEqual(t14.check_for_points_after_game_monastery(), {2: 9})


if __name__ == '__main__':
    unittest.main()
