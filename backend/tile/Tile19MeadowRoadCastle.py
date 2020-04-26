from backend.tile.Enums import Terrains, TileIDs
from backend.tile.TileCastle import TileCastle
from backend.tile.TileMeadow import TileMeadow
from backend.tile.TileRoad import TileRoad


class Tile19(TileCastle, TileMeadow, TileRoad):

    id = TileIDs.TILE19

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3], Terrains.CASTLE, 1, None],
                      [[4, 12], Terrains.MEADOW, 2, None],
                      [[6, 7], Terrains.MEADOW, 3, None],
                      [[9, 10], Terrains.MEADOW, 4, None],
                      [[11], Terrains.ROAD, 5, None],
                      [[5], Terrains.ROAD, 6, None],
                      [[8], Terrains.ROAD, 7, None]]
        self.center = [[0], Terrains.DEFAULT, 8, None]
        self.amount = 3
