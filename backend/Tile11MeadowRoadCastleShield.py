from Enums import Terrains
from TileMeadow import TileMeadow
from TileCastleShield import TileCastleShield
from TileRoad import TileRoad


class Tile11(TileMeadow, TileCastleShield, TileRoad):

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3, 10, 11, 12], Terrains.CASTLESHIELD, 1, None],
                      [[5, 8], Terrains.ROAD, 2, None],
                      [[4, 9], Terrains.MEADOW, 3, None],
                      [[6, 7], Terrains.MEADOW, 4, None]]
        self.center = [[0], Terrains.DEFAULT, 5, None]
        self.amount = 2