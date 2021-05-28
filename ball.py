import pygame
from random import randint

BG = 40, 42, 54
GREEN = 80, 250, 123


class Ball():

    def __init__(self, x,y,color, width, height):

        self.x = x
        self.y = y
        self.scoreA = 0
        self.scoreB = 0
        self.type = 'b'
        self.color = color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.image.set_colorkey(color)

        self.velocity = [randint(4, 8), randint(-8, 8)]

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):

        self.x += self.velocity[0]
        self.y += self.velocity[1]

        if self.x >= 690:
            self.velocity[0] = -self.velocity[0]
            self.scoreA+=1
            self.x += self.velocity[0]
        if self.x <= 0:
            self.velocity[0] = -self.velocity[0]
            self.scoreB += 1
            self.x += self.velocity[0]
        if self.y >= 490:
            self.velocity[1] = -self.velocity[1]
            self.y += self.velocity[1]
        if self.y <= 0:
            self.velocity[1] = -self.velocity[1]
            self.y += self.velocity[1]

        self.update()

    def update(self):
        self.rect = (self.x, self.y, 10, 10)

    def check_collision(self, obj):
        if obj.x <= self.x <= obj.x + 10 and obj.y <= self.y <= obj.y + 50:
            self.bounce()

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)






