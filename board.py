from pawn import *
from tile import *

class board():
    def __init__(self,nb_lignes,nb_colonnes):
        self.__nb_lignes = nb_lignes
        self.__nb_colonnes = nb_colonnes
        #self.__board = [[0] * self.__nb_colonnes] * self.__nb_colonnes
               
        self.__board = [0] * nb_colonnes
        for i in range(nb_colonnes):
            self.__board[i] = [0] * nb_lignes


    def add_pawn(self,x,y,color):
        pass


    def __str__(self):
        code = 65
        ligne1 = ' '
        ligne2 = ' +'
        chaine = ''
        for i in range(self.__nb_colonnes):
            ligne1 += '   ' + (chr(code+i))
            ligne2 += '---+'
        chaine += '\n' + ligne1 + '\n' + ligne2 
        for i in range(self.__nb_lignes):
            chaine += "\n" + str(i+1) + '|' 
            for j in range(self.__nb_colonnes):
                chaine += " " + str(self.__board[i][j]).replace("0"," ") +  " |"
            chaine += '\n' + ligne2
        return chaine


m= board(8,8)
m.add_pawn(1,1,'o')
print(m)


