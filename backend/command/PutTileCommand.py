from json import dumps
from backend.command.Command import Command
from backend.command.JSONConstructor import JSONConstructor


class PutTileCommand(Command):
    def __init__(self, game, data):
        super(PutTileCommand, self).__init__(game, data)

    def execute(self):
        self._game.getBoard().putTile(self._game.getCurrTile(), self._data['data']['x'], self._data['data']['y'])

        players = self._game.getPlayers()

        json = {p.getWebsocket(): [dumps(JSONConstructor.board_state(
            self._game.getTilesLeftAmount(),
            [[p.getId(), p.getColor(), p.getPoints(), p.getPawnsNumber()] for p in players],
            self._game.getBoard().getTiles()
        ))] for p in players if p.ifActive()}

        currPlayer = self._game.getCurrPlayer()
        json[currPlayer.getWebsocket()].append(dumps(JSONConstructor.put_pawn(
            currPlayer.getId(),
            self._game.getCurrTile().code7x7,
            self._game.getCurrTile().orientation,
            self._game.getPawnPositions()
            )))

        return json
