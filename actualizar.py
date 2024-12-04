import pygame
import constantes
from utilidades import distancia_manhattan
import funciones
import csv
from mundo import Mundo
from personaje import Personaje

def actualizar_estado(estado_del_juego):
    jugador = estado_del_juego['jugador']
    mundo = estado_del_juego['mundo']
    lista_animales = estado_del_juego['lista_animales']
    pistola = estado_del_juego['pistola']
    grupo_balas = estado_del_juego['grupo_balas']
    lista_azulejos = estado_del_juego['lista_azulejos']
    sonidos_animales = estado_del_juego['sonidos_animales']
    sonido_agua = estado_del_juego['sonido_agua']
    nivel = estado_del_juego['nivel']
    animaciones_animales = estado_del_juego['animaciones_animales']
    
    delta_x = 0
    delta_y = 0

    if estado_del_juego['mover_derecha']:
        delta_x = constantes.VELOCIDAD
    if estado_del_juego['mover_izquierda']:
        delta_x = -constantes.VELOCIDAD
    if estado_del_juego['mover_arriba']:
        delta_y = -constantes.VELOCIDAD
    if estado_del_juego['mover_abajo']:
        delta_y = constantes.VELOCIDAD

    nivel_completado = jugador.movimiento(delta_x, delta_y, mundo.azulejos_obstaculos, mundo.azulejo_salida)

    if not funciones.permitir_atravesar_flecha(jugador, lista_azulejos[4], mundo.mapa_de_azulejos, lista_azulejos[0]):
        jugador.forma.right = min(jugador.forma.right, constantes.ANCHO_VENTANA - constantes.TALLA_AZULEJO)

    jugador.actualizar()
    for animal in lista_animales:
        animal.actualizar()

    bala = pistola.actualizar(jugador)
                    
    if bala:
        grupo_balas.add(bala)

    for bala in grupo_balas:
        bala.actualizar(mundo.azulejos_obstaculos, mundo.mapa_de_azulejos, mundo, lista_azulejos, estado_del_juego)

    # Actualizar lista de animales si se cambia de nivel
    if nivel == 2:
        lista_animales.clear()
        tapir = Personaje(780, 450, animaciones_animales[3])
        gallitoDeLasRocas = Personaje(450, 90, animaciones_animales[0])
        lista_animales.extend([tapir, gallitoDeLasRocas])
        estado_del_juego['nivel'] = 3

    # Gestionar cambio de nivel
    if nivel_completado and not funciones.verificar_llamas(mundo.mapa_de_azulejos, lista_azulejos[0]):
        estado_del_juego['nivel'] += 1
        if estado_del_juego['nivel'] < 4:
            data_mundo = funciones.resetear_mundo(grupo_balas)
            with open(f"niveles/nivel_{estado_del_juego['nivel']}.csv", newline='') as csvfile:
                lector = csv.reader(csvfile, delimiter=',')
                for x, fila in enumerate(lector):
                    for y, columna in enumerate(fila):
                        data_mundo[x][y] = int(columna)
            mundo = Mundo()
            mundo.procesar_datos(data_mundo, lista_azulejos)
            estado_del_juego['mundo'] = mundo
            estado_del_juego['data_mundo'] = data_mundo

    # Gestionar sonidos de animales basados en la distancia
    rango_proximidad = 200

    nombres_animales_nivel = []
    if estado_del_juego['nivel'] == 1:
        nombres_animales_nivel = ["gallitoDeLasRocas", "monoChoro", "otorongo"]
    elif estado_del_juego['nivel'] == 3:
        nombres_animales_nivel = ["tapir", "gallitoDeLasRocas"]

    for i, animal in enumerate(lista_animales):
        if i < len(nombres_animales_nivel):
            nombre_animal = nombres_animales_nivel[i]
            distancia = distancia_manhattan(jugador, animal)
            if distancia <= rango_proximidad:
                volumen = max(0, 1 - distancia / rango_proximidad)
                sonidos_animales[nombre_animal].set_volume(volumen)
            else:
                sonidos_animales[nombre_animal].set_volume(0)