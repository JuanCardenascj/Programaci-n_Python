"""Instrucción:

Crea una lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Usa un bucle for para encontrar el primer número mayor a 5
Usa break para detener el bucle cuando lo encuentres
Muestra el número encontrado

Explicación:
break → Detiene el bucle inmediatamente
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero > 5:
        print(f"El primer número mayor a 5 es: {numero}")
        break