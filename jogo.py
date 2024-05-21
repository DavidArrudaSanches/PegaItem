import pygame
import random
from personagem import personagem
from Itens import Item
pygame.init()

#Constrindo a tela
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("JOGO")
tela.fill((80,120,200))

jogador = personagem("Imagens/Cachorro.gif",150,100,300,270)

lista_pato=[Item("Imagens/pato.png",80,70,),
            Item("Imagens/pato.png",80,70,),
            Item("Imagens/pato.png",80,70,),
            Item("Imagens/pato.png",80,70,),]

FUNDO = pygame.image.load("Imagens/Fundo.png")
FUNDO = pygame.transform.scale(FUNDO,(800,500))

fonte = pygame.font.SysFont("Castellar",14)
clock = pygame.time.Clock()


rodando = True
while rodando:
    #Tratando eventos
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("Você clicou!!")
        if evento.type == pygame.QUIT:
            rodando = False
    tela.blit(FUNDO,(0,0))
    
    for pato in lista_pato:
        pato.movimenta()   
        pato.desenhar(tela)

        if jogador.mascara.overlap(pato.mascara,(pato.pos_x-jogador.pos_x , pato.pos_y-jogador.pos_y)):
            jogador.pontuacao += 1
            pato.movimenta()
            pato.desenhar(tela)
    
    
    texto_pontuacao = fonte.render(f"Pontuação: {jogador.pontuacao}",True,(255,0,0))
    tela.blit(texto_pontuacao,(0,10))
    
    jogador.movimentar_via_controle(pygame.K_RIGHT,pygame.K_LEFT)
    jogador.desenhar(tela)
    
    pygame.display.update()
    clock.tick(60)