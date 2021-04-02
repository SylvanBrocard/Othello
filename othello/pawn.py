from common import constants

class Pawn():
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,value):
        self._color = value

    @property
    def pvalue(self):
        if self.color==constants.symbol_black:
            return -1
        if self.color==constants.symbol_white:
            return 1

    def reverse_pawn(self):
        if self.color == constants.symbol_black:
            self.color = constants.symbol_white
        elif self.color == constants.symbol_white:
            self.color = constants.symbol_black

if __name__ == "__main__":
    pion = Pawn('o')
    print(pion.color)