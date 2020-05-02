from backend.tile.Enums import Terrains, TileIDs
from backend.tile.TileCastleShield import TileCastleShield
from backend.tile.TileMeadow import TileMeadow
from backend.tile.TileRoad import TileRoad
from backend.tile.AuxFunctions import merge_dicts_during_game, merge_dicts_after_game


class Tile7(TileCastleShield, TileMeadow, TileRoad):

    id = TileIDs.TILE7
    amount = 2

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3, 4, 5, 6, 10, 11, 12], Terrains.CASTLESHIELD, 1, None],
                      [[7], Terrains.MEADOW, 2, None],
                      [[8], Terrains.ROAD, 3, None],
                      [[9], Terrains.MEADOW, 4, None]]
        self.center = [[0], Terrains.DEFAULT, 5, None]

    def after_move(self):  # returns dictionary {player: [points, pawns]}
        monastery = self.check_for_points_after_move_monastery()
        castle = self.check_for_points_after_move_castle()
        road = self.check_for_points_after_move_road()
        return merge_dicts_during_game(monastery, castle, road)

    def after_game(self):  # returns dictionary {player: points]}
        castle = self.check_for_points_after_game_castle()
        meadow = self.check_for_points_after_game_meadow()
        road = self.check_for_points_after_game_road()
        return merge_dicts_after_game(castle, meadow, road)
