"""Segundo Reto.
   1. Pida 5 números
   2. Guarde los números en una lista
   3. Calcule el promedio"""

numeros = []

for i in range(5):
    numero = int(input("Digite un número: "))
    numeros.append(numero)

for n in numeros:
    suma = suma + n

promedio = suma / 5

print("El promedio es:", promedio)