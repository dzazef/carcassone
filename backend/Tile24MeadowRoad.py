from Enums import Terrains, TileIDs
from TileMeadow import TileMeadow
from TileRoad import TileRoad


class Tile19(TileMeadow, TileRoad):

    id = TileIDs.TILE24

    def __init__(self):
        super().__init__()
        self.sides = [[[3, 4], Terrains.MEADOW, 1, None],
                      [[6, 7], Terrains.MEADOW, 2, None],
                      [[9, 10], Terrains.MEADOW, 3, None],
                      [[12, 1], Terrains.MEADOW, 4, None],
                      [[2], Terrains.ROAD, 5, None],
                      [[5], Terrains.ROAD, 6, None],
                      [[8], Terrains.ROAD, 7, None],
                      [[11], Terrains.ROAD, 8, None]]
        self.center = [[0], Terrains.DEFAULT, 9, None]
        self.amount = 1
