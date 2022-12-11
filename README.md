<h1 align="left">Glitch (DEMO)</h1>

Programa desarrollado con Python que permite ejecutar un videojuego 2D de plataformas basado en [GLITCH THE GAME](http://www.glitchthegame.com).
Consta de varios menus en los cuales el usuario podra navegar segun lo requiera, la posibilidad de guardar partida (a traves del uso de SQLITE) y de configurar el volumen del juego.

<h3 align="left">Video de la demo:</h3>
<p align="left"> <a href="https://www.youtube.com/watch?v=kE6Hpu-GOVY" target="_blank" rel="noreferrer"> <img src="https://cdn.discordapp.com/attachments/1036152912600121356/1051167099122368542/main_menu.png" alt="python" width="300" height="200"/> </a>


<h2 align="left">Version Alfa:</h2>
- El funcionamiento del juego se basa en objetos **Form** y **Widget**, que permiten la interaccion entre usuario y videojuego
- Para guardar y acceder a la informacion de la partida correspondiente se utiliza la biblioteca [SQLITE3](https://docs.python.org/es/3/library/sqlite3.html?highlight=sqlite3#module-sqlite3) que permite la conexion entre python y sqlite.
- La informacion de cada nivel se almacena en archivos JSON que luego es recibida por el programa para construir el nivel.



####Formularios y Widgets####
Un objeto **Form** es una superficie que sera colocada en la pantalla junto con los elementos que la conforman.
~~~
class Form():
    '''
    Clase padre de todos los menus del juego; 
    cada formulario creado es agregado a 'forms_dict'
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
        self.master_surface = master_surface  #La superficie de la pantalla
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border
        self.image_background = imagen_background
        self.surface = pygame.Surface((w,h))
        self.slave_rect = self.surface.get_rect(x = x, y = y)
        self.active = active
        self.lista_widget = []
~~~

Ademas de las funciones para actualizarse y colocarse en pantalla, la clase **Form** tiene metodos que permiten activar musica, efectos de sonido y la navegabilidad entre los distintos formularios en **forms_dict**.
El metodo que se utiliza en el main principal es update_form:
~~~
def update_form(self, lista_eventos, delta_ms, segundo, teclas_presionadas):
        '''
        Recorre toda el diccionario de formulario, actualiza y muestra en
		pantalla al formulario que este ACTIVO
        '''
        for form in self.forms_dict.values():
            if form.active:
                form.update(lista_eventos, delta_ms, segundo)
                form.draw(lista_eventos, delta_ms, teclas_presionadas)
                break
~~~

De esta forma:
~~~
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
clock = pygame.time.Clock()

segundo = pygame.USEREVENT + 0
pygame.time.set_timer(segundo,1000)

main_menu = FormMenuMain(name="main", master_surface = screen)
while True:
    
    delta_ms = clock.tick(FPS)
    lista_eventos = pygame.event.get()
    teclas_presionadas = pygame.key.get_pressed()
    for event in lista_eventos:
        if event.type == pygame.QUIT:       
            pygame.quit()
            sys.exit() 
    
    main_menu.update_form(lista_eventos, delta_ms, segundo, teclas_presionadas) 
    pygame.display.flip()
~~~









