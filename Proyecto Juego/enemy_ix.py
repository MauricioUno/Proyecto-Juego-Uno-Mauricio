import pygame
from aux_constantes import *
from aux_frames import Auxiliar
from class_enemy import Guard


class SpiritIx(Guard):
    def __init__(self, pos_x, pos_y, screen):
        self.walk = {}
        self.walk[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\enemies\ix\talk.png",7,18, False, 1, True, 130, 100)[:122]
        self.walk[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\enemies\ix\talk.png",7,18, True, 1, True, 130, 100)[:122]      
        super().__init__(self.walk, pos_x, pos_y, 7, screen)
        self.rect_hitbox = pygame.Rect(pos_x + 20, pos_y + 10, 90, self.rect.h - 20)
        self.rect_collide_l = pygame.Rect(self.rect.left + 20, self.rect_hitbox.y, 10, self.rect_hitbox.h-15)
        self.rect_collide_r = pygame.Rect(self.rect.right - 20, self.rect_hitbox.y, 10, self.rect_hitbox.h-15)
        self.rect_pies = pygame.Rect(self.rect_hitbox.centerx - self.rect_hitbox.w/4, self.rect_hitbox.bottom - 10, self.rect_hitbox.w/2, 10)
        self.damage = 20
        self.vida = 80
        self.puntos = 250
