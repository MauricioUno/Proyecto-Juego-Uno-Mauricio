import pygame
from aux_constantes import *
from aux_json import *
from gui_form import Form
from gui_widget import Widget
from gui_widget_bar import HealthBar


from manager_data import obtener_data_nivel
from class_plataforma import ListaPlataformas
from class_trampa import ListaTrampas
from class_portal import Portal
from class_item import ListaItems
from enemy_lista import ListaEnemigos
from jugador import Jugador



class FormNivel(Form):
    '''
    Formulario que representa el nivel del juego 
    '''
    def __init__(self, save_file, nivel, master_surface,x=0, y=0, w=ANCHO_VENTANA, h=ALTO_VENTANA, color_background=None, imagen_background=None, color_border=None, active=False):
        '''
        Inicializacion del nivel; conformado por un contador, los widgets requeridos para representar la informacion
        que se mostrara en pantalla (vida, ammo, score, tiempo).
        Todo lo relacionado a la construccion del nivel es recibido del archivo json correspondiente
        '''
        self.name = "level_{0}".format(nivel)
        self.tiempo = 60
        data_nivel = importar_lista(PATH_JSON.format(self.name), self.name)[0]
        
        super().__init__(self.name, master_surface, x, y, w, h, color_background, PATH_RECURSOS + data_nivel["background"], color_border, active)
        self.plataformas = ListaPlataformas(data_nivel["plataformas"], self, self.name)
        self.trampas = ListaTrampas(data_nivel["trampas"], self, self.name)
        self.enemigos = ListaEnemigos(data_nivel["enemigos"], self)
        self.items = ListaItems(data_nivel["items"], self, self.enemigos)
        self.jugador = Jugador(data_nivel["pos_player"][0], data_nivel["pos_player"][1], self)
        self.portal = Portal(data_nivel["pos_portal"][0], data_nivel["pos_portal"][1], self, self.name)

        self.orb = Widget(master=self, x=10, y = 40, w=25, h=25,image_background=PATH_RECURSOS + r"\items\orb.png")
        self.ammo = Widget(master=self, x=50, y = 40, w=50, h=25,image_background=PATH_RECURSOS + r"\gui\ammo.png",text=" ",font_size=25,font_color=C_BLUE)
        self.score = Widget(master=self, x=1390, y = 50, w=100, h=30,image_background=PATH_RECURSOS + r"\gui\score.png", text=" ",font_size=30, font_color=C_BLACK)
        self.health_bar = HealthBar(master=self,x=10,y=10,w=350,h=20,color_background=M_BRIGHT_HOVER,color_border=C_WHITE, value =self.jugador.vida, value_max = self.jugador.vida)
        self.time = Widget(master=self, x=1390, y = 10, w=100, h=30,image_background=PATH_RECURSOS + r"\gui\time.png", text="{0}".format(self.tiempo),font_size=30, font_color=C_BLACK)
        self.lista_widget = [self.health_bar, self.orb, self.ammo, self.score, self.orb, self.ammo, self.time]
    
        self.cargar_datos_jugador(save_file, nivel)
        


    def cargar_datos_jugador(self, save_file, nivel):
        '''
        Carga la informacion del jugador en la partida y nivel pasados como parametro
        '''
        datos = obtener_data_nivel(save_file, nivel)
        self.jugador.vida = datos[0]
        self.jugador.municion = datos[1]
        self.jugador.score = datos[2]

    def actualizar_valor_widgets(self):
        '''
        Actualiza la informacion que muestran los widget
        '''
        self.health_bar.value = self.jugador.vida
        self.ammo.text = f"{self.jugador.municion}"
        self.score.text = f"{self.jugador.score}"
        self.time.text = f"{self.tiempo}"
 
    def update(self, lista_eventos, delta_ms, segundo):
        '''
        Actualiza los widgets del formulario
        Verifica si se aprieta la tecla ESC (pausa) y determina el tiempo de juego.
        En caso que el jugador gane o pierda, se activaran los formularios 'win' / 'lose' respectivamente
        '''
        self.actualizar_valor_widgets()

        for widget in self.lista_widget:
            widget.update(lista_eventos)

        for event in lista_eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.set_active("pause")
            
            if event.type == segundo:
                self.tiempo += -1
                

        if self.jugador.lose or self.tiempo < 0:
            self.set_active("lose")
            self.play_efecto_sonido("death")
        elif self.jugador.win:
            self.forms_dict["win"].puntaje_obtenido(self.jugador.vida, self.jugador.score, self.jugador.municion, self.tiempo)
            self.set_active("win")
            self.play_efecto_sonido("win")

        

    def draw(self, lista_eventos, delta_ms, teclas_presionadas):
        '''
        Se encarga de mostrar en pantalla a todos los elementos que conforman el formulario.
        '''
        self.master_surface.blit(self.surface, self.slave_rect)
        self.render()
        self.plataformas.actualizar(delta_ms)
        self.trampas.actualizar(delta_ms, [self.jugador])
        self.items.actualizar(delta_ms, [self.jugador])
        self.enemigos.actualizar(self.jugador, delta_ms, self.plataformas.lista)
        self.jugador.actualizar(self.plataformas.lista, self.enemigos.lista, delta_ms, lista_eventos, teclas_presionadas)
        self.portal.actualizar([self.jugador], delta_ms)

        for aux_boton in self.lista_widget:
            aux_boton.draw()
            
            


    
        