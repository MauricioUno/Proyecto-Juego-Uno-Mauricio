import pygame
from aux_constantes import *

class Auxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path,columnas,filas,flip=False, step = 1, escalar = False, ancho = 0, alto = 0, repeat_frame = 1):
        lista = []
        surface_imagen = pygame.image.load(path).convert_alpha()

        fotograma_ancho = int(surface_imagen.get_width()/columnas)
        fotograma_alto = int(surface_imagen.get_height()/filas)
        
        for fila in range(filas):
            y = fila * fotograma_alto
            for columna in range(0,columnas,step):
                x = columna * fotograma_ancho
                surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto).convert_alpha()
                if(flip):
                    surface_fotograma = pygame.transform.flip(surface_fotograma,True,False).convert_alpha()

                if escalar:
                    surface_fotograma = pygame.transform.scale(surface_fotograma, (ancho, alto)).convert_alpha()

                for i in range(repeat_frame):
                    lista.append(surface_fotograma)
        return lista

    @staticmethod
    def getSurfaceFromSeparateFiles(path_format,quantity,flip=False,step = 1,scale=1,w=0,h=0,repeat_frame=1):
        lista = []
        for i in range(1,quantity+1):
            path = path_format.format(i)
            surface_fotograma = pygame.image.load(path).convert_alpha()
            fotograma_ancho_scaled = int(surface_fotograma.get_rect().w * scale)
            fotograma_alto_scaled = int(surface_fotograma.get_rect().h * scale)
            if(scale == 1 and w != 0 and h != 0):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(w, h)).convert_alpha()
            if(scale != 1):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha() 
            if(flip):
                surface_fotograma = pygame.transform.flip(surface_fotograma,True,False).convert_alpha() 
            
            for i in range(repeat_frame):
                lista.append(surface_fotograma)
        return lista






