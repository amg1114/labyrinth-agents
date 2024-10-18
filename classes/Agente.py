
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
        # Si Piggy ya ha encontrado a René, detén el movimiento
        if self.find_rene:
            print("Piggy ya encontró a René, deteniendo movimiento.")
            return self.position  # No realizar más movimientos

        if self.position == target_position:
            self.find_rene = True
            print("¡Piggy ha encontrado a René!")
            return self.position

        # Decide si cambiará la estrategia por A* con 40% de probabilidad
        if random.random() < 0.4:
            self.use_a_star = True
        else:
            self.use_a_star = False

        # Usar A* o BFS según la probabilidad
        if self.use_a_star:
            print(f"Moviendo a Piggy usando A*")
            path, costo = a_star_search(
                self.position, target_position, grid, self.movimientos, self)
            print("find galleta? ", self.find_galleta)
        else:
            if self.find_galleta:
                costo = 0.5
            else:
                costo = 1
            print(f"Moviendo a Piggy usando BFS")
            path = bfs(self.position, target_position,
                       grid, self.movimientos, self)
            print("find galleta? ", self.find_galleta)

        # Si no se encuentra un camino, devuelve la posición actual
        if not path:
            print("No hay camino encontrado")
            return self.position

        try:
            self.position = path[1]  # Mover al siguiente nodo en el camino
            print(f"Piggy se mueve a {self.position}")

            # Si Piggy llega a la posición de René, detén el movimiento
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
