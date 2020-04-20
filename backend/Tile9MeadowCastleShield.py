from Enums import Terrains, TileIDs
from TileCastleShield import TileCastleShield
from TileMeadow import TileMeadow


class Tile9(TileCastleShield, TileMeadow):

    id = TileIDs.TILE9

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3, 10, 11, 12], Terrains.CASTLESHIELD, 1, None],
                      [[4, 5, 6, 7, 8, 9], Terrains.MEADOW, 2, None]]
        self.center = [[0], Terrains.DEFAULT, 3, None]
        self.amount = 2
