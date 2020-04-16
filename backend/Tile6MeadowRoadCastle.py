from TileCastle import TileCastle
from TileMeadow import TileMeadow


class Tile6(TileCastle, TileMeadow):

    def __init__(self):
        super().__init__()
        self.sides = [([1, 2, 3, 4, 5, 6, 10, 11, 12], Tile6.CASTLE, 1, None),
                      ([7], Tile6.MEADOW, 2, None),
                      ([8], Tile6.ROAD, 3, None),
                      ([9], Tile6.MEADOW, 4, None)]
        self.center = ([0], Tile6.DEFAULT, 5, None)
        self.amount = 1
