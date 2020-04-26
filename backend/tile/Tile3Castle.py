from Enums import Terrains, TileIDs
from TileCastleShield import TileCastleShield


class Tile3(TileCastleShield):

    id = TileIDs.TILE3

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], Terrains.CASTLESHIELD, 1, None]]
        self.center = [[0], Terrains.DEFAULT, 2, None]
        self.amount = 1
