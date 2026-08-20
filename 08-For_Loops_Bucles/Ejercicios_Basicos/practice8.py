"""Instrucción:

Crea una lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Usa un bucle for y if para mostrar solo los números pares
Muestra cada número par

Explicación:
if numero % 2 == 0: → Verifica si es par
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for numero in numeros:
    if numero % 2 == 0:
        print(numero)