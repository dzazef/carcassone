from backend.command.Command import Command


class RotateTileCommand(Command):
    def __init__(self, game, data):
        super(RotateTileCommand, self).__init__(game, data)

    def execute(self):
        pass
