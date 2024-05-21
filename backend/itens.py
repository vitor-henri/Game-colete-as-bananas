#dev from vito
import pygame
import random


class Item:
    
    def __init__(self):
        self.reset()
    
    def movimenta(self):
        self.pos_y += self.velocidade
        if self.pos_y == 800:
            self.pos_y = 0
    

    def apareca(self,tela):
        tela.blit(self.imagem,(self.pos_x,self.pos_y))
    
    def reset(self):
        aleatorio = random.randint(0,1)
        if aleatorio == 0:
            self.imagem = pygame.image.load("image/banana.png")
        else:
            self.imagem = pygame.image.load("image/bomba.png")
        self.imagem = pygame.transform.scale(self.imagem, (70, 70))
        self.altura = -self.imagem.get_height()
        self.largura = -self.imagem.get_width()
        self.pos_x = random.randint(0,800-70)
        self.pos_y = -self.altura
        self.velocidade = random.randint(0,5)
        self.mask = pygame.mask.from_surface(self.imagem)

