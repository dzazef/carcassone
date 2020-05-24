import unittest
from backend.tile.AuxFunctions import attach_left_right, attach_up_down

from backend.tile.Enums import Terrains
from backend.tile.Tile8MeadowCastle import Tile8
from backend.tile.Tile18MeadowRoadCastle import Tile18
from backend.tile.Tile13MeadowCastleShield import Tile13
from backend.tile.Tile19MeadowRoadCastle import Tile19
from backend.tile.Tile14MeadowCastle import Tile14
from backend.tile.Tile17MeadowRoadCastle import Tile17
from backend.tile.Tile20MeadowRoadCastle import Tile20
from backend.tile.Tile15MeadowCastle import Tile15
from backend.tile.Tile2MonasteryMeadowRoad import Tile2
from backend.tile.Tile23MeadowRoad import Tile23
from backend.tile.Tile22MeadowRoad import Tile22
from backend.tile.Tile25Start import Tile25
from backend.tile.Tile9MeadowCastleShield import Tile9
from backend.tile.Tile4MeadowCastle import Tile4
from backend.tile.Tile16MeadowCastle import Tile16


class TestCountingPointsAfterGame(unittest.TestCase):

    def test_counting_points(self):
        # t1  t2  t3  t4  t5  t6
        # t7  t8  t9  t10 t11 t12
        # t13 t14 t15 t16 t17 t18
        # t19 t20 t21 t22 t23 t24

        t1 = Tile18()  # 1 turn
        t1.turn_clockwise()
        t1.turn_clockwise()
        t1.place_a_pawn(10, 1)  # 1 player put pawn on meadow

        t2 = Tile8()  # 2 turn
        t2.turn_clockwise()
        t2.turn_clockwise()
        attach_left_right(t1, t2)

        t3 = Tile13()  # 3 turn
        attach_left_right(t2, t3)

        t4 = Tile18()  # 4 turn
        t4.turn_counterclockwise()
        attach_left_right(t3, t4)

        t5 = Tile19()  # 5 turn
        t5.turn_clockwise()
        attach_left_right(t4, t5)

        t6 = Tile14()  # 6 turn
        t6.turn_counterclockwise()
        attach_left_right(t5, t6)

        t7 = Tile13()  # 7 turn
        t7.turn_clockwise()
        attach_up_down(t1, t7)

        t8 = Tile8()  # 8 turn
        t8.turn_clockwise()
        attach_left_right(t7, t8)
        attach_up_down(t2, t8)
        t8.place_a_pawn(7, 2)  # 2 player put pawn on meadow

        t9 = Tile17()  # 9 turn
        t9.turn_counterclockwise()
        attach_left_right(t8, t9)
        attach_up_down(t3, t9)

        t10 = Tile20()  # 10 turn
        t10.turn_clockwise()
        t10.turn_clockwise()
        attach_left_right(t9, t10)
        attach_up_down(t4, t10)

        t11 = Tile22()  # 11 turn
        t11.turn_clockwise()
        attach_left_right(t10, t11)
        attach_up_down(t5, t11)
        t11.place_a_pawn(4, 4)  # 4 player put pawn on meadow

        t12 = Tile13()  # 12 turn
        t12.turn_clockwise()
        attach_left_right(t11, t12)
        attach_up_down(t6, t12)

        t13 = Tile15()  # 13 turn
        attach_up_down(t7, t13)

        t14 = Tile2()  # 14 turn
        t14.turn_counterclockwise()
        attach_left_right(t13, t14)
        attach_up_down(t8, t14)

        t15 = Tile23()  # 15 turn
        t15.turn_clockwise()
        attach_left_right(t14, t15)
        attach_up_down(t9, t15)

        t16 = Tile15()  # 16 turn
        attach_left_right(t15, t16)
        attach_up_down(t10, t16)
        t16.place_a_pawn(1, 3)  # 3 player put pawn on castle

        t17 = Tile22()  # 17 turn
        t17.turn_counterclockwise()
        attach_left_right(t16, t17)
        attach_up_down(t11, t17)

        t18 = Tile25()  # 18 turn
        attach_left_right(t17, t18)
        attach_up_down(t12, t18)
        t18.place_a_pawn(6, 4)  # 4 player put pawn on meadow

        t19 = Tile9()  # 19 turn
        t19.turn_clockwise()
        attach_up_down(t13, t19)

        t20 = Tile4()  # 20 turn
        t20.turn_clockwise()
        t20.turn_clockwise()
        attach_left_right(t19, t20)
        attach_up_down(t14, t20)

        t21 = Tile18()  # 21 turn
        t21.turn_counterclockwise()
        attach_left_right(t20, t21)
        attach_up_down(t15, t21)

        t22 = Tile25()  # 22 turn
        attach_left_right(t21, t22)
        attach_up_down(t16, t22)

        t23 = Tile17()  # 23 turn
        t23.turn_clockwise()
        attach_left_right(t22, t23)
        attach_up_down(t17, t23)
        t23.place_a_pawn(11, 1)  # 1 player put pawn on road

        t24 = Tile16()  # 24 turn
        t24.turn_counterclockwise()
        attach_left_right(t23, t24)
        attach_up_down(t18, t24)
        t24.place_a_pawn(10, 1)  # 1 player put pawn on castle

        self.assertEqual(t1.after_game(), {1: 6})  # there is only 1 player on tile1
        self.assertEqual(t2.after_game(), {})
        self.assertEqual(t3.after_game(), {})
        self.assertEqual(t4.after_game(), {})
        self.assertEqual(t5.after_game(), {})
        self.assertEqual(t6.after_game(), {})
        self.assertEqual(t7.after_game(), {})
        self.assertEqual(t8.after_game(), {2: 9, 4: 9})  # there are 2 pawns(from player 2 and 4)
        self.assertEqual(t9.after_game(), {})
        self.assertEqual(t10.after_game(), {})
        self.assertEqual(t11.after_game(), {4: 12})  # player 4 is the only one on this meadow
        self.assertEqual(t12.after_game(), {})
        self.assertEqual(t13.after_game(), {})
        self.assertEqual(t14.after_game(), {})
        self.assertEqual(t15.after_game(), {})
        self.assertEqual(t16.after_game(), {3: 2})
        self.assertEqual(t17.after_game(), {})
        self.assertEqual(t18.after_game(), {})
        self.assertEqual(t19.after_game(), {})
        self.assertEqual(t20.after_game(), {})
        self.assertEqual(t21.after_game(), {})
        self.assertEqual(t22.after_game(), {})
        self.assertEqual(t23.after_game(), {1: 6})  # there is a pawn from player 1 on the castle
        self.assertEqual(t24.after_game(), {1: 2})


if __name__ == '__main__':
    unittest.main()
