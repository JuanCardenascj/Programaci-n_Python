"""Instrucción:

Usa comprensión de listas para crear una lista con los cuadrados de los números del 1 al 10
"""

#Forma larga (sin compresión)
cuadrados = []
for x in range(1, 11):
    cuadrados.append(x ** 2)
print(cuadrados)

#Forma corta (Con comprensión)
cuadrados = [x ** 2 for x in range(1, 11)]
print(cuadrados)