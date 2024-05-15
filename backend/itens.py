import random
import pygame
from back_end import *
# Definindo a lista de itens (bananas e bombas)
itens = ['banana', 'bomba']

# Função para escolher um item aleatoriamente
def escolher_item():
    return random.choice(itens)


