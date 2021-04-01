from othello.pawn import Pawn


class Tile():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.has_pawn = False
        self.pawn = None

    def get_coordonates(self):
        return self.x, self.y

    def add_pawn(self,color):
        self.pawn = Pawn(color)
