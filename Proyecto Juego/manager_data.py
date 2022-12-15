import sqlite3

def crear_archivo_DB():
    '''
    Parametros:
    - None

    Funcion:
    - Establece conexion con el archivo DATABASE que contiene informacion del juego
    (ranking, partidas guardadas). En caso que no existan el archivo o las tablas donde
    se guarda la informacion, las creara.

    Retorno:
    - None
    '''
    with sqlite3.connect("DATA_GLITCH.db") as conexion:
            try:
                ranking = ''' create table if not exists Ranking
                        (
                                id integer primary key autoincrement,
                                Player text,
                                Score integer,
                                Timer integer
                        )
                    '''
                conexion.execute(ranking)

                saves = ''' create table if not exists Saves
                        (
                                Save text,
                                Name text,
                                Level integer,
                                Unlock bool,
                                Health integer,
                                Ammo integer,
                                Score integer,
                                Timer integer
                        )
                    '''
                conexion.execute(saves)                    
            except sqlite3.OperationalError:
                print("Error al crear el archivo db")


def guardar_score(name, score, time):
    '''
    Parametros:
    - Nombre del jugador
    - Puntaje del jugador
    - Cronometro del jugador

    Funcion:
    - Inserta una nueva fila en la tabla de ranking, con los datos que se pasaron como parametro

    Retorno:
    - None
    '''
    with sqlite3.connect("DATA_GLITCH.db") as conexion:
        try:
            conexion.execute("insert into Ranking (Player, Score, Timer) values (?, ?, ?)", (name,score,time))
        except:
            print("Error al guardar score! Tabla Ranking no existente")


def recibir_scores():
    '''
    Parametros:
    - None

    Funcion:
    - Selecciona las 5 filas con mayor score ordenadas de manera descendente, como segundo
    parametro se utiliza el tiempo de juego.

    Retorna:
    - Una lista de tuplas con informacion de los mejores 5 puntajes
    - Una lista de una tupla vacia en caso de error
    '''
    with sqlite3.connect("DATA_GLITCH.db") as conexion:
        try:
            cursor=conexion.execute("SELECT `Player`, `Score`, `Timer` FROM ranking ORDER BY `Score` DESC, `Timer` ASC LIMIT 5")
            return cursor.fetchall()
        except:
            print("Error al cargar scores! Tabla Ranking no existente")
            return [()]


def guardar_partida(save, nivel, health, ammo, score, timer, unlock):
    '''
    Parametros:
    - Save en el que se guardara la informacion
    - Nivel que recibira la actualizacion
    - Vida del jugador
    - Municion del jugador
    - Puntaje del jugador
    - Cronometro del jugador
    - Cambio en el estado del nivel (LOCK/UNLOCK)


    Funcion:
    - Dentro del save especificado, actualiza la informacion del nivel pasado como parametro

    Retorno:
    - None
    '''
    with sqlite3.connect("DATA_GLITCH.db") as conexion:
        try:
            sentencia = "UPDATE Saves SET health=?, ammo=?, score=?, timer=?, unlock=?  WHERE save=? AND level=?"
            conexion.execute(sentencia,(health, ammo, score, timer, unlock, save, nivel))
        except:
            print("Error al guardar partida! Tabla Saves no existente!")


def crear_partida(save, name, niveles):
    '''
    Parametros:
    - El nombre del save de la partida
    - Nombre del jugador
    - La cantidad de niveles existentes

    Funcion:
    - Inserta N cantidad de filas en funcion de la cantidad de niveles pasados como parametro
    a la tabla de SAVES, estas filas almacenaran la informacion del jugador a medida
    que avanza en la partida

    Retorno:
    - None
    '''
    with sqlite3.connect("DATA_GLITCH.db") as conexion:
        try:
            sentencia = "insert into Saves values (?,?,?,?,?,?,?,?)"
            unlock = 1
            for nivel in range(1,niveles + 1):
                conexion.execute(sentencia,(save, name, nivel, unlock, 100, 10, 0, 0))
                unlock = 0
        except:
            print("Error al crear partida! Tabla Saves no existente!")


def obtener_data_nivel(save, nivel):
    '''
    Parametros:
    - Save del que se obtendra la informacion 
    - Nivel (dentro del save) del cual se obtendra la informacion

    Funcion:
    - Selecciona los datos del jugador necesarios para cargar la partida correctamente

    Retorno:
    - Una tupla con los datos del jugador
    - Una tupla con unos datos por default en caso de error
    '''
    with sqlite3.connect("DATA_GLITCH.db") as conexion:
        try:
            sentencia = "SELECT  `health`, `ammo`, `score` FROM Saves WHERE save=? AND level=?"
            cursor = conexion.execute(sentencia,(save, nivel))
            return cursor.fetchall()[0]
        except:
            print("Error al obtener los datos")
            return (100, 10, 0)


def obtener_state_nivel(save, nivel):
    '''
    Parametros:
    - Save del que se obtendra la informacion 
    - Nivel (dentro del save) del cual se obtendra el estado

    Funcion:
    - Selecciona el estado del nivel (dentro del save) pasado como parametro

    Retorno:
    - Un booleano indicando el estado del nivel (LOCK/UNLOCK)
    - True en caso de error
    '''
    with sqlite3.connect("DATA_GLITCH.db") as conexion:
        try:
            sentencia = "SELECT `unlock` FROM Saves WHERE save=? AND level=?"
            cursor = conexion.execute(sentencia,(save, nivel))
            datos = cursor.fetchall()
            return datos[0][0]
        except:
            print("Error al obtener estado del nivel")
            return True


def obtener_reloj_nivel(save, nivel):
    '''
    Parametros:
    - Save del que se obtendra la informacion 
    - Nivel (dentro del save) del cual se obtendra el timer

    Funcion:
    - Selecciona el timer del nivel (dentro del save) pasado como parametro

    Retorno:
    - Un entero indicando el timer del nivel
    - 0 en caso de error
    '''
    with sqlite3.connect("DATA_GLITCH.db") as conexion:
        try:
            sentencia = "SELECT `timer` FROM Saves WHERE save=? AND level=?"
            cursor = conexion.execute(sentencia,(save, nivel))
            datos = cursor.fetchall()
            return datos[0][0]
        except:
            print("Error al obtener timer del nivel")
            return 0


def obtener_name_save(save):
    '''
    Parametros:
    - El save del cual se obtendra el nombre

    Funcion:
    - Selecciona el nombre del jugador dentro del save pasado como parametro

    Retorno:
    - El nombre del jugador del save 
    - None en caso de error
    '''
    with sqlite3.connect("DATA_GLITCH.db") as conexion:
        try:
            cursor = conexion.execute("SELECT `name` from saves WHERE save=?",(save,))
            nombre = cursor.fetchall()[0][0]
            return nombre
        except:
            return None
            

def delete_save(save):  
    '''
    Parametros:
    - El save que se eliminara 

    Funcion:
    - Elimina de la tabla de saves todas las filas que tengan el save pasado como parametro

    Retorno:
    - None
    '''
    with sqlite3.connect("DATA_GLITCH.db") as conexion:
        try:
            conexion.execute("DELETE FROM saves WHERE save=?",(save,))
        except:
            print("Error al intentar eliminar el save")



