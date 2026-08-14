"""Instrucción:

Pide dos números
Pide la operación (+, -, *, /)
Usa if para realizar la operación
Muestra el resultado

Explicación:
Múltiples condicionales para diferentes operaciones
"""
numero1 = int(input("Digite un número: "))
numero2 = int(input("Digite un número: "))
operacion = input("Operación (+ - * /): ")

if operacion == "+":
    print(f"{numero1} + {numero2} = {numero1 + numero2}")
elif operacion == "-":
    print(f"{numero1} - {numero2} = {numero1 - numero2}")
elif operacion == "*":
    print(f"{numero1} * {numero2} = {numero1 * numero2}")
elif operacion == "/":
    if numero2 != 0:
        print(f"{numero1} / {numero2} = {numero1 / numero2}")
    else:
        print("Error: División por cero")
else:
    print("Operación no válida")

