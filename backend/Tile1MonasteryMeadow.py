from Enums import Terrains
from TileMeadow import TileMeadow
from TileMonastery import TileMonastery


class Tile1(TileMeadow, TileMonastery):

    def __init__(self):
        super().__init__()
        self.sides = [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], Terrains.MEADOW, 1, None)]
        self.center = ([0], Terrains.MONASTERY, 2, None)
        self.amount = 4
