"""Ejercicio 1: Par o impar
Escribe un programa que:

Pida un número

Diga si es par o impar"""

numero = int(input("Escriba un número... "))
if numero % 2 == 0:
    print("El numero es par")
elif numero:
    print("El número es impar")
