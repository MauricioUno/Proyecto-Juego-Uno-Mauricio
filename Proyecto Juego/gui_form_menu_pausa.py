from aux_constantes import *
from gui_form import *
from gui_button import *

class FormPausa(Form):
    def __init__(self, nro_lvl, name, master_surface, x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background = None, color_border= None,active=False):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)
        self.surface.set_colorkey(C_BLACK)
        self.clave_lvl = "level_{0}".format(nro_lvl)
        self.reanudar = Button(master=self, x = w/2-110 , y = h/4, w = 220, h = 50,on_click=self.on_click_boton, on_click_param=self.clave_lvl ,text="Reanudar", font_size= 50, font_color=COLOR_TEXTO_MENU)
        self.sonido = Button(master=self, x = w/2-75 , y = h/2, w = 150, h = 50,on_click=print, on_click_param="sound",text="Sonido",font_size= 50, font_color=COLOR_TEXTO_MENU)
        self.salir = Button(master=self, x = w/2-60 , y = h/2 + h/4, w = 120, h = 50,on_click=self.volver_a_main,text="Salir",font_size= 50, font_color=COLOR_TEXTO_MENU)
        self.lista_widget = [self.reanudar, self.sonido, self.salir]
        


    def volver_a_main(self, parametro):
        self.eliminar_formularios([self.clave_lvl, "levels", "pause", "win", "lose"])
        self.activar_musica("music_main")
        self.on_click_boton("main")
