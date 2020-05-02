from backend.tile.Enums import Terrains, TileIDs
from backend.tile.TileCastle import TileCastle
from backend.tile.TileMeadow import TileMeadow
from backend.tile.TileRoad import TileRoad


class Tile20(TileCastle, TileMeadow, TileRoad):

    id = TileIDs.TILE20
    amount = 3

    def __init__(self):
        super().__init__()
        self.sides = [[[5, 11], Terrains.ROAD, 4, None],
                      [[1, 2, 3], Terrains.CASTLE, 1, None],
                      [[4, 12], Terrains.MEADOW, 2, None],
                      [[6, 7, 8, 9, 10], Terrains.MEADOW, 3, None]]
        self.center = [[0], Terrains.DEFAULT, 5, None]
