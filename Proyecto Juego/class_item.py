import pygame
import re
from aux_constantes import *
from class_A import *

class Item(Objeto):
    def __init__(self, tipo, ancho, alto, pos_x, pos_y, efecto, screen) -> None:
        super().__init__("/items/{0}.png".format(tipo), ancho, alto, pos_x, pos_y, screen)
        self.activo = True
        self.timer = 0
        self.efecto = efecto


    def verificar_colision(self, objetivos, enemigos):
        for objetivo in objetivos:
            if self.rect.colliderect(objetivo.rect_hitbox):
                self.activo = False
                self.master_form.play_efecto_sonido("collect")
                self.aplicar_efecto(objetivo, enemigos)
    


    def aplicar_efecto(self, objetivo, enemigos):
        if re.search("score", self.efecto, re.IGNORECASE):
            objetivo.score += 200

        elif re.search("spawn", self.efecto, re.IGNORECASE):
            objetivo.score += 1000
            enemigos.agregar_batterfly(3, self.master_form)

        elif re.search("ammo", self.efecto, re.IGNORECASE):
            objetivo.municion += 5
        
        
    def actualizar(self, delta_ms, objetivos, enemigos):
        if self.activo:
            self.timer += delta_ms
            if self.timer > 30:
                self.timer = 0
                self.verificar_colision(objetivos, enemigos)
                self.draw()



class ListaItems:
    def __init__(self, lista_items, screen, enemigos) -> None:
        self.lista = []
        self.master_form = screen
        self.lista_enemigos = enemigos
        self.agregar_item(lista_items)


    def agregar_item(self, lista_items):
        for item in lista_items:
            aux_item = Item(item["item"], item["dimension"][0], item["dimension"][1], item["coordenadas"][0], item["coordenadas"][1],item["efecto"], self.master_form)
            self.lista.append(aux_item)

    def actualizar(self, delta_ms, objetivos):
        for item in self.lista:
            item.actualizar(delta_ms, objetivos, self.lista_enemigos)
            if not item.activo:
                self.lista.remove(item)