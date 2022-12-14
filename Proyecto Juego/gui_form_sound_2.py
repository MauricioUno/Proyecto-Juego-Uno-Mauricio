import pygame
from pygame.locals import *
from aux_constantes import *
from gui_form import Form
from gui_widget_button import Button
from gui_widget import Widget
from gui_widget_bar import ElementBar


class FormPausaSonido(Form):
    '''
    Version miniatura de FormSonido, leer su documentacion, la unica diferencia es la funcion retroceder,
    que activara el formulario 'pause' en lugar de 'main'
    '''
    def __init__(self, name, master_surface, x,y,w=300,h=350,color_background= None, imagen_background = None, color_border= None,active=False):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)
        self.surface.set_colorkey(C_BLACK)
        self.sonido = Widget(master = self, x = 100, y = 20, w = 120, h = 40, color_background=None, color_border= None, image_background= None, text="Musica",font_size=35, font_color=COLOR_TEXTO_MENU)
        self.plus_sound = Button(master=self,x=255,y=80,w=25,h=25,image_background=PATH_RECURSOS + r"\gui\suma.png",on_click=self.change_sound,on_click_param=1)
        self.minus_sound = Button(master=self,x=20,y=80,w=25,h=25,image_background=PATH_RECURSOS + r"\gui\resta.png",on_click=self.change_sound,on_click_param=-1)
        self.sound_bar = ElementBar(master=self,x=50,y=70,w=200,h=45,color_background=None,color_border=None, value=(pygame.mixer.music.get_volume()*20) ,value_max = 10, image_background=PATH_RECURSOS + r"\gui\gray_bar.png",element= PATH_RECURSOS + r"\gui\green2.png")
        
        self.efecto = Widget(master = self, x = 100, y = 150, w = 120, h = 40, color_background=None, color_border= None, image_background= None, text="Efectos",font_size=35, font_color=COLOR_TEXTO_MENU)
        self.plus_efect = Button(master=self,x=255,y=210,w=25,h=25,image_background=PATH_RECURSOS + r"\gui\suma.png",on_click=self.change_efecto,on_click_param=1)
        self.minus_efect = Button(master=self,x=20,y=210,w=25,h=25,image_background=PATH_RECURSOS + r"\gui\resta.png",on_click=self.change_efecto,on_click_param=-1)
        self.effect_bar = ElementBar(master=self,x=50,y=200,w=200,h=45,color_background=None,color_border=None, value=(self.sounds_dict["click"].get_volume()*40), value_max = 10, image_background= PATH_RECURSOS + r"\gui\gray_bar.png",element= PATH_RECURSOS + r"\gui\green2.png")

        self.back = Button(master=self,x=90, y=280, w=120,h =50,image_background=None, on_click=self.retroceder, on_click_param="pause",text="atras", font_size= 50, font_color=COLOR_TEXTO_MENU) 
        self.lista_widget = [self.back, self.sonido, self.plus_sound, self.minus_sound, self.sound_bar, self.efecto, self.plus_efect, self.minus_efect, self.effect_bar]


    def change_sound(self, incremento):
        self.sound_bar.value += incremento
        pygame.mixer.music.set_volume(self.sound_bar.value/20)
        self.play_efecto_sonido("click")

    def change_efecto(self, incremento):
        self.effect_bar.value += incremento
        self.ajustar_volumen_efectos_de_sonido(self.effect_bar.value/40)
        self.play_efecto_sonido("click")

    def retroceder(self, parametro):
        self.forms_dict.pop("sound")
        self.on_click_boton("pause")