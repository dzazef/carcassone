from backend.tile.Tile25Start import Tile25


class Board:
    """Main class which is responsible for board and tiles in game"""

    def __init__(self):
        """Initialize attributes"""
        self.tile_matrix = [[None for i in range(150)] for i in range(150)]
        self.tile_matrix[75][75] = Tile25()

    def getTiles(self):
        """Return board in as array of tuples
        board = [(x1, y1, id1, rotate1, pawn1), (x2, y2, id2, rotate2, pawn2), ...]
        pawn = (id, x, y)"""
        board = []
        for i in range(len(self.tile_matrix)):
            for j in range(len(self.tile_matrix[0])):
                if self.tile_matrix[i][j] is not None:
                    board.append((i - 75, j - 75, self.tile_matrix[i][j].code7x7, self.tile_matrix[i][j].orientation,
                                  self.tile_matrix[i][j].pawns_in_7x7()))
        return board

    def putTile(self, tile, x, y):
        """Put tile on coordinates x, y"""
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
        """Return true if tile is already on board, false otherwise"""
        for i in range(len(self.tile_matrix)):
            for j in range(len(self.tile_matrix[0])):
                if self.tile_matrix[i][j] == tile:
                    return True
        return False

    def getTilePositions(self, tile):
        """Return [(x, y)], where x and y are coordinates on board"""
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

    def addFinalPoints(self, players):
        """Add points at the end of the game"""
        for i in range(len(self.tile_matrix)):
            for j in range(len(self.tile_matrix[0])):
                if self.tile_matrix[i][j] is not None:
                    awarded = self.tile_matrix[i][j].after_game()
                    for p in players:
                        if p.ifActive() and p.getId() in awarded:
                            p.addPoints(awarded[p.getId()])

    def __hasNeighbour(self, i, j):
        """Return true, if coordinates ixj has neighbour, false otherwise"""
        if i > 0 and self.tile_matrix[i - 1][j] is not None:
            return True
        if i < 149 and self.tile_matrix[i + 1][j] is not None:
            return True
        if j > 0 and self.tile_matrix[i][j - 1] is not None:
            return True
        if j < 149 and self.tile_matrix[i][j + 1] is not None:
            return True
        return False
