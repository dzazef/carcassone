class JSONConstructor:

    @staticmethod
    def players_info_json(your_id, your_color, ready, players_list):
        # players_list = [(id1, color1, ready1), (id2, color2, ready2), ...]
        json1 = {
            "type": "player_lobby",
            "data": {
                "me": {
                    "id": your_id,
                    "color": your_color,
                    "ready": ready
                },
                "lobby": []
            }
        }

        player_json = []
        for i in range(0, len(players_list)):
            player = {"id": players_list[i][0], "color": players_list[i][1], "ready": players_list[i][2]}
            player_json.append(player)

        json1["data"]["lobby"] = player_json
        return json1

    @staticmethod
    def start_game(your_id, your_color, ready):
        json2 = {
            "type": "start",
            "data": {
                "me": {
                    "id": your_id,
                    "color": your_color,
                    "ready": ready
                }
            }
        }
        return json2

    @staticmethod
    def board_state(tiles_left, players_list, board_list):
        # players_list = [(id1, color1, points1, pawns_left1), (id2, color2, points2, pawns_left2), ...]
        # board = [(x1, y1, id1, rotate1, pawn1), (x2, y2, id2, rotate2, pawn2), ...]
        # pawn = (id, x, y)
        json3 = {
            "type": "board",
            "data": {
                "tiles_left": tiles_left,
                "players": [],
                "board": []
            }
        }

        player_json = []
        for i in range(0, len(players_list)):
            player = {"id": players_list[i][0], "color": players_list[i][1], "points": players_list[i][2], "pawns_left": players_list[i][3]}
            player_json.append(player)

        json3["data"]["players"] = player_json

        board_json = []
        for i in range(0, len(board_list)):
            board1 = {"x": board_list[i][0],
                      "y": board_list[i][1],
                      "id": board_list[i][2],
                      "rotate": board_list[i][3]
                      }

            if board_list[i][4]:
                board1["pawn"] = {
                    "id": board_list[i][4][0],
                    "x": board_list[i][4][1],
                    "y": board_list[i][4][2]
                }

            board_json.append(board1)

        json3["data"]["board"] = board_json
        return json3

    @staticmethod
    def tile_possible_places(iD, tile_id, rotate, places):
        # places = [(x1, y1), (x2, y2), ...]
        json4 = {
            "type": "turn_info",
            "data": {
                "id": iD,
                "tile": {
                    "id": tile_id,
                    "rotate": rotate
                },
                "possible_places": [],
            }
        }

        board_json = []
        for i in range(0, len(places)):
            board = {"x": places[i][0], "y": places[i][1]}
            board_json.append(board)

        json4["data"]["possible_places"] = board_json
        return json4

    @staticmethod
    def put_pawn(iD, tile_id, rotate, places):
        # places = [(x1, y1), (x2, y2), ...]
        json5 = {
            "type": "pawn_info",
            "data": {
                "id": iD,
                "tile": {
                    "id": tile_id,
                    "rotate": rotate
                },
                "possible_places": [],
            }
        }

        places_json = []
        for i in range(0, len(places)):
            place = {"x": places[i][0], "y": places[i][1]}
            places_json.append(place)

        json5["data"]["possible_places"] = places_json
        return json5

    @staticmethod
    def end_game(winners):
        # winners = [(place1, id1, points1), (place2, id2, points2)]
        json6 = {
            "type": "end_game",
            "data": {
                "winners": []
            }
        }
        winners_json = []
        for i in range(0, len(winners)):
            winner = {"place": winners[i][0], "id": winners[i][1], "points": winners[i][2]}
            winners_json.append(winner)

        json6["data"]["winners"] = winners_json
        return json6
