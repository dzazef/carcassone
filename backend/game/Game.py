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

    # returns [(x, y)], where x and y are coordinates on board
    def getTilePositions(self, tile):
        result = []

        for boardTile in self.__board.getTiles():
            if boardTile.upTile is None and boardTile.fit_up(tile):
                result.append((boardTile.x, boardTile.y - 1))
            if boardTile.downTile is None and boardTile.fit_down(tile):
                result.append((boardTile.x, boardTile.y + 1))
            if boardTile.leftTile is None and boardTile.fit_left(tile):
                result.append((boardTile.x - 1, boardTile.y))
            if boardTile.rightTile is None and boardTile.fit_right(tile):
                result.append((boardTile.x + 1, boardTile.y))

        return result

    # returns [(x, y)], where x and y are coordinates on tile (7x7 representation)
    def getPawnPositions(self, tile):
        result = []

        for number in [placeInfo[0] for placeInfo in tile.offer_to_place_a_pawn()]:
            if 1 <= number <= 3:
                result.append([(0, 1 + number)])
            elif 4 <= number <= 6:
                result.append([(-2 + number, 6)])
            elif 7 <= number <= 9:
                result.append([(6, -number + 11)])
            elif 10 <= number <= 12:
                result.append([(-number + 14, 0)])

        return result

    def __setNextTile(self):
        for tile in self.__tileStack:
            for _ in range(4):
                if self.getTilePositions(tile):
                    self.__currTile = tile
                    return True
                tile.turn_clockwise()

        return False

    def __setTileStack(self):
        self.__tileStack.extend([tiles.Tile1()] * tiles.Tile1.amount)
        self.__tileStack.extend([tiles.Tile2()] * tiles.Tile2.amount)
        self.__tileStack.extend([tiles.Tile3()] * tiles.Tile3.amount)
        self.__tileStack.extend([tiles.Tile4()] * tiles.Tile4.amount)
        self.__tileStack.extend([tiles.Tile5()] * tiles.Tile5.amount)
        self.__tileStack.extend([tiles.Tile6()] * tiles.Tile6.amount)
        self.__tileStack.extend([tiles.Tile7()] * tiles.Tile7.amount)
        self.__tileStack.extend([tiles.Tile8()] * tiles.Tile8.amount)
        self.__tileStack.extend([tiles.Tile9()] * tiles.Tile9.amount)
        self.__tileStack.extend([tiles.Tile10()] * tiles.Tile10.amount)
        self.__tileStack.extend([tiles.Tile11()] * tiles.Tile11.amount)
        self.__tileStack.extend([tiles.Tile12()] * tiles.Tile12.amount)
        self.__tileStack.extend([tiles.Tile13()] * tiles.Tile13.amount)
        self.__tileStack.extend([tiles.Tile14()] * tiles.Tile14.amount)
        self.__tileStack.extend([tiles.Tile15()] * tiles.Tile15.amount)
        self.__tileStack.extend([tiles.Tile16()] * tiles.Tile16.amount)
        self.__tileStack.extend([tiles.Tile17()] * tiles.Tile17.amount)
        self.__tileStack.extend([tiles.Tile18()] * tiles.Tile18.amount)
        self.__tileStack.extend([tiles.Tile19()] * tiles.Tile19.amount)
        self.__tileStack.extend([tiles.Tile20()] * tiles.Tile20.amount)
        self.__tileStack.extend([tiles.Tile21()] * tiles.Tile21.amount)
        self.__tileStack.extend([tiles.Tile22()] * tiles.Tile22.amount)
        self.__tileStack.extend([tiles.Tile23()] * tiles.Tile23.amount)
        self.__tileStack.extend([tiles.Tile24()] * tiles.Tile24.amount)

        shuffle(self.__tileStack)
