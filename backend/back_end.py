# dev from vito
import pygame
from bananinhas import *
from jogador import *
from bombinhas import * 
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

#Criando A BCTINHA DOS OBSTACULOS
array_obstaculos = [bananas("image/banana.png",100,100,0,0),
                            bananas("image/bomba.png",100,100,100,0),
                            bananas("image/bomba.png",100,100,150,0),
                            bananas("image/bomba.png",100,100,200,0),
                            bananas("image/bomba.png",100,100,250,0),
                            bananas("image/bomba.png",100,100,300,0),]
# printando o player
player = donkey("image/donkey.png",100,100,250,400)

running = True
while running:
    #começando o eventinho poggers
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
    
    #Colocar as imagens na screen
    tela.blit(background,(0,0))
    player.aparecer(tela)

    #macaco do krl se mexendo
    player.movimento(pygame.K_d,pygame.K_a)

    # percorre a lista de carrinhos pra aparecer o resto
    for bananicas in array_obstaculos:
        bananicas.movimenta()
        bananicas.apareca(tela)
        # pussyzinha de heatbox 
        if bananicas.mask.overlap(bananicas.mask,(bananicas.pos_x - bananicas.pos_x,bananicas.pos_y - bananicas.pos_y)):
            pass
        
    # caralhadas de pontuação
    fonte = pygame.font.SysFont("Comic Sans",30,True,False)
    pontuação = fonte.render("Pontuação: ",True,(232, 235, 52))
    tela.blit(pontuação,(0,2))

    # Atualizando a tela
    pygame.display.update()

    # Colocando o FPS
    clock.tick(60)

