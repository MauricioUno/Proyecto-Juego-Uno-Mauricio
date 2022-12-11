from aux_constantes import *
from gui_form import Form
from gui_widget_button import Button
from gui_widget import Widget



class FormControles(Form):
    '''
    Formulario que representa el menu de controles del juego
    '''
    def __init__(self, name, master_surface, x = 0, y = 0, w = ANCHO_VENTANA, h = ALTO_VENTANA, color_background = None, imagen_background = None, color_border= None, active = False):
        '''
        Inicializacion del formulario del menu de controles; dos botones para cambiar la imagen y el texto y un boton para retroceder.
        '''
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)
        self.valor = 0
        self.textos = ["[ A ] : ganar (sobre el portal)", "[ Z ] : disparar", "[ SPACE ] : saltar", "[LEFT & RIGHT] : moverse"]
        self.back = Button(master=self,x=20, y=670, w=120,h =50,on_click=self.retroceder, text="atras", font_size= 50)
        self.prev = Button(master=self, x= 300 ,y = 200, w = 75, h= 75, image_background= PATH_RECURSOS + r"\gui\prew.png",on_click=self.siguiente_pagina, on_click_param=-1)
        self.next = Button(master=self, x= 1125 ,y = 200, w = 75, h= 75, image_background= PATH_RECURSOS + r"\gui\next.png",on_click=self.siguiente_pagina, on_click_param=1)
        self.image = Widget (master=self, x = 375, y = 20, w = 750, h =450, image_background= None)
        self.text = Widget (master=self, x= 450, y = 500, w=600, h=150, image_background=PATH_RECURSOS + r"\gui\Table.png", text= "None", font_size= 40)
        self.lista_widget = [self.image, self.text, self.back, self.next, self.prev]
        self.actualizar_imagen_texto()


    def siguiente_pagina(self, modificacion):
        self.play_efecto_sonido("click")
        self.actualizar_imagen_texto(modificacion)
        
        
    def actualizar_imagen_texto(self, modificacion = 0):
        '''
        Se cambia el valor indice; que influye en los elementos que aparecen en pantalla, si se excede de los
        limites, se le asignara el otro extremo
        '''
        self.valor += modificacion
        if self.valor > 3:
            self.valor = 0
        elif self.valor < 0:
            self.valor = 3

        self.image.asignar_imagen_background(PATH_RECURSOS + r"\background\tutorial{0}.png".format(self.valor))
        try:
            self.text.text = self.textos[self.valor]
        except:
            self.text.text = "ERROR! NO DATA!"


    def retroceder(self, parametro):
        '''
        Elimina al formulario 'controls' de forms_dict y pone en activo al formulario 'options'
        '''
        self.forms_dict.pop("controls")
        self.on_click_boton("options")