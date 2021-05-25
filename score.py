import pygame
WHITE = 255, 255, 255
tamanho = 300, 300
tela=pygame.display.set_mode(tamanho)
#tela_retangulo=tela.get_rect()

class Placar:
    def __init__(self):
        pygame.font.init()
        self.fonte = pygame.font.Font(None, 36)
        self.pontos=10

    def contagem(self):
        self.text=self.fonte.render("Pontos = " + str(self.pontos), 1 , (255,255,255))
        self.textpos=self.text.get_rect()
        self.textpos.centerx=tela.get_width() /2
        tela.blit(self.text, self.textpos)
        tela.blit(tela, (0, 0))