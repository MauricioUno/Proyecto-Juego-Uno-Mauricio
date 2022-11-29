import pygame
from pygame.locals import *
from aux_constantes import *
from gui_form import Form
from gui_button import Button


class FormMenuOpciones(Form):
    def __init__(self, name, master_surface, x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background = None, color_border= None,active=False):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)
        
        self.score = Button(master=self, x = 610, y = 200, w = 280, h = 75, on_click=print, on_click_param="score",text="SCORE", font_size= 75, font_color=COLOR_TEXTO_MENU)
        self.sonido = Button(master=self, x = 610, y = 310, w = 280, h = 75, on_click=self.on_click_boton, on_click_param="sound",text="SONIDO", font_size= 75, font_color=COLOR_TEXTO_MENU)
        self.controles = Button(master=self, x = 565, y = 420, w = 370, h = 75, on_click=print, on_click_param="controls",text="CONTROLES", font_size= 75, font_color=COLOR_TEXTO_MENU)
        self.retroceder = Button(master=self,x=20, y=670, w=120,h =50,on_click=self.on_click_boton, on_click_param="main",text="atras", font_size= 50, font_color=COLOR_TEXTO_MENU)
        self.lista_widget = [self.score, self.sonido, self.controles, self.retroceder]
