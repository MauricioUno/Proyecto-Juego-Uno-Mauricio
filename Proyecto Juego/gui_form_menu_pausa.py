from aux_constantes import *
from gui_form import *
from gui_button import *
from gui_form_pausa_sonido import FormPausaSonido
from gui_form_nivel import FormNivel

class FormPausa(Form):
    '''
    Formulario que representa al menu de pausa
    '''
    def __init__(self, save_file, nro_lvl, name, master_surface, x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background = None, color_border= None,active=False):
        '''
        Inicializacion del formulario 'pause', conformado por 4 botones con distinas funciones y la informacion
        necesaria para saber de donde recibir y enviar informacion sobre la partida
        '''
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)
        self.surface.set_colorkey(C_BLACK)
        self.save_file = save_file
        self.clave_lvl = "level_{0}".format(nro_lvl)
        self.nro_lvl = nro_lvl
        self.reanudar = Button(master=self, x = w/2-110 , y = 20, w = 220, h = 50,on_click=self.on_click_boton, on_click_param=self.clave_lvl ,text="Reanudar", font_size= 50, font_color=COLOR_TEXTO_MENU)
        self.reiniciar = Button(master=self, x = w/2-110 , y = 80, w = 220, h = 50,on_click=self.replay, on_click_param=self.clave_lvl ,text="Reiniciar", font_size= 50, font_color=COLOR_TEXTO_MENU)
        self.sonido = Button(master=self, x = w/2-75 , y = 140, w = 150, h = 50,on_click=self.sound_pausa, on_click_param="sound",text="Sonido",font_size= 50, font_color=COLOR_TEXTO_MENU)
        self.salir = Button(master=self, x = w/2-60 , y = 200 , w = 120, h = 50,on_click=self.volver_a_main,text="Salir",font_size= 50, font_color=COLOR_TEXTO_MENU)
        self.lista_widget = [self.reanudar, self.sonido, self.salir, self.reiniciar]
        

    
    def replay(self, nada):
        '''
        Descarta el formulario que representa al nivel y vuelve a crearlo, lo pone en activo
        '''
        self.forms_dict.pop(self.clave_lvl)
        FormNivel(save_file = self.save_file, nivel = self.nro_lvl, master_surface = self.master_surface)
        self.on_click_boton(self.clave_lvl)


    def sound_pausa(self, parametro):
        '''
        Crea un formulario equivalente a FormSonido y lo pone en activo, formulario 'pause' sigue existiendo en forms_dict
        '''
        FormPausaSonido(name="sound", master_surface = self.master_surface, x = 600, y=180, w=300, h=350, imagen_background =PATH_RECURSOS + r"\gui\TablaV.png")
        self.on_click_boton("sound")

    def volver_a_main(self, parametro):
        '''
        Elimina de forms_dict todos los formularios que se utilizan al estar en un nivel y vuelve al menu principal
        '''
        self.eliminar_formularios([self.clave_lvl, "levels", "pause", "win", "lose"])
        self.activar_musica("music_main")
        self.on_click_boton("main")
