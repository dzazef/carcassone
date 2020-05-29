import unittest
from backend.tile.AuxFunctions import attach_left_right, attach_up_down

from backend.tile.Enums import Terrains
from backend.tile.Tile8MeadowCastle import Tile8
from backend.tile.Tile9MeadowCastleShield import Tile9
from backend.tile.Tile10MeadowRoadCastle import Tile10


class Testoffertoplaceapawn(unittest.TestCase):

    def test_offering(self):  # test capabilities of offer_to_place_a_pawn function

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
        attach_left_right(t4, t1)
        attach_up_down(t3, t4)

        self.assertEqual(t1.offer_to_place_a_pawn(), [(1, Terrains.CASTLE), (4, Terrains.MEADOW)])  # castle and meadow

        t2.place_a_pawn(t2.offer_to_place_a_pawn()[0][0], 1)  # place a pawn in the first offered site

        self.assertEqual(t1.offer_to_place_a_pawn(), [(4, Terrains.MEADOW)])  # only meadow, castle has a pawn now


if __name__ == '__main__':
    unittest.main()
