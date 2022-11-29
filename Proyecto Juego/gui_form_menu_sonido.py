import pygame
from pygame.locals import *
from aux_constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
from gui_progressbar import ElementBar


class FormSonido(Form):
    def __init__(self, name, master_surface, x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background = None, color_border= None,active=False):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)

        self.sonido = Widget(master = self, x = 500, y = 30, w = 500, h = 150, color_background=None, color_border= None, image_background= None, text="Musica",font_size=100, font_color=COLOR_TEXTO_MENU)
        self.plus_sound = Button(master=self,x=1010,y=200,w=50,h=50,image_background=PATH_RECURSOS + r"\gui\suma.png",on_click=self.change_sound,on_click_param=1)
        self.minus_sound = Button(master=self,x=440,y=200,w=50,h=50,image_background=PATH_RECURSOS + r"\gui\resta.png",on_click=self.change_sound,on_click_param=-1)
        self.sound_bar = ElementBar(master=self,x=500,y=190,w=500,h=70,color_background=None,color_border=None, value_max = 10, image_background=PATH_RECURSOS + r"\gui\gray_bar.png",element= PATH_RECURSOS + r"\gui\green.png")
        
        self.efecto = Widget(master = self, x = 500, y = 330, w = 500, h = 150, color_background=None, color_border= None, image_background= None, text="Efectos",font_size=100, font_color=COLOR_TEXTO_MENU)
        self.plus_efect = Button(master=self,x=1010,y=500,w=50,h=50,image_background=PATH_RECURSOS + r"\gui\suma.png",on_click=self.change_efecto,on_click_param=1)
        self.minus_efect = Button(master=self,x=440,y=500,w=50,h=50,image_background=PATH_RECURSOS + r"\gui\resta.png",on_click=self.change_efecto,on_click_param=-1)
        self.effect_bar = ElementBar(master=self,x=500,y=490,w=500,h=70,color_background=None,color_border=None, value_max = 10, image_background= PATH_RECURSOS + r"\gui\gray_bar.png",element= PATH_RECURSOS + r"\gui\green.png")

        self.back = Button(master=self,x=20, y=670, w=120,h =50,image_background=None, on_click=self.on_click_boton, on_click_param="options",text="atras", font_size= 50, font_color=COLOR_TEXTO_MENU) 
        self.lista_widget = [self.sonido, self.efecto, self.plus_sound, self.minus_sound, self.back, self.sound_bar, self.plus_efect, self.minus_efect, self.effect_bar]



    def change_sound(self, incremento):
        self.sound_bar.value += incremento

    def change_efecto(self, incremento):
        self.effect_bar.value += incremento