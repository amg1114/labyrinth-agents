from collections import deque
import pygame
import random
from time import sleep

from classes.Agente import Piggy, Rene


RUTA_IMAGENES = 'images/'
ANCHO = 500
ALTO = 400

VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Pacman versión Univalle')

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)


class Laberinto:
    def __init__(self, mapa):
        self.filas = len(mapa)
        self.columnas = len(mapa[0])
        self.celda_ancho = ANCHO // self.columnas
        self.celda_alto = ALTO // self.filas
        self.mapa = mapa
        self.cargar_imagenes()

    def generar_mapa(self, mapa):
        self.mapa = mapa

    def mover_agente(self, posicion, agente):
        for i in self.mapa:
            for j in self.mapa[i]:
                if self.mapa[i][j] == agente:
                    self.mapa[i][j] = 0
        self.mapa[posicion[0]][posicion[1]] = 5

    def cargar_imagenes(self):
        imagen_rene = pygame.image.load(RUTA_IMAGENES + 'imagen1.png')
        imagen_elmo = pygame.image.load(RUTA_IMAGENES + 'imagen2.png')
        imagen_piggy = pygame.image.load(RUTA_IMAGENES + 'imagen3.png')
        imagen_galleta = pygame.image.load(RUTA_IMAGENES + 'imagen4.png')
        imagen_obstaculo = pygame.image.load(RUTA_IMAGENES + 'obstaculo1.png')
        imagen_camino = pygame.image.load(RUTA_IMAGENES + 'camino.png')

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


def juego():
    pygame.display.flip()

    laberinto = Laberinto([
        # 0, 1, 2, 3, 4
        [0, 0, 0, 0, "R"],      # 0
        [0, "G", 1, 0, 0,],     # 1
        ["E", 1, 1, 0, 0,],   # 2
        [0, 1, 0, "P", 0],        # 3
    ])

    rene = Rene((0, 4))
    piggy = Piggy((3, 3))
    last_player = None

    rene_path = deque(rene.get_path(laberinto.mapa))
    rene_path.popleft()
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        if rene_path:
            mapa = mover_agente(laberinto.mapa, rene_path.popleft(), "R")
            laberinto.generar_mapa(mapa)
            last_player = rene

        if not piggy.find_rene:  # Solo mover a Piggy si no ha encontrado a René
            movimiento = piggy.move(rene.position, laberinto.mapa)
            mapa = mover_agente(laberinto.mapa, movimiento, "P")
            laberinto.generar_mapa(mapa)
            last_player = piggy

        VENTANA.fill(NEGRO)
        laberinto.dibujar(VENTANA)

        pygame.display.flip()
        sleep(1)

    pygame.quit()


def mover_agente(mapa, posicion, agente):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == agente:
                mapa[i][j] = 0

    mapa[posicion[0]][posicion[1]] = agente

    return mapa


juego()
