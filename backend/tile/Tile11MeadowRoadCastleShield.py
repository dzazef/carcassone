from backend.tile.Enums import Terrains, TileIDs
from backend.tile.TileMeadow import TileMeadow
from backend.tile.TileCastleShield import TileCastleShield
from backend.tile.TileRoad import TileRoad


class Tile11(TileMeadow, TileCastleShield, TileRoad):

    id = TileIDs.TILE11
    amount = 2

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3, 10, 11, 12], Terrains.CASTLESHIELD, 1, None],
                      [[5, 8], Terrains.ROAD, 2, None],
                      [[4, 9], Terrains.MEADOW, 3, None],
                      [[6, 7], Terrains.MEADOW, 4, None]]
        self.center = [[0], Terrains.DEFAULT, 5, None]
