from Enums import Terrains
from TileCastle import TileCastle
from TileMeadow import TileMeadow


class Tile6(TileCastle, TileMeadow):

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3, 4, 5, 6, 10, 11, 12], Terrains.CASTLE, 1, None],
                      [[7], Terrains.MEADOW, 2, None],
                      [[8], Terrains.ROAD, 3, None],
                      [[9], Terrains.MEADOW, 4, None]]
        self.center = [[0], Terrains.DEFAULT, 5, None]
        self.amount = 1
