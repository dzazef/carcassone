from abc import ABC, abstractmethod
from backend.game.Game import Game


class Command:
    def __init__(self, game, data):
        self._game = game
        self._data = data

    @abstractmethod
    def execute(self):
        pass
