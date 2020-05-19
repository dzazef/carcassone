from json import dumps
from operator import itemgetter

import JSONConstructor
from backend.command.Command import Command


class EndTurnCommand(Command):
    def __init__(self, game, data):
        super(EndTurnCommand, self).__init__(game, data)

    def execute(self):
        nextTurn = self._game.nextTurn()
        players = self._game.getPlayers()
        if nextTurn:
            pass
        else: # end the game | winners = [(place1, id1, points1), (place2, id2, points2)]
            winners = [(0,p.getId(),p.getPoints()) for p in players]
            sorted(winners, key=itemgetter(2))
            for i in range(len(players)):
                winners[i][0] = i+1
            json = {p.getWebsocket(): [dumps(JSONConstructor.end_game(winners))] for p in players}
        return json
