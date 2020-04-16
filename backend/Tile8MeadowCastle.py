from TileCastle import TileCastle
from TileMeadow import TileMeadow


class Tile8(TileCastle, TileMeadow):

    def __init__(self):
        super().__init__()
        self.sides = [([1, 2, 3, 10, 11, 12], Tile8.CASTLE, 1, None),
                      ([4, 5, 6, 7, 8, 9], Tile8.MEADOW, 2, None)]
        self.center = ([0], Tile8.DEFAULT, 3, None)
        self.amount = 3
