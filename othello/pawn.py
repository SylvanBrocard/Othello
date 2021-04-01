from othello.common import constants

class Pawn():
    def __init__(self, color):
        self.color = color

    def reverse_pawn(self):
        if self.color == constants.symbol_black:
            self.color = constants.symbol_white
        elif self.color == constants.symbol_white:
            self.color = constants.symbol_black
