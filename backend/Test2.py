from Tile8MeadowCastle import Tile8
from Tile9MeadowCastleShield import Tile9
from Tile10MeadowRoadCastle import Tile10


def test():  # test capabilities of offer_to_place_a_pawn function
    t1 = Tile8()
    t2 = Tile9()
    t3 = Tile10()
    t4 = Tile8()
    t2.turn_counterclockwise()
    t3.turn_clockwise()
    t3.turn_clockwise()
    t4.turn_clockwise()

    t1.upTile = t2
    t2.downTile = t1
    t2.leftTile = t3
    t3.rightTile = t2
    t1.leftTile = t4
    t4.rightTile = t1
    t3.downTile = t4
    t4.upTile = t3

    print(t1.offer_to_place_a_pawn())  # returns [(1, <Terrains.CASTLE: 2>), (4, <Terrains.MEADOW: 1>)]

    t2.sides[0][3] = 1  # a pawn is placed

    print(t1.offer_to_place_a_pawn()) # returns [(4, <Terrains.MEADOW: 1>)]


if __name__ == '__main__':
    test()
