import asyncio
import json
import logging
import websockets

logging.basicConfig()


class Player:
    def __init__(self, websocket, id):
        self.websocket = websocket
        self.id = id


class Connection:
    def __init__(self):
        self.players = []
        self.id = 0

    def run(self):
        start_server = websockets.serve(self.connect, "localhost", 6789)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    async def connect(self, websocket, path):
        await self.register(websocket)
        try:
            async for message in websocket:

                data = json.loads(message)
                #newJson, playersIdList = jakisObiekt.analyze(data)
                #send(newJson, playersIdList)

        finally:
            #tutaj trzeba powiedomic logikę gry że jednego gracza wywalilo, najprawdopodobniej równierz w unregister
            await self.unregister(websocket)


    async def register(self, websocket):
        self.players.append(Player(websocket, self.id))
        self.id+=1

    async def unregister(self, websocket):
        self.players = [player for player in self.players if player.websocket != websocket]
        #i tu wywolanie na game logic usuniecia gracza

connect = Connection()
connect.run()
