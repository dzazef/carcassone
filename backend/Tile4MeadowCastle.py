from Enums import Terrains, TileIDs
from TileCastle import TileCastle
from TileMeadow import TileMeadow


class Tile4(TileCastle, TileMeadow):

    id = TileIDs.TILE4

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3, 4, 5, 6, 10, 11, 12], Terrains.CASTLE, 1, None],
                      [[7, 8, 9], Terrains.MEADOW, 2, None]]
        self.center = [[0], Terrains.DEFAULT, 3, None]
        self.amount = 3
