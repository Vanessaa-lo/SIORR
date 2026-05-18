from tsp import generar_nodos, calcular_distancia_total, generar_ruta_aleatoria
from genetico import ejecutar_genetico
from tabu import ejecutar_tabu
from hibrido import ejecutar_hibrido
from plots import graficar_ruta


cantidad_nodos = 50

nodos = generar_nodos(cantidad_nodos)
ruta_inicial = generar_ruta_aleatoria(cantidad_nodos)

print("Ruta inicial:", ruta_inicial)
print("Distancia inicial:", calcular_distancia_total(ruta_inicial, nodos))


# ALGORITMO GENÉTICO
ruta_genetico, historial_genetico = ejecutar_genetico(
    nodos,
    cantidad_nodos,
    generar_ruta_aleatoria
)

distancia_genetico = calcular_distancia_total(ruta_genetico, nodos)


# BÚSQUEDA TABÚ
ruta_tabu, historial_tabu = ejecutar_tabu(
    ruta_inicial,
    nodos
)

distancia_tabu = calcular_distancia_total(ruta_tabu, nodos)


# HÍBRIDO
ruta_hibrida, historial_hibrido = ejecutar_hibrido(
    nodos,
    cantidad_nodos,
    generar_ruta_aleatoria
)

distancia_hibrida = calcular_distancia_total(ruta_hibrida, nodos)


print("\nRESULTADOS")
print("--------------------------")
print("Genético:", distancia_genetico)
print("Tabú:", distancia_tabu)
print("Híbrido:", distancia_hibrida)


graficar_ruta(nodos, ruta_hibrida)