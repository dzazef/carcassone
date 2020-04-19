from Enums import Terrains
from TileCastleShield import TileCastleShield
from TileMeadow import TileMeadow
from TileRoad import TileRoad


class Tile7(TileCastleShield, TileMeadow, TileRoad):

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3, 4, 5, 6, 10, 11, 12], Terrains.CASTLESHIELD, 1, None],
                      [[7], Terrains.MEADOW, 2, None],
                      [[8], Terrains.ROAD, 3, None],
                      [[9], Terrains.MEADOW, 4, None]]
        self.center = [[0], Terrains.DEFAULT, 5, None]
        self.amount = 2
