import pygame

class donkey:

    #Atributos do persona
    def __init__(self,img, img_x,img_y, pos_x, pos_y ):
        self.imagem = pygame.image.load(img)

        self.width = img_x
        self.height = img_y

        self.imagem = pygame.transform.scale(self.imagem,(self.width,self.height))

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.mascara = pygame.mask.from_surface(self.imagem)

        self.power = 3

    #printando na tela
    def print_char(self, screen):
        screen.blit(self.imagem,(self.pos_x,self.pos_y))
    
    #moviment
    def movements(self, left_key, right_key):
        keys = pygame.key.get_pressed()

        #teclas
        if keys[left_key]:
            if self.pos_x > 0:
                self.pos_x = self.pos_x - 5
        
        if keys[right_key]:
            if self.pos_x < 800 - self.width:
                self.pos_x = self.pos_x + 5