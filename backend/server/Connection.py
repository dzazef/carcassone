import asyncio
import json
import logging
import websockets
from abc import ABC, abstractmethod

class Connection(ABC):
    def run(self):
        start_server = websockets.serve(self.connect, "localhost", 6789)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    async def connect(self, websocket, path):
        await self.register(websocket)
        try:
            async for message in websocket:
                incomingJson = json.loads(self,message)
                self.analyze(incomingJson)
        finally:
            #tworzenie jsona że ktos sie zerwal i wyslanie go do analyze - command factory
            await self.analyze(websocket)

    async def analyze(self,data,websocket):
        pass #abstract