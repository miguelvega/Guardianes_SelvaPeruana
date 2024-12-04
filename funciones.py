import pygame
import constantes
import os
import time

def escalar_img(imagen, escala):
    w = imagen.get_width()
    h = imagen.get_height()
    nueva_imagen = pygame.transform.scale(imagen, (int(w * escala), int(h * escala)))
    return nueva_imagen

def contar_elementos(directorio):
    return len(os.listdir(directorio))

def nombres_carpetas(directorio):
    return os.listdir(directorio)

def distancia_manhattan(objeto1, objeto2):
    return abs(objeto1.forma.centerx - objeto2.forma.centerx) + abs(objeto1.forma.centery - objeto2.forma.centery)

def calcular_tiempo_restante(inicio, limite):
    tiempo_transcurrido = time.time() - inicio
    return max(0, limite - int(tiempo_transcurrido))

def resetear_mundo(grupo_balas):
    grupo_balas.empty()
    datos = []
    for fila in range(constantes.FILA):
        filas = [2] * constantes.COLUMNA
        datos.append(filas)
    return datos

def verificar_llamas(mapa_de_azulejos, azulejo_fuego):
    for azulejo in mapa_de_azulejos:
        if azulejo[0] == azulejo_fuego:
            return True
    return False

def permitir_atravesar_flecha(jugador, azulejo_salida, mapa_de_azulejos, azulejo_fuego):
    for azulejo in mapa_de_azulejos:
        if azulejo[0] == azulejo_salida and azulejo[1].colliderect(jugador.forma):
            if verificar_llamas(mapa_de_azulejos, azulejo_fuego):
                return False
    return True  # Corregido de 'return Truemiguelubuntu@...' a 'return True'
