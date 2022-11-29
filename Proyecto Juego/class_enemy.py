import pygame
import math
from aux_constantes import *
from random import *
from class_A import ObjetoAnimado
from class_proyectil import GrupoProyectiles


class RandomGhost(ObjetoAnimado):
    def __init__(self, animacion, inversion, screen):
        self.acumulador = 0
        self.move_x = randint(5,9)
        self.move_y = randint(50,100)

        if inversion:
            self.move_x *= -1
            pos_x = randrange(ANCHO_VENTANA + 100, ANCHO_VENTANA + 200, 20)
        else:
            pos_x = randrange(-200, -100, 20)
        
        pos_y = randrange(200, ALTO_VENTANA/2, 20)
        super().__init__(animacion, pos_x, pos_y, screen)

        self.vivo = True
        self.activo = True
        self.timer = 0
        self.min_x = -300
        self.max_x = 1800


    def actualizar_posicion(self):
        self.aux_y = int(math.sin(self.acumulador/50)*100 + self.move_y)
        self.acumulador += self.move_x
        self.new_y = int(math.sin(self.acumulador/50)*100 + self.move_y)
        self.move_y = self.new_y - self.aux_y

        self.rect.move_ip(self.move_x, self.move_y)




class Guard(ObjetoAnimado):
    def __init__(self, animacion, pos_x, pos_y, velocidad, min_x, max_x, screen):
        self.direccion = choice([DERECHA, IZQUIERDA])
        super().__init__(animacion[self.direccion], pos_x, pos_y, screen)
        self.velocidad = velocidad
        self.move_x = self.velocidad
        self.move_y = 0
        self.maximo_x = max_x
        self.minimo_x = min_x
        self.activo = True
        self.vivo = True
        self.timer = 0


    def controlar_ruta(self):
        if self.direccion == IZQUIERDA:
            if self.rect.x > self.minimo_x:
                self.move_x = -self.velocidad
            else:
                self.direccion = DERECHA       
        else:
            if self.rect.x < self.maximo_x:
                self.move_x = self.velocidad
            else:
                self.direccion = IZQUIERDA




class StillShooter(ObjetoAnimado):
    def __init__(self, animacion, pos_x, pos_y, master, screen):
        super().__init__(animacion, pos_x, pos_y, screen)

        self.activo = True
        self.proyectiles = GrupoProyectiles(master, screen)
        self.atacando = False
        self.timer = 0
        self.shoot_allowed = True
        self.timer_disparo = 0
        self.move_x = 0
        self.move_y = 0


    def verificar_vision(self, jugadores):
        if self.shoot_allowed:
            for jugador in jugadores:
                if self.rect_vision.colliderect(jugador.rect_hitbox) and jugador.vida > 0:
                    self.atacando = True
                    break
                else:
                    self.atacando = False


    def actualizar_cooldown_disparo(self, delta_ms):
        if not self.shoot_allowed:
            self.timer_disparo += delta_ms
            if self.timer_disparo > 750:
                self.timer_disparo = 0
                self.shoot_allowed = True