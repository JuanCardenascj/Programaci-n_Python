"""Instrucción:

Crea una lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Usa comprensión de listas para crear una lista solo con los números pares
"""
#Forma larga (Sin comprensión)
pares = []
for x in numeros:
    if x % 2 == 0:
        pares.append(x)
print(pares)

#Forma corta (Con compresión)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]
print(pares)