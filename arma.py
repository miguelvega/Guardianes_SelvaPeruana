import pygame
import constantes
import math

class Arma():
    def __init__(self, imagen_arma, imagen_bala, sonido_agua):
        self.imagen_bala = imagen_bala
        self.imagen_original = imagen_arma
        self.sonido_agua = sonido_agua
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.forma = self.imagen.get_rect()
        self.dispara = False
        self.ultimo_disparo = pygame.time.get_ticks()
    
    def actualizar(self, personaje):
        enfriamiento_disparo = constantes.ENFRIAR_BALAS
        bala = None
        self.forma.center = personaje.forma.center
        if personaje.voltear == False:
            self.forma.x += personaje.forma.width / 2
            self.rotar_arma(False)
        if personaje.voltear == True:
            self.forma.x -= personaje.forma.width / 2
            self.rotar_arma(True)
        
        # Detectar los clicks del mouse
        if pygame.mouse.get_pressed()[0] and not self.dispara and (pygame.time.get_ticks() - self.ultimo_disparo >= enfriamiento_disparo):  # 0: botón izq
            bala = Chorro_agua(self.imagen_bala, self.forma.centerx, self.forma.centery, self.angulo)
            self.sonido_agua['chorroDeAgua'].set_volume(0.5)
            self.dispara = True
        
        # Resetear el click del mouse
        if not pygame.mouse.get_pressed()[0]:
            self.sonido_agua['chorroDeAgua'].set_volume(0)
            self.dispara = False    
                
        # Mover la pistola con el mouse
        mouse_pos = pygame.mouse.get_pos()
        distancia_x = mouse_pos[0] - self.forma.centerx
        distancia_y = -(mouse_pos[1] - self.forma.centery)
        self.angulo = math.degrees(math.atan2(distancia_y, distancia_x))
        
        return bala       
    
    def rotar_arma(self, rotar):
        if rotar:
            voltear_imagen = pygame.transform.flip(self.imagen_original, True, False)
            self.imagen = pygame.transform.rotate(voltear_imagen, self.angulo)
        else:
            voltear_imagen = pygame.transform.flip(self.imagen_original, False, False)
            self.imagen = pygame.transform.rotate(voltear_imagen, self.angulo)
    
    def dibujar(self, ventana):
        self.imagen = pygame.transform.rotate(self.imagen, self.angulo)
        ventana.blit(self.imagen, self.forma)
    
class Chorro_agua(pygame.sprite.Sprite):
    def __init__(self, imagen_agua, x, y, angulo):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_original = imagen_agua
        self.angulo = angulo
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.rect = self.imagen.get_rect()
        self.rect.center = (x, y)   
        # Calculo de la velocidad
        self.delta_x = math.cos(math.radians(self.angulo)) * constantes.VELOCIDAD_BALA 
        self.delta_y = -math.sin(math.radians(self.angulo)) * constantes.VELOCIDAD_BALA         
    
    def actualizar(self, obstaculos_tiles, map_tiles, mundo, tile_list, game_state):
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y
        
        # Verificar la colisión con los tiles
        for tile_data in obstaculos_tiles:
            if tile_data[1].colliderect(self.rect):
                if tile_data[0] == tile_list[0]:  # Si es fuego (azulejo_0.png)
                    mundo.actualizar_obstaculos(tile_data, 1, tile_list, game_state)  # Cambia a azulejo_1.png
                self.kill()  # Elimina la bala después del impacto
                break
        
        # Verificar si la bala sale de la pantalla
        if (self.rect.right < 0 or self.rect.left > constantes.ANCHO_VENTANA or
                self.rect.bottom < 0 or self.rect.top > constantes.ALTO_VETANA):
            self.kill()
    
    def dibujar(self, ventana):
        ventana.blit(self.imagen, (self.rect.centerx, self.rect.centery - int(self.imagen.get_height())))
