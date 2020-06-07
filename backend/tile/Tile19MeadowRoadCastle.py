from backend.tile.AuxFunctions import merge_dicts_during_game, merge_dicts_after_game
from backend.tile.Enums import Terrains, TileIDs
from backend.tile.TileCastle import TileCastle
from backend.tile.TileMeadow import TileMeadow
from backend.tile.TileRoad import TileRoad


class Tile19(TileCastle, TileMeadow, TileRoad):
    id = TileIDs.TILE19
    amount = 3

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3], Terrains.CASTLE, 1, None],
                      [[4, 12], Terrains.MEADOW, 2, None],
                      [[6, 7], Terrains.MEADOW, 3, None],
                      [[9, 10], Terrains.MEADOW, 4, None],
                      [[11], Terrains.ROAD, 5, None],
                      [[5], Terrains.ROAD, 6, None],
                      [[8], Terrains.ROAD, 7, None]]
        self.center = [[0], Terrains.DEFAULT, 8, None]

        self.code7x7 = [
            [0, 1, 1, 1, 1, 1, 0],
            [2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2],
            [3, 3, 3, 5, 3, 3, 3],
            [2, 2, 2, 3, 2, 2, 2],
            [2, 2, 2, 3, 2, 2, 2],
            [0, 2, 2, 3, 2, 2, 0]
        ]

    def after_move(self):
        monastery = self.check_for_points_after_move_monastery()
        castle = self.check_for_points_after_move_castle()
        road = self.check_for_points_after_move_road()
        return merge_dicts_during_game(monastery, castle, road)

    def after_game(self):
        castle = self.check_for_points_after_game_castle()
        meadow = self.check_for_points_after_game_meadow()
        road = self.check_for_points_after_game_road()
        return merge_dicts_after_game(castle, meadow, road)
