""""🧩 Ejercicio 2 — Nivel un poco más alto

Haz un programa que:

Pida 3 números

Indique:

cuál es el mayor

cuál es el menor

Ejemplo:

Mayor: 9
Menor: 2
"""

numero1 = int(input("Digite el primer numero: "))
numero2 = int(input("Digite el segundo numero: "))
numero3 = int(input("Digite el tercer numero: "))

mayor = numero1
menor = numero1

if numero2 > mayor:
    mayor = numero2

if numero3 > mayor:
    mayor = numero3

if numero2 < menor:
    menor = numero2

if numero3 < menor:
    menor = numero3

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")