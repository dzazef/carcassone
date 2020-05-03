from backend.command.Command import Command


class JoinCommand(Command):
    def __init__(self, game, data):
        super(JoinCommand, self).__init__(game, data)

    def execute(self):
        pass
