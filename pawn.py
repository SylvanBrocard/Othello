class pawn():
    def __init__(self,color,tile):
        self.__color = color
        

    def get_color(self):
        return self.__color

    def reverse_pawn(self):
        if self.__color == 'o':
            self.__color = '*'
        elif self.__color == '*':
            self.__color = 'o'