class Board:
    def __init__(self):
        self.tile_matrix = [[None for i in range(150)] for i in range(150)]

    def getTiles(self):
        return self.tile_matrix

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