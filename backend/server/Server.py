from backend.server.Connection import Connection
from backend.command.CommandFactory import CommandFactory
from backend.game.Game import Game


class Server (Connection):

    def __init__(self):#server start
        self.game = Game()
        self.factory = CommandFactory()# for implementation
        self.run()

    async def analyze(self,data,websocket):
        command = self.factory.createCommand(self.game,data,websocket)
        sendBackJsonTab = (await command).execute()
        for ws, messages in sendBackJsonTab.items():
            for message in messages:
                await ws.send(message)
