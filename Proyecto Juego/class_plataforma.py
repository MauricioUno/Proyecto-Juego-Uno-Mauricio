import pygame
from aux_constantes import *
from class_A import Imagen
from math import *
import re

class Plataforma(Imagen):
    def __init__(self, pos_x, pos_y, ancho, alto, tipo, terreno, screen) -> None:
        super().__init__("/tile/{0}.png".format(tipo), ancho, alto, pos_x, pos_y, screen)
        self.rect_piso = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, 10)
        self.terreno = terreno
        self.move_x = 0
        self.move_y = 0
        self.timer = 0
        
    def actualizar_posicion(self):
        self.rect.move_ip(self.move_x, self.move_y)
        self.rect_piso.move_ip(self.move_x, self.move_y)

    def actualizar_plataforma(self, delta_ms):
        self.timer += delta_ms
        if self.timer > 30:
            self.timer = 0
            self.draw()




class PlatMov(Plataforma):
    def __init__(self, pos_x, pos_y, ancho, alto, tipo, speed, ruta, move, screen) -> None:
        super().__init__(pos_x, pos_y, ancho, alto, tipo, False, screen)
        self.speed = speed
        self.counter = 0
        self.movimiento = move
        try:
            self.max = abs(ruta // speed)
        except:
            self.max = 0


    def controlar_movimiento(self):
        self.counter += 1
        if self.counter > self.max:
            self.speed *= -1
            self.counter = 0
    
        self.move_x = self.speed
        self.move_y = self.speed
    

    def tipo_de_movimiento(self):
        if not re.search("diagonal", self.movimiento, re.IGNORECASE):

            if re.search("horizontal", self.movimiento, re.IGNORECASE):
                self.move_y = 0
            
            elif re.search("vertical", self.movimiento, re.IGNORECASE):
                self.move_x = 0


    def actualizar_plataforma(self, delta_ms):
        self.timer += delta_ms
        if self.timer > 30:
            self.timer = 0
            self.controlar_movimiento()
            self.tipo_de_movimiento()
            self.actualizar_posicion()
            self.draw()




class PlatMovExponencial(Plataforma):
    def __init__(self, pos_x, pos_y, ancho, alto, tipo, speed, move_x, move_y, screen) -> None:
        super().__init__(pos_x, pos_y, ancho, alto, tipo, False, screen)
        self.angle = 0
        self.speed = speed / 100
        self.x = move_x
        self.y = move_y


    def actualizar_movimiento(self):
        self.aux_x = (self.x) * cos(self.angle) 
        self.aux_y = (self.y) * sin(self.angle)
        self.angle += self.speed
        self.new_x = (self.x) * cos(self.angle) 
        self.new_y = (self.y) * sin(self.angle)

        self.move_x = int(self.new_x - self.aux_x)
        self.move_y = int(self.new_y - self.aux_y)


    def actualizar_plataforma(self, delta_ms):
        self.timer += delta_ms
        if self.timer > 30:
            self.timer = 0
            self.actualizar_movimiento()
            self.actualizar_posicion()
            self.draw()


class ListaPlataformas:
    def __init__(self,lista_plataformas, screen, name) -> None:
        self.lista = []
        self.screen = screen
        self.name = name

        if "terreno" in lista_plataformas.keys():
            self.agregar_terreno(lista_plataformas["terreno"])

        if "movHorizontal" in lista_plataformas.keys():
            self.agregar_plataforma_mov(lista_plataformas["movHorizontal"], "horizontal")

        if "movVertical" in lista_plataformas.keys():
            self.agregar_plataforma_mov(lista_plataformas["movVertical"], "vertical")

        if "movCircular" in lista_plataformas.keys():
            self.agregar_plataforma_mov_circular(lista_plataformas["movCircular"])


    def agregar_terreno(self, lista_plataformas):
        for dato in lista_plataformas:
            pos_y = dato["pos"][1]
            for y in range(dato["cant"][1]):
                pos_x = dato["pos"][0]
                for x in range(dato["cant"][0]):
                    tile = "{0}/{1}".format(self.name, dato["tipo"])
                    plataforma = Plataforma(pos_x, pos_y, dato["dim"][0], dato["dim"][1], tile, True, self.screen)
                    self.lista.append(plataforma)
                    pos_x += dato["dim"][0]
                pos_y += dato["dim"][1]


    def agregar_plataforma_mov(self, lista_plataformas, move):
        for dato in lista_plataformas:
            tile = "{0}/{1}".format(self.name, dato["tipo"])
            plataforma = PlatMov(dato["pos"][0], dato["pos"][1], dato["dim"][0], dato["dim"][1], tile, dato["speed"], dato["route"], move, self.screen)
            self.lista.append(plataforma)

    
    def agregar_plataforma_mov_circular(self, lista_plataformas):
        for dato in lista_plataformas:
            tile = "{0}/{1}".format(self.name, dato["tipo"])
            plataforma = PlatMovExponencial(dato["pos"][0], dato["pos"][1], dato["dim"][0], dato["dim"][1], tile, dato["speed"], dato["move"][0], dato["move"][1], self.screen)
            self.lista.append(plataforma)

    
    def actualizar(self, delta_ms):
        for plataforma in self.lista:
            plataforma.actualizar_plataforma(delta_ms)



