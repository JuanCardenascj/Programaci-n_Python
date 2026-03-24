"""
Ejercicio 2: Número positivo o negativo
Escribe un programa que:

Pida un número

Diga si es positivo, negativo o cero
"""

datos = int(input("Escriba un numero positivo o negativo.. "))

if datos > 0:
    print("El número es positivo")
elif datos < 0:
    print("El número es negativo")
else: 
    print("El número es cero")