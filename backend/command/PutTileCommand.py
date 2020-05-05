from backend.command.Command import Command


class PutTileCommand(Command):
    def __init__(self, game, data):
        super(PutTileCommand, self).__init__(game, data)

    def execute(self):
        pass
