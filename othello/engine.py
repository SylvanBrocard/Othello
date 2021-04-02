from board import Board
from common import constants


class Engine:
    def __init__(self):
        self.nb_colonnes = constants.number_of_files
        self.nb_lignes = constants.number_of_ranks
        self.board = Board(self.nb_lignes, self.nb_colonnes)
        self.active_player = constants.symbol_black

    def start_game(self):
        '''
        Démarre une partie.
        '''
        self.initial_pawns()
        while not self.is_finished():
            self.board.display_board()
            self.play_move()
            self.switch_player()
        self.end_game()

    def initial_pawns(self):
        '''
        Sets initial board configuration
        '''
        self.board.add_pawn(4, 4, constants.symbol_black)
        self.board.add_pawn(4, 5, constants.symbol_white)
        self.board.add_pawn(5, 4, constants.symbol_white)
        self.board.add_pawn(5, 5, constants.symbol_black)

    def switch_player(self):
        '''
        Change le joueur actif
        '''
        if self.active_player == constants.symbol_black:
            self.active_player = constants.symbol_white
        else:
            self.active_player = constants.symbol_black

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
            valid, move = self.valid_move(move)
            if valid:
                valid = self.resolve_move(move)

    def get_input(self):
        '''
        Reçoit le choix du joueur en cours
        '''
        move = input(
            "Enter the rank and file where you want to drop your pawn (ex: E4): ")
        move = list(move)
        return move

    def valid_move(self, move):
        '''
        Vérifie la validité du coup rentré par le joueur,
        et transforme l'entrée en coordonnées numériques
        '''
        if len(move) < 2:
            print("Oops!  That wasn't enough coordinates.  Try again...")
            return False
        x, y = move[1], move[0]
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
        move = y, x
        return True, move

    def resolve_move(self, move):
        '''
        Résoud les conséquences d'un coup,
        renvoie False si le coup n'a pas pu être joué
        '''
        x, y = move
        if self.board.has_pawn(x, y):
            print("Oops!  There's already a pawn here.  Try again...")
            return False
        self.board.add_pawn(x, y, self.active_player)
        flips = self.get_flips(x, y)
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
                    line_flips = []
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
                        elif self.board.get_pawn(x_search, y_search).color == self.active_player:
                            search_finished = True
                            flips.extend(line_flips)
                        else:
                            line_flips.append(self.board.get_pawn(
                                x_search, y_search))
        return flips

    def valid_coords(self, x, y):
        '''
        Vérifie que les coordonnées x, y sont dans le plateau
        '''
        return 1 <= x <= self.nb_lignes and 1 <= y <= self.nb_colonnes

    def is_finished(self):
        '''
        Détermine si la partie est terminée
        '''
        return len(self.get_possible_moves()) == 0

    def get_possible_moves(self):
        '''
        Renvoie la liste des coups possibles pour le joueur actif
        '''
        empty_tiles = self.board.empty_tiles()
        possible_moves = []
        for tile in empty_tiles:
            flips = self.get_flips(tile.x,tile.y)
            if len(flips) > 0:
                possible_moves.append((tile.coordinates))
        return possible_moves

    def end_game(self):
        '''
        Termine la partie
        '''
        black, white = self.board.count_pawns()
        if black > white:
            print("Black wins the game !")
        elif white > black:
            print("White wins the game !")
        else:
            print("Draw !")
        print("Final board :")
        self.board.display_board()


if __name__ == "__main__":
    engine = Engine()
    # x, y = engine.get_input()
    # print(x)
    # print(y)
    # engine.play_move()
    # lettre = 'a'
    # print(lettre.isalpha())
    # engine.start_game()
    engine.initial_pawns()
    print(engine.board.get_pawn(4,4).color)
    print(engine.board.get_pawn(4,5).color)
    # print(engine.get_flips(6,6))