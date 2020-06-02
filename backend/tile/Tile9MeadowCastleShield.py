from backend.tile.Enums import Terrains, TileIDs
from backend.tile.TileCastleShield import TileCastleShield
from backend.tile.TileMeadow import TileMeadow
from backend.tile.AuxFunctions import merge_dicts_during_game, merge_dicts_after_game


class Tile9(TileCastleShield, TileMeadow):

    id = TileIDs.TILE9
    amount = 2

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3, 10, 11, 12], Terrains.CASTLESHIELD, 1, None],
                      [[4, 5, 6, 7, 8, 9], Terrains.MEADOW, 2, None]]
        self.center = [[0], Terrains.DEFAULT, 3, None]

        self.code7x7 = [
            [6, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 2],
            [1, 1, 1, 1, 1, 2, 2],
            [1, 1, 1, 1, 2, 2, 2],
            [1, 1, 1, 2, 2, 2, 2],
            [1, 1, 2, 2, 2, 2, 2],
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
