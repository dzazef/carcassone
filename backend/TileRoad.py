from Tile import Tile
from Enums import Terrains


class TileRoad(Tile):

    def __init__(self):
        super().__init__()
        self.points = 1

    def points_for_road_after_move(self):
        score = {}
        for i in self.sides:
            if i[1] == Terrains.ROAD:
                dfs = self.dfs_start(i)
                for i in dfs:
                    if i == (None, None):
                        return "not completed roade"
                how_many_tiles = [j[0] for j in dfs]
                how_many_tiles2 = list(set(how_many_tiles))
                points = len(how_many_tiles2)

                players_list = [j[1][3] for j in dfs]
                counter2 = []
                occurence = []
                for i in players_list:
                    if i is not None and occurence.count(i) == 0:
                        occurence.append(i)
                        counter = players_list.count(i)
                        counter2.append((i, counter))
                print(counter2)
                if len(counter2) == 1:
                    score[counter2[0][0]] = points
                elif counter2[0][1] == counter2[len(counter2) - 1][1]:
                    for i in counter2:
                        score[i[0]] = points
                else:
                    score[counter2[0][0]] = points

        return score
