#Importar la libreria de Pygame en el archivo
import pygame

#Activar y empezar la libreria Pygame
#Iniciar el pygame 
pygame.init()

#Crear la ventana/display del objeto
#Darles las dimensiones de la ventana
ventana = pygame.display.set_mode((700,700))

#Darle nombre a la ventana que va mostrar
pygame.display.set_caption("Juego en Python")

#Coordenadas del tamano del objeto
 
x = 100
y = 100

#Dimensiones del objeto
altura = 50
ancho = 50

#velocidad de movimiento (entre mas sube, mas rapido)
velocidad = 10

#Indicacion si el juego esta corriendo
activo = True

#Lista para almacenar los disparos!
disparos =[]

#Bucle (loop) 
while activo:
    #Crear el tiempo de moviento
    pygame.time.delay(10)
    
    #Iterar sobre los eventos y objetos (nuestro personaje)
    for evento in pygame.event.get():
        #Si el evento es que se sale del juego, vamos a salir del juego por completo y el programa tambien
        if evento.type == pygame.QUIT:
            activo = False
    #Guardar botones
    botones = pygame.key.get_pressed()
    
    #Si oprime una flecha
    #Izquierda
    if botones[pygame.K_LEFT] and x>0:
        #Baja la coordenada X (va a la izquierda)
        x-=velocidad
    #Derecha
    if botones[pygame.K_RIGHT] and x <700-ancho:
        #Sube en la coordenada de X (va a la derecha)
        x+=velocidad
    #Arriba
    if botones[pygame.K_UP] and y>0:
        #Sube el objeto
        y-=velocidad
    #Abajo
    if botones[pygame.K_DOWN] and y<700-altura:
        #Baja el objeto
        y+=velocidad
    #Si preciona espacio, va disparar
    if botones[pygame.K_SPACE]:
        disparo = {'x':x+ancho/2,'y':y}
        disparos.append(disparo)
    #Actualizar posicion disparos mirando la lista de diccionarios
    for disparo in disparos:
        disparo['y'] -= velocidad *2 # Velocidad del disparo y que dispare arriba
        if disparo['y'] < 0:
            disparos.remove(disparo)
    #Completa el relleno del objeto
    ventana.fill((0,0,0))
    
    # Dibujar los disparos
    for disparo in disparos:
        pygame.draw.rect(ventana, (250, 0, 100), (disparo['x'], disparo['y'], 5, 5))
    #Dibujar el objeto en la ventana 
    pygame.draw.rect(ventana, (0,100,0), (x,y,ancho,altura))
    
    #Actualizar la ventana
    pygame.display.update()
    
#Cerrar la ventana
pygame.quit()
        
    
        
        
        