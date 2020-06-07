from backend.tile.TileCastle import TileCastle


class TileCastleShield(TileCastle):  # inherits its entire logic from TileCastle, it only changes amount of points

    def __init__(self):
        super().__init__()
        self.points = 4
        self.penalty_points = 2
