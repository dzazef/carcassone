from backend.tile.AuxFunctions import merge_dicts_during_game, merge_dicts_after_game
from backend.tile.Enums import Terrains, TileIDs
from backend.tile.TileCastle import TileCastle
from backend.tile.TileMeadow import TileMeadow


class Tile14(TileCastle, TileMeadow):
    id = TileIDs.TILE14
    amount = 2

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3], Terrains.CASTLE, 1, None],
                      [[10, 11, 12], Terrains.CASTLE, 2, None],
                      [[4, 5, 6, 7, 8, 9], Terrains.MEADOW, 3, None]]
        self.center = [[0], Terrains.DEFAULT, 4, None]

        self.code7x7 = [
            [0, 1, 1, 1, 1, 1, 0],
            [1, 2, 2, 2, 2, 2, 2],
            [1, 2, 2, 2, 2, 2, 2],
            [1, 2, 2, 2, 2, 2, 2],
            [1, 2, 2, 2, 2, 2, 2],
            [1, 2, 2, 2, 2, 2, 2],
            [0, 2, 2, 2, 2, 2, 0]
        ]

    def after_move(self):
        monastery = self.check_for_points_after_move_monastery()
        castle = self.check_for_points_after_move_castle()
        return merge_dicts_during_game(monastery, castle)

    def after_game(self):
        castle = self.check_for_points_after_game_castle()
        meadow = self.check_for_points_after_game_meadow()
        return merge_dicts_after_game(castle, meadow)
