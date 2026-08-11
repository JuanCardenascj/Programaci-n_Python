"""Instrucción:

Pide tres lados de un triángulo
Usa condiciones para clasificar:
Todos iguales: Equilátero
Dos iguales: Isósceles
Todos diferentes: Escaleno
Muestra el tipo

Explicación:
Compara los tres lados
"""

a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

if a == b == c:
    print("Equilátero")
elif a == b or a == c or b == c:
    print("Isósceles")
else:
    print("Escaleno")