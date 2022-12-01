from aux_constantes import *
from aux_frames import Auxiliar
import pygame
from class_enemy import StillShooter

class SpiritGroodle(StillShooter):

    def __init__(self, pos_x, pos_y, screen) -> None:
        self.stay = {}
        self.stay[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\enemies\groodle\stay.png",9,10, False, 1, True, 100, 130)[:85]
        self.stay[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\enemies\groodle\stay.png",9,10, True, 1, True, 100, 130)[:85]
        self.attack = {}
        self.attack[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\enemies\groodle\attack.png",9,2, False, 1, True, 100, 130)[:17]
        self.attack[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\enemies\groodle\attack.png",9,2, True, 1, True, 100, 130)[:17]       
        self.shoot = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\enemies\groodle\proyectil.png",10,2)

        
        super().__init__(self.stay, pos_x, pos_y, self, screen)
        self.rect_hitbox = pygame.Rect(pos_x + 15, pos_y + 30, 70, 70)
        self.rect_vision_r = pygame.Rect(self.rect_hitbox.right, self.rect.y, 600, 100)
        self.rect_vision_l = pygame.Rect(self.rect_hitbox.left - 600, self.rect.y, 600, 100)

        self.damage = 15
        self.dmg_shoot = 20
        self.vida = 100
        self.puntos = 500


    def verificar_vision(self, jugadores):
        if self.shoot_allowed:
            for jugador in jugadores:
                if self.rect_vision_l.colliderect(jugador.rect_hitbox):
                    self.direccion = IZQUIERDA
                    self.velocidad = -15
                    self.disparar()
                    break
                elif self.rect_vision_r.colliderect(jugador.rect_hitbox):
                    self.direccion = DERECHA
                    self.velocidad = 15
                    self.disparar()
                    break
                else:
                    self.atacando = False


    def disparar(self):
        self.atacando = True
        self.shoot_allowed = False
        self.proyectiles.agregar_disparo(self.rect.x + 15, self.rect.y + 60, self.velocidad, 35, 10, 15, 15, self.shoot, self.dmg_shoot)


    def actualizar_cooldown_disparo(self, delta_ms):
        if not self.shoot_allowed:
            self.timer_disparo += delta_ms
            if self.timer_disparo > 750:
                self.timer_disparo = 0
                self.shoot_allowed = True


    def animaciones(self):
        if not self.atacando:
            self.cambiar_animacion(self.stay)
        else:
            self.cambiar_animacion(self.attack)


    def cambiar_animacion(self, animacion):
        if self.animacion != animacion[DERECHA] and self.animacion != animacion[IZQUIERDA]:
            self.frame = 0
        self.animacion = animacion[self.direccion]


    def recibir_golpe(self, elemento):
        self.vida += -elemento.damage
        if self.vida < 1:
            self.activo = False
            elemento.master.score += self.puntos
        
    
    def actualizar_posicion(self):
        self.rect.move_ip(self.move_x, self.move_y)
        self.rect_hitbox.move_ip(self.move_x, self.move_y)
        self.rect_vision_l.move_ip(self.move_x, self.move_y)
        self.rect_vision_r.move_ip(self.move_x, self.move_y)


    def actualizar(self, jugador, delta_ms, plataformas):
        if self.activo:
            self.timer += delta_ms
            if self.timer > 30:
                self.timer = 0
                self.verificar_vision([jugador])
                self.actualizar_cooldown_disparo(delta_ms)
                self.actualizar_posicion()
                self.animaciones()
                self.updatear_frames()
                self.proyectiles.actualizar_disparos([jugador])
                self.draw()
