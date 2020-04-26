from backend.tile.Enums import Terrains, TileIDs
from backend.tile.TileMeadow import TileMeadow
from backend.tile.TileMonastery import TileMonastery
from backend.tile.TileRoad import TileRoad


class Tile2(TileMeadow, TileMonastery, TileRoad):

    id = TileIDs.TILE2

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12], Terrains.MEADOW, 1, None],
                      [[8], Terrains.ROAD, 2, None]]
        self.center = [[0], Terrains.MONASTERY, 3, None]
        self.amount = 2
