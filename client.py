import pygame
from network import Network
from utils import *
from player import Player
from ball import Ball

BG = 40, 42, 54
GREEN = 80, 250, 123
WHITE = (255, 255, 255)


def redrawWindow(win, players, scoreA, scoreB):
    win.fill(BG)

    for player in players:
        player.draw(win)

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
    pygame.display.set_caption("Client")

    run = True
    n = Network()

    x, y, h, w, color, type = read_single_object_info(n.getPos())

    p = Player(x, y, w, h, color, type)
    ball = Ball(90, 40, BG, 10, 10)
    other_players = [Player(x, y, w, h, BG, type), Player(x, y, w, h, BG, type),
                     Player(x, y, w, h, BG, type), ball]

    clock = pygame.time.Clock()

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


        objects = read_objects_info(n.send(create_single_object_info(p)))
        attributes = [['x', 0], ['y', 1], ['width', 3], ['height', 2], ['color', 4], ['type', 5]]
        j = 0

        for obj in objects:
            for atr, i in attributes:
                setattr(other_players[j], atr, obj[i])
            j += 1


        scoreA = other_players[3].height
        scoreB = other_players[3].width

        for player in other_players:
            player.update()

        p.move()
        redrawWindow(win, [p, other_players[0], other_players[1], other_players[2], ball],scoreA,scoreB)


        clock.tick(60)

run_client()
