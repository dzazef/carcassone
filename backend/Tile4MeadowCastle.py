from TileCastle import TileCastle
from TileMeadow import TileMeadow


class Tile4(TileCastle, TileMeadow):

    def __init__(self):
        super().__init__()
        self.sides = [([1, 2, 3, 4, 5, 6, 10, 11, 12], Tile4.CASTLE, 1, None),
                      ([7, 8, 9], Tile4.MEADOW, 2, None)]
        self.center = ([0], Tile4.DEFAULT, 3, None)
        self.amount = 3
