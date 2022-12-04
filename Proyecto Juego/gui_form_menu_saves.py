from gui_form import Form
from gui_button import Button
from aux_constantes import *
from gui_widget import Widget
from Data_lvl_SQL import * 
from gui_form_menu_nivel import FormMenuNiveles


class FormSaves(Form):
    def __init__(self, name, master_surface, x=0, y=0, w=ANCHO_VENTANA, h=ALTO_VENTANA, color_background=None, imagen_background=None, color_border=None, active=False):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)

        self.boton1 = Button(master=self,x=375,y=20,w=750,h=180,on_click=self.cargar_datos,on_click_param="Save_1", text= "Partida A", image_background= PATH_RECURSOS + r"\gui\TablaH.png", font_size= 70, font_color= COLOR_TEXTO_MENU)
        self.boton2 = Button(master=self,x=375,y=220,w=750,h=180,on_click=self.cargar_datos,on_click_param="Save_2", text= "Partida B", image_background= PATH_RECURSOS + r"\gui\TablaH.png", font_size= 70, font_color= COLOR_TEXTO_MENU)
        self.boton3 = Button(master=self,x=375,y=420,w=750,h=180,on_click=self.cargar_datos,on_click_param="Save_3", text= "Partida C", image_background= PATH_RECURSOS + r"\gui\TablaH.png", font_size= 70, font_color= COLOR_TEXTO_MENU)
        self.back = Button(master=self,x=20, y=670, w=120,h =50,image_background=None, on_click=self.retroceder, on_click_param="main",text="atras", font_size= 50, font_color=COLOR_TEXTO_MENU) 
        self.lista_widget = [self.boton1, self.boton2, self.boton3, self.back]



    def cargar_datos(self, archivo):
        crear_data_base_niveles(archivo)
        FormMenuNiveles(save_file=archivo, name="levels",master_surface = self.master_surface, imagen_background =PATH_RECURSOS + r"\background\Pradera1.png")
        self.on_click_boton("levels")

    
    def retroceder(self, parametro):
        self.forms_dict.pop("saves")
        self.on_click_boton("main")