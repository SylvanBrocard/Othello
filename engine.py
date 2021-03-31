from board import board


class Engine:
    def __init__(self):
        self.nb_colonnes = 8
        self.nb_lignes = 8
        self.board = board(self.nb_lignes, self.nb_colonnes)
        self.active_player = 'black'

    def start_game(self):
        '''
        Démarre une partie.
        '''
        pass

    def print_board(self):
        '''
        Imprime l'état du plateau à l'écran
        '''
        print(self.board)

    def get_input(self):
        '''
        Reçoit le choix du joueur en cours
        '''
        valid_input = False
        while not valid_input:
            valid_input = True
            rankandfile = input(
                "Enter the rank and file where you want to drop your pawn (ex: 4 E): ")
            x, y = rankandfile.split()
            try:
                x = int(x)
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
                valid_input = False
            else:
                try:
                    assert 1 <= x <= self.nb_lignes 
                    assert A <= y.upper() <= chr(ord('A') + self.nb_colonnes)
                except:
                    print("Oops!  That's outside the board.  Try again...")
                    valid_input = False
        if A.isupper:
            y = ord(y) - 64
        else : 
            y = ord(y) - 96
        return x, y

    def resolve_move(self, input):
        '''
        Résoud les conséquences d'un coup
        '''
        x, y = input
        flips = self.get_flips(self, x, y)
        for pawn in flips:
            pawn.reverse_pawn()

    def get_flips(self, x, y):
        '''
        Trouve tous les pions qui doivent être retournés
        '''
        flips = []
        for direction_x in [-1, 0, 1]:
            for direction_y in [-1, 0, 1]:
                if not (x == 0 or y == 0):
                    search_finished = False
                    x_search = x
                    y_search = y
                    while not search_finished:
                        x_search = x_search + direction_x
                        y_search = y_search + direction_y
                        if (
                            not self.board.has_pawn(x_search, y_search)
                            or self.board.get_pawn(x_search, y_search).color == self.active_player
                            or not self.valid_coords(x_search, y_search)
                        ):
                            search_finished = True
                        else:
                            flips.append(self.board.get_pawn(
                                x_search, y_search))
        return flips

    def valid_coords(x, y):
        return 1 <= x <= self.nb_lignes and 1 <= y <= self.nb_colonnes

    def is_finished(self):
        pass

    def end_game(self):
        pass

# engine = Engine()
# x, y = engine.get_input()
# print(x)
# print(y)
print(ord('a'))
