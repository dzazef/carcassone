from backend.tile.Enums import Terrains
from backend.tile.Tile import Tile


class TileMonastery(Tile):

    def check_for_points_after_game_monastery(self):
        result = {}  # dictionary- player: points
        i = self.center
        points = 1
        if i[1] == Terrains.MONASTERY:
            if i[3] is not None:
                j = self.upTile
                if j is not None:
                    points += 1
                    if j.leftTile is not None:
                        points += 1
                    if j.rightTile is not None:
                        points += 1
                j = self.downTile
                if j is not None:
                    points += 1
                    if j.leftTile is not None:
                        points += 1
                    if j.rightTile is not None:
                        points += 1
                j = self.leftTile
                if j is not None:
                    points += 1
                j = self.rightTile
                if j is not None:
                    points += 1
                result[i[3]] = points
                i[3] = None  # clear pawn
        return result
