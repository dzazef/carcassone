from itertools import count, filterfalse
from json import dumps
from backend.command.Command import Command
from backend.player.Human import Human
from backend.command.JSONConstructor import JSONConstructor


class JoinCommand(Command):
    def __init__(self, game, data, websocket):
        super(JoinCommand, self).__init__(game, data)
        self.__websocket = websocket
        self.__colors = ['blue', 'yellow', 'purple', 'red', 'black']

    def execute(self):
        if self._game.getCurrPlayer() is None:
            # game hasn't started yet, add player
            players = self._game.getPlayers()

            for player in players:
                self.__colors.remove(player.getColor())
            color = self.__colors[0]

            # find the smallest positive id number not in list
            id = next(filterfalse([player.getId() for player in players].__contains__, count(1)))

            players.append(Human(id, self.__websocket, color))

            # create json
            playersList = [[p.getId(), p.getColor(), p.getReady()] for p in players]
            json = {p.getWebsocket(): [dumps(JSONConstructor.players_info_json(
                p.getId(), p.getColor(), p.getReady(), playersList))] for p in players}
        else:
            # game has already started, send information about being late
            json = {self.__websocket: {'type': 'belated'}}

        return json
