from itertools import count, filterfalse
from backend.command.Command import Command
from backend.player.Human import Human
from backend.command.JSONConstructor import JSONConstructor


class JoinCommand(Command):
    def __init__(self, game, data, websocket):
        super(JoinCommand, self).__init__(game, data)
        self.__websocket = websocket
        self.__colors = ['blue', 'yellow', 'green', 'red', 'black']

    def execute(self):
        players = self._game.getPlayers()

        for player in players:
            self.__colors.remove(player.getColor())
        color = self.__colors[0]

        # find the smallest positive id number not in list
        id = next(filterfalse([player.getId() for player in players].__contains__, count(1)))

        players.append(Human(id, self.__websocket, color))

        # return json
        playersList = [[p.getId(), p.getColor(), p.getReady()] for p in players]
        return {p.getWebsocket(): JSONConstructor.players_info_json(p.getId(), p.getColor(), p.getReady(), playersList)
                for p in players}
