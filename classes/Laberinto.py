import random
import pygame
class Laberinto:
    def __init__(self, mapa, ancho, alto):
        self.filas = len(mapa)
        self.columnas = len(mapa[0])
        self.cant_obstaculos = 5
        self.celda_ancho = ancho // self.columnas
        self.celda_alto = alto // self.filas
        self.mapa = mapa
        self.ruta_imagenes = 'images/'
        self.cargar_imagenes()
        
    def posicion_aleatoria(self, ocupados):
        while True:
            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)
            if (fila, columna) not in ocupados:
                ocupados.append((fila, columna))
                return fila, columna

    def generar_mapa(self):
        ocupados = []
        obstaculos = self.cant_obstaculos

        rene_fila, rene_columna = self.posicion_aleatoria(ocupados)
        self.mapa[rene_fila][rene_columna] = "R"  # Rene

        elmo_fila, elmo_columna = self.posicion_aleatoria(ocupados)
        self.mapa[elmo_fila][elmo_columna] = "E"  # Elmo

        piggy_fila, piggy_columna = self.posicion_aleatoria(ocupados)
        self.mapa[piggy_fila][piggy_columna] = "P"  # Piggy

        galleta_fila, galleta_columna = self.posicion_aleatoria(ocupados)
        self.mapa[galleta_fila][galleta_columna] = "G"  # Galleta

        for i in range(obstaculos):
            obstaculo_fila, obstaculo_columna = self.posicion_aleatoria(
                ocupados)
            self.mapa[obstaculo_fila][obstaculo_columna] = 1  # Obstaculo

        rene_pos = (rene_fila, rene_columna)
        piggy_pos = (piggy_fila, piggy_columna)
        elmo_pos = (elmo_fila, elmo_columna)
        galleta_pos = (galleta_fila, galleta_columna)

        return self.mapa, rene_pos, piggy_pos, elmo_pos, galleta_pos

    def mover_agente(self, pos_nueva, agente, elmo_pos, pos_anterior, galleta_pos):
        if not pos_anterior:
            for i in range(len(self.mapa)):
                for j in range(len(self.mapa[i])):
                    if self.mapa[i][j] == agente:
                        self.mapa[i][j] = 0
        else:
            if pos_anterior == elmo_pos:
                for i in range(len(self.mapa)):
                    for j in range(len(self.mapa[i])):
                        if self.mapa[i][j] == agente:
                            self.mapa[i][j] = "E"
            elif agente == "R" and pos_anterior == galleta_pos:
                for i in range(len(self.mapa)):
                    for j in range(len(self.mapa[i])):
                        if self.mapa[i][j] == agente:
                            self.mapa[i][j] = "G"
            else:
                for i in range(len(self.mapa)):
                    for j in range(len(self.mapa[i])):
                        if self.mapa[i][j] == agente:
                            self.mapa[i][j] = 0
        if pos_nueva:
            self.mapa[pos_nueva[0]][pos_nueva[1]] = agente

    def cargar_imagenes(self):
        imagen_rene = pygame.image.load('images/imagen1.png')
        imagen_elmo = pygame.image.load('images/imagen2.png')
        imagen_piggy = pygame.image.load('images/imagen3.png')
        imagen_galleta = pygame.image.load('images/imagen4.png')
        imagen_obstaculo = pygame.image.load('images/obstaculo1.png')
        imagen_camino = pygame.image.load('images/camino.png')

        tamaño_imagen = (self.celda_ancho, self.celda_alto)
        self.rene = pygame.transform.scale(imagen_rene, tamaño_imagen)
        self.elmo = pygame.transform.scale(imagen_elmo, tamaño_imagen)
        self.piggy = pygame.transform.scale(imagen_piggy, tamaño_imagen)
        self.galleta = pygame.transform.scale(imagen_galleta, tamaño_imagen)
        self.obstaculo = pygame.transform.scale(
            imagen_obstaculo, tamaño_imagen)
        self.camino = pygame.transform.scale(imagen_camino, tamaño_imagen)

    def dibujar(self, ventana):
        for fila in range(len(self.mapa)):
            for columna in range(len(self.mapa[0])):
                x = columna * self.celda_ancho
                y = fila * self.celda_alto

                if self.mapa[fila][columna] == "R":
                    ventana.blit(self.rene, (x, y))  # Rana René
                elif self.mapa[fila][columna] == "E":
                    ventana.blit(self.elmo, (x, y))  # Elmo
                elif self.mapa[fila][columna] == "P":
                    ventana.blit(self.piggy, (x, y))  # Piggy
                elif self.mapa[fila][columna] == "G":
                    ventana.blit(self.galleta, (x, y))  # Galleta
                elif self.mapa[fila][columna] == 1:
                    ventana.blit(self.obstaculo, (x, y))  # Obstáculo
                elif self.mapa[fila][columna] == 0:
                    ventana.blit(self.camino, (x, y))  # Espacio vacío