from othello.pawn import Pawn
from othello.tile import Tile
from collections import Counter
from othello.common import constants


class Board():
    def __init__(self, nrows, ncols):
        self.nrows = nrows
        self.ncols = ncols
        tilearray = [[Tile(x, y) for x in range(self.nrows)]
                     for y in range(self.ncols)]
        self._tilearray = tilearray

    @property
    def tilearray(self):
        return self._tilearray

    @tilearray.setter
    def tilearray(self, value):
        self._tilearray = value

    def get_value_matrix(self):
        nrows, ncols = len(self.tilearray), len(self.tilearray[0])
        value_matrix = [['0' for _ in range(nrows)] for _ in range(nrows)]
        for i in range(nrows):
            for j in range(ncols):
                if self.tilearray[i][j].has_pawn:
                    value_matrix[i][j] = self.tilearray[i][j].pawn.color
        return value_matrix

    def add_pawn(self, x, y, color):
        '''
        Adds a pawn of color in the x,y tile
        '''
        self.tilearray[x][y].pawn = Pawn(color)
        self.tilearray[x][y].has_pawn = True

    def remove_pawn(self, x, y):
        '''
        Adds a pawn of color in the x,y tile
        '''
        if self.has_pawn(x, y):
            self.tilearray[x][y].has_pawn=False

    def __str__(self):
        code = 65
        ligne1 = ' '
        ligne2 = ' +'
        chaine = ''
        for i in range(self.ncols):
            ligne1 += '   ' + (chr(code+i))
            ligne2 += '---+'
        chaine += '\n' + ligne1 + '\n' + ligne2
        for i in range(self.nrows):
            chaine += "\n" + str(i+1) + '|'
            for j in range(self.ncols):
                chaine += " " + \
                    str(self.tilearray[i][j].pawn.color).replace(
                        "0", " ") + " |"
            chaine += '\n' + ligne2
        return chaine
    
    @staticmethod
    def get_move_string(possible_moves):
        outstr='Possible moves:'
        for move in possible_moves:
            (x, y) = move
            outstr= outstr+chr(ord('@')+x+1)+str(y+1)+" "
        return outstr
        

    @staticmethod
    def generate_display_matrix(position_matrix):
        nrows, ncols = len(position_matrix)+1, len(position_matrix[0])+1
        display_matrix = [[""] * nrows for i in range(ncols)]
        for i in range(1, nrows):
            for j in range(1, ncols):
                display_matrix[i][j] = (position_matrix[i-1][j-1])
        return display_matrix

    @staticmethod
    def dstring(string, locval, indexes):
        newstr = string[:indexes[locval[0]]] + \
            (locval[1])+string[indexes[locval[0]]+1:]
        return newstr

    def display_board(self, possible_moves=[]):
        
        hints = possible_moves        
        mvals = self.get_value_matrix()
        for i in range(len(mvals)):
            for j in range(len(mvals[0])):
                if (i, j) in hints:
                    mvals[i][j]="?"
        m = self.generate_display_matrix(mvals)
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
                    new = Board.dstring(new, locval, indexes)
            new = new.replace("0", " ")
            # new = new.replace("1", "X")
            # print("white")
            # new = new.replace("-1 ","O")

            print(new)
            print(colseps)
            print(hline)
        whitescore, blackscore=self.count_pawns()

        print(self.get_move_string(possible_moves))
        print("*****Score: white: %d ; black: %d; current eval: %d ********** "  % (whitescore, blackscore, self.get_evaluation()))
    


    def has_pawn(self, x, y) -> bool:
        '''
        Renvoie True si la case en x,y a un pion
        '''
        return self.get_tile(x, y).has_pawn

    def get_pawn(self, x, y) -> Pawn:
        '''
        Renvoie le pion sur la case x,y (exception 
        si la case n'a pas de pion)
        '''
        if self.get_tile(x, y).has_pawn:
            return self.get_tile(x, y).pawn
        else:
            # return None
            raise ValueError("Tile has no pawn")

    def get_tile(self, x, y) -> Tile:
        '''
        Renvoie la case en x,y
        '''
        return self.tilearray[x][y]

    def get_all_pawns(self) -> list:
        '''
        Returns the list of all pawns
        '''
        return [
            self.get_pawn(x, y)
            for x in range(self.nrows)
            for y in range(self.ncols)
            if self.has_pawn(x, y)
        ]

    def count_pawns(self) -> tuple:
        '''
        Décompte les pions noirs et blancs
        '''
        color_counter = Counter([pawn.color for pawn in self.get_all_pawns()])
        return color_counter[constants.symbol_black], color_counter[constants.symbol_white]

    def get_evaluation(self):
        count_black, count_white = self.count_pawns()
        return count_white-count_black

    def empty_tiles(self) -> list:
        '''
        Renvoie la liste des tuiles vides
        '''
        return [
            self.get_tile(x, y)
            for x in range(self.nrows)
            for y in range(self.ncols)
            if not self.has_pawn(x, y)
        ]


if __name__ == "__main__":
    m = Board(8, 8)
    m.add_pawn(3, 3, constants.symbol_black)
    m.add_pawn(2, 5, constants.symbol_white)
    # print(m.get_pawn(3,3).color)
    # print(m.get_pawn(1,5).color)

    # print(m.generate_display_matrix( m.get_value_matrix())[4][:])
    # print(m.generate_display_matrix( m.get_value_matrix())[5][:])
    m.display_board()
