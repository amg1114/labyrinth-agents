
from abc import ABC, abstractmethod

import random

from search.a_star_search import a_star_search
from search.bfs_search import bfs
from search.deep_search import deep_search


class Agente(ABC):
    def __init__(self, position):
        self.position = position
        self.encontrado = False
        self.movimientos = [
            (-1, 0),  # ARRIBA
            (0, 1),  # DERECHA
            (1, 0),  # ABAJO
            (0, -1),  # IZQUIERDA
        ]


class Piggy(Agente):
    def __init__(self, position):
        self.use_a_star = False
        self.find_rene = False
        self.find_galleta = False
        super().__init__(position)

    def move(self, target_position, grid):

        if self.position == target_position:
            self.find_rene = True
            print("¡Piggy ha encontrado a René!")
            return self.position

        if random.random() < 0.4:
            self.use_a_star = True
        else:
            self.use_a_star = False

        if self.use_a_star:
            print(f"Moviendo a Piggy usando A*")
            path, costo = a_star_search(
                self.position, target_position, grid, self.movimientos, self)
        else:
            if self.find_galleta:
                costo = 0.5
            else:
                costo = 1
            print(f"Moviendo a Piggy usando BFS")
            path = bfs(self.position, target_position,
                       grid, self.movimientos, self)

        if not path:
            print("No hay camino encontrado")
            return self.position

        try:
            self.position = path[1]

            if self.position == target_position:
                self.find_rene = True
                print("¡Piggy ha encontrado a René!")

            return self.position, costo

        except IndexError:
            print("Error en el movimiento de Piggy, manteniendo posición actual.")
            return self.position, costo


class Rene(Agente):
    def get_path(self, grid):
        ruta = deep_search(self.position, grid, self.movimientos)

        if ruta:
            return ruta
        else:
            print("No hay camino encontrado")
            return None
