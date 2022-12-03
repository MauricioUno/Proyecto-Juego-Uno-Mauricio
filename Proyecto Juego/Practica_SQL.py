import sqlite3

def crear_data_base_ranking():
    with sqlite3.connect("Ranking.db") as conexion:
        try:
            sentencia = ''' create table ranking
                    (
                            id integer primary key autoincrement,
                            Player text,
                            Score integer,
                            time integer
                    )
                '''
            conexion.execute(sentencia)                       
        except sqlite3.OperationalError:
            print("La tabla ranking ya existe")


def insertar_fila(name, score, time):
    with sqlite3.connect("Ranking.db") as conexion:
        try:
            conexion.execute("insert into ranking (Player, Score, time) values (?, ?, ?)", (name,score,time))
            conexion.commit()
        except:
            print("Error al ingresar datos a la DB")


def obtener_filas():
    with sqlite3.connect("Ranking.db") as conexion:
        try:
            cursor=conexion.execute("SELECT `Player`, `Score`, `Time` FROM ranking ORDER BY `Score` DESC LIMIT 5")
            datos = cursor.fetchall()
            return datos
        except:
            print("Error al obtener los datos de la DB")

        



    
