# Simulación de Partículas Cargadas en Campo Magnético

Este repositorio contiene el código desarrollado (execution.py) para simular el comportamiento de dos partículas cargadas moviéndose en un campo magnético constante bajo las siguientes condiciones:


Aceleración inicial nula.

Velocidad inicial no nula.

Las partículas inician acercándose.

Campo magnético no nulo.

## Estructura del proyecto

El proyecto se ha desarrollado en Python utilizando clases para representar las partículas y métodos para simular su dinámica. Se han empleado las ecuaciones de fuerza de Lorentz y fuerza de Coulomb para calcular la aceleración de cada partícula, así como también las ecuaciones del movimiento uniformemente acelerado para calcular su posición y velocidad en cada paso de tiempo.

## Resultados
Los resultados de la simulación se encuentran en la carpeta "GRÁFICAS", donde se incluyen las gráficas para cada coordenada espacial de la posición, velocidad y aceleración para cada partícula en función del tiempo, así como la trayectoria total de las dos partículas simuladas.

## Consideraciones particulares

Los valores de las cargas y masas utilizados en este proyecto son arbitrarios y no corresponden a valores reales. En un contexto real, las cargas y masas de las partículas involucradas en este tipo de simulaciones suelen ser extremadamente pequeñas, lo que podría generar problemas de precisión numérica, tales como la pérdida de significancia debido a la limitada capacidad de representación de números en punto flotante. Sin embargo, para los propósitos de esta simulación y con fines didácticos, se han elegido valores que permiten una ejecución eficiente del código sin enfrentar tales problemas.

## Contribuidores

Este proyecto fue desarrollado para el curso de física computacional I del Instituto de Física, Universidad de Antioquia, por el equipo conformado por:

Caterine Bedoya (@caterine.bedoyab)

Jhonatan Jurado (@JhonatanJ)