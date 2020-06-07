from backend.server.Connection import Connection
from backend.command.CommandFactory import CommandFactory
from backend.game.Game import Game


class Server (Connection):
    """Main Server class that inherits after connection,
     it calls commands and sends back information to clients"""
    def __init__(self):#server start
        """Initialize game, create factory, run connection"""
        self.game = Game()
        self.factory = CommandFactory()# for implementation
        self.run()

    async def analyze(self,data,websocket):
        """Gets json(data) from websocket,
        Creates command for that data and executes it
        sends back prepared inforamtion to all clients"""
        command = self.factory.createCommand(self.game,data,websocket)
        sendBackJsonTab = (await command).execute()
        for ws, messages in sendBackJsonTab.items():
            for message in messages:
                await ws.send(message)
