import pygame as py
from ChessMain import main

py.init()
py.display.set_caption("Welcome to PyChess Engine!!!")

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

win = py.display.set_mode((WIDTH, HEIGHT))

def drawStartScreen(surface, text, size, color):
    font = py.font.SysFont('Times New Roman', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (150 + 230 / 2 - (label.get_width() / 2), 100 + 300 / 2 - (label.get_height() / 2)))

def start():
    run = True
    while run:
        win.fill(BLACK)
        drawStartScreen(win, 'Press Any Key To Play', 40, GREEN)
        py.display.update()

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

            if event.type == py.KEYDOWN or event.type == py.MOUSEBUTTONDOWN:
                main()

    py.display.quit()