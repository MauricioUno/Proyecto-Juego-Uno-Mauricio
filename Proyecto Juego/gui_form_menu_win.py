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
        self.nro_lvl = None
        self.clave_lvl = None
        self.win = Widget(master=self, x = w/2 -150, y = 5, w = 300, h = 70, text= "Ganaste!", font_size=70, font_color=COLOR_TEXTO_MENU)
        self.home = Button(master=self, x= w/2 - 33 ,y = 370, w = 50, h= 50, image_background= PATH_RECURSOS + r"\gui\menu.png", on_click= self.on_click_boton_reset, on_click_param= "main")
        self.replay = Button(master=self, x= w/2 - 190 ,y = 370, w = 50, h= 50, image_background= PATH_RECURSOS + r"\gui\restart.png", on_click= self.on_click_boton_reset, on_click_param= None)
        self.next = Button(master=self, x= w/2 + 133 ,y = 370, w = 50, h= 50, image_background= PATH_RECURSOS + r"\gui\next.png", on_click= self.on_click_boton_next_lvl, on_click_param= None)
        self.clock = Widget (master=self, x= w/4 -100, y = h/4-20, w=40, h=40, image_background=PATH_RECURSOS + r"\gui\win_time.png")
        self.heart = Widget (master=self, x= w/4 -100, y = h/4+30, w=40, h=40, image_background=PATH_RECURSOS + r"\gui\win_heart.png")
        self.score = Widget (master=self, x= w/4 -100, y = h/4+80, w=40, h=40, image_background=PATH_RECURSOS + r"\gui\win_star.png")
        
        self.text_total = Widget (master=self, x= w/4 -100, y = h/4+130, w = self.w, h = 70, text= "Score Total: ", font_size=60, font_color=COLOR_TEXTO_MENU, center=False)
        self.text_clock = Widget(master=self, x = w/4 - 40, y = self.clock.y, w = self.w, h = 50, text= " ", font_size=40, font_color=COLOR_TEXTO_MENU, center=False)
        self.text_heart = Widget(master=self, x = w/4 - 40, y = self.heart.y, w = self.w, h = 50, text= " ", font_size=40, font_color=COLOR_TEXTO_MENU, center=False)
        self.text_score = Widget(master=self, x = w/4 - 40, y = self.score.y, w = self.w, h = 50, text= " ", font_size=40, font_color=COLOR_TEXTO_MENU, center=False)
        self.lista_widget = [self.win, self.home, self.replay, self.next, self.clock, self.heart, self.score, self.text_clock, self.text_heart, self.text_score, self.text_total]
        self.score_total = 0


    def on_click_boton_next_lvl(self, aux):
        next_lvl = self.nro_lvl + 1
        if next_lvl < 4:
            self.forms_dict[self.clave_lvl].resetear()
            self.forms_dict["pause"].cambiar_nivel(next_lvl)
            self.forms_dict["win"].cambiar_nivel(next_lvl)
            self.forms_dict["lose"].cambiar_nivel(next_lvl)
            self.set_active(self.clave_lvl)


    def on_click_boton_reset(self, parametro):
        self.forms_dict[self.clave_lvl].resetear()
        self.set_active(parametro)
        

    def cambiar_nivel(self, nro_lvl):
        self.clave_lvl = "level_{0}".format(nro_lvl)
        self.nro_lvl = nro_lvl
        self.replay.on_click_param = self.clave_lvl


    def puntaje_obtenido(self, vida = 0, scoreVida = 0, tiempo = 0, scoreTiempo = 0, scorePlayer = 0):
        self.text_clock.text = "{0} x {1} = {2}".format(tiempo, scoreTiempo, tiempo*scoreTiempo)
        self.text_heart.text = "{0} x {1} = {2}".format(vida, scoreVida, vida*scoreVida)
        self.text_score.text = "{0} x {1} = {2}".format(scorePlayer, 1, scorePlayer*1)
        
        self.score_total = scorePlayer + tiempo*scoreTiempo + vida*scoreVida
        self.text_total.text = "Score Total: {0}".format(self.score_total)