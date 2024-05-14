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

#Imagem de fundo
background = pygame.image.load("imagens/estrada.png")
background = pygame.transform.scale(background,(800,500))

# configurando os jogadores na tela
jogador = jogador_elprimo("Imagens/normal.png",100,100,250,410)
jogador2 = jogador_elprimo("Imagens/colt.png",100,100,350,410)

# caralhadas de pontuação
fonte = pygame.font.SysFont("Comic Sans",16,True,False)

#Criando A BCTINHA DOS OBSTACULOS
array_carrinhos = [obstaculo("imagens/carro-1.png",120,50,950,50),
                            obstaculo("imagens/carro-2.png",120,50,950,100),
                            obstaculo("imagens/carro-3.png",120,50,950,150),
                            obstaculo("imagens/carro-1.png",120,50,950,200),
                            obstaculo("imagens/carro-2.png",120,50,950,250),
                            obstaculo("imagens/carro-3.png",120,50,950,370),]

#configurando o clock pro FPS pro carrinho nao ir rapido
clock = pygame.time.Clock()

running = True 
while running:
    # Fazendo o eventinho poggers
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
    tela.fill((0,200,0))

    tela.blit(background,(0,0))

    jogador.movimento(pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT,pygame.K_e)
    jogador.aparecer(tela)

    jogador2.movimento(pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_a,0)
    jogador2.aparecer(tela)
    # percorre a lista de carrinhos pra aparecer o resto
    for carro in array_carrinhos:
        carro.movimenta()
        carro.apareca(tela)
        # pussyzinha de heatbox 
        if jogador.mask.overlap(carro.mask,(jogador.posição_x - carro.pos_x,jogador.posição_y - carro.pos_y)):
            jogador.posição_x = 250
            jogador.posição_y = 400
        
        if jogador2.mask.overlap(carro.mask,(jogador2.posição_x - carro.pos_x,jogador2.posição_y - carro.pos_y)):
            jogador2.posição_x = 350
            jogador2.posição_y = 400              


    texto_pontos_elprimo = fonte.render("Pontuação do El Primo: ",True,(255))
    texto_pontos_colt = fonte.render("Pontuação do Colt: ",True,(0,0,255))
    tela.blit(texto_pontos_elprimo,(0,2))
    tela.blit(texto_pontos_colt,(0,20))
    # Atualizando a tela
    pygame.display.update()
    # Colocando o FPS
    clock.tick(60)