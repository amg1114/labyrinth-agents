
class Node:
    def __init__(self, position, parent=None, c=1, g=0, h=0, nivel=0):
        self.position = position
        self.parent = parent
        self.c = c # Costo de la celda
        self.g = g  # Costo desde el inicio
        self.h = h  # Heurística
        self.f = g + h  # Costo total
        self.nivel = nivel

    def __str__(self):
        return f"{self.position}"
    
    def __lt__(self, other):
        return self.f < other.f
    
    def __repr__(self):
        return self.__str__()
    