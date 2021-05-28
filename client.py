import pygame
from network import Network
from utils import *
from player import Player
from ball import Ball

BG = 40, 42, 54
GREEN = 80, 250, 123
BG = (40, 42, 54)
PINK = (255, 121, 198)
GREEN = (80, 250, 123)
CYAN = 139, 233, 253
WHITE = (255, 255, 255)

def winner_is(winner,color,win):
    win.fill(BG)

    font1 = pygame.font.Font(None, 74)
    text1 = font1.render("Vitória do time {}!!!".format(winner), True, color)
    win.blit(text1, (10, 10))

    font2 = pygame.font.Font(None, 48)
    text2 = font2.render("Fim de jogo.", True, WHITE)
    win.blit(text2, (250, 200))

    pygame.display.update()

def redrawWindow(win, objects, scoreA, scoreB):
    win.fill(BG)

    for obj in objects:
        obj.draw(win)

    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), True, WHITE)
    win.blit(text, (250, 10))
    text = font.render(str(scoreB), True, WHITE)
    win.blit(text, (420, 10))

    pygame.draw.line(win, WHITE, [349, 0], [349, 500], 5)
    pygame.display.update()


def run_client():

    pygame.init()

    size = 700, 500
    win = pygame.display.set_mode(size)
    pygame.display.set_caption("Pong Client")

    run = True
    n = Network()

    x, y, color, aux = read_single_object_info(n.getPos())


    p = Player(x, y, 10, 50, color, 'p')
    ball = Ball(345, 255, GREEN, 10, 10)
    other_objects = [Player(x, y, 10, 50, BG, 'p'), Player(x, y, 10, 50, BG, 'p'),
                     Player(x, y, 10, 50, BG, 'p'), ball]

    clock = pygame.time.Clock()


    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        updates = read_objects_info(n.send(create_single_object_info(p)))
        attributes = [['x', 0], ['y', 1],['color', 2]]
        j = 0

        # Atualiza a posição e cor dos outros jogadores
        for obj in updates[:3]:
            for atr, i in attributes:
                setattr(other_objects[j], atr, obj[i])
            j += 1

        # Atualiza posição da bola
        setattr(other_objects[3], 'x', updates[3][0])
        setattr(other_objects[3], 'y', updates[3][1])

        # Atualiza os scores
        scoreA = updates[3][2]
        scoreB = updates[3][3]

        if scoreA >= 10:
            winner = "ROSA"
            winner_color = PINK
            break

        if scoreB >= 10:
            winner = "AZUL"
            winner_color = CYAN
            break

        for player in other_objects:
            player.update()

        p.move()
        redrawWindow(win, [p, other_objects[0], other_objects[1], other_objects[2], ball],scoreA,scoreB)

        clock.tick(60)

    endgame = True
    while endgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endgame = False
                pygame.quit()
        winner_is(winner, winner_color, win)

run_client()
