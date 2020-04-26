from .Enums import Terrains, TileIDs
from .TileCastle import TileCastle
from .TileMeadow import TileMeadow


class Tile16(TileCastle, TileMeadow):

    id = TileIDs.TILE16

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3], Terrains.CASTLE, 1, None],
                      [[4, 5, 6, 7, 8, 9, 10, 11, 12], Terrains.MEADOW, 2, None]]
        self.center = [[0], Terrains.DEFAULT, 3, None]
        self.amount = 5
