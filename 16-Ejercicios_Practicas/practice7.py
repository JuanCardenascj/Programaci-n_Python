"""
Ejercicio 7: Tabla de multiplicar
Escribe un programa que:

Pida un número

Muestre su tabla de multiplicar del 1 al 10
"""
dato = int(input("Escriba un número: "))

for i in range(1, 11):
    resultado = dato * i
    print(f"{dato} x {i} = {resultado}")