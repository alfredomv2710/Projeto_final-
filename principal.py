from funcoes import embaralhar
import pygame
import random
pygame.init()

largura = 938
altura = 620
diametro = 5

white = (255, 255, 255)
green = (0, 255, 0)
green_table = (10, 75, 10)
black = (0, 0, 0)

window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Exemplo 3')

# TODO
posicoes_possiveis = []
aux = list(posicoes_possiveis)

img_da_carta = {}
valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
naipes = ['deespadas', 'decopas', 'deouros', 'depaus']

baralho = []
for valor in valores:
    for naipe in naipes:
        baralho.append(valor + naipe)
print(baralho)
random.shuffle(baralho)
j = 0
for ii in range(len(baralho)):
    carta_auxiliar = baralho[ii]
    i = ii % 13
    if i == 0:
        j += 1
    img_da_carta[carta_auxiliar] = [pygame.image.load(f"imgs/{carta_auxiliar}.jpg"), ((i + 1) * int(largura / 14), (j) * int(largura / 9))]

#print (img_da_carta)
centro = pygame.Vector2(largura / 2, 0)

continua = True
while continua:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continua = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continua = False
    # Para que serve os vetores?
    window.fill(green_table)

    # Comando para mostrar na tela
    for valor_e_naipe_da_carta in img_da_carta:
        carta = img_da_carta[valor_e_naipe_da_carta][0]
        rect = carta.get_rect()
        rect.center = img_da_carta[valor_e_naipe_da_carta][1]
        window.blit(carta, rect)
    pygame.display.update()

pygame.quit()