##### DS-404: Maria da Guia Rocha Barbosa RA 17412 - 20201103 ####
# Jogo da cobra
# Comandos: setas ou w-a-s-z


import pygame, random, sys

# Funcao de aleatoriedade dos pontos
def on_grid_random():
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)