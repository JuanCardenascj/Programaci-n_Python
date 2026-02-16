"""
🧩 Mini reto para subir nivel (este sí desarrolla lógica real)

Haz un programa que:

Pida 3 números

Los muestre ordenados de menor a mayor

Ejemplo:

Entrada:
7
2
5

Salida:
2 - 5 - 7
"""

num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))

# Encontrar menor
menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

# Encontrar mayor
mayor = num1
if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3

# Encontrar el del medio
medio = num1 + num2 + num3 - mayor - menor

print("Ordenados de menor a mayor:")
print(menor, medio, mayor)
