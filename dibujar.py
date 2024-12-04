import funciones
import pygame
import time

def dibujar_elementos(ventana, estado_de_juego, puntaje):
    jugador = estado_de_juego['jugador']
    mundo = estado_de_juego['mundo']
    lista_animales = estado_de_juego['lista_animales']
    pistola = estado_de_juego['pistola']
    grupo_balas = estado_de_juego['grupo_balas']
    tiempo_inicial = estado_de_juego['tiempo_inicial']
    tiempo_limite = estado_de_juego['tiempo_limite']
    
    mundo.dibujar(ventana)
    jugador.dibujar(ventana)
    
    fondo_temporizador = pygame.font.Font(None, 70)
    tiempo_restante = max(0, tiempo_limite - int(time.time() - tiempo_inicial))
    texto_temporizador = fondo_temporizador.render(f"Tiempo: {tiempo_restante}", True, (128, 0, 128))
    ventana.blit(texto_temporizador, (300, 10))
    
    puntaje.dibujar(ventana, estado_de_juego['puntaje'])
    
    for animal in lista_animales:
        animal.dibujar(ventana)
    pistola.dibujar(ventana)
    for bala in grupo_balas:
        bala.dibujar(ventana)
