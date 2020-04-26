from Enums import Terrains, TileIDs
from TileRoad import TileRoad
from TileMeadow import TileMeadow


class Tile22(TileMeadow, TileRoad):

    id = TileIDs.TILE22

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3, 4, 5, 6, 7, 12], Terrains.MEADOW, 1, None],
                      [[8, 11], Terrains.ROAD, 2, None],
                      [[9, 10], Terrains.MEADOW, 3, None]]
        self.center = [[0], Terrains.DEFAULT, 4, None]
        self.amount = 9
