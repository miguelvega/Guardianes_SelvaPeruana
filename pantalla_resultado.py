import pygame

class Pantalla_resultado:
    def __init__(self, ancho, alto, ganar=False, puntaje=0):
        self.ancho = ancho
        self.alto = alto
        self.fondo = pygame.font.SysFont(None, 35)
        
        # Mensaje de Ganar o Perder
        if ganar:
            self.texto = self.fondo.render(f"¡GANASTE! Puntaje: {puntaje}", True, (0, 255, 0))
            self.nombre_texto = self.fondo.render(
                "¡Felicitaciones! Lograste salvar a la selva y apagar todos los incendios.",
                True, (255, 255, 255)
            )
        else:
            self.texto = self.fondo.render(f"¡PERDISTE! Puntaje: {puntaje}", True, (255, 0, 0))
            self.nombre_texto = self.fondo.render(
                "¡Fallaste! No lograste salvar a la selva ni apagar todos los incendios.",
                True, (255, 255, 255)
            )
        
        # Posicionamiento de los textos
        self.texto_rect = self.texto.get_rect(center=(ancho // 2, alto // 3))
        self.nombre_texto_rect = self.nombre_texto.get_rect(center=(ancho // 2, (alto // 3) + 40))
        
        # Propiedades del botón "Volver a jugar"
        self.boton_color = (0, 128, 0)           # Verde
        self.boton_hover_color = (0, 200, 0)     # Verde claro al pasar el mouse
        self.boton_rect = pygame.Rect(ancho//2 - 100, alto//2, 200, 50)  # Posición y tamaño del botón
        self.boton_text = self.fondo.render("Volver a jugar", True, (255, 255, 255))
        self.boton_text_rect = self.boton_text.get_rect(center=self.boton_rect.center)

    def dibujar(self, ventana):
        # Dibujar textos de resultado
        ventana.blit(self.texto, self.texto_rect)
        ventana.blit(self.nombre_texto, self.nombre_texto_rect)
        
        # Obtener posición del mouse
        mouse_pos = pygame.mouse.get_pos()
        
        # Cambiar color del botón si el mouse está sobre él
        if self.boton_rect.collidepoint(mouse_pos):
            color = self.boton_hover_color
        else:
            color = self.boton_color
            
        # Dibujar botón
        pygame.draw.rect(ventana, color, self.boton_rect)
        ventana.blit(self.boton_text, self.boton_text_rect)
    
    def manejar_evento(self, evento):
        """
        Maneja los eventos relacionados con el botón.
        Retorna True si el botón fue presionado, de lo contrario False.
        """
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.boton_rect.collidepoint(evento.pos):
                return True
        return False
