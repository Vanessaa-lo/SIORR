import random
import math


# ============================================================
# GENERAR NODOS
# Crea ubicaciones aleatorias para el problema
# ============================================================
def generar_nodos(cantidad_nodos, limite_x=100, limite_y=100):

    nodos = {}

    for i in range(cantidad_nodos):
        x = random.randint(0, limite_x)
        y = random.randint(0, limite_y)

        nodos[i] = (x, y)

    return nodos


# ============================================================
# CALCULAR DISTANCIA
# Obtiene distancia euclidiana entre dos nodos
# ============================================================
def calcular_distancia(nodo_a, nodo_b):

    x1, y1 = nodo_a
    x2, y2 = nodo_b

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# ============================================================
# GENERAR MATRIZ DE DISTANCIAS
# Precalcula todas las distancias entre nodos
# ============================================================
def generar_matriz_distancias(nodos):

    cantidad = len(nodos)

    matriz = [
        [0 for _ in range(cantidad)]
        for _ in range(cantidad)
    ]

    for i in range(cantidad):
        for j in range(cantidad):

            if i != j:
                matriz[i][j] = calcular_distancia(
                    nodos[i],
                    nodos[j]
                )

    return matriz


# ============================================================
# CALCULAR DISTANCIA TOTAL
# Evalúa el fitness de una ruta completa
# ============================================================
def calcular_distancia_total(ruta, matriz_distancias):

    distancia_total = 0

    for i in range(len(ruta) - 1):
        distancia_total += matriz_distancias[
            ruta[i]
        ][
            ruta[i + 1]
        ]

    # Regreso al nodo inicial
    distancia_total += matriz_distancias[
        ruta[-1]
    ][
        ruta[0]
    ]

    return distancia_total


# ============================================================
# GENERAR RUTA ALEATORIA
# Crea una solución inicial válida para el TSP
# ============================================================
def generar_ruta_aleatoria(cantidad_nodos):

    ruta = list(range(1, cantidad_nodos))

    random.shuffle(ruta)

    return [0] + ruta