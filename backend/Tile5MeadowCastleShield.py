from Enums import Terrains, TileIDs
from TileCastleShield import TileCastleShield
from TileMeadow import TileMeadow


class Tile5(TileCastleShield, TileMeadow):

    id = TileIDs.TILE5

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3, 4, 5, 6, 10, 11, 12], Terrains.CASTLESHIELD, 1, None],
                      [[7, 8, 9], Terrains.MEADOW, 2, None]]
        self.center = [[0], Terrains.DEFAULT, 3, None]
        self.amount = 1
