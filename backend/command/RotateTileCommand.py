from json import dumps

from backend.command.JSONConstructor import JSONConstructor
from backend.command.Command import Command


class RotateTileCommand(Command):
    def __init__(self, game, data):
        super(RotateTileCommand, self).__init__(game, data)

    def execute(self):
        players = self._game.getPlayers()
        rotation = self._data['data']['tile']['rotate']
        currTile = self._game.getCurrTile()
        while currTile.orientation != rotation:
            currTile.turn_clockwise()
        places = self._game.getBoard().getTilePositions(currTile)
        json = {self._game.getCurrPlayer().getWebsocket(): [[dumps(JSONConstructor.tile_possible_places(self._game.getCurrPlayer().getId(), currTile.code7x7, currTile.orientation, places))]]}
        return json
