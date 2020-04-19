from Enums import Terrains
from TileRoad import TileRoad
from TileMeadow import TileMeadow


class Tile21(TileMeadow, TileRoad):

    def __init__(self):
        super().__init__()
        self.sides = [[[3, 4, 5, 6, 7], Terrains.MEADOW, 1, None],
                      [[9, 10, 11, 12, 1], Terrains.MEADOW, 2, None],
                      [[2, 8], Terrains.ROAD, 3, None]]
        self.center = [[0], Terrains.DEFAULT, 4, None]
        self.amount = 8
