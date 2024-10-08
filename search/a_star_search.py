from classes.Node import Node
import heapq

# Implementación de A*

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(start, goal, grid):
    open_list = []
    closed_list = set()

    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Devuelve el camino en orden correcto

        # Explorar vecinos
        # Movimientos: arriba, abajo, izquierda, derecha
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_pos = (
                current_node.position[0] + dx, current_node.position[1] + dy)

            if (0 <= neighbor_pos[0] < len(grid) and
                0 <= neighbor_pos[1] < len(grid[0]) and
                # Verifica que no sea un obstáculo
                grid[neighbor_pos[0]][neighbor_pos[1]] != 1 and
                    neighbor_pos not in closed_list):

                g = current_node.g + 1
                h = heuristic(neighbor_pos, goal)
                neighbor_node = Node(neighbor_pos, current_node, g, h)

                # Solo añadir si no está en la lista abierta o si se encontró un mejor costo
                if neighbor_node not in open_list:
                    heapq.heappush(open_list, neighbor_node)

    return []  # No hay camino encontrado
