import sqlite3

def crear_data_base_niveles():
    with sqlite3.connect("Levels.db") as conexion:
        try:
            sentencia = ''' create table Levels
                    (
                            Nivel integer,
                            Unlock bit,
                            Health integer,
                            Ammo integer,
                            Score integer,
                            cronometro integer
                    )
                '''
            conexion.execute(sentencia)
            conexion.execute("insert into Levels values (?, ?, ?, ?, ?, ?)", (1, 1, 100, 10, 0, 0))
            conexion.execute("insert into Levels values (?, ?, ?, ?, ?, ?)", (2, 0, 100, 10, 0, 0))
            conexion.execute("insert into Levels values (?, ?, ?, ?, ?, ?)", (3, 0, 100, 10, 0, 0))
        except sqlite3.OperationalError:
            print("La tabla niveles ya existe")


def actualizar_datos_nivel(nivel, health, ammo, score, cronometro, unlock):
    with sqlite3.connect("Levels.db") as conexion:
        try:
            sentencia = "UPDATE Levels SET health=?, ammo=?, score=?, cronometro=?, unlock=?  WHERE Nivel=?"
            conexion.execute(sentencia,(health, ammo, score, cronometro, unlock, nivel))
        except:
            print("Error al actualizar datos del nivel")


def obtener_datos_nivel(nivel):
    with sqlite3.connect("Levels.db") as conexion:
        try:
            sentencia = "SELECT  `health`, `ammo`, `score`, `cronometro`, `unlock` FROM Levels WHERE Nivel=?"
            cursor = conexion.execute(sentencia,(nivel,))
            datos = cursor.fetchall()
            return datos[0]
        except:
            print("Error al obtener datos del nivel")


def obtener_estado_nivel(nivel):
    with sqlite3.connect("Levels.db") as conexion:
        try:
            sentencia = "SELECT `unlock` FROM Levels WHERE Nivel=?"
            cursor = conexion.execute(sentencia,(nivel,))
            datos = cursor.fetchall()
            return datos[0]
        except:
            print("Error al obtener datos del nivel")