import unittest
from backend.command.JoinCommand import JoinCommand
from backend.command.ReadyCommand import ReadyCommand
from backend.game.Game import Game


class CommandTest(unittest.TestCase):
    def test_beginGame(self):
        game = Game()

        command1 = JoinCommand(game, {}, 'websocket1')
        self.assertDictEqual(command1.execute(),
                             {'websocket1': ['{"type": "player_lobby", '
                                             '"data": {'
                                             '"me": {'
                                             '"id": 1, '
                                             '"color": "blue", '
                                             '"ready": false'
                                             '}, '
                                             '"lobby": [{"id": 1, "color": "blue", "ready": false}]}}']},
                             "wrong lobby_info json")

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

        self.assertEqual(json['websocket1'][0],
                         '{"type": "start", "data": {"me": {"id": 1, "color": "blue", "ready": true}}}',
                         "wrong start json")

        self.assertEqual(json['websocket2'][0],
                         '{"type": "start", "data": {"me": {"id": 2, "color": "yellow", "ready": true}}}',
                         "wrong start json")

        self.assertEqual(json['websocket3'][0],
                         '{"type": "start", "data": {"me": {"id": 3, "color": "purple", "ready": true}}}',
                         "wrong start json")


if __name__ == '__main__':
    unittest.main()
