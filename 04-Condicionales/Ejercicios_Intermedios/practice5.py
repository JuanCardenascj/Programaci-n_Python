"""Instrucción:

Pide tres números
Encuentra el mayor
Muestra el resultado

Explicación:
Compara a con b y c
"""
a = int(input("Primer número: "))
b = int(input("Segundo número: "))
c = int(input("Tercer número: "))

if a >= b and a >= c:
    mayor = a
elif b >= a and b >= c:
    mayor = b
else:
    mayor = c

print(f"El mayor es: {mayor}")