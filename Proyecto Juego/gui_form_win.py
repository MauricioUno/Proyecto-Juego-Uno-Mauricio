from aux_constantes import *
from gui_form import Form
from gui_widget_button import Button
from gui_widget import Widget
from gui_form_level import FormNivel
from manager_data import *
from aux_json import importar_lista


class FormWin(Form):
    '''
    Formulario que representa el menu de victoria
    '''
    def __init__(self, save_file, nro_lvl, name, master_surface, x, y, w, h, color_background = None, imagen_background = None, color_border = None, active = False):
        '''
        Inicializacion del menu win; conformado por 3 botones; cada uno con funciones distintas, los widgets necesarios
        para representar la informacion del jugador, junto con todo lo referente para saber de donde recibir y enviar
        informacion de la partida
        '''   
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active) 
        self.surface.set_colorkey(C_BLACK)
        self.save_file = save_file
        self.nro_lvl = nro_lvl
        self.clave_lvl = "level_{0}".format(nro_lvl)
        data_nivel = importar_lista(PATH_JSON.format(self.clave_lvl), self.clave_lvl)[0]
        self.score_tiempo = data_nivel["score_tiempo"]
        self.score_vida = data_nivel["score_vida"]
        self.win = Widget(master=self, x = w/2 -150, y = 5, w = 300, h = 70, text= "Ganaste!", font_size=70, font_color=COLOR_TEXTO_MENU)
        self.home = Button(master=self, x= w/2 - 33 ,y = 370, w = 50, h= 50, image_background= PATH_RECURSOS + r"\gui\menu.png", on_click= self.volver_a_main)
        self.reset = Button(master=self, x= w/2 - 190 ,y = 370, w = 50, h= 50, image_background= PATH_RECURSOS + r"\gui\restart.png", on_click= self.replay, on_click_param= self.clave_lvl)
        self.next = Button(master=self, x= w/2 + 133 ,y = 370, w = 50, h= 50, image_background= PATH_RECURSOS + r"\gui\next.png", on_click= self.next_lvl, on_click_param= None)
        self.clock = Widget (master=self, x= w/4 -100, y = h/4-20, w=40, h=40, image_background=PATH_RECURSOS + r"\gui\win_time.png")
        self.heart = Widget (master=self, x= w/4 -100, y = h/4+30, w=40, h=40, image_background=PATH_RECURSOS + r"\gui\win_heart.png")
        self.score = Widget (master=self, x= w/4 -100, y = h/4+80, w=40, h=40, image_background=PATH_RECURSOS + r"\gui\win_star.png")
        
        self.text_total = Widget (master=self, x= w/4 -100, y = h/4+130, w = self.w, h = 70, text= "Score Total: ", font_size=60, font_color=COLOR_TEXTO_MENU, center=False)
        self.text_clock = Widget(master=self, x = w/4 - 40, y = self.clock.y, w = self.w, h = 50, text= " ", font_size=40, font_color=COLOR_TEXTO_MENU, center=False)
        self.text_heart = Widget(master=self, x = w/4 - 40, y = self.heart.y, w = self.w, h = 50, text= " ", font_size=40, font_color=COLOR_TEXTO_MENU, center=False)
        self.text_score = Widget(master=self, x = w/4 - 40, y = self.score.y, w = self.w, h = 50, text= " ", font_size=40, font_color=COLOR_TEXTO_MENU, center=False)
        self.lista_widget = [self.win, self.home, self.reset, self.next, self.clock, self.heart, self.score, self.text_clock, self.text_heart, self.text_score, self.text_total]
        self.score_total = 0


    def next_lvl(self, nada):
        '''
        En caso que no sea el ultimo nivel, se elimina a todos los formularios relacionados al nivel actual, y se llama
        a la funcion 'start_level' del formulario 'levels'
        '''
        if self.nro_lvl < ULTIMO_NIVEL:
            self.eliminar_formularios([self.clave_lvl, "pause", "win", "lose"])
            self.forms_dict["levels"].start_level(self.nro_lvl + 1)


    def replay(self, nada):
        '''
        Descarta el formulario que representa al nivel y vuelve a crearlo, lo pone en activo
        '''
        self.forms_dict.pop(self.clave_lvl)
        FormNivel(save_file = self.save_file, nivel = self.nro_lvl, master_surface = self.master_surface)
        self.on_click_boton(self.clave_lvl)


    def volver_a_main(self, parametro):
        '''
        Elimina de forms_dict todos los formularios que se utilizan al estar en un nivel y vuelve al menu principal
        '''
        self.eliminar_formularios([self.clave_lvl, "levels", "pause", "win", "lose"])
        self.activar_musica("music_main")
        self.on_click_boton("main")
        

    def puntaje_obtenido(self, vida, scorePlayer, municion, tiempo):
        '''
        Recibe como parametro los datos relacionados al jugador al momento de superar el nivel, estos
        parametros se utilizan para aisgnarles un valor a los widget que los representan.
        Guarda la partida del jugador en el save que corresponda, en caso de ser el ultimo nivel
        guardara el score en la tabla de ranking
        '''
        self.text_clock.text = f"{tiempo} x {self.score_tiempo} = {tiempo*self.score_tiempo}"
        self.text_heart.text = f"{vida} x {self.score_vida} = {vida*self.score_vida}"
        self.text_score.text = f"Score nivel = {scorePlayer}"
        
        self.score_total = scorePlayer + tiempo*self.score_tiempo + vida*self.score_vida
        self.text_total.text = f"Score Total: {self.score_total}"

        cronometro = obtener_reloj_nivel(self.save_file, self.nro_lvl)
        if self.nro_lvl < ULTIMO_NIVEL:
            guardar_partida(self.save_file, self.nro_lvl + 1, vida, municion, self.score_total, (cronometro + 60 - tiempo), True)
        else:
            guardar_score(obtener_name_save(self.save_file), self.score_total, (cronometro + 60 - tiempo))