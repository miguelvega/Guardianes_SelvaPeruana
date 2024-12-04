import constantes

# Lista de obstáculos iniciales
obstaculos = [2, 0]  # Incluye 0 (fuego) como obstáculo

class Mundo():
    def __init__(self):
        self.mapa_de_azulejos = []  # Almacena datos de cada azulejo
        self.azulejos_obstaculos = []  # Lista de azulejos considerados obstáculos
        self.azulejo_salida = None  # Azulejo de salida, si existe

    def procesar_datos(self, datos, lista_de_azulejos):
        # Procesa los datos del nivel y los convierte en azulejos gráficos.
        for y, fila in enumerate(datos):
            for x, azulejo in enumerate(fila):
                imagen = lista_de_azulejos[azulejo]
                imagen_rect = imagen.get_rect()
                imagen_x = x * constantes.TALLA_AZULEJO + constantes.TALLA_AZULEJO / 2
                imagen_y = y * constantes.TALLA_AZULEJO + constantes.TALLA_AZULEJO / 2
                imagen_rect.center = (imagen_x, imagen_y)
                dato_de_azulejo = [imagen, imagen_rect, imagen_x, imagen_y]
                
                # Agregar azulejos iniciales a obstáculos
                if azulejo in obstaculos:
                    self.azulejos_obstaculos.append(dato_de_azulejo)
                
                self.mapa_de_azulejos.append(dato_de_azulejo)
                
                # Si el azulejo es de salida
                if azulejo == 4:
                    self.azulejo_salida = dato_de_azulejo

    def actualizar_obstaculos(self, dato_de_azulejo, nuevo_azulejo, lista_de_azulejos, estado_de_juego):
        # Actualiza un azulejo específico en el mapa y cambia su estado de obstáculo.
        if nuevo_azulejo == 1:  # Si cambia a azulejo_1.png, deja de ser obstáculo
            if dato_de_azulejo in self.azulejos_obstaculos:
                self.azulejos_obstaculos.remove(dato_de_azulejo)
                estado_de_juego['puntaje'] += 1 
        elif nuevo_azulejo in obstaculos:  # Si el nuevo azulejo es un obstáculo
            if dato_de_azulejo not in self.azulejos_obstaculos:
                self.azulejos_obstaculos.append(dato_de_azulejo)
        
        # Cambiar la imagen del azulejo en el mapa
        dato_de_azulejo[0] = lista_de_azulejos[nuevo_azulejo]

    def dibujar(self, ventana):
        # Dibuja los azulejos en la superficie proporcionada.
        for azulejo in self.mapa_de_azulejos:
            ventana.blit(azulejo[0], azulejo[1])