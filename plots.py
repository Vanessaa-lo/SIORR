import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def graficar_nodos(nodos):
    plt.figure()

    for indice, (x, y) in nodos.items():
        plt.scatter(x, y)
        plt.text(x + 1, y + 1, str(indice))

    plt.title("Nodos generados")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.grid(True)
    plt.show()


def graficar_ruta(nodos, ruta):
    """
    Anima el recorrido continuo de la ruta.
    """
    figura, eje = plt.subplots()

    for indice, (x, y) in nodos.items():
        eje.scatter(x, y)
        eje.text(x + 1, y + 1, str(indice))

    ruta_completa = ruta + [ruta[0]]

    puntos_x = []
    puntos_y = []

    for i in range(len(ruta_completa) - 1):
        nodo_inicio = nodos[ruta_completa[i]]
        nodo_fin = nodos[ruta_completa[i + 1]]

        x_intermedios = np.linspace(nodo_inicio[0], nodo_fin[0], 30)
        y_intermedios = np.linspace(nodo_inicio[1], nodo_fin[1], 30)

        puntos_x.extend(x_intermedios)
        puntos_y.extend(y_intermedios)

    linea, = eje.plot([], [], linewidth=2)
    vehiculo, = eje.plot([], [], marker='o', markersize=8)

    eje.set_title("Recorrido de la ruta")
    eje.set_xlabel("Coordenada X")
    eje.set_ylabel("Coordenada Y")
    eje.grid(True)

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
        interval=50,
        repeat=False
    )

    plt.show()