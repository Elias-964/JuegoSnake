import pygame
import random


def dibujar_reticula(window, Ancho, Alto, Tamaño_cuadro, Negro, Verde):
    window.fill(Verde)

    for x in range(0, Ancho, Tamaño_cuadro):
        pygame.draw.line(window, Negro, (x, 0), (x, Alto))

    for y in range(0, Alto, Tamaño_cuadro):
        pygame.draw.line(window, Negro, (0, y), (Ancho, y))


def dibujar_serpiente(window, lista_serpiente, tamaño, color):
    for segmento in lista_serpiente:
        pygame.draw.rect(window, color, (segmento[0], segmento[1], tamaño, tamaño))


def generar_comida(Ancho, Alto, Tamaño_cuadro):
    comida_x = random.randrange(0, Ancho, Tamaño_cuadro)
    comida_y = random.randrange(0, Alto, Tamaño_cuadro)
    return comida_x, comida_y


def dibujar_comida(window, x, y, tamaño, color):
    pygame.draw.rect(window, color, (x, y, tamaño, tamaño))


def mostrar_texto(window, texto, tamaño, color, x, y):
    fuente = pygame.font.SysFont(None, tamaño)
    render = fuente.render(texto, True, color)
    window.blit(render, (x, y))
    