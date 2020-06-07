import asyncio
import json
import logging
import websockets
from abc import ABC, abstractmethod

class Connection(ABC):
    """Abstract class that manages connection with websockets"""
    def run(self):
        """Start server connection"""
        self.incomingJson = None
        start_server = websockets.serve(self.connect, "localhost", 3030)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    async def connect(self, websocket, path):
        """Take messages from websocket and analyze them
        if connection closes create disconnect json"""
        self.incomingJson = None
        try:
            async for message in websocket:
                self.incomingJson = json.loads(message)
                await self.analyze(self.incomingJson,websocket)
        except:
            pass
        finally:
            disconnectJson = {'type': 'disconnect'}
            if(self.incomingJson["type"] != "disconnect"):
                await self.analyze(disconnectJson, websocket)
            self.incomingJson = {'type': 'disconnected'}

    async def analyze(self,data,websocket):
        """Implemented in Server.py"""
        pass