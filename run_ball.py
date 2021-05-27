import pygame
from network import Network
from utils import *
from ball import Ball
from player import Player


BG = 40, 42, 54
GREEN = 80, 250, 123

def redrawWindow(win, players):
    win.fill(BG)


    for player in players:
        player.draw(win)

    pygame.display.update()


def run_b():

    run = True
    n = Network()

    x, y, h, w, color, type = read_single_object_info(n.getPos())

    p = Ball(x,y,GREEN,w,h)
    other_players = [Player(x, y, w, h, BG, type),Player(x, y, w, h, BG, type),
                     Player(x, y, w, h, BG, type),Player(x, y, w, h, BG, type)]
    clock = pygame.time.Clock()

    while run:

        objects = read_objects_info(n.send(create_single_object_info(p)))
        attributes = [['x', 0], ['y', 1], ['width', 3], ['height', 2], ['color', 4], ['type', 5]]
        j = 0

        for obj in objects:
            for atr, i in attributes:
                setattr(other_players[j], atr, obj[i])
            other_players[j].update()
            j += 1

        for player in other_players:
            p.check_collision(player)

        p.move()
        clock.tick(60)

run_b()
