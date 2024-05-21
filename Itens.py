import pygame
import random
class Item:

    def __init__(self,arquivo_imagem,largura_imagem,altura_imagem,):
        self.imagem = pygame.image.load(arquivo_imagem)

        self.largura = largura_imagem
        self.altura = altura_imagem

        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))

        self.pos_x = random.randint(0,800)
        self.pos_y = random.randint(0,500)

        self.velocidade = random.randint(1, 20)

        self.mascara = pygame.mask.from_surface(self.imagem)
    

    def movimenta(self):
        self.pos_y = self.pos_y + self.velocidade
        if self.pos_y > +270:
            self.pos_y = 0
            self.velocidade = random.randint(1, 5)


    def desenhar(self, tela):
        tela.blit(self.imagem,(self.pos_x,self.pos_y))        