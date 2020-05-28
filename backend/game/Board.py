from backend.tile.Tile25Start import Tile25


class Board:
    def __init__(self):
        self.tile_matrix = [[None for i in range(150)] for i in range(150)]
        self.tile_matrix[75][75] = Tile25()

    def getTiles(self):
        # board = [(x1, y1, id1, rotate1, pawn1), (x2, y2, id2, rotate2, pawn2), ...]
        # pawn = (id, x, y)
        board = []
        for i in range(len(self.tile_matrix)):
            for j in range(len(self.tile_matrix[0])):
                if self.tile_matrix[i][j] is not None:
                    board.append((i-75, j-75, self.tile_matrix[i][j].code7x7, self.tile_matrix[i][j].orientation, self.tile_matrix[i][j].pawns_in_7x7()))
        return board

    def putTile(self, tile, x, y):
        x += 75
        y += 75
        if y-1 >= 0 and self.tile_matrix[x][y-1] != None:
            tile.leftTile = self.tile_matrix[x][y-1]
            (self.tile_matrix[x][y-1]).rightTile = tile
        if x-1 >= 0 and self.tile_matrix[x-1][y] != None:
            tile.upTile = self.tile_matrix[x-1][y]
            (self.tile_matrix[x-1][y]).downTile = tile
        if y+1 <= 149 and self.tile_matrix[x][y+1] != None:
            tile.rightTile = self.tile_matrix[x][y+1]
            (self.tile_matrix[x][y+1]).leftTile = tile
        if x+1 <= 149 and self.tile_matrix[x+1][y] != None:
            tile.downTile = self.tile_matrix[x+1][y]
            (self.tile_matrix[x+1][y]).uptTile = tile
        self.tile_matrix[x][y] = tile

    def putPawn(self, tile, color, x, y):
        pass

    # returns [(x, y)], where x and y are coordinates on board
    def getTilePositions(self, tile):
        result = []
        for i in range(len(self.tile_matrix)):
            for j in range(len(self.tile_matrix[0])):
                if self.tile_matrix[i][j] is not None:
                    if self.tile_matrix[i][j].upTile is None and self.tile_matrix[i][j].fit_up(tile):
                        result.append((i - 75, j - 1 - 75))
                    if self.tile_matrix[i][j].downTile is None and self.tile_matrix[i][j].fit_down(tile):
                        result.append((i - 75, j + 1 - 75))
                    if self.tile_matrix[i][j].leftTile is None and self.tile_matrix[i][j].fit_left(tile):
                        result.append((i - 1 - 75, j - 75))
                    if self.tile_matrix[i][j].rightTile is None and self.tile_matrix[i][j].fit_right(tile):
                        result.append((i + 1 - 75, j - 75))
        return result
