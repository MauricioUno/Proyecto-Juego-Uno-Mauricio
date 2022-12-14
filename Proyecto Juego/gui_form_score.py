from aux_constantes import *
from gui_form import *
from gui_widget_button import *
from gui_widget import Widget
from manager_data import *

class FormScore(Form):
    '''
    Formulario que representa el top 5 mejores puntajes del juego
    '''
    def __init__(self, name, master_surface, x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background = None, color_border= None,active=False):
        '''
        Inicializacion del formulario del menu scores; conformado por una 'tabla' y un boton
        '''
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)

        self.jugador = Widget(master=self, x = 280, y = 50, w = 260, h = 90, text="Jugador", font_size= 75)
        self.score = Widget(master=self, x = 605, y = 50, w = 260, h = 90, text="Puntos", font_size= 75)
        self.tiempo = Widget(master=self, x = 930, y = 50, w = 260, h = 90, text="Tiempo", font_size= 75)
        self.back = Button(master=self,x=20, y=670, w=120,h =50,on_click=self.retroceder, text="atras", font_size= 50)
        self.lista_widget = [self.score, self.jugador, self.tiempo, self.back]
        self.crear_tabla(recibir_scores())


    def crear_tabla(self, lista_tuplas):
        '''
        Recibe como parametro una lista de tuplas, se creara una fila de widgets
        por cada tupla, la cantidad de widgets en la fila depende de la cantidad
        de elementos de la tupla, cada fila y columna esta separada por parametros
        hardcodeados
        '''
        pos_y = 200
        nro = 1
        for tupla in lista_tuplas:
            pos_x = 310
            for dato in tupla:
                data = Widget(master=self, x = pos_x, y = pos_y, w=200, h= 60, text= "{0}".format(dato), font_size=30, font_color=C_BLACK, image_background= PATH_RECURSOS + r"\gui\gui_score_{0}.png".format(nro))
                self.lista_widget.append(data)
                pos_x += 325
            pos_y += 100
            nro += 1

    
    def retroceder(self, parametro):
        '''
        Elimina al formulario 'score' de forms_dict y pone en activo al formulario 'options'
        '''
        self.forms_dict.pop("score")
        self.on_click_boton("options")