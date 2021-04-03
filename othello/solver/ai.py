from othello.engine import Engine
from othello.common import constants


class Ai_engine(Engine):
    def __init__(self):
        Engine.__init__(self)
        self.bestMove = (0,0)


    def start_game(self):
        '''
        Démarre une partie, donne le coup de l'IA.
        '''
        self.initial_pawns()
        while not Engine.is_finished(self):
            self.board.display_board(self.get_possible_moves())
            self.show_ai_move()
            self.play_move()
            self.switch_player()
        self.end_game()

    @staticmethod
    def move_string(x,y):
        '''
        Transforme un coup en un format lisible
        '''
        outstr='Possible moves:'
        outstr= chr(ord('@')+x+1)+str(y+1)
        return outstr

    def show_ai_move(self):
        '''
        Affiche à l'écran le coup privilégié par l'IA
        '''
        x_ai, y_ai, evaluation = self.ai_move()
        print("Move chosen by the AI : " + self.move_string(x_ai, y_ai))
        print("Move evaluation : " + str(evaluation))

    def ai_move(self):
        '''
        Calcule le coup optimal
        '''
        evaluation = self.alphabeta(constants.ai_tree_search_depth,float('-inf'),float('inf'),is_top=True)
        x_ai, y_ai = self.bestMove
        return x_ai, y_ai, evaluation

    def alphabeta(self,depth,alpha,beta, is_top=False):
        '''
        algorithme alphabeta
        '''
        finished, score = self.is_finished()
        if finished:
            return score
        if depth <= 0:
            return self.board.get_evaluation()
        for move in self.get_possible_moves():
            x, y = move
            flips = self.get_flips(x, y)
            self.resolve_move(move)
            self.switch_player()
            score = -self.alphabeta(depth-1, -beta, -alpha)
            self.unresolve_move(move,flips)
            self.switch_player()
            if (score >= alpha):
                alpha = score
                self.bestMove = move
                if (alpha >= beta):
                    break
        return alpha

    def is_finished(self):
        finished = Engine.is_finished(self)
        score = 0
        if finished:
            evaluation = self.board.get_evaluation()
            if evaluation == 0:
                score = 0
            elif evaluation > 0:
                score = float('inf')
            else :
                score = float('-inf')
        return finished, score

    def unresolve_move(self, move, flips):
        for pawn in flips:
            pawn.reverse_pawn()
        x, y = move
        self.board.remove_pawn(x, y)

        

