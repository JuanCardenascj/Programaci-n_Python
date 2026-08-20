"""Instrucción:

Crea una lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Usa un bucle for para mostrar solo los números impares
Usa continue para saltar los números pares

Explicación:
continue → Salta a la siguiente iteración
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero % 2 == 0:
        continue
    print(numero)