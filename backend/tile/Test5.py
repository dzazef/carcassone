from backend.tile.Tile8MeadowCastle import Tile8
from backend.tile.Tile9MeadowCastleShield import Tile9
from backend.tile.Tile10MeadowRoadCastle import Tile10


def test():  # test capabilities of check_for_points_after_game
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
    print(t1.check_for_points_after_move())  # scenario 1 after finishing a move, returns {}

    print(t1.check_for_points_after_game())  # scenario 2 after finishing a game, returns {}

    print(t2.check_for_points_after_game())  # scenario 3 after finishing a game, returns {1: 4}


if __name__ == '__main__':
    test()
