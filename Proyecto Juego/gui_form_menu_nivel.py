import pygame
from pygame.locals import *
from aux_constantes import *
from gui_form import Form
from gui_button import Button
from gui_form_nivel import FormNivel
from gui_widget import Widget
from Data_lvl_SQL import obtener_estado_nivel
from gui_form_menu_pausa import FormPausa
from gui_form_menu_win import FormWin
from gui_form_menu_lose import FormLose

class FormMenuNiveles(Form):
    def __init__(self,save_file, name,master_surface,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background = None, color_border= None,active=False):
        self.save_file = save_file
        super().__init__(name,master_surface,x,y,w,h,color_background, imagen_background, color_border,active)
        self.boton1 = Button(master=self,x=20,y=20,w=750,h=180,image_background=PATH_RECURSOS + r"\background\Forest0.png",on_click=self.click_nivel,on_click_param=1)
        self.boton2 = Button(master=self,x=20,y=220,w=750,h=180,image_background=PATH_RECURSOS + r"\background\Snow3.png",on_click=self.click_nivel,on_click_param=2)
        self.boton3 = Button(master=self,x=20,y=420,w=750,h=180,image_background=PATH_RECURSOS + r"\background\Cave0.png",on_click=self.click_nivel,on_click_param=3)
        self.boton4 = Button(master=self,x=20, y=670, w=120,h =50,image_background=None, on_click=self.retroceder, on_click_param="saves",text="atras", font_size= 50, font_color=COLOR_TEXTO_MENU) 
        
        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4]
        self.data_levels(1, self.boton1)
        self.data_levels(2, self.boton2)
        self.data_levels(3, self.boton3)
   


    def data_levels(self, nivel, boton):
        if not obtener_estado_nivel(self.save_file, nivel)[0]:
            boton.active = False
            boton.image_background = pygame.image.load(PATH_RECURSOS + r"\gui\lock.png").convert_alpha()
            boton.image_background = pygame.transform.scale(boton.image_background,(boton.w, boton.h)).convert_alpha()


    def retroceder(self, parametro):
        self.forms_dict.pop("levels")
        self.on_click_boton(parametro)


    def click_nivel(self, nro_lvl):
        self.forms_dict.pop("saves")
        self.start_level(nro_lvl)


    def start_level(self, nro_lvl):
        FormNivel(save_file = self.save_file,nivel = nro_lvl, master_surface = self.master_surface)
        FormPausa(nro_lvl=nro_lvl, name="pause", master_surface=self.master_surface, x = 600, y=180, w=300, h=350, imagen_background= PATH_RECURSOS + r"\gui\TablaV.png")
        FormWin(save_file= self.save_file,nro_lvl= nro_lvl, name="win", master_surface=self.master_surface, x = 375, y = 135, w = 750, h =450, imagen_background= PATH_RECURSOS + r"\gui\TablaH.png")
        FormLose(save_file = self.save_file,nro_lvl= nro_lvl,name="lose", master_surface=self.master_surface, x = 550, y = 180, w = 400, h=350, imagen_background= PATH_RECURSOS + r"\gui\TablaH.png")
        self.on_click_boton("level_{0}".format(nro_lvl))

       
        
        