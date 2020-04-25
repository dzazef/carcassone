from random import shuffle
from game.Board import Board
from backend import *


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

    def __setTileStack(self):
        self.__tileStack.extend([Tile1MonasteryMeadow.py for _ in range(4)])
        self.__tileStack.extend([Tile2MonasteryMeadowRoad.py for _ in range(2)])
        self.__tileStack.extend([Tile3Castle.py for _ in range(1)])
        self.__tileStack.extend([Tile4MeadowCastle.py for _ in range(3)])
        self.__tileStack.extend([Tile5MeadowCastleShield.py for _ in range(1)])
        self.__tileStack.extend([Tile6MeadowRoadCastle.py for _ in range(1)])
        self.__tileStack.extend([Tile7MeadowRoadCastleShield.py for _ in range(2)])
        self.__tileStack.extend([Tile8MeadowCastle.py for _ in range(3)])
        self.__tileStack.extend([Tile9MeadowCastleShield.py for _ in range(2)])
        self.__tileStack.extend([Tile10MeadowRoadCastle.py for _ in range(3)])
        self.__tileStack.extend([Tile11MeadowRoadCastleShield.py for _ in range(2)])
        self.__tileStack.extend([Tile12MeadowCastle.py for _ in range(1)])
        self.__tileStack.extend([Tile13MeadowCastleShield.py for _ in range(2)])
        self.__tileStack.extend([Tile14MeadowCastle.py for _ in range(2)])
        self.__tileStack.extend([Tile15MeadowCastle.py for _ in range(3)])
        self.__tileStack.extend([Tile16MeadowCastle.py for _ in range(5)])
        self.__tileStack.extend([Tile17MeadowRoadCastle.py for _ in range(3)])
        self.__tileStack.extend([Tile18MeadowRoadCastle.py for _ in range(3)])
        self.__tileStack.extend([Tile19MeadowRoadCastle.py for _ in range(3)])
        self.__tileStack.extend([Tile20MeadowRoadCastle.py for _ in range(3)])
        self.__tileStack.extend([Tile21MeadowRoad.py for _ in range(8)])
        self.__tileStack.extend([Tile22MeadowRoad.py for _ in range(9)])
        self.__tileStack.extend([Tile23MeadowRoad.py for _ in range(4)])
        self.__tileStack.extend([Tile24MeadowRoad.py for _ in range(1)])

        shuffle(self.__tileStack)
