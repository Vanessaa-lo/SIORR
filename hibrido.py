from genetico import ejecutar_genetico
from tabu import ejecutar_tabu
from tsp import calcular_distancia_total


def ejecutar_hibrido(
    nodos,
    cantidad_nodos,
    generar_ruta_aleatoria,
    intentos=5
):
    """
    Ejecuta enfoque híbrido multiarranque:
    algoritmo genético + búsqueda tabú.
    """
    mejor_ruta_global = None
    mejor_distancia_global = float("inf")
    mejor_historial = []

    for _ in range(intentos):
        ruta_genetico, historial_genetico = ejecutar_genetico(
            nodos,
            cantidad_nodos,
            generar_ruta_aleatoria
        )

        ruta_refinada, historial_tabu = ejecutar_tabu(
            ruta_genetico,
            nodos,
            iteraciones=120,
            tamaño_lista_tabu=15
        )

        distancia = calcular_distancia_total(ruta_refinada, nodos)

        if distancia < mejor_distancia_global:
            mejor_distancia_global = distancia
            mejor_ruta_global = ruta_refinada
            mejor_historial = historial_genetico + historial_tabu

    return mejor_ruta_global, mejor_historial