# dev from vito
import pygame
from back_end import *
from bananinhas import *
from jogador import *
#inicia o pygame 
pygame.init()

# config tela
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Colete as Bananas🍌")
tela.fill((0,200,0))
#configurando o clock pro FPS pras bombinha ir devagar
clock = pygame.time.Clock()

#Imagem de fundo
background = pygame.image.load("image/background.jpg")
background = pygame.transform.scale(background,(800,500))

# printando o player
player = ("image/donkey.png",100,100,250,410)

running = True
while running:
    #começando o eventinho poggers
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
    # caralhadas de pontuação
    fonte = pygame.font.SysFont("Comic Sans",16,True,False)
    pontuação = fonte.render("Pontuação do El Primo: ",True,(255))
    tela.blit(pontuação,(0,2))
    #Colocar as imagens na screen
    tela.blit(background,(0,0))
    tela.blit(player,(0,0))
    # Atualizando a tela
    pygame.display.update()
    # Colocando o FPS
    clock.tick(60)

