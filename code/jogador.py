import pygame

class donkey:

    def __init__(self,arquivo_imagem,altura_imagem,largura_imagem,x_inicial,y_inicial):
        self.imagem = pygame.image.load(arquivo_imagem)
        self.altura = altura_imagem
        self.largura = largura_imagem
        self.pos_x = x_inicial
        self.pos_y = y_inicial
        # proporção da imagem
        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))
                # Posição do bonequinho main
        self.posição_x = x_inicial
        self.posição_y = y_inicial
        self.mask = pygame.mask.from_surface(self.imagem)

    def aparecer(self,tela):
        tela.blit(self.imagem,(self.posição_x,self.posição_y))
    
    def movimento(self,direita,esquerda): 
        keys = pygame.key.get_pressed()

        #Atualizando a posição do carrinho para direita
        if keys[direita]:
            if self.posição_x < 700:
                self.posição_x+=3

        if keys[esquerda]:
            if self.posição_x > 0:
                self.posição_x-=3