from TileMeadow import TileMeadow
from TileCastle import TileCastle
from TileRoad import TileRoad


class Tile10(TileMeadow, TileCastle, TileRoad):

    def __init__(self):
        super().__init__()
        self.sides = [([1, 2, 3, 10, 11, 12], Tile10.CASTLE, 1, None),
                      ([5, 8], Tile10.ROAD, 2, None),
                      ([4, 9], Tile10.MEADOW, 3, None),
                      ([6, 7], Tile10.MEADOW, 4, None)]
        self.center = ([0], Tile10.DEFAULT, 5, None)
        self.amount = 3
