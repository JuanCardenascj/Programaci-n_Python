"""Instrucción:

Crea una variable numeros que use comprensión de listas para generar los cuadrados del 1 al 5
Muestra la lista

Explicación:
[x ** 2 for x in range(1, 6)] → Genera [1, 4, 9, 16, 25]
"""

numeros = [x ** 2 for x in range(1, 6)]
print(numeros)  # [1, 4, 9, 16, 25]