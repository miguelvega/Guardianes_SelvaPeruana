import pygame
import constantes

class Personaje():
    def __init__(self, x, y, animaciones):
        self.voltear = False   # False: el jugador no se voltea, True: se voltea
        self.animaciones = animaciones
        # Imagen de la animacion que se esta mostrando actualmente
        self.frame_indice = 0
        # Aqui se almacena la hora actual (en ms desde que se inicio 'pygame')
        self.actualizar_tiempo = pygame.time.get_ticks()
        self.imagen = animaciones[self.frame_indice]
        self.forma = self.imagen.get_rect()
        self.forma.center = (x,y)
    
    def actualizar(self):
        enfriar_animacion = 100
        self.imagen = self.animaciones[self.frame_indice]
        if pygame.time.get_ticks() - self.actualizar_tiempo >= enfriar_animacion:
            self.frame_indice = self.frame_indice + 1
            self.actualizar_tiempo = pygame.time.get_ticks()
        if self.frame_indice >= len(self.animaciones):
            self.frame_indice = 0    
    
    def movimiento(self, delta_x, delta_y, azulejos_obstaculos, azulejo_salida):
        # Gestionar el cambio de niveles
        nivel_completado = False
        # Para invertir la imagen
        if delta_x < 0:
            self.voltear = True
        if delta_x > 0:
            self.voltear = False  
        
        # Colisiones en el eje X      
        self.forma.x = self.forma.x + delta_x
        for obstaculo in azulejos_obstaculos:
            if obstaculo[1].colliderect(self.forma):
                if delta_x > 0:
                    self.forma.right = obstaculo[1].left
                if delta_x < 0:
                    self.forma.left = obstaculo[1].right  
        
        # Colisiones en el eje Y
        self.forma.y = self.forma.y + delta_y
        for obstaculo in azulejos_obstaculos:
            if obstaculo[1].colliderect(self.forma):
                if delta_y > 0:
                    self.forma.bottom = obstaculo[1].top
                if delta_y < 0:
                    self.forma.top = obstaculo[1].bottom
        
        if azulejo_salida[1].colliderect(self.forma):
            nivel_completado = True
        
        return nivel_completado                
    
    def dibujar(self, ventana):
        # Para invertir la imagen
        voltear_imagen = pygame.transform.flip(self.imagen, self.voltear, False)
        ventana.blit(voltear_imagen, self.forma)    