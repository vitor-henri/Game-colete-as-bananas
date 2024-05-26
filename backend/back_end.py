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
player = donkey("image/donkey.png",100,100,250,395)

#SOUNDS

pygame.mixer.music.load("sounds/soundtrack.mp3")
pygame.mixer.music.set_endevent(pygame.USEREVENT)
pygame.mixer.music.play()


point_up = pygame.mixer.Sound("sound/bom.mp3")

point_down = pygame.mixer.Sound("sound/ruim.mp3")

power_sound = pygame.mixer.Sound("sound/power_sound.mp3")

#Obstáculos
obstaculos = []

#Pra tirar o bug chato 
poder_ativo = False

#contagem de itens ruins que ele pegou
itens_ruins = 0

running = True
while running:
    #começando o eventinho poggers
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False


    #macaco do krl se mexendo
    player.movimento(pygame.K_d,pygame.K_a)
    tela.blit(background,(0,0))


    # caralhadas de pontuação
    fonte = pygame.font.SysFont("Comic Sans",30,True,False)
    pontuação = fonte.render(f"Pontuação: ",True,(232, 235, 52))
    tela.blit(pontuação,(0,2))

    #OBSTACULOS
    if len(obstaculos) <= 7:
        novo_obstaculo = Item()  # Cria um novo obstáculo
        obstaculos.append(novo_obstaculo)  # Adiciona na lista de obstáculos
    for obstaculokk in obstaculos:
        if obstaculokk.pos_y > 600:
            obstaculos.remove(obstaculokk)
    

    # COLOCA OS OBSTACULOS NA TELA E CHECKA A COLISAO
    for obstaculo in obstaculos:
        obstaculo.load(tela)
        obstaculo.movimenta()


    #Colocar as imagens na screen
    player.aparecer(tela)


    # Atualizando a tela
    pygame.display.update()


    # Colocando o FPS
    clock.tick(60)

