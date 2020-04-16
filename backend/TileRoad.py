from Tile import Tile


# logika drogi, pod postawieniu klocka trzeba sprawdzić
# droga mogła się albo zakończyć, albo zapętlić
class TileRoad(Tile):

    def check_for_points_after_move(self):
        pass  # returns list of tuples (player, points)
