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
        while not self.is_finished:
            self.play_move()
            self.switch_player()
        self.end_game()

    def print_board(self):
        '''
        Imprime l'état du plateau à l'écran
        '''
        print(self.board)

    def play_move(self):
        '''
        Joue un coup complet
        '''
        valid = False
        while not valid:
            move = self.get_input()
            valid = self.valid_move(move)
            if valid:
                valid = self.resolve_move(move)

    def get_input(self):
        '''
        Reçoit le choix du joueur en cours
        '''
        move = input(
            "Enter the rank and file where you want to drop your pawn (ex: 4 E): ")
        move = move.split()
        return move

    def valid_move(self, move):
        '''
        Vérifie la validité du coup rentré par le joueur,
        et transforme l'entrée en coordonnées numériques
        '''
        if len(move) < 2:
            print("Oops!  That wasn't enough coordinates.  Try again...")
            return False
        x, y = move
        if not x.isdigit():
            print("Oops!  That was no valid rank.  Try again...")
            return False
        x = int(x)
        if not y.isalpha():
            print("Oops!  That was no valid file.  Try again...")
            return False
        if y.isupper():
            y = ord(y) - 64
        else:
            y = ord(y) - 96
        if not self.valid_coords(x, y):
            print("Oops!  That's outside the board.  Try again...")
            return False
        return True

    def resolve_move(self, move):
        '''
        Résoud les conséquences d'un coup,
        renvoie False si le coup n'a pas pu être joué
        '''
        x, y = move
        if self.board.has_pawn(x, y):
            print("Oops!  There's already a pawn here.  Try again...")
            return False
        self.board.add_pawn(x, y)
        flips = self.get_flips(self, x, y)
        if len(flips) == 0:
            print("Oops!  That move doesn't flip any pawn.  Try again...")
            return False
        for pawn in flips:
            pawn.reverse_pawn()
        return True

    def get_flips(self, x, y):
        '''
        Trouve tous les pions qui doivent être retournés
        '''
        flips = []
        for direction_x in [-1, 0, 1]:
            for direction_y in [-1, 0, 1]:
                if not (direction_x == 0 and direction_y == 0):
                    search_finished = False
                    line_flips=[]
                    x_search = x
                    y_search = y
                    while not search_finished:
                        x_search = x_search + direction_x
                        y_search = y_search + direction_y
                        if (
                            not self.board.has_pawn(x_search, y_search)
                            or not self.valid_coords(x_search, y_search)
                        ):
                            search_finished = True
                        if self.board.get_pawn(x_search, y_search).color == self.active_player:
                            search_finished = True
                            flips.extend(line_flips)
                        else:
                            line_flips.append(self.board.get_pawn(
                                x_search, y_search))
        return flips

    def valid_coords(self, x, y):
        return 1 <= x <= self.nb_lignes and 1 <= y <= self.nb_colonnes

    def is_finished(self):
        pass

    def end_game(self):
        pass


engine = Engine()
# x, y = engine.get_input()
# print(x)
# print(y)
engine.play_move()
# lettre = 'a'
# print(lettre.isalpha())
