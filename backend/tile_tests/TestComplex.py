import unittest

from backend.tile.AuxFunctions import attach_left_right, attach_up_down
from backend.tile.Enums import Terrains
from backend.tile.Tile11MeadowRoadCastleShield import Tile11
from backend.tile.Tile14MeadowCastle import Tile14
from backend.tile.Tile16MeadowCastle import Tile16
from backend.tile.Tile20MeadowRoadCastle import Tile20
from backend.tile.Tile25Start import Tile25
from backend.tile.Tile2MonasteryMeadowRoad import Tile2
from backend.tile.Tile8MeadowCastle import Tile8
from backend.tile.Tile9MeadowCastleShield import Tile9


class TestMeadow(unittest.TestCase):

    def test_1(self):
        # IDs
        #    t1 t2 t3
        # t4 t5 t6 t7

        # Tiles
        #    T14 T16 T8
        # T9 T20 T2  T16

        t1 = Tile14()
        t2 = Tile16()
        t3 = Tile8()
        t4 = Tile11()
        t5 = Tile20()
        t6 = Tile2()
        t7 = Tile16()

        # rotate
        t1.turn_clockwise()
        t1.turn_clockwise()
        t2.turn_counterclockwise()
        t3.turn_clockwise()
        t3.turn_clockwise()
        t6.turn_clockwise()

        # connect
        attach_left_right(t1, t2)
        attach_left_right(t2, t3)
        attach_left_right(t4, t5)
        attach_left_right(t5, t6)
        attach_left_right(t6, t7)
        attach_up_down(t1, t5)
        attach_up_down(t2, t6)
        attach_up_down(t3, t7)

        # place pawns
        t1.sides[2][3] = 2
        t2.sides[1][3] = 2
        t3.sides[0][3] = 2
        t4.sides[2][3] = 2
        t5.sides[0][3] = 1
        t6.center[3] = 1
        t7.sides[1][3] = 1

        # first tile, player two gains 3 points for each castle adjecent to his meadow
        self.assertEqual(t1.after_game(), {2: 6})

        # second tile, player two gains 3 points for each castle adjecent to his meadow and player 1 gains nothing,
        # because player 2 outnumbers his pawns on this meadow
        self.assertEqual(t2.after_game(), {2: 6})

        # third tile, player two gains 1 point for each fragment of his unfinished castle
        self.assertEqual(t3.after_game(), {2: 2})

        # fourth tile, this meadow was already checked, so there is no pawn
        self.assertEqual(t4.after_game(), {})

        # fifth tile, player 1 gets 3 points for his unfinished road
        self.assertEqual(t5.after_game(), {1: 3})

        # sixth tile, player 1 gets 6 points for his unfinished monastery
        self.assertEqual(t6.after_game(), {1: 6})

        # seventh tile, this meadow was already checked, so there is no pawn
        self.assertEqual(t7.after_game(), {})

    def test_2(self):
        t1 = Tile25()  # first tile

        t2 = Tile9()
        self.assertEqual(t1.fit_up(t2), False)
        t2.turn_counterclockwise()
        self.assertEqual(t1.fit_up(t2), True)  # fits after rotating
        attach_up_down(t2, t1)
        # can place a pawn in the castle and on the meadow
        self.assertEqual(t2.offer_to_place_a_pawn(), [(10, Terrains.CASTLE), (1, Terrains.MEADOW)])
        t2.place_a_pawn(10, 1)  # player 1 place a pawn in the castle
        self.assertEqual(t2.after_move(), {})  # no points given

        # one turn:
        # -if no tiles remain run function after_game() for each tile, merge their dictionaries and send to all clients
        # -if there is a tile remaining take it from a deck
        # -check if it can be placed anywhere on the board in any of its 4 possible rotations
        # -if no, cast it aside and draw another tile
        # -otherwise, send possible coordinates to the client
        # -upon response from the client attach the tile to all adjecent ones
        # -run offer_to_place_a_pawn() in the recently placed tile
        # -for the convenience of frontend representation position of these pawns should be translated with the
        #   other_reciprocal(num) function from Tile.py  ex. 4 = (1, 6) and then sent, upon response
        #   if client did place a pawn its position should be translated back and then function
        #   place_a_pawn(position, player) should be executed with the translated position as a 'position' parameter
        # -execute function after_move() and sent the resulting dictionary to the client ({player: [points, No. pawns]})

        t3 = Tile16()
        t3.turn_clockwise()
        self.assertTrue(t2.fit_left(t3))  # fits
        attach_left_right(t3, t2)  # what a bad move from player 2!
        self.assertEqual(t3.offer_to_place_a_pawn(), [(7, Terrains.MEADOW)])
        # decides not to place a pawn
        self.assertEqual(t3.after_move(), {1: [8, 1]})  # he gave player 1 8 points!(6 from catle tiles 2 from a shield)


if __name__ == '__main__':
    unittest.main()
