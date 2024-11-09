from classes.Node import Node
import heapq


# Implementación de A*
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star_search(start, goal, grid, movimientos, self):

    open_list = []
    closed_list = set()
    camino = []
    g_score = {start: 0}

    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)
        coordenadas = current_node.position

        try:
            cell = grid[coordenadas[0]][coordenadas[1]]
        except IndexError:
            print("Error: Coordenadas fuera de rango")

        if cell == "R" or current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent

            camino = path[::-1]

            next_step = camino[1]
            if grid[next_step[0]][next_step[1]] == "G":
                self.find_galleta = True
                print("Piggy encontro la galleta!!!!")

            return camino

        # Explorar vecinos
        for dx, dy in movimientos:

            neighbor_pos = (
                current_node.position[0] + dx, current_node.position[1] + dy)

            if neighbor_pos in closed_list:
                continue

            if (0 <= neighbor_pos[0] < len(grid) and
                0 <= neighbor_pos[1] < len(grid[0]) and
                    grid[neighbor_pos[0]][neighbor_pos[1]] != 1):

                if self.find_galleta:
                    g = current_node.g + 0.5
                else:
                    g = current_node.g + 1

                h = heuristic(neighbor_pos, goal)
                neighbor_node = Node(neighbor_pos, current_node, g, h)

                if neighbor_pos in g_score and g >= g_score[neighbor_pos]:
                    continue

                g_score[neighbor_pos] = g
                heapq.heappush(open_list, neighbor_node)

    return camino
