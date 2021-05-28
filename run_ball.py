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


def main():
    run = True
    n = Network()

    x, y, aux1, aux2 = read_single_object_info(n.getPos())

    ball = Ball(x, y, GREEN, 10, 10)

    players = [Player(x, y, 10, 50, BG, 'p'), Player(x, y, 10, 50, BG, 'p'),
               Player(x, y, 10, 50, BG, 'p'), Player(x, y, 10, 50, BG, 'p')]

    clock = pygame.time.Clock()

    while run:

        objects = read_objects_info(n.send(create_single_object_info(ball)))
        attributes = [['x', 0], ['y', 1], ['color', 2]]
        j = 0

        if ball.scoreB >= 10 or ball.scoreA >= 10:
            run = False
            pygame.quit()

        for obj in objects:
            for atr, i in attributes:
                setattr(players[j], atr, obj[i])
            players[j].update()
            j += 1

        for player in players:
            ball.check_collision(player)

        ball.move()
        clock.tick(60)


main()
