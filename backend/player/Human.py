from backend.player.Player import Player


class Human(Player):
    """Class which is responsible for control humans"""

    def __init__(self, id, websocket, color):
        """"Initialize attributes"""
        super(Human, self).__init__(id, websocket, color)
