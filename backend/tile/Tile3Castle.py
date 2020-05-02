from backend.tile.Enums import Terrains, TileIDs
from backend.tile.TileCastleShield import TileCastleShield
from backend.tile.AuxFunctions import merge_dicts_during_game, merge_dicts_after_game


class Tile3(TileCastleShield):

    id = TileIDs.TILE3
    amount = 1

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], Terrains.CASTLESHIELD, 1, None]]
        self.center = [[0], Terrains.DEFAULT, 2, None]

    def after_move(self):  # returns dictionary {player: [points, pawns]}
        monastery = self.check_for_points_after_move_monastery()
        castle = self.check_for_points_after_move_castle()
        return merge_dicts_during_game(monastery, castle)

    def after_game(self):  # returns dictionary {player: points]}
        castle = self.check_for_points_after_game_castle()
        return castle
