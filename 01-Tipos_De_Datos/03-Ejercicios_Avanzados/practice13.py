"""Instrucción:

Crea una lista anidada matriz = [[1, 2], [3, 4], [5, 6]]
Usa un bucle anidado para mostrar todos los elementos
"""

matriz = [[1, 2], [3, 4], [5, 6]]

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()