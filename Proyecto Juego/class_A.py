from aux_constantes import *
from random import choice
import pygame

class ObjetoAnimado:
    def __init__(self, animacion, pos_x, pos_y, screen):
        self.screen = screen
        self.animacion = animacion
        self.frame = 0
        self.imagen = self.animacion[self.frame]
        self.rect = self.imagen.get_rect(x = pos_x, y = pos_y)


    def updatear_frames(self):
        if(self.frame < len(self.animacion) - 1):
            self.frame += 1 
        else: 
            self.frame = 0


    def draw(self):
        self.imagen = self.animacion[self.frame]
        self.screen.blit(self.imagen,self.rect)



class Imagen:
    def __init__(self, path_imagen, ancho, alto, pos_x, pos_y, screen) -> None:
        self.imagen = pygame.image.load(PATH_RECURSOS + path_imagen).convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto)).convert_alpha()
        self.rect = self.imagen.get_rect(x = pos_x, y = pos_y)
        self.screen = screen

    
    def draw(self):
        self.screen.blit(self.imagen, self.rect)



