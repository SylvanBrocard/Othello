from othello.engine import Engine
from othello.solver.ai import Ai_engine

def run():
    engine = Ai_engine()
    engine.start_game()

if __name__=='__main__':
    run()