"""Instrucción:

Crea una lista numeros = [1, 2, 3, 4, 5]
Usa un bucle for para crear una nueva lista con el doble de cada número
Muestra la nueva lista

Explicación:
nueva_lista = [] → Inicializa la nueva lista
nueva_lista.append(numero * 2) → Agrega el doble
"""

numeros = [1, 2, 3, 4, 5]
doble = []

for numero in numeros:
    doble.append(numero * 2)

print(doble)