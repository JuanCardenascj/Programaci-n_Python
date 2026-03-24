"""
Ejercicio 9: Números pares
Escribe un programa que:

Muestre todos los números pares del 1 al 50
"""

dato = int(input("Escriba un número: "))

for i in range(1, 51):
    if i % 2 == 0:
        print(i)
