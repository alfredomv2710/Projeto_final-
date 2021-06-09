from funcoes import *
import pygame
import random
pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
green_table = (10, 75, 10)
black = (0, 0, 0)

window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Exemplo 3')

valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
naipes = ['deespadas', 'decopas', 'deouros', 'depaus']

img_da_carta = embaralhar(valores, naipes)
centro = pygame.Vector2(largura / 2, 0)

continua = True
while continua:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continua = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continua = False
            if event.key == pygame.K_r:
                img_da_carta = embaralhar(valores, naipes)
    # Para que serve os vetores?
    window.fill(green_table)

    # Comando para mostrar na tela
    for valor_e_naipe_da_carta in img_da_carta:
        carta = img_da_carta[valor_e_naipe_da_carta][0]
        rect = carta.get_rect()
        rect.center = img_da_carta[valor_e_naipe_da_carta][1]
        window.blit(carta, rect)
    texto(window, f'Paciência Acordeão', white, 25, largura / 2 - 90, 15)
    texto(window, f'Clique na carta que deseja empilhar', white, 25, 30, altura - 150)
    texto(window, f'Para finalizar, pressione ESC', white, 25, 30, altura - 130)
    texto(window, f'Pressione "R" para reiniciar o jogo ou embaralhar novamente', white, 25, 30, altura - 110)
    pygame.display.update()

pygame.quit()