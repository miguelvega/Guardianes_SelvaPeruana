import pygame
from arma import Chorro_agua

class Puntaje:
    def __init__(self):
        self.fondo_puntaje = pygame.font.Font(None, 50)
        self.texto_puntaje = None

    def dibujar(self, ventana, puntaje):
        self.texto_puntaje = self.fondo_puntaje.render(f"Puntaje: {puntaje}", True, (139, 0, 0))
        ventana.blit(self.texto_puntaje, (680, 15))