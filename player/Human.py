from player import Player


class Human(Player):
    def __init__(self, id, websocket, color):
        super(Human, self).__init__(id, websocket, color)
