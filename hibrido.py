from genetico import ejecutar_genetico
from tabu import ejecutar_tabu
from tsp import calcular_distancia_total


# ============================================================
# ALGORITMO HÍBRIDO MEMÉTICO
# Combina algoritmo genético con búsqueda tabú
# ============================================================
def ejecutar_hibrido(
    matriz_distancias,
    cantidad_nodos,
    generar_ruta_aleatoria
):

    # --------------------------------------------------------
    # FASE 1: EXPLORACIÓN GLOBAL
    # Ejecuta algoritmo genético para encontrar una buena ruta
    # --------------------------------------------------------
    mejor_ruta, historial_genetico = ejecutar_genetico(
        matriz_distancias,
        cantidad_nodos,
        generar_ruta_aleatoria
    )

    mejor_distancia = calcular_distancia_total(
        mejor_ruta,
        matriz_distancias
    )

    # Guarda historial de convergencia
    historial_completo = historial_genetico[:]

    # --------------------------------------------------------
    # FASE 2: REFINAMIENTO LOCAL
    # Aplica búsqueda tabú varias veces sobre la mejor ruta
    # --------------------------------------------------------
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

        # Si la nueva ruta es mejor, se actualiza
        if distancia_refinada < mejor_distancia:
            mejor_ruta = refinada
            mejor_distancia = distancia_refinada

        # Agrega historial del refinamiento
        historial_completo.extend(historial_tabu)

    # ========================================================
    # MEJOR SOLUCIÓN FINAL
    # ========================================================
    return mejor_ruta, historial_completo