import pygame
from pygame.locals import *
from aux_constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
from gui_form_nivel import FormNivel


class FormLose(Form):
    def __init__(self, save_file, nro_lvl,name, master_surface, x, y, w, h, color_background = None, imagen_background = None, color_border = None, active = False):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)
        self.surface.set_colorkey(C_BLACK)
        self.save_file = save_file
        self.clave_lvl = "level_{0}".format(nro_lvl)
        self.nro_lvl = nro_lvl
        self.lose = Widget(master=self, x = w/2 -150, y = 5, w = 300, h = 70, text= "Perdiste!", font_size=70, font_color=COLOR_TEXTO_MENU)
        self.home = Button(master=self, x= 100,y = h-80, w = 50, h= 50, image_background= PATH_RECURSOS + r"\gui\menu.png", on_click= self.menu, on_click_param= "main")
        self.reset = Button(master=self, x= 250,y = h-80, w = 50, h= 50, image_background= PATH_RECURSOS + r"\gui\restart.png", on_click=self.replay, on_click_param=self.clave_lvl)
        self.lista_widget = [self.lose, self.home, self.reset]

    
    def replay(self, nada):
        self.forms_dict.pop(self.clave_lvl)
        FormNivel(save_file = self.save_file, nivel = self.nro_lvl, master_surface = self.master_surface)
        self.on_click_boton(self.clave_lvl)

    def menu(self, parametro):
        self.eliminar_formularios([self.clave_lvl, "levels", "pause", "win", "lose"])
        self.activar_musica("music_main")
        self.on_click_boton("main")