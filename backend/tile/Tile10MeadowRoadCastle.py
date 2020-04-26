from Enums import Terrains, TileIDs
from TileMeadow import TileMeadow
from TileCastle import TileCastle
from TileRoad import TileRoad


class Tile10(TileMeadow, TileCastle, TileRoad):

    id = TileIDs.TILE10

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3, 10, 11, 12], Terrains.CASTLE, 1, None],
                      [[5, 8], Terrains.ROAD, 2, None],
                      [[4, 9], Terrains.MEADOW, 3, None],
                      [[6, 7], Terrains.MEADOW, 4, None]]
        self.center = [[0], Terrains.DEFAULT, 5, None]
        self.amount = 3
