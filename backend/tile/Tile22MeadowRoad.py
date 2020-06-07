from backend.tile.AuxFunctions import merge_dicts_during_game, merge_dicts_after_game
from backend.tile.Enums import Terrains, TileIDs
from backend.tile.TileMeadow import TileMeadow
from backend.tile.TileRoad import TileRoad


class Tile22(TileMeadow, TileRoad):
    id = TileIDs.TILE22
    amount = 9

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3, 4, 5, 6, 7, 12], Terrains.MEADOW, 1, None],
                      [[8, 11], Terrains.ROAD, 2, None],
                      [[9, 10], Terrains.MEADOW, 3, None]]
        self.center = [[0], Terrains.DEFAULT, 4, None]

        self.code7x7 = [
            [0, 2, 2, 2, 2, 2, 0],
            [2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2],
            [3, 3, 3, 3, 2, 2, 2],
            [2, 2, 2, 3, 2, 2, 2],
            [2, 2, 2, 3, 2, 2, 2],
            [0, 2, 2, 3, 2, 2, 0]
        ]

    def after_move(self):
        monastery = self.check_for_points_after_move_monastery()
        road = self.check_for_points_after_move_road()
        return merge_dicts_during_game(monastery, road)

    def after_game(self):
        meadow = self.check_for_points_after_game_meadow()
        road = self.check_for_points_after_game_road()
        return merge_dicts_after_game(meadow, road)
