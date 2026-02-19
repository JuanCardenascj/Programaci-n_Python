"""Crear un programa que encuentre el número MENOR de una lista"""

numeros = [98, 32, 432, 41, 87, 0, -2, -5, -980]

menor = numeros[0]

for numero in numeros[1:]: #Evita comparar el primer elemento dos veces!
    if numero < menor:
        menor = numero

print("El número menor es: ", menor)