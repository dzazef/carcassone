from TileCastleShield import TileCastleShield
from TileMeadow import TileMeadow


class Tile7(TileCastleShield, TileMeadow):

    def __init__(self):
        super().__init__()
        self.sides = [([1, 2, 3, 4, 5, 6, 10, 11, 12], Tile7.CASTLESHIELD, 1, None),
                      ([7], Tile7.MEADOW, 2, None),
                      ([8], Tile7.ROAD, 3, None),
                      ([9], Tile7.MEADOW, 4, None)]
        self.center = ([0], Tile7.DEFAULT, 5, None)
        self.amount = 2
