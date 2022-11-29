import pygame
from pygame.locals import *
from aux_constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget


class FormMenuNiveles(Form):
    def __init__(self,name,master_surface,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background = None, color_border= None,active=False):
        super().__init__(name,master_surface,x,y,w,h,color_background, imagen_background, color_border,active)

        #self.nivel = Widget(master_form=self, x=1135 -250, y=20, w=500, h=120, text="Bosque", font_size= 100, font_color= COLOR_TEXTO_MENU)
        self.boton1 = Button(master=self,x=20,y=20,w=750,h=180,image_background=PATH_RECURSOS + r"\background\Forest0.png",on_click=self.start_level,on_click_param="level_1", color_border= C_GREEN_2)
        self.boton2 = Button(master=self,x=20,y=220,w=750,h=180,image_background=PATH_RECURSOS + r"\background\Snow0.png",on_click=self.start_level,on_click_param="level_2", color_border=C_BLUE_3)
        self.boton3 = Button(master=self,x=20,y=420,w=750,h=180,image_background=PATH_RECURSOS + r"\background\Cave0.png",on_click=print,on_click_param="level_3", color_border=C_BROWN)
        self.boton4 = Button(master=self,x=20, y=670, w=120,h =50,image_background=None, on_click=self.on_click_boton, on_click_param="main",text="atras", font_size= 50, font_color=COLOR_TEXTO_MENU) 
        
        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4]



    def start_level(self, parametro):
        super().on_click_boton(parametro)
        self.forms_dict["pause"].cambiar_nivel(parametro)
        self.forms_dict["win"].cambiar_nivel(parametro)
        self.forms_dict["lose"].cambiar_nivel(parametro)