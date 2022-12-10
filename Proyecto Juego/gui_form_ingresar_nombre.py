from aux_constantes import *
from gui_form import *
from gui_button import *
from gui_textbox import TextBox
from gui_widget import Widget
from gui_button import Button
from manager_data import crear_partida
import re

class FormName(Form):
    '''
    Formulario que representa el menu de ingresar nombre
    '''
    def __init__(self, save_file, name, master_surface, x, y, w, h, color_background = None, imagen_background = None, color_border = None, active = False):
        '''
        Se llamara a este formulario para empezar una partida nueva, su inicializacion consta de dos botones con distintas
        funciones y una caja de texto, donde el usuario podra ingresar su nombre
        '''
        self.save_file = save_file
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)
        self.surface.set_colorkey(C_BLACK)
        self.title = Widget(master=self, x= self.w/8, y = 20, w = 3*self.w/4, h = 50, font_size= 35, font_color= COLOR_TEXTO_MENU, text="Ingresar nombre")
        self.input = TextBox(master=self, x = self.w/8, y = self.h/2 + 50 - 100, w = 3*self.w/4, h = 80, image_background= PATH_RECURSOS + r"\gui\table.png", font_size= 35, font_color= COLOR_TEXTO_MENU)
        self.back = Button(master=self, x= 100,y = h-80, w = 50, h= 50, image_background= PATH_RECURSOS + r"\gui\close.png", on_click=self.retroceder, on_click_param= "saves")
        self.save = Button(master=self, x= 250,y = h-80, w = 50, h= 50, image_background= PATH_RECURSOS + r"\gui\ok.png", on_click=self.guardar_nombre, on_click_param="levels")
        self.lista_widget = [self.title, self.input, self.back, self.save]


    def retroceder(self, parametro):
        '''
        Elimina el formulario 'name' de forms_dict y activa el formularios 'saves'
        '''
        self.forms_dict.pop("name")
        self.on_click_boton("saves")


    def guardar_nombre(self, parametro):
        '''
        Guarda el nombre del jugador y crea una nueva partida con este y el save_file que corresponda.
        Elimina el formulario 'name' de forms_dict y empieza la partida
        '''
        if re.search("^ | $", self.input.text):
            self.input.text = self.input.text.strip()

        if re.search("^$",self.input.text):
            self.input.text = "Anonimo"

        crear_partida(self.save_file, self.input.text, ULTIMO_NIVEL)
        self.forms_dict.pop("name")
        self.forms_dict["saves"].iniciar_save_file(self.save_file)