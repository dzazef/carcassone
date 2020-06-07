from abc import ABC, abstractmethod

from backend.game.Game import Game


class Command:
    """Abstract class created when we receive message from client"""

    def __init__(self, game, data):
        """Initialize attributes"""
        self._game = game
        self._data = data

    # returns dictionary {websocket: [json_in_string]}
    @abstractmethod
    def execute(self):
        """Executes instructions according to command type"""
        pass
