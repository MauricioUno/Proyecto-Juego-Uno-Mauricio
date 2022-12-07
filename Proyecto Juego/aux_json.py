import json
import pygame
import sys

def importar_lista(direccion: str, key):
    '''
    Parametros:
    - La direccion de la base de datos con la que se trabajara

    Lee el archivo.json y lo almacena en una variable

    Retorna:
    - La lista dentro del diccionario
    '''
    
    try:
        with open(direccion, "r") as archivo:
            diccionario = json.load(archivo)
            return diccionario[key]
    except:
        print("ERROR! ARCHIVO JSON NO ENCONTRADO!")
        pygame.quit()
        sys.exit() 

    