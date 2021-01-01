#!/usr/bin/env python3

import os
import chess.pgn

for fn in os.listdir("images"):
    pgn = open(os.path.join("images", fn))
    while 1:
        try:
            game = chess.pgn.read_game(pgn)
        except Exception:
            break

        print(game)