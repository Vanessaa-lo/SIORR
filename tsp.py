import random
import math


def generar_nodos(cantidad_nodos, limite_x=100, limite_y=100):
    """
    Genera nodos aleatorios con coordenadas dentro de un área definida.
    """
    nodos = {}

    for i in range(cantidad_nodos):
        x = random.randint(0, limite_x)
        y = random.randint(0, limite_y)
        nodos[i] = (x, y)

    return nodos


def calcular_distancia(nodo_a, nodo_b):
    """
    Calcula la distancia euclidiana entre dos nodos.
    """
    x1, y1 = nodo_a
    x2, y2 = nodo_b

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def calcular_distancia_total(ruta, nodos):
    """
    Calcula la distancia total de una ruta cerrada.
    """
    distancia_total = 0

    for i in range(len(ruta) - 1):
        nodo_actual = nodos[ruta[i]]
        nodo_siguiente = nodos[ruta[i + 1]]

        distancia_total += calcular_distancia(nodo_actual, nodo_siguiente)

    nodo_final = nodos[ruta[-1]]
    nodo_inicial = nodos[ruta[0]]

    distancia_total += calcular_distancia(nodo_final, nodo_inicial)

    return distancia_total


def generar_ruta_aleatoria(cantidad_nodos):
    """
    Genera una ruta aleatoria iniciando desde el nodo 0.
    """
    ruta = list(range(1, cantidad_nodos))
    random.shuffle(ruta)

    return [0] + ruta