import pygame
from aux_constantes import *
from aux_frames import Auxiliar
from class_enemy import RandomGhost
from random import choice

class Batterfly(RandomGhost):
    def __init__(self, screen):
        self.invertido = choice([True, False])
        self.fly= Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\enemies\batterfly\fly.png",8,5, self.invertido)
        super().__init__(self.fly, self.invertido, screen)
        self.rect_hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 10 , 65, 60)
        self.vida = 5
        self.damage = 20
        self.puntos = 50    
        self.timer_respawn = 0
    

    def actualizar_posicion(self):
        super().actualizar_posicion()
        self.rect_hitbox.move_ip(self.move_x, self.move_y)


    def recibir_golpe(self, proyectil):
        self.vida += -proyectil.damage
        if self.vida < 1:
            self.vivo = False
            proyectil.master.score += self.puntos


    def actualizar_cooldown_spawn(self, delta_ms):
        self.timer_respawn += delta_ms
        if self.timer_respawn > 1000:
            self.timer_respawn = 0
            self.acumulador = 0
            self.__init__(self.screen)
    

    def verificar_limite_x(self):
        if not (self.min_x < self.rect_hitbox.x and self.rect_hitbox.x < self.max_x):
            self.vivo = False


    def actualizar(self, jugador, delta_ms):
        if self.vivo:
            self.timer += delta_ms
            if self.timer > 30:
                self.timer = 0
                self.updatear_frames()
                self.actualizar_posicion()
                self.verificar_limite_x()
                self.draw()
        else:
            self.actualizar_cooldown_spawn(delta_ms)
        