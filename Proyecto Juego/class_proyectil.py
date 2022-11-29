import pygame
from class_A import ObjetoAnimado

class Proyectil(ObjetoAnimado):
    def __init__(self, animacion, pos_x, pos_y, minimo, maximo, velocidad, aux_x, aux_y, ancho, alto, damage, master, screen):
        self.proyectil = animacion
        self.min_x = minimo
        self.max_x = maximo
        self.move_x = velocidad
        self.activo = True
        self.damage = damage
        self.master = master
        super().__init__(self.proyectil, pos_x, pos_y, screen)
        self.rect_hitbox = pygame.Rect(pos_x + aux_x, pos_y + aux_y , ancho, alto)


    def actualizar_posicion(self):
        self.rect.x += self.move_x
        self.rect_hitbox.x += self.move_x


    def verificar_colision(self,objetivos):
        for objetivo in objetivos:
            if self.rect_hitbox.colliderect(objetivo.rect_hitbox) and objetivo.vida > 0:
                objetivo.recibir_golpe(self)
                self.activo = False


    def verificar_limite_x(self):
        if not (self.min_x < self.rect_hitbox.x and self.rect_hitbox.x < self.max_x):
            self.activo = False


    def actualizar_disparo(self, objetivos):
        self.updatear_frames()
        self.actualizar_posicion()
        self.verificar_colision(objetivos)
        self.verificar_limite_x()
        self.draw()

    

class GrupoProyectiles:
    def __init__(self, master, screen) -> None:
        self.lista_disparos = []
        self.master = master
        self.screen = screen


    def agregar_disparo(self, pos_x, pos_y, velocidad, aux_x, aux_y, ancho, alto, animacion, damage):
        disparo = Proyectil(animacion, pos_x, pos_y, -100, 1600, velocidad, aux_x, aux_y, ancho, alto, damage, self.master, self.screen)
        self.lista_disparos.append(disparo)

    def actualizar_disparos(self, objetivos):
        for disparo in self.lista_disparos:
            disparo.actualizar_disparo(objetivos)
            if not disparo.activo:
                self.lista_disparos.remove(disparo)




                
        


