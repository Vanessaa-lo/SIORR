# SIORR
# SIORR - Sistema Inteligente de Optimización de Rutas y Recursos

## Descripción
SIORR (Sistema Inteligente de Optimización de Rutas y Recursos) es un proyecto desarrollado en Python enfocado en la optimización de rutas mediante algoritmos metaheurísticos aplicados al Problema del Viajante (Travelling Salesman Problem, TSP).

El sistema implementa y compara tres enfoques de optimización:

- Algoritmo Genético
- Búsqueda Tabú
- Algoritmo Híbrido Memético

El objetivo es encontrar rutas eficientes minimizando la distancia total recorrida dentro de un escenario simulado de distribución.

---

## Objetivo
Diseñar e implementar un modelo de optimización basado en metaheurísticas híbridas que permita resolver problemas de ruteo inteligente, comparando desempeño mediante métricas cuantitativas como fitness, convergencia, robustez y tiempo de ejecución.

---

## Tecnologías utilizadas
- Python 3
- NumPy
- Matplotlib

---

## Estructura del proyecto
```bash
SIORR/
│
├── main.py          # Ejecución principal y experimentación
├── tsp.py           # Generación del problema y cálculo de distancias
├── genetico.py      # Algoritmo genético
├── tabu.py          # Búsqueda tabú
├── hibrido.py       # Algoritmo híbrido memético
├── plots.py         # Visualización de resultados
└── README.md
```

---

## Algoritmos implementados

### Algoritmo Genético
Implementa:

- población inicial aleatoria
- selección por torneo
- cruce ordenado (OX)
- mutación por inversión
- elitismo
- evaluación mediante fitness

Configuración:
- población: 80 individuos
- generaciones: 200
- mutación: 10%
- elitismo: 5 individuos

---

### Búsqueda Tabú
Implementa:

- generación de vecinos mediante 2-opt
- lista tabú
- criterio de aspiración
- límite de estancamiento

Configuración:
- iteraciones máximas: 300
- lista tabú: 20 movimientos
- vecinos evaluados por iteración: 80

---

### Algoritmo Híbrido Memético
Combina:

- exploración global mediante algoritmo genético
- refinamiento local mediante búsqueda tabú

Configuración:
- algoritmo genético base
- 5 refinamientos tabú
- 80 iteraciones por refinamiento
- lista tabú de 10 movimientos

---

## Métricas evaluadas
El sistema compara algoritmos utilizando:

- Fitness promedio (distancia total)
- Tiempo promedio de ejecución
- Desviación estándar
- Convergencia
- Robustez experimental

---

## Resultados experimentales
Resultados obtenidos tras 20 ejecuciones independientes:

| Algoritmo | Fitness promedio | Tiempo promedio | Desviación estándar |
|----------|-----------------|----------------|--------------------|
| Genético | 713.20 | 0.88 s | 46.34 |
| Tabú | 601.73 | 0.11 s | 26.44 |
| Híbrido Memético | **592.51** | 1.02 s | **23.89** |

### Conclusiones principales
- El algoritmo híbrido obtuvo la mejor calidad de solución.
- La búsqueda tabú presentó el menor tiempo de ejecución.
- El algoritmo híbrido mostró la mayor estabilidad experimental.

---

## Visualizaciones generadas
El sistema genera automáticamente:

- gráfica de convergencia
- comparación de fitness promedio
- boxplot de robustez
- comparación de tiempos
- animación de la mejor ruta encontrada

---

## Instalación
Clona el repositorio:

```bash
git clone https://github.com/Vanessaa-lo/SIORR.git
```

Entra al proyecto:

```bash
cd SIORR
```

Instala dependencias:

```bash
pip install numpy matplotlib
```

---

## Ejecución
Ejecuta:

```bash
python main.py
```

o en Windows:

```bash
py main.py
```

---

## Autor
Proyecto desarrollado por:

**Vanessa Loyola Merino**

Proyecto académico — Algoritmos Metaheurísticos