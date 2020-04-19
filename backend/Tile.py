# ekserymentalna klasa reprezentacji płytek
from Enums import Terrains


def reciprocal(num):
    rec1 = [1, 2, 3, 4, 5, 6]
    rec2 = [9, 8, 7, 12, 11, 10]
    for i, j in enumerate(rec1):
        if j == num:
            return rec2[i]
    for i, j in enumerate(rec2):
        if j == num:
            return rec1[i]
    return None


class Tile:

    #    1 2 3
    # 12       4
    # 11   0   5
    # 10       6
    #    9 8 7

    def __init__(self):
        # each member of the tuple containing connected edges type of terrain, id (internal), and player's pawn
        self.sides = [[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], Terrains.DEFAULT, 1, None]]
        self.center = [[0], Terrains.DEFAULT, 2, None]
        self.orientation = 0  # 0- standard, 1- once to the left, 2- twice to the left, 3- thrice to the left
        self.amount = 0

        self.upTile = None
        self.rightTile = None
        self.downTile = None
        self.leftTile = None

        self.points = 0
        self.penalty_points = 0

    def turn_clockwise(self):
        for i in self.sides:
            for j in range(len(i[0])):
                i[0][j] = (i[0][j] + 2) % 12 + 1
        self.orientation = (self.orientation - 1) % 4

    def turn_counterclockwise(self):
        for i in self.sides:
            for j in range(len(i[0])):
                i[0][j] = (i[0][j] - 4) % 12 + 1
        self.orientation = (self.orientation + 1) % 4

    def find_side(self, terrain):
        for i in self.sides:
            if terrain in i[0]:
                return i[1]
        return None

    def find_side_whole(self, terrain):
        for i in self.sides:
            if terrain in i[0]:
                return i
        return None

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
        neighbours = [(self, side)]  # (Tile, one of the sides)
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

    def place_a_pawn(self, position, player):
        pass

    def final_score(self, player):
        pass
