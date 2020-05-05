from backend.command.Command import Command
from backend.command.JSONConstructor import JSONConstructor


class ReadyCommand(Command):
    def __init__(self, game, data):
        super(ReadyCommand, self).__init__(game, data)

    def execute(self):
        playerId = self._data['data']['id']
        players = self._game.getPlayers()

        for player in players:
            if player.getId() == playerId:
                player.setReady(True)

        if False in [player.getReady() for player in players]:
            # not all players ready
            playersList = [[p.getId(), p.getColor(), p.getReady()] for p in players]
            json = {p.getWebsocket(): JSONConstructor.players_info_json(p.getId(), p.getColor(),
                                                                        p.getReady(), playersList)for p in players}
        else:
            # all players ready, start game
            self._game.start()
            json = {p.getWebsocket(): JSONConstructor.start_game() for p in players}
            # to add to json info about board

        return json
