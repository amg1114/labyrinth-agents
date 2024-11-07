import pygame
import random

from collections import deque
from time import sleep

from classes.Agente import Piggy, Rene

pygame.init()

RUTA_IMAGENES = 'images/'
ANCHO = 500
ALTO = 400
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Pacman versión Univalle')


class Laberinto:
    def __init__(self, mapa):
        self.filas = len(mapa)
        self.columnas = len(mapa[0])
        self.celda_ancho = ANCHO // self.columnas
        self.celda_alto = ALTO // self.filas
        self.mapa = mapa
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
        obstaculos = 5

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

        elmo_pos = (elmo_fila, elmo_columna)

        return self.mapa, rene_fila, rene_columna, piggy_fila, piggy_columna, elmo_pos

    def set_mapa(self, mapa):
        self.mapa = generar_mapa()

    def mover_agente(self, pos_nueva, agente, elmo_pos, pos_anterior):
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
            else:
                for i in range(len(self.mapa)):
                    for j in range(len(self.mapa[i])):
                        if self.mapa[i][j] == agente:
                            self.mapa[i][j] = 0
        if pos_nueva:
            self.mapa[pos_nueva[0]][pos_nueva[1]] = agente

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


def welcome():
    fondo = pygame.image.load(RUTA_IMAGENES + 'fondo_bienvenida.png')
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    play_button = pygame.rect.Rect(ANCHO // 2 - 50, ALTO // 2 - 25, 100, 50)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
                return False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(evento.pos):
                    return True

        VENTANA.blit(fondo, (0, 0))
        mouse = pygame.mouse.get_pos()

        button_color = BLANCO
        shadow_offset = 0

        if play_button.collidepoint(mouse):
            button_color = (200, 200, 200)
            shadow_offset = 5

        shadow_rect = pygame.rect.Rect(
            play_button.left + shadow_offset, play_button.top + shadow_offset, play_button.width, play_button.height)
        pygame.draw.rect(VENTANA, (50, 50, 50), shadow_rect, border_radius=10)
        pygame.draw.rect(VENTANA, button_color, play_button, border_radius=10)

        font = pygame.font.Font(None, 40)
        text = font.render("Jugar", True, NEGRO)
        VENTANA.blit(text, (play_button.x + 20, play_button.y + 10))

        pygame.display.flip()


def juego():
    costo_acumulado = 0
    pygame.display.flip()

    laberinto = Laberinto([[0 for _ in range(5)] for _ in range(5)])
    mapa_aleatorio, rene_fila, rene_columna, piggy_fila, piggy_columna, elmo_pos = laberinto.generar_mapa()

    rene = Rene((rene_fila, rene_columna))
    piggy = Piggy((piggy_fila, piggy_columna))

    turno = rene
    rene_pos = None
    rene_pos_anterior = None
    piggy_pos = None
    piggy_pos_anterior = None

    rene_path = deque(rene.get_path(laberinto.mapa))
    rene_path.popleft()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        if piggy.find_rene or not rene_path:
            pygame.quit()
            quit()
        elif turno == piggy:

            if not piggy.find_rene:
                piggy_pos_anterior = piggy_pos
                movimiento, costo = piggy.move(rene_pos, laberinto.mapa)
                costo_acumulado += costo
                piggy_pos = movimiento

                laberinto.mover_agente(
                    piggy_pos, "P", elmo_pos, piggy_pos_anterior)

                print("Mueve piggy")
                print("Costo Acumulado de piggy", costo_acumulado)
                sleep(1)

            turno = rene

        elif turno == rene and rene_path:

            rene_pos_anterior = rene_pos
            rene_pos = rene_path.popleft()

            laberinto.mover_agente(rene_pos, "R", elmo_pos, rene_pos_anterior)

            turno = piggy
            print("Mueve Rene")
            sleep(1)

        VENTANA.fill(NEGRO)
        laberinto.dibujar(VENTANA)

        pygame.display.flip()

    pygame.quit()


if welcome():
    juego()
