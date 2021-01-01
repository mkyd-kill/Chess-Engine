'''
    This is the main driver file resposible for user input and user return displays
''' 

import pygame as p
from ChessEngine import GameState

p.init()
p.display.set_caption('Chess Engine')
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # for animation purposes
IMAGES = {} # an empty image dictionary
WHITE = (255, 255, 255)
SALMON = (255,160,122)

def loadImages():
    pieces = ['bB', 'bK', 'bN', 'bp', 'bQ', 'bR', 'wB', 'wK', 'wN', 'wp', 'wQ', 'wR']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load('images/' + piece + '.png'), (SQ_SIZE, SQ_SIZE))


# the main driver handling user input and graphics update
def main():
    screen =  p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color(WHITE))
    gs = GameState()
    loadImages()
    running = True

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

# The drawGameState is responsible for all user graphics
def drawGameState(screen, gs):
    drawBoard(screen) # draws the board squares
    drawPieces(screen, gs.board)


def drawBoard(screen):
    colors = [p.Color(WHITE), p.Color(SALMON)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": # not empty
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()