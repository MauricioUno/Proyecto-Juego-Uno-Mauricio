import pygame
from aux_constantes import *

class Form():
    '''
    Clase padre de todos los menus del juego; cada formulario creado es agregado a 'forms_dict'
    '''
    forms_dict = {}
    sounds_dict = {}
    def __init__(self,name,master_surface,x,y,w,h,color_background, imagen_background, color_border,active):
        '''
        Inicializacion del formulario; conformado por sus dimensiones, superficie, 
        fondo, su estado (que determina si se muestra el formulario) y una lista 
        de widgets que se usan para interactuar con el usuario
        '''
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border

        self.surface = pygame.Surface((w,h))
        self.slave_rect = self.surface.get_rect(x = x, y = y)
        self.active = active
        
        if imagen_background != None:
            try:
                self.image_background  = pygame.image.load(imagen_background).convert_alpha()
                self.image_background  = pygame.transform.scale(self.image_background, (self.w, self.h)).convert_alpha()
            except:
                self.image_background = None
                print("Imagen background para el formulario no encontrada")
        else:
            self.image_background = None

        self.lista_widget = []


    def on_click_boton(self, parametro):
        '''
        Metodo general que se llama al apretar un boton, activa el efecto de sonido 'click' y el formulario
        pasado como parametro
        '''
        self.play_efecto_sonido("click")
        self.set_active(parametro)


    def eliminar_formularios(self, lista_claves):
        '''
        Metodo para eliminar formularios de 'forms_dict' se usa cuando se quieran descartar
        varios formularios que ya no sean requeridos, en caso de error informa que la clave no existe
        '''
        for clave in lista_claves:
            try:
                self.forms_dict.pop(clave)
            except:
                print("La clave no existe")


    def set_active(self,name):
        '''
        Metodo que desactiva a todos los formularios de 'forms_dict', y luego activa al formulario pasado
        como parametro. Este metodo se utiliza cuando se quiere viajar entre formularios
        '''
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True


    def update_form(self, lista_eventos, delta_ms, segundo, teclas_presionadas):
        '''
        Metodo que actualiza y muestra en pantalla al primer formulario que se encuentre activo
        '''
        for form in self.forms_dict.values():
            if form.active:
                form.update(lista_eventos, delta_ms, segundo)
                form.draw(lista_eventos, delta_ms, teclas_presionadas)
                break
    

    def crear_efectos_de_sonido(self, lista_paths):
        '''
        Metodo que agregara al diccionario de sonidos los sonidos que se encuentren dentro de una lista de diccionarios
        con dos claves; 'name' y 'file'. Se utiliza al principio del programa para que los sonidos esten listos para usar
        '''
        for path in lista_paths:
            try:
                self.sounds_dict[path["name"]] = pygame.mixer.Sound(PATH_RECURSOS + "/auxiliar/{0}".format(path["file"]))
                self.sounds_dict[path["name"]].set_volume(0.25)
            except:
                print("ERROR AL CARGAR LOS SONIDOS")


    def ajustar_volumen_efectos_de_sonido(self, value):
        '''
        Metodo que recorre el diccionario de efectos de sonido y 
        ajusta el volumen de la misma manera para todos
        '''
        for sound_effect in self.sounds_dict.values():
            try:
                sound_effect.set_volume(value)
            except:
                print("Error al ajustar sonido!")

    
    def play_efecto_sonido(self, key):
        '''
        Metodo para activar el sonido que se pase como parametro, 
        si el sonido pasado como parametr no existe informa el error
        '''
        try:
            self.sounds_dict[key].play()
        except:
            print("No se puede ejecutar el sonido, key no valida")


    def activar_musica(self, music):
        '''
        Metodo para activar la musica del juego, 
        si el archivo pasado como parametro no existe informa el error
        '''
        try:
            pygame.mixer.music.load(PATH_RECURSOS + "/auxiliar/{0}.wav".format(music))
            pygame.mixer.music.play(-1)
        except:
            print("ARCHIVO NO ENCONTRADO")
    

    def render(self):
        '''
        Coloca los elementos de fondo en la superficie del formulario, 
        en caso de no tenerlos, no hara nada
        '''
        if(self.color_background != None):
            self.surface.fill(self.color_background)

        if(self.image_background != None):
            self.surface.blit(self.image_background, (0,0))

        if self.color_border != None:
            pygame.draw.rect(self.surface, self.color_border, self.surface.get_rect(), 2)


    def update(self, lista_eventos, delta_ms, segundo):
        '''
        Recorre la lista de widgets del formulario y los actualiza, recibe la lista de eventos
        para verificar el tiempo, mouse y teclado.
        '''
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)


    def draw(self, lista_eventos, delta_ms, teclas_presionadas):
        '''
        Blitea la superficie del formulario sobre la master_surface (la pantalla), luego
        en la superficie del form, coloca el fondo y los widgets
        '''
        self.master_surface.blit(self.surface,self.slave_rect)
        self.render()
        for aux_boton in self.lista_widget:
            aux_boton.draw()
            
        
        
        
        
        


