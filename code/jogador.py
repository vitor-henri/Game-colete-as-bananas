import pygame

class donkey:

    def __init__(self,arquivo_imagem,altura_imagem,largura_imagem,x_inicial,y_inicial):
        self.imagem = pygame.image.load(arquivo_imagem)
        self.altura = altura_imagem
        self.largura = largura_imagem
        