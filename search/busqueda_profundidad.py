from collections import deque
from time import sleep

from classes.celda import Celda
from classes.nodo import Nodo

movimientos = [
    (-1, 0, "ARRIBA"), # ARRIBA
    (1, 0, "ABAJO"), # ABAJO
    (0, 1, "DERECHA"), # DERECHA
    (0, -1, "IZQUIERDA"), # IZQUIERDA  
]
        
laberinto = [
    [Celda(), Celda(), Celda(), Celda(), Celda()],
    [Celda(), Celda('G'), Celda('B'), Celda(), Celda()],
    [Celda('E'), Celda('B'), Celda('B'), Celda('P'), Celda()],
    [Celda(), Celda('B'), Celda(), Celda(), Celda()],
]

def busqueda_profundidad(laberinto: list, inicio: Nodo):
    stack = deque([inicio])
    filas, columnas = len(laberinto), len(laberinto[0])
    limite = filas * columnas - 1
    
    while stack:
        nodo = stack.popleft()
        
        coordenadas_celda = nodo.celda
        iteracion = nodo.nivel
        
        celda = laberinto[coordenadas_celda[0]][coordenadas_celda[1]]
        
        print(f"Extraer: {coordenadas_celda}, iteracion: {iteracion}, {celda}")
        
        # Chequear si la celda es el objetivo
        if celda.tipo == 'E':
            print("¡Encontré a Elmo!")
            return True
        
        
        if iteracion < limite:
            # Expandir los nodos vecinos
            for movimiento in movimientos[::-1]:
                x = coordenadas_celda[0] + movimiento[0]
                y = coordenadas_celda[1] + movimiento[1]
                
                # Chequear si las coordenadas son válidas y no son un bloque
                x_valido = 0 <= x < filas
                y_valido = 0 <= y < columnas            
                
                if x_valido and y_valido:
                    nueva_celda = laberinto[x][y]
                    if nueva_celda.tipo != 'B':
                        
                        # Agregar a la pila para explorar en la siguiente iteración
                        stack.appendleft(Nodo((x, y), iteracion + 1))
                
    print("No encontré a Elmo :(")                
    return False                


busqueda_profundidad(laberinto, Nodo((0, 4), 0))