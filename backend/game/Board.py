from tile import Tile2, Tile3


class Board:
    def __init__(self):
        self.tile_matrix = [[None for i in range(150)] for i in range(150)]

    def getTiles(self):
        # board = [(x1, y1, id1, rotate1, pawn1), (x2, y2, id2, rotate2, pawn2), ...]
        # pawn = (id, x, y)
        tileList = list()
        for i in range(150):
            for j in range(150):
                if(self.tile_matrix[i][j] != None):
                    tile = self.tile_matrix[i][j]
                    tileList.append((i,j,tile.id,tile.orientation,None)) #TODO None >>> Pawn + tile.id wraca obiekt enum zamiast ciągu znaków
        return tileList

    def putTile(self, tile, x, y):
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