import pygame
import constantes
from utilidades import escalar_img, contar_elementos, nombres_carpetas

def cargar_imagenes_personaje():
    animaciones = []
    for i in range(1, 20):
        img = pygame.image.load(f"activos/imagenes/personajes/jugador/jugador_{i}.png")
        img = escalar_img(img, constantes.ESCALA_PERSONAJE)
        animaciones.append(img)
    return animaciones

def cargar_imagenes_animales():
    directorio_animales = "activos/imagenes/personajes/animales"
    tipo_animales = nombres_carpetas(directorio_animales)
    animaciones_animales = []
    for animal in tipo_animales:
        lista_temp = []
        ruta_temp = f"{directorio_animales}/{animal}"
        num_animaciones = contar_elementos(ruta_temp)
        for i in range(num_animaciones):
            img_animal = pygame.image.load(f"{ruta_temp}/{animal}_{i}.png")
            img_animal = escalar_img(img_animal, constantes.ESCALA_ANIMAL)
            lista_temp.append(img_animal)
        animaciones_animales.append(lista_temp)
    return animaciones_animales, tipo_animales

def cargar_imagenes_arma():
    imagen_pistola = pygame.image.load("activos/imagenes/armas/pistola_de_agua.png")
    imagen_pistola = escalar_img(imagen_pistola, constantes.ESCALA_ARMA)
    return imagen_pistola

def cargar_imagenes_bala():
    imagen_balas = pygame.image.load("activos/imagenes/armas/chorro_de_agua.png")
    imagen_balas = escalar_img(imagen_balas, constantes.ESCALA_BALA)
    return imagen_balas

def cargar_imagenes_azulejos():    
    lista_azulejos = []
    for x in range(5):
        imagen_azulejo = pygame.image.load(f"activos/imagenes/azulejos/azulejo_{x}.png")
        imagen_azulejo = pygame.transform.scale(imagen_azulejo, (constantes.TALLA_AZULEJO, constantes.TALLA_AZULEJO))
        lista_azulejos.append(imagen_azulejo)
    return lista_azulejos

def cargar_sonidos_animales():
    sonidos_animales = {
        "gallitoDeLasRocas": pygame.mixer.Sound("activos/sonidos/animales/gallitoDeLasRocas.mp3"),
        "monoChoro": pygame.mixer.Sound("activos/sonidos/animales/monoChoro.mp3"),
        "otorongo": pygame.mixer.Sound("activos/sonidos/animales/otorongo.mp3"),
        "tapir": pygame.mixer.Sound("activos/sonidos/animales/tapir.mp3")
    }
    for sonido in sonidos_animales.values():
        sonido.set_volume(0)
        sonido.play(loops=-1)
    return sonidos_animales

def cargar_sonido_agua():
    sonido_agua = {
        "chorroDeAgua": pygame.mixer.Sound("activos/sonidos/agua/chorro_de_agua.mp3")
    }
    for sonido in sonido_agua.values():
        sonido.set_volume(0)
        sonido.play(loops=-1)
    return sonido_agua
