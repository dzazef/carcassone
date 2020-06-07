from random import shuffle

import backend.tile as tiles
from backend.game.Board import Board
from backend.tile.Tile import other_reciprocal


class Game:
    """Main class which is responsible for control board, tiles and players"""

    def __init__(self):
        """"Initialize attributes"""
        self.__players = []
        self.__board = Board()
        self.__tileStack = []
        self.__setTileStack()
        self.__currPlayer = None
        self.__currTile = None

    def restart(self):
        """Reset attributes"""
        self.__players = []
        self.__board = Board()
        self.__tileStack = []
        self.__setTileStack()
        self.__currPlayer = None
        self.__currTile = None

    def getPlayers(self):
        """Return array of players"""
        return self.__players

    def getCurrPlayer(self):
        """Return current player"""
        return self.__currPlayer

    def start(self):
        """Start game, set current player and current file"""
        self.__currPlayer = self.__players[0]
        self.__setNextTile()

    def nextPlayer(self):
        """Set next active player as current player"""
        index = (self.__players.index(self.__currPlayer) + 1) % len(self.__players)
        while not self.__players[index].ifActive():
            index = (index + 1) % len(self.__players)
        self.__currPlayer = self.__players[index]

    # it sets currPlayer, currTile and add new points
    # return true, if next turn is possible, false otherwise
    def nextTurn(self):
        """Set currPlayer, currTile and add new points.
        Return true, if next turn is possible, false otherwise"""
        # add points to players
        awarded = self.__currTile.after_move()
        for p in self.__players:
            if p.ifActive() and p.getId() in awarded:
                p.setPawnsNumber(p.getPawnsNumber() + awarded[p.getId()][1])
                p.addPoints(awarded[p.getId()][0])

        # set currPlayers
        self.nextPlayer()

        # set currTile
        self.__tileStack.remove(self.__currTile)
        return self.__setNextTile()

    def getCurrTile(self):
        """Return current tile"""
        return self.__currTile

    def getBoard(self):
        """Return board object"""
        return self.__board

    def getTilesLeftAmount(self):
        """Return amount of tiles remaining"""
        return len(self.__tileStack)

    def getPawnPositions(self):
        """Return [(x, y)], where x and y are coordinates on tile (7x7 representation)"""
        return [other_reciprocal(n) for n in [place[0] for place in self.__currTile.offer_to_place_a_pawn()]]

    def __setNextTile(self):
        """Set current tile.
        Return true, if is tile to place on board, false otherwise"""
        for tile in self.__tileStack:
            for _ in range(4):
                if self.__board.getTilePositions(tile):
                    self.__currTile = tile
                    return True
                tile.turn_clockwise()

        return False

    def __setTileStack(self):
        """Set tile stack"""
        self.__tileStack.extend([tiles.Tile1() for _ in range(tiles.Tile1.amount)])
        self.__tileStack.extend([tiles.Tile2() for _ in range(tiles.Tile2.amount)])
        self.__tileStack.extend([tiles.Tile3() for _ in range(tiles.Tile3.amount)])
        self.__tileStack.extend([tiles.Tile4() for _ in range(tiles.Tile4.amount)])
        self.__tileStack.extend([tiles.Tile5() for _ in range(tiles.Tile5.amount)])
        self.__tileStack.extend([tiles.Tile6() for _ in range(tiles.Tile6.amount)])
        self.__tileStack.extend([tiles.Tile7() for _ in range(tiles.Tile7.amount)])
        self.__tileStack.extend([tiles.Tile8() for _ in range(tiles.Tile8.amount)])
        self.__tileStack.extend([tiles.Tile9() for _ in range(tiles.Tile9.amount)])
        self.__tileStack.extend([tiles.Tile10() for _ in range(tiles.Tile10.amount)])
        self.__tileStack.extend([tiles.Tile11() for _ in range(tiles.Tile11.amount)])
        self.__tileStack.extend([tiles.Tile12() for _ in range(tiles.Tile12.amount)])
        self.__tileStack.extend([tiles.Tile13() for _ in range(tiles.Tile13.amount)])
        self.__tileStack.extend([tiles.Tile14() for _ in range(tiles.Tile14.amount)])
        self.__tileStack.extend([tiles.Tile15() for _ in range(tiles.Tile15.amount)])
        self.__tileStack.extend([tiles.Tile16() for _ in range(tiles.Tile16.amount)])
        self.__tileStack.extend([tiles.Tile17() for _ in range(tiles.Tile17.amount)])
        self.__tileStack.extend([tiles.Tile18() for _ in range(tiles.Tile18.amount)])
        self.__tileStack.extend([tiles.Tile19() for _ in range(tiles.Tile19.amount)])
        self.__tileStack.extend([tiles.Tile20() for _ in range(tiles.Tile20.amount)])
        self.__tileStack.extend([tiles.Tile21() for _ in range(tiles.Tile21.amount)])
        self.__tileStack.extend([tiles.Tile22() for _ in range(tiles.Tile22.amount)])
        self.__tileStack.extend([tiles.Tile23() for _ in range(tiles.Tile23.amount)])
        self.__tileStack.extend([tiles.Tile24() for _ in range(tiles.Tile24.amount)])

        shuffle(self.__tileStack)
