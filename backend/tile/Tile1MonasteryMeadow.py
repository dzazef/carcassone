from backend.tile.AuxFunctions import merge_dicts_during_game, merge_dicts_after_game
from backend.tile.Enums import Terrains, TileIDs  # dziala
from backend.tile.TileMeadow import TileMeadow
from backend.tile.TileMonastery import TileMonastery


class Tile1(TileMeadow, TileMonastery):
    id = TileIDs.TILE1
    amount = 4

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], Terrains.MEADOW, 1, None]]
        self.center = [[0], Terrains.MONASTERY, 2, None]

        self.code7x7 = [
            [0, 2, 2, 2, 2, 2, 0],
            [2, 2, 2, 2, 2, 2, 2],
            [2, 2, 4, 4, 4, 2, 2],
            [2, 2, 4, 4, 4, 2, 2],
            [2, 2, 4, 4, 4, 2, 2],
            [2, 2, 2, 2, 2, 2, 2],
            [0, 2, 2, 2, 2, 2, 0]
        ]

    def after_move(self):  # returns dictionary {player: [points, pawns]}
        monastery = self.check_for_points_after_move_monastery()
        return monastery

    def after_game(self):  # returns dictionary {player: points]}
        monastery = self.check_for_points_after_game_monastery()
        meadow = self.check_for_points_after_game_meadow()
        return merge_dicts_after_game(monastery, meadow)
