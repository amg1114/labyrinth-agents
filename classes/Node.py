
class Node:
    def __init__(self, position, parent=None, g=0, h=0, nivel=0):
        self.position = position
        self.parent = parent
        self.g = g  # Costo desde el inicio
        self.h = h  # Heurística
        self.f = g + h  # Costo total
        self.nivel = nivel

    def __lt__(self, other):
        return self.f < other.f