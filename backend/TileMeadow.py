from Enums import Terrains
from Tile import Tile


class TileMeadow(Tile):

    #  def check_for_points_after_move(self):
    #  pass  # doesn't do anything

    def check_for_points_after_game(self):  # awards points and then removes pawns
        # neighours of castles work on simple rules: terrain 3 neighbours 2 and 4 etc.
        # should have individual dfs that on each tile searches adjecent castles and whether they are completed
        result = {}  # dictionary- player: points
        for i in self.sides:  # check all areas
            if i[1] == Terrains.MEADOW:  # if it's the area we want
                if i[3] is not None:
                    whole_meadow = self.dfs_start(i)

                    # count pawns on the given meadow

                    # for all neighboring castles check if they are completed and add 3 points per each individual one
