from backend.tile.Tile import Tile
from backend.tile.Enums import Terrains
import operator


class TileRoad(Tile):

    def __init__(self):
        super().__init__()
        self.points = 1

    def check_for_points_after_move_road(self):
        score = {}
        x = 0
        for i in self.sides:
            if i[1] == Terrains.ROAD:
                dfs = self.dfs_start(i)
                for i in dfs:
                    if i == (None, None):
                        return "not completed road"
                how_many_tiles = [j[0] for j in dfs]
                how_many_tiles2 = list(set(how_many_tiles))
                points = len(how_many_tiles2)

                players_list = [j[1][3] for j in dfs]
                counter2 = []
                occurence = []
                for l in players_list:
                    if l is not None and occurence.count(l) == 0:
                        occurence.append(l)
                        counter = players_list.count(l)
                        counter2.append((l, counter))
                counter2.sort(key=operator.itemgetter(1), reverse=True)
                score[counter2[0][0]] = [points, counter2[0][1]]
                for c in range(1, len(counter2)):
                    if counter2[c][1] == counter2[0][1]:
                        score[counter2[c][0]] = [points, counter2[c][1]]
                    else:
                        score[counter2[c][0]] = [0, counter2[c][1]]
                for j in dfs:  # clear pawns
                    j[1][3] = None
        return score

    def check_for_points_after_game_road(self):
        score = {}
        for i in self.sides:
            if i[1] == Terrains.ROAD and i[3] is not None:
                dfs = self.dfs_start(i)
                dfs = [road for road in dfs if road != (None, None)]
                how_many_tiles = [j[0] for j in dfs]
                how_many_tiles2 = list(set(how_many_tiles))
                points = len(how_many_tiles2)

                players_list = [j[1][3] for j in dfs]
                counter2 = []
                occurence = []
                for l in players_list:
                    if l is not None and occurence.count(l) == 0:
                        occurence.append(l)
                        counter = players_list.count(l)
                        counter2.append((l, counter))
                counter2.sort(key=operator.itemgetter(1), reverse=True)
                score[counter2[0][0]] = points
                for c in range(1, len(counter2)):
                    if counter2[c][1] == counter2[0][1]:
                        score[counter2[c][0]] = points
                    else:
                        score[counter2[c][0]] = 0
                for j in dfs:  # clear pawns # do we have to though?
                    j[1][3] = None
        return score
