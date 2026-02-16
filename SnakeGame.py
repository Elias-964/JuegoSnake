import sys
import pygame
pygame.init()

# Declaración de variables
Alto = 720
Ancho = 1280
Negro = (0, 0, 0)
Rojo = (255, 0, 122)
Azul = (0, 191, 255)
Naranja = (255, 140, 0)
Verde = (0, 225,127)
Tamaño_cuadro = 20

Serpiente_x = 100
Serpiente_y = 100

Velocidad_x = 0
Velocidad_y = 0

# En este parte se dibuja la ventana gráfica con las dimenciones establecidas en las variables "Alto y Ancho"
def dibujar_reticula(window):
    window.fill(Verde)
    x = 0
    y = 0
    for x in range(0, Ancho, Tamaño_cuadro):      
        pygame.draw.line(window, Negro, (x, 0), (x, Alto))
    
    for y in range(0, Alto, Tamaño_cuadro):
        pygame.draw.line(window, Negro, (0, y), (Ancho, y))

# Aqui estoy estableciendo la función "main" lo que indica que todo loq ue está identado de aquí en adelante solo se ejecutará al llamer esta función
def main ():
    
    #En este apartado hago uso de la declaración "global" para que se modifiquen variables que están fuera de la identación
    global Serpiente_x, Velocidad_x
    global Serpiente_y, Velocidad_y    
    
    pygame.init()
    window = pygame.display.set_mode((Ancho,Alto)) 
    pygame.display.set_caption("Juego de la Serpiente")  
    
    #En esta parte se establece un reloj que va a controlar el movimeinto de la serpiente
    clock = pygame.time.Clock()
    
    #Aquí se usa la vvariable "while" para crear un blucle, y se establecen las teclas a usar para controlar a la serpeinte.
    #En este caso las teclas a usar son W-A-S-D
    
    while True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
             
            #Cabe señalar que al ejecutar el código va a aparecer la ventana gráfica y la cabeza de la serpiente.
            #La cabeza de la serpiente no se moverá hasta presionar una de las teclas designadas a continuación...
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    Velocidad_x = 0
                    Velocidad_y = -Tamaño_cuadro
                    
                if event.key == pygame.K_s:
                    Velocidad_x = 0
                    Velocidad_y = Tamaño_cuadro
                    
                if event.key == pygame.K_a:
                    Velocidad_x = -Tamaño_cuadro
                    Velocidad_y = 0
            
                if event.key == pygame.K_d:
                    Velocidad_x = Tamaño_cuadro
                    Velocidad_y = 0
         
        #En esta parte se dibuja el rectángulo que va a simbolizar la cabeza de la serpiente
        Serpiente_x += Velocidad_x
        Serpiente_y += Velocidad_y
                    
        dibujar_reticula(window)   
        
        pygame.draw.rect(window, Rojo, (Serpiente_x, Serpiente_y, Tamaño_cuadro, Tamaño_cuadro)) 
        
        pygame.display.update()    
        
        #Esto indica que el juego se actualizará 10 veces por cada segundo
        #Este valor puede modificarse para que el movimiento sea mas rápido o mas lento
        clock.tick(10)                        
main()

