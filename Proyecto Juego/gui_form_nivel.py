import pygame
from aux_constantes import *
from aux_json import *
from gui_form import Form
from gui_widget import Widget
from gui_progressbar import HealthBar


from Data_lvl_SQL import obtener_datos_nivel
from class_plataforma import ListaPlataformas
from class_trampa import ListaTrampas
from class_portal import Portal
from class_item import ListaItems
from enemy_lista import ListaEnemigos
from jugador import Jugador



class FormNivel(Form):
    def __init__(self, save_file, nivel, master_surface,x=0, y=0, w=ANCHO_VENTANA, h=ALTO_VENTANA, color_background=None, imagen_background=None, color_border=None, active=False):
        self.save_file = save_file
        self.name = "level_{0}".format(nivel)
        self.nro_nivel = nivel
        data_nivel = importar_lista(PATH_JSON.format(self.name), self.name)[0]
        imagen_background = PATH_RECURSOS + data_nivel["background"]
        self.tiempo = data_nivel["tiempo"]
        self.health_score = data_nivel["score_vida"]
        self.tiempo_score = data_nivel["score_tiempo"]
        self.cronometro = 0
        super().__init__(self.name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)
        self.plataformas = ListaPlataformas(data_nivel["plataformas"], master_surface, self.name)
        self.trampas = ListaTrampas(data_nivel["trampas"], master_surface, self.name)
        self.enemigos = ListaEnemigos(data_nivel["enemigos"], master_surface)
        self.items = ListaItems(data_nivel["items"], master_surface, self.enemigos)
        self.jugador = Jugador(data_nivel["pos_player"][0], data_nivel["pos_player"][1], master_surface, self)
        self.portal = Portal(data_nivel["pos_portal"][0], data_nivel["pos_portal"][1], master_surface, self.name)

        self.orb = Widget(master=self, x=10, y = 40, w=25, h=25,image_background=PATH_RECURSOS + r"\items\orb.png")
        self.ammo = Widget(master=self, x=50, y = 40, w=50, h=25,image_background=PATH_RECURSOS + r"\gui\ammo.png",text=" ",font_size=25,font_color=C_BLUE)
        self.score = Widget(master=self, x=1390, y = 50, w=100, h=30,image_background=PATH_RECURSOS + r"\gui\score.png", text=" ",font_size=30, font_color=C_BLACK)
        self.health_bar = HealthBar(master=self,x=10,y=10,w=350,h=20,color_background=M_BRIGHT_HOVER,color_border=C_WHITE, value =self.jugador.vida, value_max = self.jugador.vida)
        self.time = Widget(master=self, x=1390, y = 10, w=100, h=30,image_background=PATH_RECURSOS + r"\gui\time.png", text="{0}".format(self.tiempo),font_size=30, font_color=C_BLACK)
        self.lista_widget = [self.health_bar, self.orb, self.ammo, self.score, self.orb, self.ammo, self.time]

        datos = obtener_datos_nivel(self.save_file, self.nro_nivel)
        self.cargar_datos_jugador(datos[0], datos[1], datos[2], datos[3])
        


    def cargar_datos_jugador(self, vida, municion, score, tiempo):
        self.jugador.vida = vida
        self.jugador.municion = municion
        self.jugador.score = score
        self.cronometro = tiempo

    def update(self, lista_eventos, delta_ms, segundo):
        self.health_bar.value = self.jugador.vida
        self.ammo.text = "{0}".format(self.jugador.municion)
        self.score.text = "{0}".format(self.jugador.score)
        self.time.text = "{0}".format(self.tiempo)

        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

        for event in lista_eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.set_active("pause")
            
            if event.type == segundo:
                self.tiempo += -1
                

        if self.jugador.lose or self.tiempo < 0:
            self.set_active("lose")
        elif self.jugador.win:
            self.forms_dict["win"].puntaje_obtenido(self.jugador.vida, self.health_score, self.tiempo, self.tiempo_score, self.jugador.score, self.jugador.municion, self.cronometro)
            self.set_active("win")

        


    def draw(self, lista_eventos, delta_ms, teclas_presionadas):
        self.master_surface.blit(self.surface, self.slave_rect)
        self.render()
        self.plataformas.actualizar(delta_ms)
        self.trampas.actualizar(delta_ms, [self.jugador])
        self.items.actualizar(delta_ms, [self.jugador])
        self.enemigos.actualizar(self.jugador, delta_ms, self.plataformas.lista)
        self.jugador.actualizar(self.plataformas.lista, self.enemigos.lista, delta_ms, lista_eventos, teclas_presionadas)
        self.portal.actualizar([self.jugador], delta_ms)

        for aux_boton in self.lista_widget:
            aux_boton.draw()
            
            


    
        