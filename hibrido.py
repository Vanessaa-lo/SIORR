from genetico import ejecutar_genetico
from tabu import ejecutar_tabu
from tsp import calcular_distancia_total


def ejecutar_hibrido(
    matriz_distancias,
    cantidad_nodos,
    generar_ruta_aleatoria
):
    """
    Algoritmo híbrido memético.
    """
    mejor_ruta, historial_genetico = ejecutar_genetico(
        matriz_distancias,
        cantidad_nodos,
        generar_ruta_aleatoria
    )

    mejor_distancia = calcular_distancia_total(
        mejor_ruta,
        matriz_distancias
    )

    historial_completo = historial_genetico[:]

    for _ in range(5):
        refinada, historial_tabu = ejecutar_tabu(
            mejor_ruta,
            matriz_distancias,
            iteraciones=80,
            tamaño_lista_tabu=10
        )

        distancia_refinada = calcular_distancia_total(
            refinada,
            matriz_distancias
        )

        if distancia_refinada < mejor_distancia:
            mejor_ruta = refinada
            mejor_distancia = distancia_refinada

        historial_completo.extend(historial_tabu)

    return mejor_ruta, historial_completo