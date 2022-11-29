import pygame
import re
from aux_constantes import *
from class_A import *
from aux_frames import *

class Portal(ObjetoAnimado):
    def __init__(self, pos_x, pos_y, screen, nivel):
        self.stay = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "/items/portal_{0}.png".format(nivel), 7, 9) [:60]
        super().__init__(self.stay, pos_x, pos_y, screen)
        self.rect_hitbox = pygame.Rect(self.rect.x + self.rect.w/4, self.rect.y + 30, self.rect.w/2, self.rect.h - 30)
        self.timer = 0


    def verificar_colision(self, objetivos):
        for objetivo in objetivos:
            if self.rect_hitbox.colliderect(objetivo.rect_hitbox):
                objetivo.is_on_portal = True
            else:
                objetivo.is_on_portal = False

    

    def actualizar(self, objetivos, delta_ms):
        self.timer += delta_ms
        if self.timer > 30:
            self.timer = 0
            self.updatear_frames()
            self.verificar_colision(objetivos)
            self.draw()
