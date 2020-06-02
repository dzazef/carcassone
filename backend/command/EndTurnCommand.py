from json import dumps
from operator import itemgetter

from backend.command.JSONConstructor import JSONConstructor
from backend.command.Command import Command


class EndTurnCommand(Command):
    def __init__(self, game, data):
        super(EndTurnCommand, self).__init__(game, data)

    def execute(self):
        currTile = self._game.getCurrTile()
        pawnCount = self._game.getCurrPlayer().getPawnsNumber()
        position = (self._data['data']['pawn_info']['x'],self._data['data']['pawn_info']['y'])
        if self._data['data']['pawn_placed'] == "True" and pawnCount > 0: # stawiamy piona
            self._game.getCurrPlayer().setPawnsNumber(pawnCount - 1)
            currTile.place_a_pawn(position,
                                  self._game.getCurrPlayer().getId())
        nextTurn = self._game.nextTurn()
        players = self._game.getPlayers()

        if nextTurn:
            json = {p.getWebsocket(): [dumps(JSONConstructor.board_state(
                self._game.getTilesLeftAmount(),
                [[p.getId(), p.getColor(), p.getPoints(), p.getPawnsNumber()] for p in players],
                self._game.getBoard().getTiles()
            ))] for p in players if p.ifActive()}

            possible_tile_places = self._game.getBoard().getTilePositions(self._game.getCurrTile())
            currPlayer = self._game.getCurrPlayer()
            json[currPlayer.getWebsocket()].append(dumps(JSONConstructor.tile_possible_places(
                currPlayer.getId(),
                self._game.getCurrTile().code7x7,
                self._game.getCurrTile().orientation,
                possible_tile_places
            )))
        else: # end the game | winners = [(place1, id1, points1), (place2, id2, points2)]
            winners = [[0,p.getId(),p.getPoints()] for p in players]
            sorted(winners, key=itemgetter(2))
            for i in range(len(players)):
                winners[i][0] = i+1
            json = {p.getWebsocket(): [dumps(JSONConstructor.end_game(winners))] for p in players}
        return json
