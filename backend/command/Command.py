from abc import ABC, abstractmethod
from backend.game.Game import Game


class Command:
    def __init__(self, game, data):
        self._game = game
        self._data = data

    # returns dictionary {websocket: [json_in_string]}
    @abstractmethod
    def execute(self):
        pass
