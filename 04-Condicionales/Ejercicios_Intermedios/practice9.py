"""Instrucción:

Pide un número
Usa condiciones para verificar si es primo (solo divisible por 1 y por sí mismo)
Muestra el resultado

Explicación:
Un número es primo si no es divisible por ningún número entre 2 y su raíz cuadrada
"""

import math

numero = int(input("Número: "))

if numero <= 1:
    print("No es primo")
else:
    es_primo = True
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            es_primo = False
            break
    
    if es_primo:
        print("Es primo")
    else:
        print("No es primo")