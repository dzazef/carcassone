from backend.command.Command import Command


class ReadyCommand(Command):
    def __init__(self, game, data):
        super(ReadyCommand, self).__init__(game, data)

    def execute(self):
        pass
