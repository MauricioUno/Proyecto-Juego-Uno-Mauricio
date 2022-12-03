from aux_constantes import *
from gui_form import *
from gui_button import *
from gui_widget import Widget
from Practica_SQL import obtener_filas


class FormScore(Form):
    def __init__(self, name, master_surface, x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background = None, color_border= None,active=False):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)

        self.jugador = Widget(master=self, x = 280, y = 50, w = 260, h = 90, text="Jugador", font_size= 75, font_color=COLOR_TEXTO_MENU)
        self.score = Widget(master=self, x = 605, y = 50, w = 260, h = 90, text="Puntos", font_size= 75, font_color=COLOR_TEXTO_MENU)
        self.tiempo = Widget(master=self, x = 930, y = 50, w = 260, h = 90, text="Tiempo", font_size= 75, font_color=COLOR_TEXTO_MENU)
        self.retroceder = Button(master=self,x=20, y=670, w=120,h =50,on_click=self.salir, on_click_param="options",text="atras", font_size= 50, font_color=COLOR_TEXTO_MENU)
        self.lista_widget = [self.score, self.jugador, self.tiempo, self.retroceder]
        self.crear_tabla()


    def crear_tabla(self):
        lista = obtener_filas()
        pos_y = 200
        nro = 1
        for tupla in lista:
            pos_x = 310
            for dato in tupla:
                data = Widget(master=self, x = pos_x, y = pos_y, w=200, h= 60, text= "{0}".format(dato), font_size=30, font_color=C_BLACK, image_background= PATH_RECURSOS + r"\gui\gui_score_{0}.png".format(nro))
                self.lista_widget.append(data)
                pos_x += 325
            pos_y += 100
            nro += 1

    
    def salir(self, parametro):
        self.forms_dict.pop("score")
        self.on_click_boton(parametro)