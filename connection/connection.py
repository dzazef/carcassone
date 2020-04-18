import asyncio
import json
import logging
import websockets

logging.basicConfig()


class Player:
    def __init__(self, websocket, id, color):
        self.websocket = websocket
        self.id = id
        self.color = color
        self.ifReady = False

    def ready(self):
        self.ifReady = True


class Connection:
    def __init__(self):
        self.players = []

    def run(self):
        start_server = websockets.serve(self.connect, "localhost", 6789)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    async def connect(self, websocket, path):
        await self.register(websocket)
        try:
            await self.notify()
            async for message in websocket:
                data = json.loads(message)

                if data["type"] == "ready":
                    for player in self.players:
                        if str(player.id) == data["data"]["id"]:
                            player.ready()
                    await self.notify()
                else:
                    logging.error("unsupported event: {}", data)
        finally:
            await self.unregister(websocket)

    async def notify(self):
        if self.players:
            await asyncio.wait([player.websocket.send(self.newJson(player)) for player in self.players])

    async def register(self, websocket):
        self.players.append(Player(websocket, len(self.players) + 1, "green"))
        await self.notify()

    async def unregister(self, websocket):
        player = [p for p in self.players if p.websocket == websocket][0]
        self.players.remove(player)
        await self.notify()

    def newJson(self, player):
        return json.dumps({"type": "player_count", "data": {
            "me": {
                "id": player.id,
                "color": player.color,
                "ready": player.ifReady
            },
            "players": ' '.join(str(p.id) + str(p.color) +
                                str(p.ifReady) for p in self.players)
        }
                           })


connect = Connection()
connect.run()
