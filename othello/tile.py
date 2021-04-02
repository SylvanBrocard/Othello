from pawn import Pawn

from pawn import *


class Tile():

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._has_pawn = False
        self._pawn = None

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def has_pawn(self):
        return self._has_pawn

    @property
    def pawn(self):
        return self._pawn

    @property
    def coordinates(self):
        return self._x, self._y

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

    @has_pawn.setter
    def has_pawn(self, value):
        self._has_pawn = value

    @pawn.setter
    def pawn(self, value):
        self._pawn = value



if __name__ == "__main__":
    tuile = Tile(1,2)
    print(tuile)