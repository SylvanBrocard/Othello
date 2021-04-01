from othello.pawn import Pawn

from pawn import *


class tile():

    def init(self, x, y):
        self.x = x
        self.y = y
        self.has_pawn = False
        self.pawn = None

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def has_pawn(self):
        return self.has_pawn

    @property
    def pawn(self):
        return self.pawn

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

    @has_pawn.setter
    def has_pawn(self, value):
        self.has_pawn = value

    @pawn.setter
    def pawn(self, value):
        self.pawn = value

    def get_coordonates():
        return self.x, self.y
