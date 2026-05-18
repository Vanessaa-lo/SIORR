import time
import numpy as np

from tsp import (
    generar_nodos,
    generar_ruta_aleatoria,
    calcular_distancia_total,
    generar_matriz_distancias
)

from genetico import ejecutar_genetico
from tabu import ejecutar_tabu
from hibrido import ejecutar_hibrido

from plots import (
    graficar_ruta,
    graficar_convergencia,
    graficar_comparacion,
    graficar_boxplot,
    graficar_tiempos
)

cantidad_nodos = 50
cantidad_corridas = 20

datos_genetico = []
datos_tabu = []
datos_hibrido = []

tiempos_genetico = []
tiempos_tabu = []
tiempos_hibrido = []

mejor_ruta_global = None
mejor_distancia_global = float("inf")
mejor_nodos = None

mejor_historial_genetico = []
mejor_historial_tabu = []
mejor_historial_hibrido = []

for corrida in range(cantidad_corridas):

    print(f"\nCORRIDA {corrida + 1} de {cantidad_corridas}")
    print("--------------------------")

    nodos = generar_nodos(cantidad_nodos)
    matriz_distancias = generar_matriz_distancias(nodos)

    ruta_inicial = generar_ruta_aleatoria(cantidad_nodos)

    distancia_inicial = calcular_distancia_total(
        ruta_inicial,
        matriz_distancias
    )

    print("Distancia inicial:", distancia_inicial)

    # GENÉTICO
    inicio = time.time()

    ruta_genetico, historial_genetico = ejecutar_genetico(
        matriz_distancias,
        cantidad_nodos,
        generar_ruta_aleatoria
    )

    fin = time.time()

    tiempo_genetico = fin - inicio
    tiempos_genetico.append(tiempo_genetico)

    distancia_genetico = calcular_distancia_total(
        ruta_genetico,
        matriz_distancias
    )

    # TABÚ
    inicio = time.time()

    ruta_tabu, historial_tabu = ejecutar_tabu(
        ruta_inicial,
        matriz_distancias
    )

    fin = time.time()

    tiempo_tabu = fin - inicio
    tiempos_tabu.append(tiempo_tabu)

    distancia_tabu = calcular_distancia_total(
        ruta_tabu,
        matriz_distancias
    )

    # HÍBRIDO
    inicio = time.time()

    ruta_hibrida, historial_hibrido = ejecutar_hibrido(
        matriz_distancias,
        cantidad_nodos,
        generar_ruta_aleatoria
    )

    fin = time.time()

    tiempo_hibrido = fin - inicio
    tiempos_hibrido.append(tiempo_hibrido)

    distancia_hibrida = calcular_distancia_total(
        ruta_hibrida,
        matriz_distancias
    )

    print("\nRESULTADOS")
    print("--------------------------")
    print("Genético:", distancia_genetico)
    print("Tabú:", distancia_tabu)
    print("Híbrido:", distancia_hibrida)

    print("\nTIEMPOS")
    print("--------------------------")
    print("Genético:", tiempo_genetico)
    print("Tabú:", tiempo_tabu)
    print("Híbrido:", tiempo_hibrido)

    datos_genetico.append(distancia_genetico)
    datos_tabu.append(distancia_tabu)
    datos_hibrido.append(distancia_hibrida)

    if distancia_hibrida < mejor_distancia_global:
        mejor_distancia_global = distancia_hibrida
        mejor_ruta_global = ruta_hibrida
        mejor_nodos = nodos

        mejor_historial_genetico = historial_genetico
        mejor_historial_tabu = historial_tabu
        mejor_historial_hibrido = historial_hibrido


# PROMEDIOS FITNESS
promedio_genetico = sum(datos_genetico) / len(datos_genetico)
promedio_tabu = sum(datos_tabu) / len(datos_tabu)
promedio_hibrido = sum(datos_hibrido) / len(datos_hibrido)

# PROMEDIOS TIEMPO
promedio_tiempo_genetico = sum(tiempos_genetico) / len(tiempos_genetico)
promedio_tiempo_tabu = sum(tiempos_tabu) / len(tiempos_tabu)
promedio_tiempo_hibrido = sum(tiempos_hibrido) / len(tiempos_hibrido)

# DESVIACIÓN ESTÁNDAR
desv_genetico = np.std(datos_genetico)
desv_tabu = np.std(datos_tabu)
desv_hibrido = np.std(datos_hibrido)

print("\nPROMEDIOS FITNESS")
print("--------------------------")
print("Genético:", promedio_genetico)
print("Tabú:", promedio_tabu)
print("Híbrido:", promedio_hibrido)

print("\nPROMEDIOS TIEMPO")
print("--------------------------")
print("Genético:", promedio_tiempo_genetico)
print("Tabú:", promedio_tiempo_tabu)
print("Híbrido:", promedio_tiempo_hibrido)

print("\nDESVIACIÓN ESTÁNDAR")
print("--------------------------")
print("Genético:", desv_genetico)
print("Tabú:", desv_tabu)
print("Híbrido:", desv_hibrido)

graficar_convergencia(
    mejor_historial_genetico,
    mejor_historial_tabu,
    mejor_historial_hibrido
)

graficar_comparacion(
    promedio_genetico,
    promedio_tabu,
    promedio_hibrido
)

graficar_boxplot(
    datos_genetico,
    datos_tabu,
    datos_hibrido
)

graficar_tiempos(
    promedio_tiempo_genetico,
    promedio_tiempo_tabu,
    promedio_tiempo_hibrido
)

graficar_ruta(
    mejor_nodos,
    mejor_ruta_global
)