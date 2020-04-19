from Tile import Tile
from Enums import Terrains
from collections import Counter


class TileCastle(Tile):  # tutaj cała logika zamków, czyli jak naliczają punkty

    def __init__(self):
        super().__init__()
        self.points = 2

    def check_for_points_after_move(self):
        result = {}  # dictionary- player: points
        for i in self.sides:  # check all areas
            if i[1] == Terrains.CASTLE:  # if it's the area we want
                whole_castle = self.dfs_start(i)  # search adjecent tiles to get the whole structure
                if (None, None) not in whole_castle:  # no (None, None) records means the castle is completed
                    # count points
                    tiles = [j[0] for j in whole_castle]
                    tilesnodup = list(set(tiles))
                    points = 0
                    for j in tilesnodup:
                        points += j.points

                    players = [j[1][3] for j in whole_castle]  # extract players from that list
                    counter = Counter(players)  # count pawns of each player in a structure
                    del counter[None]  # delete None as it is not a player
                    counter2 = counter.most_common()
                    while len(counter2) > 1:  # all with highest number of pawns get points
                        if counter2[0][1] != counter2[-1][1]:
                            counter2 = counter2[:-1]
                        else:
                            break
                    for j in counter2:
                        if j[0] in result:
                            result[j[0]] += points
                        else:
                            result[j[0]] = points
        return result

