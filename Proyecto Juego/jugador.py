from aux_constantes import *
from aux_frames import Auxiliar
from class_proyectil import GrupoProyectiles
import pygame

class Jugador:
    def __init__(self, pos_x, pos_y, screen, form) -> None:
        self.form = form
        self.screen = screen
        self.direccion = DERECHA
        self.stay = {}
        self.stay[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\players\stink\idle_plus.png",26,2)[:51]
        self.stay[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\players\stink\idle_plus.png",26,2,True)[:51]
        
        self.walk = {}
        self.walk[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\players\stink\walk.png",15,1)[:12]
        self.walk[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\players\stink\walk.png",15,1,True)[:12]

        self.jump = {}
        self.jump[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\players\stink\jump.png", 33, 1)[:23]
        self.jump[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\players\stink\jump.png", 33, 1, True)[:23]

        self.fall = {}
        self.fall[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\players\stink\jump.png", 33, 1)[22:28]
        self.fall[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\players\stink\jump.png", 33, 1, True)[22:28]
        
        
        self.animacion = self.stay[self.direccion]
        self.frame = 0
        self.imagen = self.animacion[self.frame]
        self.rect = self.imagen.get_rect(x = pos_x, y = pos_y)
        self.rect_pies = pygame.Rect(self.rect.centerx - self.rect.w/4, self.rect.y + self.rect.h -10, self.rect.w/2 + 5, 10)
        self.rect_cabeza = pygame.Rect(self.rect.centerx - self.rect.w/4, self.rect.y + 10, self.rect.w/2 + 5, 10)
        self.rect_hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 10, self.rect.w - 30, self.rect.h - 15)
        self.rect_der = pygame.Rect(self.rect.centerx + 30, self.rect.y + 20, 10, self.rect.h-37)
        self.rect_izq = pygame.Rect(self.rect.centerx - 30, self.rect.y +20, 10, self.rect.h-37)
        self.move_x = 0
        self.move_y = 0

        self.speed_walk = {}
        self.speed_walk[DERECHA] = 10
        self.speed_walk[IZQUIERDA] = -10

        self.sobre_plataforma = True
        self.caminando = False
        self.saltando = False
        self.cayendo = False

        self.speed_jump = 10
        self.gravedad = 10
        self.inicio_salto = self.rect_pies.y

        self.move_allowed = {}
        self.move_allowed[DERECHA] = True
        self.move_allowed[IZQUIERDA] = True

        self.speed_shoot = {}
        self.speed_shoot[DERECHA] = 20
        self.speed_shoot[IZQUIERDA] = -20
        self.orb = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\players\stink\disparo_animacion.png",16,2)[:31]
        self.municion = 10
        self.proyectiles = GrupoProyectiles(self, self.screen)
        self.timer_disparo = 0
        self.shoot_allowed = True


        self.invulnerable = False
        self.golpeado = False
        self.hitted = {}
        self.hitted[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\players\stink\surprise.png",21,1)[:13]
        self.hitted[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\players\stink\surprise.png",21,1, True)[:13]
        self.timer_invulnerable = 0
        self.timer = 0

        self.vida = 100
        self.vivo = True
        self.death = {}
        self.death[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS +  r"\players\stink\angry.png",20,1,False, repeat_frame=2)[8:26]
        self.death[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS +  r"\players\stink\angry.png",20,1,True,repeat_frame=2)[8:26]
        self.activo = True
        self.score = 0
        self.is_on_portal = False
        self.win = False
        self.lose = False

    def mover(self,direccion):
        if not self.golpeado:
            self.direccion = direccion
            self.caminando = True
            if self.move_allowed[self.direccion]:
                self.move_x = self.speed_walk[self.direccion]
            
    def detener(self):
        if not self.golpeado:
            self.caminando = False
            self.move_x = 0


    def saltar(self, saltar):
        if not self.golpeado:
            if saltar:
                if self.sobre_plataforma:
                    self.saltando = True
                    self.move_x = 0
                    self.move_y = -self.speed_jump
                    self.inicio_salto = self.rect_pies.y
            else:
                self.saltando = False


    def limitar_salto(self):
        if self.rect_pies.y < self.inicio_salto - 150:
            self.saltando = False


    def verificar_plataforma(self, plataformas):
        if not self.saltando and not self.golpeado:
            self.sobre_plataforma = False
            for plataforma in plataformas:
                if self.rect_pies.colliderect(plataforma.rect_piso):
                    self.move_y = plataforma.move_y
                    self.sobre_plataforma = True
                    if self.move_allowed[self.direccion]:
                        if self.caminando:
                            self.move_x = self.speed_walk[self.direccion] + plataforma.move_x
                        else:
                            self.move_x = plataforma.move_x
                        
                    break
        else:
            for plataforma in plataformas:
                if self.rect_cabeza.colliderect(plataforma.rect) and plataforma.terreno:
                    self.saltando = False

    
    def verificar_paredes(self, plataformas):
        self.move_allowed[DERECHA] = True
        self.move_allowed[IZQUIERDA]= True

        for plataforma in plataformas:
            if plataforma.terreno:
                if self.rect_izq.colliderect(plataforma.rect) and self.move_allowed[IZQUIERDA]:
                    self.move_allowed[IZQUIERDA] = False
                    self.move_x = 0
                
                if self.rect_der.colliderect(plataforma) and self.move_allowed[DERECHA]:
                    self.move_allowed[DERECHA] = False
                    self.move_x = 0


    def aplicar_gravedad(self):
        if not self.golpeado and not self.saltando:
            if not self.sobre_plataforma:
                self.move_y = self.gravedad
                self.cayendo = True
            else:
                self.cayendo = False


    def disparar(self):
        if self.municion > 0 and not self.golpeado and self.shoot_allowed:
            self.shoot_allowed = False  
            self.proyectiles.agregar_disparo(self.rect.centerx, self.rect.centery, self.speed_shoot[self.direccion], 0, 0, 30, 30, self.orb, 25)
            self.municion -= 1

    def cooldown_disparo(self, delta_ms):
        if not self.shoot_allowed:
            self.timer_disparo += delta_ms
            if self.timer_disparo > 250:
                self.timer_disparo = 0
                self.shoot_allowed = True


    def recibir_golpe(self, atacante):
        if not self.invulnerable:
            self.modificar_vida(-atacante.damage)
            self.golpeado = True
            self.invulnerable = True
            self.saltando = False
            
            self.move_x = -self.speed_walk[self.direccion] / 2
            self.move_y = -2
            
            
    def modificar_vida(self,modificacion):
        self.vida += modificacion
        if self.vida < 1:
            self.vivo = False


    def cooldown_invulnerabilidad(self, delta_ms):
        if self.invulnerable:
            self.timer_invulnerable += delta_ms
            if self.timer_invulnerable > 1000:
                self.timer_invulnerable = 0
                self.invulnerable = False


    def verificar_colision_enemigos(self,enemigos):
        for enemigo in enemigos:
            if self.rect_hitbox.colliderect(enemigo.rect_hitbox) and enemigo.vida > 0:
                self.recibir_golpe(enemigo)



    def animaciones(self):
        if self.vivo:
            if not self.golpeado:
                if self.saltando:
                    self.cambiar_animacion(self.jump)
                else:
                    if self.cayendo:
                        self.cambiar_animacion(self.fall)
                    else:
                        if self.caminando:
                            self.cambiar_animacion(self.walk)
                        else:
                            self.cambiar_animacion(self.stay)
            else:
                self.cambiar_animacion(self.hitted)
        else:
            self.cambiar_animacion(self.death)


    def cambiar_animacion(self, animacion):
        if self.animacion != animacion[DERECHA] and self.animacion != animacion[IZQUIERDA]:
            self.frame = 0
        self.animacion = animacion[self.direccion]

         
    def actualizar_posicion(self):
    
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        self.rect_pies.x += self.move_x
        self.rect_pies.y += self.move_y
        self.rect_cabeza.x += self.move_x
        self.rect_cabeza.y += self.move_y
        self.rect_hitbox.x += self.move_x
        self.rect_hitbox.y += self.move_y
        self.rect_der.x += self.move_x
        self.rect_der.y += self.move_y
        self.rect_izq.x += self.move_x
        self.rect_izq.y += self.move_y


    def updatear_frames(self):
        if(self.frame < len(self.animacion) - 1):
            self.frame += 1 
        else:
            self.frame = 0

            if not self.vivo:
                self.activo = False

            if self.golpeado:
                self.golpeado = False
                self.detener()
            
            if self.cayendo:
                self.frame = len(self.animacion) - 1

    
    def draw(self):
        self.imagen = self.animacion[self.frame]
        self.form.surface.blit(self.imagen,self.rect)
        # pygame.draw.rect(self.form.surface, C_BLACK, self.rect_cabeza)
        # pygame.draw.rect(self.form.surface, C_BLACK, self.rect_pies)
        # pygame.draw.rect(self.form.surface, C_BLACK, self.rect_der)
        # pygame.draw.rect(self.form.surface, C_BLACK, self.rect_izq)

    def controles(self, lista_eventos, teclas_presionadas):
        
        for event in lista_eventos:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.saltar(True)

                if event.key == pygame.K_z:
                    self.disparar()

                if event.key == pygame.K_a:
                    if self.is_on_portal:
                        self.win = True

                    

        if teclas_presionadas[pygame.K_LEFT] and not teclas_presionadas[pygame.K_RIGHT] :
            self.mover(IZQUIERDA)

        elif teclas_presionadas[pygame.K_RIGHT] and not teclas_presionadas[pygame.K_LEFT] :
            self.mover(DERECHA)
        
        else:
            self.detener()


        if teclas_presionadas[pygame.K_SPACE]:
            self.limitar_salto()
        else:
            self.saltar(False)


    def verificar_limite_y(self):
        if self.rect_pies.y > ALTO_VENTANA + 200:
            self.modificar_vida(-100)
    

    def actualizar(self, plataformas, objetivos, delta_ms, lista_eventos, teclas_presionadas):
        if self.activo:
            self.timer += delta_ms
            if self.timer > 30:
                self.timer = 0
                self.verificar_paredes(plataformas)
                self.controles(lista_eventos, teclas_presionadas)
                self.verificar_plataforma(plataformas)
                self.aplicar_gravedad()
                self.actualizar_posicion()
                self.animaciones()
                self.updatear_frames()
                self.proyectiles.actualizar_disparos(objetivos, plataformas)
                self.verificar_colision_enemigos(objetivos)
                self.cooldown_invulnerabilidad(delta_ms)
                self.cooldown_disparo(delta_ms)
                self.verificar_limite_y()
                self.draw()
        else:
            self.lose = True

        


