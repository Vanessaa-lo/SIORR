import random
import math


def generar_nodos(cantidad_nodos, limite_x=100, limite_y=100):
    """
    Genera nodos aleatorios.
    """
    nodos = {}

    for i in range(cantidad_nodos):
        x = random.randint(0, limite_x)
        y = random.randint(0, limite_y)
        nodos[i] = (x, y)

    return nodos


def calcular_distancia(nodo_a, nodo_b):
    """
    Distancia euclidiana entre dos nodos.
    """
    x1, y1 = nodo_a
    x2, y2 = nodo_b

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def generar_matriz_distancias(nodos):
    """
    Genera matriz de distancias precalculadas.
    """
    cantidad = len(nodos)

    matriz = [[0 for _ in range(cantidad)] for _ in range(cantidad)]

    for i in range(cantidad):
        for j in range(cantidad):
            if i != j:
                matriz[i][j] = calcular_distancia(
                    nodos[i],
                    nodos[j]
                )

    return matriz


def calcular_distancia_total(ruta, matriz_distancias):
    """
    Calcula distancia total usando matriz precalculada.
    """
    distancia_total = 0

    for i in range(len(ruta) - 1):
        distancia_total += matriz_distancias[
            ruta[i]
        ][
            ruta[i + 1]
        ]

    distancia_total += matriz_distancias[
        ruta[-1]
    ][
        ruta[0]
    ]

    return distancia_total


def generar_ruta_aleatoria(cantidad_nodos):
    """
    Genera ruta iniciando desde nodo 0.
    """
    ruta = list(range(1, cantidad_nodos))
    random.shuffle(ruta)

    return [0] + ruta