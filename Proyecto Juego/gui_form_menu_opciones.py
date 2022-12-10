import pygame
from pygame.locals import *
from aux_constantes import *
from gui_form import Form
from gui_form_menu_score import FormScore
from gui_button import Button
from gui_form_menu_sonido import FormSonido
from gui_form_menu_controles import FormControles


class FormMenuOpciones(Form):
    '''
    Formulario que representa el menu de opciones del juego
    '''
    def __init__(self, name, master_surface, x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background = None, color_border= None,active=False):
        '''
        Inicializacion del formulario del menu opciones; conformado por cuatro botones, cada uno con una funcion distinta.
        '''
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)
        
        self.puntos = Button(master=self, x = 610, y = 200, w = 280, h = 75, on_click=self.score, text="SCORE", font_size= 75)
        self.sonido = Button(master=self, x = 610, y = 310, w = 280, h = 75, on_click=self.sound, text="SONIDO", font_size= 75)
        self.controles = Button(master=self, x = 565, y = 420, w = 370, h = 75, on_click=self.controls, text="CONTROLES", font_size= 75)
        self.back = Button(master=self,x=20, y=670, w=120,h =50,on_click=self.retroceder, text="atras", font_size= 50)
        self.lista_widget = [self.puntos, self.sonido, self.controles, self.back]


    
    def score(self, parametro):
        '''
        Crea el formulario 'score' y lo activa, el formulario 'opciones' sigue existiendo dentro de forms_dict
        '''
        FormScore(name="score", master_surface=self.master_surface, imagen_background= PATH_RECURSOS + r"\background\Pradera2.png")
        self.on_click_boton("score")


    def sound(self, parametro):
        '''
        Crea el formulario 'sound' y lo activa, el formulario 'opciones' sigue existiendo dentro de forms_dict
        '''
        FormSonido(name="sound", master_surface = self.master_surface, imagen_background =PATH_RECURSOS + r"\background\Pradera3.png")
        self.on_click_boton("sound")


    def controls(self, parametro):
        '''
        Crea el formulario 'controls' y lo activa, el formulario 'opciones' sigue existiendo dentro de forms_dict
        '''
        FormControles(name="controls", master_surface= self.master_surface, imagen_background= PATH_RECURSOS + r"\background\Pradera4.png")
        self.on_click_boton("controls")


    def retroceder(self, parametro):
        '''
        Elimina al formulario 'options' de forms_dict y pone en activo al formulario 'main'
        '''
        self.forms_dict.pop("options")
        self.on_click_boton("main")
