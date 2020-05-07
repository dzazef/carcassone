from backend.tile.Enums import Terrains, TileIDs
from backend.tile.TileMeadow import TileMeadow
from backend.tile.TileCastleShield import TileCastleShield
from backend.tile.TileRoad import TileRoad
from backend.tile.AuxFunctions import merge_dicts_during_game, merge_dicts_after_game


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

        self.code7x7 = [
            [6, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 2],
            [1, 1, 2, 2, 2, 2, 2],
            [1, 1, 2, 3, 3, 3, 3],
            [1, 1, 2, 3, 2, 2, 2],
            [1, 1, 2, 3, 2, 2, 2],
            [0, 2, 2, 3, 2, 2, 0]
        ]

    def after_move(self):
        monastery = self.check_for_points_after_move_monastery()
        castle = self.check_for_points_after_move_castle()
        road = self.check_for_points_after_move_road()
        if road == "not completed road":
            road = {}
        return merge_dicts_during_game(monastery, castle, road)

    def after_game(self):
        castle = self.check_for_points_after_game_castle()
        meadow = self.check_for_points_after_game_meadow()
        road = self.check_for_points_after_game_road()
        return merge_dicts_after_game(castle, meadow, road)
