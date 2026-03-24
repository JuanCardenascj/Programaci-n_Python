"""
Ejercicio 3: Mayor de 3 números
Escribe un programa que:

Pida 3 números

Muestre cuál es el mayor
"""

num1 = int(input("Escriba el primer número: "))
num2 = int(input("Escriba el segundo número: "))
num3 = int(input("Escriba el tercer número: "))

mayor = max(num1, num2, num3)
print(f"El número mayor es {mayor}")
