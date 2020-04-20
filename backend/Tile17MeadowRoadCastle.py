from Enums import Terrains, TileIDs
from TileCastle import TileCastle
from TileMeadow import TileMeadow
from TileRoad import TileRoad


class Tile17(TileCastle, TileMeadow, TileRoad):

    id = TileIDs.TILE17

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3], Terrains.CASTLE, 1, None],
                      [[4, 5, 6, 7, 12], Terrains.MEADOW, 2, None],
                      [[8, 11], Terrains.ROAD, 3, None],
                      [[9, 10], Terrains.MEADOW, 4, None]]
        self.center = [[0], Terrains.DEFAULT, 5, None]
        self.amount = 3
