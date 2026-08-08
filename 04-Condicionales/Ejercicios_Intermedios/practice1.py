"""Instrucción:

Pide dos números al usuario
Pide una operación: "+", "-", "*", "/"
Usa if, elif, else para realizar la operación
Muestra el resultado

Explicación:
Diferentes condicionales para cada operación
"""

a = int(input("Digite un número: "))
b = int(input("Digite un número: "))
operacion = input("Operación (+ - * /): ")

if operacion == "+":
    print(a + b)
elif operacion == "-":
    print(a - b)
elif operacion == "*":
    print(a * b)
elif operacion == "/":
    if b != 0:
        print(a / b)
    else:
        print("Error: División por cero")
else:
    print("Operación no válida")