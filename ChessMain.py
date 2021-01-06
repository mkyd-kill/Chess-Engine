'''
    This is the main driver file resposible for user input and user return displays
''' 

import pygame as p
from ChessEngine import GameState, Move

p.init()
p.display.set_caption('Chess Engine')
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # for animation purposes
IMAGES = {} # an empty image dictionary
WHITE = p.Color("white")
SALMON = p.Color("salmon")

# function in pygame that loads the elements images onto the board once
def loadImages():
    pieces = ['bB', 'bK', 'bN', 'bp', 'bQ', 'bR', 'wB', 'wK', 'wN', 'wp', 'wQ', 'wR']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load('images/' + piece + '.png'), (SQ_SIZE, SQ_SIZE))


# the main driver handling user input and graphics update
def main():
    screen =  p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color(WHITE))
    gs = GameState()    # gs is the game state
    validMoves = gs.getValidMoves()
    moveMade = False
    loadImages()    # we are only loading the images once in pygame
    running = True
    sqSelected = () # keeps track of the last user mouse clicks
    playerClicks = [] # keeps track of the last player clicks
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            # mouse key handlers
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # location of x and y
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col):
                    sqSelected = ()
                    playerClicks = []
                # if the player clicks on a chess piece
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) # this appends both the 1st and the 2nd clicks
                if len(playerClicks) == 2: # if the user made 2 mouse clicks
                    move = Move(playerClicks[0], playerClicks[1], gs.board)
                    print(str(move.getChessNotation()) + ' id: ' + str(move.moveID))

                    for i in range(len(validMoves)):
                        if move == validMoves[i]:
                            gs.makeMove(validMoves[i])
                            moveMade = True
                            sqSelected = ()
                            playerClicks = [] # resets user clicks
                    if not moveMade:
                        playerClicks = [sqSelected]
                        
            # keyboard handlers
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z: # the undo key
                    gs.undoMove()
                    moveMade = True
                        

        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

# The drawGameState is responsible for all user graphics
def drawGameState(screen, gs):
    drawBoard(screen) # draws the board squares
    drawPieces(screen, gs.board)

# random color placements
def drawBoard(screen):
    colors = [p.Color(WHITE), p.Color(SALMON)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

# drawPieces responsible for the chess pieces
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": # not empty
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()