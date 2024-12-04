import pygame
import constantes
from personaje import Personaje
from arma import Arma
from mundo import Mundo
import csv
import activos

def inicializar_juego():
    # Cargar imágenes y sonidos
    animaciones = activos.cargar_imagenes_personaje()
    animaciones_animales, tipo_animales = activos.cargar_imagenes_animales()
    imagen_pistola = activos.cargar_imagenes_arma()
    imagen_balas = activos.cargar_imagenes_bala()
    lista_azulejos = activos.cargar_imagenes_azulejos()
    sonidos_animales = activos.cargar_sonidos_animales()
    sonido_agua = activos.cargar_sonido_agua()

    # Crear jugador y animales
    jugador = Personaje(100, 60, animaciones)
    gallitoDeLasRocas = Personaje(370, 300, animaciones_animales[0])
    monoChoro = Personaje(105, 330, animaciones_animales[1])
    otorongo = Personaje(735, 300, animaciones_animales[2])
    lista_animales = [gallitoDeLasRocas, otorongo, monoChoro]

    # Crear arma y grupo de balas
    pistola = Arma(imagen_pistola, imagen_balas, sonido_agua)
    grupo_balas = pygame.sprite.Group()

    # Crear datos del mundo
    data_mundo = []
    for fila in range(constantes.FILA):
        filas = [2] * constantes.COLUMNA
        data_mundo.append(filas)

    # Cargar el archivo con el nivel
    with open("niveles/nivel_1.csv", newline='') as csvfile:
        lector = csv.reader(csvfile, delimiter=',')
        for x, fila in enumerate(lector):
            for y, columna in enumerate(fila):
                data_mundo[x][y] = int(columna)

    mundo = Mundo()
    lista_azulejos = activos.cargar_imagenes_azulejos()
    mundo.procesar_datos(data_mundo, lista_azulejos)

    # Variables de movimiento del jugador
    mover_arriba = False
    mover_abajo = False
    mover_izquierda = False
    mover_derecha = False

    nivel = 1

    return {
        'jugador': jugador,
        'lista_animales': lista_animales,
        'pistola': pistola,
        'grupo_balas': grupo_balas,
        'mundo': mundo,
        'data_mundo': data_mundo,
        'lista_azulejos': lista_azulejos,
        'sonidos_animales': sonidos_animales,
        'sonido_agua': sonido_agua,
        'nivel': nivel,
        'animaciones_animales': animaciones_animales,
        'mover_arriba': mover_arriba,
        'mover_abajo': mover_abajo,
        'mover_izquierda': mover_izquierda,
        'mover_derecha': mover_derecha,
    }
