import pygame
from network import Network

pygame.init()

size = 300, 300
win = pygame.display.set_mode(size)
pygame.display.set_caption("Client")


def redrawWindow(win, players):
    win.fill((40, 42, 54))

    for player in players:
        player.draw(win)

    pygame.display.update()


def main():
    run = True
    n = Network()

    p = n.getPos()

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        players = n.send(p)
        p2, p3, p4 = players[0], players[1], players[2]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, [p, p2, p3, p4])


main()
