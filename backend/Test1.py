from Tile8MeadowCastle import Tile8
from Tile9MeadowCastleShield import Tile9
from Tile10MeadowRoadCastle import Tile10

t1 = Tile8()
t2 = Tile9()
t3 = Tile10()
t4 = Tile8()
t2.turn_counterclockwise()
t3.turn_clockwise()
t3.turn_clockwise()
t4.turn_clockwise()

print(t1.fit_up(t2))
t1.upTile = t2
t2.downTile = t1
print(t2.fit_left(t3))
t2.leftTile = t3
t3.rightTile = t2
print(t3.fit_down(t4))
print(t1.fit_left(t4))
t1.leftTile = t4
t4.rightTile = t1
t3.downTile = t4
t4.upTile = t3


print(t1.dfs_start(t1.sides[0]))  # no instances of (None, None) tuples, so the castle is complete
