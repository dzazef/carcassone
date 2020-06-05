from json import dumps
from operator import itemgetter

from Game import Game
from backend.command.Command import Command
from backend.command.JSONConstructor import JSONConstructor


class DisconnectCommand(Command):
    def __init__(self, game, data, websocket):
        super(DisconnectCommand, self).__init__(game, data)
        self.__websocket = websocket

    def execute(self):
        players = self._game.getPlayers()

        if self._game.getCurrPlayer() is None:
            # game has not been started yet, remove player and check, if all players are ready
            for player in players:
                if player.getWebsocket() == self.__websocket:
                    players.remove(player)
                    break

            if len(players) < 2 or False in [player.getReady() for player in players]:
                # not all players ready
                playersList = [[p.getId(), p.getColor(), p.getReady()] for p in players]
                json = {p.getWebsocket(): [dumps(JSONConstructor.players_info_json(
                    p.getId(), p.getColor(), p.getReady(), playersList))] for p in players}
            else:
                # all players ready, start game
                playersList = [[p.getId(), p.getColor(), p.getPoints(), p.getPawnsNumber()] for p in players]
                boardList = self._game.getBoard().getTiles()
                tilesLeft = self._game.getTilesLeftAmount()
                self._game.start()
                json = {p.getWebsocket(): [dumps(JSONConstructor.start_game(p.getId(), p.getColor(), p.getReady())),
                                           dumps(JSONConstructor.board_state(tilesLeft, playersList, boardList))]
                        for p in players}
        else:
            # game is running, set player.active to false and send info to other players or end game
            if self._game.getCurrPlayer().getWebsocket() == self.__websocket:
                self._game.nextTurn()

            for player in players:
                if player.getWebsocket() == self.__websocket:
                    player.setActive(False)

            # check, if only one player is active
            if sum(player.ifActive() for player in players) > 1:
                # more players are active
                playersList = [[p.getId(), p.getColor(), p.getPoints(), p.getPawnsNumber()] for p in players]
                boardList = self._game.getBoard().getTiles()
                tilesLeft = self._game.getTilesLeftAmount()

                json = {p.getWebsocket(): [dumps(JSONConstructor.board_state(tilesLeft, playersList, boardList))]
                        for p in players if p.ifActive()}
            else:
                # only one player is active, end game
                self._game.getBoard().addFinalPoints(players)

                winners = [[0, p.getId(), p.getPoints()] for p in players]
                sorted(winners, key=itemgetter(2))
                for i in range(len(players)):
                    winners[i][0] = i + 1
                json = {p.getWebsocket(): [dumps(JSONConstructor.end_game(winners))] for p in players if p.ifActive()}
                self._game.restart()
        return json
