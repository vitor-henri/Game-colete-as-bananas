# dev from vito
import pygame
import random
from jogador import *
from itens import *


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


# configurando a posição e o tamanho do donkey
player = donkey("image/donkey.png",100,100,250,400)


# array objetos caindo
objetos = []


running = True
while running:
    #começando o eventinho poggers
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
    

    #macaco do krl se mexendo
    player.movimento(pygame.K_d,pygame.K_a)


    # caralhadas de pontuação
    fonte = pygame.font.SysFont("Comic Sans",30,True,False)
    pontuação = fonte.render(f"Pontuação: ",True,(232, 235, 52))
    tela.blit(pontuação,(0,2))


    # randomizar os itens
    aleatorio = random.randint(0,1)


    # itens 
    if aleatorio == 0:
            objeto = itens(banana_imagem,0, random.randint(0,800))
            itens.apareca(tela)
            itens.movimenta
        

    if aleatorio == 1:
            objeto = itens(bomba_imagem,0, random.randint(0,800))
            objetos.append(objeto)
            itens.apareca(tela)
            itens.movimenta


    #Colocar as imagens na screen
    tela.blit(background,(0,0))
    player.aparecer(tela)


    # Atualizando a tela
    pygame.display.update()


    # Colocando o FPS
    clock.tick(60)

