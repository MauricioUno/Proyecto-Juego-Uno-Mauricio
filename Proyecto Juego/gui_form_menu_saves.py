from gui_form import Form
from gui_button import Button
from aux_constantes import *
from manager_data import obtener_name_save
from gui_form_menu_nivel import FormMenuNiveles
from gui_form_ingresar_nombre import FormName

class FormSaves(Form):
    '''
    Formulario que representa el menu de seleccion de partidas
    '''
    def __init__(self, name, master_surface, x=0, y=0, w=ANCHO_VENTANA, h=ALTO_VENTANA, color_background=None, imagen_background=None, color_border=None, active=False):
        '''
        Inicializacion del formulario menu saves; Conformado por cuatro botones, 
        3 de ellos tienen la funcion de cargar los datos de la partida a la que hagan referencia,
        el ultimo vuelve al menu main
        '''
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)

        self.boton1 = Button(master=self,x=375,y=60,w=750,h=180,on_click=self.cargar_datos,on_click_param="Save_1", text= "Partida A", image_background= PATH_RECURSOS + r"\gui\TablaH.png", font_size= 70)
        self.boton2 = Button(master=self,x=375,y=260,w=750,h=180,on_click=self.cargar_datos,on_click_param="Save_2", text= "Partida B", image_background= PATH_RECURSOS + r"\gui\TablaH.png", font_size= 70)
        self.boton3 = Button(master=self,x=375,y=460,w=750,h=180,on_click=self.cargar_datos,on_click_param="Save_3", text= "Partida C", image_background= PATH_RECURSOS + r"\gui\TablaH.png", font_size= 70)
        self.back = Button(master=self,x=20, y=670, w=120,h =50,on_click=self.retroceder, text="atras", font_size= 50) 
        self.lista_widget = [self.boton1, self.boton2, self.boton3, self.back]



    def cargar_datos(self, save_file):
        '''
        Verifica si hay informacion sobre el save pasado como parametro en la DATABASE, en caso de existir, inicia
        la partida con los datos extraidos de la DATABASE, caso contrario, se pedira crear una nueva partida
        '''
        if obtener_name_save(save_file) == None:
            FormName(save_file = save_file, name="name", master_surface=self.master_surface, x = 550, y = 180, w = 400, h=350, imagen_background= PATH_RECURSOS + r"\gui\TablaH.png")
            self.on_click_boton("name")
        else:
            self.iniciar_save_file(save_file)


    def iniciar_save_file(self, archivo):
        '''
        Crea al formulario menu seleccion de niveles, y lo pone en activo, el formulario 'saves' sigue existiendo en forms_dict
        '''
        FormMenuNiveles(save_file=archivo, name="levels",master_surface = self.master_surface, imagen_background =PATH_RECURSOS + r"\background\Snow1.png")
        self.on_click_boton("levels")


    def retroceder(self, parametro):
        '''
        Elimina al formulario 'saves' de forms_dict y pone en activo al formulario 'main'
        '''
        self.forms_dict.pop("saves")
        self.on_click_boton("main")