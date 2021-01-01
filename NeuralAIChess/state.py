#!/usr/bin/env python3 #creates the python3 environment to run the script
import chess

class State(object):
    def __init__(self):
        self.board = chess.Board()

    def serialize(self):
        # 257 bit representation
        pass

    def edges(self):
        return list(self.board.legal_moves) # lists all the legal moves in chess

    def value(self):
        return 0

if __name__ == "__main__":
    s = State()
    print(s.edges())