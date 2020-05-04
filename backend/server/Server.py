from backend.server.Connection import Connection
from backend.command.CommandFactory import CommandFactory
from backend.game.Game import Game


class Server (Connection):

    def main(self):#server start
        self.game = Game()
        self.factory = CommandFactory()# for implementation
        self.run()

    async def analyze(self,data,websocket):
        command = self.factory.createCommand(self.game,data,websocket)
        sendBackJsonTab = command.execute()
        for data in sendBackJsonTab:
            for ws, message in data.items():
                ws.send(message)

