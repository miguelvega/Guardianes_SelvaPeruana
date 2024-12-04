import pygame

def manejar_eventos(evento, estado_de_juego):
    if evento.type == pygame.QUIT:
        estado_de_juego['ejecutar'] = False

    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_a:
            estado_de_juego['mover_izquierda'] = True
        if evento.key == pygame.K_d:
            estado_de_juego['mover_derecha'] = True
        if evento.key == pygame.K_w:
            estado_de_juego['mover_arriba'] = True
        if evento.key == pygame.K_s:
            estado_de_juego['mover_abajo'] = True

    if evento.type == pygame.KEYUP:
        if evento.key == pygame.K_a:
            estado_de_juego['mover_izquierda'] = False
        if evento.key == pygame.K_d:
            estado_de_juego['mover_derecha'] = False
        if evento.key == pygame.K_w:
            estado_de_juego['mover_arriba'] = False
        if evento.key == pygame.K_s:
            estado_de_juego['mover_abajo'] = False
