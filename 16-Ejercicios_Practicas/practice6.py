"""
Ejercicio 6: Suma de números
Escribe un programa que:

Pida un número N

Sume todos los números del 1 hasta N

Muestre el resultado
"""

N = int(input("Escriba un número: "))

suma = 0  # Acumulador empieza en cero

for i in range(1, N + 1):  # i = 1, 2, 3, ..., N
    suma = suma + i         # Suma cada número

print(f"La suma de 1 hasta {N} es: {suma}")