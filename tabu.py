from tsp import calcular_distancia_total
import random


# ============================================================
# GENERAR VECINO
# Crea una nueva solución usando movimiento 2-opt
# ============================================================
def generar_vecino(ruta):
    vecino = ruta[:]

    # Seleccionar dos posiciones aleatorias
    i = random.randint(1, len(ruta) - 2)
    j = random.randint(i + 1, len(ruta) - 1)

    # Invertir segmento de la ruta
    vecino[i:j+1] = reversed(vecino[i:j+1])

    movimiento = (i, j)

    return vecino, movimiento


# ============================================================
# BÚSQUEDA TABÚ
# Mejora una ruta explorando vecinos y evitando ciclos
# ============================================================
def ejecutar_tabu(
    ruta_inicial,
    matriz_distancias,
    iteraciones=300,
    tamaño_lista_tabu=20
):

    # Inicializar mejor solución
    mejor_ruta = ruta_inicial[:]
    mejor_distancia = calcular_distancia_total(
        mejor_ruta,
        matriz_distancias
    )

    ruta_actual = ruta_inicial[:]
    lista_tabu = []
    historial = []

    iteraciones_sin_mejora = 0
    limite_estancamiento = 120

    # --------------------------------------------------------
    # PROCESO PRINCIPAL
    # --------------------------------------------------------
    for _ in range(iteraciones):
        mejor_vecino = None
        mejor_movimiento = None
        mejor_distancia_vecino = float("inf")

        # Explorar vecinos
        for _ in range(80):
            vecino, movimiento = generar_vecino(ruta_actual)

            distancia = calcular_distancia_total(
                vecino,
                matriz_distancias
            )

            # Evitar movimientos tabú
            if movimiento in lista_tabu and distancia >= mejor_distancia:
                continue

            # Guardar mejor vecino encontrado
            if distancia < mejor_distancia_vecino:
                mejor_vecino = vecino
                mejor_movimiento = movimiento
                mejor_distancia_vecino = distancia

        if mejor_vecino is None:
            continue

        # Actualizar ruta actual
        ruta_actual = mejor_vecino
        lista_tabu.append(mejor_movimiento)

        # Mantener tamaño de lista tabú
        if len(lista_tabu) > tamaño_lista_tabu:
            lista_tabu.pop(0)

        # ----------------------------------------------------
        # ACTUALIZAR MEJOR SOLUCIÓN
        # ----------------------------------------------------
        if mejor_distancia_vecino < mejor_distancia:
            mejor_ruta = mejor_vecino[:]
            mejor_distancia = mejor_distancia_vecino
            iteraciones_sin_mejora = 0
        else:
            iteraciones_sin_mejora += 1

        historial.append(mejor_distancia)

        # Detener si no hay mejoras
        if iteraciones_sin_mejora >= limite_estancamiento:
            break

    # ========================================================
    # MEJOR SOLUCIÓN FINAL
    # ========================================================
    return mejor_ruta, historial