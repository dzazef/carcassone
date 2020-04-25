from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def __init__(self, id, websocket, color):
        self.__id = id
        self.__websocket = websocket
        self.__color = color
        self._points = 0
        self.__pawns = 8
        self.__ready = False

    def getWebsocket(self):
        pass

    def getReady(self):
        pass

    def setReady(self):
        pass

    def getPawns(self):
        pass

    def setPawns(self):
        pass

    def addPoints(self):
        pass
