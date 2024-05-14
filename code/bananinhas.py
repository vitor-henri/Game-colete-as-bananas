import pygame
import random
class bananas:
    
    def __init__(self,arquivo_imagem,largura_imagem,altura_imagem,x_inicial,y_inicial):
        self.imagem = pygame.image.load(arquivo_imagem)
        
        self.largura = largura_imagem
        self.altura = altura_imagem
        
        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))
        
        self.pos_x = x_inicial
        self.pos_y = y_inicial

        self.velocidade = 5
        self.mask = pygame.mask.from_surface(self.imagem)

    def apareca(self,tela):
        tela.blit(self.imagem,(self.pos_x,self.pos_y))

    def movimenta(self):
        self.pos_y += self.velocidade
        if self.pos_y < 800:
            self.pos_y = 0