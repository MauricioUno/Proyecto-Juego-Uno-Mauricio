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
        self.move_y = 0

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
        self.max_x = ANCHO_VENTANA + 300


    def actualizar_posicion(self):
        self.aux_y = int(math.sin(self.acumulador/50)*100 + self.move_y)
        self.acumulador += self.move_x
        self.new_y = int(math.sin(self.acumulador/50)*100 + self.move_y)
        self.move_y = self.new_y - self.aux_y
        self.rect.move_ip(self.move_x, self.move_y)




class Guard(ObjetoAnimado):
    def __init__(self, animacion, pos_x, pos_y, velocidad, screen):
        self.direccion = choice([DERECHA, IZQUIERDA])
        super().__init__(animacion[self.direccion], pos_x, pos_y, screen)
        self.velocidad = velocidad
        if self.direccion == IZQUIERDA:
            self.velocidad *= -1
        self.sobre_plataforma = False
        self.gravedad = 10

        self.move_x = self.velocidad
        self.move_y = 0
        self.activo = True
        self.vivo = True
        self.timer = 0

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
        self.rect_pies.move_ip(self.move_x, self.move_y)


    def actualizar(self, jugador, delta_ms, plataformas):
        if self.activo:
            self.timer += delta_ms
            if self.timer > 30:
                self.timer = 0
                self.updatear_frames()
                self.controlar_ruta(plataformas)
                self.aplicar_gravedad()
                self.actualizar_posicion()
                self.verificar_limite_y()
                # pygame.draw.rect(self.screen, C_GREEN_2, self.rect_collide_l)
                # pygame.draw.rect(self.screen, C_GREEN_2, self.rect_collide_r)
                # pygame.draw.rect(self.screen, C_GREEN_2, self.rect_pies)
                self.draw()

    def controlar_ruta(self, plataformas):
        for plataforma in plataformas:
            if self.rect_collide_r.colliderect(plataforma.rect) and self.direccion == DERECHA:
                self.move_x *= -1
                self.direccion = IZQUIERDA
                break
            elif self.rect_collide_l.colliderect(plataforma.rect) and self.direccion == IZQUIERDA:
                self.move_x *= -1
                self.direccion = DERECHA
                break

        self.sobre_plataforma = False
        for plataforma in plataformas:
            if self.rect_pies.colliderect(plataforma.rect_piso):
                self.sobre_plataforma = True
                self.move_y = plataforma.move_y         
                break

        self.animacion = self.walk[self.direccion]

    def aplicar_gravedad(self):
        if not self.sobre_plataforma:
            self.move_y = self.gravedad

    def verificar_limite_y(self):
        if self.rect_pies.y > ALTO_VENTANA + 200:
            self.activo = False


class StillShooter(ObjetoAnimado):
    def __init__(self, animacion, pos_x, pos_y, master, screen):
        self.direccion = choice([DERECHA, IZQUIERDA])
        super().__init__(animacion[self.direccion], pos_x, pos_y, screen)
        self.activo = True
        self.proyectiles = GrupoProyectiles(master, screen)
        self.atacando = False
        self.shoot_allowed = True
        self.timer = 0
        self.timer_disparo = 0
        self.move_x = 0
        self.move_y = 0
