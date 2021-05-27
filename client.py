import pygame
from network import Network
from utils import *
from player import Player
from ball import Ball

BG = 40, 42, 54
GREEN = 80, 250, 123

def redrawWindow(win, players):
    win.fill(BG)

    for player in players:
        player.draw(win)

    pygame.display.update()


def run_client():
    pygame.init()

    size = 300, 300
    win = pygame.display.set_mode(size)
    pygame.display.set_caption("Client")

    run = True
    n = Network()

    x, y, h, w, color, orientation = read_single_object_info(n.getPos())

    p = Player(x, y, w, h, color, orientation)
    ball = Ball(90, 40, BG, 10, 10)
    other_players = [Player(x, y, w, h, BG, orientation), Player(x, y, w, h, BG, orientation),
                     Player(x, y, w, h, BG, orientation),ball]


    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        objects = read_objects_info(n.send(create_single_object_info(p)))
        attributes = [['x', 0], ['y', 1], ['width', 3], ['height', 2], ['color', 4], ['type', 5]]
        j = 0

        for obj in objects:
            for atr, i in attributes:
                setattr(other_players[j], atr, obj[i])
            j += 1


        for player in other_players:
            player.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, [p,other_players[0], other_players[1], other_players[2],ball])

run_client()
