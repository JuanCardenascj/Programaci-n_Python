"""Instrucción:

Importa el módulo random
Crea una variable numero_aleatorio que contenga un número aleatorio entre 1 y 10
Muestra el número

Explicación:
import random → Trae el módulo para números aleatorios
random.randint(1, 10) → Genera un número entero entre 1 y 10
"""

import random

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)