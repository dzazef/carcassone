from collections import Counter
from backend.tile.Enums import Terrains
from backend.tile.Tile import Tile


def neigbouring(side):
    if side == 1:
        return 12, 2
    if side == 12:
        return 11, 1
    return side - 1, side + 1


class TileMeadow(Tile):

    def check_for_points_after_move_meadow(self):  # not used but left on purpose, if ever used mistakenly
        return {}

    def check_for_points_after_game_meadow(self):  # awards points and then removes pawns
        # neighours of castles work on simple rules: terrain 3 neighbours 2 and 4 etc.
        # should have individual dfs that on each tile searches adjecent castles and whether they are completed
        result = {}  # dictionary- player: points
        for i in self.sides:  # check all areas
            if i[1] == Terrains.MEADOW:  # if it's the area we want
                if i[3] is not None:
                    whole_meadow = self.dfs_start(i)
                    whole_meadow = [value for value in whole_meadow if value != (None, None)]  # delete all (None, None)

                    players = [j[1][3] for j in whole_meadow]  # extract players from that list
                    counter = Counter(players)  # count pawns of each player in a structure
                    if None in counter:
                        del counter[None]  # delete None as it is not a player
                    counter2 = counter.most_common()
                    while len(counter2) > 1:  # all with highest number of pawns get points
                        if counter2[0][1] != counter2[-1][1]:
                            counter2 = counter2[:-1]
                        else:
                            break

                    castles = []
                    for j in whole_meadow:
                        for k in j[1][0]:  # j[1][0] = [1, 2, 4 .. ]
                            neigbour1, neigbour2 = neigbouring(k)
                            if j[0].find_side(neigbour1) == Terrains.CASTLE:
                                castle = j[0].dfs_start(j[0].find_side_whole(neigbour1))
                                if (None, None) not in castle:
                                    castles.append(castle)
                            if j[0].find_side(neigbour2) == Terrains.CASTLE:
                                castle = j[0].dfs_start(j[0].find_side_whole(neigbour2))
                                if (None, None) not in castle:
                                    castles.append(castle)
                    for j in castles:
                        j.sort(key=lambda x: (id(x[0]), x[1][2]))  # sorts by: (id of a tile, internal id of side)

                    nodupcastles = []
                    for elem in castles:
                        if elem not in nodupcastles:
                            nodupcastles.append(elem)

                    for j in counter2:
                        if j[0] in result:
                            result[j[0]] += len(nodupcastles) * 3
                        elif len(nodupcastles) != 0:  # no need to report 0 points
                            result[j[0]] = len(nodupcastles) * 3

                    for j in whole_meadow:  # clear pawns
                        j[1][3] = None

        return result
