from othello.pawn import Pawn
from othello.tile import Tile


class Board():
    def __init__(self, nrows, ncols):
        tiles=[]
        for i in range(nrows):
            for j in range(ncols):
                tile=tile(0, 0)
                tile.x=j
                tile.y=i
                tiles.append(tile)
    
    def get_value_matrix(self):
        nrows, ncols=len(self._tiles), len(self._tiles[0])
        value_matrix = [[0] *nrows] * nrows
        for i in range(nrows):
            for j in range(ncols):
                if self._tiles[i][j].has_pawn():
                    value_matrix[i][j]=self._tiles[i][j].self._tiles[i][j].pawn

    def add_pawn(self, x, y, color):
        board_matrix = self.__board
        board_matrix[x][y] = color
        self.__board = board_matrix

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
                chaine += " " + \
                    str(self.__board[i][j]).replace("0", " ") + " |"
            chaine += '\n' + ligne2
        return chaine

    @staticmethod
    def generate_display_matrix(position_matrix):
        nrows, ncols = len(position_matrix)+1, len(position_matrix[0])+1
        display_matrix = [[""] * nrows for i in range(ncols)]
        for i in range(1, nrows):
            for j in range(1, ncols):
                display_matrix[i][j] = str(position_matrix[i-1][j-1])
        return display_matrix

    @staticmethod
    def dstring(string, locval, indexes):
        newstr = string[:indexes[locval[0]]] + \
            (locval[1])+string[indexes[locval[0]]+1:]
        return newstr

    def display_board(self):
        m = board.generate_display_matrix(self.__board)
        nrows, ncols = len(m), len(m[0])
        hline = "--------"*(ncols)+"-"
        colseps = "|       "*(ncols)+"|"
        valueprints = "|   0   "*(ncols)+"|"
        # get a list [A, B, C...H]
        charlist = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        col_names = [charlist[i] for i in range(ncols)]
        indexes = [i for i in range(len(valueprints))
                   if valueprints.startswith('0', i)]
        print(hline+"\n"+colseps)
        newstr = "|   0   "*(ncols)+"|"

        for index in range(1, len(indexes)):
            valueprints = valueprints[:indexes[index]] + \
                col_names[index-1]+valueprints[indexes[index]+1:]
        print(valueprints.replace("0", " ")+"\n"+colseps+"\n"+hline)
        for ind in range(1, nrows):
            print(colseps)
            new = newstr[:indexes[0]]+str(ind)+newstr[indexes[0]+1:]
            indbw = [[i, val] for i, val in enumerate(m[ind]) if val != ""]
            if indbw:
                for locval in indbw:
                    new = board.dstring(new, locval, indexes)
            new = new.replace("0", " ")
            new = new.replace("x", "X")
            new = new.replace("o", "O")

            print(new)
            print(colseps)
            print(hline)

    def has_pawn(self, x, y) -> bool:
        '''
        Renvoie True si la case en x,y a un pion
        '''
        pass

    def get_pawn(self, x, y) -> pawn:
        '''
        Renvoie le pion sur la case x,y (exception 
        si la case n'a pas de pion)
        '''
        pass

    def count_pawns(self) -> int, int:
        '''
        Décompte les pions noirs et blancs
        '''
        pass
        color_counter = Counter([pawn.color for pawn in self.get_all_pawns])
        return Counter[constants.symbol_black], Counter[constants.symbol_white]

    def get_all_pawns(self) -> list:
        '''
        Returns the list of all pawns
        '''
        return [
            self.get_pawn(x,y)
            for x in range(self.__nb_lignes)
            for y in range(self.__nb_colonnes)
            if self.has_pawn(x,y)
            ]

    def empty_tiles(self) -> list:
         '''
         Renvoie la liste des tuiles vides
         '''
		pass
        return [
            self.get_tile(x,y)
            for x in range(self.__nb_lignes)
        '''
         Décompte les pions noirs et blancs
         '''
		pass
        color_counter = Counter([pawn.color for pawn in self.get_all_pawns])
        return Counter[constants.symbol_black], Counter[constants.symbol_white]
            self.get_pawn(x,y)
            for x in range(self.__nb_lignes)
            for y in range(self.__nb_colonnes)
            if self.has_pawn(x,y)
            ]

if __name__ == "__main__":
    m = board(8, 8)
    m.add_pawn(1, 1, 'o')
    m.add_pawn(1, 5, 'x')
    # print(m)
    m.display_board()
