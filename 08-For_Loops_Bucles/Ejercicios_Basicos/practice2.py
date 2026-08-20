"""Instrucción:

Crea una lista numeros = [1, 2, 3, 4, 5]
Usa un bucle for para sumar todos los números
Muestra la suma total

Explicación:
total = 0 → Inicializa el acumulador
total += numero → Suma cada número al acumulador
"""

numeros = [1, 2, 3, 4, 5]
total = 0

for numero in numeros:
    total += numero

print(f"La suma es:  {total}")