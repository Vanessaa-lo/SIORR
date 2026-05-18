import random
from tsp import calcular_distancia_total



def generar_poblacion(cantidad_poblacion, cantidad_nodos, generar_ruta_aleatoria):
    poblacion = []

    for _ in range(cantidad_poblacion):
        poblacion.append(generar_ruta_aleatoria(cantidad_nodos))

    return poblacion


def seleccionar_por_torneo(poblacion, matriz_distancias, tamaño_torneo=3):
    participantes = random.sample(poblacion, tamaño_torneo)

    return min(
        participantes,
        key=lambda ruta: calcular_distancia_total(ruta, matriz_distancias)
    )


def cruce_ordenado(padre1, padre2):
    genes_padre1 = padre1[1:]
    genes_padre2 = padre2[1:]

    tamaño = len(genes_padre1)

    inicio = random.randint(0, tamaño - 2)
    fin = random.randint(inicio + 1, tamaño)

    hijo_genes = [None] * tamaño

    hijo_genes[inicio:fin] = genes_padre1[inicio:fin]

    restantes = [
        nodo for nodo in genes_padre2
        if nodo not in hijo_genes
    ]

    indice = 0

    for nodo in restantes:
        while hijo_genes[indice] is not None:
            indice += 1
        hijo_genes[indice] = nodo

    return [0] + hijo_genes


def mutar(ruta, probabilidad_mutacion):
    if random.random() < probabilidad_mutacion:
        i = random.randint(1, len(ruta) - 2)
        j = random.randint(i + 1, len(ruta) - 1)

        ruta[i:j+1] = reversed(ruta[i:j+1])

    return ruta


def ejecutar_genetico(
    matriz_distancias,
    cantidad_nodos,
    generar_ruta_aleatoria,
    cantidad_poblacion=80,
    generaciones=200,
    probabilidad_mutacion=0.1
):
    poblacion = generar_poblacion(
        cantidad_poblacion,
        cantidad_nodos,
        generar_ruta_aleatoria
    )

    historial = []

    for generacion in range(generaciones):
        nueva_poblacion = []

        elite = sorted(
            poblacion,
            key=lambda ruta: calcular_distancia_total(
                ruta,
                matriz_distancias
            )
        )[:5]

        nueva_poblacion.extend(elite)

        for _ in range(cantidad_poblacion - 5):
            padre1 = seleccionar_por_torneo(
                poblacion,
                matriz_distancias
            )

            padre2 = seleccionar_por_torneo(
                poblacion,
                matriz_distancias
            )

            hijo = cruce_ordenado(padre1, padre2)
            hijo = mutar(hijo, probabilidad_mutacion)

            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

        mejor_distancia = min(
            calcular_distancia_total(
                ruta,
                matriz_distancias
            )
            for ruta in poblacion
        )

        historial.append(mejor_distancia)

    mejor_ruta = min(
        poblacion,
        key=lambda ruta: calcular_distancia_total(
            ruta,
            matriz_distancias
        )
    )

    return mejor_ruta, historial