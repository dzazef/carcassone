from TileMeadow import TileMeadow
from TileMonastery import TileMonastery
from TileRoad import TileRoad


class Tile2(TileMeadow, TileMonastery, TileRoad):

    def __init__(self):
        super().__init__()
        self.sides = [([1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12], Tile2.MEADOW, 1, None), ([8], Tile2.ROAD, 2, None)]
        self.center = ([0], Tile2.MONASTERY, 3, None)
