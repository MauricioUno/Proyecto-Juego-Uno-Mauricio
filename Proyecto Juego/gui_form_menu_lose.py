import pygame
from pygame.locals import *
from aux_constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
from gui_progressbar import ElementBar


class FormLose(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_background = None, imagen_background = None, color_border = None, active = False):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)
        self.surface.set_colorkey(C_BLACK)
        self.nivel = name
        self.lose = Widget(master=self, x = w/2 -150, y = 5, w = 300, h = 70, text= "Perdiste!", font_size=70, font_color=COLOR_TEXTO_MENU)
        self.home = Button(master=self, x= 100,y = h-80, w = 50, h= 50, image_background= PATH_RECURSOS + r"\gui\menu.png", on_click= self.on_click_boton_r, on_click_param= "main")
        self.replay = Button(master=self, x= 250,y = h-80, w = 50, h= 50, image_background= PATH_RECURSOS + r"\gui\restart.png", on_click= self.on_click_boton_r, on_click_param= self.nivel)
        self.lista_widget = [self.lose, self.home, self.replay]



    def on_click_boton_r(self, parametro):
        self.forms_dict[self.nivel].resetear()
        self.set_active(parametro)
        
        
    def cambiar_nivel(self, parametro):
        self.nivel = parametro
        self.replay.on_click_param = parametro