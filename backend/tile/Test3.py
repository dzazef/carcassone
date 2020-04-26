from backend.tile.Tile21MeadowRoad import Tile21
from backend.tile.Tile17MeadowRoadCastle import Tile17
from backend.tile.Tile18MeadowRoadCastle import Tile18
from backend.tile.Tile20MeadowRoadCastle import Tile20
from backend.tile.Tile22MeadowRoad import Tile22


def test():
    t1 = Tile21()
    t2 = Tile17()
    t3 = Tile18()
    t4 = Tile20()
    t5 = Tile22()
    t6 = Tile22()

    t4.turn_clockwise()
    t5.turn_clockwise()
    t5.turn_clockwise()
    t6.turn_clockwise()

    t1.upTile = t2
    t2.downTile = t1
    t2.leftTile = t3
    t3.rightTile = t2
    t3.downTile = t4
    t4.upTile = t3
    t1.leftTile = t4
    t4.rightTile = t1
    t4.downTile = t5
    t5.upTile = t4
    t5.rightTile = t6
    t6.leftTile = t5
    t1.downTile = t6
    t6.upTile = t1

    t1.sides[0][3] = 1

    """
    dfs = t1.dfs_start(t1.sides[0])
    for i in dfs:
        if i == (None, None):
            print("road not completed")
            break
    """
    print(t1.count_points_after_game())  # returns {1: 6}
    t4.sides[0][3] = 2
    t3.sides[0][3] = 1
    print(t3.count_points_after_game())  # returns {1: 6, 2: 6}


if __name__ == '__main__':
    test()
