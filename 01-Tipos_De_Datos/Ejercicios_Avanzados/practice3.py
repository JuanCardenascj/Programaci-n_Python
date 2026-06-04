"""
Dada:

numeros = [12, 7, 18, 5, 20, 3, 14]

Crea dos listas nuevas:

una con los pares
otra con los impares
"""

#Creando las dos listas nuevas
numeros = [12, 7, 18, 5, 20, 3, 14]

pares1 = []
impares1 = []

for numero in numeros:
    if numero % 2 == 0:
        pares1.append(numero)
    else: 
        impares1.append(numero)

print("Pares:", pares1)
print("Impares:", impares1)