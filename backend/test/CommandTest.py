import unittest
from backend.command.JoinCommand import JoinCommand
from backend.command.ReadyCommand import ReadyCommand
from backend.game.Game import Game


class CommandTest(unittest.TestCase):
    def test_beginGame(self):
        game = Game()

        command1 = JoinCommand(game, {}, 'websocket1')
        self.assertDictEqual(command1.execute(),
                             {'websocket1': {
                                 'type': 'player_lobby',
                                 'data': {
                                     'me': {
                                         'id': 1,
                                         'color': 'blue',
                                         'ready': False
                                     },
                                     'players': [{'id': 1, 'color': 'blue', 'ready': False}]
                                 }
                             }
                             }, "wrong player_lobby json")

        command2 = JoinCommand(game, {}, 'websocket2')
        command2.execute()

        command3 = ReadyCommand(game, {'type': 'ready', 'data': {'id': 1}})
        command3.execute()

        command4 = JoinCommand(game, {}, 'websocket3')
        command4.execute()

        command5 = ReadyCommand(game, {'type': 'ready', 'data': {'id': 2}})
        command5.execute()

        command6 = ReadyCommand(game, {'type': 'ready', 'data': {'id': 3}})
        json = command6.execute()

        self.assertDictEqual(json['websocket1'], {'type': 'start', 'data': {}}, "wrong start json")
        self.assertDictEqual(json['websocket2'], {'type': 'start', 'data': {}}, "wrong start json")
        self.assertDictEqual(json['websocket3'], {'type': 'start', 'data': {}}, "wrong start json")


if __name__ == '__main__':
    unittest.main()
