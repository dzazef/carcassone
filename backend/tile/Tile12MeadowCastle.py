from Enums import Terrains, TileIDs
from TileCastle import TileCastle
from TileMeadow import TileMeadow


class Tile12(TileCastle, TileMeadow):

    id = TileIDs.TILE12

    def __init__(self):
        super().__init__()
        self.sides = [[[4, 5, 6, 10, 11, 12], Terrains.CASTLE, 1, None],
                      [[1, 2, 3], Terrains.MEADOW, 2, None],
                      [[7, 8, 9], Terrains.MEADOW, 3, None]]
        self.center = [[0], Terrains.DEFAULT, 4, None]
        self.amount = 1
