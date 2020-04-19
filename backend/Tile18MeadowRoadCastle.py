from Enums import Terrains
from TileCastle import TileCastle
from TileMeadow import TileMeadow
from TileRoad import TileRoad


class Tile18(TileCastle, TileMeadow, TileRoad):

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3], Terrains.CASTLE, 1, None],
                      [[4, 9, 10, 11, 12], Terrains.MEADOW, 2, None],
                      [[5, 8], Terrains.ROAD, 3, None],
                      [[6, 7], Terrains.MEADOW, 4, None]]
        self.center = [[0], Terrains.DEFAULT, 5, None]
        self.amount = 3
