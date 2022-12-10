import pygame
from pygame.locals import *
from aux_constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
from gui_progressbar import ElementBar


class FormSonido(Form):
    '''
    Formulario que representa el menu de sonido del juego
    '''
    def __init__(self, name, master_surface, x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background = None, color_border= None,active=False):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)
        '''
        Inicializacion del formulario del menu de sonido; conformado dos barras que representan el volumen de musica
        y de efectos, junto con sus botones para variar el volumen y por ultimo, un boton para retroceder.
        '''
        self.sonido = Widget(master = self, x = 500, y = 30, w = 500, h = 150, text="Musica",font_size=100)
        self.plus_sound = Button(master=self,x=1010,y=200,w=50,h=50,image_background=PATH_RECURSOS + r"\gui\suma.png",on_click=self.change_music,on_click_param=1)
        self.minus_sound = Button(master=self,x=440,y=200,w=50,h=50,image_background=PATH_RECURSOS + r"\gui\resta.png",on_click=self.change_music,on_click_param=-1)
        self.sound_bar = ElementBar(master=self,x=500,y=190,w=500,h=70, value=(pygame.mixer.music.get_volume()*20) ,value_max = 10, image_background=PATH_RECURSOS + r"\gui\gray_bar.png",element= PATH_RECURSOS + r"\gui\green.png")
        
        self.efecto = Widget(master = self, x = 500, y = 330, w = 500, h = 150, text="Efectos",font_size=100)
        self.plus_efect = Button(master=self,x=1010,y=500,w=50,h=50,image_background=PATH_RECURSOS + r"\gui\suma.png",on_click=self.change_sound,on_click_param=1)
        self.minus_efect = Button(master=self,x=440,y=500,w=50,h=50,image_background=PATH_RECURSOS + r"\gui\resta.png",on_click=self.change_sound,on_click_param=-1)
        self.effect_bar = ElementBar(master=self,x=500,y=490,w=500,h=70, value=(self.sounds_dict["click"].get_volume()*40), value_max = 10, image_background= PATH_RECURSOS + r"\gui\gray_bar.png",element= PATH_RECURSOS + r"\gui\green.png")

        self.back = Button(master=self,x=20, y=670, w=120,h =50,on_click=self.retroceder, text="atras", font_size= 50) 
        self.lista_widget = [self.sonido, self.efecto, self.plus_sound, self.minus_sound, self.back, self.sound_bar, self.plus_efect, self.minus_efect, self.effect_bar]


    def change_music(self, incremento):
        '''
        Cambia el valor de la barra de musica y setea el volumen de la musica pygame.mixer
        Se divide por 20 para que el valor maximo sea 0.5
        '''
        self.sound_bar.value += incremento
        pygame.mixer.music.set_volume(self.sound_bar.value/20)
        self.play_efecto_sonido("click")

    def change_sound(self, incremento):
        '''
        Cambia el valor de la barra de efectos y setea el volumen de los sonidos
        Se divide por 40 para que el valor maximo sea 0.25
        '''
        self.effect_bar.value += incremento
        self.ajustar_volumen_efectos_de_sonido(self.effect_bar.value/40)
        self.play_efecto_sonido("click")

    def retroceder(self, parametro):
        '''
        Elimina al formulario 'sound' de forms_dict y pone en activo al formulario 'options'
        '''
        self.forms_dict.pop("sound")
        self.on_click_boton("options")