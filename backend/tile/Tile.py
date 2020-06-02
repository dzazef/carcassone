from backend.tile.Enums import Terrains


def reciprocal(num):  # returns position on the opposite side of a tile
    rec1 = [1, 2, 3, 4, 5, 6]
    rec2 = [9, 8, 7, 12, 11, 10]
    for i, j in enumerate(rec1):
        if j == num:
            return rec2[i]
    for i, j in enumerate(rec2):
        if j == num:
            return rec1[i]
    return None


def other_reciprocal(num):  # translates pawn position from backend representation to 7x7 matrix tuple (row, column)
    rec = [(3, 3), (0, 1), (0, 3), (0, 5), (1, 6), (3, 6), (5, 6), (6, 5), (6, 3), (6, 1), (5, 0), (3, 0), (1, 0)]
    if num in range(0, 13):
        return rec[num]
    return None


def reverse_other_reciprocal(num):  # translates pawn position from 7x7 matrix tuple to backend representation
    rec = [(3, 3), (0, 1), (0, 3), (0, 5), (1, 6), (3, 6), (5, 6), (6, 5), (6, 3), (6, 1), (5, 0), (3, 0), (1, 0)]
    for i, j in enumerate(rec):
        if j == num:
            return i
    return None


class Tile:

    #    1 2 3
    # 12       4
    # 11   0   5
    # 10       6
    #    9 8 7
    amount = 0  # how many of this kind of tile is in the deck

    def __init__(self):
        # each member of the tuple containing connected edges type of terrain, id (internal), and player's pawn
        # sides is a list of all connected sections of terrain on the tile, each member of this list is a list of length
        # of 4, which has the following contents:
        # sides[_][0] - a list of all positions a given side spans e.g. [1, 2, 3] means it covers the entire top of
        # a tile
        # sides[_][1] - kind of terrain defined in Enums.Terrains e.g. Terrains.MEADOW or Terrains.CASTLE
        # sides[_][2] - internal ID, all sides (and center) must have other internal ID to differentiate between
        # seperate sections of same terrain e.g. two sides of Terrain.MEADOW that are not connected, so they must be
        # distinguished in some other way
        # sides[_][3] - player ID, or None if no player has a pawn on this side
        self.sides = [[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], Terrains.DEFAULT, 1, None]]
        # center is the same as sides, but has only one member and it can only be a Terrain.Monastery or nothing
        # (Terrain.DEFAILT)
        self.center = [[0], Terrains.DEFAULT, 2, None]
        self.orientation = 0  # 0- standard, 1- once to the left, 2- twice to the left, 3- thrice to the left

        # representation as 7x7 matrix for frontend
        self.code7x7 = [[0, 0, 0, 0, 0, 0, 0] for _ in range(0, 7)]

        # neighbours of the tile
        self.upTile = None
        self.rightTile = None
        self.downTile = None
        self.leftTile = None

        # points given for each section of a castle depending on whether it is finished or not
        # ( Probably redundant can be deleted )
        self.points = 0
        self.penalty_points = 0

    # representation of pawns on the tile in 7x7 matrix
    def pawns_in_7x7(self):
        players = []  # list of (playerID, row, column (row, column on 7x7 tile))
        i = self.center
        if i[3] is not None:
            j = other_reciprocal(i[0][0])
            players.append((i[3], j[0], j[1]))
        for i in self.sides:
            if i[3] is not None:
                j = other_reciprocal(i[0][0])
                players.append((i[3], j[0], j[1]))

        return players

    def turn_clockwise(self):
        self.code7x7 = list(zip(*self.code7x7[::-1]))

        for i in self.sides:
            for j in range(len(i[0])):
                i[0][j] = (i[0][j] + 2) % 12 + 1
        self.orientation = (self.orientation - 1) % 4

    def turn_counterclockwise(self):
        self.code7x7 = list(zip(*self.code7x7))[::-1]

        for i in self.sides:
            for j in range(len(i[0])):
                i[0][j] = (i[0][j] - 4) % 12 + 1
        self.orientation = (self.orientation + 1) % 4

    # returns a kind of terrain, where the given position is
    def find_side(self, position):
        for i in self.sides:
            if position in i[0]:
                return i[1]
        return None

    # returns a side, where the given position is
    def find_side_whole(self, position):
        for i in self.sides:
            if position in i[0]:
                return i
        return None

    # ( Not used, can be deleted )
    def find_side_internal(self, terrain):
        for i in self.sides:
            if terrain in i[0]:
                return i[2]
        return None

    def fit_up(self, other):  # can I place the other tile on top of this one?
        if (
                self.find_side(1) == other.find_side(9)
                and self.find_side(2) == other.find_side(8)
                and self.find_side(3) == other.find_side(7)
        ):
            return True
        return False

    def fit_right(self, other):  # can I place the other tile right of this one?
        if (
                self.find_side(4) == other.find_side(12)
                and self.find_side(5) == other.find_side(11)
                and self.find_side(6) == other.find_side(10)
        ):
            return True
        return False

    def fit_down(self, other):  # can I place the other tile below this one?
        if (
                self.find_side(9) == other.find_side(1)
                and self.find_side(8) == other.find_side(2)
                and self.find_side(7) == other.find_side(3)
        ):
            return True
        return False

    def fit_left(self, other):  # can I place the other tile left of this one?
        if (
                self.find_side(12) == other.find_side(4)
                and self.find_side(11) == other.find_side(5)
                and self.find_side(10) == other.find_side(6)
        ):
            return True
        return False

    def dfs_start(self, side):  # depth-first search
        neighbours = [(self, side)]  # returns list of tuples (Tile, one of the sides)
        self.dfs(side, neighbours)
        return neighbours

    def dfs(self, side, neighbours):
        for i in side[0]:
            if i in range(1, 4):
                if self.upTile is not None:
                    newelem = (self.upTile, self.upTile.find_side_whole(reciprocal(i)))
                    if newelem not in neighbours:
                        neighbours.append(newelem)
                        self.upTile.dfs(newelem[1], neighbours)
                else:
                    neighbours.append((None, None))
            if i in range(4, 7):
                if self.rightTile is not None:
                    newelem = (self.rightTile, self.rightTile.find_side_whole(reciprocal(i)))
                    if newelem not in neighbours:
                        neighbours.append(newelem)
                        self.rightTile.dfs(newelem[1], neighbours)
                else:
                    neighbours.append((None, None))
            if i in range(7, 10):
                if self.downTile is not None:
                    newelem = (self.downTile, self.downTile.find_side_whole(reciprocal(i)))
                    if newelem not in neighbours:
                        neighbours.append(newelem)
                        self.downTile.dfs(newelem[1], neighbours)
                else:
                    neighbours.append((None, None))
            if i in range(10, 13):
                if self.leftTile is not None:
                    newelem = (self.leftTile, self.leftTile.find_side_whole(reciprocal(i)))
                    if newelem not in neighbours:
                        neighbours.append(newelem)
                        self.leftTile.dfs(newelem[1], neighbours)
                else:
                    neighbours.append((None, None))

    def offer_to_place_a_pawn(self):
        available = [(i[0][0], i[1]) for i in self.sides
                     if i[1] != Terrains.DEFAULT  # all sides where terrain is not DEFAULT (0)
                     and not ["Pawn detected" for j in self.dfs_start(i) if j[1] is not None and j[1][3] is not None]]  # and have no pawns
        if self.center[1] != Terrains.DEFAULT and self.center[3] is None:
            available.append((self.center[0][0], self.center[1]))
        return available  # returns list of tuples (position, terrain)

    # places a pawn on the given position
    # position: number from 0 to 12 returned as first element in tuple returned from offer_to_place_a_pawn
    # position may also be a tuple in 7x7 matrix and it gets translated
    def place_a_pawn(self, position, player):
        if isinstance(position, int) and 0 <= position <= 12:  # if backend representation
            pass
        elif isinstance(position, tuple) and list(map(type, position)) == [int, int]:  # # if frontend representation
            position = reverse_other_reciprocal(position)
        else:
            return

        if position == 0:
            self.center[3] = player
            return
        side = self.find_side_whole(position)
        if side is not None:
            side[3] = player
        else:
            print("Couldn't place a pawn here due to an error!")


    def count_neighbours(self):
        neighbours = 0
        j = self.upTile
        if j is not None:
            neighbours += 1
            if j.leftTile is not None:
                neighbours += 1
            if j.rightTile is not None:
                neighbours += 1
        j = self.downTile
        if j is not None:
            neighbours += 1
            if j.leftTile is not None:
                neighbours += 1
            if j.rightTile is not None:
                neighbours += 1
        j = self.leftTile
        if j is not None:
            neighbours += 1
        j = self.rightTile
        if j is not None:
            neighbours += 1
        return neighbours

    # returns a list of tiles around it
    def neighbours(self):
        neighbours = []
        j = self.upTile
        if j is not None:
            neighbours.append(j)
            if j.leftTile is not None:
                neighbours.append(j.leftTile)
            if j.rightTile is not None:
                neighbours.append(j.rightTile)
        j = self.downTile
        if j is not None:
            neighbours.append(j)
            if j.leftTile is not None:
                neighbours.append(j.leftTile)
            if j.rightTile is not None:
                neighbours.append(j.rightTile)
        j = self.leftTile
        if j is not None:
            neighbours.append(j)
        j = self.rightTile
        if j is not None:
            neighbours.append(j)
        return neighbours

    # if placed check if any surrounding tile has a monastery and if it's its last neigbour, award points
    def check_for_points_after_move_monastery(self):  # ad hoc solution, may be refractored
        from backend.tile.TileMonastery import TileMonastery
        result = {}
        n = self.neighbours()
        n.append(self)  # can also be already finished
        for i in n:
            if isinstance(i, TileMonastery) and i.center[3] is not None and i.count_neighbours() == 8:  # and is instance of TileMonastery ?
                result[i.center[3]] = [9, 1]
                i.center[3] = None  # clear pawn
        return result


