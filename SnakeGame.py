import sys
import pygame
pygame.init()

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


def dibujar_reticula(window):
    window.fill(Verde)
    x = 0
    y = 0
    for x in range(0, Ancho, Tamaño_cuadro):      
        pygame.draw.line(window, Negro, (x, 0), (x, Alto))
    
    for y in range(0, Alto, Tamaño_cuadro):
        pygame.draw.line(window, Negro, (0, y), (Ancho, y))

#
def main ():
    global Serpiente_x, Velocidad_x
    global Serpiente_y, Velocidad_y    
    
    pygame.init()
    window = pygame.display.set_mode((Ancho,Alto)) 
    pygame.display.set_caption("Juego de la Serpiente")  
    
    #
    clock = pygame.time.Clock()
    
    while True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
             
            #
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
         
        #   
        Serpiente_x += Velocidad_x
        Serpiente_y += Velocidad_y
                    
        dibujar_reticula(window)   
        
        pygame.draw.rect(window, Rojo, (Serpiente_x, Serpiente_y, Tamaño_cuadro, Tamaño_cuadro)) 
        
        pygame.display.update()    
        
        #
        clock.tick(10)                        
main()

