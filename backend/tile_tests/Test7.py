from backend.tile.Tile8MeadowCastle import Tile8
from backend.tile.Tile9MeadowCastleShield import Tile9
from backend.tile.Tile10MeadowRoadCastle import Tile10


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

    t1.sides[1][3] = 1  # a pawn is placed (player 1)
    t4.sides[1][3] = 2  # a pawn is placed (player 1)

    print(t1.check_for_points_after_game_meadow())  # scenario 1 castle is unfinished

    t1.leftTile = t4
    t4.rightTile = t1
    t3.downTile = t4
    t4.upTile = t3

    t1.sides[1][3] = 1  # a pawn is placed (player 1)

    print(t1.check_for_points_after_game_meadow())  # scenario 2 castle completed, and pawn added anew

    print(t4.check_for_points_after_game_meadow())  # scenario 3 another meadow, same castle


if __name__ == '__main__':
    test()
