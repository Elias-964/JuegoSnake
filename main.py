import sys
import pygame
from funciones import (
    dibujar_reticula,
    dibujar_serpiente,
    generar_comida,
    dibujar_comida,
    mostrar_texto,
)

pygame.init()

Alto = 720
Ancho = 1280

Negro = (0, 0, 0)
Rojo = (255, 0, 122)
Verde = (0, 225, 127)
Azul = (0, 191, 255)

Tamaño_cuadro = 20


def main():

    window = pygame.display.set_mode((Ancho, Alto))
    pygame.display.set_caption("Juego de la Serpiente")

    clock = pygame.time.Clock()

    estado = "menu"
    puntaje = 0

    while True:

        if estado == "menu":

            Serpiente_x = 620
            Serpiente_y = 320
            Velocidad_x = 0
            Velocidad_y = 0

            lista_serpiente = []
            longitud_serpiente = 1

            comida_x, comida_y = generar_comida(Ancho, Alto, Tamaño_cuadro)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if estado == "menu":
                    if event.key == pygame.K_RETURN:
                        estado = "jugando"

                elif estado == "gameover":
                    if event.key == pygame.K_RETURN:
                        estado = "menu"
                        puntaje = 0

                elif estado == "jugando":

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

        if estado == "menu":

            window.fill(Verde)
            mostrar_texto(window, "JUEGO DE LA SERPIENTE", 60, Rojo, 400, 200)
            mostrar_texto(window, "Presiona ENTER para jugar", 40, Negro, 420, 300)

        elif estado == "jugando":

            Serpiente_x += Velocidad_x
            Serpiente_y += Velocidad_y

            # Colisión con bordes
            if (
                Serpiente_x < 0
                or Serpiente_x >= Ancho
                or Serpiente_y < 0
                or Serpiente_y >= Alto
            ):
                estado = "gameover"

            cabeza = [Serpiente_x, Serpiente_y]
            lista_serpiente.append(cabeza)

            if len(lista_serpiente) > longitud_serpiente:
                del lista_serpiente[0]

            # Colisión con su propio cuerpo
            for segmento in lista_serpiente[:-1]:
                if segmento == cabeza:
                    estado = "gameover"

            # Comer comida
            if Serpiente_x == comida_x and Serpiente_y == comida_y:
                comida_x, comida_y = generar_comida(Ancho, Alto, Tamaño_cuadro)
                longitud_serpiente += 1
                puntaje += 1

            dibujar_reticula(window, Ancho, Alto, Tamaño_cuadro, Negro, Verde)
            dibujar_comida(window, comida_x, comida_y, Tamaño_cuadro, Azul)
            dibujar_serpiente(window, lista_serpiente, Tamaño_cuadro, Rojo)

            mostrar_texto(window, f"Puntaje: {puntaje}", 30, Negro, 20, 20)

        elif estado == "gameover":

            window.fill(Verde)
            mostrar_texto(window, "GAME OVER", 70, Rojo, 500, 250)
            mostrar_texto(window, f"Puntaje final: {puntaje}", 40, Negro, 520, 350)
            mostrar_texto(window, "Presiona ENTER para volver al menu", 35, Negro, 400, 450)

        pygame.display.update()
        clock.tick(10)


main()
