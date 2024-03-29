from othello.board import Board
from othello.common import constants
from othello.common.converters import move_string
from othello.common.utilities import cls
from IPython.display import clear_output


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
            possible_moves = self.get_possible_moves()
            self.board.display_board(possible_moves)
            self.show_move_string(possible_moves)
            self.play_move()
            self.switch_player()
            clear_output(wait=True)
            cls()
        self.end_game()

    @staticmethod
    def show_move_string(possible_moves):
        outstr = 'Possible moves:'
        for move in possible_moves:
            x, y = move
            outstr = outstr+" "+move_string(x, y)
        print(outstr)

    def initial_pawns(self):
        '''
        Sets initial board configuration
        '''
        self.board.add_pawn(self.nb_colonnes//2 - 1,
                            self.nb_lignes//2-1, constants.symbol_black)
        self.board.add_pawn(self.nb_colonnes//2 - 1,
                            self.nb_lignes//2, constants.symbol_white)
        self.board.add_pawn(self.nb_colonnes//2,
                            self.nb_lignes//2-1, constants.symbol_white)
        self.board.add_pawn(self.nb_colonnes//2,
                            self.nb_lignes//2, constants.symbol_black)

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
            valid, x, y = self.valid_move(move)
            if valid:
                valid = self.resolve_move((x, y))

    def get_input(self):
        '''
        Reçoit le choix du joueur en cours
        '''
        if self.active_player == constants.symbol_black:
            player = 'Black'
        else:
            player = 'White'
        move = input(
            "Enter the rank and file where you want to drop your pawn (ex: E4). "
            + player + " to move (" + self.active_player + ") ")
        move = list(move)
        return move

    def valid_move(self, move):
        '''
        Vérifie la validité du coup rentré par le joueur,
        et transforme l'entrée en coordonnées numériques
        '''
        if len(move) < 2:
            print("Oops!  That wasn't enough coordinates.  Try again...")
            return False, None, None
        x, y = move[1], move[0]
        if not x.isdigit():
            print("Oops!  That was no valid rank.  Try again...")
            return False, None, None
        x = int(x)
        if not y.isalpha():
            print("Oops!  That was no valid file.  Try again...")
            return False, None, None
        if y.isupper():
            y = ord(y) - 64
        else:
            y = ord(y) - 96
        y, x = y-1, x-1
        if not self.valid_coords(x, y):
            print("Oops!  That's outside the board.  Try again...")
            return False, None, None
        return True, x, y

    def resolve_move(self, move):
        '''
        Résoud les conséquences d'un coup,
        renvoie False si le coup n'a pas pu être joué
        '''
        x, y = move
        if self.board.has_pawn(x, y):
            print("Oops!  There's already a pawn here.  Try again...")
            return False
        flips = self.get_flips(x, y)
        if len(flips) == 0:
            print("Oops!  That move doesn't flip any pawn.  Try again...")
            return False
        for pawn in flips:
            pawn.reverse_pawn()
        self.board.add_pawn(x, y, self.active_player)
        return True

    def get_flips(self, x, y):
        '''
        Trouve tous les pions qui doivent être retournés
        '''
        flips = []
        for direction_x in [-1, 0, 1]:
            for direction_y in [-1, 0, 1]:
                # print("direction x = " + str(direction_x) + ", direction y = " + str(direction_y))
                if not (direction_x == 0 and direction_y == 0):
                    search_finished = False
                    line_flips = []
                    x_search = x
                    y_search = y
                    while not search_finished:
                        x_search = x_search + direction_x
                        y_search = y_search + direction_y
                        # print("x = " + str(x_search) +", y = " + str(y_search))
                        if (
                            not self.valid_coords(x_search, y_search)
                            or not self.board.has_pawn(x_search, y_search)
                        ):
                            search_finished = True
                        elif self.board.get_pawn(x_search, y_search).color == self.active_player:
                            search_finished = True
                            flips.extend(line_flips)
                        else:
                            line_flips.append(self.board.get_pawn(
                                x_search, y_search))
                    # print(line_flips)
        return flips

    def valid_coords(self, x, y):
        '''
        Vérifie que les coordonnées x, y sont dans le plateau
        '''
        return 0 <= x <= self.nb_lignes-1 and 0 <= y <= self.nb_colonnes-1

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
        # print("empty_tiles = " + str(empty_tiles))
        possible_moves = []
        for tile in empty_tiles:
            # print(str(tile.x) + ", " + str(tile.y))
            flips = self.get_flips(tile.x, tile.y)
            if len(flips) > 0:
                # print("move possible")
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
    engine.start_game()
    # engine.initial_pawns()
    # print(engine.board.get_pawn(3,3).color)
    # print(engine.board.get_pawn(3,4).color)
    # print(engine.get_flips(3,5))
    # print(engine.get_possible_moves())
    # print(engine.get_flips(6,6))
    # print(engine.board.tilearray)
