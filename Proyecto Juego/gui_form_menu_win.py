import pygame
from pygame.locals import *
from aux_constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget


class FormWin(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_background = None, imagen_background = None, color_border = None, active = False):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)    
        self.surface.set_colorkey(C_BLACK)
        self.nivel = name
        self.win = Widget(master=self, x = w/2 -150, y = 5, w = 300, h = 70, text= "Ganaste!", font_size=70, font_color=COLOR_TEXTO_MENU)
        self.home = Button(master=self, x= w/2 - 33 ,y = 370, w = 50, h= 50, image_background= PATH_RECURSOS + r"\gui\menu.png", on_click= self.on_click_boton_r, on_click_param= "main")
        self.replay = Button(master=self, x= w/2 - 190 ,y = 370, w = 50, h= 50, image_background= PATH_RECURSOS + r"\gui\restart.png", on_click= self.on_click_boton_r, on_click_param= self.nivel)
        self.next = Button(master=self, x= w/2 + 133 ,y = 370, w = 50, h= 50, image_background= PATH_RECURSOS + r"\gui\next.png", on_click= print, on_click_param= "NEXT")
        self.clock = Widget (master=self, x= w/4 -100, y = h/4-20, w=40, h=40, image_background=PATH_RECURSOS + r"\gui\win_time.png")
        self.heart = Widget (master=self, x= w/4 -100, y = h/4+30, w=40, h=40, image_background=PATH_RECURSOS + r"\gui\win_heart.png")
        self.score = Widget (master=self, x= w/4 -100, y = h/4+80, w=40, h=40, image_background=PATH_RECURSOS + r"\gui\win_star.png")
        self.total = Widget (master=self, x= w/4 -100, y = h/4+100, w = self.w, h = 50, text= " ", font_size=40, font_color=COLOR_TEXTO_MENU, center=False)

        self.text_clock = Widget(master=self, x = w/4 - 40, y = self.clock.y, w = self.w, h = 50, text= " ", font_size=40, font_color=COLOR_TEXTO_MENU, center=False)
        self.text_heart = Widget(master=self, x = w/4 - 40, y = self.heart.y, w = self.w, h = 50, text= " ", font_size=40, font_color=COLOR_TEXTO_MENU, center=False)
        self.text_score = Widget(master=self, x = w/4 - 40, y = self.score.y, w = self.w, h = 50, text= " ", font_size=40, font_color=COLOR_TEXTO_MENU, center=False)
        self.lista_widget = [self.win, self.home, self.replay, self.next, self.clock, self.heart, self.score, self.text_clock, self.text_heart, self.text_score]
       
        self.score_total = 0

    def on_click_boton_r(self, parametro):
        self.valor_texto()
        self.forms_dict[self.nivel].resetear()
        self.set_active(parametro)
        
    def on_click_boton(self, parametro):
        self.valor_texto()
        super().on_click_boton(parametro)
        
    def cambiar_nivel(self, parametro):
        self.nivel = parametro
        self.replay.on_click_param = parametro


    def puntaje_obtenido(self, vida = 0, scoreVida = 0, tiempo = 0, scoreTiempo = 0, scorePlayer = 0):
        puntaje_tiempo = "{0} x {1} = {2}".format(tiempo, scoreTiempo, tiempo*scoreTiempo)
        puntaje_vida = "{0} x {1} = {2}".format(vida, scoreVida, vida*scoreVida)
        puntaje_jugador = "{0}".format(scorePlayer)
        self.valor_texto(puntaje_tiempo, puntaje_vida, puntaje_jugador)
        self.score_total = scorePlayer + tiempo*scoreTiempo + vida*scoreVida


    def valor_texto (self, tiempo = " ", vida = " ", score = " "):
        self.text_clock.text = tiempo
        self.text_heart.text = vida
        self.text_score.text = score