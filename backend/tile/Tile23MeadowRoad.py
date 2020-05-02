from backend.tile.Enums import Terrains, TileIDs
from backend.tile.TileMeadow import TileMeadow
from backend.tile.TileRoad import TileRoad


class Tile23(TileMeadow, TileRoad):

    id = TileIDs.TILE23
    amount = 4

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3, 4, 12], Terrains.MEADOW, 1, None],
                      [[6, 7], Terrains.MEADOW, 2, None],
                      [[9, 10], Terrains.MEADOW, 3, None],
                      [[11], Terrains.ROAD, 4, None],
                      [[5], Terrains.ROAD, 5, None],
                      [[8], Terrains.ROAD, 6, None]]
        self.center = [[0], Terrains.DEFAULT, 7, None]
