from backend.tile.Enums import Terrains, TileIDs
from backend.tile.TileCastle import TileCastle
from backend.tile.TileMeadow import TileMeadow
from backend.tile.TileRoad import TileRoad
from backend.tile.AuxFunctions import merge_dicts_during_game, merge_dicts_after_game


class Tile18(TileCastle, TileMeadow, TileRoad):

    id = TileIDs.TILE18
    amount = 3

    def __init__(self):
        super().__init__()
        self.sides = [[[5, 8], Terrains.ROAD, 3, None],
                      [[1, 2, 3], Terrains.CASTLE, 1, None],
                      [[4, 9, 10, 11, 12], Terrains.MEADOW, 2, None],
                      [[6, 7], Terrains.MEADOW, 4, None]]
        self.center = [[0], Terrains.DEFAULT, 5, None]

        self.code7x7 = [
            [0, 1, 1, 1, 1, 1, 0],
            [2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 3, 3, 3, 3],
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
