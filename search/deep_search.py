from collections import deque
from time import sleep
from classes.Node import Node

def deep_search(position, grid, movimientos):
    stack = deque([Node(position)])
    filas, columnas = len(grid), len(grid[0])
    limit = filas * columnas - 1
    
    while stack:
        current_node: Node = stack.popleft()
        
        coordenadas = current_node.position
        iteracion = current_node.nivel
        
        cell = grid[coordenadas[0]][coordenadas[1]]
        
        # print("Extraer:", coordenadas, "iteracion:", iteracion, cell)
        if cell == "E":
            return construir_ruta(current_node)
        
        if iteracion < limit:
            for movimiento in movimientos[::-1]:
                x = coordenadas[0] + movimiento[0]
                y = coordenadas[1] + movimiento[1]
                
                # Chequear si las coordenadas son válidas y no son un bloque
                x_valido = 0 <= x < filas
                y_valido = 0 <= y < columnas            
                
                if x_valido and y_valido:
                    nueva_celda = grid[x][y]
                    if nueva_celda != 1:
                        # Agregar a la pila para explorar en la siguiente iteración
                        new_node = Node((x,y), current_node, nivel=iteracion + 1)
                        # print("Agregar:", new_node.position, "iteracion:", new_node.nivel, nueva_celda)
                        
                        stack.appendleft(new_node)
        # sleep(1)
        
    return None

def construir_ruta(nodo: Node):
    ruta = []
    while nodo:
        ruta.append(nodo.position)
        nodo = nodo.parent
    return ruta[::-1]