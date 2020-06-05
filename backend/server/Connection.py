import asyncio
import json
import logging
import websockets
from abc import ABC, abstractmethod

class Connection(ABC):
    def run(self):
        self.incomingJson = None
        start_server = websockets.serve(self.connect, "localhost", 3030)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    async def connect(self, websocket, path):
        self.incomingJson = None
        try:
            async for message in websocket:
                self.incomingJson = json.loads(message)
                await self.analyze(self.incomingJson,websocket)
        except:
            pass
        finally:
            disconnectJson = {'type': 'disconnect'}# tworzenie jsona że ktos sie zerwal i wyslanie go do analyze - command factory
            if(self.incomingJson["type"] != "disconnect"): # zabezpieczenie przed podwójnym wykonaniem disconnecta
                await self.analyze(disconnectJson, websocket)
            self.incomingJson = {'type': 'disconnected'}#jezeli ktos wyjdzie noramalnie to incoming json bedzie disconnect, a potem ktos sie zerwie to nic sie nie stanie

    async def analyze(self,data,websocket):
        pass #abstract