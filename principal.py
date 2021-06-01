import pygame
import random
pygame.init()

largura = 940
altura = 620
diametro = 5

white = (255, 255, 255)
black = (0, 0, 0)

window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Exemplo 3')

# TODO
posicoes_possiveis = []
aux = list(posicoes_possiveis)

img_da_carta = {}
'''valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
naipes = ['♠', '♥', '♦', '♣']'''
valores = ['A', '2']
naipes = ['♣']

for valor in valores:
    for naipe in naipes:
        carta_auxiliar = valor + naipe
        img_da_carta[carta_auxiliar] = [pygame.image.load(f"imgs\{carta_auxiliar}.jpg"), (random.randint(10, largura), random.randint(10, altura))]

centro = pygame.Vector2(largura / 2, 0)
vx = 0
vy = 0
v = pygame.Vector2(vx, vy)

ax = 0
ay = 0.0001 # simula a gravidade
a = pygame.Vector2(ax, ay)

pos = centro + v

continua = True
while continua:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continua = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continua = False
    # Para que serve os vetores?
    window.fill((0, 0, 0))

    # Comando para mostrar na tela
    for valor_e_naipe_da_carta in img_da_carta:
        carta = img_da_carta[valor_e_naipe_da_carta][0]
        rect = carta.get_rect()
        rect.center = img_da_carta[valor_e_naipe_da_carta][1]
        window.blit(carta, rect)
    if pos.y > altura:
        v = -v
        #print(v)
    v += a
    pos += v
    pygame.draw.circle(window, white, pos, diametro)
    pygame.display.update()

pygame.quit()