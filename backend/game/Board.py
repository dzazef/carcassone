from backend.tile.Tile25Start import Tile25


class Board:
    def __init__(self):
        self.tile_matrix = [[None for i in range(150)] for i in range(150)]
        self.tile_matrix[75][75] = Tile25()

    def printself(self):
        print('------')
        for i in range(len(self.tile_matrix)):
            for j in range(len(self.tile_matrix[0])):
                if self.tile_matrix[i][j] is not None:
                    print('x: {0}, y: {1}, type: {2}, sides: {3}, orientation: {4}, udlr: {5} {6} {7} {8}'
                          .format(i - 75,
                                  j - 75,
                                  type(self.tile_matrix[i][j]).__name__,
                                  self.tile_matrix[i][j].sides,
                                  self.tile_matrix[i][j].orientation,
                                  self.tile_matrix[i][j].upTile,
                                  self.tile_matrix[i][j].downTile,
                                  self.tile_matrix[i][j].leftTile,
                                  self.tile_matrix[i][j].rightTile))
        print('------')

    def getTiles(self):
        # board = [(x1, y1, id1, rotate1, pawn1), (x2, y2, id2, rotate2, pawn2), ...]
        # pawn = (id, x, y)
        board = []
        for i in range(len(self.tile_matrix)):
            for j in range(len(self.tile_matrix[0])):
                if self.tile_matrix[i][j] is not None:
                    board.append((i - 75, j - 75, self.tile_matrix[i][j].code7x7, self.tile_matrix[i][j].orientation,
                                  self.tile_matrix[i][j].pawns_in_7x7()))
        return board

    def putTile(self, tile, x, y):
        x += 75
        y += 75
        if y - 1 >= 0 and self.tile_matrix[x][y - 1] != None:
            tile.leftTile = self.tile_matrix[x][y - 1]
            (self.tile_matrix[x][y - 1]).rightTile = tile
        if x - 1 >= 0 and self.tile_matrix[x - 1][y] != None:
            tile.downTile = self.tile_matrix[x - 1][y]
            (self.tile_matrix[x - 1][y]).upTile = tile
        if y + 1 <= 149 and self.tile_matrix[x][y + 1] != None:
            tile.rightTile = self.tile_matrix[x][y + 1]
            (self.tile_matrix[x][y + 1]).leftTile = tile
        if x + 1 <= 149 and self.tile_matrix[x + 1][y] != None:
            tile.upTile = self.tile_matrix[x + 1][y]
            (self.tile_matrix[x + 1][y]).downTile = tile
        self.tile_matrix[x][y] = tile

    def isTileOnBoard(self, tile):
        for i in range(len(self.tile_matrix)):
            for j in range(len(self.tile_matrix[0])):
                if self.tile_matrix[i][j] == tile:
                    return True
        return False

    # returns [(x, y)], where x and y are coordinates on board
    def getTilePositions(self, tile):
        result = []
        for i in range(len(self.tile_matrix)):
            for j in range(len(self.tile_matrix[0])):
                if self.tile_matrix[i][j] is None and self.__hasNeighbour(i, j):
                    if (self.tile_matrix[i + 1][j] is None or self.tile_matrix[i + 1][j].fit_down(tile)) \
                            and (self.tile_matrix[i - 1][j] is None or self.tile_matrix[i - 1][j].fit_up(tile)) \
                            and (self.tile_matrix[i][j - 1] is None or self.tile_matrix[i][j - 1].fit_right(tile)) \
                            and (self.tile_matrix[i][j + 1] is None or self.tile_matrix[i][j + 1].fit_left(tile)):
                        result.append((i - 75, j - 75))
        return result

    # add points at the end of the game
    def addFinalPoints(self, players):
        for i in range(len(self.tile_matrix)):
            for j in range(len(self.tile_matrix[0])):
                if self.tile_matrix[i][j] is not None:
                    awarded = self.tile_matrix[i][j].after_game()
                    for p in players:
                        if p.ifActive() and p.getId() in awarded:
                            p.addPoints(awarded[p.getId()])

    def __hasNeighbour(self, i, j):
        if i > 0 and self.tile_matrix[i - 1][j] is not None:
            return True
        if i < 149 and self.tile_matrix[i + 1][j] is not None:
            return True
        if j > 0 and self.tile_matrix[i][j - 1] is not None:
            return True
        if j < 149 and self.tile_matrix[i][j + 1] is not None:
            return True
        return False
