from backend.tile.Enums import Terrains, TileIDs
from backend.tile.TileCastle import TileCastle
from backend.tile.TileMeadow import TileMeadow


class Tile12(TileCastle, TileMeadow):

    id = TileIDs.TILE12
    amount = 1

    def __init__(self):
        super().__init__()
        self.sides = [[[4, 5, 6, 10, 11, 12], Terrains.CASTLE, 1, None],
                      [[1, 2, 3], Terrains.MEADOW, 2, None],
                      [[7, 8, 9], Terrains.MEADOW, 3, None]]
        self.center = [[0], Terrains.DEFAULT, 4, None]
