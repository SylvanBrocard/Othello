class board():
    def __init__(self,nb_lignes,nb_colonnes):
        self.__nb_lignes = nb_lignes
        self.__nb_colonnes = nb_colonnes
        self.__board = [[0] * self.__nb_colonnes] * self.__nb_colonnes

    def add_pawn(self,x,y,color):
        pass

    
    def reverse_pawn(self,liste):
        for i in liste :
            i.reverse_pawn()
        pass

    def print(self):
        pass


