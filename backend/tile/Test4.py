from Tile8MeadowCastle import Tile8
from Tile9MeadowCastleShield import Tile9
from Tile10MeadowRoadCastle import Tile10


def test():  # test capabilities of check_for_points_after_move
    t1 = Tile8()
    t2 = Tile9()  # this one has a shield
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

    t2.sides[0][3] = 1  # a pawn is placed (player 1)
    print(t1.check_for_points_after_move())  # scenario 0 castle is unfinished

    t1.leftTile = t4
    t4.rightTile = t1
    t3.downTile = t4
    t4.upTile = t3

    t2.sides[0][3] = 1  # a pawn is placed (player 1)
    t4.sides[0][3] = 2  # (player 2)
    t3.sides[0][3] = 2  # (player 2)

    print(t1.check_for_points_after_move())  # scenario 1 player 2 has more pawns

    t2.sides[0][3] = 1  # a pawn is placed (player 1)
    t3.sides[0][3] = 2  # (player 2), now player 2 has more pawns in this structure

    print(t1.check_for_points_after_move())  # scenario 2 player 2 and 1 have equal numbers of pawns

    print(t1.check_for_points_after_move())  # scenario 3 there are no pawns upon completion


if __name__ == '__main__':
    test()
