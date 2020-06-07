from json import dumps
from operator import itemgetter

from backend.command.Command import Command
from backend.command.JSONConstructor import JSONConstructor


class DisconnectCommand(Command):
    """Handle disconnection"""
    def __init__(self, game, data, websocket):
        """Initialize attributes"""
        super(DisconnectCommand, self).__init__(game, data)
        self.__websocket = websocket

    def execute(self):
        """If game hasn't started, remove player and
        check if game can start, return json for start game or updated player lobby
        else remove player and check if game can continue, return end game json or next tur json """
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
            for player in players:
                if player.getWebsocket() == self.__websocket:
                    player.setActive(False)

            # check, if more than one player is active
            if sum(player.ifActive() for player in players) > 1:
                # more players are active
                playersList = [[p.getId(), p.getColor(), p.getPoints(), p.getPawnsNumber()] for p in players]
                boardList = self._game.getBoard().getTiles()
                tilesLeft = self._game.getTilesLeftAmount()

                json = {p.getWebsocket(): [dumps(JSONConstructor.board_state(tilesLeft, playersList, boardList))]
                        for p in players if p.ifActive()}


                isPlaced = self._game.getBoard().isTileOnBoard(self._game.getCurrTile())
                if isPlaced:
                    self._game.nextTurn()
                else:
                    self._game.nextPlayer()

                possible_tile_places = self._game.getBoard().getTilePositions(self._game.getCurrTile())
                currPlayer = self._game.getCurrPlayer()
                json[currPlayer.getWebsocket()].append(dumps(JSONConstructor.tile_possible_places(
                    currPlayer.getId(),
                    self._game.getCurrTile().code7x7,
                    self._game.getCurrTile().orientation,
                    possible_tile_places
                )))
            else:
                # only one player is active, end game
                self._game.getBoard().addFinalPoints(players)

                winners = [[0, p.getId(), p.getPoints()] for p in players]
                winners = sorted(winners, key=itemgetter(2), reverse=True)
                for i in range(len(players)):
                    winners[i][0] = i + 1
                json = {p.getWebsocket(): [dumps(JSONConstructor.end_game(winners))] for p in players if p.ifActive()}
                self._game.restart()
        return json
