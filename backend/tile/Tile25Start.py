from backend.tile.AuxFunctions import merge_dicts_during_game, merge_dicts_after_game
from backend.tile.Enums import Terrains, TileIDs
from backend.tile.TileCastle import TileCastle
from backend.tile.TileMeadow import TileMeadow
from backend.tile.TileRoad import TileRoad


class Tile25(TileCastle, TileMeadow, TileRoad):
    id = TileIDs.TILESTART
    amount = 1

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3], Terrains.CASTLE, 1, None],
                      [[4, 12], Terrains.MEADOW, 2, None],
                      [[6, 7, 8, 9, 10], Terrains.MEADOW, 3, None],
                      [[5, 11], Terrains.ROAD, 4, None]]
        self.center = [[0], Terrains.DEFAULT, 5, None]

        self.code7x7 = [
            [0, 1, 1, 1, 1, 1, 0],
            [2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3, 3, 3],
            [2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2],
            [0, 2, 2, 2, 2, 2, 0]
        ]

    def after_move(self):
        monastery = self.check_for_points_after_move_monastery()
        road = self.check_for_points_after_move_road()
        castle = self.check_for_points_after_move_castle()
        return merge_dicts_during_game(monastery, road, castle)

    def after_game(self):
        meadow = self.check_for_points_after_game_meadow()
        road = self.check_for_points_after_game_road()
        castle = self.check_for_points_after_game_castle()
        return merge_dicts_after_game(meadow, road, castle)
