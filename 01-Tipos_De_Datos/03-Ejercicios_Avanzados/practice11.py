"""Instrucción:

Usa comprensión de diccionarios para crear un diccionario que tenga como claves los números del 1 al 5 y como valores sus cuadrados
"""

#Forma Larga (Sin compresión)
cuadrados_dict = {}
for x in range(1, 6):
    cuadrados_dict[x] = x ** 2
print(cuadrados_dict)

#Forma corta (con comprensión)
numeros = {x: x ** 2 for x in range(1, 6)}
print(numeros)