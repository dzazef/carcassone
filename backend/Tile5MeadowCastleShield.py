from TileCastleShield import TileCastleShield
from TileMeadow import TileMeadow


class Tile5(TileCastleShield, TileMeadow):

    def __init__(self):
        super().__init__()
        self.sides = [([1, 2, 3, 4, 5, 6, 10, 11, 12], Tile5.CASTLESHIELD, 1, None),
                      ([7, 8, 9], Tile5.MEADOW, 2, None)]
        self.center = ([0], Tile5.DEFAULT, 3, None)
        self.amount = 1
