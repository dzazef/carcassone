from random import shuffle
from backend.game.Board import Board
import backend.tile as tiles


class Game:
    def __init__(self):
        self.__players = []
        self.__board = Board()
        self.__tileStack = []
        self.__setTileStack()
        self.__currPlayer = None
        self.__currTile = None

    def getPlayers(self):
        return self.__players

    def getCurrPlayer(self):
        return self.__currPlayer

    def start(self):
        self.__currPlayer = self.__players[0]
        self.__setNextTile()

    # it sets currPlayer and currTile
    # return true, if next turn is possible, false otherwise
    def nextTurn(self):
        self.__currPlayer = self.__players[(self.__players.index(self.__currPlayer) + 1) % len(self.__players)]
        self.__tileStack.remove(self.__currTile)
        return self.__setNextTile()

    def getCurrTile(self):
        return self.__currTile

    def getBoard(self):
        return self.__board

    def __setNextTile(self):
        for tile in self.__tileStack:
            for _ in range(4):
                if self.__board.getTilePositions(tile):
                    self.__currTile = tile
                    return True
                tile.turn_clockwise()

        return False

    def __setTileStack(self):  # to change, tile's number will be in tile class as static value
        self.__tileStack.extend([tiles.Tile1() for _ in range(4)])
        self.__tileStack.extend([tiles.Tile2() for _ in range(2)])
        self.__tileStack.extend([tiles.Tile3() for _ in range(1)])
        self.__tileStack.extend([tiles.Tile4() for _ in range(3)])
        self.__tileStack.extend([tiles.Tile5() for _ in range(1)])
        self.__tileStack.extend([tiles.Tile6() for _ in range(1)])
        self.__tileStack.extend([tiles.Tile7() for _ in range(2)])
        self.__tileStack.extend([tiles.Tile8() for _ in range(3)])
        self.__tileStack.extend([tiles.Tile9() for _ in range(2)])
        self.__tileStack.extend([tiles.Tile10() for _ in range(3)])
        self.__tileStack.extend([tiles.Tile11() for _ in range(2)])
        self.__tileStack.extend([tiles.Tile12() for _ in range(1)])
        self.__tileStack.extend([tiles.Tile13() for _ in range(2)])
        self.__tileStack.extend([tiles.Tile14() for _ in range(2)])
        self.__tileStack.extend([tiles.Tile15() for _ in range(3)])
        self.__tileStack.extend([tiles.Tile16() for _ in range(5)])
        self.__tileStack.extend([tiles.Tile17() for _ in range(3)])
        self.__tileStack.extend([tiles.Tile18() for _ in range(3)])
        self.__tileStack.extend([tiles.Tile19() for _ in range(3)])
        self.__tileStack.extend([tiles.Tile20() for _ in range(3)])
        self.__tileStack.extend([tiles.Tile21() for _ in range(8)])
        self.__tileStack.extend([tiles.Tile22() for _ in range(9)])
        self.__tileStack.extend([tiles.Tile23() for _ in range(4)])
        self.__tileStack.extend([tiles.Tile24() for _ in range(1)])

        shuffle(self.__tileStack)
