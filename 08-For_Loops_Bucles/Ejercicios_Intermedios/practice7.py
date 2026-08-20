"""Instrucción:

Pide un número al usuario
Usa un bucle for del 1 al 10 para mostrar la tabla de multiplicar
Muestra cada resultado

Explicación:
numero * i → Calcula el producto
"""

numeros = int(input("Digite un número: "))

for numero in range(1, 11):
    print(f"{numeros} x {numero} = {numeros * numero}")