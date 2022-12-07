from gui_form import Form
from gui_button import Button
from aux_constantes import *
from manager_data import obtener_name_save
from gui_form_menu_nivel import FormMenuNiveles
from gui_form_ingresar_nombre import FormName

class FormSaves(Form):
    def __init__(self, name, master_surface, x=0, y=0, w=ANCHO_VENTANA, h=ALTO_VENTANA, color_background=None, imagen_background=None, color_border=None, active=False):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)

        self.boton1 = Button(master=self,x=375,y=60,w=750,h=180,on_click=self.cargar_datos,on_click_param="Save_1", text= "Partida A", image_background= PATH_RECURSOS + r"\gui\TablaH.png", font_size= 70, font_color= COLOR_TEXTO_MENU)
        self.boton2 = Button(master=self,x=375,y=260,w=750,h=180,on_click=self.cargar_datos,on_click_param="Save_2", text= "Partida B", image_background= PATH_RECURSOS + r"\gui\TablaH.png", font_size= 70, font_color= COLOR_TEXTO_MENU)
        self.boton3 = Button(master=self,x=375,y=460,w=750,h=180,on_click=self.cargar_datos,on_click_param="Save_3", text= "Partida C", image_background= PATH_RECURSOS + r"\gui\TablaH.png", font_size= 70, font_color= COLOR_TEXTO_MENU)
        self.back = Button(master=self,x=20, y=670, w=120,h =50,image_background=None, on_click=self.retroceder, on_click_param="main",text="atras", font_size= 50, font_color=COLOR_TEXTO_MENU) 
        self.lista_widget = [self.boton1, self.boton2, self.boton3, self.back]



    def cargar_datos(self, archivo):
        if obtener_name_save(archivo) == None:
            FormName(save_file = archivo, name="name", master_surface=self.master_surface, x = 550, y = 180, w = 400, h=350, imagen_background= PATH_RECURSOS + r"\gui\TablaH.png")
            self.on_click_boton("name")
        else:
            self.iniciar_save_file(archivo)


    def iniciar_save_file(self, archivo):
        FormMenuNiveles(save_file=archivo, name="levels",master_surface = self.master_surface, imagen_background =PATH_RECURSOS + r"\background\Snow1.png")
        self.on_click_boton("levels")


    def retroceder(self, parametro):
        self.forms_dict.pop("saves")
        self.on_click_boton("main")