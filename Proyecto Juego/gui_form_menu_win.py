import pygame
from pygame.locals import *
from aux_constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
from gui_form_nivel import FormNivel
from Practica_SQL import *
from Data_lvl_SQL import *


class FormWin(Form):
    def __init__(self, save_file, nro_lvl, name, master_surface, x, y, w, h, color_background = None, imagen_background = None, color_border = None, active = False):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)    
        self.surface.set_colorkey(C_BLACK)
        self.save_file = save_file
        self.nro_lvl = nro_lvl
        self.clave_lvl = "level_{0}".format(nro_lvl)
        self.win = Widget(master=self, x = w/2 -150, y = 5, w = 300, h = 70, text= "Ganaste!", font_size=70, font_color=COLOR_TEXTO_MENU)
        self.home = Button(master=self, x= w/2 - 33 ,y = 370, w = 50, h= 50, image_background= PATH_RECURSOS + r"\gui\menu.png", on_click= self.volver_a_main)
        self.reset = Button(master=self, x= w/2 - 190 ,y = 370, w = 50, h= 50, image_background= PATH_RECURSOS + r"\gui\restart.png", on_click= self.replay, on_click_param= self.clave_lvl)
        self.next = Button(master=self, x= w/2 + 133 ,y = 370, w = 50, h= 50, image_background= PATH_RECURSOS + r"\gui\next.png", on_click= self.next_lvl, on_click_param= None)
        self.clock = Widget (master=self, x= w/4 -100, y = h/4-20, w=40, h=40, image_background=PATH_RECURSOS + r"\gui\win_time.png")
        self.heart = Widget (master=self, x= w/4 -100, y = h/4+30, w=40, h=40, image_background=PATH_RECURSOS + r"\gui\win_heart.png")
        self.score = Widget (master=self, x= w/4 -100, y = h/4+80, w=40, h=40, image_background=PATH_RECURSOS + r"\gui\win_star.png")
        
        self.text_total = Widget (master=self, x= w/4 -100, y = h/4+130, w = self.w, h = 70, text= "Score Total: ", font_size=60, font_color=COLOR_TEXTO_MENU, center=False)
        self.text_clock = Widget(master=self, x = w/4 - 40, y = self.clock.y, w = self.w, h = 50, text= " ", font_size=40, font_color=COLOR_TEXTO_MENU, center=False)
        self.text_heart = Widget(master=self, x = w/4 - 40, y = self.heart.y, w = self.w, h = 50, text= " ", font_size=40, font_color=COLOR_TEXTO_MENU, center=False)
        self.text_score = Widget(master=self, x = w/4 - 40, y = self.score.y, w = self.w, h = 50, text= " ", font_size=40, font_color=COLOR_TEXTO_MENU, center=False)
        self.lista_widget = [self.win, self.home, self.reset, self.next, self.clock, self.heart, self.score, self.text_clock, self.text_heart, self.text_score, self.text_total]
        self.score_total = 0


    def next_lvl(self, nada):
        if self.nro_lvl < ULTIMO_NIVEL:
            self.eliminar_formularios([self.clave_lvl, "pause", "win", "lose"])
            self.forms_dict["levels"].start_level(self.nro_lvl + 1)


    def replay(self, nada):
        self.forms_dict.pop(self.clave_lvl)
        FormNivel(save_file = self.save_file, nivel = self.nro_lvl, master_surface = self.master_surface)
        self.on_click_boton(self.clave_lvl)


    def volver_a_main(self, parametro):
        self.eliminar_formularios([self.clave_lvl, "levels", "pause", "win", "lose"])
        self.activar_musica("music_main")
        self.on_click_boton("main")
        

    def puntaje_obtenido(self, vida = 0, scoreVida = 0, tiempo = 0, scoreTiempo = 0, scorePlayer = 0, municion = 0, reloj = 0):
        self.text_clock.text = "{0} x {1} = {2}".format(tiempo, scoreTiempo, tiempo*scoreTiempo)
        self.text_heart.text = "{0} x {1} = {2}".format(vida, scoreVida, vida*scoreVida)
        self.text_score.text = "{0} x {1} = {2}".format(scorePlayer, 1, scorePlayer*1)
        
        self.score_total = scorePlayer + tiempo*scoreTiempo + vida*scoreVida
        self.text_total.text = "Score Total: {0}".format(self.score_total)

        if self.nro_lvl < ULTIMO_NIVEL:
            actualizar_datos_nivel(self.save_file, self.nro_lvl + 1, vida, municion, self.score_total, reloj + 60 - tiempo, True)
        else:
            nombre = obtener_nombre(self.save_file)
            crear_data_base_ranking()
            insertar_fila(nombre, self.score_total, reloj + 60 - tiempo)