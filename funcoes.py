import random
import pygame

#medidas/tamanho da tela
largura = 938  
altura = 620

def texto(window, msg, cor, tam, x, y): #função que define o local dos textos/mensagens
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    window.blit(texto1, [x, y])

def cria_baralho():   #função de criar o baralho para o jogo
    baralho = ["A♥️","2♥️","3♥️","4♥️","5♥️","6♥️","7♥️","8♥️","9♥️","10♥️","Q♥️","J♥️","K♥️","A♠️","2♠️","3♠️","4♠️","5♠️","6♠️","7♠️","8♠️","9♠️","10♠️","Q♠️","J♠️","K♠️","A♦️","2♦️","3♦️","4♦️","5♦️","6♦️","7♦️","8♦️","9♦️","10♦️","Q♦️","J♦️","K♦️","A♣️","2♣️","3♣️","4♣️","5♣️","6♣️","7♣️","8♣️","9♣️","10♣️","Q♣️","J♣️","K♣️"]
    random.shuffle(baralho)
    return baralho

def embaralhar(valores, naipes): #função de embaralhar as cartas
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


def extrai_naipe (card): #função que recebe uma carta (string) e devolve apenas o naipe dela (sem o valor)
    np = card[len(card)-1]
    return np
    
    
def extrai_valor(palavra): #função que recebe uma carta (string) e devolve apenas o valor dela (sem o naipe)
    if len (palavra)== 2:
        return palavra[0]
    elif len (palavra) == 3:
        return palavra [0] + palavra[1] 
        
        
def lista_movimentos_possiveis(baralho, posicao): #função que recebe um baralho representado como uma lista de strings e o índice (posição) de uma carta e devolve uma lista contendo os movimentos possíveis para essa carta
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
    
def empilha(baralho, origem, destino): #função que recebe um baralho representado por uma lista de cartas(strings), uma posição de origem e uma posição de destino e devolve um novo baralho (lista) com a carta da posição de origem no lugar da posição de destino e realizando as devidas movimentações nas cartas restantes
    baralho[destino] = baralho[origem]
    baralho.pop(origem)
    return baralho
    
def possui_movimentos_possiveis(baralho): #função que recebe um baralho representado por uma lista de strings e indica se há ou não movimentos possíveis sobrando
    for i in range(len(baralho)):
        if lista_movimentos_possiveis(baralho, i) != []:
            return True
    return False