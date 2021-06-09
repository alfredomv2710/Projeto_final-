from funcoes import *
import pygame
import random
pygame.init()   #inicia o pygame

#define a cor do fundo da tela interativa
white = (255, 255, 255) 
green = (0, 255, 0)
green_table = (10, 75, 10) 
black = (0, 0, 0)

window = pygame.display.set_mode((largura, altura)) #abre a tela com medidas já especificadas
pygame.display.set_caption('Paciência Acordeão') #exibe o nome da tela interativa

valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] #lista de valores das cartas
naipes = ['deespadas', 'decopas', 'deouros', 'depaus'] #lista de naipes das cartas

img_da_carta = embaralhar(valores, naipes) #criar todas as cartas possíveis com os valores e naipes passados anteriormente
centro = pygame.Vector2(largura / 2, 0) #posição da tela interativa

#entrando ou saindo do jogo
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
    # cor da tela interativa
    window.fill(green_table)

    # Comando para mostrar na tela
    for valor_e_naipe_da_carta in img_da_carta:
        carta = img_da_carta[valor_e_naipe_da_carta][0]
        rect = carta.get_rect()
        rect.center = img_da_carta[valor_e_naipe_da_carta][1]
        window.blit(carta, rect)
    texto(window, f'Paciência Acordeão', white, 25, largura / 2 - 90, 15)      #exibe o nome do jogo na tela do pygame e onde o nome deve aparecer na tela
    texto(window, f'Clique na carta que deseja empilhar', white, 25, 30, altura - 150) #exibe na tela do jogo de que maneira começar o jogo e onde isso deve aparecer na tela
    texto(window, f'Para finalizar, pressione ESC', white, 25, 30, altura - 130) #exibe na tela do jogo o que apertar para finalizar o jogo e onde isso deve aparecer na tela
    texto(window, f'Pressione "R" para reiniciar o jogo ou embaralhar novamente', white, 25, 30, altura - 110) #exibe na tela do jogo o que fazer para reiniciar o jogo ou embaralhar as cartas e onde isso deve aparecer na tela
    pygame.display.update()

pygame.quit()     #sai do pygame