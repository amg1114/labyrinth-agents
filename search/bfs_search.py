from collections import deque
from classes.Node import Node


# Implementación de BFS (ahora amplitud)
def bfs(start, goal, grid, movimientos, self):

    queue = deque([Node(start)])
    visited = set()
    parent_map = {start: None}

    while queue:

        current = queue.popleft()
        coordenadas = current.position
        visited.add(current.position)  # Añadir coordenadas, no el objeto

        # Verifica si estamos en la meta (usando "goal" o si es Rene)
        if grid[coordenadas[0]][coordenadas[1]] == "R" or current.position == goal:
            path = []
            while current:
                path.append(current.position)
                current = current.parent

            camino = path[::-1]

            next_step = camino[1]
            if grid[next_step[0]][next_step[1]] == "G":
                self.find_galleta = True
                print("Piggy encontro la galleta!!!!")
            return camino  # Devuelve el camino en orden correcto

        # Explorar vecinos
        for dx, dy in movimientos:
            x = coordenadas[0] + dx
            y = coordenadas[1] + dy

            x_valido = 0 <= x < len(grid)
            y_valido = 0 <= y < len(grid[0])

            if x_valido and y_valido:

                nueva_celda = grid[x][y]
                vecino_pos = (x, y)

                # Verifica que no sea un obstáculo y no haya sido visitado
                if nueva_celda != 1 and vecino_pos not in visited:

                    # Agregar a la cola para explorar en la siguiente iteración
                    new_node = Node(vecino_pos, current)

                    queue.append(new_node)
                    visited.add(vecino_pos)

                    # Registro del predecesor
                    parent_map[vecino_pos] = current.position

    return []  # No hay camino encontrado
