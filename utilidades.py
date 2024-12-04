import pygame
import os
import time

def escalar_img(imagen, escala):
    w = imagen.get_width()
    h = imagen.get_height()
    nueva_imagen = pygame.transform.scale(imagen, (w * escala, h * escala))
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