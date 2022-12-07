import sqlite3

def crear_archivo_DB():
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
    with sqlite3.connect("DATA_GLITCH.db") as conexion:
        try:
            conexion.execute("insert into Ranking (Player, Score, Timer) values (?, ?, ?)", (name,score,time))
        except:
            print("Error al guardar score! Tabla Ranking no existente")


def cargar_scores():
    with sqlite3.connect("DATA_GLITCH.db") as conexion:
        try:
            cursor=conexion.execute("SELECT `Player`, `Score`, `Timer` FROM ranking ORDER BY `Score` DESC, `Timer` ASC LIMIT 5")
            return cursor.fetchall()
        except:
            print("Error al cargar scores! Tabla Ranking no existente")
            return [()]


def guardar_partida(save, nivel, health, ammo, score, timer, unlock):
    with sqlite3.connect("DATA_GLITCH.db") as conexion:
        try:
            sentencia = "UPDATE Saves SET health=?, ammo=?, score=?, timer=?, unlock=?  WHERE save=? AND level=?"
            conexion.execute(sentencia,(health, ammo, score, timer, unlock, save, nivel))
        except:
            print("Error al guardar partida! Tabla Saves no existente!")


def crear_partida(save, name, niveles):
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
    with sqlite3.connect("DATA_GLITCH.db") as conexion:
        try:
            sentencia = "SELECT  `health`, `ammo`, `score`, `timer` FROM Saves WHERE save=? AND level=?"
            cursor = conexion.execute(sentencia,(save, nivel))
            return cursor.fetchall()[0]
        except:
            print("Error al obtener los datos")
            return (100, 10, 0, 0)


def obtener_state_nivel(save, nivel):
    with sqlite3.connect("DATA_GLITCH.db") as conexion:
        try:
            sentencia = "SELECT `unlock` FROM Saves WHERE save=? AND level=?"
            cursor = conexion.execute(sentencia,(save, nivel))
            datos = cursor.fetchall()
            return datos[0][0]
        except:
            print("Error al obtener estado del nivel")
            return True


def obtener_name_save(save):
    with sqlite3.connect("DATA_GLITCH.db") as conexion:
        try:
            cursor = conexion.execute("SELECT `name` from saves WHERE save=?",(save,))
            nombre = cursor.fetchall()[0][0]
            return nombre
        except:
            return None
            

def delete_save(save):
    with sqlite3.connect("DATA_GLITCH.db") as conexion:
        try:
            conexion.execute("DELETE FROM saves WHERE save=?",(save,))
        except:
            print("Error al intentar eliminar el save")





