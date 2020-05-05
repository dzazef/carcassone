from backend.tile.Tile21MeadowRoad import Tile21
from backend.tile.Tile22MeadowRoad import Tile22
from backend.tile.Tile1MonasteryMeadow import Tile1


def test():  # test capabilities of check_for_points_after_move_monastery
    t1 = Tile1()  # monastery here
    t2 = Tile21()
    t3 = Tile22()
    t4 = Tile21()

    t5 = Tile21()

    t4.turn_clockwise()

    t1.rightTile = t2
    t1.upTile = t4

    t2.leftTile = t1
    t2.upTile = t3

    t3.downTile = t2
    t3.leftTile = t4

    t4.rightTile = t3
    t4.downTile = t1

    t1.center[3] = 1  # player 1

    print(t1.check_for_points_after_game_monastery())  # 3 Tiles around

    t1.leftTile = t5
    t5.rightTile = t1

    print(t1.check_for_points_after_game_monastery())  # 4 Tiles around


if __name__ == '__main__':
    test()
