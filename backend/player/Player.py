from abc import ABC, abstractmethod


class Player(ABC):
    """Class which is responsible for control player"""

    @abstractmethod
    def __init__(self, id, websocket, color):
        """"Initialize attributes"""
        self._id = id
        self._websocket = websocket
        self._color = color
        self._points = 0
        self._pawnsNumber = 8
        self._ready = False
        self._active = True

    def getId(self):
        """Return id"""
        return self._id

    def getWebsocket(self):
        """Return websocket"""
        return self._websocket

    def getColor(self):
        """Return color"""
        return self._color

    def addPoints(self, points):
        """Add new points"""
        self._points += points

    def getPoints(self):
        """Return points number"""
        return self._points

    def getPawnsNumber(self):
        """Return pawns number"""
        return self._pawnsNumber

    def setPawnsNumber(self, number):
        """Set pawns number"""
        self._pawnsNumber = number

    def getReady(self):
        """Return true, if player is ready, false otherwise"""
        return self._ready

    def setReady(self, ready):
        """Set attributes 'ready'"""
        self._ready = ready

    def ifActive(self):
        """Return true, if player is active, false otherwise"""
        return self._active

    def setActive(self, active):
        """Set attributes 'active'"""
        self._active = active
