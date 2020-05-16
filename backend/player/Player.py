from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def __init__(self, id, websocket, color):
        self._id = id
        self._websocket = websocket
        self._color = color
        self._points = 0
        self._pawnsNumber = 8
        self._ready = False

    def getId(self):
        return self._id

    def getWebsocket(self):
        return self._websocket

    def getColor(self):
        return self._color

    def addPoints(self, points):
        self._points += points

    def getPoints(self):
        return self._points

    def getPawnsNumber(self):
        return self._pawnsNumber

    def setPawnsNumber(self, number):
        self._pawnsNumber = number

    def getReady(self):
        return self._ready

    def setReady(self, ready):
        self._ready = ready
