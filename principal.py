import pygame

pygame.init()

largura = 500
altura = 400
diametro = 5

white = (255, 255, 255)
black = (0, 0, 0)

window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Exemplo 3')

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
    if pos.y > altura:
        v = -v
        #print(v)
    v += a
    pos += v
    pygame.draw.circle(window, white, pos, diametro)
    pygame.display.update()

pygame.quit()