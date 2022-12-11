<h1 align="left">Glitch (DEMO)</h1>

Programa desarrollado con Python que permite ejecutar un videojuego 2D de plataformas basado en [GLITCH THE GAME](http://www.glitchthegame.com).
Consta de varios menus en los cuales el usuario podra navegar segun lo requiera, la posibilidad de guardar partida (a traves del uso de SQLITE) y de configurar el volumen del juego.

<h3 align="left">Video de la demo:</h3>
<p align="left"> <a href="https://www.youtube.com/watch?v=kE6Hpu-GOVY" target="_blank" rel="noreferrer"> <img src="https://cdn.discordapp.com/attachments/1036152912600121356/1051167099122368542/main_menu.png" alt="python" width="300" height="200"/> </a>


<h2 align="left">Version Alfa:</h2>

- El funcionamiento del juego se basa en objetos **Form** y **Widget**, que permiten la interaccion entre usuario y videojuego
- Para guardar y acceder a la informacion de la partida correspondiente se utiliza la biblioteca [SQLITE3](https://docs.python.org/es/3/library/sqlite3.html?highlight=sqlite3#module-sqlite3) que permite la conexion entre python y sqlite. **manager_data.py** contiene todas las funciones necesarias de comunicacion.
- La informacion para construir cada nivel se almacena en archivos JSON que luego es recibida por **gui_form_level.py**.

<h4 align="left">Formularios</h4>

Un objeto **Form** es una superficie que sera colocada en la pantalla junto con los elementos que la conforman.
~~~
class Form():
    '''
    Clase padre de todos los menus del juego; 
    cada formulario creado es agregado a FORMS_DICT
    '''
    forms_dict = {}
    sounds_dict = {}
    def __init__(self,name,master_surface,x,y,w,h,color_background, imagen_background, color_border,active):
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

Ademas de las funciones para actualizarse y colocarse en pantalla, la clase **Form** tiene metodos que permiten activar musica, efectos de sonido y permiten la navegabilidad entre los distintos formularios en **forms_dict**. Para mas informacion ver ***gui_form.py***

<h5 align="left">Nota</h5>

- Form es la clase padre de todos los distintos objetos formulario que hay, cada uno conformado por una lista de widgets distinta y metodos que se adaptan a lo que se quiere hacer en ese formulario.

- El form mas diferente es el de FormNivel, ya que ademas de tener widgets, estara conformado por todos los elementos que se necesitan para jugar (jugador, plataformas, enemigos, etc)
___

<h4 align="left">Widgets</h4>

La clase **Widget** es la clase padre de todos los elementos que permiten la interaccion del usuario con el menu, desde imagenes hasta cajas de texto, todo widget es dependiente de los formularios, ya que la superficie en la que se colocaran es la de su **formulario maestro**
~~~
class Widget:
    def __init__(self,master,x,y,w,h,color_background, color_border, image_background, 
	text, font_size, font_color, center):
        self.center = center
        self.master_form = master # Objeto Form
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border
        self.image_background = image_background
		self.text = text
        self.font_color = font_color
		self.font_sys = pygame.font.Font("JingleBalonsGTDemo.ttf", font_size)

        self.slave_surface = pygame.Surface((self.w,self.h), pygame.SRCALPHA)
        self.slave_rect = self.slave_surface.get_rect(x = self.x, y = self.y)
        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self.master_form.x
        self.slave_rect_collide.y += self.master_form.y
~~~
Los metodos de **Widget** actualizan la informacion que contienen y los blitea en la superficie de su formulario maestro, los objetos que heredan la clase **Widget**, tendran mas atributos y metodos de actualizacion mas complejos. Para mas informacion ver **gui_widget.py**.











