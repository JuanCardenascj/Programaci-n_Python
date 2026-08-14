"""Instrucción:

Pide 3 números al usuario
Calcula el promedio
Muestra el resultado

Explicación:
float() para permitir decimales
"""
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
num3 = float(input("Número 3: "))

promedio = (num1 + num2 + num3) / 3
print(f"El promedio es: {promedio:.2f}")