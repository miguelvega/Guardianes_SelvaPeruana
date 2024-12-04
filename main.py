import pygame
import constantes
from iniciar_juego import inicializar_juego
import actualizar
import dibujar
import controlador_eventos
from pantalla_resultado import Pantalla_resultado
import time
from puntaje import Puntaje

pygame.init()


ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VETANA))
pygame.display.set_caption("Salvando Animales del Peru")


def resetear_juego():
    pygame.mixer.stop()  
    estado = inicializar_juego()
    estado['ejecutar'] = True
    estado['ventana'] = ventana
    estado['tiempo_inicial'] = time.time()
    estado['tiempo_limite'] = constantes.TIEMPO_LIMITE  # 60s
    estado['puntaje'] = 0
    return estado


estado_del_juego = resetear_juego()
pantalla_resultado = None
reloj = pygame.time.Clock()
puntaje = Puntaje()

while estado_del_juego['ejecutar']:
    reloj.tick(constantes.FPS)
    ventana.fill(constantes.COLOR_FONDO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            estado_del_juego['ejecutar'] = False
        elif pantalla_resultado is None:
            
            controlador_eventos.manejar_eventos(evento, estado_del_juego)
        else:
            
            if pantalla_resultado.manejar_evento(evento):
                estado_del_juego = resetear_juego()
                pantalla_resultado = None
                puntaje = Puntaje() 

    if pantalla_resultado is None:
        # Actualizar el estado del juego
        actualizar.actualizar_estado(estado_del_juego)
        tiempo_restante = max(0, 60 - int(time.time() - estado_del_juego['tiempo_inicial']))
        if estado_del_juego['nivel'] < 4 and tiempo_restante > 0:
            dibujar.dibujar_elementos(ventana, estado_del_juego, puntaje)
        else:
            if pantalla_resultado is None:
                if tiempo_restante > 0:
                    pantalla_resultado = Pantalla_resultado(
                        constantes.ANCHO_VENTANA,
                        constantes.ALTO_VETANA,
                        ganar=True,
                        puntaje=estado_del_juego['puntaje']
                    )
                else:
                    pantalla_resultado = Pantalla_resultado(
                        constantes.ANCHO_VENTANA,
                        constantes.ALTO_VETANA,
                        ganar=False,
                        puntaje=estado_del_juego['puntaje']
                    )
    else:
        pantalla_resultado.dibujar(ventana)

    pygame.display.update()

pygame.quit()
