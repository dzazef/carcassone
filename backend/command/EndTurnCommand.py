from backend.command.Command import Command


class EndTurnCommand(Command):
    def __init__(self, game, data):
        super(EndTurnCommand, self).__init__(game, data)

    def execute(self):
        pass
