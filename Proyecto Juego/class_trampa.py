from class_A import Objeto
import re

class Trampa(Objeto):
    def __init__(self, pos_x, pos_y, ancho, alto, path_imagen, screen) -> None:
        super().__init__(path_imagen, ancho, alto, pos_x, pos_y, screen)
        self.damage = 20
        self.move_x = 0
        self.move_y = 0
        self.timer = 0


    def actualizar_posicion(self):
        self.rect.move_ip(self.move_x, self.move_y)


    def verificar_colision(self, objetivos):
        for objetivo in objetivos:
            if objetivo.rect_hitbox.colliderect(self.rect):
                objetivo.recibir_golpe(self)


    def actualizar_trampa(self, delta_ms, objetivos):
        self.timer += delta_ms
        if self.timer > 30:
            self.timer = 0
            self.actualizar_posicion()
            self.verificar_colision(objetivos)
            self.draw()


class TrampaMovil(Trampa):
    def __init__(self, pos_x, pos_y, ancho, alto, retorno, speed, move, ruta, path_imagen, screen) -> None:
        super().__init__(pos_x, pos_y, ancho, alto, path_imagen, screen)
        self.x_init = pos_x
        self.y_init = pos_y
        self.reinicio = retorno
        self.speed = speed
        self.counter = 0
        self.movimiento = move
        try:
            self.max = abs(ruta // speed)
        except:
            self.max = 0


    def controlar_movimiento(self):
        self.counter += 1
        if self.counter > self.max:
            if self.reinicio:
                self.rect.x = self.x_init 
                self.rect.y = self.y_init
            else:
                self.speed *= -1
            self.counter = 0
    
        self.move_x = self.speed
        self.move_y = self.speed
    

    def tipo_de_movimiento(self):
        if re.search("horizontal", self.movimiento, re.IGNORECASE):
            self.move_y = 0
        
        elif re.search("vertical", self.movimiento, re.IGNORECASE):
            self.move_x = 0


    def actualizar_trampa(self, delta_ms, objetivos):
        self.timer += delta_ms
        if self.timer > 30:
            self.timer = 0
            self.controlar_movimiento()
            self.tipo_de_movimiento()
            self.actualizar_posicion()
            self.verificar_colision(objetivos)
            self.draw()
    

    

class ListaTrampas():
    def __init__(self, lista_trampas, screen, name) -> None:
        self.lista = []
        self.master_form = screen
        self.name = name

        if "estatica" in lista_trampas.keys():
            self.agregar_trampa(lista_trampas["estatica"])

        
        if "movHorizontal" in lista_trampas.keys():
            self.agregar_trampa_movil(lista_trampas["movHorizontal"], "horizontal")


        if "movVertical" in lista_trampas.keys():
            self.agregar_trampa_movil(lista_trampas["movVertical"], "vertical")


    def agregar_trampa(self, lista_trampas):
        for trap in lista_trampas:
            trampa = Trampa(trap["pos"][0], trap["pos"][1], trap["dim"][0], trap["dim"][1], trap["tipo"], self.master_form)
            self.lista.append(trampa)
                    

    def agregar_trampa_movil(self, lista_trampas, move):
        for trampa in lista_trampas:
            trap = TrampaMovil(trampa["pos"][0], trampa["pos"][1], trampa["dim"][0], trampa["dim"][1], trampa["retorno"], trampa["speed"], move, trampa["route"], trampa["tipo"],self.master_form)
            self.lista.append(trap)


    def actualizar(self, delta_ms, objetivos):
        for trampa in self.lista:
            trampa.actualizar_trampa(delta_ms, objetivos)