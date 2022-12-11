import pygame
import sys
from gui_form import Form
from gui_widget_button import Button
from aux_constantes import *
from gui_widget import Widget
from gui_form_options import FormMenuOpciones
from gui_form_saves import FormSaves

class FormMenuMain(Form):
    '''
    Formulario que representa el menu principal del juego
    '''
    def __init__(self,name,master_surface,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background = None, color_border= None,active=True):
        '''
        Inicializacion del formulario del menu principal; conformado por un titulo y por tres botones, 
        cada uno con una funcion distinta.
        '''
        super().__init__(name,master_surface,x,y,w,h,color_background, imagen_background, color_border,active)

        self.title = Widget(master=self, x = 500, y = 50, w = 500, h = 150, text="GLITCH",font_size=150)
        self.start_button = Button(master=self, x = 610, y = 300, w = 280, h = 100, on_click=self.start, text="START", font_size= 100)
        self.options_button = Button(master=self, x = 505, y = 410, w = 470, h = 100, on_click=self.options, text="OPCIONES", font_size= 100)
        self.exit_button = Button(master=self, x = 610, y = 520, w = 280, h = 100, on_click=self.salir,text="SALIR", font_size= 100)
        self.lista_widget = [self.start_button, self.options_button, self.exit_button, self.title]
        self.activar_musica("music_main")


    def start(self, parametro):
        '''
        Crea el formulario 'saves' y lo activa, el formulario 'main' sigue existiendo dentro de forms_dict
        '''
        FormSaves(name="saves", master_surface= self.master_surface, imagen_background= PATH_RECURSOS + r"\background\forest2.png")
        self.on_click_boton("saves")


    def options(self, parametro):
        '''
        Crea el formulario 'options' y lo activa, el formulario 'main' sigue existiendo dentro de forms_dict
        '''
        FormMenuOpciones(name="options",master_surface = self.master_surface, imagen_background =PATH_RECURSOS + r"\background\Pradera1.png")
        self.on_click_boton("options")
        
        
    def salir(self, parametro):
        '''
        Cierra el juego
        '''
        pygame.quit()
        sys.exit() 