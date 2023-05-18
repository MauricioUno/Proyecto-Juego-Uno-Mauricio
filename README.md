<h1 align="left">Glitch (DEMO)</h1>

Version en desarrollo de un videojuego 2D con plataformas basado en [GLITCH THE GAME](http://www.glitchthegame.com). Consta de varios menus a traves de los cuales el usuario puede navegar, la posibilidad de guardar partida y de configurar el volumen del juego.
El juego consiste en superar los obstaculos y a los enemigos para poder llegar a un portal y avanzar al siguiente nivel, cuando se terminen todos los niveles, el score total del jugador se guardara en el ranking.

<h3 align="left">Video de la demo:</h3>
<p align="center"> <a href="https://www.youtube.com/watch?v=kE6Hpu-GOVY" target="_blank" rel="noreferrer"> <img src="https://cdn.discordapp.com/attachments/1058503354034159686/1108759792715051058/glitch_demo.png" alt="python" width="350" height="250"/> </a>

<h2 align="left">Lenguajes y herramientas utilizadas:</h2><p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.sqlite.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a> <a href="https://code.visualstudio.com/" target="_blank" rel="noreferrer"> <img src="https://github.com/caidevOficial/Logos/blob/master/Lenguajes/visual-studio-code.svg?raw=true" alt="VSCode Logo" width="40" height="40"/> </a> </p>


<h3 align="left">Preparacion del entorno:</h3>

- Se requiere instalar [Anaconda](https://www.anaconda.com)
- Se requiere instalar [Visual Studio Code](https://code.visualstudio.com)
- Una vez completado los pasos anteriores se debe instalar [Pygame](https://www.pygame.org/docs/)
- Se debe ajustar las constantes PATH_RECURSOS Y PATH_JSON (en aux_constantes.py) con la direccion de acceso que corresponda a su computadora
- [Video Guía](https://www.youtube.com/watch?v=SRP-dqby6rA)


<h3 align="left">Caracteristicas:</h3>

- El funcionamiento del juego se basa en objetos **Form** y **Widget**, que permiten la interaccion entre usuario y videojuego
- Para guardar y acceder a la informacion de la partida correspondiente se utiliza la biblioteca [SQLITE3](https://docs.python.org/es/3/library/sqlite3.html?highlight=sqlite3#module-sqlite3).
- La informacion de cada nivel se almacena en un JSON, que es leido por **FormNivel** para construirlo

<h4 align="left">Formularios</h4>

Un formulario es una superficie que sera colocada en la pantalla junto con los elementos que la conforman. La clase **Form** es la clase padre de todos los formularios, cada uno conformado por una lista de widgets distinta y metodos que se adaptan a lo que se quiere hacer en ese formulario.

<h4 align="left">Widgets</h4>

La clase **Widget** es la clase padre de todos los elementos que permiten la interaccion del usuario con el menu, desde imagenes hasta cajas de texto, todo widget es dependiente de los formularios, ya que la superficie en la que se colocaran es la de su **formulario maestro**.


<h3 align="left">Cambios Planeados:</h3>

- Optimizacion de la estructura de informacion del nivel en el archivo JSON
- Optimizacion de la construccion del nivel
- Optimizacion del manejo de las animaciones de los objetos y su hitbox
- Crear un manager general de proyectiles, ya que las balas desaparecen cuando muere quien las disparo
- Terminar la documentacion de los elementos que conforman los niveles

<h3 align="left">Errores:</h3>

- El cambiar el valor de FPS puede afectar de manera negativa al juego
- La posicion del jugador al estar sobre una plataforma no se ajusta correctamente
- Hay un delay en la infuencia de una plataforma sobre el movimiento del jugador
- El cambiar la velocidad de caida puede provocar que el jugador no detecte las plataformas













