from enemy_groodle import SpiritGroodle
from enemy_ix import SpiritIx
from enemy_batterflies import Batterfly
from aux_constantes import *


class ListaEnemigos:
    def __init__(self, lista_enemigos, screen) -> None:
        self.lista = []

        if "ix" in lista_enemigos.keys():
            self.agregar_spirit_ix(lista_enemigos["ix"], screen)

        if "groodle" in lista_enemigos.keys():
            self.agregar_spirit_groodle(lista_enemigos["groodle"], screen)

        if "batterfly" in lista_enemigos.keys():
            self.agregar_batterfly(lista_enemigos["batterfly"]["cant"], screen)

        


    def actualizar(self, jugador, delta_ms):     
        for enemigo in self.lista:
            enemigo.actualizar(jugador, delta_ms)
            if not enemigo.activo:
                self.lista.remove(enemigo)    


    def agregar_spirit_groodle(self, lista_groodle, screen):
        for groodle in lista_groodle:
            enemigo_groodle = SpiritGroodle(groodle["coordenadas"][0], groodle["coordenadas"][1], groodle["direccion"], screen)
            self.lista.append(enemigo_groodle)


    def agregar_spirit_ix(self, lista_ix, screen):
        for ix in lista_ix:
            enemigo_ix = SpiritIx(ix["coordenadas"][0], ix["coordenadas"][1], ix["width_ruta"], screen)
            self.lista.append(enemigo_ix)


    def agregar_batterfly(self, cantidad, screen):
        for i in range(cantidad):
            batterfly = Batterfly(screen)
            self.lista.append(batterfly)
        