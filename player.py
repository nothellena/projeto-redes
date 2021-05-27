import pygame

class Player():
    def __init__(self, x, y, width, height, color,type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Surface([width, height])
        self.vel = 3
        self.type = type
        self.image.fill(color)
        self.image.set_colorkey(color)
        self.rect = self.image.get_rect()

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if self.type == 'v':
            if keys[pygame.K_UP]:
                self.y -= self.vel
            if self.y < 0:
                self.y = 0

            if keys[pygame.K_DOWN]:
                self.y += self.vel
            if self.y > 200:
                self.y = 200

        if self.type == 'h':
            if keys[pygame.K_LEFT]:
                self.x -= self.vel
            if self.x < 0:
                self.x = 0

            if keys[pygame.K_RIGHT]:
                self.x += self.vel
            if self.x > 200:
                self.x = 200

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)