import pygame
from aux_constantes import *
from aux_frames import Auxiliar
from class_enemy import Guard


class SpiritIx(Guard):
    def __init__(self, pos_x, pos_y, recorrido, screen):
        self.walk = {}
        self.walk[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\enemies\ix\talk.png",7,18, False, 1, True, 130, 100)[:122]
        self.walk[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\enemies\ix\talk.png",7,18, True, 1, True, 130, 100)[:122]      
        super().__init__(self.walk, pos_x, pos_y, 7, pos_x - recorrido, pos_x + recorrido, screen)
        self.rect_hitbox = pygame.Rect(pos_x + 20, pos_y + 10, 90, self.rect.h - 20)
        self.rect_collide_l = pygame.Rect(self.rect.x +20, self.rect_hitbox.y, 10, self.rect_hitbox.h-10)
        self.rect_collide_r = pygame.Rect(self.rect.x + self.rect.w -30, self.rect_hitbox.y, 10, self.rect_hitbox.h-10)
        self.damage = 25
        self.vida = 80
        self.puntos = 250

    def controlar_ruta(self):
        super().controlar_ruta()
        self.animacion = self.walk[self.direccion]

    def recibir_golpe(self,elemento):
        self.vida += -elemento.damage
        if self.vida < 1:
            self.activo = False
            elemento.master.score += self.puntos    

    def actualizar_posicion(self):
        self.rect.move_ip(self.move_x, self.move_y)
        self.rect_hitbox.move_ip(self.move_x, self.move_y)
        self.rect_collide_l.move_ip(self.move_x, self.move_y)
        self.rect_collide_r.move_ip(self.move_x, self.move_y)


    def actualizar(self, jugador, delta_ms):
        if self.activo:
            self.timer += delta_ms
            if self.timer > 30:
                self.timer = 0
                self.updatear_frames()
                self.controlar_ruta()
                self.actualizar_posicion()
                self.draw()
