#dev from vito
import pygame
import random


class Item:
    def __init__(self):

        self.banana = 0

        self.bomba = 0
        
        if random.randint(0,1) == 0:

            self.img = pygame.image.load("image/banana.png")

            self.banana = 1


        else:

            self.img = pygame.image.load("image/bomba.png")

            self.bomba = 1


        self.img = pygame.transform.scale(self.img,(75,75))
        self.mascara = pygame.mask.from_surface(self.img)

        self.pos_x = random.randint(0,725)
        self.pos_y = -100
        
        self.speed = random.randint(3,5)

        
    def load(self, tela):
        tela.blit(self.img,(self.pos_x,self.pos_y))

    #Movimento random
    def movimenta(self):
        self.pos_y +=self.speed

