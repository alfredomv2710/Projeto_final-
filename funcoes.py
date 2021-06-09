import random
import pygame

largura = 938
altura = 620

def texto(window, msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    window.blit(texto1, [x, y])

def cria_baralho():
    baralho = ["A♥️","2♥️","3♥️","4♥️","5♥️","6♥️","7♥️","8♥️","9♥️","10♥️","Q♥️","J♥️","K♥️","A♠️","2♠️","3♠️","4♠️","5♠️","6♠️","7♠️","8♠️","9♠️","10♠️","Q♠️","J♠️","K♠️","A♦️","2♦️","3♦️","4♦️","5♦️","6♦️","7♦️","8♦️","9♦️","10♦️","Q♦️","J♦️","K♦️","A♣️","2♣️","3♣️","4♣️","5♣️","6♣️","7♣️","8♣️","9♣️","10♣️","Q♣️","J♣️","K♣️"]
    random.shuffle(baralho)
    return baralho

def embaralhar(valores, naipes):
    img_da_carta = {}
    baralho = []
    for valor in valores:
        for naipe in naipes:
            baralho.append(valor + naipe)
    random.shuffle(baralho)
    j = 0
    for ii in range(len(baralho)):
        carta_auxiliar = baralho[ii]
        i = ii % 13
        if i == 0:
            j += 1
        img_da_carta[carta_auxiliar] = [pygame.image.load(f"imgs/{carta_auxiliar}.jpg"), ((i + 1) * int(largura / 14), (j) * int(largura / 9))]
    return img_da_carta


def extrai_naipe (card):
    np = card[len(card)-1]
    return np
    
    
def extrai_valor(palavra):
    if len (palavra)== 2:
        return palavra[0]
    elif len (palavra) == 3:
        return palavra [0] + palavra[1] 
        
        
def lista_movimentos_possiveis(baralho, posicao):
    movimentos = []
    
    card = baralho[posicao]
    naipe = extrai_naipe(card)
    valor = extrai_valor(card)

    if posicao == 0:
        return movimentos
    elif posicao <= 2:

        naipe_1 = extrai_naipe(baralho[posicao - 1])
        valor_1 = extrai_valor(baralho[posicao - 1])
    
        if naipe == naipe_1 or valor == valor_1:
            return [1]
        else:
            return []
    
    else:
        naipe_1 = extrai_naipe(baralho[posicao - 1])
        valor_1 = extrai_valor(baralho[posicao - 1])

        naipe_3 = extrai_naipe(baralho[posicao - 3])
        valor_3 = extrai_valor(baralho[posicao - 3])
        if naipe == naipe_1 or valor == valor_1:
            movimentos.append(1)
        if naipe == naipe_3 or valor == valor_3:
            movimentos.append(3)
    return movimentos
    
def empilha(baralho, origem, destino):
    baralho[destino] = baralho[origem]
    baralho.pop(origem)
    return baralho
    
def possui_movimentos_possiveis(baralho):
    for i in range(len(baralho)):
        if lista_movimentos_possiveis(baralho, i) != []:
            return True
    return False