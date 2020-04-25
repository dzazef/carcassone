from abc import ABC, abstractmethod

class Connection(ABC):
    def __init__(self):
        self.id = 0

    def run(self):
        pass #for implementation

    async def connect(self, websocket, path):
        pass #for implementation

    async def analyze(self):
        pass #abstract