"""
Elimina los números pares de:

numeros = [1,2,3,4,5,6,7,8,9,10]

y crea una nueva lista con solo los impares.
"""

#Eliminando los números pares

numeros = [1,2,3,4,5,6,7,8,9,10]

impares = []

for numero in numeros:
    if numero % 2 != 0:
        impares.append(numero)

print(impares)