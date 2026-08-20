"""Instrucción:

Crea una lista anidada matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Usa un bucle for anidado para mostrar todos los elementos
Muestra la matriz en formato de tabla

Explicación:
for fila in matriz: → Itera sobre cada fila
for elemento in fila: → Itera sobre cada elemento de la fila
"""

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()