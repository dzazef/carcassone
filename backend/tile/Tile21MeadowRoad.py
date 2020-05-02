from backend.tile.Enums import Terrains, TileIDs
from backend.tile.TileRoad import TileRoad
from backend.tile.TileMeadow import TileMeadow
from backend.tile.AuxFunctions import merge_dicts_during_game, merge_dicts_after_game


class Tile21(TileRoad, TileMeadow):

    id = TileIDs.TILE21
    amount = 8

    def __init__(self):
        super().__init__()
        self.sides = [[[2, 8], Terrains.ROAD, 3, None],
                      [[3, 4, 5, 6, 7], Terrains.MEADOW, 1, None],
                      [[9, 10, 11, 12, 1], Terrains.MEADOW, 2, None]]
        self.center = [[0], Terrains.DEFAULT, 4, None]

    def after_move(self):
        monastery = self.check_for_points_after_move_monastery()
        road = self.check_for_points_after_move_road()
        return merge_dicts_during_game(monastery, road)

    def after_game(self):
        meadow = self.check_for_points_after_game_meadow()
        road = self.check_for_points_after_game_road()
        return merge_dicts_after_game(meadow, road)
