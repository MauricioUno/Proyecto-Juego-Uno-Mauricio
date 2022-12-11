import pygame
from pygame.locals import *
from aux_constantes import *
from gui_form import Form
from gui_widget_button import Button
from gui_form_level import FormNivel
from gui_widget import Widget
from manager_data import *
from gui_form_pause import FormPausa
from gui_form_win import FormWin
from gui_form_lose import FormLose

class FormMenuNiveles(Form):
    '''
    Formulario que representa el menu de seleccion de niveles del juego
    '''
    def __init__(self,save_file, name,master_surface,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background = None, color_border= None,active=False):
        '''
        Inicializacion del menu seleccion de niveles; conformado por botones de seleccion de nivel, un boton
        para borrar la partida, otro para retroceder, y dos textos que hacen referencia al nombre del jugador.
        PD: Los botones cuyo nivel no esten desbloqueados estaran desactivados.
        '''
        self.save_file = save_file
        super().__init__(name,master_surface,x,y,w,h,color_background, imagen_background, color_border,active)
        self.boton1 = Button(master=self,x=20,y=20,w=750,h=180,image_background=PATH_RECURSOS + r"\background\Forest0.png",on_click=self.click_nivel,on_click_param=1, active=obtener_state_nivel(self.save_file,1))
        self.boton2 = Button(master=self,x=20,y=220,w=750,h=180,image_background=PATH_RECURSOS + r"\background\Snow0.png",on_click=self.click_nivel,on_click_param=2, active=obtener_state_nivel(self.save_file,2))
        self.boton3 = Button(master=self,x=20,y=420,w=750,h=180,image_background=PATH_RECURSOS + r"\background\Cave0.png",on_click=self.click_nivel,on_click_param=3, active=obtener_state_nivel(self.save_file,3))
        self.boton4 = Button(master=self,x=20, y=670, w=120,h =50,on_click=self.retroceder, text="atras",font_size= 50) 
        self.title =  Widget(master=self, x = 1000, y = 20, w = 300, h = 100, text= "Jugador:", font_size=70)
        self.nombre = Widget(master=self, x = 1000, y = 130, w = 300, h = 70, text= obtener_name_save(self.save_file), font_size=50)
        self.delete = Button(master=self,x=1220 , y=670, w=260,h =50,on_click=self.borrar_data,text="Delete Data", font_size= 50) 
        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4, self.title, self.nombre, self.delete]


    def retroceder(self, parametro):
        '''
        Elimina al formulario 'levels' de forms_dict y pone en activo al formulario 'saves'
        '''
        self.forms_dict.pop("levels")
        self.on_click_boton("saves")


    def borrar_data(self, parametro):
        '''
        Accede a la DATABASE y elimina todo lo referente al save que haga referencia self.save_file, y tambien
        elimina a los formularios 'levels' y 'saves', pone en activo al formulario 'main'
        '''
        delete_save(self.save_file)
        self.eliminar_formularios(["levels", "saves"])
        self.on_click_boton("main")


    def click_nivel(self, nro_lvl):
        '''
        Elimina al formulario 'saves' de forms_dict y llama a la funcion start_level que se encargara de empezar el nivel
        '''
        self.forms_dict.pop("saves")
        self.start_level(nro_lvl)


    def start_level(self, nro_lvl):
        '''
        Crea al formulario que representa al nivel que se esta jugando, junto con los formularios 'pause', 'lose' y 'win'.
        Pone en activo al nivel que corresponda junto con su musica
        '''
        FormNivel(save_file = self.save_file,nivel = nro_lvl, master_surface = self.master_surface)
        FormPausa(save_file = self.save_file, nro_lvl=nro_lvl, name="pause", master_surface=self.master_surface, x = 600, y=180, w=300, h=350, imagen_background= PATH_RECURSOS + r"\gui\TablaV.png")
        FormWin(save_file= self.save_file,nro_lvl= nro_lvl, name="win", master_surface=self.master_surface, x = 375, y = 135, w = 750, h =450, imagen_background= PATH_RECURSOS + r"\gui\TablaH.png")
        FormLose(save_file = self.save_file,nro_lvl= nro_lvl,name="lose", master_surface=self.master_surface, x = 550, y = 180, w = 400, h=350, imagen_background= PATH_RECURSOS + r"\gui\TablaH.png")
        self.on_click_boton("level_{0}".format(nro_lvl))
        self.activar_musica("music_level_{0}".format(nro_lvl))

       
        
        