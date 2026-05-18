import random
from tsp import calcular_distancia_total


def generar_vecino(ruta):
    """
    Genera vecino usando 2-opt.
    """
    vecino = ruta[:]

    i = random.randint(1, len(ruta) - 2)
    j = random.randint(i + 1, len(ruta) - 1)

    vecino[i:j+1] = reversed(vecino[i:j+1])

    movimiento = (i, j)

    return vecino, movimiento


def ejecutar_tabu(
    ruta_inicial,
    nodos,
    iteraciones=300,
    tamaño_lista_tabu=20
):
    """
    Ejecuta búsqueda tabú.
    """
    mejor_ruta = ruta_inicial[:]
    mejor_distancia = calcular_distancia_total(mejor_ruta, nodos)

    ruta_actual = ruta_inicial[:]
    lista_tabu = []
    historial = []

    for _ in range(iteraciones):
        mejor_vecino = None
        mejor_movimiento = None
        mejor_distancia_vecino = float("inf")
       
        for _ in range(100):
            vecino, movimiento = generar_vecino(ruta_actual)

            distancia = calcular_distancia_total(vecino, nodos)

            if movimiento in lista_tabu and distancia >= mejor_distancia:
                continue

            if distancia < mejor_distancia_vecino:
                mejor_vecino = vecino
                mejor_movimiento = movimiento
                mejor_distancia_vecino = distancia
                mejor_vecino = vecino
                mejor_movimiento = movimiento
                mejor_distancia_vecino = distancia

        if mejor_vecino is None:
            continue

        ruta_actual = mejor_vecino

        lista_tabu.append(mejor_movimiento)

        if len(lista_tabu) > tamaño_lista_tabu:
            lista_tabu.pop(0)

        if mejor_distancia_vecino < mejor_distancia:
            mejor_ruta = mejor_vecino[:]
            mejor_distancia = mejor_distancia_vecino

        historial.append(mejor_distancia)

    return mejor_ruta, historial