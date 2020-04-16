from TileCastleShield import TileCastleShield
from TileMeadow import TileMeadow


class Tile9(TileCastleShield, TileMeadow):

    def __init__(self):
        super().__init__()
        self.sides = [([1, 2, 3, 10, 11, 12], Tile9.CASTLESHIELD, 1, None),
                      ([4, 5, 6, 7, 8, 9], Tile9.MEADOW, 2, None)]
        self.center = ([0], Tile9.DEFAULT, 3, None)
        self.amount = 2
