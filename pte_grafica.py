import pygame
import random

pygame.init()

ANCHO = 500
ALTO = 400
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Pacman versión Univalle')

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

class Laberinto:
    def __init__(self):
        self.filas = 6
        self.columnas = 6
        self.celda_ancho = ANCHO // self.columnas
        self.celda_alto = ALTO // self.filas
        self.generar_mapa()
        self.cargar_imagenes()

    def generar_mapa(self):
        self.mapa = [[0 for _ in range(self.columnas)] for _ in range(self.filas)]
        num_obstaculos = random.randint(5, 10) 

        for _ in range(num_obstaculos):
            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)
            self.mapa[fila][columna] = 1  

        self.mapa[3][2] = 2  # Galleta
        self.mapa[4][0] = 3  # Elmo
        self.mapa[5][3] = 4  # Piggy
        self.mapa[4][5] = 5  # Rana Rene

    def cargar_imagenes(self):
        imagen_rene = pygame.image.load('imagen1.png')
        imagen_elmo = pygame.image.load('imagen2.png')
        imagen_piggy = pygame.image.load('imagen3.png')
        imagen_galleta = pygame.image.load('imagen4.png')
        imagen_obstaculo = pygame.image.load('obstaculo1.png')
        imagen_camino = pygame.image.load('camino.png')

        tamaño_imagen = (self.celda_ancho, self.celda_alto)
        self.rene = pygame.transform.scale(imagen_rene, tamaño_imagen)
        self.elmo = pygame.transform.scale(imagen_elmo, tamaño_imagen)
        self.piggy = pygame.transform.scale(imagen_piggy, tamaño_imagen)
        self.galleta = pygame.transform.scale(imagen_galleta, tamaño_imagen)
        self.obstaculo = pygame.transform.scale(imagen_obstaculo, tamaño_imagen)
        self.camino = pygame.transform.scale(imagen_camino, tamaño_imagen)

    def dibujar(self, ventana):
        for fila in range(len(self.mapa)):
            for columna in range(len(self.mapa[0])): 
                x = columna * self.celda_ancho
                y = fila * self.celda_alto
                
                if self.mapa[fila][columna] == 5:
                    ventana.blit(self.rene, (x, y))  # Rana René
                elif self.mapa[fila][columna] == 3:
                    ventana.blit(self.elmo, (x, y))  # Elmo
                elif self.mapa[fila][columna] == 4:
                    ventana.blit(self.piggy, (x, y))  # Piggy
                elif self.mapa[fila][columna] == 2:
                    ventana.blit(self.galleta, (x, y))  # Galleta
                elif self.mapa[fila][columna] == 1:
                    ventana.blit(self.obstaculo, (x, y))  # Obstáculo
                elif self.mapa[fila][columna] == 0:
                    ventana.blit(self.camino, (x, y))  # Espacio vacío

def juego():
    laberinto = Laberinto()
    reloj = pygame.time.Clock()
    
    jugando = True
    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
        
        VENTANA.fill(NEGRO)
        
        laberinto.dibujar(VENTANA)
        
        pygame.display.flip()
        
        reloj.tick(60)

    pygame.quit()

juego()
