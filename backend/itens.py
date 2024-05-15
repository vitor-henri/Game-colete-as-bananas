import pygame
import random


class itens:
    
    def __init__(self, imagem, pos_x, pos_y):
        self.imagem = imagem
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.velocidade = 5
        self.mask = pygame.mask.from_surface(self.imagem)

    
    def movimenta(self):
        self.pos_y += self.velocidade
        if self.pos_y == 800:
            self.pos_y = 0
    

    def apareca(self,tela):
        tela.blit(self.imagem,)

# imagens sendo carregadas
banana_imagem = pygame.image.load("image/banana.png")
bomba_imagem = pygame.image.load("image/bomba.png")



