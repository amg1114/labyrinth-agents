from collections import deque

# Implementación de BFS


def bfs(start, goal, grid):
    queue = deque([start])
    visited = set()
    parent_map = {start: None}

    while queue:
        current = queue.popleft()
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent_map[current]
            return path[::-1]  # Devuelve el camino en orden correcto

        visited.add(current)

        # Explorar vecinos
        # Movimientos: arriba, abajo, izquierda, derecha
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_pos = (current[0] + dx, current[1] + dy)

            if (0 <= neighbor_pos[0] < len(grid) and
                0 <= neighbor_pos[1] < len(grid[0]) and
                # Verifica que no sea un obstáculo
                grid[neighbor_pos[0]][neighbor_pos[1]] != 1 and
                    neighbor_pos not in visited):

                queue.append(neighbor_pos)
                visited.add(neighbor_pos)
                parent_map[neighbor_pos] = current  # Registro del predecesor

    return []  # No hay camino encontrado
