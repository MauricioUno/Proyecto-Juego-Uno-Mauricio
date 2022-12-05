import pygame
import sys
from pygame.locals import *
from gui_form import Form
from gui_button import Button
from aux_constantes import *
from gui_widget import Widget
from gui_form_menu_opciones import FormMenuOpciones
from Data_lvl_SQL import crear_data_base_niveles
from gui_form_menu_saves import FormSaves

class FormMenuMain(Form):
    def __init__(self,name,master_surface,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background = None, color_border= None,active=True):
        super().__init__(name,master_surface,x,y,w,h,color_background, imagen_background, color_border,active)

        self.title = Widget(master=self, x = 500, y = 50, w = 500, h = 150, text="GLITCH",font_size=150, font_color=COLOR_TEXTO_MENU)
        self.boton3 = Button(master=self, x = 610, y = 300, w = 280, h = 100, on_click=self.start, text="START", font_size= 100, font_color=COLOR_TEXTO_MENU)
        self.boton4 = Button(master=self, x = 505, y = 410, w = 470, h = 100, on_click=self.options, text="OPCIONES", font_size= 100, font_color=COLOR_TEXTO_MENU)
        self.boton5 = Button(master=self, x = 610, y = 520, w = 280, h = 100, on_click=self.salir,text="SALIR", font_size= 100, font_color=COLOR_TEXTO_MENU)
        self.lista_widget = [self.boton3, self.boton4, self.boton5, self.title]
        self.activar_musica("music_main")


    def start(self, parametro):
        FormSaves(name="saves", master_surface= self.master_surface, imagen_background= PATH_RECURSOS + r"\background\forest4.png")
        self.on_click_boton("saves")

    def options(self, parametro):
        FormMenuOpciones(name="options",master_surface = self.master_surface, imagen_background =PATH_RECURSOS + r"\background\Pradera2.png")
        self.on_click_boton("options")
        
    def salir(self, parametro):
        pygame.quit()
        sys.exit() 