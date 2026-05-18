import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


# ============================================================
# GRAFICAR NODOS
# Muestra la ubicación de los nodos generados
# ============================================================
def graficar_nodos(nodos):
    plt.figure()

    for indice, (x, y) in nodos.items():
        plt.scatter(x, y)
        plt.text(
            x + 1,
            y + 1,
            str(indice)
        )

    plt.title("Nodos generados")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.grid(True)

    plt.show()


# ============================================================
# GRAFICAR RUTA
# Anima el recorrido de la mejor ruta encontrada
# ============================================================
def graficar_ruta(nodos, ruta):
    figura, eje = plt.subplots()

    # Dibujar nodos
    for indice, (x, y) in nodos.items():
        eje.scatter(x, y)
        eje.text(
            x + 1,
            y + 1,
            str(indice)
        )

    ruta_completa = ruta + [ruta[0]]

    puntos_x = []
    puntos_y = []

    # Generar puntos intermedios para animación suave
    for i in range(len(ruta_completa) - 1):
        nodo_inicio = nodos[ruta_completa[i]]
        nodo_fin = nodos[ruta_completa[i + 1]]

        x_intermedios = np.linspace(
            nodo_inicio[0],
            nodo_fin[0],
            30
        )

        y_intermedios = np.linspace(
            nodo_inicio[1],
            nodo_fin[1],
            30
        )

        puntos_x.extend(x_intermedios)
        puntos_y.extend(y_intermedios)

    linea, = eje.plot([], [], linewidth=2)

    vehiculo, = eje.plot(
        [],
        [],
        marker='o',
        markersize=8
    )

    eje.set_title("Recorrido de la ruta")
    eje.set_xlabel("Coordenada X")
    eje.set_ylabel("Coordenada Y")
    eje.grid(True)

    # Actualizar animación
    def actualizar(frame):
        linea.set_data(
            puntos_x[:frame + 1],
            puntos_y[:frame + 1]
        )

        vehiculo.set_data(
            [puntos_x[frame]],
            [puntos_y[frame]]
        )

        return linea, vehiculo

    animacion = FuncAnimation(
        figura,
        actualizar,
        frames=len(puntos_x),
        interval=20,
        repeat=False
    )

    plt.draw()
    plt.show()


# ============================================================
# GRAFICAR CONVERGENCIA
# Compara evolución del fitness entre algoritmos
# ============================================================
def graficar_convergencia(
    historial_genetico,
    historial_tabu,
    historial_hibrido
):
    plt.figure()

    plt.plot(
        historial_genetico,
        label="Genético"
    )

    plt.plot(
        historial_tabu,
        label="Tabú"
    )

    plt.plot(
        historial_hibrido,
        label="Híbrido"
    )

    plt.title("Convergencia de algoritmos")
    plt.xlabel("Iteraciones")
    plt.ylabel("Fitness (distancia)")
    plt.legend()
    plt.grid(True)

    plt.show()


# ============================================================
# GRAFICAR COMPARACIÓN DE FITNESS
# Muestra promedio de resultados obtenidos
# ============================================================
def graficar_comparacion(
    promedio_genetico,
    promedio_tabu,
    promedio_hibrido
):
    algoritmos = [
        "Genético",
        "Tabú",
        "Híbrido"
    ]

    valores = [
        promedio_genetico,
        promedio_tabu,
        promedio_hibrido
    ]

    plt.figure()

    barras = plt.bar(
        algoritmos,
        valores
    )

    # Mostrar valores sobre barras
    for barra in barras:
        altura = barra.get_height()

        plt.text(
            barra.get_x() + barra.get_width() / 2,
            altura + 5,
            f"{altura:.2f}",
            ha="center"
        )

    plt.title("Comparación de fitness promedio")
    plt.ylabel("Distancia")
    plt.grid(True, axis="y")

    plt.show()


# ============================================================
# GRAFICAR BOXPLOT
# Muestra dispersión y robustez de resultados
# ============================================================
def graficar_boxplot(
    datos_genetico,
    datos_tabu,
    datos_hibrido
):
    plt.figure()

    plt.boxplot(
        [
            datos_genetico,
            datos_tabu,
            datos_hibrido
        ],
        labels=[
            "Genético",
            "Tabú",
            "Híbrido"
        ],
        showmeans=True
    )

    plt.title("Distribución de resultados")
    plt.ylabel("Distancia")
    plt.grid(True, axis="y")

    plt.show()


# ============================================================
# GRAFICAR TIEMPOS
# Compara tiempo promedio de ejecución
# ============================================================
def graficar_tiempos(
    tiempo_genetico,
    tiempo_tabu,
    tiempo_hibrido
):
    algoritmos = [
        "Genético",
        "Tabú",
        "Híbrido"
    ]

    tiempos = [
        tiempo_genetico,
        tiempo_tabu,
        tiempo_hibrido
    ]

    plt.figure()

    barras = plt.bar(
        algoritmos,
        tiempos
    )

    # Mostrar tiempos sobre barras
    for barra in barras:
        altura = barra.get_height()

        plt.text(
            barra.get_x() + barra.get_width() / 2,
            altura + 0.02,
            f"{altura:.2f}s",
            ha="center"
        )

    plt.title("Comparación de tiempos de ejecución")
    plt.ylabel("Tiempo (segundos)")
    plt.grid(True, axis="y")

    plt.show()