<h1 align="left">Glitch (DEMO)</h1>

Programa desarrollado con Python que permite ejecutar un videojuego 2D de plataformas basado en [GLITCH THE GAME](http://www.glitchthegame.com).
Consta de varios menus en los cuales el usuario podra navegar segun lo requiera, la posibilidad de guardar partida (a traves del uso de SQLITE) y de configurar el volumen del juego.

<h3 align="left">Imagenes:</h3>
<p align="center"> <a href="https://cdn.discordapp.com/attachments/1036152912600121356/1051553422563872919/image.png" target="_blank" rel="noreferrer"> <img src="https://cdn.discordapp.com/attachments/1036152912600121356/1051553422563872919/image.png" alt="python" width="300" height="200"/> </a><a href="https://cdn.discordapp.com/attachments/1036152912600121356/1051553837762228264/image.png" target="_blank" rel="noreferrer"> <img src="https://cdn.discordapp.com/attachments/1036152912600121356/1051553837762228264/image.png" alt="python" width="300" height="200"/> </a>
<p align="center"> <a href="https://cdn.discordapp.com/attachments/1036152912600121356/1051553944473698445/image.png" target="_blank" rel="noreferrer"> <img src="https://cdn.discordapp.com/attachments/1036152912600121356/1051553944473698445/image.png" alt="python" width="300" height="200"/> </a><a href="https://cdn.discordapp.com/attachments/1036152912600121356/1051554099969142824/image.png" target="_blank" rel="noreferrer"> <img src="https://cdn.discordapp.com/attachments/1036152912600121356/1051554099969142824/image.png" alt="python" width="300" height="200"/> </a>

<h3 align="left">Video de la demo:</h3>
<p align="center"> <a href="https://www.youtube.com/watch?v=kE6Hpu-GOVY" target="_blank" rel="noreferrer"> <img src="https://cdn.discordapp.com/attachments/1036152912600121356/1051167099122368542/main_menu.png" alt="python" width="300" height="200"/> </a>


<h2 align="left">Version Alfa:</h2>
<h3 align="left">Caracteristicas:</h3>

- El funcionamiento del juego se basa en objetos **Form** y **Widget**, que permiten la interaccion entre usuario y videojuego
- Para guardar y acceder a la informacion de la partida correspondiente se utiliza la biblioteca [SQLITE3](https://docs.python.org/es/3/library/sqlite3.html?highlight=sqlite3#module-sqlite3).
- La informacion de cada nivel se almacena en un JSON, que es leido por **FormNivel** para construirlo 


<h4 align="left">Formularios</h4>

Un formulario es una superficie que sera colocada en la pantalla junto con los elementos que la conforman. La clase **Form** es la clase padre de todos los formularios, cada uno conformado por una lista de widgets distinta y metodos que se adaptan a lo que se quiere hacer en ese formulario.

Ademas de las funciones para actualizarse y colocarse en pantalla, la clase **Form** tiene metodos que permiten activar musica, efectos de sonido y permite la navegabilidad entre los distintos formularios. Para mas informacion ver ***gui_form.py***

<h4 align="left">Widgets</h4>

La clase **Widget** es la clase padre de todos los elementos que permiten la interaccion del usuario con el menu, desde imagenes hasta cajas de texto, todo widget es dependiente de los formularios, ya que la superficie en la que se colocaran es la de su **formulario maestro**.

Los metodos de **Widget** actualizan la informacion que contienen y los blitea en la superficie de su formulario maestro, los objetos que heredan la clase **Widget**, tendran mas atributos y metodos de actualizacion mas complejos. Para mas informacion ver **gui_widget.py**.















