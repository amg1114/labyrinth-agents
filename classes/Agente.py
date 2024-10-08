
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
            (0, 1), # DERECHA
            (1, 0),  # ABAJO
            (0, -1), # IZQUIERDA
        ]
   


class Piggy(Agente):
    def __init__(self, position):
        self.use_a_star = False
        super().__init__(position)
        
    def move(self, target_position, grid):
         # Decide si cambiará la estrategia por A* con 40% de probabilidad
        if random.random() < 0.4:
            self.use_a_star = True
        else:
            self.use_a_star = False

        if self.use_a_star:
            # print(f"Moviendo a Piggy usando A*")
            path = a_star_search(self.position, target_position, grid, self.movimientos)
        else:
            # print(f"Moviendo a Piggy usando búsqueda por amplitud hacia")
            path = bfs(self.position, target_position, grid, self.movimientos)

        if path:
            try:
                self.position = path[1]
                return self.position
            except IndexError:
                return self.position
        else:
            print("No hay camino encontrado")
            return self.position  # No hay movimiento posible
        
class Rene(Agente):
    def get_path(self, grid):
        ruta = deep_search(self.position, grid, self.movimientos)
        
        if ruta:
            return ruta
        else:
            print("No hay camino encontrado")
            return None