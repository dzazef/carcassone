from backend.tile.Enums import Terrains, TileIDs
from backend.tile.TileMeadow import TileMeadow
from backend.tile.TileMonastery import TileMonastery
from backend.tile.TileRoad import TileRoad
from backend.tile.AuxFunctions import merge_dicts_during_game, merge_dicts_after_game


class Tile2(TileMeadow, TileMonastery, TileRoad):

    id = TileIDs.TILE2
    amount = 2

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12], Terrains.MEADOW, 1, None],
                      [[8], Terrains.ROAD, 2, None]]
        self.center = [[0], Terrains.MONASTERY, 3, None]

    def after_move(self):  # returns dictionary {player: [points, pawns]}
        monastery = self.check_for_points_after_move_monastery()
        road = self.check_for_points_after_move_road()
        return merge_dicts_during_game(monastery, road)

    def after_game(self):  # returns dictionary {player: points]}
        monastery = self.check_for_points_after_game_monastery()
        meadow = self.check_for_points_after_game_meadow()
        return merge_dicts_after_game(monastery, meadow)
