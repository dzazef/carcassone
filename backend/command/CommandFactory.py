from backend.command.DisconnectCommand import DisconnectCommand
from backend.command.EndTurnCommand import EndTurnCommand
from backend.command.JoinCommand import JoinCommand
from backend.command.PutTileCommand import PutTileCommand
from backend.command.ReadyCommand import ReadyCommand
from backend.command.RotateTileCommand import RotateTileCommand


class CommandFactory:
    """Crates command type appropiate for received message"""

    def __init__(self):
        pass

    async def createCommand(self, game, data, websocket):
        """Return command type appropiate for received message"""
        if data["type"] == "join":
            return JoinCommand(game, data, websocket)
        elif data["type"] == "ready":
            return ReadyCommand(game, data)
        elif data["type"] == "rotate_tile":
            return RotateTileCommand(game, data)
        elif data["type"] == "put_tile":
            return PutTileCommand(game, data)
        elif data["type"] == "end_turn":
            return EndTurnCommand(game, data)
        elif data["type"] == "disconnect":
            return DisconnectCommand(game, data, websocket)
